---
layout: default
title: Hydroxyurea
parent: Model Prediction Only (L5)
nav_order: 358
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
monitor_inn: "Hydroxyurea"
predicted_indications: ["female breast carcinoma", "sickle cell-hemoglobin c disease syndrome", "sickle cell-hemoglobin E disease syndrome", "sickle cell-hemoglobin d disease syndrome", "sickle cell-beta-thalassemia disease syndrome", "cervical adenosarcoma", "colon mucinous adenocarcinoma", "rectum mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma"]
description: "Hydroxyurea: predicted new indication Female breast carcinoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Hydroxyurea
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Hydroxyurea: Female breast carcinoma
{: .text-alpha }

## One-Sentence Summary

Hydroxyurea is a ribonucleotide reductase inhibitor, originally used for melanoma, sickle cell anaemia and ovarian cancer.
The TxGNN model predicts it may be effective for **female breast carcinoma** (score 0.9997), but **no clinical trials** are registered for this indication and the **20 publications** retrieved are almost entirely preclinical, in-silico or off-topic.
The prediction is therefore best viewed as a hypothesis.

*Note: The ranked predictions also include sickle cell-haemoglobin C disease, which has markedly stronger evidence (a Phase 2 trial and a 2025 clinical publication). It is summarised under "Other Predicted Indications" below.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 (preclinical and mechanistic studies only) |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in the data compiled for this report. Based on known pharmacology, hydroxyurea inhibits ribonucleotide reductase, which depletes deoxynucleotide (dNTP) pools and induces DNA replication stress. This mechanism underlies its use in cancers such as melanoma and ovarian cancer.

Breast cancer cells are also dependent on DNA replication and repair. Preclinical papers link replication stress, ATR signalling and RPA2-mediated DNA repair to breast cancer cell sensitivity to hydroxyurea. Examples include valproic acid sensitising breast cancer cells to hydroxyurea, and BRCA1-deficient breast cancer cells being susceptible to ribonucleotide reductase inhibition.

The mechanistic rationale is plausible, but it has not been tested in breast cancer patients in the data compiled. The very high TxGNN score is a computational output and should not be read as clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for female breast carcinoma.

---

## Literature Evidence

None of the retrieved publications is a randomised trial of hydroxyurea in breast cancer. The most relevant items are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38211596](https://pubmed.ncbi.nlm.nih.gov/38211596/) | 2024 | In-silico/Preclinical | Drug Research | Design of hydroxyurea–lipid conjugates to improve cellular uptake in breast cancer, targeting the PI3K/AKT/mTOR pathway |
| [28837865](https://pubmed.ncbi.nlm.nih.gov/28837865/) | 2017 | Preclinical | DNA Repair | Valproic acid sensitises breast cancer cells to hydroxyurea by inhibiting RPA2 hyperphosphorylation-mediated DNA repair |
| [32795962](https://pubmed.ncbi.nlm.nih.gov/32795962/) | 2020 | Preclinical | DNA Repair | A valproic acid analogue influences RPA2-mediated DNA repair, potentially sensitising breast carcinoma cells to hydroxyurea |
| [21730979](https://pubmed.ncbi.nlm.nih.gov/21730979/) | 2011 | Preclinical | British Journal of Cancer | Novel ATR inhibitor NU6027 evaluated in breast and ovarian cancer cell lines |
| [1957839](https://pubmed.ncbi.nlm.nih.gov/1957839/) | 1991 | Phase I | American Journal of Clinical Oncology | Allopurinol, 5-FU and leucovorin followed by hydroxyurea in 20 patients with advanced gastrointestinal and breast cancer |
| [1733549](https://pubmed.ncbi.nlm.nih.gov/1733549/) | 1992 | Phase I/II | Cancer Chemotherapy and Pharmacology | 5-FU, leucovorin, hydroxyurea and escalating cisplatin with radiotherapy in mixed advanced solid tumours |
| [25814515](https://pubmed.ncbi.nlm.nih.gov/25814515/) | 2015 | Preclinical | Molecular Pharmacology | Novel ribonucleotide reductase inhibitor COH29 inhibits DNA repair in BRCA1-defective breast cancer cells |
| [30159181](https://pubmed.ncbi.nlm.nih.gov/30159181/) | 2018 | Case report | Case Reports in Hematology | Management of coexisting breast cancer and essential thrombocythaemia |

The remaining retrieved papers were either not specific to hydroxyurea or off-topic.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 4281H | Egoderm Cream | Cream 10 mg per g (1%), 50 g | Not stated in the data compiled |

The only registered Australian product is a **topical** hydroxyurea 1% cream. No oral dosage form appears in the data compiled, so the systemic route used for oncology and sickle cell disease is not represented in the ARTG data reviewed here.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antimetabolite; ribonucleotide reductase inhibitor) |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Full blood count (with differential), renal function and liver function |
| Handling Protection | Follow local cytotoxic drug handling requirements |

---

## Safety Considerations

- **Contraindications (TxGNN model (deep learning) output, not label text; may reflect similarities the model learned between related diseases, not biological evidence):** kidney disease, pyoureter, thrombocytopenia, anaemia, macrocytic anaemia, leukopenia and cutaneous vasculitis.
- **Drug Interactions:** 100 interactions were identified. Only the severity of levofloxacin (Minor) is classified; the others (for example doxycycline, amphotericin B, hydrocortisone, famotidine, acetylsalicylic acid, pantoprazole, morphine, metformin, omeprazole, vancomycin, prednisone and simvastatin) have no assigned severity level in the source. Review the full interaction list before use.

Please refer to the TGA-approved Product Information (PI) for formal warnings and contraindications.

---

## Other Predicted Indications

| Rank | Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Sickle cell-haemoglobin C disease | 0.9967 | L5 | Phase 2 trial [NCT00532883](https://clinicaltrials.gov/study/NCT00532883) (n=44, terminated) plus a 2025 NEJM Evidence publication ([39647172](https://pubmed.ncbi.nlm.nih.gov/39647172/)) and cohort studies. No Phase 3 trial is evident. Research question. |
| 3–5 | Sickle cell-HbE, sickle cell-HbD, HPFH-sickle cell | 0.9967 | L5 | Only indirect or irrelevant literature. Hold. |
| 6 | Sickle cell-beta-thalassaemia | 0.9967 | L5 | Small 1999 clinical trial ([10326220](https://pubmed.ncbi.nlm.nih.gov/10326220/)); the listed trials are transplant studies, not hydroxyurea trials. Research question. |
| 7–10 | Cervical adenosarcoma; colon, rectum and gallbladder mucinous adenocarcinoma | 99.28–0.9940 | L5 | Model prediction only, with no trials or literature. Hold. |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The breast carcinoma prediction rests on a plausible mechanism and preclinical work only. There are no registered trials and no clinical efficacy data, and the Australian product is a topical cream rather than a systemic formulation. Of the predictions, sickle cell-haemoglobin C disease is the strongest candidate for further investigation.

**To proceed, the following is needed:**
- Mechanism of action data to support the mechanistic-link analysis
- TGA Product Information warnings and contraindications (a blocking gap for safety screening)
- Clinical evidence in breast cancer, such as a well-designed Phase 2 study or a systematic review of existing combination-chemotherapy data
- Confirmation of whether a systemic hydroxyurea formulation is available in Australia
- For sickle cell-haemoglobin C disease, a review of the 2025 trial and the terminated Phase 2 trial to decide whether it should be prioritised
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

