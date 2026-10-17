---
layout: default
title: Ondansetron
parent: Model Prediction Only (L5)
nav_order: 529
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ondansetron: predicted new indication Tourette syndrome (evidence level L5). Approved use: Not stated in the data compiled for this report (ondansetron is a 5-H…"
monitor_inn: "Ondansetron"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "Tourette syndrome", "trichotillomania", "schizotypal personality disorder", "schizoid personality disorder", "histrionic personality disorder (disease)", "paranoid personality disorder", "common cold", "allergic urticaria", "acute intermittent porphyria"]
---

# Ondansetron
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

# Ondansetron: From Nausea and Vomiting to Tourette Syndrome

## One-Sentence Summary

Ondansetron is a 5-HT3 receptor antagonist, marketed in Australia as Zofran tablets. The TxGNN model predicts it may be effective for **Tourette syndrome** (the highest-ranked prediction with clinical evidence; the top-ranked prediction overall, nephrogenic syndrome of inappropriate antidiuresis, has no supporting data). This direction is supported by **1 completed clinical trial** and **11 publications**, including two RCTs.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (ondansetron is a 5-HT3 antagonist antiemetic) |
| Predicted New Indication | Tourette syndrome (selected as the best-supported prediction; rank 2 of 10) |
| TxGNN Prediction Score | 97.96% (rank 1 prediction, nephrogenic syndrome of inappropriate antidiuresis: 98.65%, with no evidence) |
| Evidence Level | L1 (as assigned in the data; see caveat below) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold (treat as a research question pending trial results) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, ondansetron is a selective 5-HT3 receptor antagonist, widely used to prevent and treat nausea and vomiting.

5-HT3 receptors modulate dopaminergic activity in mesolimbic and striatal circuits, which are implicated in tics and obsessive-compulsive spectrum symptoms. This gives a plausible mechanistic basis for use in Tourette syndrome. A 2025 RCT also tested whether ondansetron modulates an interoceptive-sensorimotor circuit linked to the sensory phenomena that drive repetitive behaviours.

The link between antiemesis and tics is not a classic indication-to-indication relationship. It rests on neuropharmacology rather than disease similarity.

**Note on the top-ranked prediction:** nephrogenic syndrome of inappropriate antidiuresis (score 98.65%) has no trials or literature. The disease arises from activating AVPR2 mutations, and 5-HT3 antagonism has no recognised role. It is likely a graph-based artefact. Other lower-ranked predictions (trichotillomania, personality disorders, common cold, allergic urticaria, acute intermittent porphyria) also have no meaningful supporting evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03239210](https://clinicaltrials.gov/study/NCT03239210) | Phase 4 | Completed | 110 | Ondansetron 24 mg/day vs placebo for 4 weeks in obsessive-compulsive and tic disorders, with MRI and symptom assessments. Results not provided in the data compiled, so efficacy is unconfirmed. |

No ANZCTR trial identifiers were available.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39876680](https://pubmed.ncbi.nlm.nih.gov/39876680/) | 2025 | RCT | Am J Psychiatry | 4 weeks of high-dose ondansetron vs placebo on sensory phenomena and brain connectivity in OCD and tic disorders. Outcome data were truncated in the data compiled. |
| [15816793](https://pubmed.ncbi.nlm.nih.gov/15816793/) | 2005 | RCT | J Clin Psychiatry | 3-week randomised, double-blind, placebo-controlled study of ondansetron in Tourette's disorder. Outcome data were not available. |
| [10565805](https://pubmed.ncbi.nlm.nih.gov/10565805/) | 1999 | Open-label pilot | Int Clin Psychopharmacol | Six haloperidol-resistant men with Tourette's treated with ondansetron, assessed with YGTSS, Y-BOCS and TS-CGI. |
| [40489853](https://pubmed.ncbi.nlm.nih.gov/40489853/) | 2025 | Review | Medicine | Narrative review of Phase III and IV trials of pharmacological treatments for Tourette's syndrome. |
| [21183132](https://pubmed.ncbi.nlm.nih.gov/21183132/) | 2010 | Review | Semin Pediatr Neurol | Review of RCTs of treatments for tics, Tourette syndrome and stereotypies in autism. |
| [11474424](https://pubmed.ncbi.nlm.nih.gov/11474424/) | 2001 | Review | CNS Drug Rev | Ondansetron and its applications in CNS-related disorders. |
| [18184945](https://pubmed.ncbi.nlm.nih.gov/18184945/) | 2008 | Case report | J Child Neurol | A boy with leukaemia and Tourette syndrome whose tics improved on ondansetron and re-emerged after dose reduction. |
| [16314763](https://pubmed.ncbi.nlm.nih.gov/16314763/) | 2005 | Genetic association study | Psychiatr Genet | HTR3A and HTR3B variants were not associated with Tourette syndrome. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1594X | Zofran | Tablet 4 mg (as hydrochloride dihydrate) | Not available in the data compiled |

## Safety Considerations

- **Disease associations from the knowledge graph (not label text):** long QT syndrome, familial long QT syndrome, torsades de pointes, liver failure, epilepsy, basal ganglia disease, focal hand dystonia and blepharospasm. These should be verified against the Product Information.
- **Drug interactions (DDInter, 100 reported; examples shown):**
  - *Major:* fentanyl, alfentanil, tramadol, dextromethorphan, almotriptan, sumatriptan, amiodarone, amisulpride, amitriptyline, anagrelide. Many involve QT prolongation or serotonin syndrome risk.
  - *Moderate:* abametapir, abiraterone, dihydrocodeine, codeine, famotidine, formoterol, adenosine, salbutamol, alfuzosin, celecoxib.
- **Acute intermittent porphyria:** ondansetron is generally listed as a drug to use with caution in porphyria.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold (research question)**

**Rationale:**
Tourette syndrome has a plausible mechanism and direct controlled-trial evidence (two RCTs and a completed Phase 4 trial). However, the efficacy results are not summarised in the data compiled, and no confirmed Phase 3 RCT is available. The L1 label is therefore a strong signal rather than proof. The other predictions have only model-based support.

**To proceed, the following is needed:**
- Primary outcomes of NCT03239210 and the 2025 RCT (PMID 39876680), and the results of the 2005 RCT
- Mechanism of action data and Australian approved indication text
- TGA PI warnings and contraindications (a blocking data gap), with particular attention to QT prolongation, serotonergic interactions and hepatic impairment
- Dose and formulation considerations, since trials used higher doses (24 mg/day) than the standard antiemetic use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

