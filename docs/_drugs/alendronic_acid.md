---
layout: default
title: Alendronic Acid
parent: 僅模型預測 (L5)
nav_order: 30
evidence_level: L5
indication_count: 10
---

# Alendronic Acid
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

# Alendronic Acid: From Osteoporosis to HIV Infectious Disease

## One-Sentence Summary

Alendronic acid is a bisphosphonate well-established globally for the prevention and treatment of osteoporosis and related metabolic bone disorders.
The TxGNN model predicts it may be effective for **HIV Infectious Disease** — specifically in managing HIV-associated bone loss —
with **4 clinical trials** and **2 publications** currently supporting this direction.
The clinical evidence base is notably strong, anchored by a completed Phase 3 RCT conducted directly in HIV patients with osteoporosis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Osteoporosis (no ARTG entry found; well-established internationally for osteoporosis and Paget's disease of bone) |
| Predicted New Indication | HIV Infectious Disease |
| TxGNN Prediction Score | 96.78% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed (no ARTG entries identified) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, alendronic acid is a nitrogen-containing bisphosphonate that works by inhibiting osteoclast activity through the mevalonate pathway — the same biochemical route used by statins, though with bone-specific tissue distribution. By suppressing osteoclast-mediated bone resorption, alendronate preserves and rebuilds bone mineral density (BMD) across a range of conditions characterised by excess bone loss.

People living with HIV (PLWH) are at substantially elevated risk of osteoporosis and fracture for several converging reasons. HIV itself triggers chronic systemic inflammation, driving osteoclast activation via cytokines such as RANKL and TNF-α. Older antiretroviral agents — particularly tenofovir disoproxil fumarate (TDF) and protease inhibitors — are associated with direct adverse effects on bone metabolism, including impaired vitamin D activation and direct tubular toxicity affecting calcium homeostasis. Hypogonadism and vitamin D deficiency, both common in PLWH, compound the risk further. Taken together, HIV-related bone loss is a condition characterised by overactive osteoclast activity — precisely the mechanism that alendronate is designed to counteract.

This prediction therefore reflects a targeted application of alendronate's existing mechanism to a well-characterised complication of HIV disease, rather than a novel or speculative use. The biological rationale is strong, and the clinical evidence base — including a multicentre Phase 3 RCT (ANRS 120 Fosivir) conducted specifically in HIV-1 patients with primary osteoporosis, two further completed Phase 2 RCTs, and a published systematic review pooling eight RCTs — is among the most robust seen in TxGNN repurposing analyses.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT00120757](https://clinicaltrials.gov/study/NCT00120757) | Phase 3 | Completed | 140 | ANRS 120 Fosivir: Multicentre, randomised, double-blind, placebo-controlled RCT evaluating alendronate efficacy vs placebo over 2 years in HIV-1 patients with primary osteoporosis; all participants received calcium and vitamin D supplementation. This is the core L1 evidence for this indication. |
| [NCT00061256](https://clinicaltrials.gov/study/NCT00061256) | Phase 2 | Completed | 80 | Randomised, double-blind, placebo-controlled study of once-weekly alendronate in HIV-infected individuals with decreased BMD receiving calcium and vitamin D; directly evaluated safety and efficacy of this dosing schedule in the HIV population. |
| [NCT00921557](https://clinicaltrials.gov/study/NCT00921557) | Phase 2 | Completed | 52 | Oral alendronate therapy in HIV-infected children and adolescents with low BMD; assessed changes in lumbar spine BMD at 24 and 48 weeks, extending the safety and efficacy evidence base to paediatric populations with perinatally acquired HIV. |
| [NCT02322099](https://clinicaltrials.gov/study/NCT02322099) | Phase 4 | Terminated | 53 | Multicentre, prospective RCT of short-course alendronate vs placebo to prevent BMD loss in antiretroviral-naïve HIV-1 subjects initiating ART; terminated early with only 53 of the planned cohort enrolled. **The reason for termination should be investigated before clinical use** — early termination due to safety concerns carries different implications to recruitment difficulties. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25300622](https://pubmed.ncbi.nlm.nih.gov/25300622/) | 2014 | Systematic Review & Meta-analysis | AIDS Reviews | Pooled analysis of 8 RCTs evaluating bisphosphonate effects on BMD in adults with HIV infection; outcomes assessed at lumbar spine, femoral neck, and total hip via DXA using a fixed-effects model; provides the highest level of aggregated evidence for bisphosphonate use in this population. |
| [26890207](https://pubmed.ncbi.nlm.nih.gov/26890207/) | 2016 | Review / Clinical Guideline | Current Opinion in HIV and AIDS | Comprehensive review of pharmacological approaches to prevention and management of low BMD in PLWH, contextualising fracture risk and offering practical treatment guidance for clinicians managing this patient group. |

---

## Australia Market Information

No ARTG entries were identified for alendronic acid at the time of this analysis. The Australian market status is recorded as **Not marketed** based on available regulatory data.

> **Important note for clinicians**: Alendronic acid (marketed as Fosamax® and numerous generics) is widely available and TGA-approved in comparable markets including the United Kingdom, United States, New Zealand, and across the EU. The absence of ARTG entries in this dataset may reflect a search gap or data currency issue rather than a true absence from the Australian market. Prescribers are strongly advised to verify current ARTG registration status directly via the [TGA ARTG search portal](https://www.tga.gov.au/resources/artg) before any clinical application.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for complete safety information.

> **Additional clinical note**: Oral bisphosphonates including alendronate are associated with oesophageal irritation and, rarely, oesophageal ulceration. Standard precautions require patients to take the tablet with a full glass of water and remain upright for at least 30 minutes post-ingestion. This is of particular relevance in the HIV context, where oesophageal comorbidities (e.g., candidiasis, CMV oesophagitis) may be present. Drug interaction data was not available in this analysis — a formal DDI review against common antiretroviral regimens (including TDF, PIs, and integrase inhibitors) is required before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 RCT conducted specifically in HIV-1 patients with primary osteoporosis (ANRS 120 Fosivir, n=140), supported by two further completed Phase 2 RCTs and a systematic review and meta-analysis pooling eight RCTs, constitutes a clinically substantial evidence base. The mechanistic link between HIV-related bone loss and alendronate's osteoclast-inhibiting mechanism is direct and well-characterised.

**To proceed, the following is needed:**

- **Verify ARTG registration**: Confirm current TGA registration status for alendronic acid in Australia — the 0-entry result may reflect a data gap rather than true unavailability
- **Resolve early termination of NCT02322099**: Investigate whether the Phase 4 trial was terminated due to safety signals, recruitment difficulties, or sponsor decisions; this distinction is critical to risk assessment
- **Obtain full TGA Product Information (PI)**: Download and parse the TGA-approved PI to complete the key warnings, contraindications, and precautions assessment (currently a blocking data gap)
- **Conduct DDI review**: Perform a formal drug-drug interaction analysis between alendronate and commonly prescribed antiretroviral agents (TDF, PIs, NNRTIs, integrase inhibitors), given that HIV patients are routinely on complex polypharmacy
- **Retrieve MOA data from DrugBank (DB00630)**: Complete the mechanistic analysis with structured pharmacological data
- **Define target population**: Clarify whether the intended use is prevention of ART-initiation-related BMD loss, treatment of established HIV-associated osteoporosis, or both — as the evidence base, dosing schedule, and monitoring requirements differ across these scenarios

---

*This report is intended for research and evaluation purposes only and does not constitute medical advice. Drug repurposing candidates require prospective clinical validation before therapeutic application. All content should be considered in conjunction with current TGA-approved prescribing information and clinical judgement.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

