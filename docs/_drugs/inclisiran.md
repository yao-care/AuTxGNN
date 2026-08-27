---
layout: default
title: Inclisiran
parent: 僅模型預測 (L5)
nav_order: 347
evidence_level: L5
indication_count: 10
---

# Inclisiran
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

# Inclisiran: From Hypercholesterolaemia (Inferred) to Potassium Deficiency Disease

## One-Sentence Summary

Inclisiran is a PCSK9-targeting siRNA whose established pharmacology is LDL-cholesterol lowering, referenced throughout this evidence pack in the context of familial hypercholesterolaemia; the pack's own regulatory data (original indication, MOA) is not populated. The TxGNN model's top-ranked prediction for this drug is **Potassium Deficiency Disease**, but this candidate is supported by **zero clinical trials** and **zero publications** — it is a model score only, and the pack's own mechanistic assessment finds no known biological link between hepatic PCSK9 inhibition and renal/mineralocorticoid-mediated potassium regulation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally documented in this evidence pack (`original_indications` empty, `original_moa` marked as a data gap). Trial titles and rationale text elsewhere in the pack (e.g. heterozygous/homozygous familial hypercholesterolaemia trials, LDL-C clearance mechanism) indicate the drug's established use is lipid-lowering, but this is inferred, not sourced from a regulatory field |
| Predicted New Indication | Potassium Deficiency Disease |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Inclisiran is not available in this evidence pack. Based on information embedded elsewhere in the pack (trial titles and rationale for other candidate indications), Inclisiran is a small interfering RNA (siRNA) that suppresses hepatic PCSK9 synthesis, reducing PCSK9-mediated degradation of LDL receptors and thereby increasing hepatic clearance of LDL-cholesterol.

For the Potassium Deficiency Disease prediction specifically, the pack's own mechanistic review is explicit that there is **no known biological connection**: hepatic PCSK9/LDL-receptor pharmacology has no established relationship to renal potassium handling or mineralocorticoid-axis regulation, which are the pathways that actually govern potassium balance. This candidate reflects a knowledge-graph-derived statistical association only, with no supporting trial or literature evidence and no plausible mechanistic bridge identified.

Given the absence of both mechanistic plausibility and empirical evidence, this prediction should be treated as exploratory model output rather than a credible repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Inclisiran currently has no ARTG entries in this evidence pack (0 licences; market status "Not marketed"). No product/dosage form data is available to tabulate.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Note that as Inclisiran is not currently marketed in Australia per this evidence pack, no TGA-approved PI exists yet — safety review should draw on the manufacturer's overseas-approved PI (e.g. EMA/FDA) pending local registration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Potassium Deficiency Disease prediction has no clinical trial or literature support, and the evidence pack's own mechanistic analysis finds no plausible biological link to Inclisiran's known PCSK9-lowering pharmacology. This is a model-score-only (L5) signal and does not meet the bar for further development work.

**To proceed, the following is needed:**
- Confirmed original indication and MOA data for Inclisiran (currently data gaps; DG002 flagged High severity)
- TGA/ARTG registration status confirmation, since the drug is not currently marketed in Australia
- Any mechanistic or preclinical rationale specifically linking PCSK9/LDL-C pathways to potassium regulation, before this candidate is reconsidered
- TFDA/TGA-equivalent Product Information for safety review (DG001 flagged Blocking severity — currently prevents any safety pre-assessment)

**Note on this evidence pack:** this pack contains 10 candidate indications for Inclisiran, and the top-ranked candidate by TxGNN score (reported above, per the required extraction rule) is not the strongest overall candidate. Rank 8, **Aortic Malformation**, has materially stronger support — Evidence Level L2, two actively recruiting Phase 3 paediatric trials (NCT06597019, NCT06597006) in heterozygous/homozygous familial hypercholesterolaemia populations, and a coherent mechanistic rationale (LDL-C-driven aortic valve/root calcification) — and carries a "Proceed with Guardrails" recommendation in the underlying data. That candidate likely warrants a separate, dedicated evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

