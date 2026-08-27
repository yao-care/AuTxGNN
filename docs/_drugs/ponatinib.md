---
layout: default
title: Ponatinib
parent: 僅模型預測 (L5)
nav_order: 543
evidence_level: L5
indication_count: 10
---

# Ponatinib
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

# Ponatinib: From an Unspecified Original Indication to Gingival Fibromatosis

## One-Sentence Summary

No original indication data was returned for Ponatinib in this Evidence Pack (original indications and Australian licence records are both empty). The TxGNN model's top-ranked signal for this compound is **Gingival Fibromatosis**, but this is the model's lowest evidence tier (L5), with **zero clinical trials** and **zero publications** identified, and the pack's own mechanistic analysis states there is no known pathological pathway connecting the two.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this Evidence Pack — no original indications or ARTG entries were returned |
| Predicted New Indication | Gingival Fibromatosis (fibromatosis, gingival) |
| TxGNN Prediction Score | 99.04% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Ponatinib is not available in this Evidence Pack (flagged as Data Gap DG002, High severity, remediation: query DrugBank directly). No original indication was returned either, so a pharmacological rationale linking Ponatinib to a prior approved use cannot be established from this dataset alone.

Literature attached to other candidates in this same pack (not this top-ranked prediction) consistently characterise Ponatinib as a third-generation, multi-target tyrosine kinase inhibitor acting on BCR-ABL, FGFR1–4, PDGFRα/β, KIT, RET and SRC-family kinases, used in the treatment of chronic myeloid leukaemia and Philadelphia-chromosome-positive acute lymphoblastic leukaemia (e.g. PMID [37399979](https://pubmed.ncbi.nlm.nih.gov/37399979/), PMID [36927623](https://pubmed.ncbi.nlm.nih.gov/36927623/)). None of this establishes a plausible pathway to gingival fibromatosis, a condition primarily driven by SOS1/CTNNB1-related fibrotic signalling — a pathway not known to involve any of Ponatinib's kinase targets.

The Evidence Pack's own repurposing rationale for this specific candidate states explicitly that there is no known pathogenic pathway overlap, and that the prediction is a pure TxGNN embedding-similarity artefact with no clinical or mechanistic support. This should be treated as a hypothesis-generation signal only, not a genuine repurposing lead. (For reference, the pack's rank-2 candidate, liposarcoma, has a somewhat more plausible FGFR/PDGFR-based mechanistic rationale and in-vitro screening evidence, but remains at evidence level L4/S1.)

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

Ponatinib is not currently registered on the Australian Register of Therapeutic Goods (ARTG) — market status is "Not Marketed" with 0 listed entries. No product/dosage-form information is available.

## Cytotoxicity

Ponatinib is classified here as an antineoplastic agent based on the literature contained in this Evidence Pack, which consistently describes it as an oncology tyrosine kinase inhibitor used in leukaemia (e.g. PMID [37399979](https://pubmed.ncbi.nlm.nih.gov/37399979/)).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-target tyrosine kinase inhibitor: BCR-ABL, FGFR1–4, PDGFRα/β, KIT, RET, SRC family) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions — not detailed in this Evidence Pack |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Literature in this pack references cardiovascular toxicity (arterial occlusive events), pulmonary toxicity, and vascular toxicity for Ponatinib and related TKIs (PMID [30629146](https://pubmed.ncbi.nlm.nih.gov/30629146/), PMID [32527740](https://pubmed.ncbi.nlm.nih.gov/32527740/), PMID [26008987](https://pubmed.ncbi.nlm.nih.gov/26008987/)) — blood pressure, cardiac and pulmonary monitoring, plus FBC and liver/renal function, are indicated pending PI confirmation |
| Handling Protection | Standard cytotoxic/hazardous drug handling precautions should apply pending confirmation via TGA PI |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Gingival Fibromatosis) has no supporting clinical trials or literature, and the Evidence Pack's own analysis states there is no known mechanistic link — this is a model-similarity artefact rather than a repurposing signal. Ponatinib is also unregistered in Australia, and critical safety data (TGA/PI warnings, contraindications, MOA) are marked as data gaps, one of which (TGA labelling) is classified Blocking.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications) — currently a Blocking data gap
- Confirmed mechanism of action from DrugBank or another primary source
- Original indication history, to establish any pharmacological rationale for repurposing
- If this compound is to be pursued further, evaluation should focus on the higher-evidence candidates in this same pack (e.g. liposarcoma, L4/S1) rather than this L5 top-ranked signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

