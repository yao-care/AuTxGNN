---
layout: default
title: Trimethoprim
parent: Model Prediction Only (L5)
nav_order: 704
evidence_level: L5
indication_count: 10
---

# Trimethoprim
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

Using the evidence pack's `predicted_indications[0]` (rank 1, highest TxGNN score) as the primary indication per the template's extraction rule. Note: this candidate has zero supporting evidence — the pack's rank 2 candidate (conjunctivitis) is materially stronger, so I've flagged that at the end.

---

# Trimethoprim: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Trimethoprim is a synthetic dihydrofolate reductase (DHFR) inhibitor historically used against susceptible bacterial infections, and it is not currently registered for sale in Australia.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis** with a very high confidence score, but currently **no clinical trials and no published literature** support this specific prediction.
Given the mechanistic mismatch (this condition is typically viral in origin, while trimethoprim is antibacterial), the evidence does not currently support progressing this candidate.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (trimethoprim is not registered in Australia); internationally used for susceptible bacterial infections |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for trimethoprim is not available in this evidence pack. Based on established pharmacology, trimethoprim is a synthetic antibacterial agent that inhibits bacterial dihydrofolate reductase, blocking folate synthesis and bacterial replication. It is most often used in combination with sulfamethoxazole (systemic infections) or polymyxin B (topical ophthalmic infections), rather than as a standalone agent.

Punctate epithelial keratoconjunctivitis is most commonly caused by viral pathogens (notably adenovirus), rather than bacteria. Trimethoprim's antibacterial mechanism has no established activity against viral agents, so there is no clear mechanistic pathway from the drug's original antibacterial use to this specific predicted indication. A theoretical, indirect rationale could only apply in cases of secondary bacterial co-infection of the ocular surface — this is not supported by any direct evidence in the current pack.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Australia Market Information

Trimethoprim is not currently registered on the Australian Register of Therapeutic Goods (ARTG). No product licences are recorded in this evidence pack.

## Safety Considerations

As trimethoprim is not currently registered in Australia, no local TGA-approved Product Information exists for this drug alone. Safety data (warnings, contraindications, drug interactions) were not available in this evidence pack — please refer to overseas regulatory Product Information for trimethoprim-containing products (e.g., combination products with sulfamethoxazole or polymyxin B) for safety guidance.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or literature evidence supporting trimethoprim for punctate epithelial keratoconjunctivitis, and the drug's antibacterial mechanism does not plausibly address the predominantly viral aetiology of this condition. The prediction score alone is insufficient to justify further evaluation.

**To proceed, the following is needed:**
- TFDA/TGA product label warnings and contraindications (currently a blocking data gap — required before any S1 safety screening)
- Confirmed mechanism of action data via DrugBank or equivalent source
- Any preclinical or *in vitro* evidence of antiviral or immunomodulatory activity relevant to this indication
- Re-evaluation if new clinical or mechanistic evidence emerges

---

**Note on other candidates in this evidence pack:** This drug was evaluated against 10 TxGNN-predicted indications. The rank-1 prediction above is the highest-scoring but has no supporting evidence. By contrast, **conjunctivitis (bacterial)** (rank 2, score 99.17%) is supported by 3 clinical trials — including a completed Phase 4 RCT directly comparing a trimethoprim/polymyxin B ophthalmic solution to moxifloxacin — and multiple RCT-level publications, reaching Evidence Level L2 with a **"Proceed with Guardrails"** recommendation. This is likely the more actionable candidate and may warrant its own dedicated evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

