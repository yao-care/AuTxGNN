---
layout: default
title: Trastuzumab Deruxtecan
parent: Model Prediction Only (L5)
nav_order: 697
evidence_level: L5
indication_count: 10
---

# Trastuzumab Deruxtecan
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

Using no additional skill — this is a direct content-generation task fully specified by the report template already provided in context, so I'll produce the report directly from the evidence pack.

---

# Trastuzumab Deruxtecan: Original Indication Not Recorded → Predicted Link to Drug-Induced Osteoporosis

## One-Sentence Summary

The evidence pack does not record Trastuzumab deruxtecan's original approved indication (data gap), so no baseline comparison indication is available for this drug. The TxGNN model predicts a possible link to **Drug-Induced Osteoporosis**, but this is supported by **zero clinical trials** and **zero publications**, and the evidence pack's own mechanistic review explicitly finds no biological rationale for the link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the evidence pack (original_indications empty; MOA marked as data gap) |
| Predicted New Indication | Drug-Induced Osteoporosis |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for trastuzumab deruxtecan is not available in this evidence pack (data gap). However, the evidence pack's mechanistic rationale identifies it as an antibody-drug conjugate (ADC) combining a HER2-targeted antibody with a topoisomerase I inhibitor payload (DXd), consistent with its known class as an oncology ADC.

The predicted indication — drug-induced osteoporosis — relates to bone remodelling pathways (RANKL/OPG signalling, osteoclast activity). The evidence pack explicitly states there is no known intersection between the HER2/topoisomerase I cytotoxic mechanism and bone metabolism regulation. No supporting clinical trials or literature were identified for this pairing, and the reviewer's own assessment describes this as "a high TxGNN score without mechanistic grounding."

It is also worth noting that across this drug's full top-10 predicted indication list, several entries (severe nonproliferative diabetic retinopathy, diabetic retinopathy, diabetic cataract, bronchitis) are flagged in the evidence pack as running in the **opposite direction** to therapeutic benefit — i.e., these are areas where the drug is associated with known adverse effects (ocular toxicity, interstitial lung disease/pneumonitis) rather than potential efficacy. This pattern suggests the current prediction set for this drug should be treated with caution rather than as a genuine repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

This drug currently has no ARTG (Australian Register of Therapeutic Goods) entries recorded in this evidence pack (`total_licenses = 0`, market status: Not marketed). No product listing information is available for extraction.

## Cytotoxicity

Trastuzumab deruxtecan is an antineoplastic antibody-drug conjugate (ADC) with a cytotoxic payload, so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — HER2-directed antibody-drug conjugate incorporating a topoisomerase I inhibitor payload (DXd) |
| Myelosuppression Risk | Not detailed in the evidence pack; please refer to the Product Information (PI) for haematological toxicity data |
| Emetogenicity Classification | Not detailed in the evidence pack; please refer to the PI |
| Monitoring Items | Based on class risks flagged within the evidence pack's rationale text: pulmonary function/chest imaging (interstitial lung disease is a recognised boxed-warning risk for this ADC class), ophthalmic review (ocular/corneal toxicity noted in evidence rationale), renal function (a case report within the evidence pack describes deruxtecan-induced Fanconi syndrome), FBC, LFT |
| Handling Protection | As a cytotoxic antibody-drug conjugate, standard cytotoxic drug handling precautions apply |

## Safety Considerations

Formal safety data (key warnings, contraindications, drug interactions) were not available in this evidence pack — this is recorded as a Blocking data gap (DG001: TFDA/TGA Product Information not yet obtained). Please refer to the TGA-approved Product Information (PI) for complete and authoritative safety information.

Note: within the mechanistic rationale text (not the formal safety fields), several known class-level risks for this ADC were referenced — interstitial lung disease/pneumonitis, ocular toxicity, and a reported case of deruxtecan-induced Fanconi syndrome. These have not been formally verified against the PI in this pack and should not be relied upon in place of the official document.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a pure model-generated prediction (L5, decision stage S0) with zero supporting clinical trials or literature, and the evidence pack's own mechanistic review finds no plausible biological link between the drug's HER2/topoisomerase I ADC mechanism and drug-induced osteoporosis. Several other top-ranked predictions for this drug are flagged as running in the opposite direction to therapeutic benefit, reinforcing that this candidate set should not proceed without independent verification.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications, drug interactions) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action from DrugBank — currently a High-severity data gap (DG002)
- Confirmation of original approved indication(s) and ARTG registration status for this drug in Australia
- Any preclinical or mechanistic literature specifically linking HER2/topoisomerase I inhibition to bone metabolism, should repurposing interest continue
- Given the pattern across all 10 ranked predictions (all L5/Hold, several with contradictory safety signals), recommend deprioritising this candidate pending a materially stronger signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

