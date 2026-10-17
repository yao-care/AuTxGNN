---
layout: default
title: Isosorbide Dinitrate
parent: Model Prediction Only (L5)
nav_order: 394
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Isosorbide Dinitrate: predicted new indication Alopecia (evidence level L5). Approved use: Not available"
monitor_inn: "Isosorbide dinitrate"
predicted_indications: ["alopecia", "congenital hypotrichosis milia", "hypotrichosis simplex of the scalp", "pulmonary hypertension", "diffuse alopecia areata", "vascular disease", "hypertrichosis (disease)", "visceral calciphylaxis", "arterial thoracic outlet syndrome"]
---

# Isosorbide Dinitrate
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

# Isosorbide Dinitrate: From Angina (Original Use) to Alopecia

> **Note on indication selection:** The top-ranked prediction by TxGNN score is alopecia, but it has no supporting evidence. The report below presents it as the primary prediction, as the template requires. Because the evidence is concentrated in other predictions, the clinical trial and literature sections draw on the best-supported candidates (vascular disease and pulmonary hypertension), clearly labelled.

## One-Sentence Summary

Isosorbide dinitrate (ISDN) is a nitric oxide (NO) donor and vasodilator, marketed in Australia as a sublingual tablet.
The TxGNN model's top-ranked prediction is **alopecia** (score 99.99%), but there are **0 clinical trials** and **0 publications** for it.
The best-supported predictions are **vascular disease** (6 trials, 20 publications, L2) and **pulmonary hypertension** (20 publications, L3, no trials).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication text in the data compiled for this report) |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (alopecia). For comparison: vascular disease L2, pulmonary hypertension L3 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold (alopecia). For comparison: vascular disease Proceed with Guardrails, pulmonary hypertension Research Question |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, ISDN releases nitric oxide, which activates soluble guanylate cyclase, raises cGMP and relaxes vascular smooth muscle. This is the basis of its use as a vasodilator.

For **alopecia**, the link is a hypothesis only. Improved scalp microcirculation is plausible, and minoxidil (a vasodilator and potassium-channel opener) is an established hair-growth agent. However, no trials or literature support this for ISDN. The other hair-related predictions (congenital hypotrichosis milia, hypotrichosis simplex of the scalp, diffuse alopecia areata, hypertrichosis) appear to reflect graph proximity in the model rather than a mechanistic basis. Alopecia areata is autoimmune and the hereditary hair disorders are genetic, so vasodilation is not expected to address them.

The mechanistic case is much stronger for **pulmonary hypertension** (the same NO-cGMP pathway targeted by approved therapies such as riociguat and PDE5 inhibitors) and **vascular disease** (preload and afterload reduction, improved coronary collateral flow).

## Clinical Trial Evidence

**Alopecia:** Currently no related clinical trials registered.

**Vascular disease (best-supported prediction).** Whether ISDN was the studied intervention could not be verified for several trials.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02789033](https://clinicaltrials.gov/study/NCT02789033) | Phase 3 | Completed | 68 | ISDN spray plus chitosan in diabetic foot ulcers; most relevant trial (combination, topical) |
| [NCT00803634](https://clinicaltrials.gov/study/NCT00803634) | Phase 3 | Completed | 117 | Blood pressure control in acute heart failure (clevidipine vs standard IV agents); ISDN role unverified |
| [NCT00000478](https://clinicaltrials.gov/study/NCT00000478) | Phase 3 | Completed | Not reported | Asymptomatic cardiac ischaemia pilot; anti-ischaemic strategies including nitrates |
| [NCT02135315](https://clinicaltrials.gov/study/NCT02135315) | Not applicable | Completed | 1500 | Intensive vs standard BP treatment in NSTE-ACS; nitrate strategy plausible but unconfirmed |
| [NCT01513070](https://clinicaltrials.gov/study/NCT01513070) | Phase 4 | Completed | 120 | Traditional blood-quickening formula vs ISDN in moderate coronary stenosis (angina, plaque, cardiac outcomes) |
| [NCT03011775](https://clinicaltrials.gov/study/NCT03011775) | Phase 4 | Completed | 43 | Pioglitazone and atherosclerosis in coronary disease; ISDN likely not the studied intervention |

No ANZCTR identifiers were available in the data compiled for this report.

## Literature Evidence

**Alopecia:** Currently no related literature available.

**Pulmonary hypertension (selected from 20 publications):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39164577](https://pubmed.ncbi.nlm.nih.gov/39164577/) | 2025 | Clinical study | Heart Vessels | Bolus ISDN effects on mean pulmonary arterial pressure and BP in PH with cardiopulmonary comorbidities |
| [373940](https://pubmed.ncbi.nlm.nih.gov/373940/) | 1979 | Randomised, double-blind hemodynamic study | Clin Pharmacol Ther | Oral ISDN vs placebo in COPD with pulmonary hypertension (18 patients) |
| [6423015](https://pubmed.ncbi.nlm.nih.gov/6423015/) | 1984 | Hemodynamic study | Bull Eur Physiopathol Respir | Sublingual ISDN and nitroglycerin lowered pulmonary pressure in COPD; only nitroglycerin reduced pulmonary vascular resistance |
| [3409916](https://pubmed.ncbi.nlm.nih.gov/3409916/) | 1988 | Clinical study | Eur Heart J | Two years of ISDN gave sustained haemodynamic improvement in PH from interstitial lung fibrosis (18 patients) |
| [8908227](https://pubmed.ncbi.nlm.nih.gov/8908227/) | 1996 | Hemodynamic study | Acta Anaesthesiol Scand | Pulmonary vascular effects of nitroglycerin and ISDN in end-stage cardiomyopathy |
| [2868878](https://pubmed.ncbi.nlm.nih.gov/2868878/) | 1986 | Review | Drugs | Drug treatment of primary pulmonary hypertension; ISDN among vasodilators reported to help |
| [28810603](https://pubmed.ncbi.nlm.nih.gov/28810603/) | 2017 | Animal | Exp Ther Med | Intratracheal ISDN improved pulmonary pressure in a rat heart failure model |

**Vascular disease (selected from 20 publications):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1969017](https://pubmed.ncbi.nlm.nih.gov/1969017/) | 1990 | Clinical study | Lancet | ISDN and prostaglandin E1 acted synergistically on platelet deposition in peripheral vascular disease |
| [1094819](https://pubmed.ncbi.nlm.nih.gov/1094819/) | 1975 | Placebo-controlled hemodynamic study | Am Heart J | Oral ISDN vs placebo in significant coronary artery disease |
| [3925742](https://pubmed.ncbi.nlm.nih.gov/3925742/) | 1985 | Review | Am Heart J | Nitrate tolerance |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 13491C | Isordil Sublingual | Tablet 5 mg (sublingual) | Not listed in the data compiled for this report |

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text):** hypotensive disorder, hypertrophic cardiomyopathy, recent or previous myocardial infarction, stroke and cerebrovascular disorders, intracerebral haemorrhage, intracranial hypertension (pseudotumor cerebri), anaemia and haemoglobinopathy, and hyperthyroidism/thyrotoxicosis. Several of these (for example hypertrophic cardiomyopathy) are clinical cautions rather than absolute contraindications, and they should be verified against the Product Information.
- **Drug Interactions:** 100 interactions were identified. The main ones rated Moderate are bupropion, morphine, opium, dronabinol, nabilone, sapropterin, rosiglitazone, and the SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin). Omeprazole is rated Minor. The evidence trail for the prediction also flags PDE5 inhibitors as a contraindicated combination.
- **Other cautions from the literature:** nitrate tolerance, hypotension, and possible worsening of V/Q matching in lung disease.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold (alopecia)**

**Rationale:**
The alopecia prediction rests on a model score alone, with no trials, no literature and no established mechanism. Pulmonary hypertension (L3) and vascular disease (L2, Proceed with Guardrails) are better-supported directions, but the vascular evidence is mostly indirect, and ISDN's contribution is unconfirmed in most of the listed Phase 3 trials.

**To proceed, the following is needed:**
- Approved indication text and PI safety information for the Australian product (ARTG 13491C)
- Mechanism of action data
- For alopecia: preclinical or pilot evidence that ISDN affects hair growth, and a topical-route feasibility assessment (only a sublingual product is currently registered)
- For vascular disease: confirmation of ISDN's role in the Phase 3 trials, particularly NCT02789033
- For pulmonary hypertension: a controlled study with defined PH subtypes, assessing blood pressure and V/Q effects
- A hypotension and PDE5 inhibitor interaction safeguard for any repurposed use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

