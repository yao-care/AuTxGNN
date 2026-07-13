---
layout: default
title: Insulin Glulisine
parent: 僅模型預測 (L5)
nav_order: 266
evidence_level: L5
indication_count: 10
---

# Insulin Glulisine
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

# Insulin Glulisine: From Glycaemic Management to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin glulisine (Apidra®, Sanofi) is a rapid-acting insulin analogue with established global regulatory approvals (FDA 2004, EMA, TGA) for glycaemic management in adults and children aged 4 years and over.
The TxGNN model ranks **type 1 diabetes mellitus (T1DM)** as the top predicted indication with a score of **99.55%**, confirming strong pharmacological alignment with the drug's established clinical profile.
The automated evidence query returned **0 clinical trials and 0 publications** for this indication pair, and the ARTG query returned 0 registered products — both results require manual verification given the known extensive evidence base for this drug.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No ARTG registration data available (TGA approval referenced in mechanistic documentation) |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L1 (pre-assigned based on established global RCT evidence; automated query returned 0 results) |
| Australia Market Status | Not marketed (per ARTG query, 9 March 2026) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Insulin glulisine binds to the insulin receptor (INSR), stimulating glucose uptake in peripheral tissues, suppressing hepatic glycogenolysis, and inhibiting gluconeogenesis. Compared to regular human insulin, it is structurally engineered (Lys³→Glu, Asn²⁹→Lys substitutions) for faster subcutaneous absorption and shorter duration of action, making it well suited to prandial insulin replacement regimens.

Type 1 diabetes mellitus is characterised by autoimmune destruction of pancreatic beta cells, resulting in absolute endogenous insulin deficiency. Exogenous rapid-acting insulin analogues are the pharmacological cornerstone of T1DM management, providing physiological mimicry of postprandial insulin secretion. The TxGNN model's highest-ranked prediction for insulin glulisine is therefore a **validation of its established indication** rather than a novel repurposing discovery — a finding that itself lends confidence to the model's knowledge graph architecture.

It is important to note that the mechanistic rationale for this candidate explicitly references TGA approval for T1DM in adults and children (≥4 years), which is at odds with the ARTG query result of 0 registered products. Clinicians should verify current ARTG status directly before any prescribing decision.

---

## Clinical Trial Evidence

Currently no related clinical trials were retrieved in this specific automated query.

> **Important caveat:** This reflects a query result of 0 records, not an absence of published evidence. Insulin glulisine has an extensive Phase 3 RCT evidence base for T1DM in the global literature (the source of the pre-assigned L1 rating). Manual search of ClinicalTrials.gov and ANZCTR is strongly recommended to supplement this section before clinical use.

---

## Literature Evidence

Currently no related literature was retrieved in this specific automated query.

> **Important caveat:** As above, this reflects a query result of 0 records rather than absence of evidence. A manual PubMed search for "insulin glulisine type 1 diabetes" is expected to return a substantial body of peer-reviewed publications and should be conducted prior to clinical decision-making.

---

## Australia Market Information

No ARTG entries were found for Insulin glulisine in the current dataset (ARTG query date: 9 March 2026).

> **Data discrepancy:** The mechanistic documentation for this candidate references TGA approval of insulin glulisine for T1DM in adults and children (≥4 years). This directly conflicts with the ARTG query result of 0 registered products. This discrepancy must be resolved before any clinical or regulatory conclusions are drawn. Current ARTG status should be confirmed directly at [tga.gov.au/resources/artg](https://www.tga.gov.au/resources/artg).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for full safety information, including hypoglycaemia risk, injection-site reactions, and use in special populations.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN model's top prediction validates the well-established use of insulin glulisine in type 1 diabetes mellitus, consistent with known global regulatory approvals. However, significant data gaps exist across ARTG status, automated clinical trial and literature retrieval, and formal safety documentation — all of which must be resolved before this candidate can progress through a standard repurposing evaluation pathway.

**To proceed, the following is needed:**

- **ARTG verification:** Manually confirm current Australian registration status and retrieve registered product details from the TGA ARTG database — the automated query result of 0 products contradicts known TGA approval status referenced in this pack
- **Clinical trial evidence retrieval:** Manual search of ClinicalTrials.gov and ANZCTR for "insulin glulisine" + "type 1 diabetes" (automated pipeline returned 0 results despite an established evidence base)
- **Literature evidence retrieval:** Manual PubMed search to document the RCT evidence base underpinning the L1 rating
- **TGA Product Information (PI):** Download and parse the approved PI document for complete warning, contraindication, and drug interaction data (currently [Data Gap])
- **MOA data:** Retrieve formal mechanism of action detail from DrugBank API to support structured pharmacological analysis

---

### Note on Other TxGNN Predictions (Ranks 2–10)

The remaining nine predicted indications in this Evidence Pack are all rated **L5 (Hold)** or **L4 (Research Question)**, with no supporting clinical trial or literature evidence retrieved. Several require specific clinical attention:

- **Rank 7 — Pancreatic agenesis (L4):** Absolute insulin deficiency from beta cell agenesis represents a physiologically sound rationale for insulin replacement. This is best classified as an *extension of the established indication mechanism* rather than a novel repurposing. Individual case management is appropriate; no glulisine-specific case series were retrieved.

- **Rank 8 — Drug-induced localised lipodystrophy:** ⚠️ **Reverse causation flag.** Insulin injection is a well-documented *cause* of injection-site lipohypertrophy and lipoatrophy, not a treatment for it. The high TxGNN score almost certainly reflects an adverse-effect edge in the knowledge graph being misread as a therapeutic association. **This prediction should be classified as a false positive (reverse causation) and excluded from further development.**

- **Ranks 2–6 and 9–10:** Associations via autoimmune co-morbidity clustering (stiff person syndrome, autoimmune oophoritis), shared signalling pathway graph proximity (opsismodysplasia/SHIP2), or lipodystrophy category overlap. None carry a plausible direct therapeutic mechanism for insulin glulisine and should remain on Hold pending model refinement.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

