---
layout: default
title: Avatrombopag
parent: 僅模型預測 (L5)
nav_order: 68
evidence_level: L5
indication_count: 10
---

# Avatrombopag
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

# Avatrombopag: From Thrombocytopenia to Marcothrombocytopenia with Mitral Valve Insufficiency

## One-Sentence Summary

Avatrombopag (Doptelet) is an oral thrombopoietin receptor agonist (TPO-RA) approved internationally for thrombocytopenia in adults with chronic liver disease undergoing procedures, and for chronic immune thrombocytopenia (ITP).
The TxGNN model predicts it may be effective for **Marcothrombocytopenia with Mitral Valve Insufficiency**, a rare syndrome combining giant-platelet thrombocytopenia with structural cardiac valve disease.
Currently, **no clinical trials** and **no publications** specifically supporting this combination have been identified, meaning this prediction rests entirely on model inference.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Thrombocytopenia associated with chronic liver disease (pre-procedural) and chronic ITP |
| Predicted New Indication | Marcothrombocytopenia with Mitral Valve Insufficiency |
| TxGNN Prediction Score | 99.995% (global rank #147) |
| Evidence Level | L5 — Model prediction only; no supporting clinical or preclinical studies identified |
| Australia Market Status | Not Marketed in Australia |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Avatrombopag is a small-molecule TPO receptor agonist (TPO-RA) that binds to the transmembrane domain of the thrombopoietin receptor (c-MPL) and stimulates megakaryocyte proliferation and differentiation in the bone marrow, ultimately increasing platelet production. This mechanism is pharmacologically distinct from other TPO-RAs such as eltrombopag (which binds the extracellular domain) and romiplostim (a peptibody).

The core feature of Marcothrombocytopenia with Mitral Valve Insufficiency is giant-platelet thrombocytopenia (macrothrombocytopenia), which involves both reduced platelet counts and abnormally enlarged platelets — characteristics that overlap mechanistically with the conditions Avatrombopag is already approved for. Since Avatrombopag stimulates platelet production via the TPO/c-MPL axis, it is plausible that it could partially address the quantitative platelet deficit component of this syndrome. The TxGNN knowledge graph likely connects this indication through the shared thrombocytopenia node and the TPO pathway.

However, a critical limitation must be highlighted: Marcothrombocytopenia with Mitral Valve Insufficiency (as seen in MYH9-related disorders or similar genetic syndromes) involves underlying structural and functional platelet defects driven by cytoskeletal gene mutations. Increasing platelet numbers via TPO-RA stimulation may not correct the intrinsic functional abnormalities of these giant platelets. Furthermore, the concurrent mitral valve insufficiency component is unrelated to platelet biology and would require independent management. The mechanistic relevance of Avatrombopag to this syndrome is therefore assessed as **moderate** — plausible for the quantitative platelet component, uncertain for functional correction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the combination of Avatrombopag and Marcothrombocytopenia with Mitral Valve Insufficiency.

---

## Literature Evidence

Currently no related literature available for the combination of Avatrombopag and Marcothrombocytopenia with Mitral Valve Insufficiency.

---

## Australia Market Information

Avatrombopag is **not currently listed on the Australian Register of Therapeutic Goods (ARTG)**. As of the data cut-off date (5 April 2026), no ARTG entries have been identified for this drug.

> **Note for clinicians:** Avatrombopag (brand name Doptelet®) is approved by the US FDA (2018) and the EMA for CLD-related thrombocytopenia and ITP. Australian clinicians wishing to access this medicine would need to apply via the TGA Special Access Scheme (SAS) or Authorised Prescriber pathway.

---

## Safety Considerations

Please refer to the TGA Special Access Scheme documentation and the internationally approved Product Information (PI) for comprehensive safety information, as no Australia-specific TGA Product Information is available for this unlisted medicine.

For reference, key safety considerations known from international approvals include:
- **Thrombotic/thromboembolic risk**: As with all TPO-RAs, excessive platelet stimulation may increase thrombotic risk; platelet count monitoring is required.
- **Portal vein thrombosis**: Of particular relevance in the CLD-related thrombocytopenia indication.
- **Drug interactions**: Avatrombopag is a substrate of CYP2C9 and CYP3A; interactions with inducers/inhibitors may alter drug exposure.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported by a plausible mechanistic hypothesis (TPO-RA activity addressing the quantitative platelet deficit in macrothrombocytopenia) but is currently at Evidence Level L5 — model inference only, with zero clinical trials and zero publications directly supporting this specific indication. Additionally, Avatrombopag is not registered in Australia, meaning both regulatory and clinical evidence gaps must be addressed before any repurposing pathway can be meaningfully evaluated.

**To proceed, the following is needed:**

- **Mechanism clarification**: Confirm whether Avatrombopag improves platelet counts in MYH9-related or other genetic macrothrombocytopenias — literature review of TPO-RA use in hereditary thrombocytopenias broadly would be a useful starting point.
- **Genetic subtype mapping**: Identify the specific genetic aetiology of the target patient population (e.g., MYH9, FLNA, or other loci), as TPO-RA responsiveness varies significantly by subtype.
- **Clinical case series or registry data**: Search for case reports or compassionate use data on TPO-RA (any class) use in macrothrombocytopenia with structural cardiac defects.
- **Safety data retrieval**: Obtain the full international PI for Avatrombopag (Doptelet) to assess contraindications and warnings relevant to this population.
- **TGA regulatory pathway assessment**: If evidence from the above steps is encouraging, evaluate whether a TGA Special Access Scheme Category B application or an Authorised Prescriber arrangement is appropriate for compassionate use in a named patient.
- **Cardiac specialist input**: Assess whether the mitral valve insufficiency component of this syndrome introduces additional thrombotic risk that would contraindicate a TPO-RA approach.

---

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. Clinicians should consult current TGA-approved product information and exercise independent professional judgement.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

