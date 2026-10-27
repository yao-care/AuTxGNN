---
layout: default
title: Iron Sucrose
parent: Model Prediction Only (L5)
nav_order: 391
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Iron Sucrose: predicted new indication Primary hyperoxaluria (evidence level L5). Approved use: Hyperphosphataemia"
monitor_inn: "Iron sucrose"
predicted_indications: ["primary hyperoxaluria", "pancreatitis", "tumoral calcinosis, hyperphosphatemic, familial", "familial apolipoprotein C-II deficiency", "esophageal varices with bleeding", "esophageal varices without bleeding", "familial hyperphosphatemic tumoral calcinosis/hyperphosphatemic hyperostosis syndrome", "hyperparathyroidism", "hyperlipidemia", "immune-mediated necrotizing myopathy"]
---

# Iron Sucrose
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Iron Sucrose: From Hyperphosphataemia to Primary Hyperoxaluria
{: .text-alpha }

## One-Sentence Summary

Iron sucrose is an intravenous iron preparation, and the knowledge graph used by the model lists hyperphosphataemia as its original indication.
The TxGNN model predicts it may be effective for **primary hyperoxaluria**, but there are **no clinical trials and no publications** supporting this prediction.
The result is a computational prediction only, with no identified mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperphosphataemia (per the knowledge graph; the ARTG entry has no indication text recorded) |
| Predicted New Indication | Primary hyperoxaluria |
| TxGNN Prediction Score | 98.82% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Iron sucrose is an intravenous iron (III) carbohydrate complex used to replace iron. The knowledge graph links it to hyperphosphataemia, and the model appears to have extended that link to other predicted conditions.

For primary hyperoxaluria, no plausible mechanism is evident. The condition is a hepatic enzyme defect (for example in AGXT) that causes oxalate overproduction. Intravenous iron has no known role in correcting this defect. The high score (98.82%) is therefore a computational output that should not be read as clinical support.

Other predictions in the top ten were also reviewed. Most have no supporting evidence. A few raise safety concerns rather than benefit:
- **Pancreatitis (score 97.85%):** Laboratory studies suggest intravenous iron preparations at pharmacologically relevant concentrations may cause pancreatic beta cell death through oxidative stress. This is a possible harm signal, not support for treatment.
- **Hyperparathyroidism (score 96.18%, evidence level L3):** This is the only prediction with some associative literature. The studies are in dialysis and chronic kidney disease populations, where iron sucrose served as a comparator or background therapy. They were not designed to treat hyperparathyroidism. This supports a research question about effects on mineral metabolism, not a treatment indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for primary hyperoxaluria.

---

## Literature Evidence

Currently no related literature available for primary hyperoxaluria.

For context, the literature retrieved for the other top predictions is summarised below. None of it concerns primary hyperoxaluria.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35482713](https://pubmed.ncbi.nlm.nih.gov/35482713/) | 2022 | RCT / clinical study | Nephrol Dial Transplant | Ferric citrate versus intravenous iron sucrose and their effects on mineral, bone and iron markers in a rat model of CKD-MBD (hyperparathyroidism) |
| [34629085](https://pubmed.ncbi.nlm.nih.gov/34629085/) | 2021 | RCT protocol | Trials | Oral polysaccharide iron complex versus iron sucrose in haemodialysis patients (hyperparathyroidism) |
| [32444112](https://pubmed.ncbi.nlm.nih.gov/32444112/) | 2020 | Review | Mol Aspects Med | Overview of intravenous iron therapy and the available formulations (hyperparathyroidism) |
| [28372549](https://pubmed.ncbi.nlm.nih.gov/28372549/) | 2017 | RCT (background and rationale) | BMC Nephrol | Ferumoxytol versus iron sucrose in haemodialysis patients with CKD anaemia; not relevant to pancreatitis |
| [24349622](https://pubmed.ncbi.nlm.nih.gov/24349622/) | 2013 | Preclinical (in vitro) | Am J Transl Res | Intravenous iron preparations caused pancreatic beta cell death at pharmacologically relevant concentrations (pancreatitis; safety signal) |
| [11929146](https://pubmed.ncbi.nlm.nih.gov/11929146/) | 2002 | Clinical study | Perit Dial Int | Low-dose intravenous iron sucrose regimen in peritoneal dialysis patients (hyperparathyroidism) |
| [17543848](https://pubmed.ncbi.nlm.nih.gov/17543848/) | 2007 | Preclinical (animal) | Transl Res | Peritoneal effects of intravenous iron sucrose in rats (pancreatitis) |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10229J | Venofer | Concentrate for solution for infusion, 2.7 g (equivalent to 100 mg iron (III)) in 5 mL | Not recorded in the data compiled for this report |

---

## Safety Considerations

- **Drug Interactions:** 42 interactions were identified in total. The only one rated Major is **dimercaprol**. Moderate interactions include:
  - Tetracycline antibiotics (doxycycline, minocycline, tetracycline) and chloramphenicol
  - Vitamin D analogues (cholecalciferol, calcifediol, ergocalciferol, dihydrotachysterol, doxercalciferol)
  - Bisphosphonates (alendronic acid, risedronic acid, ibandronate)
  - ACE inhibitors (benazepril, captopril, enalapril)
  - Thyroid hormones (levothyroxine, liothyronine, porcine thyroid)
  - Other iron products
- **Potential concerns from the literature:** Iron-induced oxidative stress and pancreatic beta cell toxicity (laboratory data only). Some intravenous iron products are also known to affect FGF23.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for primary hyperoxaluria rests on a model score alone (evidence level L5). There are no trials or publications, and no plausible mechanism. Among the other top predictions, only hyperparathyroidism has associative evidence (L3), and it supports a research question rather than a treatment indication.

**To proceed, the following is needed:**
- Mechanism of action data, which was not available for this report
- Retrieval and review of the TGA Product Information, including the approved indication, warnings and contraindications
- A mechanistic rationale and preclinical data linking iron sucrose to oxalate metabolism before any clinical consideration
- If the hyperparathyroidism signal is pursued, a purpose-designed study of mineral metabolism (PTH, FGF23, phosphate) in CKD, with attention to the pancreatic and oxidative stress safety signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

