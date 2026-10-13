---
layout: default
title: Iodine
parent: Moderate Evidence (L3-L4)
nav_order: 386
evidence_level: L4
indication_count: 10
---

# Iodine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Iodine: From an Unspecified Original Indication to Sjogren Syndrome

## One-Sentence Summary

Iodine is registered in Australia, but the data compiled for this report do not state its approved indication.
The TxGNN model predicts it may be effective for **Sjogren syndrome**, but there are **no registered clinical trials** and the literature is mostly about harms, diagnostic imaging, or disease associations rather than benefit.
The prediction is best treated as a model artefact. The only indication with trial-level evidence in the data is **keratitis**, through povidone-iodine.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available data |
| Predicted New Indication | Sjogren syndrome |
| TxGNN Prediction Score | 94.09% |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Iodine is an essential trace element for thyroid hormone synthesis, and iodine-based antiseptics are widely used topically. Neither role provides a therapeutic rationale for Sjogren syndrome.

The literature links iodine to the salivary glands mainly through harm and diagnostics. Radioiodine can cause sialadenitis that mimics Sjogren features, and iodine is used in salivary imaging. Sodium iodide symporter (NIS) work also describes autoimmune thyroid disease and Sjogren syndrome occurring together. These are associations or harms, not evidence of benefit. The high TxGNN score probably reflects network proximity through thyroid and salivary gland biology rather than a real treatment effect.

**Other predictions reviewed**

| Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|
| Prolapse of lacrimal gland | 93.64% | L5 | Prediction only, with no plausible mechanism |
| Acne | 93.11% | L4 | Topical povidone-iodine has antimicrobial activity, but the evidence is weak. Systemic iodine can worsen acne (iodism). |
| Seborrheic keratosis | 91.41% | L4 | One diagnostic study only |
| Fetal erythroblastosis | 91.03% | L4 | The only relevant report describes fetal harm (thyroid hyperplasia) |
| Recurrent corneal erosion | 90.66% | L4 | One 1964 paper, with no modern support |
| **Keratitis** | 89.70% | L1 (tempered) | Povidone-iodine trials in infectious keratitis. See below. |
| Vulvar inverted follicular keratosis | 89.63% | L5 | Prediction only |
| Peptic esophagitis | 89.39% | L4 | Diagnostic staining (Lugol) only |
| Lacrimal gland neoplasm | 89.35% | L3 | Evidence is mostly radioiodine toxicity. I-125 brachytherapy is a different technique. |

Keratitis is the most credible alternative. Povidone-iodine is a broad-spectrum antiseptic that acts on bacteria, fungi, viruses and Acanthamoeba through oxidative disruption of microbial proteins and membranes, which gives a direct mechanistic rationale. The L1 grade rests on trial phase alone. The Phase 3 trial was terminated early with 78 participants, so it should be read cautiously.

## Clinical Trial Evidence

No clinical trials are registered for Sjogren syndrome. Currently no related clinical trials registered for the top-ranked prediction.

For reference, the trials below relate to **keratitis**, the best-supported alternative prediction. They test povidone-iodine, not elemental iodine.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00516399](https://clinicaltrials.gov/study/NCT00516399) | Phase 3 | Terminated | 78 | 1.25% povidone-iodine ophthalmic solution vs an antifungal antibiotic in small to medium fungal corneal ulcers. Terminated early, so power is limited. |
| [NCT00386958](https://clinicaltrials.gov/study/NCT00386958) | Phase 2 | Completed | 172 | Povidone-iodine as an inexpensive treatment for bacterial corneal ulcers |
| [NCT03484507](https://clinicaltrials.gov/study/NCT03484507) | Phase 2 | Completed | 49 | Acanthamoeba keratitis pilot. Chlorhexidine alone vs chlorhexidine plus povidone-iodine, then re-randomisation to corticosteroid timing. Iodine's contribution needs checking. |

## Literature Evidence

No publication shows a therapeutic benefit of iodine in Sjogren syndrome. The items below are the most relevant.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41516079](https://pubmed.ncbi.nlm.nih.gov/41516079/) | 2025 | In silico/Mechanistic | Int J Mol Sci | Predicted NIS epitopes; explores where Sjogren's syndrome and Hashimoto's thyroiditis converge |
| [24899999](https://pubmed.ncbi.nlm.nih.gov/24899999/) | 2011 | Cohort | Nucl Med Mol Imaging | Salivary gland scintigraphy in Sjogren's patients and in thyroid cancer patients after radioiodine |
| [35817018](https://pubmed.ncbi.nlm.nih.gov/35817018/) | 2023 | Case report/Review | ORL | Sialendoscopy for chronic sialadenitis from Sjogren's syndrome and radioiodine therapy |
| [7485204](https://pubmed.ncbi.nlm.nih.gov/7485204/) | 1995 | Cohort | Am J Med | Prevalence of autoimmune thyroid disease in primary Sjogren's syndrome |
| [28059621](https://pubmed.ncbi.nlm.nih.gov/28059621/) | 2017 | Review | Neuroradiol J | Imaging of sialadenitis |

Supporting literature for keratitis:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32959365](https://pubmed.ncbi.nlm.nih.gov/32959365/) | 2020 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Interventions for preventing ophthalmia neonatorum |
| [37944600](https://pubmed.ncbi.nlm.nih.gov/37944600/) | 2024 | Review | Surv Ophthalmol | Povidone-iodine as a bactericidal, fungicidal and virucidal agent in ophthalmology |
| [28984794](https://pubmed.ncbi.nlm.nih.gov/28984794/) | 2018 | Review | Curr Opin Ophthalmol | Use of povidone-iodine in ophthalmology, including endophthalmitis prophylaxis |
| [12605049](https://pubmed.ncbi.nlm.nih.gov/12605049/) | 2003 | Animal/Experimental | Cornea | Polyhexamethylene biguanide and povidone-iodine in experimental Aspergillus keratitis |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 285B | Not available | Not available | Not available |

The data compiled for this report list one valid single-ingredient licence. Product name, dosage form and approved indication are not available.

## Safety Considerations

- **Drug Interactions** (all moderate severity): Iodide I-131, Iodide I-123 and lithium carbonate.
- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not product label text): thyroid conditions (hypothyroidism, myxedema, congenital hypothyroidism, Hashimoto thyroiditis), kidney disease, liver disease, gallbladder disease, epilepsy, blood disorders (thrombocytopenia, neutropenia, agranulocytosis), respiratory conditions (bronchitis, respiratory failure, pulmonary tuberculosis), cardiac conduction disorders (atrioventricular block, atrioventricular dissociation, heart block), pyoureter, and hypocomplementemic urticarial vasculitis.
- **Safety signals in the literature**: radioiodine-related salivary and lacrimal gland dysfunction, fetal thyroid hyperplasia after iodinated contrast, and acne exacerbation with systemic iodine.

Please refer to the TGA-approved Product Information (PI) for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
For Sjogren syndrome, the prediction rests on model output alone. The literature shows harms, diagnostic uses and disease co-occurrence, with no evidence of benefit. The one direction with trial evidence, povidone-iodine for infectious keratitis, is better framed as a separate research question than as an iodine repurposing recommendation.

**To proceed, the following is needed:**
- The approved indication, product details and PI from the TGA record for the ARTG entry, to establish the original indication and safety profile
- Mechanism of action data
- If pursuing keratitis: published results of the Phase 3 and Phase 2 povidone-iodine trials, and a corneal toxicity assessment
- Confirmation of which iodine form (elemental, povidone-iodine or radioisotope) the prediction refers to
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

