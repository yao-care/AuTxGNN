---
layout: default
title: Prazosin
parent: Model Prediction Only (L5)
nav_order: 598
evidence_level: L5
indication_count: 10
---

# Prazosin
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

# Prazosin: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Prazosin is an alpha-1 adrenergic blocker, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease** (score 90.2%), but there are currently **no registered clinical trials** and **no publications** specific to this indication.
The prediction rests on model output alone. Of the ten predictions generated, the one with the most supporting material is malignant renovascular hypertension, and that material is only indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder). The Australian registry data compiled for this report contain no approved indication text. |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 90.2% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Prazosin is generally known as an alpha-1 adrenergic receptor antagonist. It lowers blood pressure by relaxing blood vessels (vasodilation), and its efficacy in hypertension is established.

Malignant hypertensive renal disease is kidney injury driven by severe, accelerated hypertension. Blood pressure lowering is mechanistically relevant, so the prediction is biologically plausible. However, it is largely an extension of prazosin's existing hypertension use rather than a distinct new therapeutic area. No trials or publications were supplied to confirm benefit in this specific population.

### Other Predictions Reviewed

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Malignant renovascular hypertension | 90.2% | L4 | Indirect literature only. Close to the existing hypertension use. |
| 3 | Attention deficit-hyperactivity disorder | 89.7% | L4 | Plausible noradrenergic hypothesis, supported by preclinical papers only. Classed as a research question. |
| 4 | ADHD, inattentive type | 89.7% | L5 | Prediction only. |
| 5 | Faciodigitogenital syndrome | 89.4% | L5 | No mechanistic link identified. |
| 6 | Pulmonary hypertension owing to lung disease and/or hypoxia | 89.3% | L4 | Preclinical and physiological papers only. Vasodilators may worsen ventilation-perfusion matching. |
| 7 | Pulmonary hypertension, unclear multifactorial mechanism | 89.3% | L5 | Prediction only. |
| 8 | Specific developmental disorder | 87.2% | L5 | Supplied papers concern alcohol use disorder, so they do not support this indication. |
| 9 | Braddock syndrome | 86.2% | L5 | No mechanistic link identified. |
| 10 | Chondromyxoid fibroma | 77.3% | L5 | No mechanistic link identified. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for malignant hypertensive renal disease.

For the closely related second-ranked prediction, malignant renovascular hypertension, the following indirect publications were identified:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1055318](https://pubmed.ncbi.nlm.nih.gov/1055318/) | 1975 | Case series | N Z Med J | 24 hypertensive patients treated with prazosin. 20 reached standing BP below 140/90 mmHg at six weeks. Two cases of severe renovascular hypertension responded excellently. Side effects were trivial. |
| [22147655](https://pubmed.ncbi.nlm.nih.gov/22147655/) | 2012 | Review | Horm Metab Res | Factors affecting the aldosterone/renin ratio. A diagnostic paper that does not test prazosin. |
| [22294399](https://pubmed.ncbi.nlm.nih.gov/22294399/) | 2009 | Preclinical | Curr Protoc Pharmacol | Rat models of hypertension (SHR, DOCA-salt, Goldblatt). Prazosin was the most active reference compound in the SHR model. |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13367M | APO-Prazosin | Tablet 5 mg (as hydrochloride) | Not stated in the data compiled for this report |

---

## Safety Considerations

- **Disease contraindication signals (knowledge graph, not label text)**: chronic kidney disease, chronic renal failure, end-stage renal failure, intraoperative floppy iris syndrome, narcolepsy, narcolepsy-cataplexy syndrome, central nervous system disease, Balo concentric sclerosis, X-linked adrenoleukodystrophy. These come from a knowledge graph and should be verified against the label. The renal signals are particularly relevant to a kidney-related indication.
- **Drug Interactions**: 77 interactions were identified. Those shown are mostly Moderate severity:
  - Corticosteroids (hydrocortisone, prednisolone, prednisone, dexamethasone, betamethasone, budesonide, triamcinolone)
  - Opioids (morphine, liposomal morphine, opium)
  - SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin)
  - Cannabinoids (dronabinol, nabilone)
  - Bupropion and acetylsalicylic acid
  - Pantoprazole and metformin are listed with unknown severity.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is supported only by a model score, with no trials or specific literature. It is also essentially an extension of prazosin's established hypertension use. The ADHD prediction is the most distinct hypothesis, but it rests on preclinical data alone and is best treated as a research question.

**To proceed, the following is needed:**
- Mechanism of action data (for example, from DrugBank)
- TGA Product Information, including approved indications, warnings and contraindications
- Targeted literature searching and trial registry review for malignant hypertension with renal involvement
- A renal safety assessment, given the knowledge graph kidney-disease contraindication signals
- For ADHD, dedicated clinical studies before any further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

