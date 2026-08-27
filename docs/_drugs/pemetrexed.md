---
layout: default
title: Pemetrexed
parent: 僅模型預測 (L5)
nav_order: 520
evidence_level: L5
indication_count: 10
---

# Pemetrexed
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

# Pemetrexed: From Pleural Mesothelioma to Malignant Peritoneal Mesothelioma

## One-Sentence Summary

Pemetrexed is an antifolate chemotherapy already established (in combination with cisplatin) as a treatment for pleural mesothelioma. The TxGNN model predicts it may also be effective for **Malignant Peritoneal Mesothelioma**, with **11 clinical trials** and **20 publications** currently identified in the evidence pack for this indication.

*Note: This evidence pack contains no Australian regulatory (TFDA/TGA) license data for pemetrexed — the drug is currently not marketed in Australia under this dataset, and mechanism-of-action data is also a confirmed gap (see Data Gaps below). The "original indication" above is drawn from the trial/literature context within this evidence pack (see Clinical Trial Evidence for pleural mesothelioma, ranked #3), not from an ARTG-approved product label.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pleural mesothelioma (with cisplatin) — per trial-context evidence in this pack; no ARTG label text available |
| Predicted New Indication | Malignant Peritoneal Mesothelioma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for pemetrexed is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on well-established pharmacology, pemetrexed is a multitargeted antifolate that inhibits thymidylate synthase (TS), dihydrofolate reductase (DHFR), and glycinamide ribonucleotide formyltransferase (GARFT) — enzymes required for folate-dependent DNA synthesis in rapidly dividing cells.

Malignant peritoneal mesothelioma and pleural mesothelioma are both tumours of mesothelial cell origin, sharing overlapping molecular biology (including BAP1 alterations and mesothelin expression). Pemetrexed plus cisplatin is already an established regimen for pleural mesothelioma, and the mechanism of antifolate-driven cytotoxicity is not organ-site specific — it targets the same underlying proliferative biology regardless of whether the mesothelioma arises in the pleura or peritoneum.

This mechanistic overlap is reflected in the trial evidence itself: several trials for peritoneal mesothelioma directly reuse pemetrexed/cisplatin-based regimens developed for the pleural disease (e.g. NCT00061477, NCT05001880), and case-level literature (PMID 23291819, 28594258) reports clinical responses when pemetrexed-cisplatin is applied specifically to peritoneal disease. However, no completed Phase 3 RCT exists specifically for the peritoneal site, which is why the evidence level here is L2 rather than L1.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT06057935](https://clinicaltrials.gov/study/NCT06057935) | Phase 2 | Recruiting | 64 | ICARuS II: compares intraperitoneal vs intravenous chemotherapy after cytoreductive surgery + HIPEC in malignant peritoneal mesothelioma |
| [NCT03875144](https://clinicaltrials.gov/study/NCT03875144) | Phase 2 | Suspended | 66 | MESOTIP: PIPAC + systemic chemotherapy (cisplatin+pemetrexed) vs systemic chemotherapy alone as 1st-line treatment |
| [NCT06543069](https://clinicaltrials.gov/study/NCT06543069) | Phase 2 | Recruiting | 28 | Sintilimab + bevacizumab + pemetrexed + cisplatin in unresectable malignant peritoneal mesothelioma |
| [NCT04462809](https://clinicaltrials.gov/study/NCT04462809) | Phase 2 | Unknown | 40 | Talazoparib maintenance following 1st-line platinum-based chemotherapy in pleural/peritoneal mesothelioma |
| [NCT00061477](https://clinicaltrials.gov/study/NCT00061477) | Phase 2 | Completed | 48 | ALIMTA (pemetrexed) + gemcitabine as front-line chemotherapy, explicitly including a peritoneal mesothelioma cohort |
| [NCT00402766](https://clinicaltrials.gov/study/NCT00402766) | Phase 1 | Completed | 19 | Cisplatin + pemetrexed + imatinib mesylate in unresectable/metastatic malignant mesothelioma |
| [NCT02029690](https://clinicaltrials.gov/study/NCT02029690) | Phase 1 | Terminated | 85 | ADI-PEG 20 + pemetrexed + cisplatin (TRAP study), including a peritoneal mesothelioma dose-escalation cohort |
| [NCT05001880](https://clinicaltrials.gov/study/NCT05001880) | Phase 2 | Recruiting | 66 | Carboplatin + pemetrexed + bevacizumab ± atezolizumab in peritoneal mesothelioma |
| [NCT01353482](https://clinicaltrials.gov/study/NCT01353482) | Phase 1/2 | Withdrawn | 0 | Vorinostat + pemetrexed-cisplatin, covering both pleural and peritoneal mesothelioma (withdrawn before enrolment) |
| [NCT02535312](https://clinicaltrials.gov/study/NCT02535312) | Phase 1/2 | Active, not recruiting | 30 | TRC102 + cisplatin/pemetrexed in solid tumours/mesothelioma refractory to pemetrexed-platinum |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35407498](https://pubmed.ncbi.nlm.nih.gov/35407498/) | 2022 | Review (treatment-focused) | J Clin Med | Overview of treatment approaches for malignant peritoneal mesothelioma, including systemic chemotherapy role |
| [31417959](https://pubmed.ncbi.nlm.nih.gov/31417959/) | 2019 | Cohort | Pleura and Peritoneum | Bidirectional chemotherapy improved resectability in initially unresectable peritoneal mesothelioma |
| [28594258](https://pubmed.ncbi.nlm.nih.gov/28594258/) | 2017 | Retrospective study | Expert Rev Anticancer Ther | First-line pemetrexed + cisplatin evaluated specifically in malignant peritoneal mesothelioma |
| [31287877](https://pubmed.ncbi.nlm.nih.gov/31287877/) | 2019 | Retrospective study | Jpn J Clin Oncol | Efficacy and safety of pemetrexed + cisplatin as first-line therapy in advanced peritoneal mesothelioma |
| [38806763](https://pubmed.ncbi.nlm.nih.gov/38806763/) | 2024 | Multi-centre cohort | Ann Surg Oncol | Treatment strategies and outcomes across a multi-centre peritoneal mesothelioma population |
| [34723916](https://pubmed.ncbi.nlm.nih.gov/34723916/) | 2022 | Case series | J Immunother | Chemoimmunotherapy in platinum-nonresponsive metastatic peritoneal mesothelioma |
| [33257382](https://pubmed.ncbi.nlm.nih.gov/33257382/) | 2020 | Case report | BMJ Case Rep | Nivolumab used after prior pemetrexed-based chemotherapy in peritoneal mesothelioma |
| [23291819](https://pubmed.ncbi.nlm.nih.gov/23291819/) | 2013 | Case report | BMJ Case Rep | Response to rechallenge with cisplatin + pemetrexed in peritoneal mesothelioma |
| [26941986](https://pubmed.ncbi.nlm.nih.gov/26941986/) | 2016 | Review | J Gastrointest Oncol | Diagnosis and management overview of peritoneal mesothelioma, including systemic therapy options |
| [30450291](https://pubmed.ncbi.nlm.nih.gov/30450291/) | 2018 | Review | Transl Lung Cancer Res | General review of peritoneal mesothelioma biology and treatment |

---

## Australia Market Information

Pemetrexed is currently **not marketed in Australia** under the data available in this evidence pack — there are no ARTG entries recorded (total_licenses = 0). No product-level Australian regulatory information (brand names, dosage forms, or approved indication text) is available to report.

---

## Cytotoxicity

Pemetrexed is an antineoplastic agent (multitargeted antifolate class), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antifolate class) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Full blood count (with differential), renal function, and hepatic function are standard monitoring parameters for antifolate cytotoxic therapy |
| Handling Protection | Standard cytotoxic drug handling and protection protocols apply |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No key warnings, contraindications, or drug-drug interaction data are available for pemetrexed in this evidence pack (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The mechanistic rationale for extending pemetrexed to malignant peritoneal mesothelioma is strong given its established role in pleural mesothelioma, and several Phase 1/2 trials and retrospective studies support activity in the peritoneal setting. However, no completed Phase 3 RCT exists for this specific site, and most supporting trials are early-phase, small, or use pemetrexed as part of multi-drug combinations rather than as the sole variable under study.

**To proceed, the following is needed:**
- TFDA/TGA-approved Product Information (warnings, contraindications, DDI) — currently a Blocking data gap
- Detailed mechanism of action documentation from DrugBank — currently a High-severity data gap
- A dedicated prospective (ideally randomised) trial in peritoneal mesothelioma to confirm efficacy independent of pleural-disease extrapolation
- Confirmation of intended route of administration and dosing compatibility for the peritoneal setting (e.g. IP vs IV, as tested in NCT06057935)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

