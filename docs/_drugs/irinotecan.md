---
layout: default
title: Irinotecan
parent: 僅模型預測 (L5)
nav_order: 274
evidence_level: L5
indication_count: 10
---

# Irinotecan
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

# Irinotecan: From Colorectal Cancer to Female Breast Carcinoma

## One-Sentence Summary

Irinotecan is a topoisomerase I inhibitor used internationally as a core component of FOLFIRI and FOLFIRINOX regimens for colorectal and pancreatic cancers, though it is not currently registered in Australia.
The TxGNN model predicts it may be effective for **female breast carcinoma**, with **22 clinical trials** and **20 publications** currently supporting this direction.
Evidence is particularly compelling given that its active metabolite SN-38 is the cytotoxic payload of sacituzumab govitecan — an FDA-approved antibody-drug conjugate for both triple-negative and HR+/HER2− metastatic breast cancer.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Australia (TGA); internationally indicated for colorectal cancer (FOLFIRI/FOLFIRINOX), gastric cancer, and small cell lung cancer |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Irinotecan is a semisynthetic camptothecin analogue that acts as a prodrug. It is converted by carboxylesterases — primarily in the liver and tumour tissue — to its active metabolite SN-38, which inhibits topoisomerase I by stabilising the enzyme-DNA cleavage complex. This prevents the re-ligation of single-strand DNA breaks during replication, inducing double-stranded DNA breaks in the S-phase of cell division. Because rapidly dividing cancer cells are disproportionately affected, this mechanism has broad antitumour potential across many solid tumour types. Notably, UGT1A1 mediates hepatic glucuronidation of SN-38; patients with UGT1A1\*28 homozygosity (7/7 genotype) have significantly reduced clearance and are at heightened risk of severe toxicity, making pre-dose genotyping essential.

The mechanistic link to breast cancer is most powerfully validated through the clinical success of sacituzumab govitecan (SG), an anti-Trop-2 antibody-drug conjugate that delivers SN-38 directly to Trop-2-expressing tumour cells. SG has received FDA approval for metastatic triple-negative breast cancer (ASCENT trial, PMID 30786188) and HR+/HER2− endocrine-resistant metastatic breast cancer (TROPiCS-02, PMID 36027558), establishing that the cytotoxic payload of irinotecan has definitive clinical activity in breast cancer across molecular subtypes. Trop-2 is overexpressed in the majority of breast tumours, providing a biological explanation for why SN-38 delivery is particularly efficacious in this setting.

Beyond the ADC evidence, direct clinical studies of irinotecan itself in breast cancer have been conducted. A Phase 2 trial (NCT03562390, n=124) evaluated irinotecan monotherapy in patients with anthracycline- and taxane-refractory locally recurrent or metastatic breast cancer. A Phase 1 study of nanoliposomal irinotecan (Nal-IRI/MM-398; NCT01770353, n=45) directly characterised tumour drug biodistribution in breast cancer patients using ferumoxytol MRI, confirming accumulation of the irinotecan-class compound in breast tumour tissue. The 2026 PHENOMENAL Phase 2 study (PMID 41371050) further demonstrated that liposomal irinotecan crosses the blood-brain barrier and has antitumour activity in HER2-negative breast cancer patients with brain metastases — an area of high unmet clinical need.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03562390](https://clinicaltrials.gov/study/NCT03562390) | Phase 2 | Unknown | 124 | Direct irinotecan monotherapy in patients with anthracycline- and taxane-refractory locally recurrent or metastatic breast cancer (≥3rd-line); highest-priority direct efficacy study — outcome data should be confirmed if published |
| [NCT01770353](https://clinicaltrials.gov/study/NCT01770353) | Phase 1 | Completed | 45 | MM-398 (nanoliposomal irinotecan/Nal-IRI) Phase 1 in solid tumours; characterised tumour drug biodistribution in breast cancer patients using ferumoxytol MRI, confirming irinotecan-class accumulation in breast tumour tissue |
| [NCT01631552](https://clinicaltrials.gov/study/NCT01631552) | Phase 1/2 | Completed | 515 | Sacituzumab govitecan (anti-Trop-2 antibody conjugated to SN-38, irinotecan's active metabolite) in epithelial cancers including TNBC; pivotal study underpinning FDA approval for metastatic breast cancer |
| [NCT00072852](https://clinicaltrials.gov/study/NCT00072852) | Phase 2 | Completed | 134 | Randomised Phase 2 comparing two irinotecan oral capsule schedules (5-day vs 14-day in 21-day cycles) in metastatic breast cancer refractory to anthracycline, taxane, and capecitabine |
| [NCT00031681](https://clinicaltrials.gov/study/NCT00031681) | Phase 1 | Completed | 41 | UCN-01 (7-hydroxystaurosporine, checkpoint kinase inhibitor) plus irinotecan; Part II specifically enrolled triple-negative breast cancer, evaluating synergistic DNA-damage checkpoint abrogation with topoisomerase I inhibition |
| [NCT02033551](https://clinicaltrials.gov/study/NCT02033551) | Phase 1 | Completed | 47 | Extension safety study of veliparib (PARP inhibitor) combined with FOLFIRI (containing irinotecan) in solid tumours; provides combination safety data relevant to PARP inhibitor + irinotecan strategies in breast cancer |
| [NCT05453825](https://clinicaltrials.gov/study/NCT05453825) | Phase 2 | Unknown | 180 | Navicixizumab (anti-DLL4/VEGF bispecific antibody) combined with paclitaxel or irinotecan across solid tumour cohorts; Cohort C specifically evaluates irinotecan combination in triple-negative breast cancer |
| [NCT00083148](https://clinicaltrials.gov/study/NCT00083148) | Phase 1 | Completed | 12 | Irinotecan followed by capecitabine in advanced breast carcinoma; studied whether irinotecan sensitises tumour cells to capecitabine via topoisomerase I upregulation |
| [NCT02419495](https://clinicaltrials.gov/study/NCT02419495) | Phase 1 | Terminated | 221 | Selinexor (XPO1 nuclear export inhibitor) combined with multiple standard chemotherapy regimens including FOLFIRI (irinotecan-based) in advanced malignancies; provides additional safety dataset for irinotecan combination therapy |
| [NCT04640480](https://clinicaltrials.gov/study/NCT04640480) | Phase 1 | Completed | 21 | SNB-101, a novel polymeric nanoparticle formulation of SN-38 (irinotecan's active metabolite), dose escalation in advanced solid tumours; explores next-generation delivery strategies |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30786188](https://pubmed.ncbi.nlm.nih.gov/30786188/) | 2019 | Phase 3 RCT | N Engl J Med | ASCENT trial: sacituzumab govitecan vs single-agent chemotherapy in mTNBC; significantly improved PFS and OS; FDA approval basis — highest-level validation that SN-38 (irinotecan metabolite) is clinically active in breast cancer |
| [36027558](https://pubmed.ncbi.nlm.nih.gov/36027558/) | 2022 | Phase 3 RCT | J Clin Oncol | TROPiCS-02: sacituzumab govitecan vs chemotherapy in HR+/HER2− endocrine-resistant MBC; improved PFS and OS; confirms SN-38 efficacy extends beyond TNBC to luminal breast cancer subtypes |
| [36302269](https://pubmed.ncbi.nlm.nih.gov/36302269/) | 2022 | Systematic Review | Breast | Comprehensive review of TROP-2-directed ADCs incorporating SN-38 in metastatic breast cancer; contextualises irinotecan payload utility across HER2-negative subtypes and summarises development history |
| [28291390](https://pubmed.ncbi.nlm.nih.gov/28291390/) | 2017 | Phase 1/2 | J Clin Oncol | Sacituzumab govitecan in heavily pretreated mTNBC: 33.3% ORR, median PFS 5.5 months; landmark early validation of SN-38 anti-Trop-2 delivery in relapsed/refractory TNBC prior to Phase 3 |
| [41371050](https://pubmed.ncbi.nlm.nih.gov/41371050/) | 2026 | Phase 2 | Eur J Cancer | PHENOMENAL trial: liposomal irinotecan (nal-IRI) in HER2-negative breast cancer with brain metastases; demonstrates blood-brain barrier penetration and antitumour activity in a high-unmet-need population |
| [32223649](https://pubmed.ncbi.nlm.nih.gov/32223649/) | 2020 | Phase 3 Protocol | Future Oncol | TROPiCS-02 trial design publication; describes mechanism of SN-38 delivery via pH-hydrolysable linker and biological rationale for Trop-2 targeting in HR+/HER2− MBC |
| [31208270](https://pubmed.ncbi.nlm.nih.gov/31208270/) | 2019 | Review | mAbs | Detailed review of anti-Trop-2 sacituzumab govitecan development; describes irinotecan-to-SN-38 conversion, topoisomerase I inhibition, and ADC design rationale |
| [28558150](https://pubmed.ncbi.nlm.nih.gov/28558150/) | 2017 | Phase 1/2 | Cancer | Sacituzumab govitecan multi-cycle safety and pharmacokinetics at 8–10 mg/kg in diverse epithelial cancers; establishes clinical pharmacology of SN-38 ADC across tumour types including breast cancer |
| [12800602](https://pubmed.ncbi.nlm.nih.gov/12800602/) | 2003 | Review | Oncology | Mechanistic rationale for mitomycin + irinotecan in hormone-refractory advanced breast cancer; documents that mitomycin upregulates topoisomerase I (irinotecan's target), establishing synergism basis |
| [9726101](https://pubmed.ncbi.nlm.nih.gov/9726101/) | 1998 | Review | Oncology | Early review of irinotecan antitumour activity spectrum; documented Phase 2 activity in breast, pancreatic, ovarian, and small cell lung cancers, establishing the breadth of irinotecan's clinical reach |

---

## Australia Market Information

Irinotecan is **not currently registered** on the Australian Register of Therapeutic Goods (ARTG). There are no ARTG entries for irinotecan in any dosage form, and it is not available on the Australian market through standard channels.

Internationally, irinotecan is marketed as Camptosar® (Pfizer) in the United States for metastatic colorectal cancer in combination regimens, and liposomal irinotecan (Onivyde®) is FDA-approved for metastatic pancreatic ductal adenocarcinoma. Any clinical application in Australia would require one of the following pathways: Special Access Scheme (SAS) Category B authorisation, Authorised Prescriber (AP) designation, or a formal TGA registration application.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Camptothecin class (Topoisomerase I inhibitor / DNA strand-break-inducing agent) |
| Myelosuppression Risk | High — severe neutropenia (including febrile neutropenia) is a dose-limiting toxicity; risk is substantially increased in patients with UGT1A1\*28 homozygosity due to impaired SN-38 clearance; thrombocytopenia is less common |
| Emetogenicity Classification | Moderate emetogenic potential — both acute cholinergic diarrhoea (early onset, within 24 hours) and delayed secretory diarrhoea (>24 hours post-dose) can occur; prophylactic 5-HT3 antagonist antiemetics recommended |
| Monitoring Items | FBC with differential (ANC and platelet count), liver function tests (ALT, AST, bilirubin), renal function, electrolytes; **UGT1A1 genotyping is strongly recommended prior to first dose**; daily diarrhoea assessment with graded management protocol |
| Handling Protection | Must be handled in accordance with SHPA Standards of Practice for the Handling of Cytotoxic Drugs; biological safety cabinet for preparation, appropriate PPE (double gloves, gown, eye protection), cytotoxic waste disposal per state/territory regulations |

---

## Safety Considerations

Irinotecan is not registered in Australia and no TGA-approved Product Information (PI) is available. Please refer to the US FDA Prescribing Information (Camptosar®) or EMA Summary of Product Characteristics for comprehensive safety data.

The following considerations are particularly critical for clinical decision-making:

- **Severe Diarrhoea (Potentially Life-threatening)**: Irinotecan causes both early (cholinergic, within 24 hours — managed with IV atropine 0.25–1 mg) and late (secretory, starting >24 hours after administration — managed with high-dose loperamide 4 mg immediately then 2 mg every 2 hours until diarrhoea-free for 12 hours) forms. Late diarrhoea has been fatal when inadequately managed.
- **Severe Neutropenia and Febrile Neutropenia**: A primary dose-limiting toxicity; septic deaths have occurred. G-CSF secondary prophylaxis protocols and clear criteria for dose delays/reductions are essential.
- **UGT1A1 Polymorphism (Critical Safety Requirement)**: Patients homozygous for UGT1A1\*28 (Gilbert's syndrome genotype, 7/7) have substantially impaired glucuronidation of SN-38, resulting in markedly elevated SN-38 plasma exposure and a significantly higher risk of Grade 3–4 neutropenia and diarrhoea. Prospective UGT1A1 genotyping and dose reduction are required in this population before commencing irinotecan therapy.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction of irinotecan efficacy in female breast carcinoma is strongly supported by FDA approval of sacituzumab govitecan — an SN-38-based antibody-drug conjugate — for both triple-negative and HR+/HER2− metastatic breast cancer, providing the highest-level mechanistic validation that the cytotoxic payload of irinotecan is definitively active in breast cancer. Direct Phase 2 evidence for irinotecan monotherapy in refractory metastatic breast cancer (NCT03562390, n=124) and the 2026 PHENOMENAL Phase 2 data in brain metastases further confirm clinical plausibility across treatment contexts.

**To proceed, the following is needed:**
- **Regulatory pathway**: Determine appropriate TGA access mechanism — irinotecan has no ARTG entry; Special Access Scheme, Authorised Prescriber, or full TGA registration submission required before any Australian patient use
- **UGT1A1 genotyping protocol**: Mandatory pre-treatment testing to identify patients at high risk of severe toxicity; dose-adjustment algorithm must be pre-specified in any clinical protocol
- **Safety documentation**: Complete safety evaluation using US FDA Camptosar® Prescribing Information and EMA SmPC; Australian PI preparation required if pursuing TGA registration
- **Formulation strategy decision**: Clarify whether the target indication is best served by conventional irinotecan, nanoliposomal irinotecan (Nal-IRI/Onivyde®), or by formally supporting an SN-38-based ADC pathway — the strongest clinical evidence currently sits with the ADC approach (sacituzumab govitecan)
- **NCT03562390 outcome verification**: Confirm whether final results of the direct Phase 2 irinotecan monotherapy trial in metastatic breast cancer have been published; this data would upgrade or confirm the current L2 evidence classification
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

