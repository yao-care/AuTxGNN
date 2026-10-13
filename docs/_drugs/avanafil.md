---
layout: default
title: Avanafil
parent: Model Prediction Only (L5)
nav_order: 72
evidence_level: L5
indication_count: 10
---

# Avanafil
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

# Avanafil: From Erectile Dysfunction to Amenorrhoea

## One-Sentence Summary

Avanafil is a PDE5 inhibitor originally used to treat erectile dysfunction (the knowledge graph also lists psychologic dyspareunia and premature ejaculation).
The TxGNN model predicts it may be effective for **amenorrhoea**,
but there are currently **0 clinical trials** and **0 publications** in the data compiled for this report, so the prediction is computational only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Erectile dysfunction (Australian ARTG indication text not available in the data compiled; original indications drawn from the TxGNN knowledge graph) |
| Predicted New Indication | Amenorrhoea |
| TxGNN Prediction Score | 94.59% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, avanafil is a PDE5 inhibitor. PDE5 inhibition raises cGMP, which promotes smooth muscle relaxation and vasodilation. This is the basis of its effect in erectile dysfunction.

A theoretical link to uterine or pelvic blood flow exists. However, amenorrhoea is mainly driven by hormonal causes (such as hypothalamic, pituitary or ovarian dysfunction) or structural causes. A vasodilatory mechanism is unlikely to address these directly. The high TxGNN score is a computational prediction only, with no supporting trials or literature.

**Other top-ranked predictions** (all L5, no trials or literature):

| Rank | Predicted Indication | Score | Comment |
|------|------|------|------|
| 2 | Hypoalphalipoproteinaemia | 91.54% | No clear mechanistic link to HDL metabolism; speculative |
| 3 | Malignant catarrh | 90.62% | Veterinary ruminant viral disease; likely a knowledge-graph artefact |
| 4 | Infectious bovine rhinotracheitis | 90.62% | Veterinary disease; likely a knowledge-graph artefact |
| 5 | Raynaud disease | 88.54% | Most mechanistically plausible (digital artery vasodilation). Other PDE5 inhibitors have been studied, but no avanafil-specific data are available. Flagged as a research question |
| 9 | Stroke disorder | 79.21% | Theoretical relevance only; cardiovascular safety concerns |

Raynaud disease is the candidate most worth separate follow-up. Any class-effect evidence from other PDE5 inhibitors would need independent verification before the evidence level could be upgraded.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11837B | Spedra | Tablet 50 mg (oral) | Not available in the data compiled |

## Safety Considerations

- **Drug Interactions**: 53 interactions were identified in total. Examples from the 20 listed:
  - **Major**: aprepitant, clarithromycin, cobicistat, amyl nitrite
  - **Moderate**: SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin), dexamethasone, ethanol, papaverine, phentolamine, diazoxide, epoprostenol, iloprost, deferasirox, fostamatinib, lorcaserin, troglitazone, nitrous acid
- Interactions with nitrates (such as amyl nitrite) and with CYP3A4 inhibitors (such as clarithromycin and cobicistat) are of particular clinical importance. They may cause marked hypotension or raised avanafil exposure.
- For warnings and contraindications, please refer to the TGA-approved Product Information (PI). Label-level safety data were not available in the data compiled.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for amenorrhoea rests only on a model score, with no clinical trials or literature, and the mechanistic link is weak. Most other top predictions have no plausible mechanism. Raynaud disease is the one candidate with a credible rationale, and it could be pursued as a separate research question.

**To proceed, the following is needed:**
- Avanafil-specific literature and trial searches (including ANZCTR) for the predicted indications, especially Raynaud disease
- Review of class-effect evidence from other PDE5 inhibitors, verified independently
- Detailed mechanism of action data
- TGA Product Information warnings, contraindications and approved indication text, to enable safety screening
- Assessment of cardiovascular safety and DDI risk in the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

