---
layout: default
title: Benzocaine
parent: Model Prediction Only (L5)
nav_order: 85
evidence_level: L5
indication_count: 10
---

# Benzocaine
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

# Benzocaine: From Tinea Pedis, Dermatitis and Pharyngitis to Papillary Conjunctivitis

## One-Sentence Summary

Benzocaine is a topical ester local anaesthetic, originally used for symptom relief in conditions such as tinea pedis, dermatitis, pharyngitis, tinea corporis and tinea infections.
The TxGNN model predicts it may be effective for **papillary conjunctivitis** (its top-ranked prediction), but there are currently **0 clinical trials** and **0 publications** supporting this specific indication.
The strongest evidence in the data compiled for this report relates to a lower-ranked prediction, **dyspepsia** (2 publications, including 1 RCT).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the ARTG data compiled for this report. Knowledge-graph indications: tinea pedis, dermatitis, pharyngitis, tinea corporis, tinea infection |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 (model prediction only) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, benzocaine is a topical ester local anaesthetic that blocks voltage-gated sodium channels. This provides symptomatic relief of pain and irritation rather than treating the underlying disease.

Its existing indications (dermatitis, tinea, pharyngitis) are largely conditions where surface discomfort or itch is relieved. The TxGNN prediction for papillary conjunctivitis likely reflects this graph-level association with surface and mucosal inflammatory conditions. Benzocaine could plausibly ease ocular surface discomfort, but it has no known effect on the allergic or mechanical pathophysiology of papillary conjunctivitis. Repeated use of topical ocular anaesthetics is also associated with corneal toxicity. The mechanistic link therefore cannot be verified and is weak.

**Other predictions in the top 10** share a similar pattern:
- **Eye and eyelid conditions** (blepharoconjunctivitis, rosacea conjunctivitis, ulcerative blepharitis, parasitic eyelid infestation, noninfectious eyelid dermatoses): all are prediction-only. The diseases are driven by inflammation, infection, parasites or gland dysfunction, none of which benzocaine addresses.
- **Cutaneous candidiasis:** benzocaine has no established antifungal activity.
- **Nasal cavity disease and acute laryngopharyngitis:** topical mucosal anaesthesia is plausible. Acute laryngopharyngitis is adjacent to the existing pharyngitis use, so it is closer to a label extension than true repurposing.
- **Dyspepsia** (rank 4): the only prediction with supporting literature (see below).

## Clinical Trial Evidence

Currently no related clinical trials registered for papillary conjunctivitis or for any of the other top-10 predicted indications in the data compiled for this report.

## Literature Evidence

No literature is available for the top-ranked prediction (papillary conjunctivitis). The only literature identified relates to the rank 4 prediction, dyspepsia:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15219296](https://pubmed.ncbi.nlm.nih.gov/15219296/) | 2004 | RCT | J Emerg Med | Prospective, randomised, single-blinded comparison of viscous lidocaine versus benzocaine as the topical anaesthetic in a "GI cocktail" for dyspepsia in emergency patients. Benzocaine was tested as a component of the cocktail, not as a standalone therapy. The abstract provided was truncated, so results are not confirmed. |
| [23565580](https://pubmed.ncbi.nlm.nih.gov/23565580/) | 2013 | Mechanistic physiology study | Neurogastroenterol Motil | Examined the role of duodenal mucosal nerve endings in the acid-induced duodenogastric reflex, using benzocaine in healthy humans. Provides indirect mechanistic support, as duodenal acid hypersensitivity is a proposed mechanism in functional dyspepsia. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 156F | Not available | Not available | Not available |

Only one licence record was found, and its product name, dosage form and approved indication fields are empty in the data compiled for this report. The licence number should be verified against the ARTG directly.

## Safety Considerations

The TGA-approved Product Information (PI) was not available in the data compiled for this report, so please refer to it for warnings, contraindications and drug interactions. No drug interaction records were found.

The following are **knowledge-graph contraindication associations** (not label text) and should be interpreted with caution. They include:
- **Hepatic and renal:** liver failure, liver disease, hepatic coma, hepatic encephalopathy, kidney disease, gallbladder disease
- **Haematological:** thrombocytopenia, neutropenia, agranulocytosis, blood coagulation disease, porphyria (including inherited porphyria and porphyrin metabolism disease)
- **Neuropsychiatric:** epilepsy, anxiety disorder, neurotic disorder, dysthymic disorder, substance abuse/dependence
- **Metabolic and other:** diabetes mellitus, diabetic ketoacidosis, hyperparathyroidism, hypercalcaemia, nephrocalcinosis, sarcoidosis, gastritis, herpes simplex infection, exanthem, and others

Several of these appear to reflect class-wide or non-specific associations rather than benzocaine-specific risks, and they require verification against the PI.

Additional considerations from the prediction rationale:
- Topical ocular anaesthetics carry a risk of corneal toxicity with repeated use.
- Benzocaine can cause contact sensitisation and dermatitis, and periocular application adds risk.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (papillary conjunctivitis) rests on model score alone (L5), with no trials or literature and a weak mechanistic link. Ocular use also carries a recognised corneal toxicity concern. Of the ten predictions, only dyspepsia has any supporting literature (L4, flagged as a research question), and that evidence is indirect, with benzocaine used as a cocktail component or physiological probe rather than a tested standalone therapy.

**To proceed, the following is needed:**
- Mechanism of action data (currently unavailable)
- The TGA-approved PI, and complete ARTG details (product, dosage form, indication) for licence 156F
- A full-text review of PMID 15219296 to confirm results
- For any ocular indication, a corneal safety assessment and evidence of benefit beyond symptomatic relief
- Route and formulation compatibility assessment between the registered product and the predicted indication
- Consideration of acute laryngopharyngitis as a pragmatic label extension, given its proximity to the existing pharyngitis use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

