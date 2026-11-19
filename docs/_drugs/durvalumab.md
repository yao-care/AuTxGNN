---
layout: default
title: Durvalumab
parent: Model Prediction Only (L5)
nav_order: 236
evidence_level: L5
indication_count: 6
monitor_inn: "Durvalumab"
predicted_indications: ["uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
last_modified_at: 2026-11-20
description: "Durvalumab: predicted new indication Uterine ligament adenocarcinoma (evidence level L5). Approved use: Transitional cell carcinoma"
---

# Durvalumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Durvalumab: From Transitional Cell Carcinoma to Uterine Ligament Adenocarcinoma
{: .text-alpha }

## One-Sentence Summary

Durvalumab has a recorded relation to **transitional cell carcinoma** in the knowledge graph. In Australia it is marketed as Imfinzi.
The TxGNN model predicts it may be useful for **uterine ligament adenocarcinoma**.
However, **no clinical trials and no publications** were found for this disease, so the prediction currently rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Transitional cell carcinoma (a relation recorded in the knowledge graph; the Australian licence record contains no approved indication text) |
| Predicted New Indication | Uterine ligament adenocarcinoma |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (at least 20 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for durvalumab: "Expression of programmed cell death ligand-1 (PD-L1) can be induced by inflammatory signals (e.g., IFN-gamma) and can be expressed on both tumor cells and tumor-associated immune cells in the tumor microenvironment. PD-L1 blocks T-cell function and activation through interaction with PD-1 and CD80 (B7.1). […] Durvalumab is a human immunoglobulin G1 kappa (IgG1κ) monoclonal antibody that binds to PD-L1 and blocks the interaction of PD-L1 with PD-1 and CD80 (B7.1)." ([DailyMed: Imfinzi (durvalumab) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8baba4ea-2855-42fa-9bd9-5a7548d4cec3), label version 2026-08-31; accessed 2026-11-19.) Durvalumab is generally understood to be an anti-PD-L1 antibody, a type of immune checkpoint inhibitor. This comes from general knowledge of the drug class, not from the compiled data.

A possible rationale is that some gynaecological adenocarcinomas may depend on PD-L1 signalling to evade the immune system. In that case, blocking PD-L1 could be relevant. This is speculative. No study in the compiled data examines PD-L1 biology or durvalumab response in uterine ligament adenocarcinoma, and the link to the original tumour type cannot be verified.

The model score is very high (0.9992), but it is a statistical prediction and not evidence of clinical benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for uterine ligament adenocarcinoma.

---

## Literature Evidence

Currently no related literature available for uterine ligament adenocarcinoma.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11911X | Imfinzi | Solution concentrate for I.V. infusion, 120 mg in 2.4 mL | Not stated in the licence record compiled for this report |

This is a single-ingredient product and its licence status is valid.

---

## Cytotoxicity

Durvalumab is used in cancer, so this section is included.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-L1 antibody, not a conventional cytotoxic) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the Product Information (PI) warnings and precautions |
| Handling Protection | Please refer to the Product Information (PI) and local institutional policy |

---

## Safety Considerations

**Drug Interactions**: The interaction screen returned 81 interactions. The first 20 are summarised here.
- **Major**: adalimumab.
- **Moderate**:
  - Corticosteroids: hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone, methylprednisolone and deflazacort.
  - Immunomodulators: alefacept, alemtuzumab and anakinra.
  - Others: roflumilast, a tetanus toxoid vaccine and an anthrax vaccine.
- **Minor**: zinc salts (acetate, gluconate, sulfate and chloride).

Many of these are immunosuppressive or immune-modulating agents, so co-prescribing needs careful review.

For warnings and contraindications, please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications for this specific disease, so the evidence level is L5. The mechanistic link cannot be checked because MOA data are missing. The licence record also lists no approved indication text.

**To proceed, the following is needed:**
- Any clinical or preclinical study directly examining durvalumab in uterine ligament adenocarcinoma, such as case series, PD-L1 expression data or trial registrations.
- Detailed mechanism of action data.
- The TGA Product Information (PI), to confirm the approved indications, warnings and contraindications.
- A separate review of the neighbouring prediction, **endocervical carcinoma** (score 0.9991). It has one completed Phase 1 trial (NCT03452332, n=20, radiotherapy with durvalumab and tremelimumab). This trial addresses safety and feasibility, not efficacy, but it may be a better-supported starting point.

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Imfinzi (durvalumab) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8baba4ea-2855-42fa-9bd9-5a7548d4cec3) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

