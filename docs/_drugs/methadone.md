---
layout: default
title: Methadone
parent: Moderate Evidence (L3-L4)
nav_order: 462
evidence_level: L4
indication_count: 7
last_modified_at: 2026-10-13
description: "Methadone: predicted new indication Tourette syndrome (evidence level L4). Approved use: Not available in the data compiled for this report"
monitor_inn: "Methadone"
predicted_indications: ["Tourette syndrome", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "headache disorder", "manic bipolar affective disorder", "trigeminal autonomic cephalalgia", "common cold"]
---

# Methadone
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **7** 
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

## Methadone: From Opioid Dependence/Pain Management to Tourette Syndrome
{: .text-alpha }

## One-Sentence Summary

Methadone is a synthetic mu-opioid agonist and NMDA receptor antagonist. The data compiled for this report do not include a TGA-approved indication text for the Australian product, though methadone is established in opioid substitution therapy and pain management.
The TxGNN model predicts it may be effective for **Tourette syndrome**, but there are **no registered clinical trials**, and only **1 directly relevant publication** (a 1992 case report) supports this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the ARTG entry has no indication text) |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 0.9976 |
| Evidence Level | L4 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the compiled data. Based on known pharmacology, methadone is a mu-opioid receptor agonist with NMDA receptor antagonist activity. Opioid modulation of dopaminergic and serotonergic (5-HT2A/C) pathways is a plausible link to tic and compulsive symptoms.

Preclinical and review literature notes that opioid drugs have been reported as effective in treatment-refractory obsessive-compulsive disorder and Tourette syndrome. The 5-HT2A-related head-twitch behaviour in animals has been related to tics and compulsive symptoms. A 1992 report describes methadone treatment of Tourette's disorder, but it is old, small and likely case-level.

This is a theoretical link only. The prediction has not been tested in controlled studies, and the original indication text was not available to assess its similarity to Tourette syndrome.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1728167](https://pubmed.ncbi.nlm.nih.gov/1728167/) | 1992 | Case report/series | Am J Psychiatry | Methadone treatment of Tourette's disorder (no abstract available) |
| [17102981](https://pubmed.ncbi.nlm.nih.gov/17102981/) | 2007 | Preclinical/Review | Psychopharmacology | Opiates are effective in treatment-refractory OCD and Tourette syndrome; 5-HT2A/C-mediated behaviour linked to tics and compulsions |
| [15247538](https://pubmed.ncbi.nlm.nih.gov/15247538/) | 2004 | Review | Curr Opin Neurol | Review of non-genetic causes of chorea; indirect relevance |
| [39086469](https://pubmed.ncbi.nlm.nih.gov/39086469/) | 2024 | Review | Palliat Care Soc Pract | Novel analgesics for neuropathic pain in advanced cancer; indirect relevance |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12520Y | METHADONE-AFT | Tablet containing methadone hydrochloride 10 mg | Not available in the compiled data |

---

## Safety Considerations

- **Contraindications (model-related signals, not label text):** The TxGNN model (deep learning) links methadone to contraindications in:
  - Cardiac: long QT syndrome (including familial), torsades de pointes, sudden cardiac arrest, heart conduction disease
  - Respiratory: respiratory failure, asthma
  - Neurological: epilepsy, intracranial hypertension, pseudotumor cerebri
  - Gastrointestinal: paralytic ileus, intestinal obstruction, inflammatory bowel disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, familial visceral myopathy
  - Hepatic/renal/biliary: liver disease, kidney disease, gallbladder disease
  - Endocrine: hypothyroidism, myxedema, congenital hypothyroidism
  - Other: hypotensive disorder, benign prostatic hyperplasia, urethral stricture, pyoureter, substance-related disorder and substance abuse/dependence
- **Drug Interactions:** The interaction query returned 100 interactions; 20 are shown in the compiled data. Major-level interactions include:
  - Alvimopan
  - Bupropion
  - Morphine
  - Dexamethasone
  - Clarithromycin
  - Cisapride
  - Picosulfuric acid
  - Polyethylene glycol (3350 with electrolytes)

  Moderate-level interactions include famotidine, cimetidine, aprepitant, loperamide, atropine, hyoscyamine, glycopyrronium, dicyclomine, clidinium, bisacodyl, castor oil and attapulgite.
- **Other signals from the literature:** Methadone has been associated with bradycardia (case report) and with hyperalgesia and cluster headache at high doses (case series).

Label-based warnings and contraindications were not available. Please refer to the TGA-approved Product Information (PI) for authoritative safety information.

---

## Other Predicted Indications (Context)

The remaining top-10 predictions are weaker or carry no supporting evidence:

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Nephrogenic syndrome of inappropriate antidiuresis | 0.9973 | L5 | Prediction only; mechanistically implausible (V2 receptor mutation) |
| 3 | Trichotillomania | 0.9967 | L5 | Prediction only; an agonist would act opposite to the antagonist approach |
| 4 | Headache disorder | 0.9935 | L4 | Literature mostly on opioid use disorder; guidance discourages opioids |
| 5 | Manic bipolar affective disorder | 0.9932 | L3 | A 1982 small crossover study; otherwise comorbidity data |
| 6 | Trigeminal autonomic cephalalgia | 0.9905 | L4 | Literature reports methadone inducing cluster headache (safety signal) |
| 7 | Common cold | 0.9902 | L5 | Likely keyword artifact |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Tourette syndrome prediction has a high model score, but evidence is limited to a single 1992 case report and indirect preclinical/review literature, with no registered trials. Methadone also carries significant cardiac (QT prolongation), respiratory and dependence risks that require a strong efficacy case before any new use is pursued. It is best treated as a research question rather than a candidate for clinical development.

**To proceed, the following is needed:**
- Retrieval of the TGA Product Information to establish approved indications, warnings and contraindications
- Detailed mechanism of action data (e.g., from DrugBank)
- A systematic literature review beyond the 1992 case report, including any controlled studies in Tourette syndrome
- Comparison with established Tourette treatments (e.g., alpha-2 agonists, antipsychotics, behavioural therapy) to assess a plausible benefit-risk case
- A QT, respiratory depression and dependence-risk assessment in a Tourette population, which is often young
- If pursued, a pilot or Phase 2 study design with ECG monitoring, with ethics and regulatory review (including controlled-substance requirements)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

