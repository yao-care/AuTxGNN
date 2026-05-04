---
layout: default
title: Eplerenone
parent: 僅模型預測 (L5)
nav_order: 196
evidence_level: L5
indication_count: 10
---

# Eplerenone
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

# Eplerenone: From Heart Failure to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia

## One-Sentence Summary

Eplerenone is a selective mineralocorticoid receptor (MR) antagonist that is internationally recognised for reducing cardiovascular mortality in heart failure following acute myocardial infarction and in chronic systolic heart failure (HFrEF) — though it is **not currently registered in Australia**.
The TxGNN model predicts it may be effective for **pulmonary hypertension owing to lung disease and/or hypoxia** with a prediction score of **99.50%**; however, the current evidence base comprises **0 clinical trials** and **20 general hypoxia biology publications** — none of which directly examines Eplerenone in this setting — resulting in an **L5 evidence rating**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Australia; internationally established for heart failure post-MI and chronic HFrEF |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data was not retrievable from DrugBank for this report. Based on established pharmacology, Eplerenone is a **selective mineralocorticoid receptor (MR) antagonist** — it competitively blocks aldosterone binding at the MR in the kidneys, heart, and vasculature, reducing sodium and water retention, attenuating cardiac fibrosis, and preventing the adverse vascular remodelling associated with chronic aldosterone excess. Its selectivity for the MR over androgen and progesterone receptors distinguishes it from the older agent spironolactone.

The mechanistic rationale for Eplerenone in pulmonary hypertension owing to lung disease and/or hypoxia (Group 3 PH) centres on the **hypoxia–aldosterone–MR axis**. Under sustained hypoxic conditions, HIF-1α signalling may upregulate aldosterone synthesis and increase MR expression in pulmonary vascular smooth muscle cells, potentially driving vasoconstriction and adverse vascular remodelling. Blocking the MR could theoretically interrupt this process and attenuate pulmonary vascular resistance — a hypothesis with biological plausibility given the established role of MR antagonism in systemic cardiovascular remodelling demonstrated in the landmark EPHESUS and EMPHASIS-HF trials.

It is critical to recognise, however, that this mechanistic link remains entirely **inferential**. Group 3 PH (lung disease and/or hypoxia-driven) is pathophysiologically distinct from left-sided heart failure — the right ventricular pressure overload and pulmonary vascular biology present different pharmacological challenges. The 20 retrieved publications are all general hypoxia biology reviews and basic science studies with no direct relevance to Eplerenone in this setting. No preclinical or clinical studies have tested this hypothesis.

---

## Clinical Trial Evidence

Currently no clinical trials related to Eplerenone in pulmonary hypertension owing to lung disease and/or hypoxia have been registered.

---

## Literature Evidence

The PubMed search returned 20 publications for this drug-disease pairing; however, **all are general hypoxia biology reviews or basic science studies and none directly examines Eplerenone or mineralocorticoid receptor antagonism in pulmonary hypertension owing to lung disease and/or hypoxia**. The most topically contextual are listed below for background reference only:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39841808](https://pubmed.ncbi.nlm.nih.gov/39841808/) | 2025 | Narrative Review | Science Translational Medicine | Preclinical evidence that chronic continuous hypoxia may benefit mitochondrial and autoimmune disease models; major clinical translation barriers discussed |
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Review | Ageing Research Reviews | Hypoxia drives neurodegeneration in Alzheimer's and Parkinson's disease; moderate altitude hypoxia may paradoxically have protective effects on ageing |
| [28972206](https://pubmed.ncbi.nlm.nih.gov/28972206/) | 2017 | Review | Nature Reviews Immunology | Hypoxia shapes innate and adaptive immunity in physiological niches including bone marrow, lymphoid tissue, and intestinal mucosa |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Review | Clinical Oncology (RCR) | Tumour hypoxia drives resistance to radiotherapy and immunotherapy; strategies for therapeutic modification of hypoxia reviewed |
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Review | Respiratory Care Clinics of North America | Foundational review of hypoxaemia mechanisms including V/Q mismatch, shunt, and hypoventilation — relevant physiological context for Group 3 PH |

> **Important:** None of these publications provides direct evidence supporting Eplerenone for pulmonary hypertension owing to lung disease and/or hypoxia. They represent background hypoxia physiology context only.

---

## Australia Market Information

Eplerenone is **not registered on the Australian Register of Therapeutic Goods (ARTG)**. There are currently no ARTG entries for this drug.

Healthcare professionals wishing to use Eplerenone for an Australian patient would need to access it via the **TGA Special Access Scheme (SAS) Category B** or the **Authorised Prescriber** pathway, noting that this would be entirely off-label and investigational for pulmonary hypertension owing to lung disease.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

> **Note for clinicians:** Although specific safety data was not available in this Evidence Pack for the Australian regulatory context, Eplerenone as a class carries well-recognised risks of **hyperkalaemia** (particularly in patients with renal impairment, diabetes mellitus, or concurrent use of potassium-sparing agents or ACE inhibitors/ARBs), and requires regular monitoring of **renal function and serum electrolytes**. Contraindications in approved international labelling typically include severe renal impairment (eGFR <30 mL/min), significant hyperkalaemia at baseline, and use with strong CYP3A4 inhibitors. In the Group 3 PH population — who frequently have comorbid cor pulmonale, hypoxaemia, and renal congestion — these risks warrant careful individual assessment. Please verify all safety information against the applicable approved Product Information prior to any clinical consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.50%), the evidence for Eplerenone in pulmonary hypertension owing to lung disease and/or hypoxia is rated **L5** — supported only by theoretical mechanistic inference with no dedicated preclinical or clinical studies in this indication. The drug is also **not registered in Australia**, presenting an additional regulatory barrier before any clinical application could be considered.

**To proceed, the following is needed:**
- Dedicated preclinical studies in validated Group 3 PH animal models (e.g., hypoxia-chamber mouse or rat models) using Eplerenone to establish pharmacological proof-of-concept
- Systematic review of MR antagonist class data in pulmonary vascular disease, including spironolactone and the newer agent finerenone, to assess whether a class effect exists
- Full MOA data retrieval from DrugBank to confirm the specific aldosterone/MR pathway mechanisms relevant to pulmonary vasculature
- Safety profile review from applicable international PI (FDA/EMA-approved labelling) given the absence of TGA registration, with specific assessment of risk in right heart failure and renal congestion
- Assessment of TGA Special Access Scheme (SAS) or Authorised Prescriber eligibility requirements for any future clinical investigation in Australia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

