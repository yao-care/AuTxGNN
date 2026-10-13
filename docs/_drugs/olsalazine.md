---
layout: default
title: Olsalazine
parent: Model Prediction Only (L5)
nav_order: 525
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Olsalazine: From an Unspecified Original Indication to Myelodysplastic Syndrome

## One-Sentence Summary

Olsalazine is a dimer of 5-aminosalicylic acid (5-ASA) that is registered in Australia as an oral capsule (Dipentum), but the data compiled for this report do not state an approved indication.
The TxGNN model predicts it may be effective for **myelodysplastic syndrome**, with a very high model score, but there are **0 clinical trials** and **0 publications** supporting this prediction.
This is a model-only prediction with no clinical evidence behind it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the ARTG indication text is blank) |
| Predicted New Indication | Myelodysplastic syndrome |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Olsalazine is known to be a dimer of 5-ASA that colonic bacteria cleave into two active molecules. It acts locally in the gut, and systemic exposure to the active moiety is low.

No plausible link between a locally acting colonic anti-inflammatory agent and bone marrow or haematopoietic disease can be established from the data compiled. The high score is most likely a network-proximity effect within the knowledge graph, not true pharmacology. Several other top predictions are closely related conditions (myelodysplastic syndrome subtypes, del(5q), and cytopenias or anaemias). They probably reflect the same graph cluster and do not count as independent evidence.

The remaining top-ranked predictions are alopecia-related conditions (alopecia, diffuse alopecia areata, hypotrichosis simplex of the scalp, congenital hypotrichosis milia). For autoimmune hair loss, a speculative anti-inflammatory rationale exists, but minimal systemic absorption limits its relevance, and established therapies have much stronger evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1728Y | Dipentum | Capsule containing olsalazine sodium 250 mg (oral) | Not stated in the data compiled |

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

