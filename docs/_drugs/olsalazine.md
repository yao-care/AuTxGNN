---
layout: default
title: Olsalazine
parent: Model Prediction Only (L5)
nav_order: 525
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Olsalazine: predicted new indication Myelodysplastic syndrome (evidence level L5). Approved use: Not stated in the data compiled for this report"
monitor_inn: "Olsalazine"
predicted_indications: ["myelodysplastic syndrome", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "alopecia", "diffuse alopecia areata", "partial deletion of the long arm of chromosome 5", "unclassified myelodysplastic syndrome", "refractory cytopenia of childhood", "aregenerative anemia", "severe congenital hypochromic anemia with ringed sideroblasts"]
---

# Olsalazine
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

## Olsalazine: From an Unspecified Original Indication to Myelodysplastic Syndrome
{: .text-alpha }

## One-Sentence Summary

Olsalazine is a dimer of 5-aminosalicylic acid (5-ASA) that is registered in Australia as an oral capsule (Dipentum), but the data compiled for this report do not state an approved indication.
The TxGNN model predicts it may be effective for **myelodysplastic syndrome**, with a very high model score, but there are **0 clinical trials** and **0 publications** supporting this prediction.
This is a model-only prediction with no clinical evidence behind it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the ARTG indication text is blank) |
| Predicted New Indication | Myelodysplastic syndrome |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (2 of 2 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for olsalazine: "Upon reaching the colon, colonic bacteria convert olsalazine into 5‑aminosalicylic acid (5-ASA or mesalazine). The mechanism of action of 5-ASA (mesalamine) is not fully understood, but appears to be a topical anti-inflammatory effect on colonic epithelial cells." ([DailyMed: Dipentum (olsalazine sodium) prescribing information, Viatris Specialty LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8512d0c6-db4e-4673-b3b4-28975c18413f), label version 2026-05-15; accessed 2026-11-19.) Olsalazine is known to be a dimer of 5-ASA that colonic bacteria cleave into two active molecules. It acts locally in the gut, and systemic exposure to the active moiety is low.

No plausible link between a locally acting colonic anti-inflammatory agent and bone marrow or haematopoietic disease can be established from the data compiled. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Several other top predictions are closely related conditions (myelodysplastic syndrome subtypes, del(5q), and cytopenias or anaemias). They probably reflect the same learned similarities and do not count as independent evidence.

The remaining top-ranked predictions are alopecia-related conditions (alopecia, diffuse alopecia areata, hypotrichosis simplex of the scalp, congenital hypotrichosis milia). For autoimmune hair loss, a speculative anti-inflammatory rationale exists, but minimal systemic absorption limits its relevance, and established therapies have much stronger evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 1728Y | Dipentum | Olsalazine | Capsule containing olsalazine sodium 250 mg | Valid |
| 8086N | Dipentum | Olsalazine | Tablet containing olsalazine sodium 500 mg | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the interaction screening. The 20 listed in the data compiled include the following.
  - **Major**: human immunoglobulin G (intravenous), human botulinum neurotoxin A/B immune globulin, cidofovir, iothalamic acid.
  - **Moderate (examples)**: NSAIDs (ketorolac, ibuprofen, celecoxib, diclofenac), azathioprine, cisplatin, clofarabine, and several nephrotoxic agents (acyclovir, amphotericin B, amikacin, bacitracin, capreomycin, colistimethate).
  - Many of these interactions involve potentially nephrotoxic drugs, so renal monitoring is worth considering with co-administration.
- **Haematological considerations**: 5-ASA class drugs carry haematological adverse-event warnings, which argues against benefit in bone marrow disorders. Please confirm the details in the TGA-approved Product Information (PI).

Label warnings and contraindications were not available. Please refer to the TGA-approved Product Information (PI) for these.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or publications, no mechanism of action data, and no plausible biological link between a locally acting colonic agent and myelodysplastic syndrome. The same applies to the other top-ranked predictions (alopecia-related conditions and anaemias).

**To proceed, the following is needed:**
- Mechanism of action data for olsalazine and a defensible mechanistic hypothesis for haematopoietic disease
- Preclinical or observational evidence supporting the proposed indication
- The approved indication and the safety sections (warnings and contraindications) from the TGA-approved PI
- Evidence of adequate systemic exposure at the target site, given the drug's local colonic action
- Review of the haematological safety signal for 5-ASA class drugs in patients with existing cytopenias

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Dipentum (olsalazine sodium) prescribing information, Viatris Specialty LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8512d0c6-db4e-4673-b3b4-28975c18413f) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

