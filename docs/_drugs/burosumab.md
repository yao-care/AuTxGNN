---
layout: default
title: Burosumab
parent: Model Prediction Only (L5)
nav_order: 117
evidence_level: L5
indication_count: 10
---

# Burosumab
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

# Burosumab: From Hereditary Hypophosphatemic Rickets to Renal Osteodystrophy

## One-Sentence Summary

Burosumab is an anti-FGF23 monoclonal antibody, originally used to treat hereditary hypophosphatemic rickets (X-linked hypophosphatemia, XLH).
The TxGNN model predicts it may be effective for **renal osteodystrophy**, but there are **0 registered clinical trials** and only **2 general publications** (both reviews, neither with burosumab clinical data in this condition). The prediction is currently model-based only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hereditary hypophosphatemic rickets (from the knowledge graph; no approved indication text is available for the Australian entry) |
| Predicted New Indication | Renal osteodystrophy |
| TxGNN Prediction Score | 96.93% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, burosumab neutralises FGF23, a hormone that promotes renal phosphate loss and suppresses active vitamin D production. Its efficacy in FGF23-mediated hypophosphatemia (XLH) is established, and FGF23 is also markedly elevated in chronic kidney disease–mineral and bone disorder (renal osteodystrophy), which is the likely basis of the model's prediction.

The link is plausible but not straightforward. In CKD, raised FGF23 is largely a compensatory response to phosphate retention and reduced renal clearance, not the primary driver of disease. Blocking FGF23 could worsen hyperphosphataemia, so the mechanism does not translate directly into expected benefit. The two retrieved publications are a general review of CKD mineral and bone disease and a paediatric bone disorder overview. Neither provides burosumab clinical data in renal osteodystrophy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42438722](https://pubmed.ncbi.nlm.nih.gov/42438722/) | 2026 | Review | Kidney Int Rep | Reviews CKD-mineral and bone disorder, including CKD-associated osteoporosis and its fracture risk, with controversies and gaps. No burosumab data. |
| [37927073](https://pubmed.ncbi.nlm.nih.gov/37927073/) | 2024 | Review | Curr Pediatr Rev | Overview of diagnosis and new treatments for hypophosphatasia and XLH in children. Relevant to the original indication, not to renal osteodystrophy. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13136J | Crysvita | Solution for injection 20 mg in 1 mL | Not available in the compiled data |

## Safety Considerations

- **Contraindications (knowledge graph, not label text):** Kidney failure is listed as a contraindication-linked disease. This is directly relevant to the predicted renal indication.
- **Drug Interactions (9 identified):**
  - **Major:** calcium phosphate, calcifediol, calcitriol, dihydrotachysterol, doxercalciferol, paricalcitol, sodium cellulose phosphate
  - **Moderate:** cinacalcet, etelcalcetide

  Many of these are standard therapies in CKD-mineral and bone disorder, so co-prescribing in the target population would be common and needs careful evaluation.

Please refer to the TGA-approved Product Information (PI) for warnings and formal contraindications, as these were not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5), with no registered trials and no burosumab clinical data in renal osteodystrophy. The mechanism is uncertain and may be unfavourable, because FGF23 blockade could worsen hyperphosphataemia in patients with reduced kidney function. Kidney failure is also flagged as a contraindication-linked condition.

**To proceed, the following is needed:**
- Review of the TGA-approved PI (warnings, contraindications, approved indication text), which was not available
- Detailed mechanism of action data and mechanistic analysis of FGF23 blockade in CKD
- Safety evaluation of phosphate handling, hyperphosphataemia and ectopic calcification risk at low GFR
- Assessment of interactions with vitamin D analogues, calcimimetics and phosphate products commonly used in CKD
- Preclinical or early-phase clinical data in a CKD-MBD population
- Review of the case-level evidence on burosumab in XLH patients with CKD (PMID 38195892), which relates to safe use in XLH rather than treating renal osteodystrophy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

