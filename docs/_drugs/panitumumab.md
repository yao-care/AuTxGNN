---
layout: default
title: Panitumumab
parent: Model Prediction Only (L5)
nav_order: 545
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Panitumumab: predicted new indication Drug-induced osteoporosis (evidence level L5). Approved use: Metastatic malignant neoplasm in the colon"
monitor_inn: "Panitumumab"
predicted_indications: ["drug-induced osteoporosis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "diabetic cataract", "cortical cataract", "nuclear senile cataract", "diabetes mellitus type 2 associated cataract", "craniostenosis cataract", "tetanic cataract", "immature cataract"]
---

# Panitumumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Panitumumab: From Metastatic Colorectal Cancer to Drug-Induced Osteoporosis
{: .text-alpha }

## One-Sentence Summary

Panitumumab is an anti-EGFR monoclonal antibody, originally used to treat metastatic malignant neoplasm of the colon.
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**,
but **no clinical trials and no publications** currently support this direction, so this is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic malignant neoplasm in the colon (from the knowledge graph; the ARTG indication text was not available) |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.13% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, panitumumab is an anti-EGFR monoclonal antibody, its use in metastatic colon cancer is established, and EGFR signalling has a theoretical link to bone metabolism.

EGFR signalling influences osteoblast differentiation and osteoclast regulation (for example, via RANKL). This gives a theoretical connection between panitumumab and bone biology. However, EGFR blockade would be expected to impair rather than protect bone formation, which runs against the direction of the predicted benefit.

The high TxGNN score (0.991) is a computational output only. Without supporting clinical or literature evidence, and without curated mechanism data to cross-check it, the prediction should be regarded as a hypothesis with low mechanistic credibility.

Other top-ranked predictions are also all L5 (model prediction only). They include severe nonproliferative diabetic retinopathy, diabetic retinopathy, and several cataract subtypes (diabetic, cortical, nuclear senile, type 2 diabetes-associated, craniostenosis, tetanic and immature). Several of these scores appear to reflect shared graph neighbours rather than independent evidence. For tetanic cataract, panitumumab's tendency to cause low magnesium and calcium could worsen the condition.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10069Y | Vectibix | Solution concentrate for I.V. infusion, 100 mg in 5 mL | Not available in the data compiled for this report |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-EGFR monoclonal antibody) |
| Myelosuppression Risk | Low; not a conventional myelosuppressive cytotoxic. Please refer to the Product Information (PI) |
| Emetogenicity Classification | Low |
| Monitoring Items | Electrolytes (particularly magnesium, also calcium), skin and ocular assessment, FBC and liver and renal function as clinically indicated |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions and local institutional policy for handling of antineoplastic agents |

## Safety Considerations

Product Information warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for full safety information.

**Drug Interactions** (27 interactions recorded; selected examples shown):
- **Major:** amiodarone, arsenic trioxide, bevacizumab, dofetilide, dronedarone, droperidol, irinotecan (including liposomal), levacetylmethadol, aminolevulinic acid
- **Moderate:** proton pump inhibitors (rabeprazole, omeprazole, dexlansoprazole, esomeprazole, lansoprazole, pantoprazole), methoxsalen, topical aminolevulinic acid, disopyramide, idelalisib

**Other considerations from the rationale review:** known toxicities include dermatological effects, ocular surface effects such as keratitis, and hypomagnesaemia. These weigh against use in chronic, non-oncology conditions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no trials or publications, and the biology suggests EGFR blockade would more likely harm than help bone. The systemic safety profile is also unfavourable for a chronic non-cancer indication.

**To proceed, the following is needed:**
- Parsed TGA Product Information (warnings and contraindications), which is currently a blocking gap
- Curated mechanism of action data (for example, from DrugBank)
- Preclinical or observational evidence that EGFR inhibition benefits bone, rather than impairing it
- Route and dose compatibility assessment for the proposed indication
- A benefit-risk assessment of anti-EGFR toxicity in a non-oncology population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

