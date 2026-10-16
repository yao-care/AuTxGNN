---
layout: default
title: Buprenorphine
parent: Model Prediction Only (L5)
nav_order: 115
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Buprenorphine: predicted new indication Schizophrenia (evidence level L5). Approved use: Opioid dependence"
monitor_inn: "Buprenorphine"
predicted_indications: ["acute intermittent porphyria", "lingual-facial-buccal dyskinesia", "chronic tic disorder", "continuous spikes and waves during sleep", "benign shuddering attacks", "extrapyramidal and movement disease", "schizophreniform disorder", "schizophrenia", "benign paroxysmal tonic upgaze of childhood with ataxia", "psychogenic movement disorders"]
---

# Buprenorphine
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

# Buprenorphine: From Opioid Dependence to Schizophrenia

## One-Sentence Summary

Buprenorphine is a partial mu-opioid agonist originally used to treat opioid dependence.
The TxGNN model predicts it may be effective for **schizophrenia** (the highest-evidence prediction among the top 10 candidates), with **1 Phase 2 clinical trial** (recruiting, no results yet) and **20 publications** currently supporting this direction. Most of that literature is indirect.

> Note: The top-ranked TxGNN prediction is acute intermittent porphyria. It has only a single perioperative case report and no therapeutic evidence, so this report focuses on schizophrenia, the best-supported candidate.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Opioid dependence (also substance abuse/dependence and morphine dependence, per the knowledge graph; the ARTG entry carries no indication text) |
| Predicted New Indication | Schizophrenia |
| TxGNN Prediction Score | 98.98% |
| Evidence Level | L2 (provisional: one Phase 2 trial, recruiting, no results) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold (research question only) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the literature retrieved, buprenorphine is a mu-opioid partial agonist with kappa-opioid receptor antagonist activity. Its efficacy in opioid dependence is well established.

Dynorphin and kappa-opioid receptor dysregulation has been described in schizophrenia. Kappa antagonism and mu partial agonism may modulate mesolimbic dopamine and reward circuitry, which could plausibly affect social motivation and negative symptoms. This is a hypothesis, not a demonstrated effect.

The direct clinical signal is limited. A small 1987 study (10 patients, neuroleptic-free) reported an antipsychotic effect lasting about 4 hours. A 2020 meta-analysis of placebo-controlled trials reported symptom reduction with opioid antagonists, including buprenorphine, but this is indirect evidence. Safety concerns about misuse and dependence liability in this population also remain.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05778591](https://clinicaltrials.gov/study/NCT05778591) | Phase 2 | Recruiting (2024-05 to 2027-03) | 40 | Low-dose buprenorphine as a modulator of social motivation in schizophrenia. No results yet. |

No ANZCTR registrations were identified in the data compiled for this report.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32516800](https://pubmed.ncbi.nlm.nih.gov/32516800/) | 2020 | Meta-analysis | Neuropsychopharmacology | Placebo-controlled trials of naloxone, naltrexone, nalmefene and buprenorphine; opioid antagonists associated with reduced schizophrenia symptoms (indirect) |
| [3310672](https://pubmed.ncbi.nlm.nih.gov/3310672/) | 1987 | Small early clinical study | Am J Psychiatry | 10 neuroleptic-free patients; pronounced antipsychotic effect lasting about 4 hours |
| [33459877](https://pubmed.ncbi.nlm.nih.gov/33459877/) | 2022 | Review | Handb Exp Pharmacol | Role of dynorphin and kappa-opioid receptor dysfunction in schizophrenia and depression |
| [31101511](https://pubmed.ncbi.nlm.nih.gov/31101511/) | 2019 | Review | Schizophr Res | Methadone and buprenorphine treatment in patients with schizophrenia |
| [34286498](https://pubmed.ncbi.nlm.nih.gov/34286498/) | 2021 | Systematic review | Eur Rev Med Pharmacol Sci | Psychosis reported after withdrawal from buprenorphine and other opioids |
| [15982997](https://pubmed.ncbi.nlm.nih.gov/15982997/) | 2005 | Review | J Psychopharmacol | Rationale for partial agonism in psychiatric disorders |
| [25392062](https://pubmed.ncbi.nlm.nih.gov/25392062/) | 2014 | Case report/Review | J Dual Diagn | Opiate dependence in schizophrenia |
| [37934551](https://pubmed.ncbi.nlm.nih.gov/37934551/) | 2023 | Case report | J Addict Med | Extended-release depot buprenorphine in a patient with OUD and psychosis under a community treatment order |
| [40600600](https://pubmed.ncbi.nlm.nih.gov/40600600/) | 2026 | Case report | J Addict Med | Olanzapine/samidorphan and buprenorphine as a contradictory combination |
| [36873095](https://pubmed.ncbi.nlm.nih.gov/36873095/) | 2023 | Preclinical | Addiction Neuroscience | Buprenorphine, methadone and cariprazine in a monkey opioid-versus-food choice task |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10746N | Norspan | Transdermal patch 40 mg | Not available in the data compiled for this report |

## Cytotoxicity

Not applicable. Buprenorphine is not an antineoplastic drug.

## Safety Considerations

- **Contraindications and conditions of concern (knowledge-graph associations, not label text):**
  - Cardiac: long QT syndrome (familial and acquired), torsades de pointes
  - Respiratory: respiratory failure, COPD
  - Hepatic: liver disease, chronic hepatitis B and C
  - Neurological: raised intracranial pressure (intracranial hypertension, pseudotumor cerebri)
  - Gastrointestinal: paralytic ileus, intestinal obstruction
  - Endocrine: adrenocortical insufficiency, hypothyroidism
  - Autonomic: orthostatic hypotension, multiple system atrophy
  - Other: drug dependence and substance-related disorders, benign prostatic hyperplasia, urethral stricture, gallbladder disease
- **Drug interactions** (DDInter; 100 recorded, 20 reviewed here):
  - **Major:** alvimopan, bupropion, morphine, cisapride, dolasetron
  - **Moderate:** famotidine, cimetidine, clarithromycin, aprepitant, dexamethasone, anticholinergics (atropine, hyoscyamine, glycopyrronium, dicyclomine, clidinium), loperamide, bisacodyl, castor oil, clotrimazole, dexfenfluramine
- **Disease-specific concerns:**
  - Misuse and dependence liability in people with schizophrenia.
  - Psychosis has been reported after buprenorphine withdrawal.
  - Opioid antagonists such as samidorphan can precipitate withdrawal.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications. These were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold (research question only)**

**Rationale:**
- Schizophrenia is the best-supported prediction, but the only direct evidence is one small, ongoing Phase 2 trial with no results and a 1987 pilot study. The other nine predictions have either no evidence or only off-topic literature. Buprenorphine's dependence liability and withdrawal-related psychosis add safety concerns.

**To proceed, the following is needed:**
- Results from NCT05778591 and, if positive, confirmatory randomised controlled trials
- Detailed mechanism of action data (MOA)
- TGA Product Information warnings and contraindications for Norspan and any other relevant formulation
- Route and formulation assessment: the only ARTG entry is a weekly transdermal pain patch, which may not suit a low-dose psychiatric use
- A safety plan covering misuse risk, withdrawal and the QT-prolonging and CNS-depressant interactions listed above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

