---
layout: default
title: Fosaprepitant
parent: 僅模型預測 (L5)
nav_order: 295
evidence_level: L5
indication_count: 10
---

# Fosaprepitant
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

# Fosaprepitant: From Chemotherapy-Induced Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Fosaprepitant is the intravenous prodrug of aprepitant, an NK1/substance P receptor antagonist whose established use — evident from the antiemetic trials in this evidence pack — is prevention of chemotherapy-induced nausea and vomiting (CINV). The TxGNN model's top-ranked prediction is **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, but this pack contains **zero clinical trials and zero publications** supporting that link, and the model's own rationale states there is no known mechanistic connection.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chemotherapy-induced nausea and vomiting (CINV) prevention — inferred from trial evidence in this pack; no formally registered indication text is available |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for fosaprepitant is not available in this evidence pack (flagged as a High-severity data gap). Based on the antiemetic trials captured under other candidate indications in this pack, fosaprepitant/aprepitant acts as an NK1 (substance P) receptor antagonist used alongside 5-HT3 antagonists and dexamethasone to control chemotherapy- and transplant-conditioning-induced nausea and vomiting.

For the top-ranked prediction, NSIAD, the evidence pack's own rationale is explicit that **no mechanistic link exists**: NSIAD is caused by gain-of-function mutations in the AVPR2 (vasopressin V2) receptor gene, which has no known interaction with the NK1/substance P pathway that fosaprepitant targets. This prediction therefore rests entirely on the TxGNN model's statistical score, with no pharmacological rationale, clinical trial, or literature support identified.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

Fosaprepitant is not currently marketed in Australia — there are no ARTG entries and no TGA-approved product information on file in this dataset.

## Safety Considerations

No TGA-approved Product Information is available for this product, as it is not currently registered in Australia, and no warnings, contraindications, or drug interaction data were located in this evidence pack. This is flagged as a **Blocking** data gap (DG001) that must be resolved before any safety evaluation can proceed — safety information should be sourced from an equivalent overseas-approved product information document (e.g. US FDA or EMA) as an interim reference only.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (NSIAD) has no clinical, literature, or mechanistic support — the model's own rationale confirms the biological pathways are unrelated. Combined with the drug's unmarketed status in Australia and a blocking gap in TFDA/TGA safety labelling data, there is no basis to advance this candidate.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data for fosaprepitant (DG002)
- TGA/overseas product information covering warnings, contraindications, and drug interactions (DG001)
- Independent evaluation of lower-ranked candidates with partial evidence — rank 5 (multiple endocrine neoplasia, 3 trials) and rank 7 (retinitis, 1 preclinical mouse study) — noting the rank-5 trials describe general CINV prophylaxis rather than MEN-specific outcomes, and their disease relevance has not yet been graded
- A repeat TxGNN/evidence pull once mechanistic and regulatory data gaps are closed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

