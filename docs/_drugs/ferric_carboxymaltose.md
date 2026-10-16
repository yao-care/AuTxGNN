---
layout: default
title: Ferric Carboxymaltose
parent: Model Prediction Only (L5)
nav_order: 292
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ferric Carboxymaltose: predicted new indication Bronchitis (evidence level L5). Approved use: Not available in the data compiled for this report (the approved indi…"
---

# Ferric Carboxymaltose
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

# Ferric Carboxymaltose: From Iron Deficiency Replacement to Bronchitis

## One-Sentence Summary

Ferric carboxymaltose is an intravenous iron replacement product, marketed in Australia as Ferinject.
The TxGNN model predicts it may be effective for **bronchitis** (the top-ranked prediction), but there are **no registered clinical trials** and **no publications** supporting this direction.
The prediction is a graph-based signal only, so the evidence is very weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the approved indication text for the Australian entry is blank). Intravenous iron replacement is the drug's known use. |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.00% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ferric carboxymaltose is an intravenous iron replacement product. Its role is to correct iron deficiency and iron deficiency anaemia.

No mechanistic link to bronchitis was identified. The drug has no known anti-infective or airway anti-inflammatory activity. The high TxGNN score reflects graph-based proximity only and is not supported by trials or literature.

Other top-ranked predictions were also reviewed. Most have no plausible therapeutic link either:

- **Thrombotic disease (score 98.04%):** The link is indirect and likely adverse rather than therapeutic. Iron deficiency is associated with thrombocytosis and thrombotic tendency, and correcting it may lower platelet counts. That is correction of a deficiency, not treatment of thrombosis.
- **Rheumatoid arthritis (score 96.88%):** Ferric carboxymaltose appears effective and safe for iron deficiency in people with inflammatory rheumatic disease. This supports treating the comorbid deficiency, not modifying the arthritis itself.
- **Others:** Bronchial neoplasm, myositis fibrosa, idiopathic granulomatous myositis, exostosis, laryngotracheitis, tendinitis and heparin cofactor 2 deficiency have no mechanistic link or supporting clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for bronchitis.

For context, literature was retrieved for other predicted indications, none of which supports a repurposing claim:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36282723](https://pubmed.ncbi.nlm.nih.gov/36282723/) | 2023 | Review | Eur Heart J | Iron deficiency is common in cardiovascular disease (thrombotic disease prediction) |
| [41912474](https://pubmed.ncbi.nlm.nih.gov/41912474/) | 2026 | Cohort | Renal Failure | In 41 non-dialysis CKD patients with iron deficiency, IV ferric carboxymaltose was examined for effects on platelet counts and transferrin, with potential thrombogenicity implications |
| [32079699](https://pubmed.ncbi.nlm.nih.gov/32079699/) | 2021 | Preclinical (rat) | Haematologica | Iron deficiency-induced thrombocytosis increased thrombotic tendency; ferric carboxymaltose was used to reverse deficiency |
| [31855154](https://pubmed.ncbi.nlm.nih.gov/31855154/) | 2020 | Cohort | Blood Transfus | IV ferric carboxymaltose was effective and safe for iron deficiency anaemia in inflammatory rheumatic diseases |
| [42785516](https://pubmed.ncbi.nlm.nih.gov/42785516/) | 2026 | Cohort/Review | J Pediatr | Compared effectiveness and safety of IV iron formulations in children with iron deficiency |
| [39304237](https://pubmed.ncbi.nlm.nih.gov/39304237/) | 2024 | RCT | Lancet Glob Health | IV ferric carboxymaltose vs oral ferrous sulphate for anaemia in pregnancy in Nigeria (not relevant to the predicted indications) |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 10104T | Ferinject | Injection 500 mg (iron) in 10 mL | Not available |

## Safety Considerations

- **Drug Interactions** (5 recorded in the interaction database):
  - **Major:** Dimercaprol
  - **Moderate:** Iron, ferrous fumarate, ferrous gluconate, chloramphenicol
- **Bone-related signal:** Ferric carboxymaltose can cause hypophosphatemia and, with prolonged use, osteomalacia.

For warnings and contraindications, please refer to the TGA-approved Product Information (PI).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction of bronchitis has no clinical trials, no literature and no plausible mechanism, so it rests on a graph-based score alone (Evidence Level L5). Even the best-supported alternatives (thrombotic disease, rheumatoid arthritis) reflect correction of iron deficiency rather than treatment of the disease.

**To proceed, the following is needed:**
- Mechanism of action data
- Approved indication text and PI warnings and contraindications for the Australian entry
- A plausible mechanistic or clinical rationale for any predicted indication, followed by registered trials or controlled studies
- Route compatibility and similarity-to-original-indication assessments
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

