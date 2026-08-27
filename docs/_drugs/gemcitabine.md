---
layout: default
title: Gemcitabine
parent: 僅模型預測 (L5)
nav_order: 308
evidence_level: L5
indication_count: 10
---

# Gemcitabine
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

# Gemcitabine: From Antimetabolite Chemotherapy to Female Breast Carcinoma

## One-Sentence Summary

Gemcitabine is a deoxycytidine-analogue antimetabolite chemotherapy agent (DrugBank DB00441); this evidence pack does not contain Australian licensing records specifying its original approved indication (0 ARTG entries on file, market status "Not Marketed"), so the original-indication field below reflects general pharmacological knowledge, not TGA data. The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, with roughly **50 clinical trials** and **20 publications** identified in this dataset supporting the direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in this evidence pack — no ARTG licences on record. (Gemcitabine is internationally established as a cytotoxic antimetabolite used across pancreatic cancer, NSCLC and other solid tumours; this is general background, not sourced from this pack.) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, a detailed mechanism-of-action record was not returned for this pack (flagged as a High-severity data gap, DG002). Based on known pharmacology, gemcitabine is a deoxycytidine (pyrimidine nucleoside) analogue that inhibits ribonucleotide reductase and is incorporated into DNA, causing chain termination — a broad-spectrum, cell-cycle-specific (S-phase) antimetabolite mechanism.

This mechanism is not indication-specific: antimetabolite/DNA-synthesis-disrupting chemotherapy is active across a wide range of solid tumours, which is consistent with gemcitabine's known off-label and combination use in multiple cancer types. Notably, gemcitabine plus paclitaxel is already an internationally recognised combination regimen for metastatic breast cancer, meaning the TxGNN prediction aligns with existing global clinical practice rather than proposing an entirely novel mechanistic hypothesis.

The key caveat is regulatory, not mechanistic: this evidence pack shows gemcitabine as **not currently marketed in Australia** (0 ARTG entries), so before any breast-cancer repurposing pathway could be pursued locally, the more fundamental question of TGA market registration would need to be addressed first.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00039546](https://clinicaltrials.gov/study/NCT00039546) | Phase 3 | Unknown | N/A | 'tAnGo' RCT: gemcitabine added to paclitaxel-containing, epirubicin-based adjuvant chemotherapy for ER/PgR-poor early breast cancer |
| [NCT00561119](https://clinicaltrials.gov/study/NCT00561119) | Phase 3 | Completed | 326 | Maintenance vs. observation after 6 cycles of gemcitabine+paclitaxel as 1st-line therapy for metastatic/recurrent breast cancer |
| [NCT00440622](https://clinicaltrials.gov/study/NCT00440622) | Phase 3 | Terminated | 90 | Gemcitabine+trastuzumab vs. capecitabine+trastuzumab in pretreated HER2-positive metastatic breast cancer |
| [NCT00408408](https://clinicaltrials.gov/study/NCT00408408) | Phase 3 | Unknown | 1206 | Neoadjuvant: adding capecitabine or gemcitabine to docetaxel before AC ± bevacizumab, evaluating pathologic complete response |
| [NCT00070278](https://clinicaltrials.gov/study/NCT00070278) | Phase 3 | Unknown | 800 | Neoadjuvant epirubicin/cyclophosphamide + paclitaxel ± gemcitabine in poor-risk early breast cancer |
| [NCT00006459](https://clinicaltrials.gov/study/NCT00006459) | Phase 3 | Completed | N/A | Gemcitabine+paclitaxel vs. paclitaxel alone in unresectable, locally recurrent or metastatic breast cancer |
| [NCT00110084](https://clinicaltrials.gov/study/NCT00110084) | Phase 2 | Completed | 50 | Weekly nab-paclitaxel + gemcitabine in metastatic breast cancer |
| [NCT06027268](https://clinicaltrials.gov/study/NCT06027268) | Phase 2 | Active, not recruiting | 36 | ToPCourT: trilaciclib+pembrolizumab+gemcitabine+carboplatin in locally advanced/metastatic triple-negative breast cancer |
| [NCT00005991](https://clinicaltrials.gov/study/NCT00005991) | Phase 1/2 | Completed | 76 | Gemcitabine + liposomal doxorubicin (Doxil) in advanced solid tumours/breast cancer |
| [NCT02252887](https://clinicaltrials.gov/study/NCT02252887) | Phase 2 | Completed | 45 | Gemcitabine+trastuzumab+pertuzumab in metastatic HER2-positive breast cancer after prior anti-HER2 therapy |

No ANZCTR-registered trials were identified for this indication in the pack.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12138397](https://pubmed.ncbi.nlm.nih.gov/12138397/) | 2002 | Review | Seminars in Oncology | Gemcitabine as single agent and in combination shows 16–37% response rates in metastatic breast cancer across ~20 phase II trials |
| [14754468](https://pubmed.ncbi.nlm.nih.gov/14754468/) | 2004 | Review/Clinical experience | Clinical Breast Cancer | Gemcitabine+platinum combinations in anthracycline/taxane-pretreated breast cancer |
| [14719116](https://pubmed.ncbi.nlm.nih.gov/14719116/) | 2004 | Review | International Journal of Oncology | Rationale for the use of gemcitabine in breast cancer |
| [15685819](https://pubmed.ncbi.nlm.nih.gov/15685819/) | 2004 | Review | Oncology (Williston Park) | Gemcitabine+paclitaxel in metastatic breast cancer — dosing schedules and phase II/III response rates |
| [15685820](https://pubmed.ncbi.nlm.nih.gov/15685820/) | 2004 | Review | Oncology (Williston Park) | Gemcitabine+docetaxel in metastatic breast cancer — combination rationale and regimens |
| [15685821](https://pubmed.ncbi.nlm.nih.gov/15685821/) | 2004 | Review/Clinical experience | Oncology (Williston Park) | Gemcitabine and platinum-based chemotherapy in metastatic breast cancer |
| [15685824](https://pubmed.ncbi.nlm.nih.gov/15685824/) | 2004 | Review | Oncology (Williston Park) | Gemcitabine with trastuzumab and/or platinum salts in HER2-overexpressing breast cancer |
| [12057038](https://pubmed.ncbi.nlm.nih.gov/12057038/) | 2002 | Review | Clinical Breast Cancer | Overview: gemcitabine as single-agent therapy for advanced breast cancer |
| [12722022](https://pubmed.ncbi.nlm.nih.gov/12722022/) | 2003 | Review/Trial summary | Seminars in Oncology | Gemcitabine+trastuzumab phase II trial in heavily pretreated metastatic breast cancer |
| [25398698](https://pubmed.ncbi.nlm.nih.gov/25398698/) | 2015 | Clinical study | Cancer Chemotherapy and Pharmacology | Docetaxel+gemcitabine+bevacizumab as salvage therapy for HER2-negative metastatic breast cancer |

## Australia Market Information

Gemcitabine currently has no ARTG-registered products on file in this evidence pack (market status: Not Marketed; total licences: 0). Australian marketing/registration status would need to be established as a separate step from the indication-repurposing assessment.

## Cytotoxicity

Gemcitabine is a cytotoxic antineoplastic agent (pyrimidine nucleoside analogue/antimetabolite class), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic chemotherapy (nucleoside analogue / antimetabolite class) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the Product Information (PI) warnings and precautions |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

Detailed toxicity/monitoring data was not returned for this pack — TGA warnings and contraindications are logged as a Blocking data gap (DG001), so specifics above should not be inferred beyond drug-class classification.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No key warnings, contraindications, or drug interaction data were returned in this evidence pack (DDI query status: not found).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 3 RCTs (NCT00561119, NCT00006459) plus multiple additional Phase 2/3 trials and supportive review literature give strong (L1) evidence that gemcitabine-containing regimens are active in breast cancer, consistent with gemcitabine+paclitaxel already being an internationally used combination. However, gemcitabine is not currently marketed in Australia per this pack, and formal safety/PI data is missing.

**To proceed, the following is needed:**
- TFDA/TGA-approved Product Information (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism-of-action documentation from DrugBank (DG002)
- Clarification of Australian market/registration pathway, since 0 ARTG entries are on file
- Formal relevance triage of the "pending" clinical-trial and literature entries in this pack to confirm which are breast-cancer-specific vs. tangential (e.g. urothelial carcinoma trials appearing under this indication)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

