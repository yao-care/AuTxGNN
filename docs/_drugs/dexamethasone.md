---
layout: default
title: Dexamethasone
parent: 僅模型預測 (L5)
nav_order: 149
evidence_level: L5
indication_count: 10
---

# Dexamethasone
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

# Dexamethasone: From Inflammatory and Immune Conditions to Alopecia Areata

---

## One-Sentence Summary

Dexamethasone is a potent synthetic glucocorticoid with well-established anti-inflammatory and immunosuppressive properties, widely used across a broad spectrum of inflammatory, allergic, and autoimmune conditions.
The TxGNN model predicts it may be effective for **Alopecia Areata (AA)**, with **no directly registered clinical trials** but **20 publications** currently supporting this direction — including a randomised controlled trial and multiple prospective cohort studies examining the Dexamethasone Oral Mini-Pulse (DMP) regimen specifically for AA.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anti-inflammatory and immunosuppressive therapy (no TGA-specific indication data captured in this evidence pack — TGA ARTG verification recommended) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Australia Market Status | Not Listed (0 ARTG entries — likely a data capture gap; independent TGA ARTG verification required) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not captured in this evidence pack. However, based on well-established pharmacology, dexamethasone is a synthetic glucocorticoid that binds intracellular glucocorticoid receptors (GR), triggering broad suppression of the immune cascade — including downregulation of pro-inflammatory cytokines (IL-2, IFN-γ, TNF-α), inhibition of T cell activation and proliferation, and reduction of immune cell trafficking to inflamed tissues.

Alopecia areata is a T cell-mediated autoimmune condition in which CD8+ cytotoxic T cells breach the immune privilege of the hair follicle bulb, leading to non-scarring hair loss. This pathological mechanism maps directly onto dexamethasone's primary pharmacological target. The "Dexamethasone Mini-Pulse" (DMP) regimen — typically 5 mg orally on two consecutive days per week — was specifically developed for AA to deliver immunosuppressive efficacy while substantially reducing the systemic adverse effects (HPA axis suppression, metabolic complications) associated with daily corticosteroid dosing.

The near-maximal TxGNN prediction score of 99.99% reflects the strong mechanistic and empirical association between glucocorticoids and autoimmune alopecia. Real-world evidence, including a paediatric RCT and multiple prospective cohort and multicentre studies across several countries, confirms this is not merely a model prediction — dexamethasone DMP is an established clinical practice for moderate-to-severe AA in many healthcare settings, particularly where JAK inhibitors (baricitinib, ritlecitinib) are inaccessible due to cost, contraindications, or regulatory availability.

---

## Clinical Trial Evidence

> **Important note:** The 13 clinical trials retrieved by database search involved dexamethasone primarily as a supportive or adjuvant agent in oncology settings (Grade C relevance to AA — not investigating dexamethasone as a treatment for alopecia areata). No registered Phase 2 or 3 clinical trials with dexamethasone as the primary investigational agent for alopecia areata were identified in this search. Evidence for efficacy in AA derives predominantly from the published literature (see below).

The only trial in the retrieved set with direct relevance to monitoring dexamethasone use is summarised below:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT04343560](https://clinicaltrials.gov/study/NCT04343560) | N/A | Completed | 380 | Examines effects of abnormal steroid metabolome (via dexamethasone suppression testing) on bone strength, bone density, and body composition in adults with mild autonomous cortisol secretion. Relevant as a safety reference for long-term DMP monitoring, particularly vertebral fracture risk. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [36086930](https://pubmed.ncbi.nlm.nih.gov/36086930/) | 2022 | RCT | Dermatologic Therapy | Randomised open-label trial (n=30 children) comparing dexamethasone OMP vs. diphencyclopropenone (DPCP) contact sensitisation in severe paediatric AA. Assessed effectiveness and safety of the DMP regimen directly. |
| [39042154](https://pubmed.ncbi.nlm.nih.gov/39042154/) | 2024 | Systematic Review / Meta-analysis | Archives of Dermatological Research | Network meta-analysis (PRISMA-compliant) comparing systemic steroids, oral JAK inhibitors, and contact immunotherapy in severe AA (SALT ≥ 50%). Provides comparative efficacy evidence for dexamethasone versus newer agents. |
| [35330017](https://pubmed.ncbi.nlm.nih.gov/35330017/) | 2022 | Prospective Cohort | Journal of Clinical Medicine | Real-world prospective cohort assessing effectiveness and safety of mini-pulse oral corticosteroid (dexamethasone) for AA, including factors associated with successful treatment response. |
| [36070222](https://pubmed.ncbi.nlm.nih.gov/36070222/) | 2022 | Prospective Cohort / Systematic Review | Dermatologic Therapy | Multicentre study of dexamethasone oral mini-pulse in moderate-to-severe AA (including totalis and universalis subtypes), conducted in Europe where JAK inhibitor accessibility is limited. |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Review | Pediatric Dermatology | Literature review evaluating dosing regimens, administration protocols, and adverse effects of pulse-dose corticosteroid therapy (including dexamethasone) for AA in children. |
| [31579982](https://pubmed.ncbi.nlm.nih.gov/31579982/) | 2019 | Retrospective Cohort | Dermatologic Therapy | Prospective study of 73 paediatric patients with severe AA (>30% scalp involvement) comparing 1-day vs. 3-day intravenous dexamethasone pulse regimens monthly for 6–12 months, combined with topical corticosteroids. |
| [26179196](https://pubmed.ncbi.nlm.nih.gov/26179196/) | 2015 | Cohort | Dermatologic Therapy | Long-term follow-up (median 96 months) of 65 children/adolescents with severe AA treated with oral dexamethasone pulse combined with topical corticosteroids. Provides durable outcome data. |
| [41243342](https://pubmed.ncbi.nlm.nih.gov/41243342/) | 2025 | Case Series / Clinical Observation | The Journal of Dermatological Treatment | Reports durable remission of severe AA with dexamethasone oral mini-pulse in patients ineligible for JAK inhibitors, with a focused literature review. Clinically relevant to the Australian context where access barriers may exist. |
| [10535249](https://pubmed.ncbi.nlm.nih.gov/10535249/) | 1999 | Clinical Study | The Journal of Dermatology | Early cohort study (n=30) of twice-weekly 5 mg dexamethasone oral pulse in extensive AA and alopecia totalis; evaluates terminal hair regrowth over minimum 12-week treatment. One of the foundational DMP studies. |
| [16707886](https://pubmed.ncbi.nlm.nih.gov/16707886/) | 2006 | Comparative Clinical Study | Dermatology (Basel) | Compares efficacy, relapse rates, and adverse effects among three systemic corticosteroid modalities for extensive AA, providing context for positioning dexamethasone DMP within the treatment algorithm. |

---

## Australia Market Information

No ARTG entries for Dexamethasone were returned by the data pipeline at the time of this evidence pack generation (2026-04-04). This almost certainly reflects a **data capture limitation** rather than true absence from the Australian market, as dexamethasone is a long-established medicine on the WHO Essential Medicines List and is known to be available globally in multiple formulations.

**Action required:** Verify current TGA ARTG registration status directly at [https://www.tga.gov.au/resources/artg](https://www.tga.gov.au/resources/artg) before proceeding with any prescribing or formulary decisions.

---

## Safety Considerations

Safety data (TGA-approved warnings, contraindications, and drug interactions) was not captured in this evidence pack.

Please refer to the **TGA-approved Product Information (PI)** for comprehensive safety information. When using dexamethasone for the DMP regimen in alopecia areata, the following are particularly relevant to review in the PI:

- **HPA axis suppression** — even with mini-pulse dosing, prolonged use carries suppression risk; consider monitoring with morning cortisol or low-dose ACTH stimulation test in long-term therapy
- **Metabolic effects** — glucose intolerance, weight gain, dyslipidaemia
- **Bone density** — vertebral fracture risk with chronic corticosteroid exposure (see NCT04343560 reference above)
- **Infectious risk** — reactivation of latent infections (TB screening recommended), opportunistic infections
- **Ocular effects** — posterior subcapsular cataracts, raised intraocular pressure
- **Psychiatric effects** — mood disturbance, insomnia
- **Paediatric considerations** — growth suppression with prolonged use; dosing adjustments required

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple published studies — including a paediatric RCT and several prospective multicentre cohort studies — directly support the efficacy of the dexamethasone oral mini-pulse (DMP) regimen for moderate-to-severe alopecia areata, with a well-defined mechanistic basis (T cell-mediated autoimmune suppression). The TxGNN prediction score of 99.99% reflects this established clinical signal. Evidence level L2 is assigned on the strength of one RCT and multiple prospective cohort studies; however, the absence of large completed Phase 3 RCTs dedicated to dexamethasone monotherapy for AA means guardrails around patient selection, monitoring, and duration of use are essential.

**To proceed, the following is needed:**

- **TGA ARTG verification:** Confirm current Australian registration status and retrieve the approved Product Information (PI) for complete safety, contraindication, and dosing information
- **Safety data completion:** Obtain TGA-approved warnings and contraindications; review drug interaction profile (particularly with anticoagulants, antidiabetics, immunosuppressants, and CYP3A4 inducers/inhibitors)
- **Patient eligibility criteria:** Define the target population (adults vs. paediatric; SALT score threshold; prior treatment history; JAK inhibitor eligibility assessment)
- **Dosing protocol specification:** Confirm the DMP regimen to be used (dose, frequency, duration, tapering schedule) based on published protocols and local prescribing conventions
- **Monitoring plan:** Establish baseline and ongoing monitoring for HPA axis function, bone mineral density (DEXA scan at baseline and annually), fasting glucose, and blood pressure
- **Risk-benefit documentation:** Formal clinician-patient shared decision-making documentation, particularly given the systemic adverse effect profile relative to newer approved treatments (baricitinib, ritlecitinib)
- **Specialist input:** Recommend involvement of a dermatologist (and endocrinologist if HPA monitoring is required) before initiating systemic DMP therapy for AA

---

*This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All clinical decisions must be made by qualified healthcare professionals in accordance with current Australian guidelines and TGA-approved prescribing information.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

