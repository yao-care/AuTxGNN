---
layout: default
title: Thalidomide
parent: Model Prediction Only (L5)
nav_order: 717
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Thalidomide: predicted new indication Ganglioneuroblastoma (evidence level L5). Approved use: Plasma cell myeloma"
---

# Thalidomide
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

# Thalidomide: From Plasma Cell Myeloma to Ganglioneuroblastoma

## One-Sentence Summary

Thalidomide was originally used to treat plasma cell myeloma (multiple myeloma). The TxGNN model's top-ranked prediction is **Ganglioneuroblastoma**, but this prediction has **no clinical trials and no publications** behind it. The best-supported prediction in the data compiled for this report is **Neuroblastoma** (3 clinical trials, 12 publications), which is therefore the focus of the evidence sections below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Plasma cell myeloma (approved indication text is not recorded in the ARTG data compiled) |
| Predicted New Indication | Ganglioneuroblastoma (rank 1); neuroblastoma (rank 4) is the best-evidenced related prediction |
| TxGNN Prediction Score | 98.96% (ganglioneuroblastoma); 98.66% (neuroblastoma) |
| Evidence Level | L5 (ganglioneuroblastoma); L2 (neuroblastoma) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold (ganglioneuroblastoma); Proceed with Guardrails, as a research question only (neuroblastoma) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on published literature, thalidomide has anti-angiogenic and immunomodulatory effects, including inhibition of TNF-alpha and cereblon-mediated protein degradation (for example Ikaros and Aiolos). These actions underlie its use in plasma cell myeloma.

Ganglioneuroblastoma is a neural crest tumour closely related to neuroblastoma. The high graph score for ganglioneuroblastoma has no direct supporting evidence. Any plausible link is inferred from neuroblastoma, where thalidomide has been studied.

For neuroblastoma, preclinical work shows thalidomide is anti-angiogenic in a xenograft model (PMID 14612937). It also potentiates etoposide-induced apoptosis in murine neuroblastoma, with suppression of NF-kB suggested (PMID 29423589). Clinical data come from Phase 2 trials in which thalidomide was one part of a multi-drug regimen, so its individual contribution cannot be isolated. No Phase 3 trial exists.

Several other high-scoring predictions (vertebral anomalies syndrome, brachydactyly-syndactyly syndrome, colobomatous microphthalmia syndrome) appear to reflect overlap with thalidomide's teratogenic limb-malformation phenotype rather than therapeutic benefit. They should not be treated as repurposing candidates.

## Clinical Trial Evidence

No trials are linked to ganglioneuroblastoma. The trials below are linked to neuroblastoma.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00357500](https://clinicaltrials.gov/study/NCT00357500) | Phase 2 | Completed | 101 | Oral 5-drug anti-angiogenic regimen (thalidomide, celecoxib, fenofibrate, etoposide, cyclophosphamide) in relapsed or progressive cancer. Thalidomide's effect is not isolated. |
| [NCT00098865](https://clinicaltrials.gov/study/NCT00098865) | Phase 2 | Completed | 15 | Thalidomide with temozolomide in relapsed or progressive brain tumours or neuroblastoma. Small sample. |
| [NCT00049296](https://clinicaltrials.gov/study/NCT00049296) | Phase 1 | Completed | 26 | Pharmacokinetics and safety of thalidomide with docetaxel in advanced cancer. No efficacy signal for neuroblastoma. |

## Literature Evidence

Publications linked to neuroblastoma (no literature is linked to ganglioneuroblastoma):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24123865](https://pubmed.ncbi.nlm.nih.gov/24123865/) | 2014 | Phase 2 trial | Pediatr Blood Cancer | Multi-agent oral metronomic antiangiogenic regimen in children with recurrent or progressive cancer |
| [14612937](https://pubmed.ncbi.nlm.nih.gov/14612937/) | 2003 | Preclinical (xenograft) | Int J Oncol | Thalidomide is anti-angiogenic in a neuroblastoma xenograft model |
| [29423589](https://pubmed.ncbi.nlm.nih.gov/29423589/) | 2018 | Preclinical (murine) | Pediatr Surg Int | Thalidomide potentiates etoposide-induced apoptosis via NF-kB suppression |
| [18024879](https://pubmed.ncbi.nlm.nih.gov/18024879/) | 2007 | Case report | J Clin Oncol | Report of successful antiangiogenic therapy for neuroblastoma with thalidomide |
| [10882863](https://pubmed.ncbi.nlm.nih.gov/10882863/) | 2000 | Review | Eur J Cancer | Thalidomide as an "accidental" anti-angiogenic drug |
| [27329811](https://pubmed.ncbi.nlm.nih.gov/27329811/) | 2016 | Preclinical (mechanistic) | Biochem Biophys Res Commun | Nuclear cereblon modulates Ikaros activity in human neuroblastoma cells |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 6469L | Thalomid | Capsule 50 mg | Not recorded in the data compiled |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunomodulatory agent (thalidomide analogue class), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions. Neutropenia and agranulocytosis appear among the drug-disease contraindication edges. |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Full blood count with differential; neurological assessment for peripheral neuropathy; thromboembolism surveillance |
| Handling Protection | Please refer to the PI. Teratogenic risk applies, so pregnancy prevention requirements are critical. |

## Safety Considerations

- **Contraindication signals (knowledge graph, not label text):** multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, epilepsy, neutropenia, agranulocytosis, peripheral nervous system disease, peripheral neuropathy, pulmonary embolism.
- **Drug interactions:** 100 interactions were identified; the first 20 reviewed are listed below.
  - **Major:** hydrocortisone, triamcinolone, dexamethasone, betamethasone, prednisone.
  - **Moderate:** famotidine, ranitidine, cimetidine, nizatidine, morphine, metronidazole, clarithromycin, levofloxacin, picosulfuric acid, dolasetron, palonosetron, ondansetron, metoclopramide, dronabinol, nabilone.
- **Teratogenicity:** thalidomide is a known teratogen that causes severe limb and other malformations, and this risk applies to any new use. Literature in the data also highlights irreversible axonal neuropathy and thromboembolism.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications, as label text was not available in the data compiled.

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, ganglioneuroblastoma). Neuroblastoma may be considered as a **Proceed with Guardrails** research question only.

**Rationale:**
- Ganglioneuroblastoma has a very high model score but no trials or literature (L5), so no clinical recommendation can be made.
- Neuroblastoma has L2 support from small Phase 2 combination studies and preclinical data. Thalidomide's individual contribution is unproven and no Phase 3 evidence exists.

**To proceed, the following is needed:**
- Mechanism of action data and the TGA-approved PI (warnings, contraindications, approved indication text).
- Direct evidence in ganglioneuroblastoma, or a defensible rationale extrapolated from neuroblastoma.
- Controlled studies isolating thalidomide's contribution in neuroblastoma.
- A risk management plan covering teratogenicity, neuropathy, thromboembolism and haematological monitoring, with attention to paediatric use.

**Other predictions in brief:**
- **Rheumatoid arthritis (L3):** historical uncontrolled studies only, and modern TNF-targeted biologics make a niche doubtful.
- **Myeloid leukaemia (L2):** small Phase 2 studies, several in myelodysplastic syndromes rather than leukaemia.
- **Indolent plasma cell myeloma (L2):** an extension within the original disease spectrum.
- **Acute lymphoblastic leukaemia (L3):** no efficacy evidence.
- **Retroperitoneal neoplasm (L4):** case reports only.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

