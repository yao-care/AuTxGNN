---
layout: default
title: Aclidinium
parent: 僅模型預測 (L5)
nav_order: 23
evidence_level: L5
indication_count: 10
---

# Aclidinium
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Aclidinium: From COPD to Open-Angle Glaucoma

## One-Sentence Summary

Aclidinium is a long-acting muscarinic antagonist (LAMA) used as maintenance bronchodilator therapy for Chronic Obstructive Pulmonary Disease (COPD). The TxGNN model predicts it may be effective for **open-angle glaucoma** as its top-ranked new indication, with a prediction score of 89.36%; however, **no supporting clinical trials or publications** exist for this direction, and the underlying pharmacology raises significant safety concerns — anticholinergics are traditionally contraindicated or used with caution in glaucoma patients. All 10 predicted indications in this pack currently lack positive supporting evidence and are classified as **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | COPD (maintenance bronchodilator therapy; inferred from clinical evidence in pack — not TGA-registered in Australia) |
| Predicted New Indication | Open-angle glaucoma |
| TxGNN Prediction Score | 89.36% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Aclidinium is a selective, long-acting muscarinic receptor antagonist (LAMA), delivered as an inhaled dry-powder formulation (Tudorza Pressair / Eklira Genuair). It works by blocking M3 muscarinic acetylcholine receptors in airway smooth muscle, producing sustained bronchodilation. The inhaler is deliberately engineered to have extremely low systemic bioavailability (< 0.1% following inhalation) to minimise off-target effects.

The connection between Aclidinium and open-angle glaucoma is, in fact, mechanistically **counterproductive rather than supportive**. M3 receptors are found in the iris sphincter, ciliary body, and trabecular meshwork of the eye. Anticholinergic agents cause pupillary dilation (mydriasis) and may impair aqueous humour drainage — effects that can raise intraocular pressure. While open-angle glaucoma is pharmacologically distinct from angle-closure glaucoma (the classically listed anticholinergic contraindication), multiple SmPCs for anticholinergic COPD inhalers still include a glaucoma cautionary warning. The TxGNN prediction appears to identify a shared biological pathway (M3 signalling in the eye) but in a direction that contradicts established clinical safety practice.

This pattern is consistent across most of the top 10 predicted indications in this pack. Headache and migraine appear as predictions, yet headache is a documented adverse event of Aclidinium (occurring in ~6% of patients in clinical trials). Similarly, irritable bowel syndrome shows theoretical M3-mediated plausibility for gastrointestinal smooth muscle relaxation, but the inhaled formulation's near-zero systemic absorption makes effective gut delivery impossible without a completely new drug delivery system. In summary, the model has detected pharmacological linkages, but most predictions in this pack represent off-target safety signals rather than viable therapeutic opportunities.

---

## Clinical Trial Evidence

> No clinical trials directly investigating Aclidinium for open-angle glaucoma are currently registered.

The only retrievable clinical trial associated with any of the 10 predicted indications is the following COPD study, in which headache was monitored as an **adverse event** — not a treatment target:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT02165826](https://clinicaltrials.gov/study/NCT02165826) | Phase 3 | Completed | 1,323 | Roflumilast up-titration tolerability/PK study in COPD. Headache was a safety monitoring endpoint (adverse event), not a therapeutic target. This constitutes **negative evidence** for headache disorder as a repurposing indication. |

---

## Literature Evidence

> No publications directly supporting Aclidinium for any of the 10 predicted indications are available.

The only retrievable literature is a COPD long-term safety extension study in which dermatitis was recorded as an adverse event:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [23679347](https://pubmed.ncbi.nlm.nih.gov/23679347/) | 2013 | RCT Extension | COPD | 52-week safety extension of ACCORD COPD I; aclidinium 200 μg or 400 μg BID in COPD patients. Dermatitis was captured as an adverse event, not a treatment outcome. This constitutes **negative evidence** for dermatitis as a repurposing indication. |

---

## Australia Market Information

Aclidinium is **not currently registered on the Australian Register of Therapeutic Goods (ARTG)**. There are no TGA-approved products, no ARTG entries, and no approved indications in Australia. Clinicians seeking the approved Product Information should refer to comparable regulatory filings from the EMA (Eklira Genuair) or US FDA (Tudorza Pressair).

---

## Safety Considerations

Formal TGA Product Information is not available for Australia as the drug is not registered. Based on information available from equivalent overseas regulators and the clinical trial data within this Evidence Pack:

- **Anticholinergic class effects**: Dry mouth, urinary retention, constipation, tachycardia, and blurred vision are characteristic class effects for muscarinic antagonists.
- **Glaucoma**: Anticholinergic agents — including inhaled LAMAs — carry cautionary warnings for patients with glaucoma across multiple international SmPCs. This is directly relevant to the top two TxGNN predictions (open-angle glaucoma, primary hereditary glaucoma), which appear pharmacologically contraindicated rather than supported.
- **Headache**: Reported in approximately 6% of patients in clinical trials (above placebo rate), making headache disorder and migraine predictions pharmacologically implausible as treatment targets.

Please refer to the EMA-approved Summary of Product Characteristics (SmPC) for full safety information pending TGA registration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Aclidinium are currently at evidence level L5 (model prediction only) or supported only by **negative/adverse-event data**. More critically, the top two predictions (open-angle glaucoma and primary hereditary glaucoma) are mechanistically at odds with established anticholinergic pharmacology, and the top neurological predictions (migraine, headache, trigeminal autonomic cephalalgia) are contradicted by clinical trial data showing headache as an adverse event. The IBS prediction, while theoretically plausible via M3 receptor antagonism, is rendered non-viable by the drug's near-zero systemic bioavailability by design.

**To proceed with any of these indications, the following would be required:**

- **Pharmacological safety review**: Formal ophthalmology consultation on the anticholinergic-glaucoma interaction before any glaucoma-related investigation proceeds.
- **Mechanism of action data (MOA)**: Complete DrugBank/literature search to map full receptor binding profile (M1–M5 selectivity, off-target binding).
- **Novel formulation strategy**: For IBS or gastroduodenitis, a new oral or topical ophthalmic delivery system would need to be developed to achieve therapeutic tissue concentrations — this is essentially a new drug development programme, not repurposing.
- **Negative evidence audit**: A systematic review of Aclidinium adverse event data across all Phase 2/3 COPD trials to determine whether predicted indications (headache, dermatitis, glaucoma) cluster as adverse events rather than treatment opportunities.
- **TGA registration pathway assessment**: As Aclidinium is not listed on the ARTG, any Australian clinical development would require a full registration strategy in parallel with any repurposing programme.

---

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All content should be reviewed in conjunction with the full TGA-approved Product Information once available.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

