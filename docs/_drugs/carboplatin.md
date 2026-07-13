---
layout: default
title: Carboplatin
parent: 僅模型預測 (L5)
nav_order: 125
evidence_level: L5
indication_count: 10
---

# Carboplatin
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

# Carboplatin: From Solid Tumour Chemotherapy to Female Breast Carcinoma

## One-Sentence Summary

Carboplatin is a platinum-based cytotoxic chemotherapy agent with established use in solid tumour regimens worldwide, including ovarian, lung, and head and neck cancers, though it currently holds no ARTG registration in Australia.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma** — particularly triple-negative breast cancer (TNBC) and BRCA-mutated subtypes — with **50 clinical trials** and **20 publications** currently supporting this direction.
The prediction achieves a score of **99.86%**, supported by the highest available evidence classification (L1), including multiple completed Phase 3 RCTs directly testing carboplatin in breast cancer.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current ARTG data (0 entries); carboplatin is a globally established platinum-based antineoplastic agent used in ovarian, lung, and head and neck cancers |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L1 |
| Australia Market Status | Not currently marketed (0 ARTG entries) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Carboplatin is a second-generation platinum compound that works by forming **DNA inter-strand and intra-strand crosslinks** — covalent bonds that physically tangle the two strands of the DNA double helix, preventing replication and triggering programmed cell death (apoptosis). Unlike its predecessor cisplatin, carboplatin causes significantly less nephrotoxicity and neurotoxicity, making it more practical in outpatient and combination settings. Its dose-limiting toxicity is thrombocytopenia rather than renal damage, and dosing is individualised using the Calvert formula based on renal function (target AUC × [GFR + 25]).

The mechanistic link to breast cancer is strongest in the **triple-negative breast cancer (TNBC)** subtype. TNBC cells lack oestrogen receptor (ER), progesterone receptor (PR), and HER2 expression, meaning hormone-directed therapies and trastuzumab are ineffective. These tumours depend more heavily on functional DNA damage repair to survive — a dependency that carboplatin directly exploits. When TNBC tumours harbour **BRCA1/2 mutations** or harbour homologous recombination deficiency (HRD) more broadly, carboplatin's crosslinking mechanism induces **synthetic lethality**: cells already compromised in their ability to repair double-strand DNA breaks are overwhelmed by platinum-induced damage and die selectively. This mechanistic rationale is well-characterised and widely accepted in oncology.

Multiple Phase 3 randomised trials directly validate this reasoning. The "Triple Negative Trial" (NCT00532727, n=400) is the landmark head-to-head RCT comparing carboplatin against docetaxel specifically in TNBC patients. The BROCADE3 trial (PMID 38309017) demonstrated a statistically significant progression-free survival benefit when adding veliparib (a PARP inhibitor) to carboplatin plus paclitaxel in germline BRCA-mutated HER2-negative advanced breast cancer. A meta-analysis (PMID 25247558) confirmed that carboplatin independently improves pathological complete response (pCR) rates when added to neoadjuvant regimens in TNBC. Taken together, the mechanistic rationale, subtype selectivity, and clinical trial evidence make this one of the most strongly supported TxGNN predictions in this dataset.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---|---|---|---|---|
| [NCT00532727](https://clinicaltrials.gov/study/NCT00532727) | Phase 3 | Unknown | 400 | **Triple Negative Trial**: Primary landmark RCT directly comparing carboplatin vs docetaxel in patients with ER−, PR−, HER2− metastatic or recurrent locally advanced breast cancer; the highest-grade direct evidence for carboplatin's single-agent activity in TNBC |
| [NCT03168880](https://clinicaltrials.gov/study/NCT03168880) | Phase 3 | Active, not recruiting | 720 | RCT of neoadjuvant weekly paclitaxel vs weekly paclitaxel plus weekly carboplatin in locally advanced TNBC; directly evaluates the incremental benefit of adding carboplatin to standard neoadjuvant taxane therapy |
| [NCT02003209](https://clinicaltrials.gov/study/NCT02003209) | Phase 3 | Completed | 315 | Phase 3 RCT of TCHP (docetaxel, carboplatin, trastuzumab, pertuzumab) ± oestrogen deprivation in HR+/HER2+ locally advanced breast cancer; carboplatin is a core backbone agent; completed with data to June 2025 |
| [NCT00047255](https://clinicaltrials.gov/study/NCT00047255) | Phase 3 | Completed | 263 | Docetaxel + trastuzumab ± carboplatin as first-line therapy for HER2-amplified advanced breast cancer; establishes context for platinum use in HER2+ disease |
| [NCT02978495](https://clinicaltrials.gov/study/NCT02978495) | Phase 2 | Completed | 154 | **NACATRINE Trial**: Prospective Phase 2 study of neoadjuvant carboplatin in Brazilian women with TNBC; directly assesses pCR rates with carboplatin-containing regimens in this subtype |
| [NCT00321633](https://clinicaltrials.gov/study/NCT00321633) | Phase 2 | Completed | 148 | Pilot RCT of carboplatin vs docetaxel specifically in patients with metastatic **BRCA-mutated** breast cancer; pivotal trial characterising carboplatin's activity in hereditary breast cancer |
| [NCT05843292](https://clinicaltrials.gov/study/NCT05843292) | Phase 4 | Not yet recruiting | 48 | Short-term sintilimab (anti-PD-1) + taxane + carboplatin for neoadjuvant therapy in early-stage TNBC; directly validates carboplatin's role in current combination immuno-chemotherapy paradigms |
| [NCT06027268](https://clinicaltrials.gov/study/NCT06027268) | Phase 2 | Active, not recruiting | 36 | **ToPCourT Trial**: Trilaciclib + pembrolizumab + gemcitabine + carboplatin in locally advanced unresectable or metastatic TNBC; explores CDK4/6-mediated myeloprotection alongside carboplatin backbone |
| [NCT00232505](https://clinicaltrials.gov/study/NCT00232505) | Phase 2 | Completed | 112 | Cetuximab alone vs cetuximab + carboplatin in ER−, PR−, HER2-negative metastatic breast cancer; one of the earliest trials defining carboplatin activity in molecularly-characterised TNBC |
| [NCT00117442](https://clinicaltrials.gov/study/NCT00117442) | Phase 2 | Completed | 61 | Multi-cycle dose-intensive carboplatin/paclitaxel supported by pegfilgrastim and haematopoietic progenitor cell re-infusion in advanced breast cancer; dose-finding data supporting high-intensity platinum regimens |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|---|---|---|---|---|
| [38309017](https://pubmed.ncbi.nlm.nih.gov/38309017/) | 2024 | RCT | Eur J Cancer | **BROCADE3 final OS data**: Veliparib + carboplatin + paclitaxel vs placebo + carboplatin + paclitaxel in germline BRCA1/2-mutated, HER2-negative advanced breast cancer; PFS benefit confirmed, OS trends reported |
| [39671272](https://pubmed.ncbi.nlm.nih.gov/39671272/) | 2025 | RCT | JAMA | **CamRelief trial**: Camrelizumab (anti-PD-1) + neoadjuvant chemotherapy including platinum in early/locally advanced TNBC; platinum backbone integral to the 4-drug neoadjuvant regimen tested |
| [25247558](https://pubmed.ncbi.nlm.nih.gov/25247558/) | 2014 | Meta-analysis | PLoS ONE | Meta-analysis confirming carboplatin independently improves pathological complete response (pCR) rates in neoadjuvant treatment of TNBC; strongest pooled evidence for carboplatin's neoadjuvant benefit |
| [16720915](https://pubmed.ncbi.nlm.nih.gov/16720915/) | 2006 | Systematic Review | Med Oncol | Systematic review of paclitaxel-carboplatin combination in advanced breast cancer; accumulating evidence for synergy, efficacy, and safety across multiple Phase 2 datasets |
| [40817986](https://pubmed.ncbi.nlm.nih.gov/40817986/) | 2025 | RCT | Breast Cancer Res Treat | Randomised Phase 2: Single-agent carboplatin vs carboplatin + everolimus in advanced TNBC; explores mTOR inhibition to overcome carboplatin resistance via PTEN-loss/mTOR activation |
| [9516604](https://pubmed.ncbi.nlm.nih.gov/9516604/) | 1998 | Phase 2 Trial | Oncology | Phase 2 study of paclitaxel + carboplatin (AUC 6) every 3 weeks as first-line therapy in 66 patients with advanced breast cancer; established the standard dosing combination still referenced today |
| [8893899](https://pubmed.ncbi.nlm.nih.gov/8893899/) | 1996 | Phase 2 Trial | Semin Oncol | Early evaluation of paclitaxel alone, carboplatin alone, and their combination in advanced breast cancer; established the initial rationale and preliminary safety profile for combination use |
| [39944694](https://pubmed.ncbi.nlm.nih.gov/39944694/) | 2025 | Retrospective Cohort | Front Immunol | DNA damage repair (DDR) gene signature associated with carboplatin resistance in breast cancer; identifies immune infiltration patterns and drug sensitivity correlates relevant to patient selection |
| [33256829](https://pubmed.ncbi.nlm.nih.gov/33256829/) | 2020 | Phase 2 Trial | Breast Cancer Res | Phase 2 trial of carboplatin + bevacizumab in breast cancer brain metastases; addresses an underserved high-risk clinical scenario with direct carboplatin activity data |
| [40593759](https://pubmed.ncbi.nlm.nih.gov/40593759/) | 2025 | RCT | Nat Commun | **MUKDEN 06 trial**: ARX788 + pyrotinib vs TCbHP (docetaxel + carboplatin + trastuzumab + pertuzumab) in neoadjuvant HER2+ breast cancer; carboplatin-containing TCbHP serves as the active comparator, confirming its benchmark status |

---

## Australia Market Information

Carboplatin currently has **no products registered in the ARTG** (Australian Register of Therapeutic Goods). The ARTG query conducted on 9 March 2026 returned 0 active entries. This means carboplatin does not have a currently approved product label or Product Information (PI) document available through standard TGA registration pathways.

> **For clinical use in Australia**, carboplatin would need to be accessed through one of the following pathways:
> - **TGA Special Access Scheme (SAS) — Category B**: Approval for use in an individual patient not enrolled in a clinical trial
> - **Clinical Trial Notification (CTN) or Clinical Trial Approval (CTA)**: For use within a registered clinical trial
> - **Hospital formulary arrangements**: Some hospital pharmacy systems maintain access to unregistered products under institutional governance frameworks
>
> Clinicians are advised to verify current availability and access pathways directly with the TGA (www.tga.gov.au) and their institutional pharmacy department.

---

## Cytotoxicity

Carboplatin meets criteria for this section: it is a conventional cytotoxic platinum compound used in antineoplastic chemotherapy regimens.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Platinum-based alkylating-like agent (CBDCA; *cis*-diammine[1,1-cyclobutanedicarboxylato]platinum II) |
| Myelosuppression Risk | **High** — Thrombocytopenia is the primary dose-limiting toxicity of carboplatin and is more pronounced than with cisplatin. Neutropenia and anaemia are also common. Grade 3/4 thrombocytopenia occurs frequently, particularly at AUC ≥6 or in combination regimens. TCHP regimens (docetaxel + carboplatin + trastuzumab + pertuzumab) have documented Grade 3/4 anaemia rates requiring dose reduction guidance (PMID 35837812) |
| Emetogenicity Classification | **Moderate** — Carboplatin is classified as a moderately emetogenic agent (AUC ≥4 may approach highly emetogenic threshold). Prophylactic antiemetics (5-HT3 antagonist ± dexamethasone) are recommended for all patients prior to administration |
| Monitoring Items | Full blood count (FBC) with differential and platelet count before each cycle (nadir typically Day 21); serum creatinine and eGFR before each cycle (required for Calvert formula dose calculation); liver function tests; audiometry for high-dose regimens (particularly paediatric or salvage HDCT settings) |
| Handling Protection | Must be handled in accordance with cytotoxic drug handling regulations (AS/NZS 4187 and institutional cytotoxic safety policies). Preparation must occur in a biological safety cabinet (BSC Class II) by trained pharmacy personnel wearing appropriate PPE. Administration by trained oncology nursing staff using closed-system drug transfer devices (CSTDs) is recommended |

---

## Safety Considerations

As carboplatin has no current ARTG registration, no TGA-approved Australian Product Information (PI) is available. Please refer to the **manufacturer's global Product Information document** (accessible through TGA SAS documentation) and established clinical guidelines such as:

- **eviQ Cancer Treatments Online** (Cancer Institute NSW): [www.eviq.org.au](https://www.eviq.org.au) — the primary Australian reference for carboplatin dosing protocols
- **NCCN Clinical Practice Guidelines in Oncology — Breast Cancer** (National Comprehensive Cancer Network)
- **ESMO Clinical Practice Guidelines** for early and metastatic breast cancer

Key safety considerations known from established clinical practice and published trial data include:

- **Myelosuppression** (especially thrombocytopenia) is the principal dose-limiting toxicity; platelet nadir typically occurs at Day 21 of each cycle
- **Renal function dependency**: All dosing is calculated using the Calvert formula; eGFR must be assessed before each cycle; dose reduction required if eGFR falls during treatment
- **Hypersensitivity reactions**: Can occur with repeat exposure (reported in 1–2% of patients per cycle, increasing with cumulative exposure); cross-sensitivity with cisplatin exists; emergency management protocols should be in place
- **Ototoxicity**: Relevant at high cumulative doses and in high-dose chemotherapy (HDCT) salvage regimens; hearing assessment recommended for patients receiving multiple cycles (PMID 37715631)
- **Peripheral neuropathy**: Less pronounced than with cisplatin or paclitaxel when used as monotherapy, but may be additive in combination regimens

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for carboplatin in female breast carcinoma — particularly TNBC and BRCA-mutated subtypes — is among the strongest in this dataset, meeting L1 criteria with multiple completed Phase 3 RCTs, large ongoing Phase 3 trials (combined n>1,400), and consistent meta-analytic confirmation of pathological complete response benefit. The mechanistic rationale via BRCA-mediated synthetic lethality is well-established and widely accepted. The absence of ARTG registration represents a regulatory access barrier, not an efficacy or safety concern, and carboplatin is used as a standard-of-care component in breast cancer regimens internationally.

**To proceed, the following is needed:**

- **Regulatory access pathway**: Confirm access via TGA Special Access Scheme (SAS Category B) or clinical trial enrolment; engage institutional pharmacy for procurement arrangements
- **Patient selection criteria**: Confirm BRCA1/2 germline mutation status or BRCA-like HRD tumour profile before preferentially selecting carboplatin over alternative agents; benefit is strongly subtype-dependent (TNBC ≥ BRCA-mutated HER2− > HR+/HER2+)
- **Dose protocol establishment**: Adopt Calvert formula dosing (Target AUC × [measured GFR + 25]); define AUC target per combination regimen (typically AUC 5–6 with paclitaxel; AUC 2 weekly in some regimens)
- **Cycle safety monitoring plan**: Pre-cycle FBC, platelet count, and renal function; define institutional thresholds for dose modification or delay based on thrombocytopenia grade
- **Cytotoxic handling infrastructure**: Confirm BSC availability, pharmacy compounding capacity, and nursing cytotoxic administration protocols are in place before first patient use
- **Mechanism of action data**: Detailed DrugBank MOA documentation would strengthen future regulatory submissions and pharmacist-facing communications (currently a data gap)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

