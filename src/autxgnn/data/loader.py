#!/usr/bin/env python3
"""Australia TGA ARTG drug data loader.

This module loads drug data from the Australian Register of Therapeutic Goods (ARTG).
Data must be downloaded manually from https://www.tga.gov.au/resources/artg

Expected file formats:
- data/raw/artg_export.csv  (CSV export from ARTG search)
- data/raw/artg_export.xlsx (Excel export from ARTG search)
"""

from pathlib import Path
from typing import Optional

import pandas as pd


def load_artg_data(filepath: Path) -> pd.DataFrame:
    """Load ARTG export file (CSV or Excel).

    Args:
        filepath: Path to ARTG export file

    Returns:
        DataFrame with ARTG data
    """
    if filepath.suffix.lower() == '.xlsx':
        df = pd.read_excel(filepath)
    else:
        df = pd.read_csv(filepath)

    return df


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize column names for consistency.

    ARTG exports may have varying column names. This function
    normalizes common variations.
    """
    # Common column name mappings
    column_map = {
        'ARTG ID': 'ARTG_ID',
        'ARTG Number': 'ARTG_ID',
        'Product Name': 'Product_Name',
        'Product name': 'Product_Name',
        'Active Ingredient': 'Active_Ingredients',
        'Active Ingredients': 'Active_Ingredients',
        'Active ingredient': 'Active_Ingredients',
        'Dosage Form': 'Dosage_Form',
        'Sponsor Name': 'Sponsor',
        'Sponsor': 'Sponsor',
    }

    df = df.rename(columns=column_map)
    return df


def filter_medicines(df: pd.DataFrame) -> pd.DataFrame:
    """Filter to only include registered medicines.

    ARTG includes various therapeutic goods categories.
    This filters to human medicines only.
    """
    # Check for common status/category columns
    if 'Category' in df.columns:
        # Filter to registered medicines
        df = df[df['Category'].str.contains('Medicine', case=False, na=False)]

    if 'Status' in df.columns:
        # Exclude cancelled/suspended entries
        df = df[~df['Status'].str.contains('Cancel|Suspend', case=False, na=False)]

    return df


def load_pbs_data(filepath: Path) -> pd.DataFrame:
    """Load Australian PBS (Pharmaceutical Benefits Scheme) data.

    Args:
        filepath: Path to PBS items.csv file

    Returns:
        DataFrame with standardized columns
    """
    print(f"Loading PBS data from: {filepath}")
    df = pd.read_csv(filepath)

    # PBS columns: li_item_id, drug_name, brand_name, li_form, etc.
    # Standardize to expected format
    result = pd.DataFrame({
        'ARTG_ID': df['pbs_code'],
        'Product_Name': df['brand_name'],
        'Active_Ingredients': df['drug_name'],
        'ingredients': df['drug_name'],  # For compatibility
        'brand_name': df['brand_name'],
        'dosage_form': df['li_form'],
    })

    # Remove duplicates by Active_Ingredients (drug_name)
    result = result.drop_duplicates(subset=['Active_Ingredients']).reset_index(drop=True)

    print(f"  Total PBS items: {len(result)}")
    print(f"  Unique drugs: {result['Active_Ingredients'].nunique()}")

    return result


def aggregate_ingredients(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate multiple ingredients per product if needed."""
    if 'Active_Ingredients' not in df.columns:
        return df

    # Group by ARTG_ID and aggregate ingredients
    if 'ARTG_ID' in df.columns:
        agg = df.groupby('ARTG_ID').agg({
            'Product_Name': 'first',
            'Active_Ingredients': lambda x: '; '.join(sorted(set(x.dropna().astype(str)))),
            **{col: 'first' for col in df.columns if col not in ['ARTG_ID', 'Product_Name', 'Active_Ingredients']}
        }).reset_index()
        return agg

    return df


def load_fda_drugs(filepath: Optional[Path] = None) -> pd.DataFrame:
    """Load and process TGA ARTG drug data.

    This is the main entry point, compatible with the standard TxGNN interface.

    Args:
        filepath: Optional path to ARTG data file. If not provided,
                  looks for data in standard locations.

    Returns:
        DataFrame with columns:
            - ARTG_ID: ARTG registration number
            - Product_Name: Drug product name
            - Active_Ingredients: Active ingredients (semicolon separated)
    """
    base_dir = Path(__file__).parent.parent.parent.parent
    data_dir = base_dir / "data"
    raw_dir = data_dir / "raw"

    # Try to find ARTG or PBS data file
    if filepath is None:
        possible_files = [
            raw_dir / "tables_as_csv" / "items.csv",  # PBS data
            raw_dir / "artg_export.csv",
            raw_dir / "artg_export.xlsx",
            raw_dir / "artg.csv",
            raw_dir / "artg_medicines.csv",
            data_dir / "artg_export.csv",
        ]

        for f in possible_files:
            if f.exists():
                filepath = f
                break

    if filepath is None or not filepath.exists():
        print("Warning: No ARTG/PBS data found.")
        print("Please download PBS data from https://www.pbs.gov.au/info/browse/download")
        print("Expected file: data/raw/tables_as_csv/items.csv")
        return pd.DataFrame(columns=['ARTG_ID', 'Product_Name', 'Active_Ingredients'])

    # Check if this is PBS data
    if "items.csv" in str(filepath):
        return load_pbs_data(filepath)

    print(f"Loading ARTG data from: {filepath}")

    # Load and process
    df = load_artg_data(filepath)
    df = normalize_columns(df)
    df = filter_medicines(df)
    df = aggregate_ingredients(df)

    # Ensure required columns exist
    required_cols = ['ARTG_ID', 'Product_Name', 'Active_Ingredients']
    for col in required_cols:
        if col not in df.columns:
            df[col] = ""

    print(f"  Total medicines: {len(df)}")
    print(f"  With ingredients: {df['Active_Ingredients'].notna().sum()}")

    return df


def get_unique_ingredients(df: pd.DataFrame) -> list[str]:
    """Extract unique ingredients from loaded data."""
    all_ingredients = []

    col = 'ingredients' if 'ingredients' in df.columns else 'Active_Ingredients'
    for ing_str in df[col].dropna():
        ingredients = [i.strip() for i in str(ing_str).split(';')]
        all_ingredients.extend(ingredients)

    return sorted(set(all_ingredients))


def filter_active_drugs(df: pd.DataFrame) -> pd.DataFrame:
    """Filter active drugs with valid ingredients.

    Args:
        df: Drug DataFrame

    Returns:
        Filtered DataFrame
    """
    col = 'ingredients' if 'ingredients' in df.columns else 'Active_Ingredients'
    active = df[df[col].notna() & (df[col] != '')].copy()
    active = active.reset_index(drop=True)
    return active


def get_drug_summary(df: pd.DataFrame) -> dict:
    """Get drug data summary statistics.

    Args:
        df: Drug DataFrame

    Returns:
        Summary statistics dictionary
    """
    all_ingredients = set()
    ing_col = 'ingredients' if 'ingredients' in df.columns else 'Active_Ingredients'
    name_col = 'brand_name' if 'brand_name' in df.columns else 'Product_Name'

    for ing_str in df[ing_col].dropna():
        ingredients = [i.strip() for i in str(ing_str).split(';')]
        all_ingredients.update(ingredients)

    return {
        "total_count": len(df),
        "with_ingredient": df[ing_col].notna().sum(),
        "unique_products": df[name_col].nunique() if name_col in df.columns else 0,
        "unique_ingredients": len(all_ingredients),
    }


if __name__ == "__main__":
    # Test loading
    df = load_fda_drugs()
    print(f"\nLoaded {len(df)} drugs")

    if len(df) > 0:
        ingredients = get_unique_ingredients(df)
        print(f"Unique ingredients: {len(ingredients)}")
        print(f"\nSample ingredients: {ingredients[:10]}")
