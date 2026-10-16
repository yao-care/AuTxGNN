---
layout: default
title: Ciclesonide
parent: Model Prediction Only (L5)
nav_order: 160
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ciclesonide: predicted new indication Atopic eczema (evidence level L5). Approved use: Asthma"
monitor_inn: "Ciclesonide"
predicted_indications: ["atopic eczema", "2-hydroxyethyl methacrylate sensitization", "dermatitis, atopic", "bronchitis", "contact dermatitis", "asthma-related traits, susceptibility to", "phototoxic dermatitis", "occupational dermatitis", "seborrheic dermatitis", "polyp of vocal cord"]
---

# Ciclesonide
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

# Ciclesonide: From Asthma to Atopic Eczema

## One-Sentence Summary

Ciclesonide is an inhaled corticosteroid, originally used to treat asthma and allergic or vasomotor rhinitis.
The TxGNN model predicts it may be effective for **atopic eczema**,
but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma (the licence entry has no approved indication text; asthma and allergic or vasomotor rhinitis come from the knowledge graph) |
| Predicted New Indication | Atopic eczema |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, ciclesonide is an inhaled corticosteroid prodrug that is activated to des-ciclesonide by esterases. Its anti-inflammatory activity is mediated through the glucocorticoid receptor.

Asthma and allergic rhinitis are allergic, atopic inflammatory conditions, and atopic eczema belongs to the same atopic disease spectrum. Topical corticosteroids are already standard care for atopic eczema, so a glucocorticoid anti-inflammatory rationale is plausible.

There are important caveats. The high TxGNN score is a prediction only. Ciclesonide is formulated as a pressurised inhalation, not a skin product. Skin activation, delivery and local safety have not been established for this use. The related entry "dermatitis, atopic" (score 99.73%) is essentially the same condition and is likely a redundant ontology term.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was linked to atopic eczema. Two items were linked to other predicted indications and are indirect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Guideline/Review | Basic & Clinical Pharmacology & Toxicology | Finnish COPD guideline (linked to bronchitis). It suggests inhaled corticosteroids have a role in selected COPD phenotypes. It does not evaluate ciclesonide for eczema. |
| [22957490](https://pubmed.ncbi.nlm.nih.gov/22957490/) | 2012 | Case report | Contact Dermatitis | Systemic allergic dermatitis caused by inhaled budesonide, with patch-test cross-reactivity to ciclesonide (linked to contact dermatitis). This is a safety signal, not evidence of efficacy. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14312G | Alvesco 80 | Pressurised inhalation, 80 micrograms per dose, 120 doses (CFC-free formulation) | Not stated in the data compiled for this report |

## Safety Considerations

- **Drug Interactions**: 63 interactions were identified. Key examples:
  - **Major**: cladribine.
  - **Moderate**: clarithromycin, miconazole, cobicistat, atazanavir, fosamprenavir, amprenavir, boceprevir, ceritinib, conivaptan, fostamatinib, inhaled human insulin and topical abametapir. Several of these are CYP3A4 inhibitors, which may increase systemic corticosteroid exposure.
  - **Minor**: formoterol, salbutamol and arformoterol.
  - **Unknown severity**: omeprazole, lansoprazole, famotidine and prednisolone.
- **Knowledge-graph contraindication signals** (not label text): herpes simplex keratitis, adrenocortical insufficiency, Addison disease, osteoporosis, postmenopausal osteoporosis, fungal infections, dermatophytosis, ocular hypertension, glaucoma and parasitic infection.
- **Hypersensitivity**: a published case report describes cross-reactivity in patch tests between budesonide and ciclesonide, so contact allergy to corticosteroids is a consideration.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications, as these were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output and a class-level corticosteroid rationale only. There are no trials or literature for atopic eczema (Evidence Level L5). Ciclesonide is not formulated for skin use, and approved topical corticosteroids already exist for this condition.

**To proceed, the following is needed:**
- Mechanism of action data and the TGA Product Information safety text (warnings and contraindications)
- Evidence of skin activation of ciclesonide to des-ciclesonide and a suitable topical formulation
- Preclinical or early-phase clinical data in atopic eczema, including comparison with established topical corticosteroids
- Merging of the redundant ontology entries ("atopic eczema" and "dermatitis, atopic") and review of cross-reactivity and contact allergy risk
- Review of the other predicted indications, which are also at Hold, and removal of the non-actionable "asthma-related traits, susceptibility to" entry
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

