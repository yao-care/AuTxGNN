---
layout: default
title: Voriconazole
parent: Model Prediction Only (L5)
nav_order: 784
evidence_level: L5
indication_count: 10
---

# Voriconazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Voriconazole: From Invasive Fungal Infections to Multidrug-Resistant Tuberculosis

## One-Sentence Summary

Voriconazole is a triazole antifungal originally used for invasive fungal infections such as aspergillosis, candidaemia, oesophageal candidiasis and fusariosis.
The TxGNN model predicts it may be effective for **multidrug-resistant tuberculosis**, but this is a model prediction only, with **0 clinical trials** and **3 publications** that do not show anti-tuberculosis activity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Oesophageal candidiasis, candidaemia, disseminated candidiasis, fusariosis, aspergillosis (from the knowledge graph; no approved indication text is available for the ARTG entry) |
| Predicted New Indication | Multidrug-resistant tuberculosis |
| TxGNN Prediction Score | 98.67% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Voriconazole is known to be a triazole antifungal that inhibits fungal CYP51 (lanosterol 14-alpha-demethylase), blocking ergosterol synthesis in fungal cell membranes.

On current knowledge, a credible mechanistic link to tuberculosis is lacking. *Mycobacterium tuberculosis* has no ergosterol pathway. It does carry CYP51-like enzymes, but azole activity against it is limited and not clinically established. The high TxGNN score appears to reflect network proximity to infectious disease nodes in the knowledge graph, not demonstrated biology.

The three retrieved papers all concern fungal infections:
- A case report of MDR-TB co-existing with aspergilloma and invasive aspergillosis. Voriconazole would treat the fungal co-infection, not the TB.
- An in vitro study of photodynamic inactivation of *Fonsecaea nubica*.
- A genetic diversity study of *Candida krusei* isolates.

None of them shows anti-TB activity.

Other top-ranked predictions (cysticercosis, several tuberculosis variants, and rare congenital malformation and hair disorders) also have no trials, no relevant literature and no plausible mechanism, so they are not developed further here.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18992166](https://pubmed.ncbi.nlm.nih.gov/18992166/) | 2008 | Case report | Cases Journal | MDR-TB co-existing with aspergilloma and invasive aspergillosis in a diabetic woman; the fungal disease is the antifungal target, not the TB |
| [37145297](https://pubmed.ncbi.nlm.nih.gov/37145297/) | 2023 | In vitro | Braz J Microbiol | Methylene blue photodynamic inactivation of multidrug-resistant *Fonsecaea nubica* (chromoblastomycosis); no link to TB |
| [39359062](https://pubmed.ncbi.nlm.nih.gov/39359062/) | 2024 | Microbiological study | Virulence | Biology and genetic diversity of *Candida krusei* isolates from fermented vegetables and clinical samples in China; no link to TB |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10168E | Vfend | Powder for oral suspension 40 mg per mL, 70 mL | Not available in the compiled data |

Only the oral formulation is represented in the compiled data.

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (not label text): long QT syndrome (including familial), torsades de pointes, liver disease, gallbladder disease, potassium deficiency, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disorders, impaired renal function, vision disorders and blindness, cardiomyopathies (including hypertrophic cardiomyopathy), endomyocardial fibrosis and other myocardial disorders.
- **Drug interactions:** 100 interactions were identified in total. Examples from the first 20 reviewed:
  - **Major:** loperamide, triamcinolone, budesonide, chlorpropamide.
  - **Moderate:** famotidine, rabeprazole, omeprazole, hydrocortisone, dexamethasone, betamethasone, pioglitazone, alosetron, aprepitant, bisacodyl, clarithromycin.
  - **Minor:** amphotericin B, cimetidine.
- **TB-specific concern:** voriconazole inhibits CYP3A4, CYP2C19 and CYP2C9, and rifamycins are potent inducers that markedly reduce voriconazole exposure. Co-administration with TB regimens is therefore a practical problem.

Please also refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a graph-based score alone. There are no clinical trials, the retrieved literature does not support anti-TB activity, and there is no credible mechanism, since mycobacteria lack the ergosterol target. Significant interaction problems with rifamycin-based TB regimens add to the concern.

**To proceed, the following is needed:**
- Mechanism of action data and in vitro evidence of voriconazole activity against *M. tuberculosis*, including MDR strains
- Preclinical or early clinical data showing efficacy in TB
- Pharmacokinetic and interaction assessment alongside TB regimens, particularly rifamycins
- TGA-approved PI warnings and contraindications, and the approved indication text for the ARTG entry
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

