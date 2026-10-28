---
layout: default
title: Meloxicam
parent: Model Prediction Only (L5)
nav_order: 455
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-28
monitor_inn: "Meloxicam"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "rheumatoid nodulosis", "WHIM syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
description: "Meloxicam: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Not recorded in the local data"
---

# Meloxicam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Meloxicam: Acromesomelic dysplasia, Hunter-Thompson type
{: .text-alpha }

## One-Sentence Summary

Meloxicam is a COX-2-preferential NSAID originally used for rheumatoid arthritis, osteoarthritis and related inflammatory joint conditions.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**,
but there are currently **no clinical trials** and **no publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, meloxicam is a COX-2-preferential NSAID. It reduces prostaglandin-mediated inflammation and pain, and its efficacy in inflammatory and degenerative joint disease is established.

Hunter-Thompson type acromesomelic dysplasia is a skeletal dysplasia caused by loss-of-function mutations in *CDMP1/GDF5*. Meloxicam has no known action on the GDF5/BMP signalling pathway. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. At most, an NSAID might offer symptomatic joint-pain relief. It would not modify the disease.

The other highly ranked predictions follow a similar pattern. Most are rare skeletal or genetic conditions (brachyolmia, pseudoachondroplasia, myosclerosis and others) with no plausible COX-inhibition mechanism. Two are of more practical interest because they sit close to meloxicam's existing uses:

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No publications are available for the top-ranked prediction (acromesomelic dysplasia, Hunter-Thompson type). For the rank 8 prediction (RF-positive polyarticular JIA), one indirect publication was identified:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25057265](https://pubmed.ncbi.nlm.nih.gov/25057265/) | 2014 | Safety registry (Phase 4; exact design not confirmed) | Pediatric Rheumatology Online Journal | Long-term safety and developmental data for celecoxib versus nonselective NSAIDs in JIA patients in routine practice. It is not meloxicam-specific and does not address efficacy. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 8561N | CIPLA MELOXICAM 7.5 | Tablet 7.5 mg (oral) | Not stated in the data compiled for this report |

## Safety Considerations

**Contraindications and conditions of concern (from knowledge-graph drug-disease edges, not product label text):**
- Cardiovascular: hypertension, congestive heart failure, myocardial infarction, coronary thrombosis, stroke and other cerebrovascular disorders, cardiovascular and heart disease
- Gastrointestinal: active peptic ulcer disease, gastritis
- Renal: kidney disease, impaired renal function
- Haematological: blood coagulation disease, anaemia, haemoglobinopathy
- Metabolic and other: diabetes mellitus, diabetic ketoacidosis, hyperlipidaemia (including familial), substance abuse/dependence

**Drug Interactions:** The interaction screen returned 100 interacting drugs. The 20 reviewed were mostly Moderate, with one Minor (linaclotide). The main ones were:
- Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide
- Aspirin (acetylsalicylic acid) and mesalazine/balsalazide
- Antidiabetic agents: metformin, glimepiride, chlorpropamide
- Aprepitant
- Potassium salts (potassium citrate, potassium bicarbonate)
- Bowel preparations: picosulfuric acid, polyethylene glycol with electrolytes, sodium sulfate
- Aminoglycoside and glycopeptide antibiotics: kanamycin, vancomycin

Please refer to the TGA-approved Product Information (PI) for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for acromesomelic dysplasia, Hunter-Thompson type rests on model output alone (L5). It has no trials or literature, and there is no plausible mechanistic link between COX inhibition and a GDF5 loss-of-function disorder. The knowledge graph also lists many cardiovascular, gastrointestinal and renal contraindications for meloxicam.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA)
- The TGA-approved Product Information, including warnings and contraindications, so that safety screening can proceed
- Indication text for the ARTG entry
- Any clinical or preclinical evidence of meloxicam in the predicted disease, or a symptom-based rationale (for example joint pain) with a defined outcome measure
- Consideration of the rank 8 prediction (RF-positive polyarticular JIA) as a more practical research question, with efficacy data for meloxicam in that subtype
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

