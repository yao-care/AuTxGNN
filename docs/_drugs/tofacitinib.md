---
layout: default
title: Tofacitinib
parent: Model Prediction Only (L5)
nav_order: 735
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Tofacitinib: predicted new indication Colobomatous microphthalmia-rhizomelic dysplasia syndrome (evidence level L5). Approved use: Rheumatoid arthritis"
monitor_inn: "Tofacitinib"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "indolent plasma cell myeloma", "plasma cell myeloma", "myeloid leukemia", "ganglioneuroblastoma (disease)", "marcothrombocytopenia with mitral valve insufficiency", "hereditary thrombocytopenia with normal platelets", "vertebral anomalies and variable endocrine and T-cell dysfunction", "retroperitoneal neoplasm"]
---

# Tofacitinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Tofacitinib: From Rheumatoid Arthritis to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome
{: .text-alpha }

## One-Sentence Summary

Tofacitinib is an oral Janus kinase (JAK) inhibitor, originally used to treat rheumatoid arthritis.
The TxGNN model ranks **colobomatous microphthalmia-rhizomelic dysplasia syndrome** as its top prediction, but this is a computational prediction only, with **no clinical trials** and **no publications** supporting it.
The best-supported alternative signal in the data is **plasma cell myeloma**, which has preclinical evidence only (see the note below the Quick Overview).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis (the ARTG entry in the data compiled for this report has no approved indication text) |
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 98.96% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

**Note on other predictions:** Plasma cell myeloma (TxGNN 96.09%) and myeloid leukaemia (95.43%) are rated L4 with a "Research Question" status, because they have preclinical evidence. Both remain well short of clinical-level support.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the data compiled for this report. Based on known information, tofacitinib is a pan-JAK inhibitor (mainly JAK1/JAK3) that blocks JAK/STAT cytokine signalling. Its efficacy in rheumatoid arthritis is established.

For the top-ranked prediction, colobomatous microphthalmia-rhizomelic dysplasia syndrome, **no plausible mechanistic link** to JAK/STAT signalling was identified. It is a rare developmental syndrome, and the high score reflects a graph-based prediction only. The second-ranked prediction (brachydactyly-syndactyly syndrome, 98.88%) is in the same position.

The more biologically plausible directions are haematological:
- **Plasma cell myeloma:** IL-6/JAK/STAT3 signalling promotes myeloma cell survival and growth. A 2018 preclinical study reported that tofacitinib may reverse the growth-promoting effects of the bone marrow microenvironment.
- **Myeloid leukaemia:** JAK/STAT signalling is implicated in myeloid malignancies. Preclinical work shows JAK3 inhibition enhancing imatinib activity in chronic myeloid leukaemia (CML) cells.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked indication, or for any of the 10 predicted indications.

---

## Literature Evidence

No literature is available for the top-ranked indication. The table below lists the most relevant publications for the next-best-supported predictions (plasma cell myeloma and myeloid leukaemia). Most of this evidence is preclinical, and several items are safety signals rather than efficacy evidence.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29622655](https://pubmed.ncbi.nlm.nih.gov/29622655/) | 2018 | Preclinical (in vitro) | Haematologica | Repurposing tofacitinib as an anti-myeloma agent to reverse growth-promoting effects of the bone marrow microenvironment (plasma cell myeloma) |
| [29458040](https://pubmed.ncbi.nlm.nih.gov/29458040/) | 2018 | Preclinical (in vitro) | Eur J Pharmacol | JAK3 inhibition enhances the antitumour activity of imatinib in CML cells (myeloid leukaemia) |
| [26300391](https://pubmed.ncbi.nlm.nih.gov/26300391/) | 2015 | Preclinical (cell line) | Eur J Pharmacol | JAK inhibitors alter gene expression and cell cycle in AML cell lines with JAK2 mutation (myeloid leukaemia) |
| [38992456](https://pubmed.ncbi.nlm.nih.gov/38992456/) | 2024 | Preclinical (mechanistic) | Arch Biochem Biophys | Ponatinib and tofacitinib modulate aryl hydrocarbon receptor activity (myeloid leukaemia) |
| [34693224](https://pubmed.ncbi.nlm.nih.gov/34693224/) | 2021 | Preclinical (cell line) | iScience | JAK inhibitors including tofacitinib reduced SLFN11 expression in leukaemia cells with JAK pathway mutations (myeloid leukaemia) |
| [39819734](https://pubmed.ncbi.nlm.nih.gov/39819734/) | 2025 | Cohort (retrospective) | BMC Rheumatol | Examines DMARD use and risk of multiple myeloma in US Veterans with rheumatoid arthritis; a safety-context study (plasma cell myeloma) |
| [38071595](https://pubmed.ncbi.nlm.nih.gov/38071595/) | 2024 | Cohort/Epidemiologic | J Eur Acad Dermatol Venereol | FDA adverse event database study linking immunosuppressants and haematologic malignancy to sebaceous carcinoma; a safety signal (plasma cell myeloma) |
| [31263618](https://pubmed.ncbi.nlm.nih.gov/31263618/) | 2019 | Case report | Case Rep Rheumatol | CML arising in a patient receiving tofacitinib; a safety/causality concern, not efficacy evidence (myeloid leukaemia) |
| [22777068](https://pubmed.ncbi.nlm.nih.gov/22777068/) | 2012 | Review | Z Rheumatol | Overview of new kinase inhibitors in rheumatoid arthritis; limited relevance (myeloid leukaemia) |
| [37352275](https://pubmed.ncbi.nlm.nih.gov/37352275/) | 2023 | Preclinical (compound screening) | Blood Adv | Compares mono- vs coculture for high-throughput drug screening in haematological malignancies; limited relevance (myeloid leukaemia) |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10511F | Xeljanz | Tablet 5 mg (oral) | Not available in the data compiled for this report |

---

## Safety Considerations

- **Drug Interactions:** The interaction screen returned 100 interactions in total. Major-level interactions listed among the first 20 entries are mostly with corticosteroids: hydrocortisone, triamcinolone (including ophthalmic), dexamethasone, betamethasone, budesonide, prednisone and prednisolone. Clarithromycin is also rated Major. Moderate interactions include aprepitant, morphine (including liposomal), opium, aspirin, omeprazole, esomeprazole, lansoprazole and miconazole. Zinc sulfate and zinc acetate are Minor.
- **Malignancy signals:** The literature includes reports of malignancy (CML, sebaceous carcinoma) in people exposed to tofacitinib or other immunosuppressants. Causality is not established, but this is relevant to any oncology-related repurposing.
- **Immune deficiency:** For the T-cell dysfunction syndrome (rank 9), tofacitinib's immunosuppression could worsen the underlying immune deficiency.

For warnings and contraindications, please refer to the TGA-approved Product Information (PI).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction is supported only by a graph-based score, with no clinical trials, no literature and no identifiable mechanistic link to JAK inhibition (Evidence Level L5). The more biologically plausible directions, plasma cell myeloma and myeloid leukaemia, have preclinical evidence only (L4) and are best treated as research questions, not near-term clinical options.

**To proceed, the following is needed:**
- Detailed mechanism of action data
- TGA PI warnings and contraindications, and the approved indication text for the Xeljanz ARTG entry
- A mechanistic rationale, or supporting experimental data, for the top-ranked rare syndromes
- For plasma cell myeloma, further preclinical validation and a review of the malignancy-risk signals before considering early-phase clinical studies
- Assessment of route compatibility (currently pending for all predicted indications)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

