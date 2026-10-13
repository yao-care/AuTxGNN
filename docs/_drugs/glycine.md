---
layout: default
title: Glycine
parent: Model Prediction Only (L5)
nav_order: 341
evidence_level: L5
indication_count: 2
---

# Glycine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Glycine: From Allergic Rhinitis and Related Upper Airway Conditions to Nasal Cavity Disease

## One-Sentence Summary

Glycine is an amino acid product. The TxGNN knowledge graph links it to upper airway conditions such as allergic rhinitis, vasomotor rhinitis, pharyngitis and the common cold.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but there are **no relevant clinical trials** and **no relevant publications** supporting this direction. The prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, rhinitis, nasopharyngitis (from the TxGNN knowledge graph; no approved indication text is available for the Australian listing) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Glycine is already linked in the knowledge graph to several upper airway conditions (allergic rhinitis, vasomotor rhinitis, rhinitis and nasopharyngitis). These overlap with nasal cavity disease, which may explain the high prediction score.

The score may therefore reflect similarity between indication classes rather than independent evidence. The trial and literature records retrieved do not connect glycine to nasal pathology, so no mechanistic rationale can be established from the data compiled for this report.

A second prediction, **acute laryngopharyngitis** (score 99.84%), has no trials or literature. It is adjacent to the existing pharyngitis and common cold indications. It sits at the same evidence level (L5) and carries the same Hold recommendation.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01806675](https://clinicaltrials.gov/study/NCT01806675) | Phase 1/2 | Completed | 25 | PET imaging of a new radiopharmaceutical (18F-FPPRGD2) in cancer patients receiving antiangiogenesis treatment. This is a diagnostic imaging study and does not test glycine or nasal disease. |

No trial directly supports glycine for nasal cavity disease.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7771054](https://pubmed.ncbi.nlm.nih.gov/7771054/) | 1995 | Basic research (animal tissue) | Veterinary Pathology | Lectin histochemistry of normal and herpesvirus-infected bovine nasal mucosa. It does not involve glycine as a treatment. |
| [29607903](https://pubmed.ncbi.nlm.nih.gov/29607903/) | 2018 | Preclinical formulation study | Chemical & Pharmaceutical Bulletin | Oligoarginine-polymer conjugates as mucosal adjuvants for nasal vaccination in mice. It does not involve glycine as a treatment. |

Neither publication provides clinical evidence for glycine in nasal cavity disease.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10195N | Glycine500 | Sachets of oral powder, 4 g containing 500 mg glycine, 30 sachets | Not available |

Only an oral formulation is listed. Route compatibility with nasal cavity disease has not been assessed.

## Safety Considerations

- **Contraindications from the knowledge graph (not label text):** The TxGNN knowledge graph lists contraindication links with several disease groups. These should be verified against the Product Information.
  - Kidney disease (including chronic kidney disease, chronic renal failure and end-stage renal failure) and nephrolithiasis
  - Calcium and phosphate disorders (hypercalcaemia, hyperparathyroidism, hyperphosphataemia, nephrocalcinosis)
  - Cardiovascular conditions (heart disease, ventricular fibrillation, digitalis poisoning)
  - Phenylketonuria and other disorders of phenylalanine metabolism
  - Others, including sarcoidosis, hypervitaminosis, constipation disorder and lytic metastatic bone lesions
- **Drug Interactions:** No interaction records were found.

No label-based warnings or contraindications were available. Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score alone (L5). There are no relevant clinical trials or publications, mechanism data are missing, and no approved indication text or label safety data were available. The score may reflect similarity to existing upper airway indications rather than independent evidence.

**To proceed, the following is needed:**
- Mechanism of action data for glycine (for example from DrugBank) and a plausible mechanistic link to nasal pathology
- The approved indication text and Product Information (warnings and contraindications) for the Australian listing
- Preclinical or clinical studies of glycine in nasal cavity disease
- An assessment of whether an oral sachet is a suitable route for a nasal condition
- A review of the knowledge-graph contraindication signals, especially renal, cardiovascular and phenylketonuria-related ones
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

