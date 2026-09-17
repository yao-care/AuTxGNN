---
layout: default
title: Tirofiban
parent: Model Prediction Only (L5)
nav_order: 679
evidence_level: L5
indication_count: 10
---

# Tirofiban
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

Using the evidence pack as provided — no skill matches this content-generation task, proceeding directly.

# Tirofiban: From Antiplatelet Therapy (ACS/PCI) to Primary Release Disorder of Platelets

## One-Sentence Summary

> Tirofiban is a glycoprotein IIb/IIIa (GPIIb/IIIa) receptor antagonist established as an antiplatelet agent in acute coronary syndrome (ACS) and percutaneous coronary intervention (PCI) settings.
> The TxGNN model predicts it may be effective for **primary release disorder of platelets**,
> but the **2 clinical trials** and **3 publications** identified do not actually support this indication — they instead describe tirofiban's known antiplatelet effects and an adverse thrombocytopenia signal, and the underlying mechanism appears to run in the **opposite direction** to what this indication would require.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Australian regulatory data; established use (per evidence-pack literature) is antiplatelet therapy in ACS/PCI |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 96.27% |
| Evidence Level | L4 (per model scoring — caveat: evidence is mechanistically contradictory, not supportive) |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Tirofiban is a non-peptide GPIIb/IIIa receptor antagonist. It works by blocking fibrinogen and von Willebrand factor from binding to the activated GPIIb/IIIa receptor complex on platelets, which **inhibits** platelet aggregation. A formal DrugBank MOA record was not available for this review, but this mechanism is consistently described across the literature captured in this evidence pack (e.g. the TOPSTAR trial, PMID 12204495).

The concern with this prediction is directional. "Primary release disorder of platelets" is a condition in which platelets have an intrinsic **deficiency** in granule release and activation — patients with this disorder already have impaired platelet function and are prone to bleeding. Tirofiban further **suppresses** platelet activity via GPIIb/IIIa blockade. Giving an antiplatelet agent to a patient with a platelet release deficiency would be expected to worsen bleeding risk rather than provide therapeutic benefit.

Neither identified trial actually studies tirofiban for this disease: NCT03691727 investigates tirofiban for platelet-activity suppression in aneurysmal subarachnoid haemorrhage, and NCT01863134 studies eptifibatide (a related but different GPIIb/IIIa agent) in NSTE-ACS. The literature is similarly off-target — PMID 16287613 documents tirofiban-**induced** thrombocytopenia (an adverse effect), and the other two papers concern GPIIb/IIIa inhibition in ACS/PCI settings unrelated to platelet release disorders. This pattern is consistent with a disease-label mismatch in the prediction model rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03691727](https://clinicaltrials.gov/study/NCT03691727) | Phase 1/2 | Completed | 30 | Randomised, double-blind study of tirofiban (Aggrastat) added to standard care for platelet-activity suppression in aneurysmal subarachnoid haemorrhage — **not** a study of primary platelet release disorder |
| [NCT01863134](https://clinicaltrials.gov/study/NCT01863134) | Phase 4 | Completed | 140 | Studied eptifibatide (a different GPIIb/IIIa antagonist, not tirofiban) in high-risk NSTE-ACS patients requiring urgent CABG — indirect relevance only |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12204495](https://pubmed.ncbi.nlm.nih.gov/12204495/) | 2002 | RCT | J Am Coll Cardiol | TOPSTAR trial: additional GPIIb/IIIa inhibition (tirofiban) reduces troponin release after elective PCI — an ACS/PCI antiplatelet study, not related to platelet release disorders |
| [16682384](https://pubmed.ncbi.nlm.nih.gov/16682384/) | 2006 | RCT | European Heart Journal | ELISA-2 trial: dual vs. triple antiplatelet therapy in NSTE-ACS — again an ACS antiplatelet efficacy study |
| [16287613](https://pubmed.ncbi.nlm.nih.gov/16287613/) | 2005 | Case series | Platelets | Describes tirofiban-**induced thrombocytopenia** via drug-dependent antibodies causing platelet activation — an adverse-effect report, not evidence of benefit |

---

## Australia Market Information

No ARTG entries were found for tirofiban. The evidence pack records the drug as **not currently marketed** in Australia (0 licences on file).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Detailed TFDA/TGA warnings, contraindications, and drug interaction data were not available in this evidence pack (flagged as a **Blocking** data gap — see below).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate carries a Blocking data gap (no PI warnings/contraindications available) and the top-ranked predicted indication is mechanistically contradictory — an antiplatelet agent proposed for a platelet-deficiency disorder — with no clinical trial or literature evidence actually supporting therapeutic use in this disease. Combined with tirofiban's "Not Marketed" status in Australia, this does not meet the minimum bar to proceed past initial screening.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications) — currently the Blocking gap (DG001)
- Formal DrugBank/verified mechanism-of-action data (DG002)
- Re-verification of the TxGNN disease-label mapping for "primary release disorder of platelets," which is very likely mislabelled given the directional mismatch identified above
- If continuing to explore tirofiban's repurposing potential, note that rank 8 in this evidence pack (thromboangiitis obliterans/Buerger disease) was flagged **"Research Question"** rather than Hold — antiplatelet therapy has plausible mechanistic rationale there, though currently with no direct trial or literature support either
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

