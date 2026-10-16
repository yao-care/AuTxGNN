---
layout: default
title: Cetuximab
parent: Model Prediction Only (L5)
nav_order: 150
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Cetuximab: predicted new indication Bronchial adenomas/carcinoids, childhood (evidence level L5). Approved use: Colorectal cancer and squamous cell carcinoma of the head and neck (c…"
monitor_inn: "Cetuximab"
predicted_indications: ["bronchial adenomas/carcinoids childhood", "chondroid hamartoma", "ductal or ductular proliferation", "non-seminomatous lesion", "tumor of testis and paratestis", "odontogenic cyst", "thyroglossal duct cyst", "cystic neoplasm", "epiglottis neoplasm", "pre-malignant neoplasm"]
---

# Cetuximab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Cetuximab: From Colorectal and Head and Neck Cancers to Bronchial Adenomas/Carcinoids (Childhood)

## One-Sentence Summary

Cetuximab is an anti-EGFR monoclonal antibody, originally used for colorectal cancer and squamous cell carcinoma of the head and neck.
The TxGNN model's top-ranked prediction is **bronchial adenomas/carcinoids (childhood)**, but **no clinical trials or publications** currently support it.
Among the ten predictions reviewed, the best-supported are **cystic neoplasm** (4 trials, 20 publications) and **pre-malignant neoplasm** (4 trials, 2 publications), both at L2.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Colorectal cancer and squamous cell carcinoma of the head and neck (colon, pharyngeal and laryngeal). The ARTG entry does not list an indication text. |
| Predicted New Indication | Bronchial adenomas/carcinoids, childhood (rank 1) |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 (rank 1). Highest among the other predictions: L2 (cystic neoplasm; pre-malignant neoplasm) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

The top ten predictions all have scores of about 99.95%, so the score does not separate them. The table below summarises them.

| Rank | Predicted Indication | Evidence Level | Trials | Publications | Recommendation |
|---|---|---|---|---|---|
| 1 | Bronchial adenomas/carcinoids, childhood | L5 | 0 | 0 | Hold |
| 2 | Chondroid hamartoma | L5 | 0 | 0 | Hold |
| 3 | Ductal or ductular proliferation | L4 | 0 | 20 | Hold |
| 4 | Non-seminomatous lesion | L5 | 0 | 0 | Hold |
| 5 | Tumour of testis and paratestis | L5 | 0 | 0 | Hold |
| 6 | Odontogenic cyst | L4 | 0 | 2 | Hold |
| 7 | Thyroglossal duct cyst | L5 | 0 | 0 | Hold |
| 8 | Cystic neoplasm | L2 | 4 | 20 | Research question |
| 9 | Epiglottis neoplasm | L5 | 0 | 0 | Hold |
| 10 | Pre-malignant neoplasm | L2 | 4 | 2 | Research question |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on known information, cetuximab is an antibody that binds the epidermal growth factor receptor (EGFR). Its efficacy in EGFR-expressing metastatic colorectal cancer and in squamous cell carcinoma of the head and neck is established.

For the rank 1 prediction, bronchial carcinoids in children, the compiled data contain no trials, literature or other evidence linking EGFR blockade to this disease. The prediction rests on the model score alone and should be treated as a hypothesis.

Two lower-ranked predictions have a more plausible link:

- **Cystic neoplasm.** The relevant evidence concerns adenoid cystic carcinoma and salivary gland carcinomas, where EGFR is expressed. Cetuximab has been tested in these tumours, but efficacy results were not available in the compiled data.
- **Pre-malignant neoplasm.** EGFR is overexpressed in premalignant upper aerodigestive tract lesions. A completed Phase II single-agent cetuximab study (NCT00524017) exists, which supports a chemoprevention hypothesis.

Two other predictions need caution:

- **Epiglottis neoplasm** likely overlaps with the existing head and neck squamous cell carcinoma indication, so it is probably not a true repurposing opportunity.
- **Ductal or ductular proliferation** was matched mainly to pancreatic ductal adenocarcinoma literature. KRAS is the dominant driver in that disease, which limits the benefit of EGFR blockade. The label match is loose.

---

## Clinical Trial Evidence

**Rank 1 (bronchial adenomas/carcinoids, childhood):** Currently no related clinical trials registered.

The trials below relate to the two predictions with trial data. The studies for rank 8 (cystic neoplasm) are listed first, followed by those for rank 10 (pre-malignant neoplasm).

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01192087](https://clinicaltrials.gov/study/NCT01192087) | Phase 1/2 | Unknown | 49 | Rank 8. Cetuximab with IMRT plus carbon ion boost in adenoid cystic carcinoma; toxicity and efficacy being explored. Most directly relevant to this indication. |
| [NCT00397384](https://clinicaltrials.gov/study/NCT00397384) | Phase 1 | Completed | 43 | Rank 8. Erlotinib plus cetuximab in advanced gastrointestinal, head and neck, lung and colorectal cancers; safety and dose study. Indirect link. |
| [NCT00101348](https://clinicaltrials.gov/study/NCT00101348) | Phase 1/2 | Completed | 66 | Rank 8. Erlotinib, cetuximab and bevacizumab in metastatic renal cell and other solid tumours. Not specific to cystic neoplasms. |
| [NCT01637194](https://clinicaltrials.gov/study/NCT01637194) | Phase 1 | Completed | 12 | Rank 8. Cetuximab with everolimus (RAD001) in solid tumours; small safety study. |
| [NCT00524017](https://clinicaltrials.gov/study/NCT00524017) | Phase 2 | Completed | 35 | Rank 10. Single-agent cetuximab in high-risk premalignant upper aerodigestive lesions. Most direct evidence. |
| [NCT00482222](https://clinicaltrials.gov/study/NCT00482222) | Phase 3 | Unknown | 340 | Rank 10. Oxaliplatin/fluoropyrimidine with or without cetuximab around surgery for colorectal liver metastases. Indirect relevance. |
| [NCT00719199](https://clinicaltrials.gov/study/NCT00719199) | Phase 1 | Terminated | 21 | Rank 10. FOLFIRI plus cetuximab plus IMO-2055 in previously treated colorectal cancer. Not premalignant disease. |
| [NCT00537823](https://clinicaltrials.gov/study/NCT00537823) | Phase 2 | Terminated | 9 | Rank 10. Short-course preoperative FOLFOX-based therapy before liver resection for colorectal metastases. Not specific to premalignant disease. |

No ANZCTR trial identifiers were available in the compiled data.

---

## Literature Evidence

**Rank 1 (bronchial adenomas/carcinoids, childhood):** Currently no related literature available.

The most relevant publications for the better-supported predictions are shown below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18804410](https://pubmed.ncbi.nlm.nih.gov/18804410/) | 2009 | Phase II trial | Oral Oncology | Rank 8. Cetuximab in 30 patients (23 adenoid cystic carcinoma) with recurrent or metastatic salivary gland carcinoma; clinical benefit rate was the primary measure. The efficacy result was not available in the compiled data. |
| [32518035](https://pubmed.ncbi.nlm.nih.gov/32518035/) | 2020 | Case report and review | Oral Oncology | Rank 8. Cetuximab monotherapy for relapsing high-grade mucoepidermoid carcinoma. |
| [26245271](https://pubmed.ncbi.nlm.nih.gov/26245271/) | 2016 | Tissue study | Clinical Oral Investigations | Rank 8. Phosphorylated EGFR expression and KRAS mutation status in salivary gland carcinomas. |
| [24412287](https://pubmed.ncbi.nlm.nih.gov/24412287/) | 2014 | Review | Oral Oncology | Rank 10. EGFR is overexpressed in oral premalignant lesions, supporting EGFR-targeted chemoprevention. |
| [33243986](https://pubmed.ncbi.nlm.nih.gov/33243986/) | 2020 | Review | Nature Reviews Disease Primers | Rank 10. Overview of head and neck squamous cell carcinoma. |
| [35300246](https://pubmed.ncbi.nlm.nih.gov/35300246/) | 2022 | Randomised phase II | Clin Transl Radiat Oncol | Rank 3. Long-term results of cetuximab, gemcitabine and radiotherapy in locally advanced pancreatic cancer (PARC trial). |
| [27797376](https://pubmed.ncbi.nlm.nih.gov/27797376/) | 2017 | Preclinical | Oncogene | Rank 3. Cetuximab resistance in pancreatic ductal adenocarcinoma driven by integrin β1 and Src-Akt bypass signalling; co-targeting EGFR and neuropilin-1 overcame it. |
| [30576676](https://pubmed.ncbi.nlm.nih.gov/30576676/) | 2019 | Case report | J Oral Maxillofac Surg | Rank 6. Regression of a metastasis from primary intraosseous carcinoma treated with nivolumab (not cetuximab). |
| [41546361](https://pubmed.ncbi.nlm.nih.gov/41546361/) | 2025 | Case report | Gan to Kagaku Ryoho | Rank 6. Primary intraosseous carcinoma arising in an odontogenic cyst of the mandible. |

Most other publications retrieved were about colorectal, gastric, pancreatic or head and neck cancer rather than the predicted indications, and are not listed.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10262D | Erbitux | Solution for I.V. infusion, 100 mg in 20 mL | Not listed in the data compiled for this report |

---

## Safety Considerations

**Drug Interactions** (20 records; 2 Major, 17 Moderate and 1 target-pharmacology record):

- **Major:** aminolevulinic acid, thalidomide.
- **Moderate, acid suppressants:** rabeprazole, omeprazole, dexlansoprazole, esomeprazole, lansoprazole, pantoprazole.
- **Moderate, antineoplastics:** capecitabine, carboplatin, cisplatin, fluorouracil, oxaliplatin, idelalisib, omacetaxine mepesuccinate.
- **Moderate, photosensitising agents:** methoxsalen, verteporfin, topical aminolevulinic acid, topical methyl aminolevulinate.

Cetuximab acts on its target, EGFR.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction, childhood bronchial adenomas/carcinoids, rests on a model score alone with no supporting trials or literature (L5).
- Cystic neoplasm and pre-malignant neoplasm have early-phase trial evidence (L2) and could be taken forward as research questions. Their evidence is largely indirect, comes from small early-phase studies, and does not show efficacy.

**To proceed, the following is needed:**
- Mechanism of action data for cetuximab.
- Warnings and contraindications from the TGA-approved PI, and the approved indication text for the ARTG entry.
- For the rank 1 prediction, any biological or clinical rationale linking EGFR blockade to childhood bronchial carcinoids.
- For cystic neoplasm, the efficacy results of the salivary gland Phase II study (PMID 18804410) and NCT01192087, and a more specific disease definition.
- For pre-malignant neoplasm, published results of NCT00524017, plus a risk-benefit assessment of giving an EGFR antibody for chemoprevention.
- Confirmation that the epiglottis neoplasm prediction is not already covered by the existing head and neck squamous cell carcinoma indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

