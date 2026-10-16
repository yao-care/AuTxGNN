---
layout: default
title: Atazanavir
parent: Model Prediction Only (L5)
nav_order: 64
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Atazanavir: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV infectious disease"
---

# Atazanavir
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

# Atazanavir: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Atazanavir is an HIV protease inhibitor, originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome** (score 99.98%), but **no clinical trials and no publications** support this prediction.
It is a model-only signal and should be treated as a hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease; AIDS (the ARTG entry in the compiled data has no indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on known information, atazanavir belongs to the HIV protease inhibitor class. Its efficacy in HIV infection is established, and mechanistically it may be applicable to related lentivirus infections.

Feline immunodeficiency virus (FIV) is a lentivirus related to HIV-1 and encodes its own protease. The high prediction score most likely reflects similarity to the HIV indication. However, FIV protease differs from HIV-1 protease in substrate specificity and inhibitor sensitivity, so atazanavir activity against it has not been established.

This is also a veterinary condition. It is not a human indication that could be assessed for TGA registration or PBS listing.

**Other predictions in the ranked list (for context):**
- **Simian immunodeficiency virus infection** (score 99.98%, L4): Plausible mechanism, since SIV protease is broadly susceptible to HIV protease inhibitors. The only publication is a macaque study of combination antiretroviral therapy (PMID 20497048), which does not isolate atazanavir and has no direct clinical relevance.
- **Congenital HIV** (score 99.71%, L3): Essentially the same disease as the approved indication, applied to perinatal settings. The literature covers safety and pharmacokinetics in pregnancy, not efficacy.
- **AIDS related complex** (score 99.71%, L3): A historical term for symptomatic HIV disease, so this is a relabelling of the existing indication rather than true repurposing.
- **Other predictions** (neurodevelopmental disorder, obsolete familial combined hyperlipidaemia, prostatic fibroma, Brenner tumour, benign reproductive neoplasms, benign prostate phyllodes tumour): No plausible mechanistic link, no trials and no literature. These are likely knowledge-graph artefacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked prediction (feline acquired immunodeficiency syndrome).

For the second-ranked prediction (SIV infection), one publication was found:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20497048](https://pubmed.ncbi.nlm.nih.gov/20497048/) | 2010 | Animal study | J Infect Dis | In SIV-infected macaques, combination antiretroviral therapy reduced central nervous system viral replication and inflammation, but viral DNA persisted. The study does not isolate atazanavir. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10321F | Reyataz | Capsule 300 mg (as sulfate) | Not stated in the data compiled for this report |

## Safety Considerations

**Contraindication-related disease associations (from knowledge-graph data, not label text):**
liver failure, liver disease, gallbladder disease, hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, chronic hepatitis B and C virus infection, haemophilia, hyperbilirubinaemia (including Gilbert syndrome), nephrolithiasis, acute urate nephropathy, atrioventricular block and lactic acidosis.

**Drug Interactions:** The interaction screen returned 100 records, of which 20 were reviewed. Examples include:
- **Major:** famotidine, ranitidine, rabeprazole, omeprazole (acid-suppressing agents), loperamide, and the corticosteroids triamcinolone and budesonide.
- **Moderate:** acarbose, metformin, pioglitazone, alogliptin, albiglutide, hydrocortisone, betamethasone, alosetron, aprepitant, aluminium hydroxide and calcium carbonate.

Label-based warnings and contraindications were not available. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction rests on model output alone (L5), with no trials or publications. FIV protease sensitivity to atazanavir is unproven, and the indication is veterinary rather than human.

**To proceed, the following is needed:**
- In vitro data showing atazanavir activity against FIV protease, or SIV protease if that direction is pursued
- Mechanism of action data (MOA) from DrugBank
- Package insert warnings and contraindications, to complete safety screening
- Clarification of whether a veterinary indication is within scope, as human-relevant candidates (such as congenital HIV, for pregnancy exposure and safety) are largely extensions of the existing indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

