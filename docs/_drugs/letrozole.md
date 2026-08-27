---
layout: default
title: Letrozole
parent: 僅模型預測 (L5)
nav_order: 392
evidence_level: L5
indication_count: 10
---

# Letrozole
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

# Letrozole: From Breast Cancer to Female Breast Carcinoma

## One-Sentence Summary

Letrozole is a third-generation aromatase inhibitor whose established clinical role — per the literature captured in this evidence pack — is hormone receptor-positive breast cancer in postmenopausal women. TxGNN's top-ranked signal is **Female Breast Carcinoma** (score 99.98%), backed by **50 clinical trials** and **20 publications**, but this evidence set largely reflects letrozole's already-known indication rather than a genuinely novel repurposing target — Australian regulatory (ARTG) records and the drug's original-indication field are both currently blank in this dataset.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in ARTG data in this pack; literature describes letrozole as an established hormone receptor-positive (HR+) breast cancer therapy (PMID 20095792, 36243120) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed (per current data) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data is not available for this candidate. Based on the literature retrieved in this evidence pack, letrozole is a third-generation, non-steroidal **aromatase inhibitor**: it blocks conversion of adrenal androgens to oestrogens, lowering circulating oestrogen levels and thereby slowing the growth of oestrogen-dependent tumours (PMID 20095792).

The overlap between letrozole's known use and the "predicted" indication here is important to flag transparently. Female breast carcinoma is the disease area letrozole is globally best known for treating, and several trials/publications in the supporting evidence (e.g. NCT01740427/PALOMA‑2, NCT00754845/MA.17 extension) are large, long-established registration or post-marketing studies rather than exploratory repurposing trials. The evidence pack's own annotation for the closely related "estrogen-receptor positive breast cancer" candidate (rank 5) makes this explicit: *"letrozole 直接切斷腫瘤生長驅動因子，機轉高度吻合，屬其核心已驗證適應症而非新假說"* (mechanistically well matched — this is a core, already-validated indication rather than a new hypothesis).

**Practical implication**: this candidate should be read as *confirmatory, high-confidence evidence* for letrozole in breast cancer, not as a novel repurposing signal. Because the original-indication field and Australian ARTG record are both empty in this dataset, a formal comparison against letrozole's currently approved Australian indication cannot yet be completed — this needs to be closed before any guardrailed use decision is finalised.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02600923](https://clinicaltrials.gov/study/NCT02600923) | Phase 3 | Completed | 131 | Palbociclib + letrozole in HR+/HER2- postmenopausal advanced breast cancer (Latin America access study) |
| [NCT02338310](https://clinicaltrials.gov/study/NCT02338310) | Phase 3 | Active, not recruiting | 4,486 | Large perioperative aromatase-inhibitor trial in postmenopausal HR+ breast cancer, with Ki67 as a recurrence predictor |
| [NCT01740427](https://clinicaltrials.gov/study/NCT01740427) | Phase 3 | Completed | 666 | PALOMA-2: palbociclib + letrozole vs placebo + letrozole as first-line therapy in ER+/HER2- advanced breast cancer |
| [NCT00754845](https://clinicaltrials.gov/study/NCT00754845) | Phase 3 | Completed | 1,918 | Extended adjuvant letrozole vs placebo after 5 years of prior aromatase-inhibitor therapy (MA.17-related) |
| [NCT00171340](https://clinicaltrials.gov/study/NCT00171340) | Phase 3 | Completed | 1,065 | Zoledronic acid timing for prevention of letrozole-associated bone loss in adjuvant therapy |
| [NCT00171704](https://clinicaltrials.gov/study/NCT00171704) | Phase 3 | Completed | 263 | Letrozole vs tamoxifen — effects on bone and lipid metabolism in resected HR+ early breast cancer |
| [NCT02278120](https://clinicaltrials.gov/study/NCT02278120) | Phase 3 | Completed | 672 | Ribociclib vs placebo with tamoxifen/NSAI + goserelin in premenopausal HR+/HER2- advanced breast cancer |
| [NCT03056755](https://clinicaltrials.gov/study/NCT03056755) | Phase 2 | Completed | 383 | BYLieve: alpelisib + fulvestrant or letrozole in PIK3CA-mutant HR+/HER2- advanced breast cancer |
| [NCT00310180](https://clinicaltrials.gov/study/NCT00310180) | Phase 3 | Active, not recruiting | 10,273 | TAILORx — Oncotype DX-guided hormone therapy ± chemotherapy in node-negative ER+ breast cancer |
| [NCT06223698](https://clinicaltrials.gov/study/NCT06223698) | Phase 3 | Not yet recruiting | 3,832 | SWE-Switch: extended adjuvant endocrine therapy strategy comparison in high-risk luminal breast cancer |

No ANZCTR-registered trial identifiers were found in the supplied evidence.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32683565](https://pubmed.ncbi.nlm.nih.gov/32683565/) | 2020 | RCT | Breast Cancer Res Treat | PALOMA-1 overall survival: palbociclib + letrozole vs letrozole alone in first-line ER+/HER2- advanced breast cancer |
| [16382061](https://pubmed.ncbi.nlm.nih.gov/16382061/) | 2005 | RCT | New England Journal of Medicine | Letrozole vs tamoxifen as adjuvant therapy in postmenopausal HR+ early breast cancer |
| [35464999](https://pubmed.ncbi.nlm.nih.gov/35464999/) | 2022 | Cohort/Comparative | Comput Math Methods Med | Efficacy/safety/prognosis of sequential tamoxifen–letrozole vs letrozole monotherapy |
| [36243120](https://pubmed.ncbi.nlm.nih.gov/36243120/) | 2022 | Review | Life Sciences | Overview of letrozole pharmacology, toxicity, and therapeutic effects, including its aromatase-inhibitor mechanism |
| [20095792](https://pubmed.ncbi.nlm.nih.gov/20095792/) | 2010 | Review | Expert Opin Drug Metab Toxicol | Pharmacodynamics, pharmacokinetics, clinical efficacy and safety of letrozole |
| [15001182](https://pubmed.ncbi.nlm.nih.gov/15001182/) | 2004 | Review | Women's Health Issues | Clinical implications and remaining questions from the Letrozole Breast Cancer Trial |
| [35378469](https://pubmed.ncbi.nlm.nih.gov/35378469/) | 2022 | Cohort | Current Problems in Cancer | Predictive response/prognostic factors for palbociclib + letrozole in HR+ advanced breast cancer |
| [34645649](https://pubmed.ncbi.nlm.nih.gov/34645649/) | 2022 | Biomarker study | Clin Cancer Res | Biomarkers of response/resistance to palbociclib + letrozole in ER+/HER2- breast cancer |
| [16500235](https://pubmed.ncbi.nlm.nih.gov/16500235/) | 2006 | Review | Breast (Edinburgh) | Development of letrozole and its use in advanced and neoadjuvant breast cancer |
| [27235140](https://pubmed.ncbi.nlm.nih.gov/27235140/) | 2016 | Preclinical | Med Oncol | Letrozole-induced changes in carcinoma-associated fibroblasts affecting endocrine therapy efficacy |

---

## Cytotoxicity

Letrozole is an antineoplastic agent by virtue of its cancer indication, but it is a **hormonal (endocrine) therapy**, not a conventional cytotoxic chemotherapeutic.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted/hormonal therapy — non-steroidal aromatase inhibitor (not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Low — aromatase inhibitors are not typically myelosuppressive; formal toxicity data was not available in this evidence pack |
| Emetogenicity Classification | Low |
| Monitoring Items | Bone mineral density and lipid profile (per supporting trial endpoints), liver function; formal PI-based monitoring guidance is a data gap |
| Handling Protection | Standard oral oncology medication precautions; not generally subject to injectable cytotoxic handling protocols, but confirm against institutional policy and the TGA-approved PI |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No key warnings, contraindications, or drug–drug interaction data were returned for letrozole in this evidence pack (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple large, completed Phase 3 trials and RCT-grade literature strongly support letrozole's efficacy in HR+ breast cancer, giving this candidate L1 evidence strength. However, this appears to largely confirm an already-known indication rather than reveal a new one, and two data-pack-flagged gaps remain unresolved: TFDA/ARTG product and indication data is rated a **Blocking** gap (prevents formal safety pre-assessment), and detailed mechanism-of-action data is rated **High** severity.

**To proceed, the following is needed:**
- TGA/ARTG regulatory record confirmation for letrozole (current data shows 0 entries / not marketed, which should be verified against the real ARTG register)
- Formal comparison of letrozole's currently approved Australian indication against "Female Breast Carcinoma" to confirm whether this is a genuinely new use or an evidence-pack labelling gap
- DrugBank/PI mechanism-of-action and safety data (key warnings, contraindications, DDI) to complete the S1 safety pre-assessment referenced in the Blocking data gap (DG001)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

