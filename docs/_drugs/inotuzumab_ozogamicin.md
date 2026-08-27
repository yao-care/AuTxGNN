---
layout: default
title: Inotuzumab Ozogamicin
parent: 僅模型預測 (L5)
nav_order: 351
evidence_level: L5
indication_count: 10
---

# Inotuzumab Ozogamicin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Inotuzumab Ozogamicin: From B-cell Precursor Acute Lymphoblastic Leukaemia to Drug-Induced Osteoporosis

## One-Sentence Summary

Inotuzumab ozogamicin is a CD22-targeted antibody-drug conjugate (ADC), clinically established for relapsed/refractory CD22-positive B-cell precursor acute lymphoblastic leukaemia (ALL). The TxGNN model's top-ranked prediction for this drug is **drug-induced osteoporosis**, but this signal is supported by **0 clinical trials** and **0 publications**, and the evidence pack itself flags it as a likely false-positive artefact rather than a genuine repurposing candidate.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in TGA/ARTG data (drug not marketed in Australia). Per supporting evidence text, internationally used for CD22-positive B-cell precursor acute lymphoblastic leukaemia |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 98.24% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on the information that is available, inotuzumab ozogamicin is an ADC combining a CD22-targeting antibody with the cytotoxic payload calicheamicin, and it is internationally used for CD22-positive B-cell precursor ALL — a mechanism entirely distinct from bone metabolism.

The predicted indication, drug-induced osteoporosis, has no established biological link to the CD22/calicheamicin pathway. There is no known interaction between CD22 signalling and bone remodelling regulators such as RANKL/OPG. The evidence pack's own rationale assessment concludes this is most likely a byproduct of the drug's known myelosuppressive toxicity profile being confounded with a treatable indication — a common failure mode for ADC-class drugs in knowledge-graph predictions — rather than a genuine therapeutic mechanism.

In short: this is a high TxGNN score without any corroborating mechanistic, preclinical, trial, or literature support, and the supplied rationale explicitly characterises it as prediction noise rather than a treatment hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

Inotuzumab ozogamicin has no ARTG entries and is not currently marketed in Australia (0 registered products).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (antibody-drug conjugate; calicheamicin cytotoxic payload) |
| Myelosuppression Risk | High — known to induce thrombocytopenia and neutropenia; also associated with hepatotoxicity/veno-occlusive disease (VOD/SOS) |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Full blood count (FBC) with differential, liver function tests, renal function |
| Handling Protection | Cytotoxic drug handling precautions required, consistent with ADC/cytotoxic conjugate class |

## Safety Considerations

Key warnings, contraindications, and drug interaction data are not available in this evidence pack (TGA/PI warning data is flagged as a Blocking-severity data gap). As the drug is not currently marketed in Australia, no TGA-approved Product Information exists — safety assessment should rely on the overseas regulatory label pending Australian registration.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication carries no clinical trial or literature support (Evidence Level L5), and the evidence pack's own mechanistic assessment identifies it as a likely false-positive signal rather than a plausible biological link. Combined with the drug's unregistered status in Australia and missing safety/MOA data, there is no basis to advance this candidate.

**To proceed, the following is needed:**
- Confirmed mechanism of action data (DrugBank or primary literature)
- TGA/PI-equivalent safety and warning data (currently a blocking gap)
- Independent biological plausibility review of any bone-metabolism pathway link before further evidence collection is warranted
- If pursued, preclinical or mechanistic studies to establish a genuine rationale, since none currently exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

