---
layout: default
title: Periciazine
parent: Model Prediction Only (L5)
nav_order: 561
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Periciazine: predicted new indication Migraine disorder (evidence level L5). Approved use: Not recorded in the ARTG data compiled for this report (the approved…"
monitor_inn: "Periciazine"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "atrophoderma vermiculata", "dysthymic disorder", "migraine with or without aura, susceptibility to", "ulerythema ophryogenesis", "sciatic neuropathy", "anxiety", "anxiety disorder", "open-angle glaucoma"]
---

# Periciazine
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

# Periciazine: From Antipsychotic Use (Original Indication Not Recorded) to Migraine Disorder

## One-Sentence Summary

Periciazine (also spelled pericyazine) is a phenothiazine antipsychotic, marketed in Australia as Neulactil 2.5 mg tablets. The TxGNN model predicts it may be effective for **migraine disorder**, but **no clinical trials and no publications** currently support this prediction. The evidence is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the ARTG data compiled for this report (the approved indication text is empty). Pharmacology reference data describe use in schizophrenia and other psychoses, and as short-term adjunctive management of severe anxiety, psychomotor agitation and violent or dangerously impulsive behaviour (UK approval) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available for periciazine in the data compiled for this report. Pharmacology reference data list the dopamine D1 receptor (DRD1) as a target, but note that no peer-reviewed data could be sourced to map a primary molecular target. Periciazine is a phenothiazine antipsychotic. Drugs in this class generally act through dopamine D2 antagonism, with additional antihistaminic, anticholinergic and alpha-adrenergic blocking activity. These class-level properties are not confirmed for periciazine specifically.

Other phenothiazines, such as chlorpromazine and prochlorperazine, are used in acute migraine, mainly to relieve headache and nausea. This gives the prediction a class-level rationale. However, no periciazine-specific data in migraine were identified, and the high TxGNN score is a computational prediction only.

The second-ranked prediction (migraine with brainstem aura) and the fifth (migraine susceptibility) are closely related to migraine and likely reflect ontology proximity rather than separate evidence. Other predictions have weaker or no plausible rationale:

| Predicted Indication | TxGNN Score | Comment |
|------|------|------|
| Migraine with brainstem aura | 99.84% | Same class-level rationale as migraine; no subtype-specific evidence |
| Atrophoderma vermiculata | 99.36% | No plausible mechanism; likely a knowledge-graph artefact |
| Dysthymic disorder | 99.25% | Theoretical relevance only; chronic phenothiazine use may worsen mood or cause sedation |
| Migraine with or without aura, susceptibility to | 99.22% | Genetic susceptibility entry, not a distinct treatable indication |
| Ulerythema ophryogenesis | 99.16% | No plausible mechanism |
| Sciatic neuropathy | 97.74% | Weak, indirect rationale (adjunct use in neuropathic pain) |
| Anxiety | 97.65% | Sedative properties; only linked paper is pharmacokinetic |
| Anxiety disorder | 97.44% | As above |
| Open-angle glaucoma | 97.16% | Anticholinergic activity may raise intraocular pressure, a safety concern |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

For the top-ranked prediction (migraine disorder), currently no related literature is available.

The only publication linked to any of the predictions relates to the anxiety predictions, and it does not assess efficacy:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35361275](https://pubmed.ncbi.nlm.nih.gov/35361275/) | 2022 | Case report / pharmacokinetic study | J Pharm Health Care Sci | Measured transfer of brotizolam, periciazine and sulpiride into cord blood and breast milk (and alprazolam into breast milk). This is a drug-transfer study, not evidence of efficacy in anxiety |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 3052P | Neulactil | Tablet 2.5 mg (oral) | Not available in the data compiled for this report |

---

## Cytotoxicity

Periciazine is not an antineoplastic drug, so this section does not apply.

---

## Safety Considerations

- **Drug Interactions**: The interaction query completed, but returned only a pharmacology entry (dopamine D1 receptor, DRD1, as a target) and no drug-drug interactions with a severity level.
- **Class-related concern**: Anticholinergic activity may raise intraocular pressure or precipitate angle-closure, which is relevant to the open-angle glaucoma prediction. Chronic phenothiazine use may also cause sedation or worsen mood.

Warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predictions are supported only by the TxGNN model (Evidence Level L5). No clinical trials or efficacy literature were found, and warnings and contraindications from the product information were not available. The migraine prediction has a plausible class-level rationale through other phenothiazines, but nothing specific to periciazine.

**To proceed, the following is needed:**
- The approved indication text and Product Information (warnings and contraindications) for Neulactil from the TGA, to allow safety screening
- Mechanism of action data for periciazine (for example, from DrugBank)
- A systematic search for periciazine data in migraine, and a comparison against established phenothiazine use in acute migraine
- Early-phase clinical evidence (for example, a pilot study in acute migraine) before any further consideration
- An assessment of whether the oral tablet form is suitable for acute migraine treatment (route compatibility is still pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

