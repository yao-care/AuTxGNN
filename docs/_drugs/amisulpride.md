---
layout: default
title: Amisulpride
parent: Model Prediction Only (L5)
nav_order: 44
evidence_level: L5
indication_count: 10
---

# Amisulpride
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

# Amisulpride: From Schizophrenia to Schizophrenia (Validation of an Existing Use)

## One-Sentence Summary

Amisulpride is an atypical antipsychotic (a selective dopamine D2/D3 antagonist), and the Australian licence data compiled for this report do not state an approved indication.
The TxGNN model predicts it may be effective for **schizophrenia**, which is in fact its established use in many markets, so this is a validation of an existing use rather than true repurposing.
The data compiled include **35 clinical trials** and **20 publications** for this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Australian licence data (the approved indication text is blank) |
| Predicted New Indication | Schizophrenia |
| TxGNN Prediction Score | 96.05% |
| Evidence Level | L1 (as assigned in the compiled data; see the note under Clinical Trial Evidence) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data were not available in the source record. From the supporting analysis, amisulpride selectively blocks dopamine D2 and D3 receptors, and also antagonises 5-HT7 receptors. D2 antagonism is the established basis of antipsychotic efficacy.

Published reviews describe a dual action. At higher doses, amisulpride blocks postsynaptic receptors in the limbic areas, which may reduce positive symptoms. At low doses, it blocks presynaptic autoreceptors, which may enhance dopaminergic transmission and help negative symptoms.

Because the original indication field is empty, the on-label status in Australia should be confirmed against the TGA-approved Product Information. The prediction is best read as confirming a known use, not a new one.

Other predicted indications in the data (ranks 2 to 10) are summarised briefly below.
- **Psychotic disorder (rank 5):** A broader category of the same use. It shares the same trial set, so the evidence is not independent.
- **Dysthymic disorder (rank 8):** The most credible genuinely new direction. Low-dose amisulpride (50 mg/day) was compared with placebo, amineptine, amitriptyline, fluoxetine and others in several published studies, and a 2021 systematic review examined its effect on depressive symptoms. Evidence level is provisionally L2 and the recommendation is "Research Question".
- **Anxiety disorder (rank 10):** Weak, indirect evidence only. Evidence level is L3 and the recommendation is "Research Question".
- **Retinal dystrophy, X-linked and syndromic myopias, hydranencephaly, and polymicrogyria syndrome (ranks 2, 3, 4, 6, 7, 9):** No trials or literature and no plausible mechanism. These are likely model artefacts, and the recommendation is "Hold".

## Clinical Trial Evidence

The table lists the 10 most relevant trials for schizophrenia, selected on the relevance grades in the compiled data. Many other registered trials were not graded.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01609153](https://clinicaltrials.gov/study/NCT01609153) | Phase 4 | Completed | 328 | COMBINE: randomised, double-blind trial of olanzapine plus amisulpride versus olanzapine alone in acutely ill schizophrenia |
| [NCT01246232](https://clinicaltrials.gov/study/NCT01246232) | Phase 4 | Completed | 69 | Amisulpride augmentation in clozapine-unresponsive schizophrenia |
| [NCT01105481](https://clinicaltrials.gov/study/NCT01105481) | Phase 4 | Completed | 273 | 14-week randomised, double-blind, placebo-controlled amisulpride augmentation in clozapine-resistant schizophrenia |
| [NCT00331981](https://clinicaltrials.gov/study/NCT00331981) | Phase 4 | Completed | 138 | Long-term efficacy and safety of amisulpride on positive and negative symptoms, quality of life and cognition |
| [NCT00245674](https://clinicaltrials.gov/study/NCT00245674) | Phase 4 | Completed | 300 | Amisulpride oral solution in the first days of an acute schizophrenic episode |
| [NCT01795183](https://clinicaltrials.gov/study/NCT01795183) | Phase 4 | Completed | 316 | Open-label multicentre study of effectiveness and safety in Chinese patients |
| [NCT00436371](https://clinicaltrials.gov/study/NCT00436371) | Phase 4 | Completed | 50 | Safety and response of amisulpride in acute-phase schizophrenia (small) |
| [NCT00761670](https://clinicaltrials.gov/study/NCT00761670) | Phase 4 | Completed | 37 | Amisulpride versus risperidone on cognitive function in chronic schizophrenia (small) |
| [NCT01446328](https://clinicaltrials.gov/study/NCT01446328) | Phase 4 | Completed | 151 | Bergen Psychosis Project 2: head-to-head comparison of aripiprazole, amisulpride and olanzapine over 12 months |
| [NCT01615185](https://clinicaltrials.gov/study/NCT01615185) | Phase 4 | Terminated | 96 | Double-blind comparison of amisulpride 800 mg/day versus amisulpride 400 mg/day plus sulpiride 800 mg/day |

Notes:
- The compiled data assign L1, but most amisulpride-specific trials are Phase 4. The Phase 3 trials (NCT03510325, completed, n=762; NCT04528095, status unknown, n=162) are sequential multiple-assignment antipsychotic comparison trials. I could not confirm from the data that amisulpride is a distinct arm in them, so the L1 assignment should be verified.
- Two amisulpride trials were withdrawn with no participants (NCT05956600 and NCT01448499).
- No ANZCTR trial identifiers were present in the data compiled for this report.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23810019](https://pubmed.ncbi.nlm.nih.gov/23810019/) | 2013 | Network meta-analysis | Lancet | Comparative efficacy and tolerability of 15 antipsychotics in schizophrenia |
| [41763745](https://pubmed.ncbi.nlm.nih.gov/41763745/) | 2026 | Network meta-analysis | Lancet | Antidopaminergic and muscarinic antipsychotics in acute schizophrenia |
| [19058842](https://pubmed.ncbi.nlm.nih.gov/19058842/) | 2009 | Meta-analysis | Lancet | Second-generation versus first-generation antipsychotics in schizophrenia |
| [31838873](https://pubmed.ncbi.nlm.nih.gov/31838873/) | 2020 | Dose-response meta-analysis | Am J Psychiatry | Dose-response relationships of antipsychotics in acute schizophrenia |
| [29368205](https://pubmed.ncbi.nlm.nih.gov/29368205/) | 2018 | Systematic review and meta-analysis | Eur Arch Psychiatry Clin Neurosci | Antipsychotics for predominant or prominent negative symptoms |
| [41811299](https://pubmed.ncbi.nlm.nih.gov/41811299/) | 2026 | RCT | JAMA Psychiatry | Clozapine after one failed antipsychotic trial in first-episode psychosis |
| [12076408](https://pubmed.ncbi.nlm.nih.gov/12076408/) | 2002 | Cochrane review | Cochrane Database Syst Rev | Amisulpride for schizophrenia |
| [12418608](https://pubmed.ncbi.nlm.nih.gov/12418608/) | 2002 | Review | Curr Med Res Opin | Amisulpride's D2/D3 profile and effect on positive and negative symptoms |
| [32421188](https://pubmed.ncbi.nlm.nih.gov/32421188/) | 2020 | Expert survey | Schizophr Bull | TRRIP recommendations on clozapine combination and augmentation strategies |
| [36871411](https://pubmed.ncbi.nlm.nih.gov/36871411/) | 2023 | Naturalistic study | Psychiatry Res | Relapse after switching in patients with amisulpride-induced hyperprolactinaemia |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 8594H | Amisulpride Sandoz Pharma | Tablet 100 mg (oral) | Indication text not available in the compiled data |

## Cytotoxicity

Not applicable. Amisulpride is not an antineoplastic drug, so this section is omitted.

## Safety Considerations

Warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for safety information.

**Drug interactions:** A screen returned 100 interactions in total, and the first 20 are in the compiled data. The main ones listed are:
- **Major:** cisapride, clarithromycin, dolasetron, granisetron, levofloxacin and metoclopramide. Most of these are QT-prolonging or dopamine-related combinations, and the interaction details are not given in the data.
- **Moderate:** famotidine, epinephrine, hydrocortisone, amphotericin B (including the lipid complex), several laxatives (bisacodyl, castor oil, glycerin, lactitol, lactulose, magnesium citrate, magnesium hydroxide) and loperamide.
- **Minor:** metronidazole.

The literature also flags hyperprolactinaemia as a recognised adverse effect, and one trial (NCT04446234) is evaluating QTc prolongation. Neither point replaces the PI.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Amisulpride has many completed Phase 4 trials and high-tier meta-analyses supporting its use in schizophrenia, and the mechanism is well established. However, this is confirmation of an existing use, not a new repurposing signal.

**To proceed, the following is needed:**
- Confirmation of the approved indication and the full safety text (warnings, contraindications) from the TGA Product Information, as both were blank in the compiled data.
- Verification of the L1 evidence level, because the Phase 3 trials may not include amisulpride-specific arms.
- Review of the QT-prolongation and hyperprolactinaemia risks, and of the major drug interactions, before any prescribing guidance is issued.
- For dysthymic disorder, full-text review of the key studies (PMIDs 12128243, 9892856, 9495601) and a decision on whether a dedicated research question is warranted. Note these are older studies using low doses (50 mg/day).
- No action is recommended on the other predicted indications, which lack supporting evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

