---
layout: default
title: Propranolol
parent: Model Prediction Only (L5)
nav_order: 608
evidence_level: L5
indication_count: 10
---

# Propranolol
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

# Propranolol: From Hypertension and Cardiac Arrhythmias to Distal Myopathy, Tateyama Type

## One-Sentence Summary

Propranolol is a non-selective beta-blocker, originally used for hypertension, arrhythmias, hypertrophic cardiomyopathy and infantile haemangioma.
The TxGNN model predicts it may be effective for **distal myopathy, Tateyama type** (top-ranked prediction), but there are **0 clinical trials** and **0 publications** supporting this specific prediction.
Other lower-ranked predictions, particularly vascular tumours (haemangioma subtypes) and cardiomyopathy, have more supporting literature and are discussed below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, atrial fibrillation, hypertrophic cardiomyopathy, haemangioma (the Australian licence record carries no indication text; indications are drawn from the TxGNN knowledge graph) |
| Predicted New Indication | Distal myopathy, Tateyama type |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the data compiled for this report. Propranolol is a well-known non-selective beta-adrenergic blocker. Its efficacy in cardiovascular conditions and infantile haemangioma is established, but no mechanistic rationale connects beta-blockade to this rare distal myopathy.

The top-ranked prediction rests on the model score alone. No trials or publications were found, and no biological link between beta-blockade and Tateyama-type distal myopathy is evident. Beta-blockers are also listed in the knowledge graph as carrying contraindication signals for several muscle disorders (myopathy, skeletal muscle disease, familial periodic paralysis, myasthenia gravis), which makes this prediction more questionable.

Predictions further down the list are more biologically plausible:

- **Haemangioma subtypes** (intramuscular, breast epithelioid, breast capillary): propranolol is first-line therapy for infantile haemangioma, working through vasoconstriction, reduced VEGF/bFGF signalling and endothelial apoptosis. Extrapolation to other haemangioma types is by analogy only.
- **Cardiomyopathy and hypertrophic cardiomyopathy due to athletic training**: propranolol is already used in hypertrophic cardiomyopathy, but the generic term spans many causes and the evidence is mostly confined to the established hypertrophic subtype.
- **Cirrhotic cardiomyopathy**: limited and mixed evidence (see Literature Evidence).

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction (distal myopathy, Tateyama type). No clinical trials were identified for any of the ten predictions in the data compiled for this report.

## Literature Evidence

No literature is available for the top-ranked prediction. The table below shows the most relevant publications for the better-supported lower-ranked predictions, prioritised by study type. Study designs for several records could not be confirmed from the available information.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35466712](https://pubmed.ncbi.nlm.nih.gov/35466712/) | 2023 | Systematic review / meta-analysis | Ann Otol Rhinol Laryngol | Propranolol versus atenolol for infantile haemangioma; examines whether propranolol should remain the gold standard given its side effect profile |
| [23266923](https://pubmed.ncbi.nlm.nih.gov/23266923/) | 2013 | Consensus statement | Pediatrics | Guidance on initiating propranolol for infantile haemangioma, including safety monitoring and dose escalation |
| [36243426](https://pubmed.ncbi.nlm.nih.gov/36243426/) | 2022 | Review | Dermatol Clin | Systemic propranolol is a crucial element of infantile haemangioma management |
| [32662682](https://pubmed.ncbi.nlm.nih.gov/32662682/) | 2020 | Review | Expert Rev Clin Pharmacol | Propranolol is the mainstay treatment for problematic proliferating infantile haemangioma; other beta-blockers and ACE inhibitors explored |
| [34719577](https://pubmed.ncbi.nlm.nih.gov/34719577/) | 2022 | Randomised, double-blind study | Biol Pharm Bull | Propranolol gel (1% and 5%) versus placebo for infantile haemangioma over 24 weeks |
| [38738176](https://pubmed.ncbi.nlm.nih.gov/38738176/) | 2024 | Clinical study | Front Pharmacol | Propranolol may correct prolonged QT intervals in patients with cirrhosis |
| [35763518](https://pubmed.ncbi.nlm.nih.gov/35763518/) | 2022 | Clinical study | PLoS One | Blunted cardiovascular effects of beta-blockers in cirrhosis, possibly related to disease severity |
| [32446716](https://pubmed.ncbi.nlm.nih.gov/32446716/) | 2020 | Clinical study | J Hepatol | Non-selective beta-blockers may impair circulatory and renal function in refractory ascites (safety signal) |
| [6686544](https://pubmed.ncbi.nlm.nih.gov/6686544/) | 1983 | Clinical physiology study | Eur Heart J | Effects of propranolol and verapamil on diastolic stiffness in hypertrophic cardiomyopathy |
| [25962208](https://pubmed.ncbi.nlm.nih.gov/25962208/) | 2015 | Safety review | Pediatr Endocrinol Rev | Propranolol-induced hypoglycaemia in infantile haemangioma; guidance on prevention |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13386M | APO-Propranolol | Tablet containing propranolol hydrochloride 10 mg (oral) | Not available in the data compiled for this report |

## Safety Considerations

Label-based warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for full safety information.

- **Knowledge graph contraindication signals** (not label text): The knowledge graph links propranolol to a range of conditions of concern, including bronchitis, diabetes mellitus and diabetic ketoacidosis, liver and kidney disease, pancreatitis, gout, systemic lupus erythematosus, myasthenia gravis, and several muscle disorders (myopathy, skeletal muscle disease, familial periodic paralysis). These should be verified against the PI.
- **Drug interactions**: A screen returned 100 interacting drugs. The main ones in the data compiled for this report include:
  - **Major**: epinephrine
  - **Moderate**: corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), anticholinergics (atropine, hyoscyamine, methscopolamine), bupropion, morphine, cimetidine, canagliflozin, chlorpropamide, lorcaserin, calcium salts
  - **Minor**: aspirin, ascorbic acid, magnesium oxide
- **Literature-based safety signals**: Hypoglycaemia in infants treated for haemangioma (PMID 25962208), and possible impairment of circulatory and renal function in cirrhotic patients with refractory ascites (PMID 32446716).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, distal myopathy (Tateyama type), is supported only by a model score of 99.4%, with no trials, no literature and no plausible mechanism. Knowledge graph contraindication signals for muscle disease argue against it. Predictions further down the list (haemangioma subtypes, cardiomyopathy, cirrhotic cardiomyopathy) have some indirect supporting literature, and are better framed as research questions than as repurposing candidates for the Australian market.

**To proceed, the following is needed:**
- Mechanism of action data for propranolol, to assess any link to myopathy biology
- Retrieval of the TGA Product Information for warnings, contraindications and approved indications (the ARTG entry has no indication text in the data compiled)
- A focused literature search specific to Tateyama-type distal myopathy, or a shift of focus to better-supported candidates such as haemangioma subtypes
- Preclinical or case-based evidence before any clinical study is considered
- For any cirrhosis-related use, a dedicated safety assessment given the conflicting literature signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

