---
layout: default
title: Lidocaine
parent: 僅模型預測 (L5)
nav_order: 396
evidence_level: L5
indication_count: 10
---

# Lidocaine
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

# Lidocaine: From Local Anaesthesia to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Lidocaine is a well-established local anaesthetic (and Class Ib antiarrhythmic) used across a wide range of clinical procedures. The TxGNN model assigns a very high prediction score to **punctate epithelial keratoconjunctivitis** as a new indication, but this candidate currently has **no supporting clinical trials or published literature**, and the underlying mechanism is not plausible on pharmacological grounds.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Local anaesthesia / regional nerve blockade (well-established use; no Australia-specific approved indication text is available in this evidence pack, as the product is not currently marketed here) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in this evidence pack. Based on general pharmacological knowledge, lidocaine is an amide-type local anaesthetic that blocks voltage-gated sodium channels, interrupting nerve conduction and producing loss of sensation in the area of administration. This action underlies its established efficacy in local and regional anaesthesia.

Punctate epithelial keratoconjunctivitis is a corneal/conjunctival surface disorder that is typically viral or inflammatory in origin. Lidocaine's sodium-channel blockade has no known effect on viral replication or ocular surface inflammation — at best it could numb pain or foreign-body sensation, and there is no established treatment mechanism connecting it to this condition's underlying pathology.

In fact, topical anaesthesia on the cornea carries a theoretical safety concern here rather than a therapeutic rationale: corneal anaesthesia can blunt protective reflexes and mask signs of disease progression, potentially delaying recognition of worsening keratitis. The high TxGNN score therefore appears to reflect a strong statistical association in the knowledge graph rather than a biologically grounded repurposing hypothesis, consistent with the complete absence of clinical or literature evidence for this specific drug–disease pair.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a model-only prediction (L5) with no clinical trials, no published literature, and no plausible treatment mechanism identified for lidocaine in punctate epithelial keratoconjunctivitis. There is also a theoretical safety concern (masking of disease progression) rather than a therapeutic signal.

**To proceed, the following is needed:**
- TGA/TFDA-approved Product Information, including warnings and contraindications (currently a blocking data gap for safety assessment)
- Detailed mechanism-of-action data for lidocaine to properly assess mechanistic plausibility
- Any prospective mechanistic, preclinical, or case-level evidence directly linking lidocaine to this specific ocular surface condition
- Australian registration/marketing status confirmation, as the drug is currently not marketed here

*Note: within the same evidence pack, other TxGNN-ranked candidates for lidocaine carry more substantive evidence — notably "conjunctival disorder" (rank 6, evidence level L3), where a genuine signal exists via IV lidocaine's off-label use in SUNCT/SUNA headache syndromes (which present with conjunctival injection and tearing). That candidate may warrant separate evaluation rather than being conflated with this one.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

