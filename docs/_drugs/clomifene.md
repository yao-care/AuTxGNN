---
layout: default
title: Clomifene
parent: Model Prediction Only (L5)
nav_order: 172
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Clomifene: predicted new indication 46,XY disorder of sex development due to testicular steroidogenesis defect (evidence level L5). Approved use: Female infertility"
monitor_inn: "Clomifene"
predicted_indications: ["46,XY disorder of sex development due to testicular steroidogenesis defect", "transverse vaginal septum", "longitudinal vaginal septum", "symptomatic form of fragile X syndrome in female carrier", "blepharophimosis-epicanthus inversus-ptosis", "blepharophimosis-epicanthus inversus-ptosis due to 3q23 rearrangement syndrome", "partial trisomy/tetrasomy of the short arm of chromosome 18", "partial trisomy/tetrasomy of the short arm of chromosome 5", "partial trisomy/tetrasomy of the short arm of chromosome 12", "anovulation"]
---

# Clomifene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Clomifene: From Female Infertility to 46,XY Disorder of Sex Development Due to Testicular Steroidogenesis Defect
{: .text-alpha }

## One-Sentence Summary

Clomifene is an oral ovulation-inducing medicine, originally used to treat female infertility.
The TxGNN model predicts it may be useful for **46,XY disorder of sex development due to testicular steroidogenesis defect**, with a very high model score.
However, there are currently **no clinical trials and no publications** supporting this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Female infertility |
| Predicted New Indication | 46,XY disorder of sex development due to testicular steroidogenesis defect |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in the data compiled for this report. Clomifene is a selective estrogen receptor modulator (SERM). It blocks estrogen receptors in the hypothalamus, which reduces negative feedback and raises GnRH, FSH and LH secretion. This is the basis of its use for ovulation induction in female infertility.

The link to the predicted indication is weak. In this condition, the primary defect is an enzymatic block in testicular steroid production, which sits downstream of the gonadotropin axis. Raising LH stimulation is unlikely to correct a block in the enzymes themselves. The high score (0.999) is therefore best read as a TxGNN model (deep learning) prediction, probably driven by shared reproductive-endocrine associations, rather than as evidence of a therapeutic mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1211R | Clomid | Tablet containing clomifene citrate 50 mg (oral) | Not listed in the data compiled for this report |

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

**Note:** Among the other predictions for clomifene, *anovulation* is the only one with trial and literature support (including a randomised letrozole versus clomifene trial, NCT00478504, and the M-OVIN trial, PMID 29273245). It overlaps with the existing female infertility indication, so it confirms current use rather than representing true repurposing.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

