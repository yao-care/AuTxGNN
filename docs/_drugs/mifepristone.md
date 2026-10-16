---
layout: default
title: Mifepristone
parent: Model Prediction Only (L5)
nav_order: 478
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Mifepristone: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Pregnancy disorder with abortive outcome"
monitor_inn: "Mifepristone"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "rosacea", "otitis externa", "post-bacterial disorder", "postinfectious vasculitis", "infective urethral stricture", "post-infectious syndrome", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "parasitic eyelid infestation"]
---

# Mifepristone
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

# Mifepristone: From Pregnancy Disorder with Abortive Outcome to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Mifepristone was originally used for pregnancy disorders with an abortive outcome (medical termination of pregnancy).
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction is based on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pregnancy disorder with abortive outcome (from the knowledge graph; the ARTG entry has no indication text) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 97.60% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Mifepristone is generally known as a progesterone receptor and glucocorticoid receptor antagonist. Its efficacy in terminating pregnancy is established, but any mechanistic link to ocular surface disease is speculative.

The original indication (pregnancy disorder with abortive outcome) and the predicted indication (an inflammatory condition of the cornea and conjunctiva) are clinically unrelated. A theoretical link is modulation of glucocorticoid or hormone signalling in ocular surface inflammation. The high score (97.60%) most likely reflects proximity within the knowledge graph rather than demonstrated biology.

Other predicted indications were also reviewed. All are likewise supported by model scores only, with no trials or literature. They are rosacea (97.17%), otitis externa (96.65%), post-bacterial disorder (96.65%), postinfectious vasculitis (96.61%), infective urethral stricture (96.56%), post-infectious syndrome (96.54%), Chagas cardiomyopathy (96.45%), infection-related haemolytic uraemic syndrome (96.42%) and parasitic eyelid infestation (92.82%). For postinfectious vasculitis, the direction of effect is uncertain because mifepristone may raise cortisol levels while blocking its receptor.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10211K | MS-2 Step | Pack containing 1 tablet mifepristone 200 mg and 4 tablets misoprostol 200 micrograms (oral) | Not stated in the data compiled |

This is a combination pack of mifepristone and misoprostol. No topical or ophthalmic formulation is registered, so route compatibility with the predicted ocular indication has not been established.

## Safety Considerations

**Contraindications flagged in the knowledge graph** (drug-disease links, not product label text):
- Adrenocortical insufficiency, Addison disease, adrenal insufficiency
- Blood coagulation disease
- Porphyrias (hepatic, variegate, cutanea tarda, erythropoietic protoporphyria, acute intermittent, inherited and related disorders of porphyrin metabolism)
- Infectious disease
- Ectopic pregnancy

**Drug Interactions** (100 interactions identified; examples from the first 20 returned):
- **Major:** hydrocortisone, triamcinolone, dexamethasone, beclomethasone dipropionate, betamethasone, budesonide, clarithromycin, dolasetron
- **Moderate:** famotidine, pioglitazone, loperamide, bupropion, aprepitant, bisacodyl, chlorpropamide, cimetidine, saxagliptin, picosulfuric acid, polyethylene glycol 3350 with electrolytes, budesonide (nasal)

The major interactions with corticosteroids are consistent with mifepristone's glucocorticoid receptor antagonism, which may reduce corticosteroid effect. This matters for any inflammatory indication where corticosteroids are standard care.

Product label warnings and contraindications were not available. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no registered trials or publications. The mechanism of action is missing, the original and predicted indications are unrelated, and no suitable ocular formulation is registered in Australia. Knowledge graph contraindications (including infectious disease) and major corticosteroid interactions add further concern.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) to assess biological plausibility
- Systematic literature and trial registry search (including ANZCTR) for mifepristone in ocular surface disease
- Product Information warnings and contraindications from the TGA-approved PI
- Preclinical evidence in ocular surface inflammation models
- Assessment of a suitable route and formulation (for example topical ophthalmic), as the only registered product is an oral pack
- Review of whether other predicted indications, such as rosacea, have stronger support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

