---
layout: default
title: Formoterol
parent: Model Prediction Only (L5)
nav_order: 317
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
monitor_inn: "Formoterol"
predicted_indications: ["respiratory malformation", "bronchitis", "Rienhoff syndrome"]
description: "Formoterol: predicted new indication Respiratory malformation (evidence level L5). Approved use: Not recorded in the local data"
---

# Formoterol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Formoterol: Respiratory malformation
{: .text-alpha }

## One-Sentence Summary

Formoterol is a long-acting beta2-agonist bronchodilator, originally used for pulmonary emphysema and asthma.
The TxGNN model's top-ranked prediction is **respiratory malformation**, but this has **no clinical trials** and only loosely related literature supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Respiratory malformation |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 (model prediction only) |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, formoterol is a long-acting beta2-adrenoceptor agonist that relaxes airway smooth muscle and produces bronchodilation lasting about 12 hours. Its efficacy in asthma and COPD-type disease is well established.

For **respiratory malformation**, there is no credible mechanistic link. A bronchodilator cannot be expected to correct structural congenital malformations. The retrieved literature concerns asthma and COPD, not malformations, and the high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other predictions in the list are more informative for context:
- **Bronchitis** (rank 2) is supported indirectly through COPD trials.
- Remaining predictions (Rienhoff syndrome, atopic eczema, interstitial emphysema, hyperlucent lung, compensatory emphysema, asthma-related traits) have no plausible mechanism and no supporting trials.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for respiratory malformation.

For context, the best-supported predictions by trial evidence are shown below.

**Obstructive lung disease (COPD) – selected Phase 3 trials**

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04320342](https://clinicaltrials.gov/study/NCT04320342) | Phase 3 | Completed | 3406 | 52-week study of beclomethasone/formoterol/glycopyrronium triple therapy vs beclomethasone/formoterol in COPD |
| [NCT03162055](https://clinicaltrials.gov/study/NCT03162055) | Phase 3 | Completed | 1119 | Glycopyrronium/formoterol vs umeclidinium/vilanterol over 24 weeks in COPD (AERISTO) |
| [NCT03028701](https://clinicaltrials.gov/study/NCT03028701) | Phase 4 | Completed | 33 | Bronchodilator effect of formoterol/budesonide 12/400 mcg in COPD |

**Asthma – selected Phase 3 trials**

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00381485](https://clinicaltrials.gov/study/NCT00381485) | Phase 3 | Completed | 834 | Mometasone/formoterol vs mometasone alone over 12 weeks in persistent asthma |
| [NCT00651651](https://clinicaltrials.gov/study/NCT00651651) | Phase 3 | Completed | 450 | Budesonide/formoterol vs its components in children and adults with asthma |
| [NCT01167010](https://clinicaltrials.gov/study/NCT01167010) | Phase 3 | Completed | 552 | Non-inferiority of a formoterol/budesonide inhalation capsule in asthma |
| [NCT04233190](https://clinicaltrials.gov/study/NCT04233190) | Phase 3 | Completed | 472 | Non-inferiority of a formoterol/budesonide product in moderate to severe persistent asthma |

**Bronchitis (indirect, COPD-based)**

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00064415](https://clinicaltrials.gov/study/NCT00064415) | Phase 3 | Completed | 799 | 12-month safety study of arformoterol (a formoterol enantiomer) in COPD |
| [NCT00250679](https://clinicaltrials.gov/study/NCT00250679) | Phase 3 | Completed | 443 | 6-month safety study of arformoterol in COPD |

No ANZCTR identifiers were available in the data compiled for this report.

---

## Literature Evidence

For respiratory malformation, the retrieved publications concern COPD and asthma rather than malformations, so they do not support this prediction. Context from the better-supported predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32579807](https://pubmed.ncbi.nlm.nih.gov/32579807/) | 2020 | RCT | N Engl J Med | Triple inhaled therapy at two glucocorticoid doses in moderate-to-very-severe COPD |
| [33252985](https://pubmed.ncbi.nlm.nih.gov/33252985/) | 2021 | RCT (post hoc) | Am J Respir Crit Care Med | Reduced all-cause mortality with budesonide/glycopyrrolate/formoterol in COPD (ETHOS) |
| [30232048](https://pubmed.ncbi.nlm.nih.gov/30232048/) | 2018 | RCT | Lancet Respir Med | Triple therapy vs dual therapies in COPD (KRONOS) |
| [29768149](https://pubmed.ncbi.nlm.nih.gov/29768149/) | 2018 | RCT | N Engl J Med | As-needed budesonide-formoterol in mild asthma |
| [29768147](https://pubmed.ncbi.nlm.nih.gov/29768147/) | 2018 | RCT | N Engl J Med | As-needed budesonide-formoterol vs maintenance budesonide in mild asthma |
| [31112386](https://pubmed.ncbi.nlm.nih.gov/31112386/) | 2019 | RCT | N Engl J Med | Pragmatic trial of as-needed budesonide-formoterol in mild asthma |
| [41033330](https://pubmed.ncbi.nlm.nih.gov/41033330/) | 2025 | RCT | Lancet | Budesonide-formoterol vs salbutamol as reliever in children with mild asthma (CARE) |
| [31015757](https://pubmed.ncbi.nlm.nih.gov/31015757/) | 2019 | Meta-analysis | Int J Chron Obstruct Pulmon Dis | Risks of budesonide/formoterol in stable COPD |
| [35034195](https://pubmed.ncbi.nlm.nih.gov/35034195/) | 2022 | Cohort | Eur J Appl Physiol | Compensatory responses to mechanical abnormalities in COPD during sleep (top-ranked prediction; indirect) |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14419X | Foradile | Capsule containing powder for oral inhalation, formoterol fumarate dihydrate 12 micrograms (for use in Foradile Aerolizer) | Not stated in the data compiled for this report |

---

## Safety Considerations

No label warnings or contraindication text were available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for full safety information.

**Contraindication-related signals from the knowledge graph (not label text):** hypertension, long QT syndrome, epilepsy, liver disease, gallbladder disease, and several pituitary and hypogonadotropic disorders are flagged. These should be verified against the PI.

**Drug interactions (100 recorded; examples):**
- **Moderate:** acarbose, famotidine, clarithromycin, cisapride, dolasetron (QT-related concern), ephedrine, isometheptene, diethylpropion, and several antidiabetic agents (albiglutide, alogliptin, canagliflozin, dapagliflozin, dulaglutide, empagliflozin, chlorpropamide).
- **Minor:** corticosteroids (beclomethasone, betamethasone, budesonide, dexamethasone).

**Guardrail from the asthma evidence:** long-acting beta2-agonist monotherapy in asthma carries a safety warning, so formoterol should be combined with an inhaled corticosteroid.

---

## Conclusion and Next Steps

**Decision: Hold** (for respiratory malformation)

**Rationale:**
The top-ranked prediction has no clinical trials, no relevant literature, and no plausible mechanism for a bronchodilator. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

**To proceed, the following is needed:**
- Mechanism of action data (DrugBank) and a defensible biological rationale, if any further work on respiratory malformation is planned
- TGA Product Information warnings and contraindications (currently a blocking gap for safety screening)
- Approved indication text for the Foradile ARTG entry
- If a novel use is sought, a review of lower-ranked predictions or of bronchitis (chronic bronchitis specifically), where evidence is indirect but plausible
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

