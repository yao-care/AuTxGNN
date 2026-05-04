---
layout: default
title: Citrulline
parent: 僅模型預測 (L5)
nav_order: 113
evidence_level: L5
indication_count: 10
---

# Citrulline
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

# Citrulline: From Nutritional Amino Acid Supplement to Multiple Endocrine Neoplasia

## One-Sentence Summary

Citrulline (L-citrulline) is a naturally occurring amino acid and key intermediate in the urea cycle, widely used as a nutritional supplement to support nitric oxide (NO) production and cardiovascular function — it has no formally registered therapeutic indication in Australia or in our dataset.
The TxGNN model predicts it may have potential in **Multiple Endocrine Neoplasia (MEN)**, with a prediction score of **97.00%**.
However, there are currently **no clinical trials** and **no published literature** directly supporting this indication, making this a model-only prediction with a high risk of false-positive.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No formally registered therapeutic indication; used as a nutritional supplement (urea cycle support, NO precursor) |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 97.00% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed (no TGA registration) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Citrulline was not available in our dataset. Based on known biochemistry, L-citrulline is a non-essential amino acid and a central intermediate in the urea cycle. In the small intestinal enterocytes, citrulline is synthesised from glutamine and then released into circulation, where the kidneys and other tissues convert it to L-arginine. L-arginine in turn serves as the primary substrate for nitric oxide synthase (NOS), making citrulline an indirect but biologically important precursor to nitric oxide (NO) — a key signalling molecule in vascular tone, immune modulation, and cellular metabolism.

Multiple Endocrine Neoplasia (MEN) is a group of hereditary tumour syndromes driven by germline mutations in specific genes: MEN1 (a tumour suppressor affecting the parathyroid, pituitary, and pancreatic islets) and RET (an oncogene driving medullary thyroid carcinoma and phaeochromocytoma in MEN2). These genetic mechanisms operate through cell-cycle regulation and receptor tyrosine kinase signalling pathways — there is no established biological link between Citrulline's urea cycle or NO-generating activity and the suppression or modulation of MEN tumourigenesis.

The high TxGNN score (97.00%) almost certainly reflects indirect knowledge-graph path connections — for example, shared metabolic nodes or co-occurrence patterns — rather than a direct mechanistic relationship. This is a classic false-positive risk scenario in graph-based drug repurposing models. Healthcare professionals should treat this as a computational hypothesis-generating signal only, not as clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Citrulline in Multiple Endocrine Neoplasia.

---

## Literature Evidence

Currently no related literature available for Citrulline in Multiple Endocrine Neoplasia.

---

## Australia Market Information

Citrulline (DrugBank ID: DB00155) currently has **no TGA registration** and is not marketed in Australia as a therapeutic product. No ARTG-listed prescription or OTC medicines containing citrulline as the active ingredient were identified. L-citrulline may be commercially available in Australia as a listed complementary medicine or sports nutrition product under a separate regulatory pathway, but no therapeutic goods registration was found.

---

## Safety Considerations

No drug–drug interaction data was identified in our search. No key warnings or contraindications data were available from our dataset.

Please refer to the TGA-approved Product Information (PI) for safety information, or consult comparable regulatory agency documents (e.g., FDA, EMA) given the absence of Australian PI.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model assigns a notably high prediction score (97.00%), this is entirely unsupported by clinical trials, published literature, or a credible mechanistic link — MEN is driven by specific tumour suppressor and oncogene mutations (MEN1/RET) that have no known connection to Citrulline's metabolic pathways, and the score is most likely a knowledge-graph structural artefact.

**To proceed, the following is needed:**

- Obtain detailed mechanism of action (MOA) data from DrugBank API or primary pharmacology literature
- Commission a formal literature review exploring any possible interaction between nitric oxide signalling and MEN tumour biology (e.g., MEN1 cell lines, RET signalling models)
- Conduct preclinical (in vitro / in vivo) experiments to assess whether citrulline or elevated NO production affects neuroendocrine tumour growth
- Seek expert oncology and endocrinology consultation to assess biological plausibility before further investment
- Evaluate TGA registration pathways and requirements if meaningful preclinical evidence emerges
- Review comparable regulatory safety data (FDA, EMA) in the absence of an Australian PI

> **Disclaimer:** This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before clinical application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

