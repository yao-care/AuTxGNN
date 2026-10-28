---
layout: default
title: Camphor
parent: Model Prediction Only (L5)
nav_order: 126
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Camphor: predicted new indication Migraine disorder (evidence level L4). Approved use: Not recorded"
monitor_inn: "camphor"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "erectile dysfunction (disease)", "pulmonary hypertension", "kyphoscoliotic heart disease", "ulerythema ophryogenesis", "Raynaud disease", "atrophoderma vermiculata", "Tourette syndrome"]
---

# Camphor
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Camphor: From an Unspecified Topical Counter-Irritant to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Camphor is a topical counter-irritant, marketed in Australia as an ingredient of Goanna Heat Cream. No approved indication text is recorded in the data compiled for this report.
The TxGNN model predicts it may be relevant to **migraine disorder**, but there are **no registered clinical trials** and only **3 low-tier publications** (two case reports or series and one unrelated historical review), plus one preclinical animal study found under a related migraine entry.
This is a research question, not a treatment recommendation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded (no approved indication text in the ARTG data) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, camphor is understood to act as a TRPM8 agonist and a TRPV1/TRPA1 modulator. Topical or inhaled counter-irritant effects could plausibly influence trigeminovascular pain signalling, which is relevant to migraine.

The original indication for the Australian product is not documented, so the relationship between the original and new indications cannot be assessed directly. Camphor is used as a topical rubefacient and counter-irritant for muscle and joint discomfort, and this is a different clinical setting from migraine.

The supporting literature is weak:
- Two case reports or series describe **cluster headache** temporally linked to toothpastes containing camphor and eucalyptus oils. These describe a possible *trigger*, not a benefit, and cluster headache is a different condition from migraine.
- A 2026 animal-model study (reserpine-induced migraine) reports that natural (+)-camphor reduced migraine-like changes via the p38β MAPK/ATF2 pathway. It is the most direct signal available, but it is preclinical, and its details need independent verification.
- Camphor is a constituent of feverfew (*Tanacetum parthenium*), a traditional migraine herbal. This is an indirect link only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42849823](https://pubmed.ncbi.nlm.nih.gov/42849823/) | 2026 | Preclinical (animal model) | J Ethnopharmacol | Natural (+)-camphor alleviated reserpine-induced migraine with local cerebral vasospasm in an animal model, via the p38β MAPK/ATF2 pathway |
| [35856604](https://pubmed.ncbi.nlm.nih.gov/35856604/) | 2022 | Case series | Headache | Five cluster headache cases linked to toothpastes containing pro-convulsant essential oils |
| [34373243](https://pubmed.ncbi.nlm.nih.gov/34373243/) | 2021 | Case report | BMJ Case Rep | Two cluster headache cases temporally related to toothpastes containing camphor and eucalyptus oils |
| [27324458](https://pubmed.ncbi.nlm.nih.gov/27324458/) | 2016 | Analytical chemistry | Biomed Chromatogr | Method for measuring camphor content in feverfew essential oil; not a clinical study |
| [27058833](https://pubmed.ncbi.nlm.nih.gov/27058833/) | 2016 | Review | Z Kinder Jugendpsychiatr Psychother | Historical review of paediatric neuropsychopharmacology; not relevant to camphor |

Other retrieved papers for this prediction were not relevant, including feverfew anticancer assays and a zolmitriptan formulation study.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11707E | Goanna Heat Cream | Cream 20%-5%-3.5%-3%-1%-1%-0.5%-0.5%-0.15%, 100 g | Not recorded |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

Points from the compiled evidence that deserve attention:
- Camphor has known neurotoxicity, including seizure risk, at higher exposures. This argues for caution in any neurological indication.
- Case reports describe cluster headache temporally linked to camphor-containing essential oils, so camphor may act as a headache trigger in some people.
- An animal toxicity study of edible camphor reported oxidative stress and histopathological changes (relevant to oral use, not topical).

## Other Predictions Reviewed

The remaining top-ranked predictions have no meaningful support and are all on Hold:

| Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|
| Migraine with brainstem aura | 0.9979 | L5 | Prediction only |
| Erectile dysfunction | 0.9979 | L5 | Only a rat toxicity study; a possible safety signal, not efficacy |
| Pulmonary hypertension | 0.9977 | L5 | Literature hits are a name collision with the CAMPHOR questionnaire, unrelated to the drug |
| Kyphoscoliotic heart disease | 0.9970 | L5 | No literature or trials |
| Ulerythema ophryogenesis | 0.9960 | L5 | No literature or trials |
| Raynaud disease | 0.9956 | L5 | Only an unrelated outcome-measure paper |
| Atrophoderma vermiculata | 0.9954 | L5 | No literature or trials |
| Tourette syndrome | 0.9946 | L5 | No literature or trials; neurotoxicity concerns |

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for migraine is limited to one animal study, anecdotal case reports (which describe camphor as a possible trigger of a different headache disorder) and a model prediction. There are no human trials, and neurotoxicity is a recognised concern. The prediction is best treated as a research question.

**To proceed, the following is needed:**
- Product Information warnings and contraindications for the Australian product (currently missing)
- Approved indication text for the ARTG entry
- Mechanism of action data (for example from DrugBank)
- Verification of the 2026 animal study, including mechanism and effect size
- Human safety and pharmacokinetic data for topical or inhaled camphor in headache populations
- A pilot clinical study design, if the preclinical findings are confirmed, with seizure and neurotoxicity monitoring
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

