---
layout: default
title: Disopyramide
parent: Model Prediction Only (L5)
nav_order: 220
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
monitor_inn: "Disopyramide"
predicted_indications: ["Tourette syndrome", "attention deficit-hyperactivity disorder", "trichotillomania", "attention deficit hyperactivity disorder, inattentive type", "faciodigitogenital syndrome", "specific developmental disorder", "idiopathic neonatal atrial flutter", "chondromyxoid fibroma", "multifocal atrial tachycardia (disease)", "trigeminal nerve neoplasm"]
description: "Disopyramide: predicted new indication Tourette syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Disopyramide
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

## Disopyramide: Tourette syndrome
{: .text-alpha }

## One-Sentence Summary

Disopyramide is a class Ia antiarrhythmic (sodium channel blocker with anticholinergic activity). The original indication is not recorded in the data compiled for this report.
The TxGNN model predicts it may be effective for **Tourette syndrome**, but there are **0 clinical trials** and **0 publications** supporting this prediction. It is a model-only prediction with no clinical evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 0.9986 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on its drug class, disopyramide is a class Ia antiarrhythmic that blocks cardiac sodium channels and has anticholinergic activity. Its use in supraventricular and ventricular arrhythmias is established.

No clear mechanistic link to Tourette syndrome was identified. Tourette syndrome involves dopaminergic dysfunction in cortico-striato-thalamo-cortical circuits, which are not known targets of disopyramide. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other top-ranked predictions show the same pattern. ADHD (0.9982), trichotillomania (0.9981), ADHD inattentive type (0.9974), faciodigitogenital syndrome (0.9966), specific developmental disorder (0.9954), chondromyxoid fibroma (0.9941) and trigeminal nerve neoplasm (0.9916) have no plausible mechanism and no clinical evidence. The only predictions within disopyramide's pharmacological domain are the cardiac ones: idiopathic neonatal atrial flutter (0.9942) and multifocal atrial tachycardia (0.9921). These are indirect, class-level plausibility only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for Tourette syndrome.

For context, the only publication in the data compiled for this report relates to a lower-ranked prediction (multifocal atrial tachycardia):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7418495](https://pubmed.ncbi.nlm.nih.gov/7418495/) | 1980 | Cohort (case report) | Chest | A patient with resistant ventricular and supraventricular arrhythmias failed multiple drugs, including disopyramide, and was treated with lorcainide. It does not evaluate disopyramide as a treatment for this condition. |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 13280Y | Rythmodan (Canada) | Capsule 100 mg (s19A) | Not recorded |

This is a single valid product, supplied as an oral capsule under Section 19A (imported, not a standard ARTG-registered product).

---

## Safety Considerations

**Contraindications flagged in the knowledge graph (not label text):** The TxGNN knowledge graph lists the following conditions as contraindicated with disopyramide. These must be verified against the Product Information.

- **Cardiac:** long QT syndrome (including familial), atrioventricular block, cardiomyopathy (including hypertrophic), myocarditis, endomyocardial fibrosis, myocardial disorder, atrial fibrillation, atrial flutter, hypotensive disorder
- **Anticholinergic-related:** angle-closure glaucoma, benign prostatic hyperplasia, myasthenia gravis and neuromuscular junction disease
- **Organ function and metabolic:** kidney disease, liver disease, gallbladder disease, pyoureter, potassium deficiency, hypoglycaemia

**Drug Interactions:** 100 interactions were identified. Examples:
- **Major:** clarithromycin, potassium citrate, picosulfuric acid
- **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), amphotericin B, anticholinergics (atropine, hyoscyamine, glycopyrronium, clidinium), famotidine, loperamide, aprepitant, bisacodyl, chlorpropamide
- **Minor:** cimetidine

In a paediatric or neuropsychiatric population, proarrhythmic risk and QT prolongation would be a particular concern. Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score, with no clinical trials, no literature and no plausible mechanism. The cardiac risk profile (QT prolongation, proarrhythmia, negative inotropy) is unfavourable for a non-cardiac indication.

**To proceed, the following is needed:**
- Original approved indication from the PI or ARTG record
- Mechanism of action data (e.g. from DrugBank)
- Product Information warnings and contraindications
- Preclinical or mechanistic evidence linking disopyramide to Tourette syndrome
- A comparison against established Tourette syndrome therapies
- A cardiac safety assessment for the target population

**Alternative research direction:** The cardiac predictions (idiopathic neonatal atrial flutter and multifocal atrial tachycardia) fit disopyramide's pharmacology better and could be explored as research questions. They would still require dedicated evidence and a neonatal safety review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

