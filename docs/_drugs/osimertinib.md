---
layout: default
title: Osimertinib
parent: 僅模型預測 (L5)
nav_order: 497
evidence_level: L5
indication_count: 10
---

# Osimertinib
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

# Osimertinib: From EGFR-Mutant Non-Small Cell Lung Cancer to Thrombocytopenia

## One-Sentence Summary

Osimertinib is a third-generation EGFR tyrosine kinase inhibitor (TKI) used to treat EGFR mutation-positive non-small cell lung cancer (NSCLC), as reflected throughout the clinical trial evidence in this pack. The TxGNN model predicts a possible link to **Thrombocytopenia**, but the supporting evidence base (8 trials, 20 publications) consistently describes thrombocytopenia as an **adverse effect of osimertinib**, not a condition it treats — this prediction should be treated as a low-confidence signal, not a therapeutic hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | EGFR mutation-positive non-small cell lung cancer (NSCLC) *(derived from clinical trial descriptions in this pack — no official indication text was returned by the regulatory query)* |
| Predicted New Indication | Thrombocytopenia |
| TxGNN Prediction Score | 98.46% |
| Evidence Level | L5 (model prediction only; no supporting therapeutic trials) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for osimertinib was not returned in this evidence pack (DG002, High severity data gap). What is available from the surrounding trial and literature evidence is a well-documented pharmacological picture: osimertinib is a third-generation EGFR-TKI used for EGFR-mutant NSCLC, and it has a recognised haematological adverse-effect profile that includes neutropenia, leukopenia, lymphopenia and thrombocytopenia (see PMID 33755621).

This is precisely why the prediction needs caution rather than endorsement. There is no known mechanism by which an EGFR-TKI would raise platelet counts or otherwise treat thrombocytopenia. Every clinical trial retrieved for this candidate (8/8) is an NSCLC treatment study in which thrombocytopenia appears only as a safety endpoint, and the literature is dominated by case reports and pharmacovigilance analyses of osimertinib-*induced* thrombocytopenia (e.g. PMID 36729978, PMID 36730569, PMID 40115544). The most plausible explanation is that TxGNN has picked up a drug–adverse-event co-occurrence signal in the underlying knowledge graph and represented it as a drug–disease treatment relationship — the association is real, but its direction is reversed relative to what "repurposing" would require.

This pattern is not isolated to thrombocytopenia. The other nine indications generated for osimertinib in this same evaluation batch (heart neoplasm, thrombotic disease, heart conduction disease, cardiovascular disease, heart disease, and several ultra-rare hereditary platelet disorders) show the same characteristic: high TxGNN scores driven by cardiotoxicity/haematotoxicity literature rather than genuine therapeutic rationale, and zero-evidence entries for the rarest conditions. All ten were independently scored L4–L5 with a "Hold" recommendation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03989115](https://clinicaltrials.gov/study/NCT03989115) | Phase 1/2 | Completed | 113 | RMC-4630 ± osimertinib in EGFR-mutant NSCLC; thrombocytopenia tracked only as a safety endpoint, not a treatment target |
| [NCT03455829](https://clinicaltrials.gov/study/NCT03455829) | Phase 1/2 | Completed | 30 | G1T38 (CDK4/6 inhibitor) + osimertinib in metastatic NSCLC — not a thrombocytopenia study |
| [NCT03381274](https://clinicaltrials.gov/study/NCT03381274) | Phase 1/2 | Active, not recruiting | 43 | Platform trial of novel combination therapies in previously treated EGFR-mutant NSCLC |
| [NCT07458919](https://clinicaltrials.gov/study/NCT07458919) | Early Phase 1 | Not yet recruiting | 94 | First- vs third-generation EGFR-TKI comparison for 19delins-mutant NSCLC |
| [NCT07285148](https://clinicaltrials.gov/study/NCT07285148) | Phase 1/2 | Not yet recruiting | 253 | ANS014004 + EGFR-TKI in EGFR-mutant NSCLC |
| [NCT02789345](https://clinicaltrials.gov/study/NCT02789345) | Phase 1 | Completed | 29 | Ramucirumab/necitumumab + osimertinib after progression on first-line EGFR-TKI |
| [NCT02424617](https://clinicaltrials.gov/study/NCT02424617) | Phase 1/2 | Completed | 40 | Bemcentinib (BGB324) + erlotinib in Stage IIIb/IV NSCLC |
| [NCT03940703](https://clinicaltrials.gov/study/NCT03940703) | Phase 2 | Active, not recruiting | 140 | Tepotinib + osimertinib in MET-amplified NSCLC with acquired osimertinib resistance |

**None of these trials evaluate osimertinib as a treatment for thrombocytopenia** — all are NSCLC treatment or combination-safety studies in which thrombocytopenia is a monitored adverse event.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41364874](https://pubmed.ncbi.nlm.nih.gov/41364874/) | 2025 | Real-world comparative | JCO Oncology Practice | Osimertinib vs first-generation EGFR-TKIs — real-world survival/safety comparison, no thrombocytopenia treatment claim |
| [37760942](https://pubmed.ncbi.nlm.nih.gov/37760942/) | 2023 | Cohort | Biomedicines | Plasma osimertinib levels correlated with adverse events, including haematological AEs |
| [32521871](https://pubmed.ncbi.nlm.nih.gov/32521871/) | 2020 | Cohort | J. B.U.ON. | Osimertinib + docetaxel efficacy/prognosis in NSCLC |
| [32173649](https://pubmed.ncbi.nlm.nih.gov/32173649/) | 2020 | Cohort | Pak J Pharm Sci | Osimertinib effect on serum MMP-7/MMP-9 in NSCLC |
| [38711856](https://pubmed.ncbi.nlm.nih.gov/38711856/) | 2024 | Cohort/case review | Front. Oncol. | Double-dose osimertinib + intrathecal pemetrexed for leptomeningeal metastasis |
| [34568058](https://pubmed.ncbi.nlm.nih.gov/34568058/) | 2021 | Phase 1 trial | Front. Oncol. | Dasatinib + osimertinib in TKI-naïve EGFR-mutant NSCLC |
| [36729978](https://pubmed.ncbi.nlm.nih.gov/36729978/) | 2023 | Case report | Anti-Cancer Drugs | Severe thrombocytopenia caused by osimertinib + sitagliptin; successful rechallenge after remission — describes thrombocytopenia as an **adverse effect**, not an indication |
| [36730569](https://pubmed.ncbi.nlm.nih.gov/36730569/) | 2023 | Case report | Anti-Cancer Drugs | Switch to aumolertinib after osimertinib-induced severe thrombocytopenia |
| [40115544](https://pubmed.ncbi.nlm.nih.gov/40115544/) | 2025 | Case report | Case Rep Oncol | Thrombocytopenia in an ARDS/ECMO patient on osimertinib |
| [33755621](https://pubmed.ncbi.nlm.nih.gov/33755621/) | 2021 | Clinical update | Am J Nursing | Lists thrombocytopenia among common osimertinib adverse effects (alongside leukopenia, neutropenia, lymphopenia) |

**All ten publications describe thrombocytopenia as a drug-induced adverse event of osimertinib, not as a condition it treats.** This is consistent, unambiguous evidence against the repurposing hypothesis.

---

## Australia Market Information

Osimertinib currently has **0 ARTG (Australian Register of Therapeutic Goods) entries** in this evidence pack, and market status is recorded as **not marketed**. No product, dosage form, or approved-indication data is available to summarise here.

---

## Cytotoxicity

Osimertinib is an antineoplastic agent (EGFR tyrosine kinase inhibitor used in NSCLC), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (EGFR tyrosine kinase inhibitor) — not a conventional cytotoxic chemotherapeutic |
| Myelosuppression Risk | Medium — literature in this pack reports neutropenia, leukopenia, lymphopenia and thrombocytopenia as recognised adverse effects (PMID 33755621, 36729978, 36730569) |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions — no emetogenicity data available in this pack |
| Monitoring Items | Full blood count (FBC) with differential; cardiac monitoring (ECG/LVEF) given the cardiotoxicity signal described below; renal and liver function |
| Handling Protection | Oral targeted therapy — handle per institutional cytotoxic/hazardous oral oncolytic handling policy; confirm against the TGA-approved PI once available |

---

## Safety Considerations

No TFDA warnings, contraindications, or drug interaction data were returned for osimertinib in this evidence pack (DG001, Blocking severity — safety pre-screening cannot proceed without this). Please refer to the TGA-approved Product Information (PI) for formal safety information.

For context, the literature gathered while evaluating these repurposing candidates (not part of the formal safety dataset, but relevant to clinical awareness) repeatedly flags osimertinib-associated cardiotoxicity (heart failure, cardiomyopathy), QT prolongation/arrhythmia, and thromboembolic events, in addition to the thrombocytopenia signal above. These are known risks worth flagging to prescribers pending formal PI review, independent of this repurposing assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence for a thrombocytopenia indication is not just weak but directionally contradictory — every trial and publication retrieved describes thrombocytopenia as an adverse effect caused by osimertinib, not a condition it treats. Combined with the missing TFDA/PI safety data (blocking gap) and the drug's unmarketed status in Australia, there is no basis to advance this candidate. The same pattern holds across all nine other TxGNN-ranked candidates in this batch (cardiac and haematological disease names driven by the same cardiotoxicity/haematotoxicity literature, or ultra-rare hereditary disorders with zero supporting evidence).

**To proceed, the following is needed:**
- TFDA/TGA Product Information (warnings, contraindications, DDI) to unblock the S1 safety pre-screen
- DrugBank-sourced mechanism of action data to confirm there is no biological rationale being missed
- A review of the TxGNN scoring pipeline to filter out drug–adverse-event co-occurrence signals being misclassified as drug–disease treatment relationships, since this appears to be a systematic issue affecting this entire candidate batch, not a one-off
- If market entry to Australia is ever considered for osimertinib's approved oncology indication, that would follow a separate ARTG registration pathway unrelated to this repurposing signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

