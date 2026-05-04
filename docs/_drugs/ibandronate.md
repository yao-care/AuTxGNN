---
layout: default
title: Ibandronate
parent: 僅模型預測 (L5)
nav_order: 235
evidence_level: L5
indication_count: 10
---

# Ibandronate
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

# Ibandronate: From Osteoporosis to Duodenal Ulcer

## One-Sentence Summary

Ibandronate is a nitrogen-containing bisphosphonate used internationally for osteoporosis management and prevention of bone complications from malignancy, but is currently not registered with the TGA in Australia.
The TxGNN model's highest-ranked prediction is **Duodenal Ulcer** (score: 97.79%), however this is supported by **no clinical trials** and only **2 publications** — both of which document gastrointestinal *adverse effects* of bisphosphonates rather than any therapeutic benefit.
Critically, existing pharmacological evidence identifies bisphosphonates as a known cause of gastrointestinal mucosal injury, making this top-ranked prediction a likely model artefact rather than a genuine repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Osteoporosis (internationally approved; not currently registered with TGA Australia) |
| Predicted New Indication | Duodenal Ulcer |
| TxGNN Prediction Score | 97.79% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, formal mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, ibandronate belongs to the nitrogen-containing bisphosphonate class and acts as an inhibitor of farnesyl pyrophosphate synthase (FDPS) in the mevalonate pathway. By blocking this enzyme, ibandronate disrupts prenylation of small GTPases in osteoclasts, impairing their function and accelerating apoptosis — thereby reducing bone resorption. This mechanism underpins its established international use in postmenopausal osteoporosis, glucocorticoid-induced osteoporosis, and skeletal complications of bone metastases.

The predicted link to duodenal ulcer is pharmacologically implausible. The relationship between bisphosphonates and the upper gastrointestinal tract is well established — but in the direction of *harm*, not benefit. Oral bisphosphonates are known to cause oesophageal, gastric, and duodenal mucosal irritation and ulceration, which is a primary reason intravenous formulations were developed. The two publications retrieved (see Literature section below) document gastrointestinal events occurring *during* bisphosphonate therapy, not any therapeutic role in treating peptic disease.

The high TxGNN score almost certainly reflects a confounding-by-indication artefact: the model has identified a statistical co-occurrence between bisphosphonate use and gastrointestinal diagnoses in its training data, but this association represents drug-induced harm. Notably, the three duodenum-related predictions at ranks 1, 2, and 3 (duodenal ulcer, duodenogastric reflux, duodenal obstruction — scores 97.8%, 96.9%, 96.4%) form a tightly clustered false-positive group, strongly suggesting anatomical co-location confounding in the knowledge graph. A pipeline-level review to filter this cluster is recommended.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25866298](https://pubmed.ncbi.nlm.nih.gov/25866298/) | 2015 | Retrospective Administrative Cohort | Clinical Therapeutics | Characterises occurrence of GI events — including upper GI conditions — among women initiating oral bisphosphonate therapy. Documents ibandronate as a source of GI harm rather than treatment |
| [27112533](https://pubmed.ncbi.nlm.nih.gov/27112533/) | 2016 | Retrospective Administrative Study | Clinical Therapeutics | Estimates GI event rates in a large managed care population on oral bisphosphonates; finds GI events are a major driver of non-compliance. Reinforces GI tolerability as a class-wide concern |

> **Clinical interpretation note:** Both publications provide evidence *against* ibandronate as a treatment for duodenal ulcer. Neither study was designed to investigate a therapeutic role.

---

## Australia Market Information

Ibandronate is currently **not registered** on the Australian Register of Therapeutic Goods (ARTG). No ARTG entries exist. Any clinical use in Australia would require special access via the TGA Special Access Scheme (SAS) or Authorised Prescriber pathway.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for complete safety information. Note that as a class, oral bisphosphonates carry well-documented upper gastrointestinal risks (oesophageal and gastric/duodenal mucosal injury) that are directly relevant to the top-ranked predicted indication — and represent a contraindication to, rather than a rationale for, use in duodenal ulcer.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN prediction (Duodenal Ulcer, 97.79%) is mechanistically implausible — oral bisphosphonates cause upper gastrointestinal mucosal injury and would be contraindicated in active duodenal ulcer disease. The high prediction score is a model artefact from confounding-by-indication. Across all 10 ranked predictions, 9 are rated L5 evidence with a Hold recommendation, and the one exception (rank 7, Pregnancy-Associated Osteoporosis, L4) carries a major safety barrier due to bisphosphonate teratogenicity and placental transfer (FDA Pregnancy Category D).

**To proceed, the following is needed:**

- **Knowledge graph audit:** Investigate anatomical co-location confounding — the cluster of three duodenal predictions (ranks 1–3) at near-identical high scores warrants a pipeline-level false-positive filter review
- **MOA data gap:** Obtain full mechanism of action data from DrugBank API (data gap DG002) to support any future mechanistic plausibility analysis
- **Regulatory data gap:** Download and parse the TGA Product Information document to obtain Australian-specific warnings and contraindications (data gap DG001)
- **Research question (rank 7 only):** If pursuing pregnancy-associated osteoporosis as a research question, a focused safety review addressing placental transfer, fetal bone accumulation, and postpartum-only timing of intervention should precede any further development steps
- **ARTG pathway clarification:** Since ibandronate has zero ARTG entries, any Australian clinical development pathway would require a full TGA registration or SAS application — this regulatory burden should factor into portfolio prioritisation decisions

---

> ⚠️ **Disclaimer:** This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. All clinical decisions should refer to TGA-approved Product Information and relevant clinical guidelines.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

