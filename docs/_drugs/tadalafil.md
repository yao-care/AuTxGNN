---
layout: default
title: Tadalafil
parent: Model Prediction Only (L5)
nav_order: 696
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-30
monitor_inn: "Tadalafil"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly", "kyphoscoliotic heart disease", "migraine with brainstem aura"]
description: "Tadalafil: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Not recorded in the local data"
---

# Tadalafil
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

## Tadalafil: Ambras type hypertrichosis universalis congenita
{: .text-alpha }

## One-Sentence Summary

Tadalafil is a PDE5 inhibitor originally used for erectile dysfunction, benign prostatic hyperplasia and pulmonary hypertension, among other indications.
The TxGNN model (deep learning) predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tadalafil is a PDE5 inhibitor, a class that raises cGMP levels and causes vasodilation. Its efficacy in erectile dysfunction and pulmonary hypertension is established, but no mechanistic link to the predicted new indication has been shown.

Ambras syndrome is a rare genetic disorder of hair growth. No plausible PDE5 inhibition pathway has been established, and tadalafil's vasodilatory and cGMP-related effects have no demonstrated connection to the disease mechanism. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related hair-phenotype diseases, not biological evidence.

The other top-ranked predictions are also unsupported by evidence. Several are hair-related (hypertrichosis, isolated genetic hair shaft abnormality, familial isolated trichomegaly, hypotrichosis simplex of the scalp). Hypertrichosis is a known adverse effect of some vasodilators such as minoxidil, which suggests a possible risk rather than a benefit. The only prediction with a plausible indirect rationale is kyphoscoliotic heart disease (rank 7), given tadalafil's use in pulmonary hypertension, but this is unvalidated.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the top predicted indication.

For context, the only tadalafil-specific paper found among the lower-ranked predictions is a 2006 case report ([PMID 17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/), *Cephalalgia*) describing tadalafil associated with typical migraine aura without headache. This points to an adverse effect rather than a therapeutic benefit.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12150L | Tadalca | Tablet 20 mg | Not stated in the data compiled for this report |

---

## Safety Considerations

**Contraindication signals from the knowledge graph** (drug-disease edges, not product label text):
- Cardiovascular: aortic stenosis and other aortic valve disease, hypotensive disorder, acute coronary syndrome, myocardial infarction, coronary thrombosis, stroke and cerebrovascular disorders, cerebral infarction, hypertrophic cardiomyopathy (including familial)
- Haematological: sickle cell anaemia, hemoglobinopathy, hereditary persistence of fetal haemoglobin, blood coagulation disease, plasma cell myeloma, leukaemia
- Genitourinary: priapism, Peyronie disease and related penile fibromatosis
- Other: liver failure, epilepsy, hearing loss disorders, visual loss

**Drug interactions** (DDInter, 100 interactions recorded; examples):
- Moderate: aprepitant, dexamethasone, clarithromycin, cimetidine, miconazole, clotrimazole, lorcaserin, sapropterin, troglitazone, and the SGLT2 inhibitors canagliflozin, dapagliflozin, empagliflozin and ertugliflozin
- Minor: papaverine
- Unknown severity: pantoprazole, glimepiride, doxycycline, morphine, metformin, omeprazole

Several interacting drugs are CYP3A4 inhibitors or inducers, which is relevant to tadalafil exposure. Please also refer to the TGA-approved Product Information (PI) for warnings and contraindications, as label-based data were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN model (deep learning) score, which may reflect similarities the model learned between related diseases, not biological evidence. There are no clinical trials or publications and no plausible mechanistic link between PDE5 inhibition and Ambras syndrome. The few related signals (hypertrichosis as a vasodilator class effect, migraine aura case report) suggest possible risk rather than benefit.

**To proceed, the following is needed:**
- Mechanism of action data (for example, from DrugBank) and a clear mechanistic rationale for the predicted indication
- Product Information warnings and contraindications from the TGA, which are currently missing and block safety screening
- Preclinical or clinical evidence in the predicted condition
- ARTG approved indication text for the registered product
- A review of whether a better-supported candidate indication (for example, kyphoscoliotic heart disease via pulmonary hypertension) merits evaluation instead
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

