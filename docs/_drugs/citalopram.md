---
layout: default
title: Citalopram
parent: Model Prediction Only (L5)
nav_order: 164
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Citalopram: predicted new indication Obsessive-compulsive disorder (evidence level L5). Approved use: Major depressive disorder, unipolar and endogenous depression…"
---

# Citalopram
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

# Citalopram: From Depression and Anxiety Disorders to Obsessive-Compulsive Disorder

## One-Sentence Summary

Citalopram is a selective serotonin reuptake inhibitor (SSRI) originally used for depressive and anxiety disorders.
The TxGNN model predicts it may be effective for **obsessive-compulsive disorder (OCD)**,
with **4 clinical trials** (none confirmed to test citalopram directly) and **16 publications** (several citalopram-specific) currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major depressive disorder, unipolar and endogenous depression, dysthymic disorder, anxiety disorder, neurotic disorder (the Australian ARTG entry lists no indication text) |
| Predicted New Indication | Obsessive-compulsive disorder |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L1 (see note below) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* The L1 grade reflects a completed Phase 3 trial in the data compiled for this report. That trial studied serotonin reuptake inhibitors as a class and does not name citalopram. The citalopram-specific evidence is mostly open-label or small studies, so the grade should be read as class-level support.

## Why is This Prediction Reasonable?

Detailed mechanism of action data for citalopram is not available in the data compiled for this report. Citalopram is a well-known SSRI, and OCD is known to respond to serotonin reuptake inhibition. The mechanistic link is therefore inferred from the drug class.

The original indications (depression and anxiety disorders) and OCD share serotonergic involvement. Serotonin reuptake inhibitors are a standard pharmacological approach in OCD. The literature includes citalopram-specific studies in adults with treatment-resistant OCD, citalopram concentration-response data, and open-label trials in children and adolescents. The high TxGNN score is consistent with this clinical picture.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | Completed | 124 | CBT added to serotonin reuptake inhibitor treatment in children with OCD who partially responded. Citalopram is not named, so this supports class-level evidence only. |
| [NCT02022709](https://clinicaltrials.gov/study/NCT02022709) | Phase 4 | Completed | 78 | Exposure and response prevention, SSRIs, and the combination in OCD, with predictors of response in a Chinese population. Citalopram is not confirmed as the specific agent. |
| [NCT00680602](https://clinicaltrials.gov/study/NCT00680602) | Phase 4 | Completed | 158 | Group CBT versus fluoxetine in OCD. Fluoxetine is the comparator, so relevance to citalopram is indirect. |
| [NCT02285699](https://clinicaltrials.gov/study/NCT02285699) | NA | Completed | 43 | Pilot study of gut microbiota in OCD versus healthy controls, before and after 12 weeks of open-label SSRI treatment. It does not test citalopram efficacy. |

No ANZCTR identifiers were available in the data compiled for this report.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10572334](https://pubmed.ncbi.nlm.nih.gov/10572334/) | 1999 | Clinical study (randomised, open-label) | Eur Psychiatry | Citalopram alone versus citalopram plus clomipramine in 16 adults with treatment-resistant OCD |
| [9241005](https://pubmed.ncbi.nlm.nih.gov/9241005/) | 1997 | Single-blind study | J Clin Psychopharmacol | Compared antiobsessional efficacy of fluvoxamine, paroxetine and citalopram in 30 patients |
| [15089116](https://pubmed.ncbi.nlm.nih.gov/15089116/) | 2004 | Cohort | CNS Drugs | Preliminary data on citalopram concentrations and clinical response in OCD |
| [9395151](https://pubmed.ncbi.nlm.nih.gov/9395151/) | 1997 | Open pilot study | Acta Psychiatr Scand | 24-week open pilot of citalopram in OCD |
| [12839522](https://pubmed.ncbi.nlm.nih.gov/12839522/) | 2003 | Open-label study | Psychiatry Clin Neurosci | 8-week open-label citalopram (mean 24 mg/day) in 15 children and adolescents with OCD |
| [9466233](https://pubmed.ncbi.nlm.nih.gov/9466233/) | 1997 | Open-label trial | J Child Adolesc Psychopharmacol | 23 children and adolescents on citalopram for 10 weeks. Y-BOCS/CY-BOCS scores fell from 30 to 21 (p < 0.001). |
| [10471169](https://pubmed.ncbi.nlm.nih.gov/10471169/) | 1999 | Review | Int Clin Psychopharmacol | Overview of citalopram for OCD and the link between serotonin reuptake inhibitors and OCD |
| [12607204](https://pubmed.ncbi.nlm.nih.gov/12607204/) | 2000 | Review | World J Biol Psychiatry | Serotonin and other neurobiological factors in OCD |
| [22305974](https://pubmed.ncbi.nlm.nih.gov/22305974/) | 2012 | Review | BMJ Clin Evid | Epidemiology and course of OCD |
| [20712565](https://pubmed.ncbi.nlm.nih.gov/20712565/) | 2010 | Review | Curr Med Chem | Past, present and future drugs for OCD, centred on SSRIs |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14313H | Celapram | Tablet 10 mg (as hydrobromide), oral | Not available in the data compiled for this report |

## Safety Considerations

Product Information warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for label safety information.

**Disease associations from the knowledge graph (not label text):** The knowledge graph links citalopram with contraindication edges for the following conditions: long QT syndrome (including familial), torsades de pointes, epilepsy, bipolar disorder and major affective disorder, liver disease, gallbladder disease, potassium deficiency, blood coagulation disorders, heart and cardiovascular disease, neuroleptic malignant syndrome, inappropriate ADH syndrome (including nephrogenic), and serotonin syndrome. These should be verified against the PI.

**Drug Interactions:** The interaction query returned 100 records. Major-level interactions among those listed include:
- Bupropion
- Omeprazole
- Cimetidine
- Clarithromycin
- Cisapride
- Dolasetron
- Lorcaserin
- Dexfenfluramine
- Diethylpropion

Moderate-level examples include morphine, acetylsalicylic acid, famotidine and loperamide. Minor-level examples include aprepitant and clotrimazole. Several of these are QT-prolonging or serotonergic agents, which is consistent with the QT and serotonin syndrome associations above.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
OCD responds to serotonin reuptake inhibition, and citalopram-specific studies in adults and children are supportive. However, they are mostly small and open-label, and the registered trials do not directly test citalopram. The evidence supports further evaluation rather than a clear Go.

**To proceed, the following is needed:**
- Citalopram-specific randomised, controlled evidence in OCD (current evidence is open-label, small, or class-level)
- Confirmation of the approved indications in the TGA Product Information, since no indication text was available for the ARTG entry
- Review of the PI warnings and contraindications, particularly QT prolongation, serotonin syndrome, and suicidality in young patients
- Detailed mechanism of action data
- A dose-appropriate safety and interaction monitoring plan, given the many Major-level interactions

## Other Predicted Indications (Brief Note)

- **Agoraphobia (Proceed with Guardrails, L2):** Evidence is indirect, through panic disorder. Citalopram studies in panic disorder with or without agoraphobia exist, plus a Cochrane network meta-analysis.
- **Melancholia (Hold, L1):** It is a depression subtype already covered by the existing indication, so it adds little repurposing value.
- **Personality disorders (schizoid, schizotypal, histrionic, paranoid), Ohdo syndrome variants, and benign paroxysmal torticollis of infancy (Hold, L4-L5):** These are model predictions with no supporting clinical evidence and no plausible mechanistic link.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

