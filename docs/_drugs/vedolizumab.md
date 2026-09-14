---
layout: default
title: Vedolizumab
parent: 僅模型預測 (L5)
nav_order: 717
evidence_level: L5
indication_count: 10
---

# Vedolizumab
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

# Vedolizumab: From Inflammatory Bowel Disease to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Vedolizumab is a gut-selective anti-integrin (α4β7) monoclonal antibody used internationally for inflammatory bowel disease (Crohn's disease and ulcerative colitis); it is not currently marketed in Australia. The TxGNN model predicts a possible signal for **Severe Nonproliferative Diabetic Retinopathy**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-score-only signal with no clinical or mechanistic corroboration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Inflammatory bowel disease (Crohn's disease, ulcerative colitis) — internationally established use; no ARTG licence data available for this drug |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 94.51% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on known pharmacology referenced elsewhere in the evidence pack, vedolizumab is a gut-selective α4β7 integrin antagonist — it blocks lymphocyte trafficking specifically to gastrointestinal mucosal tissue via MAdCAM-1 binding. This mechanism has no established relationship with retinal vascular pathology or diabetic microvascular disease processes.

The repurposing rationale provided for this candidate states explicitly: *"No mechanistic link: vedolizumab is a gut-selective antibody; there is no biological hypothesis connecting it to retinal neovascularisation or diabetic retinopathy pathways — this is a TxGNN algorithmic prediction score only, with no clinical or literature support."*

There is no plausible biological bridge between the original indication (IBD) and the predicted indication (diabetic retinopathy), and no supporting evidence of any kind (trials or literature) was identified. This candidate should be treated as a low-confidence algorithmic signal requiring independent mechanistic validation before any further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Vedolizumab is **not currently marketed in Australia** — 0 ARTG entries are registered for this drug, so no licence/dosage-form/indication details are available for comparison.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Note that a **Blocking**-severity data gap (DG001) was identified: TGA-equivalent product warnings and contraindications have not yet been retrieved for this drug, meaning this candidate cannot currently pass the S1 safety pre-screen stage.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (severe nonproliferative diabetic retinopathy) is supported only by a TxGNN model score, with no mechanistic rationale, no clinical trials, and no literature evidence (Evidence Level L5). The drug is also not currently marketed in Australia, and a blocking safety data gap prevents any preliminary safety assessment.

It is also worth noting that other candidate indications in this evidence pack do not offer stronger support: the second-ranked candidate, dermatitis, has 3 clinical trials (none directly testing vedolizumab for dermatitis; one withdrawn, one unrelated to dermatitis, one testing a different agent) and 20 publications — but the literature is predominantly **case reports of vedolizumab-induced dermatitis as an adverse drug reaction** (atopic, psoriasiform, granulomatous, acneiform eruptions, hidradenitis suppurativa), which argues against rather than for a therapeutic repurposing use. This reinforces an overall Hold posture across the evaluated candidates for this drug.

**To proceed, the following is needed:**
- TGA/PI-equivalent safety data (warnings, contraindications) to close data gap DG001
- Confirmed mechanism of action data (DrugBank) to close data gap DG002
- Independent preclinical/mechanistic rationale connecting α4β7 integrin blockade to retinal microvascular disease, before any further clinical evidence review
- If pursuing the dermatitis signal instead, a formal adverse-event vs. therapeutic-effect reconciliation, since current literature direction is inverse to the repurposing hypothesis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

