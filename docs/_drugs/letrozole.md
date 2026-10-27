---
layout: default
title: Letrozole
parent: High Evidence (L1-L2)
nav_order: 421
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-13
description: "Letrozole: predicted new indication Female breast carcinoma (evidence level L1). Approved use: Not available in the data compiled for this report"
monitor_inn: "Letrozole"
predicted_indications: ["nipple carcinoma", "Ehrlich tumor carcinoma", "breast fibrocystic disease", "benign mammary dysplasia"]
---

# Letrozole
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Letrozole: From Breast Cancer (Original Indication) to Female Breast Carcinoma
{: .text-alpha }

## One-Sentence Summary

Letrozole is a nonsteroidal aromatase inhibitor, marketed in Australia as Femara 2.5 mg tablets, and used in hormone-receptor-positive breast cancer.
The TxGNN model predicts it may be effective for **female breast carcinoma**, with **40 clinical trials** and **20 publications** compiled for this prediction.
This is already an established use of letrozole, so the prediction confirms an existing indication rather than revealing a new one.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the Australian licence record has no indication text) |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the compiled data. Letrozole is a nonsteroidal aromatase inhibitor. It blocks the conversion of androgens to oestrogens, which deprives hormone-receptor-positive tumours of oestrogen-driven growth.

This is also the core mechanism behind its established use in hormone-receptor-positive breast cancer. The predicted indication therefore closely matches what the drug already does, and the model's high score is consistent with that.

Phase 3 data (MONALEESA-2, PALOMA-2, COMPLEEMENT-1) show benefit when letrozole is combined with CDK4/6 inhibitors. This is not a true repurposing finding.

The other nine TxGNN predictions vary widely in quality:
- **Established or closely related use (breast disease):** oestrogen-receptor-positive breast cancer (L1, Proceed with Guardrails).
- **Research questions:** hormone-resistant breast carcinoma (L2), bilateral breast carcinoma (L2) and breast carcinoma by gene expression profile (L3).
- **Hold, limited evidence:** nipple carcinoma (L4, case reports only) and oestrogen-receptor-negative breast cancer (L4).
- **Hold, likely false positive or no clinical evidence:** oestrogen-receptor-negative breast cancer (a letrozole effect is not expected, and the matched trials are almost all in ER+/HR+ disease), Ehrlich tumour carcinoma (a mouse model with one preclinical study), breast fibrocystic disease and benign mammary dysplasia (no trials or literature, so the link rests only on the model score).

---

## Clinical Trial Evidence

The table lists the most relevant of the 40 trials compiled for this prediction. The first five are rated directly relevant (A) or relevant (B) in the data.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02941926](https://clinicaltrials.gov/study/NCT02941926) | Phase 3b | Completed | 3,246 | COMPLEEMENT-1: ribociclib plus letrozole in HR+/HER2- advanced breast cancer with no prior hormonal therapy; large safety and efficacy dataset |
| [NCT02600923](https://clinicaltrials.gov/study/NCT02600923) | Phase 3 | Completed | 131 | Palbociclib plus letrozole in postmenopausal women with HR+/HER2- advanced breast cancer (access study in Latin America) |
| [NCT03425838](https://clinicaltrials.gov/study/NCT03425838) | Phase 3 | Active, not recruiting | 1,050 | SONIA (BOOG 2017-03): CDK4/6 inhibitor with an aromatase inhibitor in first line versus second line |
| [NCT01740427](https://clinicaltrials.gov/study/NCT01740427) | Phase 3 | Completed | 666 | PALOMA-2: palbociclib plus letrozole versus placebo plus letrozole in ER+/HER2- advanced breast cancer |
| [NCT00908531](https://clinicaltrials.gov/study/NCT00908531) | Phase 3 | Terminated | 123 | DBCG trial: 4 months of letrozole versus surgery first in postmenopausal HR+ tumours over 2 cm; limited power because it ended early |
| [NCT00382070](https://clinicaltrials.gov/study/NCT00382070) | Phase 3 | Unknown | 3,966 | Five years of letrozole versus placebo after completing 5 years of hormonal therapy |
| [NCT04272801](https://clinicaltrials.gov/study/NCT04272801) | Phase 2 | Active, not recruiting | 84 | Pre-operative endocrine window in older women to inform radiation decisions |
| [NCT00728949](https://clinicaltrials.gov/study/NCT00728949) | Phase 2 | Completed | 93 | IMC-A12 alone or with antioestrogens after progression on antioestrogen therapy |
| [NCT02712723](https://clinicaltrials.gov/study/NCT02712723) | Phase 2 | Active, not recruiting | 121 | Letrozole plus ribociclib or placebo as neoadjuvant therapy in ER+/HER2- early breast cancer |
| [NCT01439711](https://clinicaltrials.gov/study/NCT01439711) | Phase 2 | Completed | 108 | Neoadjuvant letrozole in postmenopausal women with ER+ ductal carcinoma in situ |

No ANZCTR identifiers were included in the compiled data.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35263519](https://pubmed.ncbi.nlm.nih.gov/35263519/) | 2022 | RCT | N Engl J Med | Overall survival with ribociclib plus letrozole in advanced breast cancer (follow-up of a phase 3 trial that showed longer progression-free survival) |
| [29718092](https://pubmed.ncbi.nlm.nih.gov/29718092/) | 2018 | RCT | Ann Oncol | MONALEESA-2 updated efficacy and safety of first-line ribociclib plus letrozole in HR+/HER2- advanced breast cancer |
| [30632023](https://pubmed.ncbi.nlm.nih.gov/30632023/) | 2019 | RCT | Breast Cancer Res Treat | PALOMA-2 extended follow-up; palbociclib plus letrozole prolonged progression-free survival (HR 0.58 at initial analysis) |
| [15001182](https://pubmed.ncbi.nlm.nih.gov/15001182/) | 2004 | RCT | Womens Health Issues | Commentary on the Letrozole Breast Cancer Trial: clinical implications and remaining questions |
| [36243120](https://pubmed.ncbi.nlm.nih.gov/36243120/) | 2022 | Review | Life Sci | Letrozole pharmacology, toxicity and potential therapeutic effects |
| [19250202](https://pubmed.ncbi.nlm.nih.gov/19250202/) | 2009 | Review | Ann N Y Acad Sci | Aromatase inhibitors in breast cancer; letrozole sustained growth inhibition longer than tamoxifen in a preclinical model |
| [17544670](https://pubmed.ncbi.nlm.nih.gov/17544670/) | 2007 | Review | Breast | Prescribing extended adjuvant letrozole (MA-17 trial) |
| [12113048](https://pubmed.ncbi.nlm.nih.gov/12113048/) | 2002 | Review | Expert Rev Anticancer Ther | Letrozole showed superiority to tamoxifen as first-line treatment of metastatic postmenopausal breast cancer |
| [12538503](https://pubmed.ncbi.nlm.nih.gov/12538503/) | 2003 | Review | Clin Cancer Res | Clinical differences among the three third-generation aromatase inhibitors |
| [29229198](https://pubmed.ncbi.nlm.nih.gov/29229198/) | 2017 | Clinical study | Arch Med Res | Combined raloxifene and letrozole in breast cancer cell lines, to address bone adverse effects |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 13939P | Femara 2.5 mg | Tablet 2.5 mg (oral) | Not available in the data compiled for this report |

---

## Cytotoxicity

Letrozole is an endocrine (aromatase inhibitor) therapy rather than a conventional cytotoxic agent, though it is used in cancer treatment. No cytotoxicity data was available in the compiled data. Please refer to the Product Information (PI) warnings and precautions.

---

## Safety Considerations

- **Disease associations from the knowledge graph:** The knowledge graph links letrozole to liver failure, cirrhosis of the liver, osteoporosis, postmenopausal osteoporosis, hyperbilirubinaemia (including hereditary forms and Gilbert syndrome) and cerebrovascular disorder. These come from a model knowledge graph rather than label text, so they need confirmation against the PI.
- **Drug interactions:** 100 interactions were identified. The one with a stated severity is aprepitant (Moderate). Others listed, mostly with unknown severity, include calcitriol, glimepiride, metformin, simvastatin, prednisone, omeprazole and pantoprazole.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications, as label text was not available.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 trials and randomised publications support letrozole in HR+ breast cancer, which is an established use. The evidence supports the existing indication rather than a new one, and the Australian indication text and label safety data could not be confirmed.

**To proceed, the following is needed:**
- The TGA-approved indication text for Femara (ARTG 13939P) and label warnings and contraindications from the PI
- Mechanism-of-action data from DrugBank
- Confirmation of the knowledge-graph disease associations (hepatic impairment, osteoporosis, cerebrovascular disease) against the label
- Review of the severity of the flagged drug interactions
- For the other predictions, a decision to treat the oestrogen-receptor-negative, Ehrlich tumour, fibrocystic and benign dysplasia predictions as Hold, and to pursue the hormone-resistant, bilateral and gene-expression-profile predictions only as research questions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

