---
layout: default
title: Paclitaxel
parent: 僅模型預測 (L5)
nav_order: 505
evidence_level: L5
indication_count: 10
---

# Paclitaxel
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

# Paclitaxel: From Antineoplastic Chemotherapy to Female Breast Carcinoma

## One-Sentence Summary

Paclitaxel is a taxane-class cytotoxic chemotherapy agent with a long history of use across multiple solid tumour types. The TxGNN model's top-ranked prediction — **Female Breast Carcinoma** — is supported by an unusually strong evidence base of **50+ clinical trials** (including large Phase 3 randomised trials) and **20 publications**, though the evidence indicates this is a confirmation of paclitaxel's already well-established role in breast cancer treatment rather than a genuinely novel repurposing hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (drug-level indication data gap); Paclitaxel is internationally recognised as a taxane-class antineoplastic agent used across multiple solid tumours |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed (per this evidence pack) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for this drug record is not available (data gap). Based on established pharmacological knowledge, Paclitaxel is a taxane that binds to and stabilises tubulin polymers, preventing microtubule depolymerisation. This locks cells in metaphase, blocking mitotic progression and triggering apoptosis — an effect that is most pronounced in rapidly dividing cell populations such as breast carcinoma cells.

While this evidence pack does not record a specific "original indication" for the drug, the evidence trail for the predicted indication itself tells an important story: the volume, phase and completeness of the clinical trial record (including the pivotal CALGB 9344 trial establishing adjuvant benefit in node-positive breast cancer) indicate that paclitaxel's use in breast carcinoma is **already an established, guideline-endorsed practice** internationally, rather than a new hypothesis generated purely from knowledge-graph inference. The model's other top-ranked candidates for this drug — estrogen-receptor negative breast cancer, hormone-resistant breast carcinoma, and estrogen-receptor positive breast cancer — reinforce this pattern, all scoring similarly highly and drawing on overlapping trial evidence.

Mechanistically, this consistency makes sense: paclitaxel's cytotoxic, antimitotic action is independent of hormone receptor (ER/PR) or HER2 status, which is why it retains efficacy across all major molecular subtypes of breast cancer — from hormone receptor-positive disease requiring chemotherapy, through to triple-negative and HER2-overexpressing tumours. For a pharmacist reviewing this record, the key takeaway is that this "prediction" reflects the confirmation of pre-existing, high-quality clinical evidence rather than an unproven repurposing signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00991263](https://clinicaltrials.gov/study/NCT00991263) | N/A (correlative/translational) | Completed | 3,677 | CALGB 9344/9741 tissue-based analysis identifying which intrinsic breast cancer subtypes derive benefit from adjuvant paclitaxel — a pivotal, practice-informing dataset |
| [NCT00272987](https://clinicaltrials.gov/study/NCT00272987) | Phase 3 | Terminated | 63 | Randomised, double-blind, placebo-controlled trial of paclitaxel + trastuzumab ± lapatinib in HER2-overexpressing metastatic breast cancer |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Completed | 3,270 | Adjuvant chemotherapy (docetaxel/cyclophosphamide, or doxorubicin/cyclophosphamide followed by weekly paclitaxel) ± trastuzumab in node-positive/high-risk HER2-low breast cancer |
| [NCT00003088](https://clinicaltrials.gov/study/NCT00003088) | Phase 3 | Completed | 2,005 | Sequential vs concurrent doxorubicin, paclitaxel and cyclophosphamide at different dosing intervals for node-positive Stage II/IIIA breast cancer |
| [NCT02125344](https://clinicaltrials.gov/study/NCT02125344) | Phase 3 | Completed | 961 | GeparOcto: dose-dense, dose-intensified paclitaxel-containing regimens as neoadjuvant treatment for high-risk early breast cancer |
| [NCT00433420](https://clinicaltrials.gov/study/NCT00433420) | Phase 3 | Active, not recruiting | 2,000 | EC→paclitaxel vs FEC→paclitaxel (2- vs 3-weekly, pegfilgrastim-supported) for node-positive breast cancer |
| [NCT04158362](https://clinicaltrials.gov/study/NCT04158362) | Phase 3 | Active, not recruiting | 180 | AMBRE: standard chemotherapy vs endocrine therapy + abemaciclib as initial treatment for ER+/HER2- metastatic breast cancer with high visceral burden |
| [NCT00709761](https://clinicaltrials.gov/study/NCT00709761) | Phase 2 | Completed | 60 | Weekly nab-paclitaxel + lapatinib in HER2-overexpressing metastatic breast cancer |
| [NCT04771871](https://clinicaltrials.gov/study/NCT04771871) | Phase 2 | Unknown | 42 | Treatment response and microRNA profiling in triple-negative breast cancer patients receiving standard (paclitaxel-based) chemotherapy |
| [NCT05238922](https://clinicaltrials.gov/study/NCT05238922) | Phase 1 | Recruiting | 604 | INCB123667 as monotherapy and in combination with anticancer therapies (including paclitaxel-based regimens) in advanced solid tumours, including breast cancer |

*No ANZCTR-registered trials were identified in this evidence pack.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | Cohort/Clinical Study | Cancer | Phase II multicentre trial of doxorubicin + paclitaxel in metastatic breast carcinoma; efficacy influenced by prior adjuvant anthracycline exposure |
| [32461977](https://pubmed.ncbi.nlm.nih.gov/32461977/) | 2020 | Cohort/Clinical Study | BioMed Research International | Real-world evaluation of neoadjuvant epirubicin/cyclophosphamide + weekly paclitaxel-trastuzumab in HER2-positive breast carcinoma |
| [31783552](https://pubmed.ncbi.nlm.nih.gov/31783552/) | 2019 | Review | Biomolecules | Comprehensive review of paclitaxel's mechanistic and clinical effects in breast cancer, including resistance mechanisms |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug and Therapeutics Bulletin | Early independent review confirming paclitaxel/docetaxel efficacy in breast and ovarian cancer |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | Genetic Association Study | Nature Communications | TEKT4 germline variants enriched in breast tumours resistant to paclitaxel, informing predictive biomarker research |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | Preclinical/Mechanistic | Chemical Biology & Drug Design | Paclitaxel combination therapy potential and in vivo biomarkers in breast carcinoma models |
| [31515668](https://pubmed.ncbi.nlm.nih.gov/31515668/) | 2019 | Preclinical/Mechanistic | Cancer Chemotherapy and Pharmacology | SRSF3 downregulation sensitises breast cancer (and oral squamous cell carcinoma) cells to paclitaxel |
| [39009452](https://pubmed.ncbi.nlm.nih.gov/39009452/) | 2024 | Preclinical/Mechanistic | Journal for ImmunoTherapy of Cancer | Paclitaxel's effect on tumour-associated macrophages enhancing PD-1 blockade activity in breast cancer |
| [36964413](https://pubmed.ncbi.nlm.nih.gov/36964413/) | 2023 | Preclinical/Mechanistic | Human Cell | TIPE2 sensitises breast cancer cells to paclitaxel by suppressing drug-induced autophagy and cancer stem cell properties |
| [20665703](https://pubmed.ncbi.nlm.nih.gov/20665703/) | 2011 | Preclinical/In vitro | Journal of Cellular Physiology | ZD6474 (a dual EGFR/VEGFR inhibitor) enhances paclitaxel's antiproliferative and apoptotic effects in breast carcinoma cells |

---

## Australia Market Information

According to this evidence pack, Paclitaxel currently has **no ARTG entries recorded** and is listed as **not marketed** in Australia (total licenses: 0). Given that paclitaxel is a long-established, internationally used chemotherapy agent, this market status should be independently verified against the current TGA ARTG database before any regulatory or clinical decision is made, as it appears inconsistent with paclitaxel's well-known global availability.

---

## Cytotoxicity

Paclitaxel is a conventional cytotoxic chemotherapy agent (taxane class), meeting the antineoplastic classification criteria based on its established pharmacological class and its use exclusively against malignant solid tumours across all candidate indications in this evidence pack.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Taxane class — microtubule-stabilising antimitotic agent) |
| Myelosuppression Risk | High — neutropenia is the dose-limiting toxicity for paclitaxel; thrombocytopenia and anaemia are also commonly reported, particularly with dose-dense regimens |
| Emetogenicity Classification | Low to moderate (per standard oncology emetogenic-risk classifications for IV taxane monotherapy) |
| Monitoring Items | Full blood count with differential (neutrophil nadir), liver function tests, peripheral neuropathy assessment, and observation for hypersensitivity reactions during infusion |
| Handling Protection | Yes — standard cytotoxic drug handling precautions apply (personal protective equipment, closed-system transfer devices, spill management) |

*Note: specific toxicity/monitoring data was not available in this evidence pack's safety fields; the above reflects established pharmacological class knowledge for taxanes. Please cross-check against the TGA-approved Product Information once available.*

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No key warnings, contraindications, or drug-drug interaction data were available in this evidence pack, and this represents a **Blocking** data gap (DG001) that prevents completion of the initial safety assessment (S1) for this candidate.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The clinical trial and literature evidence for paclitaxel in female breast carcinoma is extensive and high-quality (L1), including pivotal Phase 3 trials such as CALGB 9344. However, this evidence largely confirms an already well-established global indication rather than validating a novel repurposing hypothesis, and critical Australian regulatory and safety data (TGA PI, ARTG status, mechanism of action) are currently missing from this record.

**To proceed, the following is needed:**
- Obtain the TGA-approved Product Information (PI) for Paclitaxel to complete the safety pre-assessment (S1) — currently a **Blocking** data gap (DG001)
- Verify the drug's actual ARTG registration status in Australia, as "not marketed / 0 entries" appears inconsistent with paclitaxel's well-documented global clinical use
- Source formal mechanism of action (MOA) documentation from DrugBank or equivalent to complete the mechanistic-relevance analysis (DG002)
- Clarify with clinical/regulatory stakeholders whether this candidate should be handled under a standard registration/label-extension pathway rather than a novel drug-repurposing pathway, given that breast carcinoma is an established use of paclitaxel internationally
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

