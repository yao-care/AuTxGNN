---
layout: default
title: Bromocriptine
parent: 僅模型預測 (L5)
nav_order: 106
evidence_level: L5
indication_count: 10
---

# Bromocriptine
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

# Bromocriptine: From Parkinson's Disease to Congenital Disorder of Glycosylation with Defective Fucosylation

## One-Sentence Summary

Bromocriptine is an established dopamine D2/D3 receptor agonist with globally recognised indications including Parkinson's disease, hyperprolactinemia, acromegaly, and type 2 diabetes, though the Australian ARTG data in this Evidence Pack records no currently registered products.
The TxGNN model assigns its highest prediction score to **Congenital Disorder of Glycosylation with Defective Fucosylation** (score: 99.83%), a rare inherited metabolic condition caused by defects in the GDP-fucose biosynthesis pathway.
No clinical trials or published literature support this repurposing direction, and the mechanistic rationale is weak — placing this candidate at **Evidence Level L5 (model prediction only)** with a recommended decision of **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not currently registered on Australian ARTG per data provided; globally established for Parkinson's disease, hyperprolactinemia, and acromegaly |
| Predicted New Indication | Congenital Disorder of Glycosylation with Defective Fucosylation |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed (0 ARTG entries recorded) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Bromocriptine is a well-characterised ergoline derivative with primary agonist activity at dopamine D2 and D3 receptors, and partial agonist activity at serotonin 5-HT2C receptors. Its established pharmacological actions include suppression of pituitary prolactin secretion (via the tuberoinfundibular pathway), enhancement of striatal dopaminergic tone (nigrostriatal pathway), and modulation of circadian metabolic rhythms — the last of which underpins its FDA-approved use in type 2 diabetes as the Cycloset formulation. Detailed mechanism of action data was not available in this Evidence Pack and should be confirmed via DrugBank (DB01200).

Congenital Disorder of Glycosylation with Defective Fucosylation (CDG-IIc, also known as Leukocyte Adhesion Deficiency type II, LAD-II) is caused by mutations in genes encoding enzymes of the GDP-fucose biosynthesis or transport pathway — most commonly *SLC35C1*, which encodes the GDP-fucose transporter. The resulting failure to fucosylate selectin ligands on circulating leukocytes leads to recurrent severe bacterial infections, intellectual disability, short stature, and abnormal blood group antigen expression (Bombay phenotype). This is a pure glycan metabolism disorder with no established intersection with dopaminergic neurotransmission.

The high TxGNN score (99.83%) is most likely an artefact of knowledge graph topology — for example, shared connectivity through rare disease intermediate nodes — rather than a genuine pharmacological signal. There is no plausible mechanistic hypothesis by which D2 receptor agonism could correct GDP-fucose pathway enzyme deficiencies or restore fucosylation of adhesion molecules. At this stage, no research investment is warranted without a primary mechanistic hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Bromocriptine in Congenital Disorder of Glycosylation with Defective Fucosylation.

---

## Literature Evidence

Currently no related literature available for Bromocriptine in Congenital Disorder of Glycosylation with Defective Fucosylation.

---

## Australia Market Information

The Evidence Pack records **no ARTG registrations** for Bromocriptine in Australia. Clinicians should verify this directly against the TGA ARTG, as Bromocriptine products may be listed under brand names (e.g., Parlodel) not captured in this data extraction. Access may be available through the Special Access Scheme (SAS) if no registered product is found.

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|-------------|--------------|-------------|---------------------|
| — | No registered products found in this data extract | — | Please verify directly at tga.gov.au/artg |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for complete safety information. If no TGA PI is available, consult the Australian Medicines Handbook or the regulatory PI from a jurisdiction where Bromocriptine is approved (e.g., FDA, EMA).

> **Note for clinicians:** Regardless of formal PI data, published literature (PMID [8120934](https://pubmed.ncbi.nlm.nih.gov/8120934/)) documents a case of Bromocriptine-induced psychosis consistent with dopamine hypothesis, and its D2 agonist mechanism contraindicates use in patients with active psychotic disorders. This is a clinically important safety consideration independent of the Australian PI status.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN rank-1 prediction for Bromocriptine in CDG with defective fucosylation achieves a high algorithmic score (99.83%) but lacks both mechanistic plausibility and any supporting clinical or preclinical evidence. The dopamine D2/D3 receptor agonist mechanism has no known relationship to the GDP-fucose pathway defects underlying this condition, and the prediction is most likely a knowledge graph artefact.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking D2 receptor signalling to glycosylation biology or fucose metabolism (none currently exists in the published literature)
- Preclinical evidence from CDG animal models or relevant cell-based assays
- Verification of current ARTG registration status directly via the TGA ARTG search portal
- Complete MOA data from DrugBank (DB01200)
- TGA PI or equivalent for contraindications, warnings, and drug interactions

---

> **Note on Broader Prediction Landscape:** Among all 10 TxGNN predictions in this Evidence Pack, **schizophrenia** (Rank 9, TxGNN score: 99.73%) is the indication with the most accumulated evidence — 3 registered clinical trials and 20 publications, classified at Evidence Level **L3**. However, this prediction carries a critical mechanistic safety concern: Bromocriptine's D2 agonism is mechanistically opposed to standard antipsychotic therapy (D2 antagonism), and a published case report (PMID [8120934](https://pubmed.ncbi.nlm.nih.gov/8120934/)) documents Bromocriptine-induced *de novo* psychosis. The schizophrenia evidence is primarily in two narrow contexts — management of antipsychotic-induced hyperprolactinemia, and adjunctive treatment of negative symptoms under neuroleptic cover — neither of which constitutes a clear repurposing opportunity without significant safety evaluation. A separate detailed report for the schizophrenia indication is recommended if this question warrants further investigation.

---

*This report is generated for research reference only. All repurposing candidates require clinical validation before any therapeutic application. Australian clinicians should consult the TGA for current registration and access pathway information. Data cutoff: 10 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

