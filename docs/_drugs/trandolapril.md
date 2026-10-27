---
layout: default
title: Trandolapril
parent: Model Prediction Only (L5)
nav_order: 745
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Trandolapril: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension (hypertensive disorder). The approved indication text fo…"
monitor_inn: "Trandolapril"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease", "Prinzmetal angina", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies", "intracerebral hemorrhage"]
---

# Trandolapril
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

## Trandolapril: From Hypertension to Malignant Hypertensive Renal Disease
{: .text-alpha }

## One-Sentence Summary

Trandolapril is an angiotensin-converting enzyme (ACE) inhibitor originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but there are currently **no clinical trials** and **no publications** directly supporting this prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder). The approved indication text for the Australian entry is not available, so this is taken from the drug's known indication data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, trandolapril is an ACE inhibitor, its efficacy in hypertension has been established, and mechanistically it may be applicable to malignant hypertensive renal disease.

Malignant hypertensive nephropathy is driven by severe hypertension and activation of the renin-angiotensin-aldosterone system (RAAS). Blocking this pathway with an ACE inhibitor is therefore plausible. The new indication is also closely related to the original one, as it is essentially a severe form of hypertension with kidney involvement. The high TxGNN score is likely driven largely by this proximity to the approved hypertension indication rather than by new evidence.

Other predicted indications were also reviewed. Most have weak or speculative rationale:
- **Malignant renovascular hypertension** (99.92%): RAAS-dependent, so ACE inhibition is plausible, but ACE inhibitors carry a known risk of acute renal function decline in bilateral renal artery stenosis. It is also largely a subtype of the approved indication.
- **Pulmonary hypertension (multifactorial or lung disease/hypoxia related)** (99.92%): Systemic ACE inhibition has no established efficacy in pulmonary vascular disease, and hypotension is a concern. Only indirect animal data exist.
- **Other predictions** (Braddock syndrome, chronic pulmonary heart disease, Prinzmetal angina, COL4A1-related syndromes, intracerebral hemorrhage): no trandolapril-specific human evidence was found.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No publications are available for the top-ranked prediction (malignant hypertensive renal disease). The literature below relates to a lower-ranked prediction, pulmonary hypertension owing to lung disease and/or hypoxia, and is indirect: it is mostly animal or off-target work.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8166049](https://pubmed.ncbi.nlm.nih.gov/8166049/) | 1994 | Review | Am J Cardiol | Molecular basis of regression of cardiac hypertrophy under chronic mechanical overload |
| [7511729](https://pubmed.ncbi.nlm.nih.gov/7511729/) | 1994 | Preclinical (animal) | J Cardiovasc Pharmacol | Trandolapril regressed left ventricular hypertrophy in ageing spontaneously hypertensive rats and affected coronary resistance and ventricular compliance |
| [9218195](https://pubmed.ncbi.nlm.nih.gov/9218195/) | 1997 | Preclinical (animal) | J Hypertens Suppl | Preclinical rationale for combining verapamil and trandolapril in hypertension with cardiovascular or metabolic comorbidity |
| [8909991](https://pubmed.ncbi.nlm.nih.gov/8909991/) | 1996 | Preclinical (animal) | Gen Pharmacol | Trandolapril plus verapamil inhibited hypoxia-induced coronary vasospasm after ischaemia-reperfusion injury in dogs |
| [8989645](https://pubmed.ncbi.nlm.nih.gov/8989645/) | 1996 | Preclinical (animal) | J Card Fail | Long-term trandolapril treatment and augmented vasoconstriction in rats with chronic heart failure |
| [17393952](https://pubmed.ncbi.nlm.nih.gov/17393952/) | 2007 | Case report | J Natl Med Assoc | Single patient with sickle cell anaemia whose chronic pain resolved on trandolapril (indirect and off-target) |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13403K | Gopten | Capsule 2 mg (oral) | Not available in the data compiled for this report |

## Safety Considerations

- **Disease-level cautions from the knowledge graph** (these come from the TxGNN knowledge graph, not from the product label): the graph links trandolapril to contraindication-type relationships with the following conditions:
  - Angioedema (including hereditary, acquired and RAAS-blocker-induced forms)
  - Kidney disease and renal artery obstruction
  - Liver disease and gallbladder disease
  - Neutropenia and agranulocytosis
  - Aortic stenosis and other aortic valve disease
  - Hypotensive disorders
  - Hypertrophic cardiomyopathy
  - Heart failure
  - Ventricular tachycardia and atrioventricular block
  - Connective tissue, bone and cartilage disease
  - Myasthenia gravis and neuromuscular junction disease
- **Drug Interactions**: 100 interactions were recorded. The main ones listed are:
  - **Major**: potassium citrate and potassium bicarbonate (risk of hyperkalaemia)
  - **Moderate**: corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), antidiabetic drugs (metformin, alogliptin, glimepiride, chlorpropamide, and the SGLT2 inhibitors canagliflozin, dapagliflozin and empagliflozin), acetylsalicylic acid, morphine, bupropion, dronabinol, picosulfuric acid and polyethylene glycol with electrolytes

Label-based warnings and contraindications were not available. Please refer to the TGA-approved Product Information (PI) for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported by model score and class-level mechanistic reasoning only (evidence level L5), with no trials or directly relevant publications. The predicted indication is also largely a severe presentation of the already-approved hypertension indication, so it may add little new value.

**To proceed, the following is needed:**
- Product Information (PI) warnings and contraindications for the Australian product (a blocking data gap for safety screening)
- Approved indication text for the ARTG entry
- Detailed mechanism of action data
- Human clinical evidence (trials or observational studies) of trandolapril in malignant hypertensive nephropathy or renovascular hypertension
- A renal safety assessment, given the known risk of renal function decline with ACE inhibitors in renovascular disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

