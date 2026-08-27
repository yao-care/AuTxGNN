---
layout: default
title: Mometasone
parent: 僅模型預測 (L5)
nav_order: 453
evidence_level: L5
indication_count: 10
---

# Mometasone
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

# Mometasone: From Corticosteroid Therapy to Primary Cutaneous T-Cell Lymphoma

## One-Sentence Summary

> Mometasone is a topical/intranasal corticosteroid; the specific original indication and mechanism-of-action detail are not provided in this evidence pack (both flagged as data gaps).
> The TxGNN model predicts it may be effective for **Primary Cutaneous T-Cell Lymphoma**, but this direction is currently supported only by **0 clinical trials** and **2 incidental case reports** — one of which explicitly reports that mometasone treatment *failed* in a related lymphoproliferative condition.
> Evidence is currently insufficient to support progressing this candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (no `taiwan_regulatory.licenses` or `original_indications` data provided) |
| Predicted New Indication | Primary Cutaneous T-Cell Lymphoma |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L4 (case-level literature only; no controlled or observational cohort data, and available reports do not demonstrate efficacy) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for mometasone in this evidence pack, and no original indication is on record. Based on general pharmacological knowledge, mometasone furoate is a topical/intranasal corticosteroid, and corticosteroids as a class have documented anti-inflammatory and immunomodulatory activity that is sometimes used adjunctively in cutaneous T-cell lymphoma (e.g. as a topical agent for skin-directed symptom control). This provides a plausible, non-specific mechanistic rationale for the TxGNN association.

However, the two literature records retrieved for this pairing do not provide supportive clinical evidence. One report describes mometasone being trialled and **failing** to control a related reactive lymphoproliferative condition (cutaneous pseudolymphoma) before the patient was switched to tapinarof. The second is a general case report of paediatric mycosis fungoides that does not clearly reference mometasone use in the available abstract text. Neither publication was designed to test mometasone's efficacy in primary cutaneous T-cell lymphoma, so the high TxGNN score likely reflects a knowledge-graph association (shared disease category, incidental drug mentions, or corticosteroid drug-class effects) rather than a validated treatment signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40821495](https://pubmed.ncbi.nlm.nih.gov/40821495/) | 2025 | Case report | Proceedings (Baylor University Medical Center) | Describes a case of refractory cutaneous pseudolymphoma (a lymphoproliferative mimic of cutaneous lymphoma) in which mometasone was tried and was **unsuccessful**; the patient subsequently responded to tapinarof. Does not support mometasone efficacy. |
| [25442255](https://pubmed.ncbi.nlm.nih.gov/25442255/) | 2015 | Case report | Journal of Cutaneous Pathology | Case report of childhood CD8+CD56+ mycosis fungoides (a primary cutaneous T-cell lymphoma subtype); the abstract excerpt provided does not mention mometasone treatment or outcome. |

---

## Australia Market Information

No ARTG entries are recorded in the evidence pack (`total_licenses = 0`, `market_status = 未上市 / Not marketed`). No product-level dosage form or approved indication data is available for the Australian market.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. This evidence pack could not retrieve drug interaction data (DDI query: not found) or specific warnings/contraindications for mometasone — notably, PI-level warnings/contraindications are flagged as a **Blocking** data gap (DG001) that must be resolved before any safety assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- There is no clinical trial evidence for mometasone in primary cutaneous T-cell lymphoma, and the only two literature records are non-supportive — one documents treatment failure in a related condition. Combined with a Blocking data gap on TFDA/PI safety information and no confirmed Australian market presence, the evidence does not meet the bar to proceed. For context, the nine other TxGNN candidates for mometasone (ranks 2–10, e.g. Crohn's colitis, myelodysplastic syndrome subtypes, cystic/dermoid lesions, orbital adnexal disease) were also assessed and held — most lack any mechanistic plausibility or supporting data and appear to reflect knowledge-graph noise rather than genuine repurposing signals.

**To proceed, the following is needed:**
- TFDA/TGA-equivalent Product Information (warnings, contraindications) — currently a Blocking gap (DG001)
- Confirmed mechanism of action and original approved indication(s) for mometasone (DG002)
- Full-text review of both cited case reports to confirm whether mometasone was actually used therapeutically for primary cutaneous T-cell lymphoma (rather than as an incidental prior/failed treatment)
- Targeted literature/trial search specifically on corticosteroid use (topical or systemic) in cutaneous T-cell lymphoma, since the current pack's disease-specific search returned only 2 tangential records
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

