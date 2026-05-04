---
layout: default
title: Dostarlimab
parent: 僅模型預測 (L5)
nav_order: 167
evidence_level: L5
indication_count: 10
---

# Dostarlimab
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

# Dostarlimab: From Oncology (dMMR Solid Tumours) to X-Linked Intellectual Disability-Epilepsy Syndrome

## One-Sentence Summary

Dostarlimab (Jemperli®) is a humanised anti-PD-1 monoclonal antibody approved internationally (FDA/EMA) for mismatch repair-deficient (dMMR) endometrial cancer and dMMR solid tumours, but is currently not registered in Australia (0 ARTG entries).
The TxGNN model's top-ranked predicted new indication is **X-linked intellectual disability-epilepsy syndrome**, with a score of **50.00%** (rank #1,228,166 out of all drug-disease pairs) — however, **no clinical trials or supporting literature** exist for this combination, and the mechanistic rationale is extremely weak.
This prediction is rated **L5** (model prediction only) and a **Hold** decision is recommended.

---

## ⚠️ Prediction Quality Alert

All 10 TxGNN-predicted indications in this Evidence Pack share an **identical score of 50.00%** with consecutive rank numbers (#1,228,166–#1,228,175). These are very low-priority predictions in the global TxGNN ranking. None of the 10 candidates have any supporting clinical trials or published literature. The most mechanistically plausible candidate in this batch is **optic pathway glioma** (Rank #10), the only oncological indication in the set, which carries a "Research Question" rating at L4. This context is essential when interpreting the top-ranked prediction below.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Australia; internationally approved for dMMR/MSI-H endometrial cancer and dMMR solid tumours |
| Predicted New Indication | X-linked intellectual disability-epilepsy syndrome |
| TxGNN Prediction Score | 50.00% (rank #1,228,166) |
| Evidence Level | L5 — model prediction only, no clinical or preclinical studies |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank is not available in this Evidence Pack. Based on established pharmacological knowledge, Dostarlimab is a humanised IgG4 monoclonal antibody that blocks the **programmed death-1 (PD-1)** receptor on T cells, preventing its engagement with PD-L1 and PD-L2 ligands. This disinhibits T-cell-mediated cytotoxicity, restoring immune surveillance against tumour cells. It is designed as an immune activator in oncological contexts — not an immunosuppressant.

**X-linked intellectual disability-epilepsy syndrome (XLIE)** is a genetic neurodevelopmental disorder driven by mutations in X-linked genes such as *ARX*, *MECP2*, and *SLC9A6*. The underlying pathology is one of neuronal circuit maldevelopment and excitatory-inhibitory imbalance — not immune dysregulation, tumour neoantigens, or checkpoint-mediated immune exhaustion. While emerging research has explored PD-1 signalling in neuroinflammation, there is no established mechanistic pathway linking PD-1 blockade to correction of the genetic neuronal deficits that characterise XLIE.

Furthermore, large-molecule biologics such as monoclonal antibodies face significant pharmacokinetic limitations at the blood-brain barrier. Dostarlimab's CNS penetration is expected to be negligible, substantially limiting any theoretical effect on central neurological targets. The mechanistic link between PD-1 inhibition and XLIE is, in summary, extremely weak — this prediction most likely reflects a statistical artefact of the knowledge graph traversal rather than a genuine biological hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Dostarlimab is **not currently registered on the Australian Register of Therapeutic Goods (ARTG)** and has no TGA-approved product listings as at 4 April 2026.

Clinicians requiring current regulatory status should consult:
- [ARTG Public Search — Therapeutic Goods Administration](https://www.tga.gov.au/resources/artg)
- GSK Australia for the current regulatory submission status of Jemperli®

For reference, Dostarlimab holds regulatory approval in the following jurisdictions:

| Jurisdiction | Approval Year | Approved Indication |
|---|---|---|
| FDA (USA) | 2021 / expanded 2023 | dMMR recurrent or advanced endometrial cancer; dMMR/MSI-H solid tumours (tumour-agnostic) |
| EMA (EU/UK) | 2021 | dMMR recurrent or primary advanced endometrial cancer |

---

## Cytotoxicity

Dostarlimab is an oncology agent (anti-PD-1 immune checkpoint inhibitor). The following classification applies:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunotherapy — immune checkpoint inhibitor (anti-PD-1 monoclonal antibody); not a conventional cytotoxic agent |
| Myelosuppression Risk | Low–Moderate; not a direct myelosuppressant, but immune-related haematological toxicities (immune thrombocytopenia, haemolytic anaemia) have been reported as irAEs |
| Emetogenicity Classification | Low (monoclonal antibody; minimal direct emetogenic potential; infusion-related reactions possible) |
| Monitoring Items | FBC with differential, LFTs, TFTs (thyroid function), fasting glucose/HbA1c, creatinine/eGFR, morning cortisol, urinalysis; regular clinical review for immune-related adverse events (irAEs) at all organ systems |
| Handling Protection | Standard biological/monoclonal antibody handling precautions apply; cytotoxic chemotherapy handling protocols are not required |

---

## Safety Considerations

No TGA-approved Australian Product Information is available (drug not registered in Australia), and safety data was not retrievable in this Evidence Pack. Please refer to the internationally approved Product Information for full prescribing guidance:

- **FDA Prescribing Information (Jemperli®)**: [DailyMed — NLM](https://dailymed.nlm.nih.gov/)
- **EMA Summary of Product Characteristics**: [European Medicines Agency](https://www.ema.europa.eu/)

Clinicians should be aware that, as a class, anti-PD-1 agents carry serious immune-related adverse event (irAE) risks affecting the gastrointestinal tract, liver, lungs, endocrine glands (thyroid, pituitary, adrenal), kidneys, skin, and nervous system. An irAE of particular relevance to this predicted indication: PD-1 inhibitors have been documented to cause **immune-mediated encephalitis and peripheral/central neurological irAEs**, which would be directly counterproductive in a patient population with an existing neurological disorder.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN prediction for Dostarlimab — X-linked intellectual disability-epilepsy syndrome — has no mechanistic plausibility, no supporting clinical trials, no literature evidence, and a borderline low TxGNN score (50.00% at global rank #1,228,166). Additionally, Dostarlimab's known irAE profile includes neurological toxicities that could directly harm patients with pre-existing epilepsy syndromes, raising a potential safety concern beyond simple lack of efficacy. This prediction does not meet the minimum threshold for further investigation.

**To proceed with any Dostarlimab repurposing research, the following is needed:**

- **Resolve Blocking data gap (DG001)**: Retrieve the full international Product Information (FDA/EMA) to complete safety and contraindication assessment, given the absence of TGA registration data
- **Resolve High-severity data gap (DG002)**: Query DrugBank API for complete MOA data to enable mechanistic linkage analysis
- **Pivot to oncological indications**: Redirect the repurposing analysis to **optic pathway glioma** (Rank #10, L4, "Research Question"), the only oncologically plausible candidate in this batch — where Dostarlimab's anti-PD-1 mechanism and the tumour-agnostic dMMR/MSI-H framework may provide a rational basis for a research hypothesis
- **Commission a targeted TxGNN run**: Request predictions filtered to solid tumour and CNS tumour indication categories, where anti-PD-1 agents have an established mechanistic framework
- **TGA registration pathway assessment**: If future evidence supports Australian use, evaluate the regulatory pathway for TGA registration, noting the existing FDA and EMA precedents as potential reference products

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require prospective clinical validation before clinical application. Australian healthcare professionals should consult TGA-approved product information where available.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

