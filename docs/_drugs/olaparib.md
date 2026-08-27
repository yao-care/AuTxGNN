---
layout: default
title: Olaparib
parent: 僅模型預測 (L5)
nav_order: 488
evidence_level: L5
indication_count: 10
---

# Olaparib
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

# Olaparib: From Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Olaparib is an oral PARP1/2 inhibitor originally developed for BRCA-mutated, platinum-sensitive ovarian cancer maintenance therapy. The TxGNN model predicts it may also be effective for **Female Breast Carcinoma**, with **50 clinical trials** and **20 publications** currently supporting this direction — including two completed Phase 3 randomised controlled trials (OlympiA, OlympiAD).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian cancer (BRCA-mutated, platinum-sensitive) — per trial-context literature in this pack; not independently confirmed via an Australian regulatory source |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Olaparib is a PARP1/2 inhibitor. In tumour cells with homologous recombination repair (HRR) deficiency — most notably germline or somatic *BRCA1/2* mutations — PARP inhibition causes synthetic lethality: the cell loses its remaining DNA-repair backup pathway and dies. This mechanism is well established and is not a mechanistic hypothesis unique to this prediction; it is the basis of olaparib's existing oncology use.

Breast and ovarian cancer share the same underlying genetic vulnerability. Approximately 5–10% of breast cancers carry a germline *BRCA1/2* pathogenic variant, and these tumours are mechanistically comparable to *BRCA*-mutated ovarian cancer, olaparib's original target population. This is why the TxGNN prediction is not purely computational extrapolation — it recapitulates a mechanism-disease relationship that has already been validated in large randomised trials (OlympiA for adjuvant early breast cancer, OlympiAD for metastatic breast cancer), both included in the evidence below.

Because the shared molecular driver (HRR/BRCA deficiency) rather than tissue-of-origin determines olaparib's activity, the extension from ovarian to breast cancer is biologically coherent rather than speculative.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04417192](https://clinicaltrials.gov/study/NCT04417192) | Phase 2 | Completed | 30 | Preoperative olaparib monotherapy vs olaparib + pembrolizumab in HRD-positive advanced epithelial ovarian/fallopian tube/peritoneal cancer (note: trial population is ovarian, not breast, despite being flagged under this indication) |
| [NCT06201234](https://clinicaltrials.gov/study/NCT06201234) | Phase 2 | Recruiting | 176 | Addition of elacestrant to olaparib in HR-positive, HER2-negative, gBRCA1/2-mutated advanced breast cancer |
| [NCT05498155](https://clinicaltrials.gov/study/NCT05498155) | Phase 2 | Active, not recruiting | 50 | Neoadjuvant olaparib ± durvalumab in BRCA-mutated, early-stage HER2-negative breast cancer |
| [NCT03109080](https://clinicaltrials.gov/study/NCT03109080) | Phase 1 | Completed | 24 | Olaparib with radiation therapy in inflammatory/locoregionally advanced/metastatic or residual triple-negative breast cancer |
| [NCT02418624](https://clinicaltrials.gov/study/NCT02418624) | Phase 1 | Completed | 25 | Carboplatin-olaparib followed by olaparib monotherapy vs capecitabine as first-line treatment in BRCA1/2-mutated HER2-negative advanced breast cancer |
| [NCT01445418](https://clinicaltrials.gov/study/NCT01445418) | Phase 1 | Completed | 103 | Olaparib (AZD2281) + carboplatin dose-finding in BRCA1/2-mutated and sporadic triple-negative breast and ovarian cancer |
| [NCT05358639](https://clinicaltrials.gov/study/NCT05358639) | Phase 1 | Active, not recruiting | 36 | Olaparib + navitoclax in BRCA1/2/PALB2-mutated triple-negative breast cancer and recurrent high-grade serous ovarian cancer |
| [NCT04330040](https://clinicaltrials.gov/study/NCT04330040) | Phase 4 | Completed | 202 | Real-world Indian cohort: olaparib in platinum-sensitive relapsed ovarian cancer and metastatic breast cancer with germline BRCA1/2 mutation |
| [NCT04024254](https://clinicaltrials.gov/study/NCT04024254) | Phase 4 | Completed | 10 | Serum folate deficiency monitoring in patients on olaparib for advanced ovarian or breast cancer |
| [NCT05209529](https://clinicaltrials.gov/study/NCT05209529) | Phase 2 | Withdrawn | 0 | Neoadjuvant olaparib ± durvalumab in BRCA-associated triple-negative breast cancer (trial withdrawn — enrolment never began) |

*50 trials in total were identified for this indication; the above are the 10 most directly relevant to breast cancer.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848/) | 2021 | RCT (Phase 3, OlympiA) | New England Journal of Medicine | Adjuvant olaparib reduced invasive disease recurrence in BRCA1/2-mutated, HER2-negative high-risk early breast cancer |
| [36228963](https://pubmed.ncbi.nlm.nih.gov/36228963/) | 2022 | RCT (OlympiA, overall survival) | Annals of Oncology | Overall survival analysis of the OlympiA trial confirming sustained benefit of adjuvant olaparib in gBRCA1/2 early breast cancer |
| [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/) | 2017 | RCT (Phase 3, OlympiAD) | New England Journal of Medicine | Olaparib improved outcomes vs chemotherapy in metastatic breast cancer with a germline BRCA mutation |
| [30689707](https://pubmed.ncbi.nlm.nih.gov/30689707/) | 2019 | RCT (OlympiAD, final OS) | Annals of Oncology | Final overall survival and tolerability results for olaparib vs physician's choice chemotherapy in gBRCAm, HER2-negative metastatic breast cancer |
| [36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/) | 2023 | RCT (OlympiAD, extended follow-up) | European Journal of Cancer | Extended follow-up safety and survival data for olaparib in gBRCAm HER2-negative metastatic breast cancer |
| [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) | 2020 | RCT (Phase 2, TBCRC 048) | Journal of Clinical Oncology | Olaparib activity in metastatic breast cancer with somatic BRCA or other homologous-recombination gene mutations (beyond germline BRCA1/2) |
| [34143979](https://pubmed.ncbi.nlm.nih.gov/34143979/) | 2021 | RCT (Phase 2, I-SPY2) | Cancer Cell | Durvalumab + olaparib + paclitaxel increased pathologic complete response in high-risk HER2-negative breast cancer |
| [38588696](https://pubmed.ncbi.nlm.nih.gov/38588696/) | 2024 | RCT (Phase 2/3, PARTNER) | Nature | Neoadjuvant olaparib added to carboplatin-paclitaxel in germline BRCA-wild-type triple-negative breast cancer |
| [33710534](https://pubmed.ncbi.nlm.nih.gov/33710534/) | 2021 | Review | Targeted Oncology | Overview of PARP inhibitors (olaparib, talazoparib) approved for deleterious/suspected deleterious germline BRCA-mutated, HER2-negative breast cancer |
| [31650727](https://pubmed.ncbi.nlm.nih.gov/31650727/) | 2020 | Review | Annals of Laboratory Medicine | BRCA1/2 pathogenic variant breast cancer: treatment and prevention strategies, including PARP inhibitor use |

*20 publications in total were identified; the above 10 are prioritised by RCT strength.*

---

## Australia Market Information

Olaparib currently has **no ARTG entries** in this evidence pack's regulatory data — it is recorded as not marketed in Australia. No approved indication text, product name, or dosage form information is available to tabulate.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PARP inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Medium — anaemia, neutropenia and thrombocytopenia are recognised class effects of PARP inhibitors, referenced in trial literature in this pack (e.g. NCT06572735 notes PARP inhibitor toxicity to haematopoietic tissue); please refer to the PI for full detail |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Full blood count (FBC) is advisable given the class-wide haematological toxicity signal; please refer to the PI for the complete monitoring schedule |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 3 RCTs (OlympiA, OlympiAD) and multiple supporting Phase 1/2 studies establish strong mechanistic and clinical evidence for olaparib in BRCA-mutated breast cancer (L1 evidence). However, olaparib is not currently registered in Australia, and key drug-level data (MOA documentation, TFDA/TGA warnings, contraindications, and DDI) remain unresolved gaps that block a complete safety assessment.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications) — currently a blocking data gap
- Confirmed mechanism of action documentation via DrugBank
- Assessment of the regulatory pathway for ARTG registration, since olaparib is not currently marketed in Australia
- Completion of drug-drug interaction (DDI) data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

