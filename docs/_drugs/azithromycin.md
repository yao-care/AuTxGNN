---
layout: default
title: Azithromycin
parent: Model Prediction Only (L5)
nav_order: 78
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Azithromycin: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Streptococcal infection, bacterial pneumonia…"
monitor_inn: "Azithromycin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "punctate epithelial keratoconjunctivitis", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder"]
---

# Azithromycin
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

## Azithromycin: From Bacterial Infections to Hyperamylasemia
{: .text-alpha }

## One-Sentence Summary

Azithromycin is a macrolide antibiotic originally used for bacterial infections such as streptococcal and staphylococcal infections, bacterial pneumonia, conjunctivitis and sexually transmitted infections.
The TxGNN model predicts it may be effective for **hyperamylasemia**, but **no clinical trials and no publications** currently support this prediction.
The result looks like a graph-based artefact rather than a credible repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Streptococcal infection, bacterial pneumonia, staphylococcal infection and related infections (the Australian licence text is blank; indications come from the knowledge graph) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, azithromycin is a macrolide antibiotic, its efficacy in bacterial infections is established, and it is also reported to have anti-inflammatory and immunomodulatory effects.

Hyperamylasemia is a laboratory finding (raised serum amylase) rather than a disease with a defined therapeutic target. Azithromycin's antibacterial and immunomodulatory actions do not plausibly address it, and no mechanistic link has been identified. The high TxGNN score therefore appears to reflect graph structure rather than biology.

Other predictions from the same model fare slightly better, though none is strong. The most notable are:
- **Congenital hematological disorder** (score 99.40%): the strongest clinical rationale, in sickle cell disease. Two trials of azithromycin or macrolide therapy for acute chest syndrome and lung function were withdrawn with zero enrolment.
- **Monogonal gammopathy** (score 99.61%): preclinical data show macrolides block autophagy and sensitise myeloma cells to bortezomib. This is in vitro evidence in myeloma, not in MGUS.
- **Septicemic plague** (score 99.52%): in vitro data show azithromycin has poor activity against *Yersinia pestis*, and established first-line agents exist.

## Clinical Trial Evidence

Currently no related clinical trials registered for hyperamylasemia.

## Literature Evidence

Currently no related literature available for hyperamylasemia.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 4115N | Zithromax | Tablet 500 mg (as dihydrate) | Not available in the data compiled for this report |

## Safety Considerations

- **Disease associations flagged in the knowledge graph (contraindication edges, not label text)**: long QT syndrome (including familial), torsades de pointes, liver disease, gallbladder disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, myasthenia gravis, neuromuscular junction disease, and hearing or auditory system disorders.
- **Drug Interactions** (100 interactions recorded; examples below):
  - **Major**: cisapride, dolasetron (QT-prolongation concern).
  - **Moderate**: famotidine, loperamide, clarithromycin, levofloxacin, granisetron, aluminium hydroxide and magnesium-containing antacids, and several laxatives (bisacodyl, lactulose, lactitol, glycerin, castor oil).
  - **Minor**: amoxicillin, metronidazole.

Please refer to the TGA-approved Product Information (PI) for authoritative warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no trials, no literature and no plausible mechanism. Hyperamylasemia is a laboratory finding, not a treatable disease target.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking azithromycin to the condition underlying the raised amylase
- Mechanism of action data for azithromycin
- Approved indication text and safety information from the TGA Product Information
- If a repurposing programme is wanted, redirect effort to better-supported candidates, such as sickle cell disease (acute chest syndrome prophylaxis), where the withdrawn trials show clinical interest but have produced no data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

