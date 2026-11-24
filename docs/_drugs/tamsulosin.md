---
layout: default
title: Tamsulosin
parent: Model Prediction Only (L5)
nav_order: 700
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Tamsulosin: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Benign prostatic hyperplasia"
monitor_inn: "Tamsulosin"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "migraine with brainstem aura"]
---

# Tamsulosin
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

## Tamsulosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita
{: .text-alpha }

## One-Sentence Summary

Tamsulosin is an alpha-1 adrenergic receptor antagonist originally used to treat benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, but there are currently **0 clinical trials** and **0 supporting publications** for this indication. The prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (6 of 6 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 6 (valid: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Tamsulosin is an alpha-1A/1D adrenergic receptor antagonist. It relaxes smooth muscle in the prostate and bladder neck, which eases urinary symptoms in BPH. This description draws on general pharmacological knowledge. According to the Mechanism of Action section of the US FDA-approved prescribing information for tamsulosin: "The symptoms associated with benign prostatic hyperplasia (BPH) are related to bladder outlet obstruction, which is comprised of two underlying components: static and dynamic. The static component is related to an increase in prostate size caused, in part, by a proliferation of smooth muscle cells in the prostatic stroma. […] Tamsulosin, an alpha 1 adrenoceptor blocking agent, exhibits selectivity for alpha 1 receptors in the human prostate." ([DailyMed: tamsulosin hydrochloride prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f6b6aeab-bedd-4254-8811-4f65cf8a351f), label version 2026-11-12; accessed 2026-11-19.)

Ambras syndrome is a rare genetic disorder of hair development, linked to chromosomal rearrangements that affect regulation of the *TRPS1* gene. The review found no plausible link between alpha-1 blockade and this underlying genetic pathology. BPH (a urological condition) and congenital hypertrichosis (a hair development disorder) share no clear biological pathway.

The very high score (1.0000) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related hair-related diseases, not biological evidence or a pharmacological rationale. Other top-ranked predictions are also hair-related or developmental conditions (hypertrichosis, hair shaft abnormalities, hypotrichosis, alopecia) and are likewise unsupported by evidence. This clustering suggests a systematic pattern in the model rather than a real signal for tamsulosin.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked indication.

For the lower-ranked prediction of alopecia (rank 9), two publications were retrieved, but neither supports tamsulosin use:
- [33175100](https://pubmed.ncbi.nlm.nih.gov/33175100/) (2021, JAMA Dermatology) concerns suicidality and psychological adverse events with **finasteride**, a different drug.
- [32826647](https://pubmed.ncbi.nlm.nih.gov/32826647/) (2021, Cornea) concerns meibomian gland changes in men with BPH and is unrelated to hair loss.

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 4070F | Flomaxtra | Tamsulosin | Tablet 400 micrograms (prolonged release) | Valid |
| 5490Y | Doubluts | Dutasteride + tamsulosin | Capsule containing dutasteride 500 micrograms with tamsulosin hydrochloride 400 micrograms | Valid |
| 10102Q | Dutasteride/Tamsulosin Lupin 500/400 | Dutasteride + tamsulosin | Capsule containing dutasteride 500 micrograms with tamsulosin hydrochloride 400 micrograms | Valid |
| 13929D | Doubluts | Dutasteride + tamsulosin | Capsule containing dutasteride 500 micrograms with tamsulosin hydrochloride 400 micrograms | Valid |
| 14184M | Dutasteride/Tamsulosin Lupin 500/400 | Dutasteride + tamsulosin | Capsule containing dutasteride 500 micrograms with tamsulosin hydrochloride 400 micrograms | Valid |
| 14200J | Flomaxtra | Tamsulosin | Tablet 400 micrograms (prolonged release) | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

The only registered route of administration is oral.

## Safety Considerations

Product Information (PI) warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for full safety information.

**Contraindications and cautions from the knowledge graph** (not label text): multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, liver disease, gallbladder disease, priapism, and intraoperative floppy iris syndrome.

**Drug interactions:** 100 interactions were identified. The main ones from the entries reviewed are:
- **Major:** clarithromycin
- **Moderate:** bupropion, aprepitant, morphine (including liposomal), lorcaserin, cimetidine, clotrimazole, miconazole, dronabinol, nabilone, opium, eliglustat, fenfluramine, dexfenfluramine, glycerol phenylbutyrate, and the SGLT2 inhibitors canagliflozin, dapagliflozin, empagliflozin and ertugliflozin

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is computational only (Evidence Level L5). No clinical trials or relevant publications exist, and no plausible mechanism links alpha-1 blockade to Ambras syndrome. The same applies to the other nine top-ranked predictions, none of which has supporting evidence.

**To proceed, the following is needed:**
- Mechanism of action data to allow a proper mechanistic analysis
- A credible biological rationale linking alpha-1 adrenergic antagonism to the predicted condition (for example, preclinical or in vitro evidence)
- TGA Product Information (PI) warnings, contraindications and approved indication text, as the current safety data is incomplete
- Registered trials or published case reports for any predicted indication before reconsidering

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-20 | "Detailed mechanism of action data was not available in the data compiled for this report, so this description draws on general pharmacological knowledge" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt (revised 2026-11-20; earlier version kept in the record) | [DailyMed: tamsulosin hydrochloride prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f6b6aeab-bedd-4254-8811-4f65cf8a351f) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

