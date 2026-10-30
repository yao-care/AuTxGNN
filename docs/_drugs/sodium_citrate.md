---
layout: default
title: Sodium Citrate
parent: Model Prediction Only (L5)
nav_order: 681
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-30
description: "Sodium Citrate: predicted new indication Papillary conjunctivitis (evidence level L5). Approved use: Peptic ulcer disease, gastroesophageal reflux disease, dyspepsia…"
monitor_inn: "Sodium citrate"
predicted_indications: ["papillary conjunctivitis", "nasal cavity disease", "stomach disease", "postgastrectomy syndrome", "gastroduodenitis", "familial visceral myopathy", "rosacea conjunctivitis", "allergic urticaria"]
---

# Sodium Citrate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Sodium Citrate: From Peptic Ulcer Disease and Reflux to Papillary Conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Sodium citrate is an acid-buffering agent, originally used for upper gastrointestinal conditions such as peptic ulcer disease, gastroesophageal reflux disease and dyspepsia, as well as upper-airway conditions such as the common cold and pharyngitis.
The TxGNN model predicts it may be effective for **papillary conjunctivitis**, but **no clinical trials and no publications** currently support this prediction.
The prediction is a model output only and should be treated as a hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease, gastroesophageal reflux disease, dyspepsia, pharyngitis, common cold (the registered ARTG indication text is not available) |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available for this report. Based on known information, sodium citrate is a buffering agent and antacid. Its efficacy in acid-related upper gastrointestinal conditions is the basis for the original indications.

For papillary conjunctivitis, no plausible mechanistic link to acid buffering is evident. Papillary conjunctivitis is an allergic or mechanically induced inflammatory eye condition. The high score (0.9995) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, so it should not be taken as independent evidence of benefit.

Other high-ranking predictions are closer to the original indications and are noted for context:
- **Nasal cavity disease** and **acute laryngopharyngitis** sit close to the existing rhinitis, nasopharyngitis, pharyngitis and common cold labels. Their scores likely reflect that proximity, and neither has trial or literature support.
- **Stomach disease** (score 0.9989) is the only prediction with a plausible mechanism (gastric acid buffering). Its evidence level is L4, but the supporting literature is mostly preclinical oncology work or incidental mentions of sodium citrate, which offer only indirect support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for papillary conjunctivitis. No ANZCTR entries were identified.

---

## Literature Evidence

Currently no related literature available for papillary conjunctivitis.

For context, the closest-supported prediction (stomach disease) returned publications that are largely indirect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25316860](https://pubmed.ncbi.nlm.nih.gov/25316860/) | 2014 | Community-based randomised trial | J Infect Dis | Tested whether a buffer solution improves the immune response to oral poliovirus vaccine in Bangladesh, based on the idea that stomach acid may neutralise vaccine viruses |
| [7086102](https://pubmed.ncbi.nlm.nih.gov/7086102/) | 1982 | Clinical study | J Clin Gastroenterol | Most patients with active duodenal ulcers did not develop ulcer-type pain after gastroduodenal acidification |
| [1777551](https://pubmed.ncbi.nlm.nih.gov/1777551/) | 1991 | Clinical/pharmacology study | Aliment Pharmacol Ther | Adding glucose and sodium citrate to azapropazone reduced gastric mucosal damage in rats, with a trend towards less blood loss in volunteers |
| [26708213](https://pubmed.ncbi.nlm.nih.gov/26708213/) | 2016 | Preclinical | Oncol Rep | 3-Bromopyruvate with sodium citrate targeted glycolysis and induced apoptosis in gastric cancer cells and slowed tumour growth in an animal model |
| [27163639](https://pubmed.ncbi.nlm.nih.gov/27163639/) | 2016 | Preclinical | Biochem Biophys Res Commun | The same combination induced apoptosis in a gastric cancer cell line |
| [29115645](https://pubmed.ncbi.nlm.nih.gov/29115645/) | 2018 | Animal xenograft/imaging | Oncol Rep | PET/CT imaging in a mouse model used to evaluate glycolysis-targeted therapy |

These papers do not demonstrate clinical efficacy of sodium citrate for the predicted indications.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 457C | Not available | Not available | Not available |

Only one valid single-ingredient licence is on record, and the product name, dosage form and indication text are not available in the data compiled for this report.

---

## Safety Considerations

Label-based warnings and contraindications are not available. Please refer to the TGA-approved Product Information (PI) for safety information.

- **Knowledge-graph contraindication signals** (not label text): hypertension, pancreatitis, adrenal insufficiency (including Addison disease and congenital adrenal hyperplasia), benign prostatic hyperplasia, anuria, impaired renal function, rhabdomyolysis, hypercalcaemia, nephrocalcinosis, coronary artery disease, myocardial infarction, metabolic acidosis, angle-closure glaucoma and ocular hypertension. These should be verified against the PI.
- **Drug Interactions** (100 interactions recorded; main ones listed):
  - **Major:** aluminium hydroxide
  - **Moderate:** tetracyclines (doxycycline, minocycline, tetracycline), levofloxacin, aspirin, iron, rosuvastatin, acalabrutinib, ephedrine and pseudoephedrine
  - **Minor:** sulfonylureas (for example glipizide, glyburide, tolbutamide), lactulose and misoprostol

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for papillary conjunctivitis rests on a model score alone. There are no trials or publications, and no plausible mechanism links an acid buffer to this eye condition. The evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data for sodium citrate, to allow a proper mechanistic-link analysis
- The full ARTG record (product name, dosage form, approved indication) and the PI warnings and contraindications, which are currently a blocking gap for safety screening
- Route and formulation compatibility assessment, since an ocular indication would need a suitable topical ophthalmic product
- A systematic literature search for any direct evidence in papillary conjunctivitis
- If a repurposing direction is pursued, consideration of better-supported candidates such as stomach disease, which would still need clinical-level evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

