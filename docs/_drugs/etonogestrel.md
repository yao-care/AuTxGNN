---
layout: default
title: Etonogestrel
parent: Model Prediction Only (L5)
nav_order: 276
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
monitor_inn: "Etonogestrel"
predicted_indications: ["amenorrhea (disease)", "breast fibrocystic disease", "apocrine adenosis of breast", "blunt duct adenosis of breast", "benign mammary dysplasia"]
description: "Etonogestrel: predicted new indication Amenorrhea (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Etonogestrel
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Etonogestrel: Amenorrhea (disease)
{: .text-alpha }

## One-Sentence Summary

Etonogestrel is a progestin delivered as a subcutaneous implant (Implanon NXT in Australia), and it is used for contraception.
The TxGNN model predicts it may be relevant to **amenorrhoea**, but there are **no registered clinical trials** and **no directly relevant publications** supporting this.
The prediction is model-based only, and amenorrhoea is better understood as a known bleeding-pattern effect of the implant than as a treatment target.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 0.9984 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on general pharmacology, etonogestrel is a progestin that suppresses ovulation and thins the endometrium.

Amenorrhoea is a well-recognised effect of etonogestrel implant use, so the link is biologically plausible. However, it is an adverse or bleeding-pattern effect, not a therapeutic indication. The model's high score likely reflects this strong association rather than a true treatment opportunity. The only linked paper (PMID 33430924) concerns BIO101 in COVID-19 pneumonia and is unrelated.

Other predicted indications were also reviewed. They are all supported by prediction only or by indirect evidence:
- **Benign breast conditions** (fibrocystic disease, adenosis variants, benign mammary dysplasia): the rationale is hormonal modulation of breast tissue, with no trials or literature.
- **Acne**: the linked paper reports acne as an adverse event of implants, so the evidence may point the opposite way.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no directly relevant literature is available for amenorrhoea. The one linked paper is unrelated to this drug and indication.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33430924](https://pubmed.ncbi.nlm.nih.gov/33430924/) | 2021 | RCT protocol (unrelated) | Trials | Study protocol for BIO101 in preventing respiratory deterioration in COVID-19 pneumonia; not relevant to etonogestrel |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 8487Q | Implanon NXT | Subcutaneous implant 68 mg | Not stated in the data compiled for this report |

---

## Safety Considerations

- **Disease associations flagged by the knowledge graph** (these come from a knowledge graph of drug-disease contraindication links, not from product label text): hypertension, epilepsy, anxiety and neurotic disorders, porphyria, kidney disease, liver disease, gallbladder disease, systemic lupus erythematosus, asthma, diabetes mellitus and diabetic ketoacidosis, hypertriglyceridaemia and hyperlipidaemia, female breast carcinoma, thrombophlebitis, migraine, coronary artery disease, and obesity.
- **Drug Interactions**: 100 interactions were found, and the 20 listed in the data are all rated Moderate. They include:
  - antidiabetic agents (acarbose, metformin, glimepiride, chlorpropamide, alogliptin, saxagliptin, canagliflozin, dapagliflozin, empagliflozin, semaglutide, dulaglutide, albiglutide)
  - insulins (aspart, degludec, detemir, glargine, glulisine)
  - others (aprepitant, clarithromycin, linaclotide)

For warnings and contraindications from the label, please refer to the TGA-approved Product Information (PI).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5). There are no trials and no relevant literature, and amenorrhoea is an expected effect of the implant rather than a condition it would treat. The other predicted indications are similarly unsupported or only indirectly supported.

**To proceed, the following is needed:**
- Retrieve the TGA Product Information to confirm the approved indication, warnings and contraindications
- Obtain mechanism of action data
- Clarify whether amenorrhoea should be considered a therapeutic target (for example, in heavy menstrual bleeding or endometriosis-related use) or just an adverse effect
- Search for direct clinical evidence of benefit for any proposed new indication
- Assess how the similarities between related diseases learned by the TxGNN model (deep learning), which are not biological evidence, apply to any new target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

