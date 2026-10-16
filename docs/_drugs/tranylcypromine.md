---
layout: default
title: Tranylcypromine
parent: Model Prediction Only (L5)
nav_order: 747
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Tranylcypromine: predicted new indication Benign paroxysmal torticollis of infancy (evidence level L5). Approved use: Unipolar depression, endogenous depression, major depressive disorder…"
monitor_inn: "Tranylcypromine"
predicted_indications: ["benign paroxysmal torticollis of infancy", "Ohdo syndrome and variants", "dysthymic disorder", "agoraphobia", "melancholia", "neurotic depression", "blepharophimosis - intellectual disability syndrome, Ohdo type", "neurotic disorder", "ligneous conjunctivitis", "Keppen-Lubinsky syndrome"]
---

# Tranylcypromine
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

# Tranylcypromine: From Depression to Benign Paroxysmal Torticollis of Infancy

## One-Sentence Summary

Tranylcypromine is an irreversible monoamine oxidase inhibitor (MAOI), originally used to treat depression and anxiety disorders.
The TxGNN model ranks **benign paroxysmal torticollis of infancy** as its top prediction, but **no clinical trials and no publications** support this specific link. The prediction is a graph-based output only.
Of the other nine predictions, the best-supported are **dysthymic disorder**, **agoraphobia**, **melancholia** and **neurotic depression**. These sit close to the existing depression and anxiety indications, so they are not truly new uses.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Unipolar depression, endogenous depression, major depressive disorder, anxiety disorder (from the knowledge graph; no approved indication text is available for the Australian listing) |
| Predicted New Indication | Benign paroxysmal torticollis of infancy |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, tranylcypromine is an irreversible, non-selective MAO inhibitor. It raises monoamine levels in the brain, which underlies its antidepressant and anti-anxiety effects. It also inhibits LSD1 (KDM1A), an epigenetic enzyme.

For the top-ranked prediction, **benign paroxysmal torticollis of infancy**, a plausible link is hard to find. It is a childhood, migraine-spectrum disorder associated with CACNA1A (a calcium channel gene). No established connection to MAO inhibition exists. MAOIs are also poorly suited to infants because of dietary (tyramine) and drug-interaction hazards. The high score (0.997) should be read as a statistical graph output rather than clinical reasoning.

Other predictions fall into two groups:

- **Close to the existing label:** dysthymic disorder, agoraphobia, melancholia, neurotic depression and neurotic disorder. These are mechanistically coherent because MAOIs have a long history in chronic, atypical and phobic-anxiety presentations. They largely overlap with current depression and anxiety indications.
- **Unsupported rare diseases:** Ohdo syndrome and its variants (KAT6B-related), ligneous conjunctivitis (plasminogen deficiency) and Keppen-Lubinsky syndrome (KCNJ6-related). For Ohdo syndrome, an LSD1-based epigenetic link is conceivable but speculative, and these congenital conditions are unlikely to respond to drug therapy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction, or for any of the other nine predicted indications.

---

## Literature Evidence

No literature was found for benign paroxysmal torticollis of infancy. The table below shows the most relevant publications retrieved for the nearest-to-label predictions, prioritising tranylcypromine-specific and higher-tier evidence. Most are reviews or reports and do not directly support the top-ranked prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28579071](https://pubmed.ncbi.nlm.nih.gov/28579071/) | 2017 | Review and meta-analysis of controlled studies | Eur Neuropsychopharmacol | Tranylcypromine-specific review of clinical pharmacology and controlled studies in depression (neurotic depression) |
| [21527126](https://pubmed.ncbi.nlm.nih.gov/21527126/) | 2011 | Meta-analysis of RCTs | J Clin Psychiatry | Antidepressants as a class are effective for dysthymia versus placebo; not tranylcypromine-specific |
| [8127928](https://pubmed.ncbi.nlm.nih.gov/8127928/) | 1993 | Double-blind trial | Pharmacopsychiatry | Moclobemide compared with tranylcypromine in depressed patients (neurotic depression) |
| [35837681](https://pubmed.ncbi.nlm.nih.gov/35837681/) | 2023 | Review / prescriber guide | CNS Spectrums | Guide to classic MAOIs, including tranylcypromine, for treatment-resistant depression (melancholia) |
| [26917855](https://pubmed.ncbi.nlm.nih.gov/26917855/) | 2016 | Review | Australas Psychiatry | Reviews whether the evidence warrants renewed use of MAOIs (melancholia) |
| [7612154](https://pubmed.ncbi.nlm.nih.gov/7612154/) | 1995 | Review / meta-analysis | Neuropsychopharmacology | Phenelzine, isocarboxazid and tranylcypromine show generally comparable efficacy in outpatients (melancholia) |
| [3050061](https://pubmed.ncbi.nlm.nih.gov/3050061/) | 1988 | Review | J Psychiatr Res | MAOIs superior to placebo in agoraphobia and mixed anxiety-depressive states; no convincing evidence in pure anxiety states |
| [20703987](https://pubmed.ncbi.nlm.nih.gov/20703987/) | 2010 | Case report | Psychiatr Prax | Tranylcypromine as part of combined therapy in one patient with therapy-resistant agoraphobia, panic disorder and depression |
| [454092](https://pubmed.ncbi.nlm.nih.gov/454092/) | 1979 | Review | Arch Gen Psychiatry | MAOIs are effective in neurotic or atypical depression; tranylcypromine-specific controlled data are limited (neurotic disorder) |
| [14132611](https://pubmed.ncbi.nlm.nih.gov/14132611/) | 1964 | Case report (safety) | Lancet | Death associated with tranylcypromine and cheese, documenting the hypertensive-crisis risk |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14401Y | Parnate | Tablet 10 mg (as sulfate) | Not available in the data compiled for this report |

---

## Safety Considerations

- **Contraindication signals (knowledge graph, not label text):** The knowledge graph links tranylcypromine to a wide range of conditions, including:
  - Cardiovascular: hypertension, coronary artery disease, heart conduction disease, orthostatic hypotension.
  - Neurological and psychiatric: epilepsy, bipolar disorder, substance abuse/dependence.
  - Organ disease: liver disease, kidney disease.
  - Endocrine and tumours: diabetes mellitus, hyperthyroidism, phaeochromocytoma.
- **Drug interactions:** 100 interactions were identified. Examples of Major-level interactions include isometheptene, bupropion, morphine, lorcaserin, diethylpropion, dolasetron, palonosetron and phentermine. Moderate interactions include epinephrine and several antidiabetic agents (chlorpropamide, glimepiride, repaglinide, insulin aspart).
- **Dietary and withdrawal risks:** The literature documents tyramine-related hypertensive crisis (1964 case report of death with cheese) and withdrawal or discontinuation phenomena after abrupt cessation, with a recognised risk of abuse and dependence (PMID 23359339).

Please refer to the TGA-approved Product Information (PI) for official warnings and contraindications, as these were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction, benign paroxysmal torticollis of infancy, has no clinical trials or literature (L5). It has no plausible link to MAO inhibition, and MAOIs carry dietary and interaction hazards that make them unsuitable for infants.
- The better-supported predictions (dysthymia, agoraphobia, melancholia, neurotic depression) are largely extensions of the existing depression and anxiety label. They have indirect or narrative evidence (L3–L4) and are better treated as research questions than as new repurposing candidates.

**To proceed, the following is needed:**
- TGA Product Information, including approved indication text, warnings and contraindications, to complete safety screening.
- Mechanism of action data (for example, from DrugBank) to support mechanistic-link analysis.
- For the near-label indications, tranylcypromine-specific controlled trials in dysthymia and agoraphobia/panic disorder.
- For the rare-disease predictions, any preclinical or mechanistic data (for example, LSD1 inhibition in KAT6B-related disease) before further consideration.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

