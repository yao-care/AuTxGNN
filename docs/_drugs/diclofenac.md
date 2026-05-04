---
layout: default
title: Diclofenac
parent: 僅模型預測 (L5)
nav_order: 152
evidence_level: L5
indication_count: 10
---

# Diclofenac
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

# Diclofenac: From Pain and Inflammatory Conditions to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Diclofenac is a well-established non-steroidal anti-inflammatory drug (NSAID), widely used for pain relief and inflammatory conditions through inhibition of the cyclooxygenase (COX-1/COX-2) enzymes.
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**, a rare hereditary hair loss disorder caused by keratin gene defects.
This prediction is currently at **model-prediction level only**, with **no supporting clinical trials** and **no published literature** identified for this specific indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from TGA registration data (data gap — see note) |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L5 |
| Australia Market Status | No ARTG entries found (likely data collection gap — see note) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

> **⚠️ Note on Australia market status:** This dataset returned zero ARTG entries for Diclofenac. In clinical practice, Diclofenac-containing products (e.g., Voltaren®) are widely available in Australia across multiple formulations. This discrepancy is most likely a data collection gap and must be verified against the current ARTG at [www.tga.gov.au/resources/artg](https://www.tga.gov.au/resources/artg) before any regulatory or clinical decisions are made.

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank was not available at the time of this report. Based on established pharmacology, Diclofenac is a non-selective COX-1/COX-2 inhibitor that reduces the biosynthesis of prostaglandins (particularly PGE₂ and TXA₂), producing anti-inflammatory, analgesic, and antipyretic effects. It is part of the broader NSAID class.

The mechanistic rationale offered by the TxGNN model centres on prostaglandin D₂ (PGD₂), a lipid mediator known to suppress hair follicle cycling and promote hair miniaturisation. The hypothesis is that COX inhibition by Diclofenac could reduce PGD₂ levels and thereby support hair follicle growth. This PGD₂–hair loss axis has been explored in androgenetic alopecia (AGA) research, where elevated scalp PGD₂ has been implicated.

However, hypotrichosis simplex of the scalp is a rare autosomal dominant or recessive condition caused by loss-of-function mutations in keratin genes (notably *KRT85* and *KRT81*), leading to structural failure of the hair shaft — not excess prostaglandin production. There is no established mechanistic connection between COX/PGD₂ inhibition and keratin gene-mediated hair shaft defects. The high TxGNN prediction score most likely reflects graph-embedding proximity to other follicular disorders in the knowledge graph, rather than a direct biological link. This represents model extrapolation and should be treated with caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

No ARTG entries are recorded for Diclofenac in this dataset. As noted above, this is inconsistent with the known clinical availability of Diclofenac in Australia, and is likely a data collection gap. Please verify current registration status directly via the ARTG search portal before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for full safety information, including warnings, contraindications, and drug interactions.

> Drug interaction data and key TGA warnings were not returned in this dataset. Given Diclofenac's broad clinical use, healthcare professionals should be aware of its well-known class-level risks, including gastrointestinal toxicity, cardiovascular risk with long-term use, and renal impairment — though formal citations require PI review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model assigns a high prediction score (99.69%), the evidence supporting Diclofenac for hypotrichosis simplex of the scalp is at the lowest level (L5 — model prediction only). The condition is fundamentally genetic in aetiology (keratin structural protein defects), and no plausible prostaglandin-mediated mechanism has been established in this context. Without any preclinical, observational, or clinical evidence, this candidate cannot be advanced at this stage.

**To proceed, the following is needed:**
- Preclinical or mechanistic studies specifically examining whether COX/PGD₂ inhibition has any demonstrable effect in keratin-deficient hair follicle models
- A systematic literature review to identify any case reports or animal studies linking NSAID use to outcomes in hypotrichosis simplex of the scalp or closely related keratin-mutation disorders
- Retrieval and review of the TGA-approved Product Information (PI) for Diclofenac, including approved indications, contraindications, and key warnings
- Manual verification of ARTG registration status and approved indication text for Australian Diclofenac products
- DrugBank MOA data retrieval to enable a more rigorous mechanistic plausibility assessment

---

> **Also of note — Rank 9 (Juvenile Idiopathic Arthritis, Evidence Level L3):**
> While this report focuses on the top-ranked TxGNN prediction, the highest-evidence candidate in this dataset is **juvenile idiopathic arthritis (JIA)**, supported by **2 clinical trials** and **18 publications** (including a crossover RCT from 1988 and comparative effectiveness studies). The mechanistic rationale is strong — Diclofenac's COX inhibition directly addresses PGE₂-driven synovial inflammation, consistent with the known NSAID class effect in JIA. Diclofenac is also noted in the literature as licensed for juvenile rheumatoid arthritis in some jurisdictions. Healthcare decision-makers may wish to prioritise the JIA candidate (recommendation: **Proceed with Guardrails**) as a more clinically actionable repurposing direction.

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. Report data cut-off: 4 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

