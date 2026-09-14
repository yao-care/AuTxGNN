---
layout: default
title: Sonidegib
parent: 僅模型預測 (L5)
nav_order: 639
evidence_level: L5
indication_count: 10
---

# Sonidegib
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

Using the drug-repurposing report template (v5) supplied in the system prompt to generate this report directly — no specialized skill applies to this documentation-formatting task.

Note on indication selection: `predicted_indications[0]` (rank 1, "medulloblastoma with extensive nodularity") carries a TxGNN score but zero trials/literature and pre-assigned `Hold`/`Research Question` status — same for ranks 2–5 and 7–10. Rank 6 ("skin cancer") is the only candidate with populated trial/literature evidence and `"pending"` scoring fields awaiting evaluation, so it is the substantive candidate this report evaluates. This is flagged below rather than silently substituted.

---

# Sonidegib: From Basal Cell Carcinoma to Skin Cancer (Confirmatory Signal)

## One-Sentence Summary

> Sonidegib is an oral Smoothened (SMO) / Hedgehog pathway inhibitor already approved overseas (e.g. Switzerland, USA, EU) for locally advanced basal cell carcinoma, but it is **not currently registered in Australia**.
> The TxGNN model — without being given this prior-approval information — independently predicts **Skin Cancer** as a top likely indication,
> supported by **10 clinical trials** and **20 publications**, including a completed Phase 2 randomised controlled trial (BOLT) with 42‑month follow‑up.
> This is best read as a **confirmatory validation signal** for the model rather than a genuinely novel indication.

*Nine other candidate indications for sonidegib were also flagged by TxGNN (e.g. medulloblastoma, xeroderma pigmentosum) but have no supporting trial or literature evidence in this dataset and remain at `Research Question`/`Hold` status — they are not covered further in this report.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Locally advanced basal cell carcinoma (per global literature — see [PMID 26323341](https://pubmed.ncbi.nlm.nih.gov/26323341/), "Sonidegib: First Global Approval"; not sourced from Australian regulatory data, as none exists) |
| Predicted New Indication | Skin Cancer |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Sonidegib is an orally bioavailable small-molecule antagonist of the Smoothened (SMO) receptor, which blocks signalling through the Hedgehog pathway ([PMID 26323341](https://pubmed.ncbi.nlm.nih.gov/26323341/); [PMID 33538567](https://pubmed.ncbi.nlm.nih.gov/33538567/)). This is a targeted mechanism rather than conventional cytotoxic chemotherapy.

Basal cell carcinoma (BCC) — the dominant tumour type in the evidence base below — is characterised by aberrant, constitutive activation of the Hedgehog pathway, most commonly via PTCH1 or SMO mutations ([PMID 31545507](https://pubmed.ncbi.nlm.nih.gov/31545507/)). Blocking SMO directly interrupts this driver pathway, which is the pharmacological basis for sonidegib's existing international approval in locally advanced and metastatic BCC.

In this evidence pack, the drug's original-indication and mechanism-of-action fields were flagged as data gaps at the structured-data level — the TxGNN model therefore generated the "Skin Cancer" prediction from knowledge-graph structure alone, without being told the drug's known approval history. That the model's top literature/trial-supported prediction converges on the disease area where sonidegib is already approved is a strong internal consistency check on the model, even though it does not represent a new indication for Australian decision-makers.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01327053](https://clinicaltrials.gov/study/NCT01327053) | Phase 2 | Completed | 230 | Randomised, double-blind BOLT study comparing two sonidegib dose levels in locally advanced/metastatic BCC — pivotal efficacy/safety trial |
| [NCT00961896](https://clinicaltrials.gov/study/NCT00961896) | Phase 2 | Completed | 18 | Double-blind, randomised, vehicle-controlled proof-of-concept study of topical LDE225 in Gorlin syndrome BCC, plus open-label extended-dosing expansion |
| [NCT03534947](https://clinicaltrials.gov/study/NCT03534947) | Phase 2 | Completed | 16 | Neoadjuvant sonidegib before surgery/imiquimod for BCC in cosmetically challenging locations, aiming to reduce surgical scarring |
| [NCT01576666](https://clinicaltrials.gov/study/NCT01576666) | Phase 1 | Completed | 120 | Dose-escalation of LDE225 + BKM120 (buparlisib) combination in advanced solid tumours including metastatic breast, pancreatic, colorectal cancer and glioblastoma |
| [NCT01033019](https://clinicaltrials.gov/study/NCT01033019) | Phase 2 | Terminated | 25 | Double-blind, randomised, vehicle-controlled study of topical LDE225 cream in sporadic superficial and nodular BCC |
| [NCT02303041](https://clinicaltrials.gov/study/NCT02303041) | Phase 2 | Terminated | 10 | Open-label pilot of sonidegib + buparlisib combination in advanced BCC |
| [NCT04007744](https://clinicaltrials.gov/study/NCT04007744) | Phase 1 | Active, not recruiting | 36 | Sonidegib + pembrolizumab combination dose-finding study in advanced solid tumours |
| [NCT06623201](https://clinicaltrials.gov/study/NCT06623201) | Phase 1 | Recruiting | 20 | Blue-light photodynamic therapy combined with sonidegib for multiple BCC lesions |
| [NCT05463757](https://clinicaltrials.gov/study/NCT05463757) | N/A | Recruiting | 80 | Netherlands prospective registration study comparing real-world use of vismodegib and sonidegib in advanced/multiple BCC |
| [NCT01757327](https://clinicaltrials.gov/study/NCT01757327) | Phase 2 | Withdrawn | 0 | Effect of Hedgehog inhibitor LDE225 on disseminated tumour cells in early-stage ER-negative/HER2-negative breast cancer (not a skin-cancer trial; withdrawn, 0 enrolled) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31545507](https://pubmed.ncbi.nlm.nih.gov/31545507/) | 2020 | RCT (42-month follow-up) | British Journal of Dermatology | Long-term efficacy and safety of sonidegib in advanced BCC from the pivotal BOLT randomised trial |
| [26323341](https://pubmed.ncbi.nlm.nih.gov/26323341/) | 2015 | Regulatory review | Drugs | "Sonidegib: First Global Approval" — SMO antagonist approved in Switzerland for advanced BCC |
| [31990414](https://pubmed.ncbi.nlm.nih.gov/31990414/) | 2020 | Expert opinion | J Eur Acad Dermatol Venereol | Joint expert opinion comparing sonidegib and vismodegib in locally advanced BCC |
| [33538567](https://pubmed.ncbi.nlm.nih.gov/33538567/) | 2021 | Review | J Drugs Dermatol | Review of Hedgehog inhibitors sonidegib and vismodegib for advanced BCC |
| [37326221](https://pubmed.ncbi.nlm.nih.gov/37326221/) | 2023 | Drug safety review | Expert Opin Drug Saf | Efficacy and safety evaluation of sonidegib for BCC management |
| [33888008](https://pubmed.ncbi.nlm.nih.gov/33888008/) | 2021 | Expert opinion | Expert Opin Drug Saf | Expert opinion on sonidegib efficacy, safety and tolerability |
| [27636236](https://pubmed.ncbi.nlm.nih.gov/27636236/) | 2016 | Review | Expert Rev Anticancer Ther | Safety and efficacy of sonidegib for locally advanced BCC |
| [35697404](https://pubmed.ncbi.nlm.nih.gov/35697404/) | 2022 | Review | Actas Dermosifiliogr | Update on Hedgehog pathway inhibitors vismodegib and sonidegib in advanced/metastatic BCC |
| [34683853](https://pubmed.ncbi.nlm.nih.gov/34683853/) | 2021 | Preclinical/formulation | Pharmaceutics | Ethosome gel formulation developed to improve sonidegib bioavailability and antitumour efficacy |
| [39861094](https://pubmed.ncbi.nlm.nih.gov/39861094/) | 2024 | Preclinical/formulation | Pharmaceuticals (Basel) | In situ pH-sensitive hydrogel of sonidegib-invasomes for intratumoral delivery in basal cell skin cancer |

---

## Australia Market Information

Sonidegib currently has **no ARTG entries** and is **not marketed in Australia**. No product listing, dosage form, or TGA-approved indication text is available to summarise.

---

## Cytotoxicity

*Sonidegib is classified as antineoplastic (Hedgehog-pathway inhibitor developed and used for BCC), so this section applies.*

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — oral Smoothened (SMO)/Hedgehog pathway inhibitor (not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions — no toxicity data available in this evidence pack |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions — no toxicity data available in this evidence pack |
| Monitoring Items | Please refer to the Product Information (PI) warnings and precautions |
| Handling Protection | As an oral targeted oncology agent, follow local institutional handling policy for oral anticancer medicines and confirm requirements against the PI |

---

## Safety Considerations

No TGA-approved Product Information exists for sonidegib, as it is not registered in Australia (0 ARTG entries). Structured safety fields (key warnings, contraindications, drug interactions) in this evidence pack are all unpopulated data gaps.

Please refer to the manufacturer's overseas-approved Product Information (e.g. FDA/EMA/Swissmedic Odomzo® labelling) for safety information until Australian TGA-approved labelling is available.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The evidence base is solid for the disease area overall (one completed Phase 2 RCT with 42-month follow-up, several additional completed/ongoing trials, and consistent supporting literature), but it largely confirms an indication sonidegib already holds overseas rather than establishing a new one for the Australian market.
- The absence of any Australian regulatory footprint (0 ARTG entries, no local PI) and the blocking safety data gap (DG001) mean this cannot proceed to routine clinical use without further local regulatory work.

**To proceed, the following is needed:**
- TGA registration status and pathway assessment (including potential use of overseas-approval-based pathways, given existing approvals elsewhere)
- Acquisition of a TGA-equivalent or overseas Product Information document to close the blocking safety data gap (DG001)
- Formal drug–drug interaction (DDI) database query, since none was found in this evidence pack
- Confirmation of drug-level mechanism of action (DG002) directly from DrugBank/PI rather than inferred from literature abstracts
- Separate scoping of the nine lower-evidence predicted indications (rank 1–5, 7–10) if research-question-stage exploration is desired
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

