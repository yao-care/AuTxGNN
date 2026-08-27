---
layout: default
title: Lercanidipine
parent: 僅模型預測 (L5)
nav_order: 391
evidence_level: L5
indication_count: 10
---

# Lercanidipine
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

# Lercanidipine: From Hypertension to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia

## One-Sentence Summary

Lercanidipine is a third-generation dihydropyridine calcium channel blocker used to treat hypertension. The TxGNN model predicts it may be effective for **pulmonary hypertension owing to lung disease and/or hypoxia** (WHO Group 3 PH), with a high prediction score of **98.79%**, but there are currently **no clinical trials** and **no drug-specific literature** supporting this direction — the 20 associated publications describe general hypoxia biology (HIF-1α signalling, altitude physiology, oncology), none mentioning lercanidipine or any calcium channel blocker in this context.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (lercanidipine is a marketed dihydropyridine calcium channel blocker; no formal TFDA/TGA indication text is available in this evidence pack) |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia |
| TxGNN Prediction Score | 98.79% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data is not available for this drug (data gap DG002). Based on the notes accompanying this evidence pack, lercanidipine is a third-generation, highly lipophilic dihydropyridine L-type calcium channel blocker with long-acting, vascular-smooth-muscle-selective activity — it lowers systemic blood pressure by relaxing peripheral arteriolar smooth muscle.

The predicted new indication, Group 3 pulmonary hypertension (secondary to chronic lung disease and/or hypoxia), is pathophysiologically distinct from systemic hypertension: it involves hypoxic pulmonary vasoconstriction and pulmonary vascular remodelling, not systemic arteriolar tone. There is no known pharmacological rationale for a peripherally-selective dihydropyridine CCB to act on the pulmonary vasculature, and systemic vasodilation could theoretically worsen ventilation-perfusion mismatch in hypoxic lung disease rather than help it.

This prediction score is driven by embedding similarity in the TxGNN knowledge graph rather than by any drug-specific mechanistic or clinical signal — the underlying literature set is about hypoxia biology broadly, not about this drug. This should be treated as a hypothesis-generating signal only, not a mechanistically supported candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

*Note: none of the publications below mention lercanidipine or calcium channel blockers directly — they describe general hypoxia biology and are surfaced only because of TxGNN embedding similarity.*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39841808](https://pubmed.ncbi.nlm.nih.gov/39841808/) | 2025 | Review | Science Translational Medicine | Chronic controlled hypoxia may be therapeutically beneficial in mitochondrial disease, autoimmunity, ischaemia and aging models |
| [28972206](https://pubmed.ncbi.nlm.nih.gov/28972206/) | 2017 | Review | Nature Reviews Immunology | Hypoxia regulates innate and adaptive immunity differently across physiological and pathological niches |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Review | Metabolic Brain Disease | Reviews clinical evidence and molecular mechanisms of cognitive impairment caused by acute/chronic hypoxia |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Review | Journal of Cellular Biochemistry | Overview of hypoxia-mediated control of growth, metabolism and disease including vascular disease and cancer |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Review | Clinical Oncology | Reviews therapeutic modification of tumour hypoxia and its impact on treatment resistance |
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Not classified | Ageing Research Reviews | Discusses hypoxia's role in neurodegeneration vs. neuroprotection in brain aging |
| [37328448](https://pubmed.ncbi.nlm.nih.gov/37328448/) | 2023 | Not classified | Advanced Science | Describes an ac4C/NAT10/HIF-1α feedback loop driving glycolysis in gastric cancer under hypoxia |
| [8817697](https://pubmed.ncbi.nlm.nih.gov/8817697/) | 1996 | Not classified | Progress in Neurobiology | Reviews effects of fetal/perinatal hypoxia on brain development and later cognitive decline |
| [31706510](https://pubmed.ncbi.nlm.nih.gov/31706510/) | 2019 | Not classified | Trends in Cancer | Reviews deubiquitinase regulation of HIF stability in cancer |
| [40963621](https://pubmed.ncbi.nlm.nih.gov/40963621/) | 2025 | Not classified | Frontiers in Immunology | Discusses HIF-1α as a shared mechanistic link between tumour hypoxia and autoimmune disease |

---

## Safety Considerations

Lercanidipine is not currently marketed in Australia (0 ARTG entries), and no TGA-approved Product Information is available. Structured safety data in this evidence pack (key warnings, contraindications, drug-drug interactions) is also missing (data gap DG001, flagged as **Blocking** — TFDA label warnings/contraindications could not be retrieved). Any safety assessment should reference the manufacturer's international product information (e.g. EU/UK SmPC) pending confirmation of an Australian PI, should this product be registered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there is no drug-specific clinical or preclinical evidence, no plausible pharmacological rationale for a peripherally-selective dihydropyridine CCB in hypoxic pulmonary hypertension, and a theoretical risk that systemic vasodilation could worsen ventilation-perfusion mismatch. Combined with a blocking data gap on TFDA/PI safety information, this candidate does not support further progression at this time.

**To proceed, the following is needed:**
- Drug-specific preclinical or clinical evidence for lercanidipine in Group 3 pulmonary hypertension
- Confirmed mechanism-of-action data via DrugBank API (DG002)
- TFDA product label / warnings and contraindications (DG001 — blocking; required before any S1 safety review)
- Pharmacological assessment of pulmonary vascular selectivity vs. systemic vasodilation risk

**Additional note:** among the 10 TxGNN-predicted indications in this evidence pack, **cerebrovascular disorder** (rank 9, score 69.6%) shows materially stronger support — evidence level L3 with a completed Phase 4 cohort study (NCT00741585) and 12 relevant publications including neuroprotection data in stroke models and a retrospective comparison to amlodipine in hypertensive stroke patients. This is likely a more promising candidate for further evaluation than the top-ranked indication above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

