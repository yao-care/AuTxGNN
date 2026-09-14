---
layout: default
title: Teriflunomide
parent: 僅模型預測 (L5)
nav_order: 662
evidence_level: L5
indication_count: 10
---

# Teriflunomide
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

# Teriflunomide: From Not-Yet-Registered Status to Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

Teriflunomide is an oral DHODH-inhibiting immunomodulator that is **not currently registered** in this market and has no locally approved indication on file. The TxGNN model predicts it may be effective for **Relapsing-Remitting Multiple Sclerosis (RRMS)**, a use already supported by **28 clinical trials** and **19 publications** — including its globally marketed indication as Aubagio®.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no locally approved indication on record (drug not registered in this market) |
| Predicted New Indication | Relapsing-Remitting Multiple Sclerosis |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L1 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Teriflunomide is an oral inhibitor of dihydro-orotate dehydrogenase (DHODH), the rate-limiting enzyme in de novo pyrimidine synthesis. By restricting the pyrimidine pool, it selectively and reversibly suppresses the proliferation of rapidly dividing, activated T and B lymphocytes while sparing resting/slowly dividing cells — an established immunomodulatory mechanism rather than a novel repurposing hypothesis.

RRMS is fundamentally an autoimmune-mediated inflammatory demyelinating disease driven by activated lymphocyte clones attacking central nervous system myelin. Suppressing the proliferation of these activated lymphocytes directly targets that pathology, which is precisely the mechanism already leveraged by Aubagio® (teriflunomide), a disease-modifying therapy approved for RRMS in multiple jurisdictions globally.

Importantly, this evidence pack flags an important nuance: because this drug is not registered in this market ("Not Marketed", 0 entries), the TxGNN prediction of "RRMS" is not a genuine novel repurposing signal — it corresponds to teriflunomide's **existing, globally approved indication**. The high score and strong trial/literature base reflect an already-validated use rather than a new hypothesis requiring de novo mechanistic justification.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00134563](https://clinicaltrials.gov/study/NCT00134563) | Phase 3 | Completed | 1,088 | TEMSO pivotal RCT: teriflunomide reduced relapse frequency and delayed disability accumulation vs placebo |
| [NCT00803049](https://clinicaltrials.gov/study/NCT00803049) | Phase 3 | Completed | 742 | TEMSO long-term extension: documented long-term safety/tolerability of 7 mg and 14 mg doses |
| [NCT00883337](https://clinicaltrials.gov/study/NCT00883337) | Phase 3 | Completed | 324 | Head-to-head vs interferon beta-1a: comparable effectiveness by time-to-treatment-failure |
| [NCT04788615](https://clinicaltrials.gov/study/NCT04788615) | Phase 3 | Completed | 185 | Ofatumumab vs first-line DMT (including teriflunomide) in newly diagnosed relapsing MS |
| [NCT03535298](https://clinicaltrials.gov/study/NCT03535298) | Phase 4 | Active, not recruiting | 800 | DELIVER-MS: real-world comparison of early-intensive vs escalation DMT strategies |
| [NCT02776072](https://clinicaltrials.gov/study/NCT02776072) | N/A | Completed | 2,978 | Multicentre real-world outcomes study across DMTs including teriflunomide (Aubagio®) |
| [NCT03302442](https://clinicaltrials.gov/study/NCT03302442) | N/A | Completed | 3,000 | French MS Observatory cohort comparing dimethyl fumarate vs teriflunomide on clinical/MRI outcomes |
| [NCT06843382](https://clinicaltrials.gov/study/NCT06843382) | N/A | Not yet recruiting | 100 | ROOF-MS: prospective cohort comparing teriflunomide vs dimethyl fumarate on physical/cognitive fatigability |
| [NCT00228163](https://clinicaltrials.gov/study/NCT00228163) | Phase 2 | Completed | 147 | Long-term extension study assessing sustained safety and efficacy |
| [NCT03464448](https://clinicaltrials.gov/study/NCT03464448) | N/A | Completed | 30 | Mechanistic study: regulatory B lymphocytes as mediators of teriflunomide's therapeutic effect |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32757523](https://pubmed.ncbi.nlm.nih.gov/32757523/) | 2020 | RCT | NEJM | Ofatumumab vs teriflunomide (ASCLEPIOS I/II) |
| [36001711](https://pubmed.ncbi.nlm.nih.gov/36001711/) | 2022 | RCT | NEJM | Ublituximab vs teriflunomide in relapsing MS |
| [40202623](https://pubmed.ncbi.nlm.nih.gov/40202623/) | 2025 | RCT | NEJM | Tolebrutinib vs teriflunomide in relapsing MS |
| [26758290](https://pubmed.ncbi.nlm.nih.gov/26758290/) | 2016 | RCT | CNS Drugs | Review of EU SmPC data; key efficacy/safety outcomes for RRMS and first demyelinating event |
| [33779698](https://pubmed.ncbi.nlm.nih.gov/33779698/) | 2021 | Phase 3 RCT | JAMA Neurology | OPTIMUM trial: ponesimod vs teriflunomide, active-comparator design |
| [35266417](https://pubmed.ncbi.nlm.nih.gov/35266417/) | 2022 | Phase 3 RCT | Mult Scler | ASCLEPIOS I/II: ofatumumab superior to teriflunomide in treatment-naive patients |
| [39307151](https://pubmed.ncbi.nlm.nih.gov/39307151/) | 2024 | Phase 3 RCT | Lancet Neurology | evolutionRMS1/2: evobrutinib vs teriflunomide active comparator |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | Network Meta-analysis | Cochrane Database Syst Rev | Comparative benefit of immunomodulators/immunosuppressants, including teriflunomide, in RRMS |
| [33620411](https://pubmed.ncbi.nlm.nih.gov/33620411/) | 2021 | Review | JAMA | Diagnosis and treatment overview of MS, including DMT positioning |
| [31098896](https://pubmed.ncbi.nlm.nih.gov/31098896/) | 2019 | Review | Drugs | Teriflunomide (Aubagio®) review of RCT and real-world evidence in RRMS |

---

## Australia Market Information

Teriflunomide currently has **no ARTG entries** (0 licenses on record) and is **not marketed** in this jurisdiction — no local product, dosage form, or approved indication text is available to summarise.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Evidence level L1 is supported by multiple completed Phase 3 RCTs (TEMSO and its extension, plus several active-comparator Phase 3 trials), giving strong efficacy and long-term safety data for teriflunomide in RRMS. However, this reflects confirmation of an **already-established global indication** rather than a genuinely novel repurposing signal, and the drug has no current local registration or safety documentation in this market.

**To proceed, the following is needed:**
- Local TFDA/TGA Product Information (warnings, contraindications, boxed warnings — e.g. known hepatotoxicity and teratogenicity risk from the broader literature) since none is currently on file
- Confirmation of local registration/import pathway status given "Not Marketed" status and 0 ARTG entries
- Drug interaction (DDI) data, currently unresolved ("not_found")
- Clarification in any downstream materials that this prediction corresponds to teriflunomide's known global indication (Aubagio®), not a novel hypothesis, to avoid overstating the repurposing narrative
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

