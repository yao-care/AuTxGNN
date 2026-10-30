---
layout: default
title: Desmopressin
parent: Model Prediction Only (L5)
nav_order: 208
evidence_level: L5
indication_count: 6
monitor_inn: "Desmopressin"
predicted_indications: ["congenital prothrombin deficiency", "inherited thrombophilia", "Glanzmann thrombasthenia", "primary release disorder of platelets", "Scott syndrome", "flood factor deficiency"]
last_modified_at: 2026-10-30
description: "Desmopressin: predicted new indication congenital prothrombin deficiency (evidence level L5). Approved use: Not recorded in the local data"
---

# Desmopressin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Desmopressin: synthetic vasopressin analogue (V2 receptor agonist) → congenital prothrombin deficiency (congenital prothrombin deficiency)
{: .text-alpha }

## One-Sentence Summary

Desmopressin is a synthetic analogue of vasopressin that is marketed in Australia as a nasal spray.
The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**, but there are **0 clinical trials** and only **1 publication** (a general 1993 review of congenital bleeding disorders) linked to this prediction, and that publication does not study desmopressin in this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | congenital prothrombin deficiency |
| TxGNN Prediction Score | 0.9970 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Desmopressin is generally understood to raise plasma von Willebrand factor (VWF) and factor VIII by promoting their release from endothelial cells, and this is the basis of its use in some bleeding disorders.

Prothrombin (factor II) is not a known target of this release mechanism, so no plausible direct mechanism links desmopressin to congenital prothrombin deficiency. The single retrieved paper is a generic review of treatment options for inherited bleeding disorders and does not support desmopressin for this condition. The high TxGNN score is probably driven by the model's proximity to other bleeding disorders rather than by a specific biological link.

This prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7684674](https://pubmed.ncbi.nlm.nih.gov/7684674/) | 1993 | Review | Drugs | General review of treatment options for common inherited bleeding disorders (haemophilia A, von Willebrand disease); does not address desmopressin in prothrombin deficiency |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12458Q | Desmopressin Nasal Spray USP (Apotex) | Nasal spray (pump pack), desmopressin acetate 10 micrograms per actuation, 50 actuations, 5 mL | Not recorded in the local data |

## Safety Considerations

**Drug Interactions**: The interaction screen returned 100 records. Those shown in the data include:
- **Major**: hydrocortisone, triamcinolone, dexamethasone, beclomethasone dipropionate, betamethasone, budesonide, prednisolone, prednisone
- **Moderate**: epinephrine, loperamide, morphine (including liposomal), opium, chlorpropamide
- **Minor**: acetylsalicylic acid

Other safety information (warnings and contraindications) is not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for safety information. Desmopressin is a pro-haemostatic agent and is known to carry a risk of hyponatraemia and, rarely, arterial thrombotic events.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or publication studies desmopressin in congenital prothrombin deficiency, and there is no plausible mechanistic link, because prothrombin is not released by the pathway through which desmopressin acts. The evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Mechanistic data showing a plausible route by which desmopressin could affect prothrombin levels or function
- Any direct preclinical or clinical study of desmopressin in congenital prothrombin deficiency
- Product Information (PI) warnings and contraindications for the Australian-registered product
- Review of safety, including hyponatraemia and thrombotic risk, before any further assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

