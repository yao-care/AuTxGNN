---
layout: default
title: Felodipine
parent: 僅模型預測 (L5)
nav_order: 267
evidence_level: L5
indication_count: 10
---

# Felodipine
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

# Felodipine: From Hypertension to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia

## One-Sentence Summary

Felodipine is a vascular-selective dihydropyridine calcium channel blocker used to manage hypertension (per literature context in this evidence pack; no formal indication text was returned by regulatory sources). The TxGNN model predicts potential use in **pulmonary hypertension owing to lung disease and/or hypoxia**, but the **20 supporting publications are general hypoxia-biology reviews that do not mention felodipine**, and no clinical trials for this specific indication exist.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (inferred from literature context — e.g. FEVER, HOT trials; not confirmed by TFDA/ARTG regulatory text, which is unavailable) |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for felodipine (Data Gap). Based on the literature contained in this evidence pack, felodipine is consistently described as a second-generation, vascular-selective dihydropyridine calcium channel blocker used for hypertension and vasospastic angina.

The mechanistic link to pulmonary hypertension due to lung disease/hypoxia is not established by the supporting literature — all 20 cited publications are general reviews on hypoxia biology (neurodegeneration, immunology, tumour metabolism, high-altitude physiology) and **none discuss felodipine**. There is a theoretical rationale (systemic vasodilators can lower pulmonary vascular resistance), but there is also a competing concern: as a non-selective systemic vasodilator, felodipine could blunt the protective hypoxic pulmonary vasoconstriction reflex, worsening ventilation-perfusion (V/Q) mismatch in patients with hypoxic lung disease. The direction of the mechanistic effect is therefore uncertain, not clearly favourable.

Given this, the high TxGNN score should be read as a graph-similarity signal rather than evidence of drug-specific efficacy for this indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Review | Ageing Research Reviews | General review of hypoxia's role in brain aging/neurodegeneration; no felodipine data |
| [39841808](https://pubmed.ncbi.nlm.nih.gov/39841808/) | 2025 | Review | Science Translational Medicine | Reviews therapeutic potential of controlled hypoxia in disease models; no felodipine data |
| [28972206](https://pubmed.ncbi.nlm.nih.gov/28972206/) | 2017 | Review | Nature Reviews Immunology | Hypoxia's regulation of immune/inflammatory niches; no felodipine data |
| [37328448](https://pubmed.ncbi.nlm.nih.gov/37328448/) | 2023 | — | Advanced Science | HIF-1α/glycolysis mechanism in gastric cancer hypoxia tolerance; no felodipine data |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | — | Metabolic Brain Disease | Review of cognitive impairment from acute/chronic hypoxia; no felodipine data |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | — | Journal of Cellular Biochemistry | General hypoxia-mediated cell biology review; no felodipine data |
| [8817697](https://pubmed.ncbi.nlm.nih.gov/8817697/) | 1996 | — | Progress in Neurobiology | Hypoxia and brain development review; no felodipine data |
| [31706510](https://pubmed.ncbi.nlm.nih.gov/31706510/) | 2019 | — | Trends in Cancer | Deubiquitinases and hypoxia in cancer; no felodipine data |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | — | Clinical Oncology | Therapeutic modification of tumour hypoxia; no felodipine data |
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | — | Respiratory Care Clinics of North America | Mechanisms of hypoxemia (physiology review); no felodipine data |

**Note:** None of the 20 retrieved publications for this indication reference felodipine directly — all are general hypoxia-biology literature. This is why the evidence level is scored L5 despite the volume of results.

## Australia Market Information

Felodipine has 0 entries on the Australian Register of Therapeutic Goods (ARTG); the drug is not currently marketed in Australia. No product listings, dosage forms, or approved-indication text are available.

## Safety Considerations

Safety data could not be assessed. This is a **blocking data gap**: TFDA/product-label warnings and contraindications were not retrievable (DG001), the mechanism of action is unconfirmed (DG002), and no drug interaction data was found. As felodipine is not registered in Australia, there is no TGA-approved Product Information to reference either. Safety evaluation (S1 stage) cannot proceed until label/warning data is sourced.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there is no felodipine-specific clinical or literature evidence for this indication, the mechanistic direction is uncertain (possible worsening of hypoxic V/Q mismatch), and safety review cannot begin due to a blocking data gap.

**To proceed, the following is needed:**
- TFDA-equivalent product label (warnings/contraindications) to clear the S1 safety gate
- Confirmed mechanism of action data from DrugBank
- Felodipine-specific pharmacology or clinical data in pulmonary hypertension/hypoxic lung disease (note: felodipine has been studied for pulmonary vascular resistance in chronic obstructive lung disease under a different candidate indication in this pack — worth cross-checking before further action)
- Regulatory pathway assessment, since felodipine is not currently marketed in Australia (0 ARTG entries)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

