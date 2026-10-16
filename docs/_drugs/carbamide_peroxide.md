---
layout: default
title: Carbamide Peroxide
parent: Model Prediction Only (L5)
nav_order: 132
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Carbamide Peroxide: predicted new indication Sinusitis (evidence level L5). Approved use: Ear wax removal (inferred from the product name \"Ear Clear for Ear Wa…"
---

# Carbamide Peroxide
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

# Carbamide Peroxide: From Ear Wax Removal to Sinusitis

## One-Sentence Summary

Carbamide peroxide is a topical oxidising agent that releases hydrogen peroxide and urea. In Australia it is marketed as ear drops for ear wax removal.
The TxGNN model predicts it may be effective for **sinusitis**, but **no clinical trials and no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ear wax removal (inferred from the product name "Ear Clear for Ear Wax Removal"; no approved indication text was available) |
| Predicted New Indication | Sinusitis |
| TxGNN Prediction Score | 94.21% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, carbamide peroxide releases hydrogen peroxide and urea. This gives it oxidative antimicrobial and debriding activity, which is the basis for its use in softening and clearing ear wax.

Mechanistically, this activity could plausibly act against bacteria involved in sinus infections. However, the drug has no established sinonasal indication, and its tolerability on sinonasal mucosa has not been established. The score of 0.942 is a computational prediction only, and the data compiled for this report contain no trial or literature support.

Other predicted conditions are less plausible. Examples are systemic infections (paratyphoid fever, relapsing fever, meningococcal infection), deep infections (bacterial arthritis, peritonitis) and paranasal sinus neoplasm, which a topical oxidising agent cannot reach or treat. Infectious otitis media is the most biologically plausible alternative, because the ear is a familiar site of use. It is still unsupported, and use with a perforated eardrum is a safety concern.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 4176T | Ear Clear for Ear Wax Removal | Ear drops 65 mg per mL (6.5%), 12 mL | Not stated in the data compiled for this report (product name indicates ear wax removal) |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not product label text): purulent otitis media, ear infection, otitis media. This is relevant to the otitis media prediction in particular.
- **Drug Interactions**: No interactions were found in the data compiled for this report.

Product label warnings and contraindications were not available. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5), with no registered trials, no literature and no mechanism data. The knowledge graph also flags ear infections as contraindications, and the product label safety data are missing.

**To proceed, the following is needed:**
- Product label warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Preclinical data on sinonasal mucosal tolerability and ciliary toxicity
- Literature and trial registry searches for peroxide-based treatment of sinusitis
- Assessment of route and formulation compatibility, since the current product is an ear drop only
- Clarification of the approved indication wording for the ARTG entry
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

