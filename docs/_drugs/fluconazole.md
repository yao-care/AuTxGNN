---
layout: default
title: Fluconazole
parent: Model Prediction Only (L5)
nav_order: 302
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Fluconazole: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Oral candidiasis, oesophageal candidiasis, vulvovaginal candidiasis…"
monitor_inn: "Fluconazole"
predicted_indications: ["punctate epithelial keratoconjunctivitis"]
---

# Fluconazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Fluconazole: From Candidiasis to Punctate Epithelial Keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Fluconazole is an azole antifungal originally used to treat candidiasis (oral, oesophageal, vulvovaginal and invasive forms) and cryptococcal meningitis.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but there are currently **no clinical trials** and **no publications** supporting this prediction. It rests on a model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Oral candidiasis, oesophageal candidiasis, vulvovaginal candidiasis, candidaemia, disseminated candidiasis, cryptococcal meningitis (the approved indication text for the Australian listing was not available) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9924 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, fluconazole is a triazole antifungal. Its efficacy in candidiasis and cryptococcal infection is established, and it is generally understood to act by inhibiting fungal ergosterol synthesis.

Punctate epithelial keratoconjunctivitis is most often viral (commonly adenoviral) or inflammatory. A fungal cause would be needed for an antifungal mechanism to be relevant. The high TxGNN score (0.9924) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No supporting clinical or literature evidence was found. The link between fluconazole and this condition is therefore currently weak and unconfirmed.


## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1471K | Diflucan | Capsule 50 mg | Not available in the data compiled |

Oral capsule is the only dosage form listed. Whether an ophthalmic or topical route would be needed for the predicted indication has not been assessed.

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** long QT syndrome, familial long QT syndrome, kidney disease, liver disease, gallbladder disease and pyoureter. These should be verified against the TGA-approved Product Information.
- **Drug Interactions:** The interaction screen returned 100 potential interactions; 20 are shown in the data compiled for this report.
  - **Major:** chlorpropamide.
  - **Moderate:** proton pump inhibitors (omeprazole, rabeprazole, dexlansoprazole), famotidine, corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), aprepitant, loperamide, saxagliptin, and several laxatives and bowel preparations (bisacodyl, picosulfuric acid, polyethylene glycol).
  - **Minor:** amphotericin B and clarithromycin.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a score from the TxGNN model (deep learning), which may reflect similarities the model learned between related diseases, not biological evidence. There are no clinical trials or publications, and no plausible mechanism links an antifungal to what is usually a viral or inflammatory eye condition.

**To proceed, the following is needed:**
- Evidence of a fungal or otherwise azole-responsive aetiology in punctate epithelial keratoconjunctivitis
- Preclinical or clinical studies of fluconazole in this condition
- Detailed mechanism of action data
- Assessment of route and formulation suitability, since only an oral capsule is listed in Australia
- Safety information from the TGA-approved Product Information, including the knowledge-graph flags for QT prolongation and kidney and liver disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

