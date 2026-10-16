---
layout: default
title: Sodium Bicarbonate
parent: Model Prediction Only (L5)
nav_order: 679
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Sodium Bicarbonate: predicted new indication Bronchitis (evidence level L5). Approved use: Not available"
---

# Sodium Bicarbonate
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

# Sodium Bicarbonate: From an Unspecified Original Indication to Bronchitis

## One-Sentence Summary

Sodium bicarbonate is an alkalinising agent and antacid with one ARTG entry in Australia, but the data compiled for this report contain no approved indication text.
The TxGNN model ranks **bronchitis** as its top prediction (score 97.9%), yet there are **no registered clinical trials** and only **1 publication** (a 1976 physiology study that is not about bronchitis treatment).
Of the ten predictions, only exercise-induced anaphylaxis shows a direct, case-level signal. The overall evidence is very weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the ARTG entry has no indication text) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 97.91% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Sodium bicarbonate is a well-known alkalinising agent and antacid that buffers acid and raises pH in the stomach and in blood. On that basis it is used in acid-base disturbances, but the data compiled for this report do not confirm an approved original indication.

For bronchitis, no credible mechanistic link has been established. The only literature item (PMID 778960, 1976) examined how the lung circulation responds to raised carbon dioxide in healthy people and patients with little airway obstruction. It is a physiology study, not evidence of benefit in bronchitis. The high TxGNN score is therefore a model output without clinical support.

Other predictions have somewhat more substance:
- **Anaphylaxis and food-dependent exercise-induced anaphylaxis**: Two small case-level reports (1986 and 1992) describe sodium bicarbonate pretreatment inhibiting exercise-induced and wheat-dependent exercise-induced anaphylaxis. A possible explanation is that it modulates systemic pH and mast cell mediator release. This is hypothesis-generating only and limited to the exercise-induced subtype.
- **Irritable bowel syndrome**: As an antacid it could plausibly alter luminal pH and intestinal ion transport, but no direct evidence supports this.
- **Glaucoma**: A genetic study links a bicarbonate transporter gene (SLC4A10) to open-angle glaucoma. This reflects bicarbonate transport biology, not a treatment effect.

## Clinical Trial Evidence

For the top-ranked indication (bronchitis), currently no related clinical trials are registered.

For context, one trial was linked to the second-ranked prediction, irritable bowel syndrome:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00796354](https://clinicaltrials.gov/study/NCT00796354) | Phase 3b/4 | Completed | 210 | Multi-centre, double-blind, randomised, placebo-controlled study of Movicol® in constipation associated with IBS. The role of sodium bicarbonate is unverified (Movicol is a macrogol-based laxative), so this should not be treated as direct evidence. |

## Literature Evidence

For bronchitis, the only linked publication is:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [778960](https://pubmed.ncbi.nlm.nih.gov/778960/) | 1976 | Physiology study | Respiration | Breathing 5% CO2 raised pulmonary artery pressure and vascular resistance in 44 patients with little or no airway obstruction and 20 normal men. It does not address bronchitis treatment. |

The most relevant publications for the more plausible signal (exercise-induced anaphylaxis) are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3024520](https://pubmed.ncbi.nlm.nih.gov/3024520/) | 1986 | Case report / small clinical study | Allergy | Reports inhibition of exercise-induced anaphylaxis with sodium bicarbonate (no abstract available). |
| [1310835](https://pubmed.ncbi.nlm.nih.gov/1310835/) | 1992 | Case report | Annals of Allergy | Pretreatment with sodium bicarbonate inhibited recurrence of anaphylactic symptoms after wheat and exercise challenge, along with the fall in blood pH relative to the rise in plasma histamine. |
| [11496564](https://pubmed.ncbi.nlm.nih.gov/11496564/) | 2001 | Review | Anales de Medicina Interna | General review of exercise-induced anaphylaxis syndrome. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 452T | Not specified | Not specified | Not specified |

## Safety Considerations

**Drug Interactions** (100 interactions were identified in total; the main ones are listed below):
- **Moderate**: doxycycline, tetracycline, minocycline, acetylsalicylic acid, atropine, bisacodyl, chlorpropamide, acetohexamide, glipizide, ephedrine, pancrelipase
- **Minor**: famotidine, ranitidine, cimetidine, hydrocortisone, triamcinolone, dexamethasone, betamethasone, misoprostol

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, bronchitis, has no clinical trials and no supportive literature, so it remains a model output only (L5). The strongest signal is exercise-induced anaphylaxis, supported only by old, small case-level reports (L4). That is a research question rather than a basis for repurposing.

**To proceed, the following is needed:**
- Approved indication text and Product Information (warnings and contraindications) for the ARTG entry
- Mechanism of action data
- Manual review of NCT00796354 to confirm whether sodium bicarbonate was an intervention
- A focused literature review and, if warranted, a controlled study in exercise-induced anaphylaxis
- Route and formulation compatibility assessment for any proposed new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

