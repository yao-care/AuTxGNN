---
layout: default
title: Alfuzosin
parent: Model Prediction Only (L5)
nav_order: 33
evidence_level: L5
indication_count: 10
---

# Alfuzosin
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

# Alfuzosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Alfuzosin is an alpha-1A-selective adrenergic antagonist originally used to treat benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, alfuzosin is an alpha-1A-selective adrenergic antagonist. Its efficacy in BPH is established, but a mechanistic link to the new indication is not.

Ambras syndrome is a rare congenital disorder linked to genomic rearrangements affecting TRPS1 regulation. An alpha-1 blocker is not expected to act on this genetic basis. The very high score most likely reflects proximity to hair-related phenotypes in the knowledge graph rather than a biologically plausible mechanism.

The other top predictions point the same way. They include hypertrichosis, several congenital hair and malformation syndromes, and hypotrichosis (the opposite phenotype). That contradiction suggests the scores reflect graph proximity rather than pharmacology. Some vasoactive drugs, such as minoxidil, are known to cause hypertrichosis, so a vascular route to hair growth is conceivable. However, alfuzosin has no documented hair-growth effect.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14183L | Xatral SR | Tablet 10 mg (oral) | Not stated in the data compiled for this report |

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these are graph relationships, not label text): multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, hypotensive disorder, long QT syndrome (including familial), torsades de pointes, liver failure, liver disease, gallbladder disease, and intraoperative floppy iris syndrome.
- **Drug Interactions**: 100 interactions were identified (the first 20 were available for review).
  - **Major**: cisapride, clarithromycin, dolasetron.
  - **Moderate**: famotidine, aprepitant, bisacodyl, bupropion, SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin), granisetron, levofloxacin, clotrimazole, dronabinol, and several laxatives (castor oil, glycerin, lactitol, lactulose).
  - **Minor**: cimetidine.
  - The QT-related items (cisapride, dolasetron, clarithromycin) are consistent with the long QT and torsades flags above.

Label warnings and contraindications were not available, so please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications (L5), and no plausible mechanism has been identified. The score appears to be a knowledge-graph artefact. The hair-related predictions are also internally inconsistent, covering both excess hair growth and hair loss.

**To proceed, the following is needed:**
- Mechanism of action data for alfuzosin, and a plausible biological link to TRPS1 or hair follicle biology
- Preclinical evidence (for example, hair follicle or cell models) showing a relevant effect
- Systematic literature and trial registry searches (including ANZCTR) to confirm there is no existing evidence
- Review of the ARTG product information, including the approved indication, warnings and contraindications
- A safety assessment for the target population, including hypotension and QT-related risks
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

