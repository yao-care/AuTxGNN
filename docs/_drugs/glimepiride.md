---
layout: default
title: Glimepiride
parent: Model Prediction Only (L5)
nav_order: 338
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "Glimepiride"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
description: "Glimepiride: predicted new indication Classic stiff person syndrome (evidence level L5). In Australia: 8 PBS items (8 currently listed)"
---

# Glimepiride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Glimepiride: Classic stiff person syndrome
{: .text-alpha }

## One-Sentence Summary

Glimepiride is a sulfonylurea originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **classic stiff person syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction. It is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (8 of 8 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 8 (valid: 8) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for glimepiride: "Glimepiride primarily lowers blood glucose by stimulating the release of insulin from pancreatic beta cells. Sulfonylureas bind to the sulfonylurea receptor in the pancreatic beta-cell plasma membrane, leading to closure of the ATP-sensitive potassium channel, thereby stimulating the release of insulin." ([DailyMed: Glimepiride 3 Mg (glimepiride) prescribing information, Lifsa Drugs LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=51157849-7990-4a8b-ae50-eda1baf93cfa), label version 2024-08-20; accessed 2026-11-19.) Glimepiride belongs to the sulfonylurea class. These drugs stimulate insulin release by closing K-ATP channels on pancreatic beta cells, and this is how they control blood glucose in type 2 diabetes.

On current information, the prediction is **not** well supported mechanistically. Stiff person syndrome is an autoimmune neurological disorder of GABAergic signalling, usually associated with anti-GAD antibodies. Glimepiride's pharmacology (beta-cell K-ATP channel blockade) has no known link to this pathway. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, such as the GAD/diabetes association, not biological evidence or a pharmacological rationale. The same applies to the closely related "focal stiff limb syndrome" prediction. The high score (0.9975) reflects the TxGNN model's output only and is not clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 8450R | Glimepiride Sandoz | Glimepiride | Tablet 1 mg | Valid |
| 8451T | Glimepiride Sandoz | Glimepiride | Tablet 2 mg | Valid |
| 8452W | Glimepiride Sandoz | Glimepiride | Tablet 4 mg | Valid |
| 8533D | Glimepiride Sandoz | Glimepiride | Tablet 3 mg | Valid |
| 13848W | Glimepiride Sandoz | Glimepiride | Tablet 1 mg | Valid |
| 13870B | Glimepiride Sandoz | Glimepiride | Tablet 2 mg | Valid |
| 14020X | Glimepiride Sandoz | Glimepiride | Tablet 3 mg | Valid |
| 14055R | Glimepiride Sandoz | Glimepiride | Tablet 4 mg | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

The approved indication text was not available for this entry. Refer to the TGA Product Information (PI).

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (not taken from label text): kidney disease, liver disease, congestive heart failure, gallbladder disease, hypopituitarism and other pituitary hormone deficiencies, osteoporosis, and infectious disease. Verify these against the PI.
- **Drug interactions**: 100 interactions were identified, and the 20 reviewed are mostly rated Moderate. Examples include:
  - ethanol
  - hydrochlorothiazide and acetazolamide
  - NSAIDs (ibuprofen, ketorolac)
  - H2 blockers (famotidine, ranitidine)
  - beta-agonists and sympathomimetics (salbutamol, formoterol, epinephrine, phenylephrine, pseudoephedrine)
  - acebutolol
  - albiglutide
  - ethinylestradiol
  - acitretin
  - nitazoxanide
  - systemic hydrocortisone

  Topical corticosteroids are rated Minor. Check the full list before any use.

Please refer to the TGA-approved Product Information (PI) for the authoritative warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. There are no trials or publications, and no plausible mechanistic link between a sulfonylurea and an autoimmune GABAergic disorder. Using glimepiride in a non-diabetic neurological condition would also expose patients to hypoglycaemia risk without any supporting benefit data.

**To proceed, the following is needed:**
- Mechanistic evidence linking glimepiride or K-ATP channel modulation to stiff person syndrome pathophysiology
- Any preclinical or clinical data in stiff person syndrome
- Confirmation of the approved indication and safety information from the TGA PI
- Review of other predicted indications in the same list. Type 1 diabetes mellitus (rank 10) has more activity, with 12 trials and 12 publications retrieved, but most of those trials involve type 2 diabetes. It would need its own dedicated evaluation.

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Glimepiride 3 Mg (glimepiride) prescribing information, Lifsa Drugs LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=51157849-7990-4a8b-ae50-eda1baf93cfa) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

