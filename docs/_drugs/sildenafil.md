---
layout: default
title: Sildenafil
parent: Model Prediction Only (L5)
nav_order: 671
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Sildenafil: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Pulmonary arterial hypertension"
monitor_inn: "Sildenafil"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "hypertrichosis (disease)", "homozygous familial hypercholesterolemia", "hypoalphalipoproteinemia", "familial isolated trichomegaly", "genetic alopecia", "obsolete patella aplasia, coxa vara, and tarsal synostosis"]
---

# Sildenafil
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

# Sildenafil: From Pulmonary Arterial Hypertension and Erectile Dysfunction to Genetic Alopecia

## One-Sentence Summary

Sildenafil is a PDE5 inhibitor originally used for pulmonary arterial hypertension, erectile dysfunction, psychologic dyspareunia and premature ejaculation.
The TxGNN model ranks **Ambras type hypertrichosis universalis congenita** as its top prediction, but the best-supported candidate in the data compiled for this report is **Genetic Alopecia**.
That candidate has **no registered clinical trials** and **1 publication** (preclinical or unspecified design), so the evidence is early.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary arterial hypertension; erectile dysfunction; psychologic dyspareunia; premature ejaculation (the ARTG entry carries no approved indication text) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita (rank 1); the most evidence-supported candidate is Genetic Alopecia (rank 9) |
| TxGNN Prediction Score | 98.41% (rank 1 candidate); 75.03% (genetic alopecia) |
| Evidence Level | L5 (rank 1 candidate); L4 (genetic alopecia) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold (rank 1 candidate); Genetic alopecia is flagged as a research question |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Sildenafil is a known phosphodiesterase type 5 (PDE5) inhibitor. It raises intracellular cGMP, which causes vasodilation. This is the basis of its use in pulmonary arterial hypertension and erectile dysfunction.

**Rank 1 (Ambras type hypertrichosis universalis congenita):** No trials or publications support this prediction. The high score (0.984) is a graph-based association only. Any link would be speculative, through hair-follicle signalling. Ambras syndrome is a rare genetic disorder with a different underlying driver, so a mechanistic basis is not established.

**Genetic alopecia (rank 9):** This is the most plausible candidate. One 2018 publication (PMID 30292404) examines the effect of sildenafil on human hair follicles. The proposed mechanism is cGMP elevation, vasodilation and improved perifollicular blood flow, possibly with effects on dermal papilla cells, similar in spirit to minoxidil. The study design and size are not confirmed in the available data, so this remains preliminary.

**Other top-ranked predictions** (malformation syndromes, Dandy-Walker syndromes, hair shaft abnormalities, homozygous familial hypercholesterolaemia, hypoalphalipoproteinaemia, trichomegaly and a skeletal malformation) have no clinical or literature support. For structural congenital malformations in particular, a postnatal PDE5 inhibitor is not expected to correct the defect.

## Clinical Trial Evidence

Currently no related clinical trials registered for the rank 1 candidate or for genetic alopecia.

## Literature Evidence

Evidence for the rank 1 candidate: currently no related literature available.

Evidence for genetic alopecia (rank 9) and hypertrichosis (rank 5):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30292404](https://pubmed.ncbi.nlm.nih.gov/30292404/) | 2018 | Preclinical/unspecified (design not confirmed) | Biochem Biophys Res Commun | "Novel effect of sildenafil on hair growth." Notes that sildenafil raises cGMP and causes vasodilation, and examines its effect on human hair follicles (effect not stated in the available excerpt). |
| [31175705](https://pubmed.ncbi.nlm.nih.gov/31175705/) | 2019 | Case report | Am J Med Genet A | Glibenclamide in a neonate with Cantú syndrome (ABCC9 gain-of-function variant; hypertrichosis feature). This concerns a different drug, so it is only indirect, tenuous evidence for sildenafil in hypertrichosis. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12138W | Sildenafil Sandoz PHT 20 | Tablet 20 mg (as citrate), oral | Not stated in the data compiled for this report |

## Safety Considerations

The following comes from knowledge-graph contraindication links, not from label text. Please confirm against the TGA-approved Product Information (PI).

- **Disease-level contraindication signals (knowledge graph):** liver failure; aortic stenosis and other aortic valve disease; hypotensive disorders; acute coronary syndrome; myocardial infarction; stroke and cerebrovascular disorders; sickle cell anaemia and other haemoglobinopathies; plasma cell myeloma; leukaemia; priapism; Peyronie disease; hypertrophic cardiomyopathy; anterior ischaemic optic neuropathy; pulmonary veno-occlusive disease; hearing loss disorders; oesophageal dyskinesia.
- **Drug interactions:** 100 interactions were identified in total. Of the 20 shown, the one rated **Major** is **clarithromycin**. Most others are rated Moderate, including aprepitant, morphine, dexamethasone, cimetidine, miconazole, clotrimazole, papaverine, opium, and the SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin). Calcitriol, acarbose and sucralfate are rated Unknown.
- **Hair-related caution:** Hypertrichosis is a known adverse effect of KATP channel openers such as minoxidil, so any hair effect of sildenafil would need direct testing.

Please refer to the TGA-approved PI for the official warnings and contraindications, as label-level data were not available.

## Conclusion and Next Steps

**Decision: Hold** (rank 1 candidate, Ambras type hypertrichosis universalis congenita). Genetic alopecia is flagged as a **research question**.

**Rationale:**
- The top predictions are supported only by graph-based scores, with no clinical trials and no direct literature. Genetic alopecia has a single preliminary sildenafil study with no controlled human data.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) and a mechanistic cross-check
- Full text of PMID 30292404 to confirm study design, model, size and findings
- Clarification of route (topical or systemic), relevance to androgenetic alopecia, and safety at hair-growth doses
- Controlled human studies, or registered trials, in alopecia
- TGA PI warnings and contraindications, and a safety screen against the contraindication and interaction signals above (the ARTG entry carries no indication text)
- Route compatibility assessment, since the only Australian product is an oral 20 mg tablet
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

