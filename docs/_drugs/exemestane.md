---
layout: default
title: Exemestane
parent: 僅模型預測 (L5)
nav_order: 212
evidence_level: L5
indication_count: 10
---

# Exemestane
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

# Exemestane: From Breast Cancer to Antithrombin Deficiency Type 2

## One-Sentence Summary

Exemestane is a steroidal, irreversible aromatase inhibitor established as a standard endocrine treatment for hormone receptor-positive breast cancer in postmenopausal women.
The TxGNN model predicts it may be effective for **Antithrombin Deficiency Type 2**, with a prediction score of **99.83%**.
Currently, **no clinical trials** and **no direct literature** support this repurposing direction — this remains a model prediction only (Evidence Level L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hormone receptor-positive breast cancer (postmenopausal women) |
| Predicted New Indication | Antithrombin Deficiency Type 2 |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 — model prediction only, no supporting studies |
| Australia Market Status | Not marketed (no ARTG entries identified in current dataset) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

> **Data Note:** The absence of ARTG entries may reflect a data collection gap. Healthcare professionals should independently verify current ARTG registration status via the [TGA website](https://www.tga.gov.au/resources/artg). Exemestane (Aromasin) is a well-established agent and may have current ARTG listings.

---

## Why Is This Prediction Reasonable?

The mechanistic rationale centres on oestrogen's known pro-coagulant effects: oestrogen upregulates several coagulation factors — including Factor VII, Factor X, and fibrinogen — and is believed to suppress antithrombin III synthesis. In principle, Exemestane's profound suppression of systemic oestrogen via irreversible aromatase inhibition could theoretically alleviate oestrogen-induced depletion of antithrombin, potentially benefiting patients with reduced antithrombin activity.

However, this mechanistic link is substantially weakened on closer examination. Antithrombin Deficiency Type 2 is characterised by a structural, functionally impaired antithrombin protein caused by specific point mutations — it is not primarily a condition of oestrogen-driven regulatory suppression. Exemestane has no capacity to restore protein structural integrity or correct a genetic defect at the protein level. Furthermore, clinical experience with aromatase inhibitors in breast cancer patients has not demonstrated measurable improvements in antithrombin levels, and some studies have reported venous thromboembolism (VTE) events in aromatase inhibitor users — suggesting the net effect on the coagulation system may not be protective.

In summary, the TxGNN score almost certainly reflects a shared knowledge-graph node connecting oestrogen modulation with the coagulation cascade, rather than a pharmacologically actionable connection specific to this rare genetic disorder. The mechanistic link is weak and potentially counterproductive in clinical application.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Exemestane in Antithrombin Deficiency Type 2.

---

## Literature Evidence

Currently no related literature available for Exemestane in Antithrombin Deficiency Type 2.

---

## Australia Market Information

No ARTG entries were identified in the current dataset for Exemestane.

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|-------------|--------------|-------------|---------------------|
| — | No entries found | — | — |

Healthcare professionals should verify current registration status directly via the [ARTG Public Summary Search](https://www.tga.gov.au/resources/artg).

---

## Cytotoxicity

Exemestane is an antineoplastic agent used for breast cancer treatment, warranting inclusion of this section. It is classified as a targeted hormonal therapy rather than a conventional cytotoxic agent.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted hormonal therapy — Steroidal Aromatase Inhibitor (Type I, irreversible); not a conventional cytotoxic |
| Myelosuppression Risk | Low — aromatase inhibitors do not cause clinically significant bone marrow suppression |
| Emetogenicity Classification | Low |
| Monitoring Items | Bone mineral density (DXA scan), liver function tests, lipid profile, musculoskeletal symptoms (arthralgia, myalgia) |
| Handling Protection | Standard pharmaceutical handling practices apply; dedicated cytotoxic drug handling precautions are not required |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for complete safety information, including warnings, contraindications, and drug interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model assigns a high prediction score of 99.83%, the mechanistic basis for Exemestane in Antithrombin Deficiency Type 2 is fundamentally misaligned — this is a structural protein mutation disorder, not an oestrogen-regulated deficiency, and no clinical or preclinical evidence supports this repurposing direction.

**To proceed, the following would be needed:**

- **MOA data:** Retrieve full DrugBank mechanism of action and pharmacodynamic profile for Exemestane to enable rigorous mechanistic analysis
- **Regulatory data:** Confirm current ARTG registration status and obtain the TGA-approved Product Information for safety profiling
- **Preclinical evidence:** Demonstrate, in a disease-relevant model, that aromatase inhibition meaningfully alters antithrombin III levels or functional activity — not merely total plasma concentrations
- **Patient subpopulation identification:** Define whether any subgroup exists (e.g., postmenopausal women with concurrent oestrogen-excess-driven acquired antithrombin depletion) where this mechanism could be plausibly operative
- **Alternative indication review:** The TxGNN top-10 list includes **Breast Fibrocystic Disease** (Rank 10, recommendation: *Research Question*) as a more mechanistically coherent target for Exemestane — this may be a more productive avenue for exploratory investigation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

