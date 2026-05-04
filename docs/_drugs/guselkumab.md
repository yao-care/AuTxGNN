---
layout: default
title: Guselkumab
parent: 僅模型預測 (L5)
nav_order: 223
evidence_level: L5
indication_count: 10
---

# Guselkumab
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

The `txgnn-pipeline` skill covers pipeline infrastructure work — the report generation instructions are already defined in the system prompt. Proceeding with the evaluation report now.

---

# Guselkumab: From Plaque Psoriasis to Drug-Induced Osteoporosis

## One-Sentence Summary

Guselkumab (Tremfya®) is a selective anti-IL-23 p19 monoclonal antibody globally approved for plaque psoriasis and psoriatic arthritis in multiple jurisdictions, but currently holds **no TGA registration in Australia** (0 ARTG entries).
The TxGNN model assigns its highest prediction score to **drug-induced osteoporosis** (99.84%), however there are **no supporting clinical trials or published literature** for this application, placing this prediction at evidence level **L5 — model prediction only**.
Of note within the same evidence pack, **psoriasis** (TxGNN rank 3, L1) and **ulcerative colitis** (TxGNN rank 6, L1) carry extensive Phase 3 RCT evidence and are recommended as higher-priority pathways for TGA registration consideration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered with TGA (globally: plaque psoriasis, psoriatic arthritis) |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on published pharmacology, guselkumab is a fully human IgG1λ monoclonal antibody that selectively binds the **p19 subunit of interleukin-23 (IL-23)**, preventing its interaction with the IL-23 receptor complex. This suppresses the IL-23/Th17 inflammatory axis — the central pathogenic driver of plaque psoriasis. Unlike ustekinumab (which blocks the shared p40 subunit of both IL-12 and IL-23), guselkumab's selective p19 blockade preserves IL-12-mediated immune surveillance.

The proposed mechanistic link between IL-23 inhibition and drug-induced osteoporosis is biologically plausible but **highly indirect**. The IL-23/IL-17 axis can modulate the RANKL/OPG balance in the context of chronic inflammatory disease, influencing osteoclast differentiation and periarticular bone resorption — an effect well documented in inflammatory arthritis. Suppressing IL-23 could therefore theoretically attenuate IL-17-driven osteoclastogenesis in inflammatory bone loss.

However, drug-induced osteoporosis — most commonly **glucocorticoid-induced osteoporosis** — operates through fundamentally different primary mechanisms: direct suppression of osteoblast proliferation and differentiation, increased osteoblast and osteocyte apoptosis, reduced intestinal calcium absorption, increased renal calcium excretion, and suppression of adrenal androgens. These pathways are not primarily mediated by IL-23. The high TxGNN prediction score is most likely driven by knowledge graph **topology proximity** (inflammation → RANKL/OPG dysregulation → bone loss node clusters) rather than a direct mechanistic link validated for this specific aetiology. The complete absence of clinical trial and literature evidence confirms this is a **knowledge graph network artefact** rather than a clinically validated repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Guselkumab currently holds no ARTG registration. There are no TGA-approved products at the time of this report (data cutoff: 20 April 2026).

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|------------|-------------|-------------|---------------------|
| — | No ARTG entries found | — | — |

For reference, guselkumab is approved in multiple international jurisdictions — including the **United States** (FDA; Tremfya®), **European Union** (EMA), **Japan**, **Canada**, and **South Korea** — primarily for moderate-to-severe plaque psoriasis and psoriatic arthritis. The FDA additionally approved guselkumab for moderately to severely active ulcerative colitis in **2024**. Australian clinicians requiring access to guselkumab may explore the **TGA Special Access Scheme (SAS Category B)** or the **Authorised Prescriber** pathway pending formal TGA registration.

---

## Safety Considerations

As guselkumab has no current TGA registration, no TGA-approved Product Information (PI) is available for Australia. Please refer to the **FDA-approved US Prescribing Information** or the **EMA Summary of Product Characteristics (SmPC)** as interim safety references. Australian prescribers utilising SAS access pathways should document their safety review of these international PI documents prior to prescribing.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN rank 1 prediction for drug-induced osteoporosis is classified at evidence level L5 (model prediction only), with no supporting clinical trials or published literature. The mechanistic connection between selective IL-23 p19 inhibition and drug-induced — particularly glucocorticoid-induced — osteoporosis is biologically indirect and insufficiently established to justify clinical investigation at this stage.

**To proceed, the following is needed:**
- Preclinical proof-of-concept studies in validated drug-induced osteoporosis models (e.g., murine glucocorticoid-induced osteoporosis) specifically assessing IL-23 pathway contribution
- Mechanistic data confirming IL-23's direct role in drug-induced (as distinct from inflammation-driven) bone loss
- At minimum one Phase 2 signal-finding clinical study before this prediction can be upgraded beyond L5
- Detailed MOA documentation (DrugBank API query recommended to resolve DG002 data gap)

---

> **⚠️ Contextual Note — Higher-Priority Indications in This Evidence Pack**
>
> This report addresses the TxGNN rank 1 prediction per standard format. Two additional predicted indications within the same evidence pack carry substantially stronger evidence and represent more immediate opportunities for Australian patients:
>
> | Rank | Indication | TxGNN Score | Evidence Level | Trials | Publications | Recommendation |
> |------|-----------|------------|---------------|--------|-------------|----------------|
> | 3 | Psoriasis | 99.75% | **L1** | 50+ (multiple completed Phase 3 RCTs) | 20 | **Proceed with Guardrails** |
> | 6 | Ulcerative Colitis | 99.70% | **L1** | 17 (including Phase 2b/3 QUASAR programme) | 20 | **Proceed with Guardrails** |
>
> Both indications reflect guselkumab's current global regulatory approvals (FDA, EMA) and are supported by landmark Phase 3 trials. **Separate detailed evaluation reports for psoriasis and ulcerative colitis are recommended as the primary pathway for TGA registration consideration.** These represent the most clinically actionable findings from this evidence pack for Australian healthcare professionals.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

