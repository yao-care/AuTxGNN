---
layout: default
title: Pilocarpine
parent: Model Prediction Only (L5)
nav_order: 575
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Pilocarpine: predicted new indication Primary hereditary glaucoma (evidence level L5). Approved use: Open-angle glaucoma and ocular hypertension"
---

# Pilocarpine
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

# Pilocarpine: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Pilocarpine is a muscarinic eye-drop medicine, originally used to lower eye pressure in open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**, but **no clinical trials and no publications** currently support this prediction.
The evidence is model-based only, and the mechanism suggests it is unlikely to work well in this condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma and ocular hypertension (the Australian licence entry has no indication text) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not formally available in the data compiled for this report. From general pharmacology, pilocarpine is a muscarinic agonist. It contracts the ciliary muscle and increases trabecular outflow of aqueous humour, which lowers intraocular pressure.

That mechanism is plausible for glaucoma in general, which is likely why the model scored this prediction so highly. However, hereditary (congenital or developmental) glaucoma usually involves malformation of the drainage angle, and miotics are typically ineffective in that setting. The high score probably reflects the shared "glaucoma" label rather than specific evidence.

**Other predictions to note (all in the top 10):**
- **Open-angle glaucoma** (score 98.64%) and **glaucoma 1, open angle** (98.75%) are the original indication under different names. They are not true repurposing opportunities.
- **Oral candidiasis** (98.90%): pilocarpine stimulates saliva through M3 receptors and may indirectly lower candidiasis risk in people with dry mouth. It has no direct antifungal activity, and the retrieved papers describe dry mouth and candidiasis risk rather than pilocarpine treating candidiasis.
- **Burning mouth syndrome** (98.56%): pilocarpine may relieve the dry-mouth component, but no study shows benefit for the syndrome itself.
- **Osteoradionecrosis of the mandible, commissural lip fistula, oral leukoedema, chronic tic disorder, and extrapyramidal and movement disease** have no supporting studies, and the mechanistic links are weak or speculative.

## Clinical Trial Evidence

Currently no related clinical trials are registered for primary hereditary glaucoma.

For context, the following trials relate to the original indication (open-angle glaucoma). They do not support the predicted new indication.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02754570](https://clinicaltrials.gov/study/NCT02754570) | Not applicable | Completed | 27 | Day and night effects of pilocarpine added to latanoprost on eye pressure and ocular perfusion pressure |
| [NCT00803803](https://clinicaltrials.gov/study/NCT00803803) | Phase 4 | Completed | 37 | Dose-response of pilocarpine on eye pressure, and once, twice and four-times-daily dosing |
| [NCT05352854](https://clinicaltrials.gov/study/NCT05352854) | Not applicable | Unknown | 120 | Imaging of ciliary body and trabecular meshwork changes after pilocarpine in high myopia with open-angle glaucoma |
| [NCT04005079](https://clinicaltrials.gov/study/NCT04005079) | Phase 3 | Withdrawn | 0 | Pilocarpine after combined cataract and Trabectome surgery; withdrawn with no participants, so it provides no evidence |

## Literature Evidence

Currently no related literature is available for primary hereditary glaucoma.

For context, selected publications on the original indication (open-angle glaucoma):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10509848](https://pubmed.ncbi.nlm.nih.gov/10509848/) | 1999 | RCT | Clin Ther | Dorzolamide vs pilocarpine as add-on to timolol in open-angle glaucoma and ocular hypertension |
| [22972069](https://pubmed.ncbi.nlm.nih.gov/22972069/) | 2012 | Review (Cochrane) | Cochrane Database Syst Rev | Medical vs surgical interventions for open-angle glaucoma |
| [36548467](https://pubmed.ncbi.nlm.nih.gov/36548467/) | 2023 | Cohort | J Glaucoma | Outflow structure changes after pilocarpine were smaller in primary open-angle glaucoma than in healthy eyes |
| [27347646](https://pubmed.ncbi.nlm.nih.gov/27347646/) | 2016 | Imaging study | JAMA Ophthalmol | Effect of pilocarpine on the Schlemm canal in healthy and glaucomatous eyes |
| [18721251](https://pubmed.ncbi.nlm.nih.gov/18721251/) | 2008 | Comparative study | Acta Ophthalmol | Latanoprost vs pilocarpine/timolol fixed combination in open-angle glaucoma or ocular hypertension |
| [2212504](https://pubmed.ncbi.nlm.nih.gov/2212504/) | 1990 | Cohort | J Fr Ophtalmol | Timolol plus pilocarpine lowered eye pressure further than timolol alone |
| [7705213](https://pubmed.ncbi.nlm.nih.gov/7705213/) | 1995 | Review | Drugs | Oral pilocarpine in dry mouth (relevant to the oral predictions, not glaucoma) |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14355M | Isopto Carpine | Eye drops, pilocarpine hydrochloride 10 mg/mL, 15 mL | Not stated in the data compiled for this report |

## Safety Considerations

**Contraindications flagged in the knowledge graph** (these come from graph relationships, not from product label text):
- Eye: angle-closure (closed-angle) glaucoma, uveitis, iritis, iridocyclitis, keratitis, keratoconjunctivitis, retinal detachment
- Lung: asthma, chronic obstructive pulmonary disease (including severe early-onset), other bronchial disease
- Kidney and urinary: nephrolithiasis (including SLC26A1-related susceptibility), acute urate nephropathy
- Liver and biliary: liver failure, cholelithiasis, cholecystolithiasis, choledocholithiasis, cholecystitis, biliary tract disease, obstructive jaundice

**Drug Interactions:** The interaction search returned 100 records. The main ones are:
- **Moderate (additive or opposing anticholinergic effects):** hyoscyamine, atropine (including ophthalmic), glycopyrronium (including topical), clidinium, dicyclomine, mepenzolate, methscopolamine, propantheline, scopolamine (including ophthalmic), trospium
- **Severity unknown:** pantoprazole, omeprazole, lansoprazole, clotrimazole, morphine, metformin, epinephrine

Please refer to the TGA-approved Product Information (PI) for authoritative warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction for primary hereditary glaucoma rests on the model score alone, with no trials or publications. The mechanism also argues against it, because miotics are usually ineffective when the drainage angle is malformed.
- Several knowledge-graph contraindications (such as angle-closure glaucoma, asthma and COPD) would also need to be managed.

**To proceed, the following is needed:**
- Detailed mechanism of action data
- TGA Product Information warnings and contraindications for Isopto Carpine, along with its approved indication text
- Specialist ophthalmology review of whether pilocarpine has any role in developmental glaucoma
- Any clinical or case-series evidence in hereditary or congenital glaucoma before further evaluation

**Other directions worth noting:**
- Of the other top predictions, **oral candidiasis** and **burning mouth syndrome** are the most biologically plausible. Both work only indirectly, through saliva stimulation in dry mouth, and would be better framed as research questions about xerostomia-related outcomes.
- Open-angle glaucoma is the existing indication. Its evidence in this dataset is limited (Level L3), with no completed Phase 3 trial, though the drug is long established for this use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

