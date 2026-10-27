---
layout: default
title: Indacaterol
parent: Model Prediction Only (L5)
nav_order: 373
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Indacaterol: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis . Evidence is asse… (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Indacaterol"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "headache disorder", "trigeminal autonomic cephalalgia", "paratenonitis", "calcific tendinitis", "hypertrichosis (disease)", "bronchial disease", "myositis", "anaphylaxis", "Ambras type hypertrichosis universalis congenita"]
---

# Indacaterol
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

## Indacaterol: From Obstructive Airway Disease to Bronchial Disease
{: .text-alpha }

## One-Sentence Summary

Indacaterol is an ultra-long-acting beta-2 agonist (LABA) inhaled once daily and marketed in Australia as Onbrez Breezhaler.
The TxGNN model's top-ranked prediction is nephrogenic syndrome of inappropriate antidiuresis, but it has no supporting evidence. The best-supported prediction is **bronchial disease** (rank 7), with **22 clinical trials** and **19 publications**, mostly in asthma.
That bronchial disease evidence is largely label-adjacent rather than true repurposing, and it comes mainly from combination products.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the ARTG entry carries no indication text) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis (rank 1, TxGNN's top prediction). Evidence is assessed below for bronchial disease (rank 7), the only prediction with supporting data. |
| TxGNN Prediction Score | 99.54% for the rank 1 prediction; 99.18% for bronchial disease |
| Evidence Level | L5 for the rank 1 prediction (prediction only); L1 for bronchial disease |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold for the rank 1 prediction; Proceed with Guardrails for bronchial disease (asthma) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Indacaterol is known to be an ultra-long-acting beta-2 adrenergic agonist. It relaxes bronchial smooth muscle through cAMP signalling, which allows once-daily dosing.

**Rank 1 prediction (nephrogenic syndrome of inappropriate antidiuresis):** The high score is a graph-based prediction only. A link to the V2 receptor gain-of-function signalling that drives this condition is not supported. Beta-2 agonism would be expected to raise cAMP rather than counter it. The same applies to the other top-ranked predictions (headache disorder, trigeminal autonomic cephalalgia, paratenonitis, calcific tendinitis, hypertrichosis, myositis, anaphylaxis and Ambras-type hypertrichosis). None has any trial or literature support, and beta agonists may actually cause headache as an adverse effect. Anaphylaxis is managed first-line with epinephrine, and indacaterol's slow onset makes it unsuitable for an acute emergency.

**Bronchial disease:** This is the only prediction with real support. Indacaterol is already used in obstructive airway disease. As part of fixed-dose combinations it has Phase 3 evidence in asthma: indacaterol/mometasone (QMF149) and indacaterol/glycopyrronium/mometasone (QVM149). This is better described as an on-label or label-adjacent use than as true repurposing. The evidence applies to combination products, not indacaterol alone. LABA monotherapy is contraindicated in asthma.

---

## Clinical Trial Evidence

The table covers the bronchial disease prediction (the other nine predictions have no registered trials). Ten of the 22 trials are shown, prioritising Phase 3 studies and larger studies.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02554786](https://clinicaltrials.gov/study/NCT02554786) | Phase 3 | Completed | 2216 | 52-week study of indacaterol/mometasone (QMF149) vs mometasone alone in poorly controlled asthma |
| [NCT00529529](https://clinicaltrials.gov/study/NCT00529529) | Phase 3 | Completed | 805 | 26-week safety study of indacaterol 300 and 600 µg vs salmeterol in moderate to severe persistent asthma |
| [NCT01079130](https://clinicaltrials.gov/study/NCT01079130) | Phase 3 | Completed | 511 | 14-day bronchodilator efficacy of indacaterol vs placebo and salmeterol in persistent asthma |
| [NCT04259164](https://clinicaltrials.gov/study/NCT04259164) | Phase 3 | Completed | 28 | Glycopyrronium added to indacaterol/mometasone, with anti-inflammatory endpoints on the allergen-induced late asthmatic response |
| [NCT00403637](https://clinicaltrials.gov/study/NCT00403637) | Phase 2/3 | Completed | 45 | Single-dose indacaterol (150, 300, 600 µg) vs formoterol and placebo in persistent asthma |
| [NCT00545272](https://clinicaltrials.gov/study/NCT00545272) | Phase 2 | Completed | 392 | 14-day dose-ranging of four indacaterol doses vs placebo and formoterol in persistent asthma |
| [NCT01609478](https://clinicaltrials.gov/study/NCT01609478) | Phase 2 | Completed | 335 | 12-week efficacy, safety and PK of indacaterol acetate (75 and 150 µg) in persistent asthma |
| [NCT01156844](https://clinicaltrials.gov/study/NCT01156844) | Phase 2 | Completed | 191 | Bronchodilator efficacy of three indacaterol maleate regimens in persistent asthma |
| [NCT02892019](https://clinicaltrials.gov/study/NCT02892019) | Phase 2 | Completed | 79 | Two-week study of indacaterol acetate (75 and 150 µg) in children aged 6 to under 12 years with asthma |
| [NCT04206761](https://clinicaltrials.gov/study/NCT04206761) | Phase 3 | Withdrawn | 0 | Xenon MRI study of triple therapy (QVM149); withdrawn, so it provides no evidence |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32653074](https://pubmed.ncbi.nlm.nih.gov/32653074/) | 2020 | RCT (Phase 3) | Lancet Respir Med | IRIDIUM: once-daily single-inhaler mometasone/indacaterol/glycopyrronium vs mometasone/indacaterol or twice-daily fluticasone/salmeterol in inadequately controlled asthma |
| [33871819](https://pubmed.ncbi.nlm.nih.gov/33871819/) | 2021 | Review | Drugs | Review of indacaterol/glycopyrronium/mometasone (Enerzair Breezhaler) in asthma, approved in the EU for adults inadequately controlled on maintenance therapy |
| [31425937](https://pubmed.ncbi.nlm.nih.gov/31425937/) | 2019 | Review | Respir Med | Ultra-LABAs in asthma; they can be prescribed only together with an inhaled corticosteroid |
| [34783265](https://pubmed.ncbi.nlm.nih.gov/34783265/) | 2022 | Review | Expert Rev Respir Med | Triple fixed-dose combination (LABA/LAMA/ICS) in moderate-to-severe asthma |
| [34329722](https://pubmed.ncbi.nlm.nih.gov/34329722/) | 2021 | Dose-bridging analysis | Pulm Pharmacol Ther | Mometasone dose bridging across once-daily indacaterol-containing combinations in asthma |
| [23348973](https://pubmed.ncbi.nlm.nih.gov/23348973/) | 2013 | Review | Am J Respir Crit Care Med | Beta-2 agonist therapy in lung disease |
| [22611179](https://pubmed.ncbi.nlm.nih.gov/22611179/) | 2012 | Review | Pharmacol Rev | Pharmacology and therapeutics of bronchodilators |
| [19609496](https://pubmed.ncbi.nlm.nih.gov/19609496/) | 2009 | Review | Adv Ther | Preclinical and clinical data on indacaterol, showing rapid and sustained bronchodilation in COPD and asthma |
| [40887869](https://pubmed.ncbi.nlm.nih.gov/40887869/) | 2025 | Pharmacology study | Pharmacol Res Perspect | In vitro comparison of short, long and ultra-long-acting beta-2 agonists, including indacaterol |
| [33446622](https://pubmed.ncbi.nlm.nih.gov/33446622/) | 2020 | Review | Med Lett Drugs Ther | Overview of drugs for asthma |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14334K | Onbrez | Capsule containing powder for oral inhalation 150 micrograms (as maleate), for use in Breezhaler | Not stated in the data compiled for this report |

---

## Cytotoxicity

Not applicable. Indacaterol is not an antineoplastic drug, so this section is omitted.

---

## Safety Considerations

Warnings and contraindications from the product label were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for these.

- **Knowledge-graph contraindication signals** (not label text): hypertension, long QT syndrome (including the familial form), epilepsy, hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, potassium deficiency, sudden cardiac arrest, heart conduction disease, coronary artery disease, thyrotoxicosis, hyperthyroidism and Graves disease. These are consistent with the known class effects of beta-2 agonists.
- **Drug interactions:** 100 interactions were identified (the 20 retrieved are summarised here).
  - Moderate: antidiabetic agents (acarbose, metformin, pioglitazone, alogliptin, saxagliptin, albiglutide, canagliflozin, dapagliflozin, chlorpropamide), epinephrine, isometheptene, famotidine and clarithromycin.
  - Minor: corticosteroids (hydrocortisone, triamcinolone, dexamethasone, beclomethasone, betamethasone, budesonide) and aprepitant.
- **Asthma:** LABA monotherapy is contraindicated in asthma. Use only with an inhaled corticosteroid.

---

## Conclusion and Next Steps

**Decision: Hold for the rank 1 prediction (nephrogenic syndrome of inappropriate antidiuresis) and the other eight unsupported predictions; Proceed with Guardrails for bronchial disease (asthma)**

**Rationale:**
- The top-ranked prediction and eight others (rank 2 to 6 and 8 to 10) are graph-based predictions only (L5), with no trials or publications and no plausible mechanism. For some, the mechanism points the wrong way.
- Bronchial disease (asthma) has L1-level evidence, including several completed Phase 3 trials and the IRIDIUM RCT. It comes from combination products and is close to existing use, so it is not novel repurposing.

**To proceed, the following is needed:**
- Mechanism of action data and original indication text (neither was available in the compiled data)
- Label warnings and contraindications from the TGA PI
- Clarification of which asthma population and which combination product (indacaterol/mometasone or the triple combination) would be considered, with confirmation of their ARTG status
- No further work is recommended for the unsupported predictions unless new mechanistic or clinical evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

