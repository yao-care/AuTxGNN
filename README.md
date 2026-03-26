# AuTxGNN - Australia Drug Repurposing Predictions

Drug repurposing predictions for TGA (Therapeutic Goods Administration) approved medications using TxGNN knowledge graph and deep learning methods.

## Overview

This project analyzes medications registered in the Australian Register of Therapeutic Goods (ARTG) to identify potential new therapeutic uses through computational methods.

## Data Sources

- **Drug Data**: [TGA ARTG](https://www.tga.gov.au/resources/artg) - Australian Register of Therapeutic Goods
- **Knowledge Graph**: [TxGNN](https://github.com/mims-harvard/TxGNN)
- **Drug Identifiers**: [DrugBank](https://go.drugbank.com/)

## Installation

```bash
uv sync
```

## Usage

```bash
# Prepare external data
uv run python scripts/prepare_external_data.py

# Run KG prediction
uv run python scripts/run_kg_prediction.py

# Generate FHIR resources
uv run python scripts/generate_fhir_resources.py
```

## Website

https://autxgnn.yao.care

## Disclaimer

This content is for **research purposes only**. Predictions are computational and have not been validated for clinical use. Always consult healthcare professionals before making any medical decisions.

## License

MIT License - See LICENSE for details.
