---
layout: default
title: Mechlorethamine
parent: 僅模型預測 (L5)
nav_order: 419
evidence_level: L5
indication_count: 10
---

# Mechlorethamine
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

# Mechlorethamine: From Hodgkin Lymphoma to Lymph Node Cancer

## One-Sentence Summary

> Mechlorethamine (nitrogen mustard, DrugBank DB00888) is historically the prototype alkylating chemotherapy agent, classically used as part of the MOPP regimen for Hodgkin lymphoma and as a topical gel for cutaneous T-cell lymphoma (based on general pharmacological knowledge — not confirmed against this evidence pack's Taiwan/Australia regulatory data).
> The TxGNN model predicts continued/expanded efficacy for **lymph node cancer** (broad lymphoma category) with a **99.43%** prediction score, supported by **50 registered clinical trials** (relevance not yet graded) and **20 literature references**, several of which directly involve mechlorethamine-containing regimens (e.g., MOPP) in Hodgkin lymphoma.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Taiwan/Australia regulatory data (drug not marketed, 0 ARTG entries). Based on general pharmacological knowledge, mechlorethamine is classically indicated for Hodgkin lymphoma (MOPP regimen) and cutaneous T-cell lymphoma (topical gel) |
| Predicted New Indication | Lymph node cancer |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L2 (historical randomized cooperative-group trials of mechlorethamine-containing regimens exist in the literature, though not tagged with formal phase data; the 50 registered clinical trials in this pack are largely unrelated regimens and remain ungraded for relevance) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not returned in this evidence pack (flagged as a High-severity data gap). Based on general pharmacological knowledge, mechlorethamine is a bifunctional alkylating agent (nitrogen mustard) that cross-links DNA, triggering apoptosis preferentially in rapidly dividing lymphoid cells. It is the original component of the MOPP regimen (mechlorethamine, vincristine, procarbazine, prednisone), one of the first combination chemotherapy regimens shown to cure advanced-stage Hodgkin lymphoma.

"Lymph node cancer" as predicted by TxGNN is essentially synonymous with nodal lymphoma — the disease category mechlorethamine was originally developed and used for. This is therefore less a novel repurposing signal and more a reflection of the drug's well-established historical role, which the literature evidence in this pack supports directly (e.g., randomized EORTC/GPMC cooperative-group trials of MOPP-based regimens in Hodgkin's disease).

The mechanistic plausibility is high: cytotoxic alkylation of DNA in malignant lymphocytes is a validated approach across Hodgkin lymphoma, non-Hodgkin lymphoma, and cutaneous T-cell lymphoma (mycosis fungoides), the latter also supported by literature on topical mechlorethamine/chlormethine gel. However, most of the 50 registered trials returned for this indication concern unrelated modern regimens (rituximab-based immunochemotherapy, CAR-T, HSCT conditioning) in breast cancer, NSCLC, and various lymphomas — not mechlorethamine itself — and their relevance has not yet been graded.

---

## Clinical Trial Evidence

*Note: the trials below are drawn from a broad "lymph node cancer" search and mostly evaluate contemporary regimens (rituximab-based chemoimmunotherapy, targeted agents) rather than mechlorethamine directly; relevance grading is still pending in the source data.*

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01611090](https://clinicaltrials.gov/study/NCT01611090) | Phase 3 | Completed | 578 | Ibrutinib + bendamustine/rituximab vs. bendamustine/rituximab in relapsed/refractory CLL/SLL |
| [NCT01732926](https://clinicaltrials.gov/study/NCT01732926) | Phase 3 | Terminated | 475 | Idelalisib + bendamustine/rituximab in previously treated indolent NHL (terminated on safety signal) |
| [NCT03462719](https://clinicaltrials.gov/study/NCT03462719) | Phase 3 | Active, not recruiting | 211 | Ibrutinib + venetoclax vs. chlorambucil + obinutuzumab, first-line CLL/SLL |
| [NCT00254163](https://clinicaltrials.gov/study/NCT00254163) | Phase 3 | Completed | 184 | Fludarabine/cyclophosphamide/rituximab vs. pentostatin/cyclophosphamide/rituximab in B-cell CLL |
| [NCT02162771](https://clinicaltrials.gov/study/NCT02162771) | Phase 3 | Completed | 140 | CT-P10 (rituximab biosimilar) + CVP vs. Rituxan + CVP in advanced follicular lymphoma |
| [NCT00301821](https://clinicaltrials.gov/study/NCT00301821) | Phase 2 | Completed | 107 | Epratuzumab + rituximab-CHOP in previously untreated diffuse large B-cell lymphoma |
| [NCT00092222](https://clinicaltrials.gov/study/NCT00092222) | Phase 2 | Active, not recruiting | 75 | Oncolytic virotherapy/natural history study of KSHV-associated multicentric Castleman disease |
| [NCT06854003](https://clinicaltrials.gov/study/NCT06854003) | Phase 2 | Recruiting | 60 | Bendamustine, rituximab, cytarabine + zanubrutinib induction/maintenance in treatment-naïve mantle cell lymphoma |
| [NCT04660799](https://clinicaltrials.gov/study/NCT04660799) | Phase 2 | Completed | 50 | Subcutaneous vs. intravenous rituximab + CHOP in CD20+ diffuse large B-cell lymphoma |
| [NCT03586999](https://clinicaltrials.gov/study/NCT03586999) | Phase 1/2 | Completed | 18 | Nivolumab + standard-of-care chemotherapy as first-line therapy for peripheral T-cell lymphoma |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7509381](https://pubmed.ncbi.nlm.nih.gov/7509381/) | 1994 | RCT | J Clin Oncol | EORTC/GPMC randomized trial comparing MOPP alone vs. MOPP/ABVD alternation in Stage IIIB/IV Hodgkin's disease |
| [3352775](https://pubmed.ncbi.nlm.nih.gov/3352775/) | 1988 | RCT | NCI Monographs | EORTC H5 study comparing total nodal irradiation vs. mantle irradiation + mechlorethamine/vincristine/procarbazine/prednisone in Stage I-II Hodgkin's disease |
| [7540419](https://pubmed.ncbi.nlm.nih.gov/7540419/) | 1995 | Prospective study | Annals of Oncology | Hybrid MOPP/ABVD plus radiotherapy in advanced Hodgkin's disease |
| [24438970](https://pubmed.ncbi.nlm.nih.gov/24438970/) | 2014 | Review | J Am Acad Dermatol | Primary cutaneous T-cell lymphoma (mycosis fungoides/Sézary syndrome) — prognosis, management, future directions |
| [31894937](https://pubmed.ncbi.nlm.nih.gov/31894937/) | 2020 | Review | American Family Physician | Lymphoma: diagnosis and treatment overview |
| [35393251](https://pubmed.ncbi.nlm.nih.gov/35393251/) | 2022 | Retrospective cohort | Clin Lymphoma Myeloma Leuk | Chlormethine (mechlorethamine) gel maintenance regimen in mycosis fungoides — single-centre experience |
| [6809030](https://pubmed.ncbi.nlm.nih.gov/6809030/) | 1982 | Cohort | Br J Dermatol | Cutaneous T-cell lymphoma outcomes in 92 patients treated with electron-beam irradiation, topical mechlorethamine (HN2), or PUVA |
| [9881077](https://pubmed.ncbi.nlm.nih.gov/9881077/) | 1998 | Review | Gan To Kagaku Ryoho | Chemotherapy for non-Hodgkin's lymphoma |
| [20564093](https://pubmed.ncbi.nlm.nih.gov/20564093/) | 2010 | Cohort | Cancer | Hodgkin lymphoma involving extranodal and nodal head and neck sites — characteristics and outcomes |
| [5001851](https://pubmed.ncbi.nlm.nih.gov/5001851/) | 1971 | Review | CA Cancer J Clin | The management of lymphoma |

---

## Australia Market Information

Mechlorethamine currently has **no ARTG entries** and is **not marketed in Australia**. No product-specific dosage form, brand name, or approved indication text is available from Taiwan/Australia regulatory sources in this evidence pack.

---

## Cytotoxicity

Mechlorethamine is a conventional cytotoxic chemotherapy agent (nitrogen mustard alkylator), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — nitrogen mustard alkylating agent class |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions — drug-specific toxicity data was not returned in this evidence pack |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the Product Information (PI) warnings and precautions |
| Handling Protection | As an alkylating cytotoxic agent, standard cytotoxic drug handling precautions would be expected to apply; confirm against the TGA-approved PI once available |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No key warnings, contraindications, or drug interaction data were returned in this evidence pack (a Blocking-severity gap has been logged against TFDA label warnings/contraindications).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Efficacy evidence for nitrogen-mustard-class regimens in nodal lymphoma is historically well established (randomized MOPP-based trials in Hodgkin's disease), but a **Blocking** data gap on TFDA/PI warnings and contraindications means safety pre-screening (S1) cannot even begin. The drug also has zero ARTG entries and is not currently marketed in Australia.

**To proceed, the following is needed:**
- TFDA/TGA-approved Product Information (PI) with full warnings and contraindications (resolves the Blocking gap)
- Confirmed mechanism-of-action data from DrugBank or an equivalent authoritative source
- Relevance grading of the 50 registered clinical trials currently marked "pending," to confirm which (if any) actually test mechlorethamine rather than unrelated regimens
- Route-of-administration compatibility assessment (IV vs. topical gel) for the specific target indication
- A TGA registration pathway assessment, given there are currently no ARTG entries for this drug
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

