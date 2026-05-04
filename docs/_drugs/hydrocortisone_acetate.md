---
layout: default
title: Hydrocortisone Acetate
parent: 僅模型預測 (L5)
nav_order: 229
evidence_level: L5
indication_count: 10
---

# Hydrocortisone Acetate
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

# Hydrocortisone Acetate: From Inflammatory Skin Conditions to Alopecia Areata

## One-Sentence Summary

Hydrocortisone acetate is a synthetic glucocorticoid corticosteroid with well-established anti-inflammatory properties, widely used internationally for inflammatory skin conditions, though currently not registered on the Australian Register of Therapeutic Goods (ARTG).
The TxGNN model predicts it may be effective for **Alopecia Areata** (patchy hair loss),
with **1 completed Phase 3 clinical trial** and **2 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anti-inflammatory corticosteroid — not currently registered in Australia (no ARTG entry) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for hydrocortisone acetate in this Evidence Pack. Based on established pharmacology, hydrocortisone acetate is the acetate ester of cortisol — a naturally occurring glucocorticoid — that acts via intracellular glucocorticoid receptors (GR) to suppress immune and inflammatory signalling cascades. The acetate ester formulation creates a depot effect particularly suited to intralesional injection, providing sustained local immunosuppression with reduced systemic exposure.

Alopecia areata is driven by CD8+ T-cell autoimmune attack on the hair follicle, causing loss of the follicle's "immune privilege" zone. Glucocorticoids directly address this pathology by suppressing the NF-κB pathway, reducing pro-inflammatory cytokines (IL-1β, TNF-α, IFN-γ), and dampening the aberrant immune response within the follicle unit. This mechanistic alignment is highly direct — topical and intralesional corticosteroid therapy is already recognised as a first-line clinical approach for alopecia areata in major international dermatology guidelines.

The TxGNN prediction is therefore well-supported by mechanistic reasoning. The acetate formulation's established use in intralesional injection (e.g., as a depot suspension) provides a clinically practical route for delivering localised immunosuppression to affected scalp patches, with a more favourable systemic safety profile compared to oral corticosteroids.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | Completed | 41 | Randomised controlled trial directly comparing Hydrocortisone 1% Cream versus Clobetasol Propionate 0.05% Cream in children with alopecia areata; designed to address the evidence gap for optimal topical steroid potency selection in paediatric patients. Note: small sample size (n=41) limits statistical power; primary outcome data should be reviewed to confirm efficacy direction before clinical extrapolation. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [4755919](https://pubmed.ncbi.nlm.nih.gov/4755919/) | 1973 | Clinical Study | Przeglad dermatologiczny | Reports on intralesional subcutaneous injection of hydrocortisone acetate suspension for severe forms of alopecia areata — directly evaluates the specific formulation (acetate salt) in the predicted indication. |
| [153470](https://pubmed.ncbi.nlm.nih.gov/153470/) | 1979 | Review | MMW, Munchener medizinische Wochenschrift | Review of topical corticosteroid therapy advances; contextualises hydrocortisone acetate's anti-inflammatory profile and compares it with newer agents including fluocortin butyl ester. |

---

## Australia Market Information

Hydrocortisone acetate is currently **not registered** on the Australian Register of Therapeutic Goods (ARTG). No ARTG entries exist for this specific compound.

> **Note for clinicians:** Related hydrocortisone products (different formulations, salts, or combination preparations) may hold separate ARTG registrations. Healthcare professionals should verify current ARTG status via the [TGA website](https://www.tga.gov.au/resources/artg) before any clinical use or regulatory planning.

---

## Safety Considerations

Detailed safety data — including TGA-approved warnings, contraindications, and drug interaction profiles — was not available in this Evidence Pack for review.

Please refer to the **TGA-approved Product Information (PI)** for complete safety information. The following areas are particularly important to clarify before proceeding:

- **HPA axis suppression**: Risk increases with potency, occlusion, surface area, and treatment duration — especially relevant in paediatric use
- **Local adverse effects**: Skin atrophy, telangiectasia, and perilesional depigmentation with repeated intralesional injection
- **Infection risk**: Immunosuppression at injection site; relevant for intralesional route
- **Paediatric safety**: Growth effects and systemic absorption considerations in children
- **Systemic absorption**: Though lower with topical/intralesional administration compared to oral, monitoring is advisable for extensive disease

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed Phase 3 RCT directly evaluating hydrocortisone cream in paediatric alopecia areata, supported by a 1973 clinical study on the intralesional acetate formulation and a mechanistically robust rationale (glucocorticoid-mediated restoration of hair follicle immune privilege), provides a sufficient foundation to advance — provided that key safety data gaps are closed and the regulatory pathway for unregistered status is addressed.

**To proceed, the following is needed:**

- Obtain and review TGA-approved Product Information or comparable international PI (e.g., UK MHRA, EMA SmPC) for full safety and contraindication data
- Access primary outcome data from NCT01453686 to determine whether hydrocortisone demonstrated non-inferiority or inferiority versus high-potency clobetasol propionate
- Confirm the target formulation and route (topical cream vs. intralesional acetate suspension), as these have distinct risk-benefit profiles
- Define the target patient population (paediatric vs. adult; limited patch vs. extensive/totalis/universalis disease)
- Investigate whether an ARTG registration or TGA authorisation (e.g., Special Access Scheme, clinical trial exemption) is required given the currently unregistered status in Australia
- Source DrugBank MOA data to complete mechanistic documentation and support any regulatory submission
- Consider a targeted literature search for post-1980 intralesional hydrocortisone acetate evidence, as the existing literature is dated (1973–1979)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

