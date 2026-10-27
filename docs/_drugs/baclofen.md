---
layout: default
title: Baclofen
parent: Model Prediction Only (L5)
nav_order: 79
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Baclofen: predicted new indication Attention deficit hyperactivity disorder (evidence level L5). Approved use: Not stated in the ARTG data compiled for this report (baclofen is a w…"
monitor_inn: "Baclofen"
predicted_indications: ["attention deficit-hyperactivity disorder", "nicotine dependence", "attention deficit hyperactivity disorder, inattentive type", "myofascial pain syndrome", "faciodigitogenital syndrome", "trigeminal nerve neoplasm", "methemoglobinemia", "chondromyxoid fibroma", "methemoglobinemia, alpha type", "specific developmental disorder"]
---

# Baclofen
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

## Baclofen: From Spasticity (Intrathecal Use) to Attention Deficit Hyperactivity Disorder
{: .text-alpha }

## One-Sentence Summary

Baclofen is a GABA-B receptor agonist marketed in Australia as an intrathecal injection. The TxGNN model predicts it may be effective for **attention deficit hyperactivity disorder (ADHD)**, but this prediction has **no clinical trials** and only **9 publications**, none of which tests baclofen in ADHD patients. Of the other predicted indications, **nicotine dependence** has the strongest evidence (3 Phase 2 trials), and it is discussed below as a more promising direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the ARTG data compiled for this report (baclofen is a well-established antispastic agent; intrathecal use is for severe spasticity) |
| Predicted New Indication | Attention deficit hyperactivity disorder |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L4 (preclinical and indirect literature only) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

**Other predicted indications (for context):**

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|------|------|------|------|
| 2 | Nicotine dependence | 99.19% | L2 | Research question |
| 3 | ADHD, inattentive type | 98.89% | L5 | Hold |
| 4 | Myofascial pain syndrome | 98.87% | L4 | Research question |
| 5 | Faciodigitogenital syndrome | 98.78% | L5 | Hold |
| 6 | Trigeminal nerve neoplasm | 98.70% | L4 | Hold |
| 7 | Methaemoglobinaemia | 98.33% | L5 | Hold |
| 8 | Chondromyxoid fibroma | 98.15% | L5 | Hold |
| 9 | Methaemoglobinaemia, alpha type | 97.97% | L5 | Hold |
| 10 | Specific developmental disorder | 97.95% | L4 | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Baclofen is known to be a GABA-B receptor agonist and a muscle relaxant. GABA-B signalling can modulate dopaminergic and glutamatergic circuits that are implicated in impulsivity, which offers a plausible but indirect link to ADHD.

However, the retrieved literature is mostly about Tourette syndrome, tic disorders and rodent studies of impulsivity and neurotransmitter agonists. None of it shows baclofen being tested in people with ADHD. The link between spasticity treatment and ADHD is weak, and the high TxGNN score is not supported by clinical data.

By contrast, the **nicotine dependence** prediction has a clearer rationale. The GABAergic system modulates mesolimbic dopamine release and nicotine reward, and baclofen attenuates nicotine reward and withdrawal in rodents (PMIDs 24553576, 18682277).

## Clinical Trial Evidence

**ADHD (the lead prediction):** Currently no related clinical trials registered.

**Nicotine dependence (rank 2, shown for context):**

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01228994](https://clinicaltrials.gov/study/NCT01228994) | Phase 2 | Terminated | 6 | Baclofen vs placebo for smoking abstinence. Terminated with only 6 participants, so uninformative on efficacy |
| [NCT00257894](https://clinicaltrials.gov/study/NCT00257894) | Phase 2 | Terminated | 41 | Effect of baclofen on smoking urge, withdrawal and reinforcement in moderate to heavy smokers. Termination limits interpretation |
| [NCT01821560](https://clinicaltrials.gov/study/NCT01821560) | Phase 2 | Completed | 44 | Baclofen effects on brain responses (fMRI) and behaviour to smoking cues. The most informative mechanistic and clinical evidence available |

**Myofascial pain syndrome (rank 4, shown for context):**

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05617118](https://clinicaltrials.gov/study/NCT05617118) | N/A | Unknown | 52 | Oral baclofen vs botulinum toxin A injections in myofascial pelvic pain. No results reported |

No ANZCTR trial identifiers were available in the data compiled for this report.

## Literature Evidence

**ADHD (the lead prediction):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35345730](https://pubmed.ncbi.nlm.nih.gov/35345730/) | 2022 | Meta-analysis | Cureus | Behavioural, antipsychotic and alpha-agonist treatments for tics in Tourette's syndrome. ADHD is mentioned only as a comorbidity |
| [24295630](https://pubmed.ncbi.nlm.nih.gov/24295630/) | 2013 | Review | Int Rev Neurobiol | Emerging treatments in Tourette syndrome. ADHD is a common comorbidity |
| [11393328](https://pubmed.ncbi.nlm.nih.gov/11393328/) | 2001 | Review | Paediatr Drugs | Clinical features and management of Tourette syndrome |
| [10342599](https://pubmed.ncbi.nlm.nih.gov/10342599/) | 1999 | Review | J Child Neurol | Baclofen with botulinum toxin A in 450 patients with tics or Tourette's. Not an ADHD study |
| [21300040](https://pubmed.ncbi.nlm.nih.gov/21300040/) | 2011 | Preclinical (animal) | Brain Res | EEG responses to neurotransmitter agonists in a rat model of ADHD and epilepsy |
| [24062084](https://pubmed.ncbi.nlm.nih.gov/24062084/) | 2014 | Preclinical (animal) | Psychopharmacology | Alpha-2A stimulation in the ventral hippocampus reduces impulsive decision-making (guanfacine, not baclofen) |

The remaining retrieved items are a methylphenidate off-label prescribing study and rodent behavioural studies, none of which assess baclofen in ADHD.

**Nicotine dependence (rank 2, selected, shown for context):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29250815](https://pubmed.ncbi.nlm.nih.gov/29250815/) | 2018 | Review | Pharmacotherapy | Current and emerging pharmacotherapies for smoking cessation |
| [24654737](https://pubmed.ncbi.nlm.nih.gov/24654737/) | 2014 | Review | Expert Opin Emerg Drugs | Emerging drugs for tobacco dependence |
| [24553576](https://pubmed.ncbi.nlm.nih.gov/24553576/) | 2014 | Preclinical (animal) | Psychopharmacology | Baclofen attenuates nicotine reward and withdrawal in rodents |
| [18682277](https://pubmed.ncbi.nlm.nih.gov/18682277/) | 2008 | Preclinical (animal) | Neurosci Lett | Baclofen effects on nicotine conditioned reward and discrimination in rats |
| [38555115](https://pubmed.ncbi.nlm.nih.gov/38555115/) | 2024 | Review | Int Rev Neurobiol | Repurposing drugs for alcohol use disorder, including baclofen |
| [34601742](https://pubmed.ncbi.nlm.nih.gov/34601742/) | 2021 | Guideline | Med J Aust | New Australian guidelines for the treatment of alcohol problems |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11126N | Sintetica Baclofen Intrathecal | Intrathecal injection 10 mg in 5 mL | Not available in the data compiled for this report |

Note: the only ARTG-listed product is an intrathecal injection, which is a specialist route. Any oral use in ADHD, nicotine dependence or myofascial pain would require a different formulation and route.

## Safety Considerations

**Contraindications flagged by the knowledge graph (not label text):** epilepsy, kidney disease, psychotic disorder, schizophrenia and related disorders (schizophreniform, schizoaffective), mental disorder, stroke and cerebrovascular disorder, cerebral infarction, autonomic nervous system disease (including autonomic dysreflexia and Horner syndrome), pyoureter, and disease of the neck of the urinary bladder.

These are relevant to the lead prediction, because ADHD populations commonly have psychiatric comorbidities.

**Drug Interactions:** 100 interactions were identified. The main ones are:
- **Major:** morphine and liposomal morphine (additive CNS and respiratory depression)
- **Moderate:** dronabinol, nabilone, metoclopramide, opium, sibutramine, difenoxin, diphenoxylate

For the full warnings and precautions, please refer to the TGA-approved Product Information (PI).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- For ADHD, the high TxGNN score is not backed by any clinical trial. The literature is limited to Tourette syndrome reviews and animal studies, and the mechanistic link is indirect. Knowledge-graph contraindications for psychiatric disorders add further caution.
- Among the other predictions, nicotine dependence (L2, three Phase 2 trials, two terminated early) is the most credible research question, and myofascial pain is a secondary one. Neither is ready for a Go decision.

**To proceed, the following is needed:**
- Mechanism of action data (for example, from DrugBank)
- The TGA Product Information, including warnings and contraindications, and the approved indication text for the ARTG entry
- For ADHD: any clinical evidence of baclofen in ADHD patients, or a decision to redirect effort to a better-supported indication
- For nicotine dependence: adequately powered randomised trials, and a review of oral formulation availability, since the only ARTG product is intrathecal
- For myofascial pain: results from NCT05617118
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

