---
layout: default
title: Fingolimod
parent: 僅模型預測 (L5)
nav_order: 278
evidence_level: L5
indication_count: 10
---

# Fingolimod
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

# Fingolimod: From Multiple Sclerosis to Borderline Ovarian Serous Tumor

## One-Sentence Summary

Fingolimod (FTY720) is a sphingosine-1-phosphate (S1P) receptor modulator approved for multiple sclerosis. The TxGNN model's top-ranked prediction for this drug is **Borderline Ovarian Serous Tumor**, but this specific candidate is currently supported by **no clinical trials and no literature** — it is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple Sclerosis (per literature source, not formal regulatory record — see note below) |
| Predicted New Indication | Borderline Ovarian Serous Tumor |
| TxGNN Prediction Score | 94.94% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

*Note: `drug.original_indications` and the regulatory license list are both empty in the evidence pack. "Multiple Sclerosis" is inferred from a literature abstract in the pack (PMID 30388910: "fingolimod (FTY720), approved for the treatment of multiple sclerosis"), not from a formal regulatory filing.*

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is flagged as a data gap in this evidence pack. Based on information embedded in the supporting literature, fingolimod is an S1P receptor functional antagonist and sphingosine kinase 1 (SphK1) inhibitor, used clinically as an immunomodulator in multiple sclerosis via lymphocyte sequestration.

Multiple sclerosis and ovarian tumours are pathophysiologically unrelated (autoimmune/neurological vs. gynaecological oncology), so this prediction represents a substantial domain jump rather than an indication-family extension.

The evidence pack's own rationale for this candidate states the mechanistic extrapolation is **weak**: SphK1/S1P signalling has literature support in *malignant* ovarian cancer (see lower-ranked candidates below), but borderline (low malignant potential) serous tumours are biologically distinct, and no literature or trial evidence specific to this subtype was found. TxGNN's high similarity score here is not corroborated by independent evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Borderline Ovarian Serous Tumor) has a high TxGNN score but zero direct evidence — no clinical trials, no literature — and the pack itself flags the mechanistic link as weak. This does not meet the threshold to advance past model-only prediction (L5).

**To proceed, the following is needed:**
- TFDA/TGA product information (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism-of-action data (DG002)
- Preclinical or clinical evidence specific to borderline (low malignant potential) ovarian serous tumour, not just malignant ovarian cancer generally
- Disease-ontology verification: other candidates in this same evidence pack (e.g. rank 8, "ovarian benign neoplasm") show literature that actually describes *malignant* ovarian cancer cell-line/xenograft studies, suggesting possible label/ontology mismatches worth checking before further triage of this drug's candidate list
- Drug interaction data (DDI query returned "not_found")
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

