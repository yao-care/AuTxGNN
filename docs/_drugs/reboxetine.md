---
layout: default
title: Reboxetine
parent: Model Prediction Only (L5)
nav_order: 628
evidence_level: L5
indication_count: 10
---

# Reboxetine
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

# Reboxetine: From Unipolar Depression to Benign Paroxysmal Torticollis of Infancy

## One-Sentence Summary

Reboxetine is a selective norepinephrine reuptake inhibitor, originally used to treat depression (unipolar, endogenous and major depressive disorder) and anxiety disorder.
The TxGNN model's top-ranked prediction is **benign paroxysmal torticollis of infancy**, but this is a computational prediction only, with **0 clinical trials** and **0 publications** supporting it.
Among the other predictions, **agoraphobia** and **dysthymic disorder** have the most plausible support from the literature (Evidence Level L3).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Unipolar depression, endogenous depression, major depressive disorder, anxiety disorder (from the knowledge graph; the ARTG indication text is not available) |
| Predicted New Indication | Benign paroxysmal torticollis of infancy (top-ranked); see the note below on other candidates |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

**Note on the other candidates:** The top-ranked prediction has no supporting evidence. Two lower-ranked predictions are better supported and are worth a closer look:

| Candidate | TxGNN Score | Evidence Level | Recommendation |
|------|------|------|------|
| Agoraphobia | 99.91% | L3 | Research Question |
| Dysthymic disorder | 99.87% | L3 | Research Question |
| Melancholia | 99.74% | L4 | Research Question (largely an on-label extension) |
| Neurotic depression | 99.74% | L4 | Research Question (legacy term) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the data compiled for this report. Based on known pharmacology, reboxetine is a selective norepinephrine reuptake inhibitor (the pharmacology data show it acts on the norepinephrine transporter, NET, encoded by SLC6A2). Its efficacy in depression is the basis of its original indications, and it may be mechanistically applicable to conditions in which noradrenergic dysregulation plays a role.

**Top-ranked prediction (benign paroxysmal torticollis of infancy):** The high score is a computational result only. No known mechanistic link exists between norepinephrine reuptake inhibition and this paediatric episodic movement disorder, which is associated with CACNA1A channelopathy and the migraine spectrum. Reboxetine is also not established for use in infants. This prediction should not be pursued without new supporting evidence.

**Agoraphobia:** Noradrenergic dysregulation is implicated in panic and anxiety disorders, and agoraphobia is commonly comorbid with panic disorder. Reboxetine has shown activity in panic disorder in a small placebo-controlled study and an open-label study of treatment-refractory patients. Agoraphobia-specific outcomes are not reported separately.

**Dysthymic disorder:** Dysthymia is a chronic depressive disorder closely related to the approved depression indications, so noradrenergic reuptake inhibition is plausible. Dysthymia-specific efficacy data for reboxetine are limited.

**Melancholia and neurotic depression:** These are depression subtypes or legacy terms within the existing indication space, so they are closer to on-label extensions than true repurposing.

**Other predictions (Ohdo syndrome and variants, Ohdo-type blepharophimosis intellectual disability syndrome, Keppen-Lubinsky syndrome, ligneous conjunctivitis, neurotic disorder):** These are prediction only, with no evidence found. The rare genetic conditions have no plausible link to norepinephrine reuptake inhibition.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (for the top-ranked prediction or for any of the ten predicted indications).

---

## Literature Evidence

No literature was found for the top-ranked prediction (benign paroxysmal torticollis of infancy). The most relevant publications for the better-supported candidates are shown below.

**Agoraphobia / panic disorder**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38014714](https://pubmed.ncbi.nlm.nih.gov/38014714/) | 2023 | Network meta-analysis | Cochrane Database Syst Rev | Compares pharmacological treatments for panic disorder in adults; covers agoraphobia only indirectly |
| [11838623](https://pubmed.ncbi.nlm.nih.gov/11838623/) | 2002 | Clinical trial | J Clin Psychiatry | Reboxetine reported as effective and well tolerated in panic disorder |
| [12415550](https://pubmed.ncbi.nlm.nih.gov/12415550/) | 2002 | Open-label study | Hum Psychopharmacol | Reboxetine in panic disorder patients who did not respond to SSRIs |
| [40946318](https://pubmed.ncbi.nlm.nih.gov/40946318/) | 2026 | Systematic review | Psychother Psychosom | Treatment options in treatment-resistant anxiety disorders |
| [26635099](https://pubmed.ncbi.nlm.nih.gov/26635099/) | 2016 | Systematic review | Expert Opin Pharmacother | Treatment-resistant panic disorder |

**Dysthymic disorder**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21527126](https://pubmed.ncbi.nlm.nih.gov/21527126/) | 2011 | Meta-analysis | J Clin Psychiatry | Antidepressant efficacy in dysthymia versus placebo (not reboxetine-specific) |
| [9818623](https://pubmed.ncbi.nlm.nih.gov/9818623/) | 1998 | Review of clinical trials | J Clin Psychiatry | Reviews reboxetine efficacy and tolerability in major depressive disorder and dysthymia |
| [10628889](https://pubmed.ncbi.nlm.nih.gov/10628889/) | 1999 | RCT (double-blind) | J Affect Disord | Reboxetine versus imipramine in elderly patients with depressive disorders |
| [15358987](https://pubmed.ncbi.nlm.nih.gov/15358987/) | 2004 | Clinical study | J Psychopharmacol | Effects of reboxetine on sleep and nocturnal cardiac autonomic activity in dysthymia (12 patients, single-blind) |
| [10616869](https://pubmed.ncbi.nlm.nih.gov/10616869/) | 1999 | Pilot study | J Geriatr Psychiatry Neurol | Tolerability of reboxetine up to 8 mg/day in 12 elderly patients with major depression or dysthymia |

**Melancholia / neurotic depression (general depression evidence)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29477251](https://pubmed.ncbi.nlm.nih.gov/29477251/) | 2018 | Network meta-analysis | Lancet | Compares 21 antidepressants in MDD; reboxetine tended to rank lower for efficacy and acceptability |
| [19185342](https://pubmed.ncbi.nlm.nih.gov/19185342/) | 2009 | Network meta-analysis | Lancet | Compares 12 newer antidepressants in major depression |
| [20940209](https://pubmed.ncbi.nlm.nih.gov/20940209/) | 2010 | Systematic review and meta-analysis | BMJ | Reboxetine versus placebo or SSRIs in acute depression, assessing publication bias |
| [23007832](https://pubmed.ncbi.nlm.nih.gov/23007832/) | 2012 | Review | Clin Ter | Reboxetine in clinical practice; not approved in the US |
| [10901157](https://pubmed.ncbi.nlm.nih.gov/10901157/) | 2000 | Review | Acta Psychiatr Scand Suppl | Tolerability and safety profile of reboxetine in major depression |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14474T | Edronax | Tablet 4 mg (as mesilate) | Not available in the data compiled for this report |

---

## Safety Considerations

- **Drug Interactions:** The data compiled for this report include only a pharmacology-based target entry (reboxetine acting on the norepinephrine transporter, NET). No clinically graded drug-drug interactions were identified.
- **Supporting literature notes:** One review reports no significant cardiovascular effects, a low potential for drug interactions and no increase in suicidal ideation in reboxetine-treated patients (PMID 10901157). A 2010 BMJ meta-analysis raised concerns about publication bias in reboxetine trials (PMID 20940209).

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications, as this information was not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (benign paroxysmal torticollis of infancy) rests on a model score alone, with no trials, no literature and no plausible mechanism, and reboxetine is not established in infants. Agoraphobia and dysthymic disorder have modest supporting evidence (L3) but are better treated as research questions than as candidates for clinical adoption.

**To proceed, the following is needed:**
- Mechanism of action data (e.g. from DrugBank) to support mechanistic analysis
- The TGA Product Information, to obtain approved indications, warnings and contraindications (a blocking gap for safety screening)
- For agoraphobia: controlled studies reporting agoraphobia-specific outcomes
- For dysthymic disorder: reboxetine-specific randomised evidence in dysthymia
- Registered clinical trials (none found for any candidate) in Australia (ANZCTR) or elsewhere
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

