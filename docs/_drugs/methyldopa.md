---
layout: default
title: Methyldopa
parent: Model Prediction Only (L5)
nav_order: 467
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Methyldopa: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertensive disorder / hypertension"
monitor_inn: "Methyldopa"
predicted_indications: ["malignant hypertensive renal disease", "malignant renovascular hypertension", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease", "congenital temporomandibular joint ankylosis", "polydipsia", "atrial flutter (disease)", "cholangiocarcinoma, susceptibility to"]
---

# Methyldopa
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

# Methyldopa: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Methyldopa is an established centrally acting antihypertensive, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but **no clinical trials and no publications** directly support this prediction. It is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder / hypertension (the approved indication text on the Australian licence entry is blank) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 96.63% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, methyldopa is a centrally acting alpha-2 agonist, acting through its metabolite alpha-methylnorepinephrine to reduce sympathetic outflow and lower blood pressure. This background knowledge is not drawn from the compiled data.

The predicted indication, malignant hypertensive renal disease, is essentially a severe, kidney-involving form of the condition methyldopa already treats. A blood pressure-lowering rationale is therefore plausible. However, this is an extension within the same therapeutic area rather than a distinct repurposing signal. The high score likely reflects the closeness of this disease to the hypertension label in the knowledge graph. No trials or literature were found to confirm efficacy in this setting.

**Other predictions in the data (for context):**

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Malignant renovascular hypertension | 96.63% | L5 | Extension of the approved indication; the one linked paper is a diagnostic study, not evidence of efficacy |
| Pulmonary hypertension owing to lung disease and/or hypoxia | 96.30% | L4 | Old rat studies (1976–1977) suggest reduced hypoxia-induced pulmonary vascular changes |
| Pulmonary hypertension with unclear multifactorial mechanism | 96.30% | L5 | Indirect extrapolation only |
| Chronic pulmonary heart disease | 85.03% | L3 | One small randomised study (1988) with inconclusive overall results |

The remaining predictions (Braddock syndrome, polydipsia, atrial flutter and others) have no credible mechanistic link or supporting evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered for malignant hypertensive renal disease.

## Literature Evidence

Currently no related literature available for malignant hypertensive renal disease.

For reference, the most relevant human study found for a related predicted indication (chronic pulmonary heart disease, rank 6) is:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3076795](https://pubmed.ncbi.nlm.nih.gov/3076795/) | 1988 | Clinical study (25 patients randomised to methyldopa 750 mg daily or placebo) | Br J Dis Chest | Effects on pulmonary haemodynamics were inconclusive overall in hypoxic cor pulmonale |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1629R | Hydopa | Tablet 250 mg (as sesquihydrate), oral | Not stated in the data compiled |

## Safety Considerations

Product label warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for authoritative safety information.

**Contraindications suggested by the knowledge graph (not label text):** the TxGNN knowledge graph links methyldopa with the following conditions, which should be verified against the PI:
- Liver disease: liver failure, cirrhosis, hepatic coma and encephalopathy
- Kidney disease and anuria
- Congestive heart failure
- Autoimmune conditions: systemic lupus erythematosus, autoimmune haemolytic anaemia
- Porphyria
- Diabetes mellitus and diabetic ketoacidosis
- Pancreatitis and gallbladder disease
- Gout, hyperparathyroidism and hypercalcaemia
- Anxiety, neurotic and dysthymic disorders
- Potassium deficiency and neonatal jaundice

**Drug Interactions:** 100 interactions are recorded (the 20 listed in the data are mostly Moderate, with a few Minor). Main ones include:
- Moderate: corticosteroids (hydrocortisone, prednisolone, prednisone, dexamethasone, betamethasone, triamcinolone, budesonide), epinephrine, ephedrine, SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), iron, naltrexone, dronabinol and nabilone
- Minor: sulfonylureas (chlorpropamide, glimepiride, tolazamide)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is plausible but is essentially an extension of methyldopa's existing antihypertensive use. It has no trials or literature behind it (L5), and the high score is a model output only. The knowledge graph also flags many potential contraindications, especially in liver and kidney disease, which is relevant to a renal population.

**To proceed, the following is needed:**
- Mechanism of action data (currently missing)
- Product Information warnings and contraindications for the Australian product, which are needed before any safety screening
- Confirmation of the approved indication text for the Australian licence entry
- Clinical or observational evidence of methyldopa use in malignant hypertension with renal involvement, compared with current standard therapies
- A safety assessment in patients with renal impairment, including the interaction burden
- If the pulmonary hypertension direction is of interest, a modern review of the older animal and small human data (PMIDs 144042, 133242, 3076795)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

