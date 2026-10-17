---
layout: default
title: Bupropion
parent: Model Prediction Only (L5)
nav_order: 116
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Bupropion: predicted new indication Attention deficit hyperactivity disorder (evidence level L5). Approved use: Major depressive disorder, nicotine dependence"
monitor_inn: "Bupropion"
predicted_indications: ["attention deficit-hyperactivity disorder", "attention deficit hyperactivity disorder, inattentive type", "faciodigitogenital syndrome", "specific developmental disorder", "chondromyxoid fibroma", "proximal 16p11.2 microdeletion syndrome", "hypervitaminosis", "benign paroxysmal torticollis of infancy", "trigeminal nerve neoplasm", "obsolete hypertelorism (disease)"]
---

# Bupropion
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

# Bupropion: From Depression and Smoking Cessation to Attention Deficit Hyperactivity Disorder

## One-Sentence Summary

Bupropion is an antidepressant and smoking cessation aid, originally used for major depressive disorder and nicotine dependence.
The TxGNN model predicts it may be effective for **attention deficit hyperactivity disorder (ADHD)**, with **6 clinical trials** (1 completed Phase 3 randomised trial) and **20 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major depressive disorder, nicotine dependence (the ARTG entry lists no indication text; indications are taken from the TxGNN knowledge graph) |
| Predicted New Indication | Attention deficit hyperactivity disorder |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 (one completed Phase 3 RCT; see note below) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level: the data compiled for this report assigns L1, but only one completed Phase 3 randomised trial (NCT00048360) was identified, and a second trial (NCT00061087) is Phase 2/3 with an unstated study drug. This report therefore rates the evidence as L2 under the stated rules. The decision remains Proceed with Guardrails.*

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, bupropion inhibits the reuptake of norepinephrine and dopamine (an NDRI). These are the same catecholamine pathways targeted by established ADHD medicines, including stimulants and atomoxetine.

Bupropion's original indications (depression and nicotine dependence) involve the same dopaminergic and noradrenergic systems. ADHD is also commonly comorbid with depression and substance use, which is why bupropion has been studied in these overlapping populations. Published reviews describe bupropion as a non-stimulant option, typically considered when stimulants are not tolerated or are unsuitable.

The other nine predictions are weaker. The "inattentive type" is a subtype of ADHD with only indirect evidence. The remaining eight (such as faciodigitogenital syndrome, chondromyxoid fibroma and hypervitaminosis) have no plausible mechanism, no trials and no relevant literature, and appear to be model artefacts. This report focuses on the top prediction.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00048360](https://clinicaltrials.gov/study/NCT00048360) | Phase 3 | Completed | 162 | 8-week randomised, double-blind, placebo-controlled trial of extended-release bupropion 300-450 mg/day in adults with ADHD; results not summarised in the data compiled |
| [NCT00936299](https://clinicaltrials.gov/study/NCT00936299) | Phase 4 | Completed | 105 | Bupropion in adolescents with ADHD and substance use disorder |
| [NCT00061087](https://clinicaltrials.gov/study/NCT00061087) | Phase 2/3 | Completed | 115 | Treatment of adult ADHD in methadone-maintained patients (study drug not stated) |
| [NCT01270555](https://clinicaltrials.gov/study/NCT01270555) | Not applicable | Completed | 32 | Open-label study of bupropion SR in adults with ADHD and recent or current substance use disorders |
| [NCT00000268](https://clinicaltrials.gov/study/NCT00000268) | Not applicable | Completed | 32 | Cocaine abuse and attention deficit disorder; supportive evidence only |
| [NCT04553263](https://clinicaltrials.gov/study/NCT04553263) | Early Phase 1 | Withdrawn | 0 | Relapse prevention in stimulant use disorder; no participants enrolled, so no evidence |

No ANZCTR trial identifiers were available in the data compiled for this report.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28965364](https://pubmed.ncbi.nlm.nih.gov/28965364/) | 2017 | Cochrane review | Cochrane Database Syst Rev | Bupropion for ADHD in adults, as an alternative where stimulants are not tolerated or not optimal |
| [30097390](https://pubmed.ncbi.nlm.nih.gov/30097390/) | 2018 | Systematic review / network meta-analysis | Lancet Psychiatry | Comparative efficacy and tolerability of ADHD medications across age groups |
| [33085721](https://pubmed.ncbi.nlm.nih.gov/33085721/) | 2020 | Systematic review / network meta-analysis | PLoS One | Comparative effects of pharmacologic treatments for adults with ADHD |
| [40203844](https://pubmed.ncbi.nlm.nih.gov/40203844/) | 2025 | Systematic review / network meta-analysis | Lancet Psychiatry | Comparative cardiovascular safety of ADHD medications |
| [37405312](https://pubmed.ncbi.nlm.nih.gov/37405312/) | 2023 | Review | Health Psychol Res | Bupropion pharmacology and effects in depression, ADHD and smoking cessation |
| [38915262](https://pubmed.ncbi.nlm.nih.gov/38915262/) | 2024 | Review | Expert Rev Neurother | Non-stimulant medications for adults with ADHD |
| [39172673](https://pubmed.ncbi.nlm.nih.gov/39172673/) | 2024 | Review | Am Fam Physician | Overview of ADHD diagnosis and management in adults |
| [26601963](https://pubmed.ncbi.nlm.nih.gov/26601963/) | 2016 | Review | Curr Pharm Des | Effects and side effects of ADHD drugs, including bupropion |
| [27738872](https://pubmed.ncbi.nlm.nih.gov/27738872/) | 2017 | Network meta-analysis | Mol Neurobiol | Efficacy and safety of ADHD treatments in children and adolescents |
| [17136226](https://pubmed.ncbi.nlm.nih.gov/17136226/) | 2006 | Review | Drugs Today | Bupropion overview; main mechanism is dopamine and noradrenaline reuptake inhibition |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 8465M | Zyban | Sustained-release tablet containing bupropion hydrochloride 150 mg (oral) | Not recorded in the data compiled |

Only one single-ingredient licence is registered, and none are cancelled. Zyban is the smoking cessation brand. ADHD is not an approved indication in the data compiled for this report.

## Safety Considerations

Product Information warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for authoritative safety information.

**Contraindications suggested by the knowledge graph (not label text, and requiring PI verification):**
- Seizure disorders (epilepsy) and central nervous system tumours
- Eating disorders (anorexia nervosa, bulimia nervosa)
- Bipolar mania, psychotic disorders and schizophrenia-spectrum disorders
- Hypertension, recent myocardial infarction
- Liver disease, cirrhosis and liver failure; kidney disease
- Substance dependence, including opiate dependence

**Drug interactions:** 100 interactions were identified. The main Major-level interactions in the first 20 listed are:
- Opioids: fentanyl, alfentanil, codeine, dihydrocodeine and tramadol
- Lidocaine
- Methylphenidate (relevant if combined with stimulants for ADHD)
- Hydrocortisone
- Aldesleukin
- Amantadine

Moderate-level interactions include alcohol (ethanol), alprazolam, nifedipine, hydrochlorothiazide, cetirizine, chlorpheniramine and alfuzosin.

Seizure risk and cardiovascular effects (blood pressure) deserve particular attention in an ADHD population.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
There is a completed Phase 3 placebo-controlled trial and a Cochrane review of bupropion for adult ADHD, supported by a plausible dopaminergic and noradrenergic mechanism. However, the evidence base is limited. It consists of one Phase 3 trial with unsummarised results and several small trials in comorbid populations. Bupropion is currently registered in Australia only as Zyban, with no recorded ADHD indication.

**To proceed, the following is needed:**
- Review the PI warnings and contraindications (a blocking data gap), particularly seizure risk and cardiovascular effects
- Obtain the results of NCT00048360 and the Cochrane review conclusions on efficacy and tolerability
- Confirm the mechanism of action from DrugBank
- Define the target population (adults versus adolescents, and comorbid substance use) and compare against first-line stimulants and other non-stimulants
- Check the regulatory pathway for a new indication, including dosing and formulation (the only ARTG entry is a 150 mg sustained-release smoking cessation product)
- Develop an interaction management plan, especially for opioids and stimulants
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

