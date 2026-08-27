---
layout: default
title: Imipramine
parent: 僅模型預測 (L5)
nav_order: 345
evidence_level: L5
indication_count: 10
---

# Imipramine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Imipramine: From Depression (Tricyclic Antidepressant Class) to Attention-Deficit/Hyperactivity Disorder

## One-Sentence Summary

Imipramine is a tricyclic antidepressant (TCA); this evidence pack does not include a confirmed original-indication record or DrugBank MOA text for the drug. The TxGNN model predicts a **99.90% likelihood** of efficacy for **Attention-Deficit/Hyperactivity Disorder (ADHD)**, but the supporting evidence is limited to 1 registered trial (assessed as clinically irrelevant) and 20 publications, mostly older reviews and case-level reports rather than a completed controlled trial of imipramine specifically in ADHD.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in this evidence pack (no DrugBank/TFDA license record); Imipramine is identified as a tricyclic antidepressant (TCA) per the repurposing rationale |
| Predicted New Indication | Attention-Deficit/Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (DrugBank MOA lookup is flagged as a High-severity data gap). Based on the information that is available, Imipramine is a tricyclic antidepressant that inhibits noradrenaline (NE) reuptake. This NE-reuptake mechanism partially overlaps with atomoxetine, a currently approved non-stimulant ADHD therapy — which is the pharmacological basis for the TxGNN prediction.

Historically, TCAs such as desipramine and imipramine were used as second-line agents for ADHD before atomoxetine's approval, and several of the retrieved publications (e.g. PMID 6849467, "Imipramine for attention deficit disorder") reflect this historical use. However, the literature set is dominated by general ADHD treatment reviews rather than imipramine-specific comparative trials, and the single registered clinical trial identified for this indication (NCT03220308) is a non-pharmacological mindfulness-training study that the evidence pipeline itself graded "C" (not relevant to imipramine). This means the mechanistic rationale is plausible, but direct, current clinical-trial support is essentially absent.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03220308](https://clinicaltrials.gov/study/NCT03220308) | NA | Completed | 103 | Mindfulness-training and mindful-parenting intervention for children with ADHD; a behavioural intervention, not a pharmacological trial of imipramine. Graded "C" (not relevant) by the evidence pipeline. |

No ANZCTR-registered trial was identified for this indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32982805](https://pubmed.ncbi.nlm.nih.gov/32982805/) | 2020 | Review (meta-review) | Frontiers in Psychiatry | Meta-review of antidepressant efficacy/tolerability/safety across paediatric psychiatric disorders including ADHD |
| [15794722](https://pubmed.ncbi.nlm.nih.gov/15794722/) | 2005 | Review | Expert Opinion on Drug Safety | Safety review of non-stimulant ADHD agents, noting TCAs (desipramine, imipramine) as possible options when stimulants fail |
| [17078784](https://pubmed.ncbi.nlm.nih.gov/17078784/) | 2006 | Cohort/Expert review | Expert Review of Neurotherapeutics | Notes non-selective NE reuptake inhibitors (desipramine, imipramine) as effective alternatives to stimulants in ADHD |
| [9465283](https://pubmed.ncbi.nlm.nih.gov/9465283/) | 1996 | Cohort | Clinical EEG (electroencephalography) | P300 latency in stimulant-non-responder ADHD children predicted poor response to subsequent imipramine treatment |
| [18304665](https://pubmed.ncbi.nlm.nih.gov/18304665/) | 2008 | Cohort | International Journal of Psychophysiology | EEG effects of imipramine in ADHD children who were non-responsive to stimulant medication |
| [6849467](https://pubmed.ncbi.nlm.nih.gov/6849467/) | 1983 | Case report/Commentary | American Journal of Psychiatry | Early report describing use of imipramine for attention deficit disorder |
| [2258453](https://pubmed.ncbi.nlm.nih.gov/2258453/) | 1990 | Cohort | Journal of Clinical Psychopharmacology | Retrospective comparison in ADHD children on imipramine vs. imipramine+carbamazepine; carbamazepine effect on plasma imipramine levels |
| [2830919](https://pubmed.ncbi.nlm.nih.gov/2830919/) | 1988 | Cohort | Biological Psychiatry | Platelet imipramine-binding studied in ADHD boys; no difference vs. controls, unaffected by methylphenidate response |
| [31776871](https://pubmed.ncbi.nlm.nih.gov/31776871/) | 2019 | Review (DDI) | CNS Drugs | Systematic review of pharmacokinetic drug-drug interactions for ADHD pharmacotherapy agents |
| [10790990](https://pubmed.ncbi.nlm.nih.gov/10790990/) | 1999 | Review | Evidence Report/Technology Assessment | Evidence assessment of long- and short-term effectiveness/safety of pharmacological and non-pharmacological ADHD interventions |

---

## Australia Market Information

Currently no ARTG entries — Imipramine is not marketed in Australia under this evidence pack's regulatory data (0 licenses recorded).

---

## Safety Considerations

Imipramine is not currently registered in Australia, so there is no TGA-approved Product Information for this indication pathway to reference. This evidence pack flags the absence of TFDA-sourced warnings/contraindications as a **Blocking** data gap (DG001) — it explicitly prevents the drug from entering the S1 safety initial-assessment stage. No drug-drug interaction records were found (query status: not found). Safety evaluation cannot proceed until label-level warning and contraindication data is obtained from a regulatory source.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited to mechanism-level/historical case data (L4) with no completed controlled trial of imipramine specifically in ADHD, the one registered trial identified is clinically irrelevant, and Imipramine is not currently marketed in Australia (0 ARTG entries). Most critically, the absence of TFDA/regulatory safety data is a Blocking gap that prevents even a preliminary (S1) safety assessment.

**To proceed, the following is needed:**
- TFDA product label data (warnings and contraindications) — Blocking gap (DG001)
- Confirmed DrugBank mechanism-of-action record — High-priority gap (DG002)
- A dedicated controlled trial comparing imipramine against current ADHD standard-of-care (e.g. atomoxetine, stimulants)
- Assessment of the regulatory pathway required, given Imipramine is currently unregistered in Australia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

