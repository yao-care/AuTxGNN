---
layout: default
title: Dosulepin
parent: Model Prediction Only (L5)
nav_order: 229
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Dosulepin: predicted new indication Benign paroxysmal torticollis of infancy (evidence level L5). Approved use: Not stated in the Australian registration data"
monitor_inn: "Dosulepin"
predicted_indications: ["benign paroxysmal torticollis of infancy", "agoraphobia", "Ohdo syndrome and variants", "Keppen-Lubinsky syndrome", "blepharophimosis - intellectual disability syndrome, Ohdo type", "ligneous conjunctivitis"]
---

# Dosulepin
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

# Dosulepin: From Depression to Dysthymic Disorder

## One-Sentence Summary

Dosulepin is a tricyclic antidepressant originally used to treat unipolar depression, endogenous depression, major depressive disorder and anxiety disorder.
The TxGNN model's top-ranked prediction is **benign paroxysmal torticollis of infancy**, but this has no clinical or literature support and no plausible pharmacological rationale. The most credible predictions are depression-spectrum conditions that largely overlap the existing label, such as **dysthymic disorder** and **melancholia**.
For the top-ranked prediction there are **0 clinical trials** and **0 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Australian registration data; the knowledge graph lists unipolar depression, endogenous depression, major depressive disorder and anxiety disorder |
| Predicted New Indication | Benign paroxysmal torticollis of infancy (rank 1) |
| TxGNN Prediction Score | 98.97% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

**Other top predictions (for context):**

| Rank | Predicted Indication | Score | Evidence Level | Recommendation |
|---|---|---|---|---|
| 2 | Dysthymic disorder | 98.86% | L5 | Hold |
| 3 | Agoraphobia | 98.83% | L5 | Hold |
| 4 | Melancholia | 98.23% | L3 | Research question |
| 5 | Neurotic depression | 98.22% | L3 | Research question |
| 6 | Ohdo syndrome and variants | 98.10% | L5 | Hold |
| 7 | Neurotic disorder | 98.01% | L5 | Hold |
| 8 | Keppen-Lubinsky syndrome | 97.70% | L5 | Hold |
| 9 | Blepharophimosis - intellectual disability syndrome, Ohdo type | 97.37% | L5 | Hold |
| 10 | Ligneous conjunctivitis | 96.88% | L5 | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, dosulepin is a tricyclic antidepressant that acts on the serotonin transporter (SERT) and the noradrenaline transporter (NET), and also binds muscarinic M1–M5 receptors and the histamine H1 receptor. Reuptake inhibition explains its antidepressant effect, while the receptor binding explains much of its anticholinergic and sedative adverse-effect profile.

**Rank 1 (benign paroxysmal torticollis of infancy):** This prediction is weakly supported. The condition is a self-limiting paediatric disorder, probably linked to calcium-channel genetics (CACNA1A). There is no established rationale for a tricyclic antidepressant, and dosulepin's anticholinergic effects, QT prolongation and overdose toxicity are unfavourable in infants. The high score most likely reflects proximity in the knowledge graph rather than a pharmacological basis.

**Depression-spectrum predictions (dysthymic disorder, melancholia, neurotic depression, neurotic disorder, agoraphobia):** These are biologically plausible because they fall within, or sit very close to, the existing approved indications. They are better described as label extensions than true repurposing. Tricyclics have a history of use in panic disorder with agoraphobia.

**Rare genetic syndromes (Ohdo syndrome and variants, Keppen-Lubinsky syndrome, Ohdo-type blepharophimosis) and ligneous conjunctivitis:** No mechanistic link is apparent. The scores likely reflect network proximity to related conditions. For ligneous conjunctivitis, dosulepin's anticholinergic effect (reduced tear production) could worsen ocular surface disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction (benign paroxysmal torticollis of infancy), nor for any of the other nine predictions.

---

## Literature Evidence

Currently no related literature available for the top-ranked prediction (benign paroxysmal torticollis of infancy).

The only indications with retrieved literature are melancholia and neurotic depression, which share largely the same depression-focused set. The most relevant items are below. None is specific to melancholia or neurotic depression, so the evidence is indirect.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34389045](https://pubmed.ncbi.nlm.nih.gov/34389045/) | 2021 | Systematic review protocol | Syst Rev | Protocol for a meta-analysis of tricyclic antidepressants versus active placebo, placebo or no intervention in adults with major depressive disorder; notes the effect is small and of questionable clinical importance |
| [24353997](https://pubmed.ncbi.nlm.nih.gov/24353997/) | 2013 | Cochrane review | Cochrane Database Syst Rev | Fluoxetine compared with other antidepressants for depression; earlier trials gave conflicting findings |
| [11719915](https://pubmed.ncbi.nlm.nih.gov/11719915/) | 2001 | Meta-analysis | Br Med Bull | Review of 108 antidepressant meta-analyses; little efficacy difference between most new and old antidepressants |
| [38379028](https://pubmed.ncbi.nlm.nih.gov/38379028/) | 2024 | Cohort study | Acta Psychiatr Scand | Long-term, nationwide comparison of response to 17 antidepressants in major depressive disorder |
| [41522586](https://pubmed.ncbi.nlm.nih.gov/41522586/) | 2025 | Observational study | J Pharm Bioallied Sci | Prospective comparison of SSRIs and TCAs in major depressive disorder |
| [19347769](https://pubmed.ncbi.nlm.nih.gov/19347769/) | 2009 | Naturalistic comparative study | Nord J Psychiatry | Venlafaxine versus dosulepin in depressive episodes in a naturalistic setting |
| [386873](https://pubmed.ncbi.nlm.nih.gov/386873/) | 1978 | Comparative clinical trial | Ann Med Psychol | Clinical trial comparing dosulepin and amitriptyline |
| [15311996](https://pubmed.ncbi.nlm.nih.gov/15311996/) | 2004 | Safety (ECG) study | Physiol Res | QT dispersion changes in 28 outpatients on dosulepin versus 37 healthy volunteers; signals cardiotoxicity |
| [15354946](https://pubmed.ncbi.nlm.nih.gov/15354946/) | 2004 | Safety (ECG) study | Prague Med Rep | QT dispersion in 27 outpatients on dosulepin using body surface potential mapping |
| [2651248](https://pubmed.ncbi.nlm.nih.gov/2651248/) | 1989 | Randomised, placebo-controlled trial | Fortschr Med | Traffic safety study in 48 healthy volunteers given dosulepin 75 mg or placebo for 16 days |

Study designs are inferred from truncated titles and abstracts and should be verified.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1357K | Dosulepin Viatris | Capsule containing dosulepin hydrochloride 25 mg (oral) | Not available in the data compiled for this report |

---

## Safety Considerations

- **Cardiac effects:** Two ECG studies in patients treated with dosulepin reported changes in QT dispersion, suggesting cardiotoxicity.
- **Anticholinergic and sedative effects:** Dosulepin binds muscarinic M1–M5 and histamine H1 receptors, which accounts for anticholinergic and sedative effects. This is a particular concern in infants and for ocular surface disease.
- **Overdose and seizure risk:** The compiled assessments flag overdose toxicity and lowered seizure threshold as concerns, especially in paediatric and rare neurodevelopmental populations.
- **Pharmacological targets:** SERT, NET, M1–M5 and H1 receptors (an 8-target pharmacology profile, not a list of drug–drug interactions with specific agents).

Please refer to the TGA-approved Product Information (PI) for full warnings, contraindications and drug interaction information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction, benign paroxysmal torticollis of infancy, has no trials, no literature and no plausible mechanism, and dosulepin's safety profile is unfavourable in infants.
- The more plausible predictions (dysthymic disorder, melancholia, neurotic depression, agoraphobia) largely overlap the existing label, so they are label extensions rather than true repurposing. Melancholia and neurotic depression reach only L3 with indirect evidence, and are best framed as research questions.

**To proceed, the following is needed:**
- Product Information (PI) warnings and contraindications for the Australian product, and its approved indication text
- Mechanism of action data
- For depression-spectrum indications: dosulepin-specific or tricyclic-class evidence for dysthymia, melancholia and agoraphobia, weighed against the cardiac safety signal
- For the rare genetic and paediatric predictions: a pharmacological rationale before any further evaluation, which currently appears unlikely
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

