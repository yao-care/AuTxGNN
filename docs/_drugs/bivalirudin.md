---
layout: default
title: Bivalirudin
parent: Moderate Evidence (L3-L4)
nav_order: 99
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Bivalirudin: predicted new indication Primary release disorder of platelets (evidence level L4). Approved use: Not stated in the ARTG data compiled for this report (anticoagulant…"
monitor_inn: "Bivalirudin"
predicted_indications: ["primary release disorder of platelets", "Glanzmann thrombasthenia", "pseudo-von Willebrand disease", "rheumatoid arthritis", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "fetal and neonatal alloimmune thrombocytopenia", "Scott syndrome", "inherited thrombophilia", "platelet-type bleeding disorder"]
---

# Bivalirudin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Bivalirudin: From Anticoagulation in Procedural Settings to Primary Release Disorder of Platelets

## One-Sentence Summary

Bivalirudin is a direct thrombin inhibitor given intravenously as an anticoagulant. The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but the data compiled for this report contain **0 clinical trials** and only **1 case report**, and that report concerns a different condition (heparin-induced thrombocytopenia). The prediction is not supported by clinical data.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the ARTG data compiled for this report (anticoagulant, direct thrombin inhibitor) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 97.84% |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Bivalirudin is known as a direct thrombin inhibitor that acts on the coagulation cascade. It is used as an anticoagulant, including as an alternative where heparin cannot be used, such as in heparin-induced thrombocytopenia (HIT).

The predicted condition is a platelet function disorder, which is a bleeding disorder. It does not involve excess thrombin activity. Bivalirudin's anticoagulant effect would add to bleeding risk rather than correct a platelet release defect. The only linked publication is a case report on spontaneous HIT, where bivalirudin is an established anticoagulant option. That is a different disorder, so the link to this prediction is indirect.

The high TxGNN score is best read as a knowledge-graph association with the platelet pathway, not as evidence of therapeutic benefit.

### Other Predictions Reviewed

The other nine predictions were also assessed. None has clinical trials, and all remain at Hold.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|---|---|---|---|---|
| 2 | Glanzmann thrombasthenia | 97.79% | L5 | A GPIIb/IIIa bleeding disorder. Anticoagulation would worsen bleeding. |
| 3 | Pseudo-von Willebrand disease | 97.34% | L5 | A GPIbα gain-of-function bleeding disorder. No corrective action; counterproductive. |
| 4 | Rheumatoid arthritis | 94.68% | L5 | A theoretical link through thrombin (PAR-1) signalling only. A short-acting IV drug is impractical for a chronic condition. |
| 5 | Bleeding diathesis due to a collagen receptor defect | 93.46% | L5 | Does not compensate for the receptor defect; increases bleeding risk. |
| 6 | Hemorrhagic disorder due to a constitutional thrombocytopenia | 93.42% | L5 | Does not treat a bleeding disorder; may worsen bleeding. |
| 7 | Fetal and neonatal alloimmune thrombocytopenia | 93.12% | L5 | An immune mechanism, managed with IVIG, corticosteroids and platelet transfusion. An anticoagulant would be hazardous. |
| 8 | Scott syndrome | 92.69% | L5 | Reduced thrombin generation is already the problem; further suppression is mechanistically unhelpful. |
| 9 | Inherited thrombophilia | 92.23% | L4 | Biologically plausible as an alternative anticoagulant, but supported only by one case report of HIT with thrombosis. |
| 10 | Platelet-type bleeding disorder | 91.89% | L5 | Would not correct platelet defects; increases bleeding risk. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35763168](https://pubmed.ncbi.nlm.nih.gov/35763168/) | 2022 | Case report | J Thromb Thrombolysis | Limb ischaemia from spontaneous heparin-induced thrombocytopenia as the first presentation of acute COVID-19 infection. This concerns HIT, not a platelet release disorder. |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 8844L | BIVALIRUDIN ARX | Powder for I.V. injection 250 mg (as trifluoroacetate) | Not available in the data compiled for this report |

---

## Safety Considerations

- **Knowledge-graph contraindication signal**: The TxGNN knowledge graph records a contraindication with **intracranial haemorrhage**. This comes from graph data, not from label text.
- **Drug Interactions**: The interaction query returned 100 entries. The first 20 reviewed include several rated **Major**:
  - Anticoagulants and thrombolytics: fondaparinux, alteplase
  - Antiplatelet agent: abciximab (Moderate)
  - Targeted anticancer agents: acalabrutinib, trastuzumab emtansine
  - Other Major entries: deferasirox, ibritumomab tiuxetan, tositumomab (including I-131)
  - Moderate examples: NSAIDs (ketorolac, ibuprofen, topical diclofenac), fluvoxamine, sugammadex, fenfluramine, dexfenfluramine, sibutramine, radioiodine (I-123, I-131)

  Many of these interactions raise bleeding risk, which is directly relevant to any bleeding-disorder indication.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications, as these were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction rests on a model score alone. Bivalirudin is an anticoagulant, and the top predictions are bleeding or platelet disorders in which anticoagulation would be mechanistically unhelpful and potentially harmful. The one linked publication is a case report on a different condition.

**To proceed, the following is needed:**
- A clear mechanistic rationale for how thrombin inhibition could benefit a platelet release disorder, with preclinical support
- Retrieval of the TGA Product Information (approved indications, warnings and contraindications)
- Mechanism of action data from DrugBank
- Clinical expert review of whether the top predictions should be discarded as knowledge-graph artefacts
- If any indication is pursued, a focus on the better-aligned hypothesis (inherited thrombophilia or HIT-related thrombosis) with a systematic literature review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

