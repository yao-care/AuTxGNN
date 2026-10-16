---
layout: default
title: Amitriptyline
parent: Model Prediction Only (L5)
nav_order: 45
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Amitriptyline: predicted new indication Benign paroxysmal torticollis of infancy (evidence level L5). Approved use: Anxiety disorder, neurotic disorder, dysthymic disorder…"
---

# Amitriptyline
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

# Amitriptyline: From Anxiety and Depressive Disorders to Benign Paroxysmal Torticollis of Infancy

## One-Sentence Summary

Amitriptyline is a long-established tricyclic antidepressant, originally used for anxiety disorder, neurotic disorder, dysthymic disorder and mixed anxiety and depressive disorder.
The TxGNN model's top-ranked prediction is **benign paroxysmal torticollis of infancy**, but this prediction has **no clinical trials and no publications** behind it.
The best-supported predictions in the data compiled for this report are depression-related (major depressive disorder and unipolar depression), which are effectively existing uses rather than novel repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anxiety disorder, neurotic disorder, dysthymic disorder, mixed anxiety and depressive disorder (from the knowledge graph; the ARTG entry has no approved indication text) |
| Predicted New Indication | Benign paroxysmal torticollis of infancy |
| TxGNN Prediction Score | 97.72% |
| Evidence Level | L5 (model prediction only) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

**Other predictions in the top 10:**

| Rank | Predicted Indication | Score | Evidence Level | Recommendation |
|---|---|---|---|---|
| 2 | Endogenous depression | 97.71% | L3 | Research Question |
| 3 | Agoraphobia | 97.27% | L4 | Hold |
| 4 | Major depressive disorder | 96.85% | L1 | Proceed with Guardrails |
| 5 | Ohdo syndrome and variants | 95.95% | L5 | Hold |
| 6 | Melancholia | 95.52% | L3 | Research Question |
| 7 | Neurotic depression | 95.48% | L3 | Research Question |
| 8 | Phobic disorder | 94.68% | L4 | Hold |
| 9 | Unipolar depression | 94.61% | L1 | Proceed with Guardrails |
| 10 | Blepharophimosis - intellectual disability syndrome, Ohdo type | 94.47% | L5 | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, amitriptyline is a tricyclic antidepressant that inhibits serotonin and norepinephrine reuptake and also acts on histaminergic and muscarinic receptors (as described in the literature, PMID 33438398). Its efficacy in depression and anxiety-related disorders is established.

**Top-ranked prediction (benign paroxysmal torticollis of infancy):** This is a migraine-equivalent childhood disorder, so a link to amitriptyline's use in migraine prophylaxis is plausible. However, no trial or publication data support it. Paediatric safety, particularly anticholinergic and cardiac effects, would need separate evaluation.

**Depression-related predictions (ranks 2, 4, 6, 7, 9):** These are historical or overlapping subtypes of depression. Because dysthymic disorder and mixed anxiety-depression are already original indications, these predictions are consistent with existing use and offer little novel repurposing value. They are best handled under major depressive disorder.

**Anxiety and phobia predictions (ranks 3, 8):** Serotonergic and noradrenergic antidepressants are used in these conditions, but the retrieved literature mostly concerns other drugs. There is no direct controlled amitriptyline evidence.

**Ohdo syndrome predictions (ranks 5, 10):** These are rare genetic syndromes with no plausible mechanistic path from amitriptyline's pharmacology. They are likely knowledge-graph artefacts.

---

## Clinical Trial Evidence

There are no registered trials for the top-ranked prediction. The table below shows the trials linked to major depressive disorder, the best-supported prediction (the same set also applies to unipolar depression).

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02014363](https://clinicaltrials.gov/study/NCT02014363) | Phase 2 | Completed | 164 | Double-blind non-inferiority study of ETS6103 vs amitriptyline in MDD after unsatisfactory SSRI response |
| [NCT00351910](https://clinicaltrials.gov/study/NCT00351910) | Phase 3 | Completed | 494 | Quetiapine XR add-on to an antidepressant vs antidepressant alone in MDD; amitriptyline's role is not confirmed |
| [NCT01049347](https://clinicaltrials.gov/study/NCT01049347) | Phase 3 | Completed | 127 | HPA-axis and mineralocorticoid receptor study during amitriptyline and paroxetine treatment; mechanistic focus |
| [NCT02237937](https://clinicaltrials.gov/study/NCT02237937) | Phase 4 | Unknown | 80 | ABCB1 genotype-guided dose escalation of antidepressants |
| [NCT05952713](https://clinicaltrials.gov/study/NCT05952713) | N/A | Completed | 73,336 | Real-world comparison of 15 antidepressants in MDD |
| [NCT00325000](https://clinicaltrials.gov/study/NCT00325000) | N/A | Terminated | Not reported | Interpersonal psychotherapy plus pharmacotherapy in severely depressed inpatients |

No ANZCTR identifiers were available in the data compiled for this report.

---

## Literature Evidence

For the top-ranked prediction (benign paroxysmal torticollis of infancy), currently no related literature is available. The table below lists key publications for major depressive disorder.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29477251](https://pubmed.ncbi.nlm.nih.gov/29477251/) | 2018 | Network meta-analysis | Lancet | Comparative efficacy and acceptability of 21 antidepressants in adult MDD |
| [23235671](https://pubmed.ncbi.nlm.nih.gov/23235671/) | 2012 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Amitriptyline versus placebo for MDD |
| [36253442](https://pubmed.ncbi.nlm.nih.gov/36253442/) | 2023 | Network meta-analysis | Mol Psychiatry | Antidepressants in the maintenance phase of MDD |
| [38902199](https://pubmed.ncbi.nlm.nih.gov/38902199/) | 2025 | Dose-response meta-analysis | Chin Med J | Efficacy and dose-response of antidepressants in acute MDD |
| [41290573](https://pubmed.ncbi.nlm.nih.gov/41290573/) | 2025 | Network meta-analysis | Transl Psychiatry | Gastrointestinal effects of antidepressants in MDD |
| [10565798](https://pubmed.ncbi.nlm.nih.gov/10565798/) | 1999 | RCT | Int Clin Psychopharmacol | Fluoxetine vs amitriptyline in anxious depression |
| [7862904](https://pubmed.ncbi.nlm.nih.gov/7862904/) | 1994 | RCT | Psychopharmacology | Nefazodone vs amitriptyline in 106 depressed inpatients; amitriptyline was superior |
| [8739658](https://pubmed.ncbi.nlm.nih.gov/8739658/) | 1996 | RCT | Acta Psychiatr Scand | Paroxetine vs amitriptyline in general practice (n=144); equal efficacy |
| [33438398](https://pubmed.ncbi.nlm.nih.gov/33438398/) | 2021 | Review | ACS Chem Neurosci | Pharmacology of amitriptyline, including its cardiotoxicity concern |
| [38856993](https://pubmed.ncbi.nlm.nih.gov/38856993/) | 2024 | Review | JAMA | Management of depression in adults |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 2417F | ENTRIP | Tablet containing amitriptyline hydrochloride 10 mg (oral) | Not specified in the data compiled for this report |

---

## Safety Considerations

**Contraindications recorded in the knowledge graph** (these come from drug-disease contraindication edges, not from label text):
- Cardiac and conduction: long QT syndrome (including familial), torsades de pointes
- Blood pressure: orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy
- Neurological: epilepsy, basal ganglia disease, focal hand dystonia, blepharospasm
- Psychiatric: manic bipolar affective disorder, psychotic disorders, schizophreniform and schizoaffective disorders, substance abuse/dependence
- Metabolic and organ: porphyria (inherited), kidney disease, liver disease, gallbladder disease, hyperglycaemia, pyoureter
- Haematological: thrombocytopenia, neutropenia, agranulocytosis
- Other: open-angle glaucoma, benign prostatic hyperplasia, female breast carcinoma

**Drug Interactions:** 100 interactions were recorded in total. Examples classed as **Major** include epinephrine, bupropion, cisapride, dexfenfluramine, dolasetron and ephedrine. Examples classed as Moderate include famotidine, cimetidine, clarithromycin, atropine, dicyclomine, activated charcoal and the sulfonylureas acetohexamide and chlorpropamide.

**Other points from the literature:** cardiotoxicity, anticholinergic effects, poorer tolerability than many alternatives, overdose toxicity, and a case report of recreational abuse.

Please refer to the TGA-approved Product Information (PI) for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, benign paroxysmal torticollis of infancy)

**Rationale:**
- The prediction is model-only (L5), with no trials or literature. The migraine-equivalent link is plausible but unsupported by data, and paediatric safety is a concern.
- The depression-related predictions (major depressive disorder and unipolar depression, L1) could be rated **Proceed with Guardrails**, but they are essentially existing uses rather than novel repurposing. Guardrails include anticholinergic burden, cardiac conduction/QT effects, overdose risk and the high interaction burden.

**To proceed, the following is needed:**
- Product Information warnings and contraindications for the Australian product (a blocking gap for safety screening)
- Mechanism of action data
- Approved indication text for the ARTG entry
- For benign paroxysmal torticollis of infancy: literature or case-series evidence on amitriptyline or related migraine prophylaxis in children, plus a paediatric cardiac and anticholinergic safety assessment
- For the depression-related indications: confirmation of amitriptyline's role in the Phase 3 trials (NCT00351910, NCT01049347), whose titles do not show the arms clearly
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

