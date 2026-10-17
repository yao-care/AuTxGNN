---
layout: default
title: Perindopril
parent: Moderate Evidence (L3-L4)
nav_order: 562
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Perindopril: predicted new indication Malignant hypertensive renal disease (evidence level L4). Approved use: Hypertension (hypertensive disorder). The ARTG entry in the data comp…"
monitor_inn: "Perindopril"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "chronic pulmonary heart disease", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies", "polydipsia", "congenital temporomandibular joint ankylosis"]
---

# Perindopril
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Perindopril: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Perindopril is an ACE inhibitor originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but there are **no registered clinical trials** and only **1 off-target publication** supporting this direction, so the prediction rests mainly on model proximity to the original indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder). The ARTG entry in the data compiled for this report has no indication text, so this comes from the knowledge graph. |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, perindopril is an angiotensin-converting enzyme (ACE) inhibitor. Its efficacy in hypertension is established, and blocking the renin-angiotensin-aldosterone system (RAAS) is mechanistically plausible in hypertensive kidney injury.

Hypertension and malignant hypertensive renal disease sit very close together in the disease network. The very high TxGNN score is probably driven by this proximity to the original indication rather than by independent evidence. The only linked paper (PMID 36382821) covers solitary kidney function after nephrectomy for renal cancer. It does not test perindopril in malignant hypertensive nephropathy.

**Other predictions in the same analysis** (all currently Hold unless noted):

| Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|
| Malignant renovascular hypertension | 99.77% | L5 | RAAS-dependent, so plausible. ACE inhibitors carry a known risk in bilateral renal artery stenosis. No trials or literature. |
| Pulmonary hypertension, unclear multifactorial mechanism | 99.75% | L5 | No established role for systemic RAAS blockade. No evidence. |
| Pulmonary hypertension owing to lung disease/hypoxia | 99.75% | L4 | One rat study (PMID 11282121) with amlodipine plus perindopril. Other retrieved papers largely unrelated. |
| Braddock syndrome | 99.66% | L5 | No evidence or clear rationale. Likely a network artefact. |
| **Chronic pulmonary heart disease** | 97.60% | L3 | **Most promising candidate.** Small, older clinical studies (see below). Status: Research Question. |
| COL4A1-related hematuria-retinal arteriolar tortuosity-contractures syndrome | 67.49% | L5 | Speculative. |
| Brain small vessel disease 1 | 65.65% | L4 | One indirect physiological study in lacunar infarction (PMID 15166388). |
| Polydipsia | 62.48% | L5 | Linked paper is off-target. ACE inhibitors may worsen volume/electrolyte disturbances. |
| Congenital temporomandibular joint ankylosis | 60.31% | L5 | Likely a model artefact. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for malignant hypertensive renal disease (no ClinicalTrials.gov, ICTRP or ANZCTR entries in the data compiled for this report).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36382821](https://pubmed.ncbi.nlm.nih.gov/36382821/) | 2022 | Cohort/Observational | Urologiia | Functional state of a solitary kidney after nephrectomy for renal cancer. Off-target: perindopril in malignant hypertensive nephropathy was not tested. |

For context, the most relevant literature in the wider analysis relates to **chronic pulmonary heart disease** (cor pulmonale):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16279041](https://pubmed.ncbi.nlm.nih.gov/16279041/) | 2005 | Clinical study | Klinicheskaia meditsina | Perindopril for 4 weeks in 42 patients with chronic obstructive bronchitis and secondary pulmonary hypertension; haemodynamics and safety evaluated. |
| [16881230](https://pubmed.ncbi.nlm.nih.gov/16881230/) | 2006 | Clinical study | Problemy tuberkuleza i boleznei legkikh | Course and long-term perindopril therapy in COPD with chronic cor pulmonale. |
| [11076421](https://pubmed.ncbi.nlm.nih.gov/11076421/) | 2000 | Clinical study | Terapevticheskii arkhiv | Efficacy and safety of perindopril in chronic cor pulmonale. |
| [11399702](https://pubmed.ncbi.nlm.nih.gov/11399702/) | 2001 | Clinical study | Chest | ACE inhibitor therapy (perindopril) improved respiratory muscle strength in chronic heart failure. |
| [8328368](https://pubmed.ncbi.nlm.nih.gov/8328368/) | 1993 | Clinical study | Am J Cardiol | Acute and long-term haemodynamic efficacy in 15 patients with severe chronic heart failure. |
| [11282121](https://pubmed.ncbi.nlm.nih.gov/11282121/) | 2001 | Preclinical (animal) | Eur J Pharmacol | Amlodipine with perindopril prevented pulmonary vascular remodelling in hypoxic rats. |

These studies are small, older, partly non-English, and their designs cannot be confirmed from titles alone.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13371R | PERISYL | Tablet containing perindopril erbumine 4 mg (oral) | Not available in the data compiled for this report |

---

## Safety Considerations

**Contraindication-related conditions (from the knowledge graph, not label text):** kidney disease, liver disease, gallbladder disease, angioedema (including acquired, hereditary, ACE-inhibitor-induced and non-histaminic forms), neutropenia, agranulocytosis, hypotensive disorder, connective tissue disease, bone disease, cartilage disease, renal artery obstruction, pyoureter.

**Drug Interactions:** 100 interactions were identified. Major-level examples:
- Potassium citrate (hyperkalaemia risk)
- Potassium bicarbonate (hyperkalaemia risk)

Moderate-level examples include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), antidiabetic agents (metformin, alogliptin, saxagliptin, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide), aspirin, morphine, bupropion and dronabinol.

**Clinical relevance to the predictions:** angioedema is a documented ACE-inhibitor risk (case reports PMIDs 37678466 and 40365500). Renal artery obstruction appears among the knowledge graph contraindications, which matters for the renovascular hypertension prediction. Please refer to the TGA-approved Product Information (PI) for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction for malignant hypertensive renal disease has no clinical trials and only one off-target publication. The high score likely reflects proximity to the original hypertension indication. Perindopril is already marketed in Australia, but evidence for this new indication is at the L4 level.
- Among the other predictions, chronic pulmonary heart disease (L3, Research Question) is the strongest candidate, though its evidence is small, old and uncontrolled.

**To proceed, the following is needed:**
- Mechanism of action data for perindopril (currently unavailable)
- TGA Product Information warnings and contraindications to complete safety screening
- Targeted literature review of ACE inhibitors in malignant hypertensive nephropathy
- For chronic pulmonary heart disease, a well-designed controlled study, with confirmation of the existing studies' designs
- Safety assessment for renal impairment, renal artery stenosis, hyperkalaemia and angioedema risk in the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

