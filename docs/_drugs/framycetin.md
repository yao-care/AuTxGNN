---
layout: default
title: Framycetin
parent: 僅模型預測 (L5)
nav_order: 297
evidence_level: L5
indication_count: 10
---

# Framycetin
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

# Framycetin: From Antibacterial Use to Sclerosing Cholangitis

## One-Sentence Summary

Framycetin is an aminoglycoside antibacterial (a neomycin B derivative); no specific original indication is recorded in the available regulatory dataset. The TxGNN model's top-ranked prediction is **Sclerosing Cholangitis**, but this candidate is currently supported by **no clinical trials and no published literature**, and the evidence pack's own mechanistic assessment flags it as a likely score artefact rather than a biologically grounded signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the available dataset (drug is an aminoglycoside antibacterial) |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for framycetin is not available in this evidence pack (recorded as a High-severity data gap). Based on information embedded elsewhere in the evidence pack itself, framycetin is an aminoglycoside antibacterial (a neomycin B derivative) that acts by inhibiting bacterial 30S ribosomal protein synthesis, and has historically been used as a topical/otic and ophthalmic antibacterial agent.

Sclerosing cholangitis, however, is primarily an autoimmune and inflammatory biliary disease rather than a condition driven by typical bacterial infection. The evidence pack's own mechanistic assessment concludes there is no clear pathophysiological link between an antibacterial mode of action and this disease, and explicitly flags the prediction as a high TxGNN-score result that is likely mechanistically unreasonable.

Because no clinical trials or literature support this specific drug–disease pairing, and the proposed mechanism does not hold up, this prediction should be treated as a low-confidence lead that would need independent biological plausibility review before any further investment.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Australia Market Information

Framycetin currently has no marketed products in Australia (Market Status: Not marketed; ARTG entries: 0).

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Sclerosing Cholangitis) has an Evidence Level of L5 — a model score alone, with no supporting clinical trials, literature, or plausible mechanism. The evidence pack's own rationale assesses the mechanistic link as unreasonable, so this candidate does not currently justify further investigation.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data for framycetin (currently a High-severity data gap, DG002)
- TGA-approved Product Information / warnings and contraindications (currently a Blocking data gap, DG001)
- Independent biological plausibility review of the antibacterial-to-autoimmune-biliary-disease link before any lab or clinical follow-up
- Consider that other candidates in this evidence pack — e.g. Bronchitis (rank 8, Evidence Level L3, historical literature support, decision stage "Research Question") and Urinary Tract Infection (rank 2, L4, one supporting case-based publication) — show stronger mechanistic and evidentiary grounding and may be more productive avenues for follow-up than the top-ranked prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

