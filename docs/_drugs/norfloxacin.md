---
layout: default
title: Norfloxacin
parent: Model Prediction Only (L5)
nav_order: 511
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Norfloxacin: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Urinary tract infection, typhoid and paratyphoid fever, salmonellosis…"
monitor_inn: "Norfloxacin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "punctate epithelial keratoconjunctivitis", "premalignant hematological system disease", "diffuse scleroderma", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
---

# Norfloxacin
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

# Norfloxacin: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Norfloxacin is a fluoroquinolone antibiotic originally used for urinary tract infections and other bacterial infections, including gastrointestinal infections such as dysentery and diarrhoeal disease.
The TxGNN model predicts it may be effective for **hyperamylasemia** with a very high score, but **no clinical trials and no publications** support this prediction.
It is a model-generated signal only and should be treated as a likely graph artefact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection, typhoid and paratyphoid fever, salmonellosis, dysentery, diarrhoeal disease, bronchitis, bacterial pneumonia and other bacterial infections (the ARTG entry in the data compiled for this report carries no indication text; these indications come from the knowledge graph) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, norfloxacin is a fluoroquinolone antibacterial that inhibits bacterial DNA gyrase and topoisomerase IV. Its efficacy in urinary tract and gastrointestinal bacterial infections is established.

Hyperamylasemia is a laboratory finding with varied causes (pancreatic, salivary and renal). No antibacterial mechanism plausibly treats it, and no link to norfloxacin's original indications could be identified. The high TxGNN score appears to be a graph-based prediction artefact rather than a biologically meaningful signal.

For context, the other predicted indications reviewed were also weak. Most had no supporting data at all. The only biologically plausible candidate was **septicaemic plague** (rank 10), where *Yersinia pestis* is susceptible to fluoroquinolones. However, support is limited to animal and in vitro studies, and better-established agents exist.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for hyperamylasemia.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 3010K | APO-Norfloxacin | Tablet 400 mg (oral) | Not stated in the data compiled for this report |

---

## Safety Considerations

**Contraindication-related disease associations (knowledge graph, not label text):**
The knowledge graph links norfloxacin to contraindications or cautions in the following groups of conditions:
- **Cardiac rhythm:** long QT syndrome, familial long QT syndrome, torsades de pointes
- **Hepatic and renal:** liver failure, liver disease, cirrhosis, gallbladder disease, kidney disease
- **Neurological and psychiatric:** epilepsy, peripheral neuropathy, peripheral nervous system disease, anxiety disorder, psychotic and schizoaffective disorders, mental disorder
- **Musculoskeletal:** tendinitis, periarthritis, rhabdomyolysis
- **Metabolic and haematological:** diabetes mellitus, diabetic ketoacidosis, potassium deficiency, thrombocytopenia, anaemia

**Drug interactions:** 100 interactions were identified. Examples of **Major** interactions:
- Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone (tendon injury risk)
- Bupropion
- Chlorpropamide (blood glucose disturbance)

Examples of **Moderate** interactions:
- Antidiabetic agents: metformin, pioglitazone, acarbose, alogliptin, canagliflozin, albiglutide
- Calcium-containing products: calcium acetate, calcium phosphate
- Others: famotidine, loperamide, acetylsalicylic acid, balsalazide, bisacodyl, potassium citrate

Please refer to the TGA-approved Product Information (PI) for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical, literature or mechanistic support, and the score appears to be a model artefact. Norfloxacin also carries notable safety concerns (QT prolongation, tendon, neurological and glucose effects) that make speculative use unattractive.

**To proceed, the following is needed:**
- A plausible mechanistic hypothesis linking norfloxacin to hyperamylasemia, which currently does not exist
- Mechanism of action data and the TGA Product Information for APO-Norfloxacin
- If a repurposing direction is still wanted, consider re-evaluating **septicaemic plague**, where the antibacterial rationale is biologically plausible. This would need norfloxacin-specific data compared against better-established agents.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

