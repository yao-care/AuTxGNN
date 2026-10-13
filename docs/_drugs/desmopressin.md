---
layout: default
title: Desmopressin
parent: Model Prediction Only (L5)
nav_order: 208
evidence_level: L5
indication_count: 10
---

# Desmopressin
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

# Desmopressin: From Von Willebrand Disease to Congenital Prothrombin Deficiency

## One-Sentence Summary

Desmopressin is a synthetic vasopressin analogue, originally used for von Willebrand disease, haemophilia A and nocturnal enuresis.
The TxGNN model's top-ranked prediction is **congenital prothrombin deficiency**, but it is supported by **0 clinical trials** and only **1 general review** (1993), which does not address desmopressin for this condition.
This prediction should be treated as a model artefact rather than a credible repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hereditary von Willebrand disease, haemophilia A (including symptomatic female carriers) and nocturnal enuresis (from the knowledge graph; the ARTG entry has no indication text) |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, desmopressin raises plasma von Willebrand factor (VWF) and factor VIII by releasing them from endothelial cells, and enhances platelet adhesion. This underpins its use in von Willebrand disease and mild haemophilia A.

Prothrombin (factor II) is not a known desmopressin release target, so there is no plausible direct mechanism for congenital prothrombin deficiency. The high TxGNN score most likely reflects network proximity to other inherited bleeding disorders rather than a true pharmacological link.

**Other predictions in the top 10 are more informative:**
- **Primary release disorder of platelets** (Evidence L3): Desmopressin shortens bleeding time in platelet function disorders. Support comes from a 2023 review and a paediatric cohort in aspirin-like defect, with no registered trials. This is the most credible candidate.
- **Glanzmann thrombasthenia** (L4): Desmopressin may shorten bleeding time, but it cannot correct the aggregation defect. Case reports describe unsuccessful use, and standard care relies on platelet transfusion, rFVIIa and antifibrinolytics.
- **Bleeding diathesis due to a collagen receptor defect** (L4): The rationale is indirect (increased VWF may partially support adhesion), with no direct evidence.
- **Thrombotic thrombocytopenic purpura (TTP), inherited thrombophilia, pseudo-von Willebrand disease:** These are **safety signals, not opportunities**. Desmopressin releases VWF and may worsen TTP, platelet-type VWD and thrombotic states. Case reports describe TTP worsening and a Moschcowitz-like syndrome after desmopressin.
- **"Flood factor deficiency"** appears to be a data-mapping artefact needing curation. **Scott syndrome** and **hereditary thrombocytosis with transverse limb defect** have no plausible mechanistic link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for congenital prothrombin deficiency, and none for any of the top 10 predicted indications.

---

## Literature Evidence

Only one publication was retrieved for the top prediction:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7684674](https://pubmed.ncbi.nlm.nih.gov/7684674/) | 1993 | Review | Drugs | General review of treatment options in congenital bleeding disorders; does not support desmopressin for prothrombin deficiency |

**Selected literature for other predictions (for context):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36656570](https://pubmed.ncbi.nlm.nih.gov/36656570/) | 2023 | Review | Eur J Haematol | Desmopressin as a haemostatic and blood-sparing agent; effective in mild haemophilia A, certain VWD subtypes, uraemic and liver-disease bleeding. Risks include hyponatraemia and rare arterial thrombosis |
| [21509710](https://pubmed.ncbi.nlm.nih.gov/21509710/) | 2011 | Cohort | Klin Padiatr | Desmopressin effect on primary haemostasis in children with aspirin-like defect |
| [15499705](https://pubmed.ncbi.nlm.nih.gov/15499705/) | 2004 | Case report | Thromb Haemost | Worsening of TTP symptoms after desmopressin |
| [21921792](https://pubmed.ncbi.nlm.nih.gov/21921792/) | 2011 | Case report | Blood Coagul Fibrinolysis | Desmopressin-induced Moschcowitz-like syndrome after treatment of postpartum haemorrhage |
| [16444446](https://pubmed.ncbi.nlm.nih.gov/16444446/) | 2006 | Case report | Clin Appl Thromb Hemost | Glanzmann thrombasthenia: desmopressin ineffective; dental extraction managed with rFVIIa |
| [1785670](https://pubmed.ncbi.nlm.nih.gov/1785670/) | 1991 | Cohort | Am J Pediatr Hematol Oncol | Desmopressin plus ethamsylate shortened bleeding time in 12 patients with constitutional bleeding disorders unresponsive to desmopressin alone |
| [12109311](https://pubmed.ncbi.nlm.nih.gov/12109311/) | 2002 | Case report | Ned Tijdschr Geneeskd | Desmopressin trial dose caused severe thrombocytopenia in VWD type 2B |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12458Q | Desmopressin Nasal Spray USP (Apotex) | Nasal spray (pump pack), desmopressin acetate 10 micrograms per actuation, 50 actuations, 5 mL | Not available in the data compiled for this report |

---

## Safety Considerations

**Contraindications and conditions flagged in the knowledge graph** (these come from graph relationships, not product label text): hypertension, coronary artery disease, impaired renal function, allergic and vasomotor rhinitis, pharyngitis, common cold, respiratory tract infection, cystic fibrosis, von Willebrand disease (certain types), dipsogenic diabetes insipidus, polydipsia and water intoxication.

**Drug Interactions** (100 interactions recorded; main ones shown):
- **Major:** Systemic and inhaled corticosteroids, including hydrocortisone, triamcinolone, dexamethasone, beclomethasone, betamethasone, budesonide, prednisolone and prednisone
- **Moderate:** Epinephrine, loperamide, morphine (including liposomal), opium and chlorpropamide
- **Minor:** Acetylsalicylic acid

**Key concerns for the predicted indications:** Desmopressin carries a thrombotic risk and can cause hyponatraemia. It may worsen TTP, platelet-type VWD and VWD type 2B (thrombocytopenia). Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top prediction (congenital prothrombin deficiency) has no clinical trials, no supportive literature and no plausible mechanism. Several other high-ranking predictions (TTP, thrombophilia, platelet-type VWD) are mechanistically contradictory and represent safety concerns.

**To proceed, the following is needed:**
- Curation of the TxGNN output, including the "flood factor deficiency" mapping error
- If a repurposing direction is pursued, prioritise **primary release disorder of platelets** (the only L3 candidate), with prospective or controlled data
- Mechanism of action data and TGA Product Information warnings and contraindications
- Indication text for the ARTG entry
- Safety assessment of thrombotic risk and hyponatraemia in target populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

