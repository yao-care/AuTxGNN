---
layout: default
title: Clomifene
parent: Model Prediction Only (L5)
nav_order: 172
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "Clomifene"
predicted_indications: ["46,XY disorder of sex development due to testicular steroidogenesis defect", "transverse vaginal septum", "longitudinal vaginal septum", "symptomatic form of fragile X syndrome in female carrier", "blepharophimosis-epicanthus inversus-ptosis", "blepharophimosis-epicanthus inversus-ptosis due to 3q23 rearrangement syndrome", "partial trisomy/tetrasomy of the short arm of chromosome 18", "partial trisomy/tetrasomy of the short arm of chromosome 5", "partial trisomy/tetrasomy of the short arm of chromosome 12"]
description: "Clomifene: predicted new indication 46,XY disorder of sex development due to testicular steroidogenesis defect (evidence level L5). In Australia: 1 PBS item (1 currently listed)"
---

# Clomifene
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

## Clomifene: 46,XY disorder of sex development due to testicular steroidogenesis defect
{: .text-alpha }

## One-Sentence Summary

Clomifene is an oral ovulation-inducing medicine, originally used to treat female infertility.
The TxGNN model predicts it may be useful for **46,XY disorder of sex development due to testicular steroidogenesis defect**, with a very high model score.
However, there are currently **no clinical trials and no publications** supporting this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | 46,XY disorder of sex development due to testicular steroidogenesis defect |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for clomifene: "Clomiphene citrate is capable of interacting with estrogen-receptor-containing tissues, including the hypothalamus, pituitary, ovary, endometrium, vagina, and cervix. It may compete with estrogen for estrogen-receptor-binding sites and may delay replenishment of intracellular estrogen receptors." ([DailyMed: Milophene (clomiphene citrate) prescribing information, Burel Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b56131e5-efc7-43af-ac13-4a2ae918df4e), label version 2025-10-07; accessed 2026-11-19.) Clomifene is a selective estrogen receptor modulator (SERM). It blocks estrogen receptors in the hypothalamus, which reduces negative feedback and raises GnRH, FSH and LH secretion. This is the basis of its use for ovulation induction in female infertility.

The link to the predicted indication is weak. In this condition, the primary defect is an enzymatic block in testicular steroid production, which sits downstream of the gonadotropin axis. Raising LH stimulation is unlikely to correct a block in the enzymes themselves. The high score (0.999) is therefore best read as a TxGNN model (deep learning) prediction, probably driven by shared reproductive-endocrine associations, rather than as evidence of a therapeutic mechanism.

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
| 1211R | Clomid | Clomifene | Tablet containing clomifene citrate 50 mg | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

---

## Safety Considerations

The data compiled for this report contains no label-based warnings or contraindications. Please refer to the TGA-approved Product Information (PI) for these.

- **Drug Interactions**: Bexarotene, rated **Major** (DDInter).
- **Contraindication signals from the knowledge graph** (not label text, and to be verified against the PI):
  - Hormone-related conditions: polycystic ovary syndrome, endometriosis, endometrial cancer, thyroid disorders (hypothyroidism, hyperthyroidism), adrenal insufficiency and pituitary tumours.
  - Ovarian conditions: ovarian cyst and ovarian hyperstimulation syndrome.
  - Other conditions: liver disease, gallbladder disease, thrombophlebitis, anxiety and mood-related disorders, and vision disorders including blindness.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (L5), and the mechanism does not plausibly address a downstream testicular steroidogenesis defect. The high score alone is not enough to justify progressing this indication.

**To proceed, the following is needed:**
- Any preclinical or clinical evidence that clomifene-induced gonadotropin stimulation benefits this condition.
- Review of whether an enzymatic block could be bypassed by increased LH drive.
- Mechanism of action data compiled from an authoritative source such as DrugBank.
- TGA Product Information review for warnings and contraindications, particularly in male and paediatric populations, since the approved use is in women.

It overlaps with the existing female infertility indication, so it confirms current use rather than representing true repurposing.

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data was not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Milophene (clomiphene citrate) prescribing information, Burel Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b56131e5-efc7-43af-ac13-4a2ae918df4e) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

