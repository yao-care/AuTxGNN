---
layout: default
title: Sulfamethoxazole
parent: Model Prediction Only (L5)
nav_order: 690
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
monitor_inn: "sulfamethoxazole"
predicted_indications: ["acute contagious conjunctivitis"]
description: "Sulfamethoxazole: predicted new indication Acute contagious conjunctivitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Sulfamethoxazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Sulfamethoxazole: Acute contagious conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Sulfamethoxazole is a sulfonamide antibacterial, usually given with trimethoprim, and is originally used for infections such as otitis media, nocardiosis, toxoplasmosis, pneumocystosis, shigellosis and conjunctivitis.
The TxGNN model predicts it may be effective for **acute contagious conjunctivitis**, with **no registered clinical trials** and **1 publication** (a retrospective cohort study) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acute contagious conjunctivitis |
| TxGNN Prediction Score | 0.9963 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, sulfamethoxazole is a sulfonamide that inhibits bacterial dihydropteroate synthase, which blocks folate synthesis. It is typically combined with trimethoprim, which blocks a later step in the same pathway. This mechanism is plausibly relevant to bacterial conjunctivitis.

"Conjunctivitis" already appears among the drug's original indications. Acute contagious conjunctivitis is therefore best viewed as a subtype of, or a close match to, an existing use rather than a new indication.

The very high TxGNN score (0.9963) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The oral tablet formulation (160 mg/800 mg) also differs from the topical antibiotics commonly used for conjunctivitis, so route suitability has not been assessed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31788487](https://pubmed.ncbi.nlm.nih.gov/31788487/) | 2019 | Cohort (retrospective) | Medical Hypothesis, Discovery & Innovation Ophthalmology Journal | Bacteriology and antibiotic susceptibility patterns in childhood acute bacterial conjunctivitis at a paediatric hospital in Western Greece. It describes microbiology and susceptibility, not the efficacy of sulfamethoxazole. |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10784N | Bactrim DS | Tablet 160 mg-800 mg | Not available in the data compiled for this report |

---

## Safety Considerations

**Contraindication-related conditions (from knowledge graph drug–disease edges, not label text):**
- Porphyria (inherited porphyria, porphyrin metabolism disease)
- Kidney disease, kidney failure, uremia, glomerulonephritis, pyoureter
- Liver disease, gallbladder disease
- Blood disorders: thrombocytopenia, neutropenia, agranulocytosis, folic acid deficiency anaemia
- G6PD deficiency
- *Clostridium difficile* colitis, perinatal necrotising enterocolitis
- Metabolic conditions: glycogen storage disease, cystinuria, galactosemia

**Drug Interactions:** 151 interactions were recorded. The first 20 returned include:
- **Moderate:** sulfonylureas and related agents (chlorpropamide, glimepiride, acetohexamide, glipizide, glyburide), multiple insulins (human, aspart, degludec, detemir, glargine, glulisine), balsalazide, picosulfuric acid. The main concern with antidiabetic agents is likely additive hypoglycaemia.
- **Minor:** famotidine, clarithromycin, dolasetron, palonosetron, cisapride, granisetron.

Warnings and contraindications from the TGA-approved Product Information (PI) were not available for this report. Please refer to the PI for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The only supporting study is a retrospective susceptibility cohort with no efficacy data, and there are no registered trials.

**To proceed, the following is needed:**
- Approved indication text and PI safety information for ARTG 10784N
- Detailed mechanism of action data
- Clarification of whether the intended use is oral therapy or a topical or ophthalmic formulation, and whether the indication is genuinely new
- Efficacy and susceptibility data specific to sulfamethoxazole or co-trimoxazole in acute bacterial conjunctivitis, ideally including Australian resistance patterns
- Review of the safety flags above, particularly G6PD deficiency, blood disorders, renal and hepatic impairment, and interactions with antidiabetic agents
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

