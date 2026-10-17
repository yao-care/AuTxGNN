---
layout: default
title: Cabergoline
parent: Model Prediction Only (L5)
nav_order: 120
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Cabergoline: predicted new indication Pituitary cancer (evidence level L5). Approved use: Hyperprolactinaemia and prolactin-producing pituitary tumour"
monitor_inn: "Cabergoline"
predicted_indications: ["progeria-short stature-pigmented nevi syndrome", "pituitary cancer", "cerebral palsy, spastic quadriplegic", "glaucoma", "progeroid syndrome, Petty type", "psychogenic movement disorders", "kleptomania", "primary orthostatic tremor", "multiple fibroadenoma of the breast"]
---

# Cabergoline
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

# Cabergoline: From Hyperprolactinaemia to Pituitary Cancer

## One-Sentence Summary

Cabergoline is a dopamine D2 receptor agonist, originally used to treat hyperprolactinaemia and prolactin-producing pituitary tumours.
The TxGNN model predicts it may be effective for **pituitary cancer**,
with **13 clinical trials** and **20 publications** currently supporting this direction. Most of this evidence concerns pituitary adenomas rather than true carcinoma.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperprolactinaemia and prolactin-producing pituitary tumour (from the knowledge graph; no approved indication text is available in the ARTG data) |
| Predicted New Indication | Pituitary cancer (note: the top-ranked prediction, pituitary adenocarcinoma, has only indirect case-report evidence; pituitary cancer is the best-supported prediction) |
| TxGNN Prediction Score | 99.04% (pituitary cancer); 99.06% (pituitary adenocarcinoma) |
| Evidence Level | L1 (pituitary cancer; see caveat below) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, cabergoline is a D2 dopamine receptor agonist. It suppresses prolactin secretion and causes tumour shrinkage in prolactin-secreting adenomas. Laboratory studies also indicate that corticotroph adenomas express D2 receptors, which supports a rationale beyond prolactinoma.

Both the original and the predicted indications are pituitary tumours. Cabergoline is already the preferred first-line treatment for prolactinoma. Phase 3 trials have tested it in corticotroph tumours and in non-functioning pituitary adenomas. A review of cabergoline's anti-tumour effects (PMID 31597135) describes newer mechanisms of suppressed proliferation and induced cell death.

**Important caveat:** the evidence concerns pituitary *adenomas*, not true pituitary *carcinoma*. Evidence for carcinoma itself is limited, and the prediction overlaps with the existing prolactinoma use. The Evidence Level of L1 applies to the adenoma setting. Two of the Phase 3 trials are completed and directly relevant, but results are not provided in the data compiled, so the L1 rating should be treated cautiously.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00889525](https://clinicaltrials.gov/study/NCT00889525) | Phase 3 | Completed | Not reported | Oral cabergoline for Cushing disease due to corticotroph pituitary adenoma; results not provided |
| [NCT03271918](https://clinicaltrials.gov/study/NCT03271918) | Phase 3 | Completed | 140 | Randomised open-label trial of cabergoline in residual non-functioning pituitary adenoma after transsphenoidal surgery |
| [NCT02288962](https://clinicaltrials.gov/study/NCT02288962) | Phase 3 | Active, not recruiting | 60 | Randomised trial of dopamine agonist treatment in non-functioning pituitary adenomas |
| [NCT07463235](https://clinicaltrials.gov/study/NCT07463235) | Phase 3 | Recruiting | 70 | High-dose vs standard-dose cabergoline in microprolactinomas (within existing label use) |
| [NCT01620138](https://clinicaltrials.gov/study/NCT01620138) | Phase 2/3 | Completed | 21 | Somatostatin and dopamine receptor expression in non-functioning and resistant adenomas |
| [NCT07034859](https://clinicaltrials.gov/study/NCT07034859) | Phase 4 | Enrolling by invitation | 30 | Cabergoline vs no treatment for 48 weeks in non-functioning pituitary adenoma |
| [NCT01915303](https://clinicaltrials.gov/study/NCT01915303) | Phase 2 | Terminated | 68 | Pasireotide alone or with cabergoline in Cushing disease |
| [NCT00376064](https://clinicaltrials.gov/study/NCT00376064) | Phase 4 | Completed | 20 | Single-arm octreotide plus cabergoline in partially responsive acromegaly |
| [NCT03457389](https://clinicaltrials.gov/study/NCT03457389) | N/A | Unknown | 68 | Prolactin target levels during cabergoline and recurrence after withdrawal in prolactinoma |
| [NCT07045935](https://clinicaltrials.gov/study/NCT07045935) | Phase 4 | Recruiting | 60 | Glucose metabolism under dopamine agonist treatment in prolactinoma |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37097352](https://pubmed.ncbi.nlm.nih.gov/37097352/) | 2023 | Review | JAMA | Diagnosis and management of pituitary adenomas |
| [40876473](https://pubmed.ncbi.nlm.nih.gov/40876473/) | 2025 | Review | Lancet Diabetes Endocrinol | Pathogenesis, diagnosis and management of prolactin-secreting adenomas |
| [36974474](https://pubmed.ncbi.nlm.nih.gov/36974474/) | 2023 | Review | J Clin Endocrinol Metab | Approach to the patient with prolactinoma |
| [31597135](https://pubmed.ncbi.nlm.nih.gov/31597135/) | 2020 | Review | Neuroendocrinology | New anti-tumour mechanisms of cabergoline and potential broader applications |
| [38989697](https://pubmed.ncbi.nlm.nih.gov/38989697/) | 2024 | Preclinical | Neuro-oncology | Targeting HTR2B suppresses non-functioning adenoma growth and sensitises cells to cabergoline |
| [25732645](https://pubmed.ncbi.nlm.nih.gov/25732645/) | 2015 | Review | Endocrinol Metab Clin North Am | Cabergoline in pituitary tumours and valvular disorders; most studies show no significant valvulopathy |
| [35460460](https://pubmed.ncbi.nlm.nih.gov/35460460/) | 2022 | Review | J Endocrinol Invest | Dopaminergic control of Cushing syndrome |
| [28025719](https://pubmed.ncbi.nlm.nih.gov/28025719/) | 2017 | Review | Pituitary | Cabergoline in acromegaly |
| [36013562](https://pubmed.ncbi.nlm.nih.gov/36013562/) | 2022 | Review | Medicina (Kaunas) | Treatment of prolactinoma, including aggressive prolactinomas |
| [20497940](https://pubmed.ncbi.nlm.nih.gov/20497940/) | 2010 | Case report | Endocr Pract | Octreotide or cabergoline in ectopic corticotropin hypersecretion (indirect evidence for the pituitary adenocarcinoma prediction) |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13901P | Dostinex | Tablet 500 micrograms (oral) | Not available in the data compiled |

## Cytotoxicity

Cabergoline is not an antineoplastic cytotoxic drug, and this section is not applicable.

## Safety Considerations

Safety data from the product information were not available for this report, so the items below come from knowledge graph associations and interaction databases and should be verified against the TGA-approved Product Information (PI).

- **Knowledge graph contraindication associations:** liver disease, gallbladder disease, heart valve disease, pulmonary fibrosis (including post-inflammatory), IgG4-related retroperitoneal fibrosis, severe pre-eclampsia and pre-eclampsia.
- **Valvular heart disease:** monitoring is recommended. Most studies do not show a significant risk at usual doses, but the topic remains debated, particularly at the higher doses used in Parkinson's disease.
- **Impulse control disorders:** pathological gambling, hypersexuality and compulsive shopping are well-documented adverse effects, with a reported prevalence of up to 59.8% in one study. This also explains the kleptomania prediction, which is a safety signal and not a therapeutic opportunity.
- **Angle-closure glaucoma:** a case report describes bilateral acute angle-closure glaucoma in a patient taking cabergoline. This argues against the glaucoma prediction.
- **Drug interactions (60 recorded):** the major interactions are **lorcaserin** and **clarithromycin**. **Metoclopramide** is a moderate interaction. Others, such as pantoprazole, metformin, glimepiride, morphine and simvastatin, have an unclassified severity.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for pituitary adenoma subtypes only; **Hold** for all other predictions)

**Rationale:**
Several Phase 3 trials support cabergoline in corticotroph and non-functioning pituitary adenomas, and its mechanism is plausible. However, evidence for true pituitary carcinoma is limited, and results from the completed trials are not provided. The remaining predictions are Hold: pituitary adenocarcinoma (indirect case report only, L4), glaucoma (L4, safety signal), kleptomania (L4, adverse-effect association, likely harmful), and six predictions with no trials or literature (L5), including progeria-short stature-pigmented nevi syndrome, spastic quadriplegic cerebral palsy, Petty-type progeroid syndrome, psychogenic movement disorders, primary orthostatic tremor and multiple breast fibroadenoma (L5, with only an unrelated case report).

**To proceed, the following is needed:**
- Published results from the completed Phase 3 trials (NCT00889525, NCT03271918)
- Restriction to adenoma subtypes with documented D2 receptor expression
- The TGA-approved PI warnings and contraindications (a blocking data gap) and approved indication text
- Detailed mechanism of action data
- A monitoring plan for valvular heart disease (echocardiography) and screening for impulse control disorders
- Evidence specific to true pituitary carcinoma, and clarification of how the indication differs from the existing prolactinoma use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

