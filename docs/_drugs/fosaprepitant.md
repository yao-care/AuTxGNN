---
layout: default
title: Fosaprepitant
parent: Model Prediction Only (L5)
nav_order: 318
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Fosaprepitant: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Fosaprepitant"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "pneumocystosis", "leprosy", "Cryptococcal meningitis", "multiple endocrine neoplasia", "intracranial abscess", "retinitis", "Plasmodium falciparum malaria", "echinococcus granulosus infectious disease", "hyperargininemia"]
---

# Fosaprepitant
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

## Fosaprepitant: From Chemotherapy-Related Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis
{: .text-alpha }

## One-Sentence Summary

Fosaprepitant is an intravenous prodrug of aprepitant, a substance P/NK1 receptor antagonist. It is marketed in Australia as Emend IV, although the data compiled for this report do not include its approved indication text.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction. This is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the ARTG entry has no indication text) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on known information, fosaprepitant is a prodrug of aprepitant, which blocks NK1 receptors (the receptors for substance P).

NSIAD is caused by gain-of-function variants of the vasopressin V2 receptor, which lead to water retention and low blood sodium. No established link connects NK1 receptor antagonism to this mechanism. Any connection, for example indirect modulation of water balance through neuropeptide signalling, is speculative.

The high TxGNN score therefore comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for NSIAD.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11103J | Emend IV | Powder for I.V. infusion 150 mg | Not stated in the data compiled |

## Cytotoxicity

Fosaprepitant is a supportive-care antiemetic, not an antineoplastic agent, so no cytotoxicity assessment applies.

## Safety Considerations

- **Contraindications (model signal, not label text)**: The TxGNN model (deep learning) flags a possible contraindication with **liver failure**. This is not derived from the product label and may reflect similarities the model learned between related diseases, not biological evidence. It should be verified against the TGA-approved Product Information (PI).
- **Drug Interactions**: 100 interactions were identified in total. The following are examples from the DDInter source.
  - **Major**: eliglustat, naloxegol
  - **Moderate**: corticosteroids (dexamethasone, hydrocortisone, betamethasone, budesonide, triamcinolone), clarithromycin, cimetidine, proton pump inhibitors (rabeprazole, lansoprazole), miconazole, pioglitazone, glimepiride, nateglinide, saxagliptin, alosetron, dronabinol, naldemedine

Please refer to the TGA-approved Product Information (PI) for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). There are no trials or publications, and no plausible mechanistic link between NK1 antagonism and the V2 receptor gain-of-function that causes NSIAD.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) and a testable mechanistic hypothesis for NSIAD
- The approved indication text and the TGA Product Information, including warnings and contraindications, to allow safety screening
- Preclinical or case-level evidence of an effect on water balance or vasopressin signalling
- Review of the liver failure contraindication signal and the CYP3A4-related interaction burden for the target population

## Other Predicted Indications (Context)

The other top-ranked predictions are also model-only (L5) with no supporting trials or literature, and all carry a Hold recommendation. They are pneumocystosis, leprosy, cryptococcal meningitis, multiple endocrine neoplasia, intracranial abscess, *Plasmodium falciparum* malaria, echinococcosis and hyperargininemia. The exception is **retinitis** (rank 7, score 0.9968), which has L4 preclinical support from one mouse study (PMID [32058829](https://pubmed.ncbi.nlm.nih.gov/32058829/), 2021, *Ocular Immunology and Inflammation*). That study showed fosaprepitant blocked UVR-B-induced NK1R expression in ocular tissues. It used a UV-induced injury model and not clinical retinitis, so its translational relevance is uncertain. It is classed as a research question and not a development candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

