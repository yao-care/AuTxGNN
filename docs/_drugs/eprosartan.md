---
layout: default
title: Eprosartan
parent: Model Prediction Only (L5)
nav_order: 262
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Eprosartan: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertension (hypertensive disorder)"
monitor_inn: "Eprosartan"
predicted_indications: ["malignant hypertensive renal disease", "chronic pulmonary heart disease", "obsolete susceptibility to ischemic stroke", "ocular tuberculosis", "congenital temporomandibular joint ankylosis", "obsolete functional visual loss"]
---

# Eprosartan
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

# Eprosartan: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Eprosartan is an angiotensin II type 1 receptor blocker, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**, but there are currently **no clinical trials** and **no publications** supporting this specific prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder); the approved indication text is not recorded for the ARTG entry |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 93.69% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, eprosartan belongs to the angiotensin II type 1 receptor blocker class. Its efficacy in hypertension is established, and renovascular hypertension is driven largely by activation of the renin-angiotensin system, so the link is biologically plausible.

However, this is a hypertensive-spectrum condition very close to the approved indication, so it is closer to a near-label extension than a true repurposing candidate. Angiotensin receptor blockers also carry a known risk in bilateral renal artery stenosis, which is a central concern in renovascular disease. The high TxGNN score (0.937) is a prediction only.

Other predictions in the list include malignant hypertensive renal disease (0.937), pulmonary hypertension with unclear multifactorial mechanism (0.930), pulmonary hypertension owing to lung disease and/or hypoxia (0.930), Braddock syndrome (0.917), and chronic pulmonary heart disease (0.685). Several lower-ranked predictions, such as ocular tuberculosis and congenital temporomandibular joint ankylosis, have no apparent mechanistic basis and look like model artefacts. All are L5 with a Hold recommendation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature is available for the lead prediction. The only publication linked to any predicted indication relates to rank 4 (pulmonary hypertension owing to lung disease and/or hypoxia) and is preclinical:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33942446](https://pubmed.ncbi.nlm.nih.gov/33942446/) | 2021 | Preclinical animal study | J Biochem Mol Toxicol | Eprosartan showed neuroprotective activity in rats with focal cerebral ischaemia-reperfusion injury; not relevant to pulmonary hypertension |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13861M | Teveten | Tablet 600 mg (as mesilate) | Not recorded in the data compiled for this report |

## Safety Considerations

- **Contraindications (from knowledge-graph drug-disease edges, not label text):** pancreatitis, systemic lupus erythematosus (including paediatric), potassium deficiency, diabetes mellitus, diabetic ketoacidosis, hyperuricaemia, hypotensive disorder, hyperparathyroidism, osteitis fibrosa, hepatic coma and encephalopathy, neonatal jaundice, anuria, gout, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disorders, and renal artery obstruction. These come from a model knowledge graph and should be verified against the Product Information. Renal artery obstruction is particularly relevant to the predicted renovascular indication.
- **Drug Interactions:** 84 interactions were identified in total. Major interactions include **potassium citrate** and **potassium bicarbonate** (hyperkalaemia risk). Moderate interactions include corticosteroids (hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide), acetylsalicylic acid, SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), insulins (aspart, degludec, detemir), bupropion, morphine, dronabinol, and bowel-preparation agents (picosulfuric acid, sodium sulfate, polyethylene glycol with electrolytes).

Label warnings and contraindications were not available. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or publications (L5), and the indication is either very close to the existing hypertension use or carries a class-specific risk in renal artery stenosis. The high model score alone is not sufficient to justify moving forward.

**To proceed, the following is needed:**
- Mechanism of action data (currently missing)
- TGA Product Information, including approved indication, warnings and contraindications (a blocking gap for safety screening)
- Clinical or observational evidence for angiotensin receptor blockers in renovascular hypertension, with specific attention to renal artery stenosis risk
- Clarification of whether this prediction offers any benefit beyond the current hypertension indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

