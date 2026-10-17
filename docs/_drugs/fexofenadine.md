---
layout: default
title: Fexofenadine
parent: Model Prediction Only (L5)
nav_order: 296
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Fexofenadine: predicted new indication Rosacea conjunctivitis (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, atopic conjunctivitis…"
monitor_inn: "Fexofenadine"
predicted_indications: ["rosacea conjunctivitis", "punctate epithelial keratoconjunctivitis", "viral conjunctivitis", "parasitic eyelid infestation", "ulcerative blepharitis", "infective urethral stricture", "postinfectious vasculitis", "post-bacterial disorder", "noninfectious dermatoses of eyelid"]
---

# Fexofenadine
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

# Fexofenadine: From Allergic Rhinitis to Rosacea Conjunctivitis

## One-Sentence Summary

Fexofenadine is a selective peripheral H1-receptor antagonist, originally used for allergic rhinitis, allergic and other forms of conjunctivitis, and idiopathic urticaria.
The TxGNN model predicts it may be effective for **rosacea conjunctivitis**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, atopic conjunctivitis, papillary conjunctivitis, vernal conjunctivitis, idiopathic urticaria |
| Predicted New Indication | Rosacea conjunctivitis |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

*Note: The original indications above come from the TxGNN knowledge graph. The ARTG entry in the data compiled for this report has no approved indication text.*

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Fexofenadine is known to be a selective peripheral H1-receptor antagonist. It is already used for allergic and atopic conjunctivitis, and mechanistically it may relieve a histamine-mediated component of ocular surface inflammation.

The link to rosacea conjunctivitis is weak. Ocular rosacea is driven mainly by meibomian gland dysfunction, Demodex mites, and neutrophil- and MMP-mediated inflammation, not primarily by histamine. At best, an antihistamine might ease itch or allergic-type symptoms. The prediction rests only on the TxGNN score, with no supporting trials or literature.

The other nine predictions are also supported by model output only (all L5, Hold). Several are mechanistically implausible and are likely knowledge-graph proximity artefacts:

| Rank | Predicted Indication | Score | Plausibility |
|---|------|------|------|
| 2 | Punctate epithelial keratoconjunctivitis | 98.63% | Symptomatic benefit at best; often viral or toxic |
| 3 | Blepharoconjunctivitis | 98.40% | Plausible for the allergic subtype only |
| 4 | Viral conjunctivitis | 98.17% | No antiviral activity; itch relief only |
| 5 | Parasitic eyelid infestation | 96.67% | Needs an antiparasitic; antihistamine relieves pruritus only |
| 6 | Ulcerative blepharitis | 96.59% | Needs antimicrobial and lid hygiene |
| 7 | Infective urethral stricture | 96.33% | No plausible link; fibrotic condition managed surgically |
| 8 | Postinfectious vasculitis | 96.13% | Indirect; not disease-modifying |
| 9 | Post-bacterial disorder | 96.11% | Term too non-specific to assess |
| 10 | Noninfectious dermatoses of eyelid | 95.84% | Most plausible after allergic conjunctival; topical therapy usually preferred |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 4237B | Telfast | Tablet 60 mg (oral) | Not specified in the data compiled for this report |

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text):** hypertension and hypertensive disorder, kidney disease, diabetes mellitus and diabetic ketoacidosis, benign prostatic hyperplasia, coronary artery disease, coronary atherosclerosis, arteriosclerosis and atherosclerosis, angle-closure glaucoma, hyperthyroidism, Graves disease and thyrotoxicosis, and pyoureter. These come from graph edges and should be verified against the Product Information (PI), as some are typical of older, sedating or decongestant-containing antihistamine products.
- **Drug Interactions:** The interaction query returned 100 interactions in total; the 20 shown in the compiled data are summarised below.
  - *Moderate:* eliglustat, eluxadoline, rolapitant, and antacids (magnesium hydroxide, aluminium hydroxide, magaldrate, magnesium carbonate). Antacids containing aluminium or magnesium may reduce fexofenadine absorption, so dosing should be separated.
  - *Minor:* clarithromycin, miconazole, clotrimazole.
  - *Severity unclassified:* calcitriol, doxycycline, cimetidine, levocarnitine, epinephrine, dolasetron, dicyclomine, chlorhexidine, famotidine, acetylsalicylic acid.

Warnings and contraindications from the label were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials or literature, and the proposed mechanism is weak for rosacea conjunctivitis. Oral fexofenadine is also not an ocular-targeted formulation.

**To proceed, the following is needed:**
- Mechanism of action data to support a mechanistic-link analysis
- Label warnings and contraindications from the TGA PI, to allow safety screening
- A literature and trial search specific to antihistamines in ocular rosacea
- Clarification of the approved indication text for ARTG 4237B
- A route and formulation assessment (oral versus ocular)
- If any prediction is pursued, the allergic blepharoconjunctivitis and eyelid dermatitis subtypes are the more mechanistically credible candidates for further review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

