---
layout: default
title: Teduglutide
parent: Model Prediction Only (L5)
nav_order: 702
evidence_level: L5
indication_count: 10
---

# Teduglutide
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

# Teduglutide: From Short Bowel Syndrome to Papillary Conjunctivitis

## One-Sentence Summary

Teduglutide is a GLP-2 receptor agonist peptide, originally used to treat short bowel syndrome.
The TxGNN model predicts it may be effective for **papillary conjunctivitis**, but this is a model prediction only,
with **0 clinical trials** and **0 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Short bowel syndrome |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 98.53% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Teduglutide is an analogue of glucagon-like peptide-2 (GLP-2) and acts on the GLP-2 receptor (GLP2R). Detailed mechanism of action data was not available in the data compiled for this report. Its known pharmacology is to promote growth of the intestinal lining and improve absorption, which is why it is used in short bowel syndrome.

The link between short bowel syndrome and papillary conjunctivitis is weak. Papillary conjunctivitis is an allergic or mechanical inflammatory condition of the ocular surface, and the eye is not a recognised GLP-2 target. No credible mechanistic bridge was identified. The high TxGNN score (98.53%) reflects a graph-based prediction only and is not supported by any clinical or literature evidence. It should be treated as a likely model artefact rather than a real therapeutic signal.

For context, other top-ranked predictions include gastroduodenitis and peptic ulcer disease, which are biologically more plausible because GLP-2 has effects on gastrointestinal mucosa. These also have no trials or publications. Two further predictions, chronic intestinal vascular insufficiency and isolated mesenteric vein thrombosis, are only indirectly related, through short bowel syndrome as a downstream consequence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11793Q | Revestive | Powder for injection 5 mg with diluent (injectable) | Not available in the data compiled for this report |

## Safety Considerations

- **Drug Interactions**: 17 interaction records were found. One is rated **Major** (bexarotene). Fifteen are rated **Moderate** and involve benzodiazepines (alprazolam, chlordiazepoxide, clobazam, clonazepam, clorazepic acid, diazepam, estazolam, flurazepam, halazepam, lorazepam, midazolam, oxazepam, quazepam, temazepam, triazolam). The remaining record is a pharmacology entry confirming the GLP-2 receptor as the target.
- **Class consideration**: Teduglutide's growth-promoting effects raise a caution regarding neoplasia in the gastrointestinal tract. This should be weighed before any new use.

Warnings and contraindications from the product label were not available. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a graph-based score. There are no clinical trials or publications, no plausible mechanism linking GLP-2 agonism to papillary conjunctivitis, and a systemic injectable would be a disproportionate option for a mostly local ocular condition.

**To proceed, the following is needed:**
- A credible mechanistic rationale for GLP-2 signalling in ocular surface inflammation, supported by preclinical data
- Detailed mechanism of action data
- TGA Product Information (approved indication, warnings and contraindications)
- Route compatibility assessment, since the available route is injectable only
- Consider redirecting effort to the more plausible gastrointestinal predictions (gastroduodenitis, peptic ulcer disease), with a neoplasia risk review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

