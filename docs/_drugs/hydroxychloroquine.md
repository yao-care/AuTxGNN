---
layout: default
title: Hydroxychloroquine
parent: 僅模型預測 (L5)
nav_order: 232
evidence_level: L5
indication_count: 10
---

# Hydroxychloroquine
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

# Hydroxychloroquine: From Autoimmune & Antimalarial Therapy to Quinquaud's Folliculitis Decalvans

## One-Sentence Summary

Hydroxychloroquine (HCQ) is an established antimalarial and immunomodulatory agent, internationally used for systemic lupus erythematosus (SLE), rheumatoid arthritis (RA), and related autoimmune conditions.
The TxGNN model predicts it may be effective for **Quinquaud's Folliculitis Decalvans** — the most common form of primary neutrophilic scarring alopecia —
with **0 clinical trials** but **4 publications** currently supporting this direction, including a 2025 EADV Task Force position statement and a 5-year retrospective cohort of 49 patients.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in ARTG dataset (HCQ internationally established for malaria, SLE, RA) |
| Predicted New Indication | Quinquaud's Folliculitis Decalvans |
| TxGNN Prediction Score | 98.66% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note:** HCQ (Plaquenil®) is widely registered internationally. The 0-entry ARTG result may reflect a data collection gap. Clinicians should verify current TGA registration status directly via the ARTG public search portal before clinical use.

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on well-established pharmacological knowledge, Hydroxychloroquine is an aminoquinoline derivative that acts primarily by elevating lysosomal pH, thereby disrupting antigen processing and TLR7/TLR9-mediated innate immune signalling. This leads to downstream suppression of IFN-α/γ production, reduced pro-inflammatory cytokine release (including IL-1β, IL-6, and TNF-α), and inhibited neutrophil chemotaxis — all without the systemic immunosuppression associated with corticosteroids.

Quinquaud's folliculitis decalvans (FD) is characterised by a neutrophil-dominant inflammatory infiltrate targeting hair follicles, leading to progressive, irreversible scarring alopecia primarily affecting the vertex scalp of younger patients. The role of dysregulated innate immune activation — rather than purely *Staphylococcus aureus* infection — is now increasingly recognised, particularly in "lichen planopilaris-like" or less-active forms of FD where autoimmune mechanisms are central. This pathogenic overlap places HCQ's mechanism of TLR inhibition and cytokine suppression directly in the relevant disease pathway.

The clinical plausibility is reinforced by the 2025 EADV Task Force on Hair Diseases Position Statement, which formally includes HCQ among the therapeutic options for FD management. A dedicated 5-year retrospective study (PMID 39340420, n=49) specifically investigated HCQ as adjuvant therapy, supporting its use in cases where follicular inflammation is not purely infection-driven. Taken together, this mechanistic rationale and emerging clinical evidence constitute a reasonable basis for further investigation.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for Hydroxychloroquine in Quinquaud's folliculitis decalvans.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [40230058](https://pubmed.ncbi.nlm.nih.gov/40230058/) | 2025 | Clinical Guideline / Task Force Statement | J Eur Acad Dermatol Venereol | EADV Task Force position statement on FD management; HCQ included as a treatment option; highlights chronic-relapsing course and need for anti-inflammatory therapy extended beyond disease resolution |
| [39340420](https://pubmed.ncbi.nlm.nih.gov/39340420/) | 2025 | Retrospective Cohort | Clin Exp Dermatology | HCQ as adjuvant therapy in 49 FD patients over 5 years; suggests particular benefit in less-active/"LPP-like" FD phenotypes where autoimmune mechanisms predominate over *S. aureus* |
| [39893632](https://pubmed.ncbi.nlm.nih.gov/39893632/) | 2025 | Review | Expert Opin Drug Metab Toxicol | Comprehensive systematic literature review (2015–2024) of alopecia treatments across scarring and non-scarring types; covers HCQ efficacy, safety, and tolerability profile |
| [32030059](https://pubmed.ncbi.nlm.nih.gov/32030059/) | 2019 | Case Report | Int J Trichology | Therapy-recalcitrant FD case; HCQ cited as a standard prior treatment option alongside corticosteroids, isotretinoin, and dapsone; ultimately controlled with adalimumab, highlighting role of biologics in refractory cases |

---

## Australia Market Information

No ARTG entries are currently recorded for Hydroxychloroquine in this dataset. The ARTG table cannot be populated from the available data.

Clinicians are advised to consult the [TGA ARTG Public Summary](https://www.tga.gov.au/resources/artg) directly for current registration status and approved Product Information.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

> **Clinical Note:** Regardless of formal TGA PI availability in this dataset, prescribers should be aware that HCQ carries a well-documented risk of **irreversible retinal toxicity** with cumulative dosing. Baseline ophthalmological assessment and annual retinal screening are standard of care for long-term HCQ use (typically from Year 5 onward, or earlier in higher-risk patients). This monitoring requirement is particularly relevant when considering use in dermatological conditions where treatment duration may be prolonged.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The 2025 EADV position statement and a dedicated 5-year retrospective cohort study provide meaningful Level 3 evidence supporting HCQ as an adjuvant anti-inflammatory agent in folliculitis decalvans, particularly for cases with autoimmune-predominant pathology. The mechanistic rationale — TLR7/9 inhibition and lysosomal pH disruption attenuating neutrophil-driven follicular inflammation — is well-grounded in HCQ pharmacology. However, the absence of controlled clinical trials and the small number of directly relevant publications preclude a higher recommendation at this stage.

**To proceed, the following is needed:**

- **Regulatory verification:** Confirm current TGA/ARTG registration status for HCQ in Australia; obtain TGA-approved PI for complete safety, contraindication, and dosing data
- **MOA documentation:** Retrieve full mechanism of action data from DrugBank (DB01611) to strengthen mechanistic analysis
- **Patient stratification strategy:** Evidence suggests HCQ is more likely effective in "LPP-like" / autoimmune-predominant FD phenotypes versus classic *S. aureus*-driven presentations; define inclusion criteria accordingly
- **Ophthalmological monitoring protocol:** Establish baseline and ongoing retinal screening schedule consistent with international HCQ safety guidelines (e.g., Royal Australian and New Zealand College of Ophthalmologists recommendations)
- **Prospective study design:** A prospective, multicentre open-label pilot study (e.g., n=30–50) with standardised FD outcome measures (e.g., Folliculitis Decalvans Activity Score) would be the logical next step
- **Efficacy boundary definition:** Based on PMID 39340420, define which FD subtype (active neutrophilic vs. LPP-like) is the primary target population before trial initiation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

