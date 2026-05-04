---
layout: default
title: Betamethasone
parent: 僅模型預測 (L5)
nav_order: 84
evidence_level: L5
indication_count: 10
---

# Betamethasone
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

# Betamethasone: From Inflammatory Conditions to Alopecia Areata

## One-Sentence Summary

Betamethasone is a potent synthetic glucocorticoid corticosteroid widely used for its anti-inflammatory and immunosuppressive properties across a broad range of inflammatory and autoimmune conditions.
The TxGNN model predicts it may be effective for **Alopecia Areata**,
with **7 clinical trials** and **20 publications** currently supporting this direction — including multiple completed RCTs and a Cochrane network meta-analysis that directly investigate betamethasone in this condition.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Corticosteroid — anti-inflammatory and immunosuppressive therapy |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| Australia Market Status | No ARTG entries identified in current dataset (TGA verification recommended) |
| Number of ARTG Entries | 0 (dataset query returned no results — likely a data gap) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Betamethasone is a potent synthetic glucocorticoid that acts as a glucocorticoid receptor (GR) agonist, approximately 8.3 times more potent than prednisolone on a milligram-for-milligram basis. Although formal MOA data was not captured in this dataset, betamethasone's mechanism is well-characterised in the literature: it binds intracellular glucocorticoid receptors to downregulate pro-inflammatory cytokines (IFN-γ, IL-2, IL-15), suppress JAK-STAT signalling, and broadly inhibit T-cell-mediated immune responses.

Alopecia Areata (AA) is an autoimmune disease in which autoreactive CD8+ T cells invade hair follicles and disrupt their normal immune privilege — a protected environment in which follicles are hidden from immune surveillance. This "immune privilege collapse" is driven predominantly by the IFN-γ / IL-2 / IL-15 axis and downstream JAK-STAT pathway activation. By suppressing these exact inflammatory mediators, betamethasone can help restore follicular immune privilege and interrupt the autoimmune attack on hair follicles.

Critically, betamethasone is already in routine clinical use for AA via three delivery routes — topical application (e.g., betamethasone valerate 0.1% cream), intralesional injection, and oral mini-pulse regimens — each of which has well-documented clinical rationale and evidence support. This multi-route applicability, combined with the Cochrane-level systematic evidence and multiple completed RCTs, makes the TxGNN model's prediction entirely consistent with current clinical practice.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT06786689](https://clinicaltrials.gov/study/NCT06786689) | Phase 2 | Completed | 60 | Direct head-to-head RCT: betamethasone oral mini-pulse (BOMP) vs weekly azathioprine pulse in moderate-to-severe AA — primary efficacy and safety comparison |
| [NCT03535233](https://clinicaltrials.gov/study/NCT03535233) | Phase 4 | Completed | 40 | Topical potent corticosteroid + 5% minoxidil combination vs intralesional triamcinolone injection in AA — corticosteroid arm directly relevant to betamethasone class |
| [NCT02350023](https://clinicaltrials.gov/study/NCT02350023) | Phase 4 | Completed | 50 | First head-to-head comparison of topical betamethasone vs topical latanoprost in localised AA — efficacy and safety outcomes |
| [NCT05803070](https://clinicaltrials.gov/study/NCT05803070) | N/A | Unknown | 59 | Direct comparison of topical cetirizine 1% vs topical betamethasone valerate 0.1% in localised AA |
| [NCT06087796](https://clinicaltrials.gov/study/NCT06087796) | Phase 1 | Unknown | 60 | Three-arm trial comparing topical pentoxifylline 2% gel and metformin 10% gel against topical betamethasone valerate 0.1% cream in patchy AA — clinical and dermoscopic outcomes |
| [NCT04207931](https://clinicaltrials.gov/study/NCT04207931) | Phase 4 | Recruiting | 250 | Central Centrifugal Cicatricial Alopecia (CCCA) — a distinct scarring alopecia; indirect relevance only |
| [NCT01111981](https://clinicaltrials.gov/study/NCT01111981) | Phase 4 | Unknown | 30 | Clobetasol propionate foam in CCCA — different drug and different alopecia subtype; indirect corticosteroid class reference only |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [40519428](https://pubmed.ncbi.nlm.nih.gov/40519428/) | 2025 | RCT | *Cureus* | Oral betamethasone mini-pulses in moderate-to-severe AA: assessed efficacy, safety, and tolerability — supports intermittent oral regimen as an alternative to long-term systemic steroids |
| [39393548](https://pubmed.ncbi.nlm.nih.gov/39393548/) | 2025 | RCT | *J Am Acad Dermatol* | Microneedle transdermal delivery of compound betamethasone vs intralesional injection in AA — demonstrates a less painful delivery method with comparable efficacy |
| [34400956](https://pubmed.ncbi.nlm.nih.gov/34400956/) | 2021 | RCT | *Iran J Pharm Res* | Randomised, double-blind, placebo-controlled trial of oral betamethasone pulse vs methotrexate vs combination in severe AA (n=36) — combination therapy showed superior outcomes |
| [38623137](https://pubmed.ncbi.nlm.nih.gov/38623137/) | 2024 | Comparative RCT | *Cureus* | Topical betamethasone dipropionate vs topical minoxidil in AA — comparison of hair regrowth outcomes and adverse effects |
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | Network Meta-Analysis | *Cochrane Database Syst Rev* | Cochrane NMA of all treatments for AA — positions corticosteroids (including betamethasone class) within the broader treatment landscape with comparative efficacy data |
| [36257912](https://pubmed.ncbi.nlm.nih.gov/36257912/) | 2022 | Comparative RCT | *Dermatol Ther* | Six-arm blinded RCT (n=108) comparing latanoprost, minoxidil 5%, betamethasone, and their combinations in AA — betamethasone combination arms showed favourable outcomes |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Review | *Dermatol Pract Conceptual* | Review of corticosteroid pulse therapy in AA: efficacy, relapse rates, adverse effects, and prognostic factors — identifies betamethasone oral mini-pulse as a key regimen |
| [32594786](https://pubmed.ncbi.nlm.nih.gov/32594786/) | 2022 | RCT | *J Dermatol Treat* | Within-patient RCT directly comparing intralesional betamethasone vs triamcinolone acetonide in localised AA — addresses evidence gap for betamethasone intralesional route specifically |
| [36114868](https://pubmed.ncbi.nlm.nih.gov/36114868/) | 2023 | Comparative Study | *Arch Dermatol Res* | Fractional CO2 laser alone vs in combination with betamethasone valerate in AA — clinical and dermoscopic evaluation demonstrating additive benefit |
| [36575890](https://pubmed.ncbi.nlm.nih.gov/36575890/) | 2023 | Comparative Study | *J Cosmet Dermatol* | Topical tacrolimus/calcipotriol mixed with betamethasone dipropionate vs topical clobetasol 0.05% in AA — trichoscopic and clinical outcome comparison |

---

## Australia Market Information

No ARTG entries for betamethasone were identified in the current dataset query. This is considered a **data gap** rather than a genuine absence from the Australian market. Betamethasone is a well-established generic corticosteroid that is widely available in Australia across multiple formulations (topical creams, ointments, lotions, and systemic preparations) under various brand names.

**Action required:** Verify current ARTG registration status directly via the TGA ARTG search portal:
🔗 [https://www.tga.gov.au/resources/artg](https://www.tga.gov.au/resources/artg)

Common betamethasone formulations available in Australia include betamethasone valerate (e.g., Celestone, Betnovate) and betamethasone dipropionate, which are directly relevant to the topical treatment pathway for alopecia areata.

---

## Safety Considerations

Safety data including key warnings, contraindications, and drug-drug interactions was not available in this dataset. Please refer to the **TGA-approved Product Information (PI)** for complete safety information for the specific betamethasone formulation being considered.

As a class, potent corticosteroids carry the following well-recognised considerations relevant to alopecia areata treatment contexts:

- **Systemic use (oral mini-pulse):** HPA axis suppression, risk of adrenal insufficiency on abrupt cessation, blood glucose elevation (caution in patients with diabetes), fluid retention, and mood disturbance
- **Intralesional use:** Local skin atrophy, hypopigmentation at injection sites, and pain
- **Topical use:** Skin atrophy, telangiectasia, and tachyphylaxis with prolonged use — particularly under occlusion or in sensitive areas (face, flexures)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for betamethasone in alopecia areata is substantial — multiple completed RCTs directly study oral mini-pulse, intralesional, and topical betamethasone formulations in AA, supported by a Cochrane network meta-analysis. This represents one of the better-evidenced drug repurposing opportunities in this dataset, and betamethasone is already in routine clinical practice for this indication globally.

**To proceed, the following is needed:**

- **Regulatory verification:** Confirm current ARTG registration status and approved indications via the TGA ARTG portal — betamethasone products may already carry skin/inflammatory indications applicable to AA
- **Formulation selection:** Clarify which route of administration is intended (topical, intralesional, or oral mini-pulse), as each has distinct evidence profiles, dose regimens, and safety monitoring requirements
- **Safety monitoring plan:** Formalise monitoring parameters including HPA axis assessment for systemic use, glucose and blood pressure monitoring, and skin assessment for topical applications
- **Paediatric considerations:** Specific dosing and safety protocols differ substantially from adults — dedicated paediatric guidelines review is recommended if treating children
- **Long-term management plan:** Given the relapsing-remitting nature of AA, define clear treatment duration, response criteria, and escalation pathways to second-line therapies (e.g., JAK inhibitors) if betamethasone response is inadequate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

