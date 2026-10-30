---
layout: default
title: Darunavir
parent: Model Prediction Only (L5)
nav_order: 200
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-30
description: "Darunavir: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV infectious disease"
monitor_inn: "Darunavir"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
---

# Darunavir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Darunavir: From HIV Infection to Feline Acquired Immunodeficiency Syndrome
{: .text-alpha }

## One-Sentence Summary

Darunavir is an HIV protease inhibitor originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, a veterinary condition, but **no clinical trials and no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease; AIDS (the Australian approved-indication text is not available in the data compiled for this report) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, darunavir is an HIV-1 protease inhibitor, its use in HIV infection and AIDS is established, and mechanistically it may be applicable to related lentiviral infections.

Feline immunodeficiency virus (FIV) is a lentivirus related to HIV-1. However, FIV protease differs from HIV-1 protease in substrate specificity and inhibitor sensitivity, so darunavir activity against FIV is not assured. The TxGNN score is high, but nothing in the data compiled for this report supports the prediction. It is also a veterinary indication and falls outside the scope of human clinical development.

**Other predictions reviewed.** The second-ranked prediction, simian immunodeficiency virus infection (score 0.9997), has only indirect preclinical macaque evidence (L4). The macaque studies used combination antiretroviral therapy, not darunavir alone, and the indication has no direct human repurposing value. Predictions such as familial combined hyperlipidaemia (an obsolete term, and mechanistically counterintuitive because protease inhibitors can cause dyslipidaemia) have no supporting evidence. Their scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered for feline acquired immunodeficiency syndrome.

For reference, trials found for the closer human-HIV predictions are listed below. Neither tests darunavir for the top-ranked prediction.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02503462](https://clinicaltrials.gov/study/NCT02503462) | Phase 4 | Terminated | 7 | Cobicistat vs ritonavir boosting and brain permeation of darunavir in HIV-infected people (AIDS related complex). Underpowered. |
| [NCT04340388](https://clinicaltrials.gov/study/NCT04340388) | Phase 4 | Completed | 10 | Dolutegravir switch and obesity/cardiovascular outcomes (congenital HIV). Not a darunavir efficacy trial; limited relevance. |

No ANZCTR identifiers were found in the data compiled for this report.

## Literature Evidence

Currently no related literature available for feline acquired immunodeficiency syndrome.

The closest literature, for simian immunodeficiency virus infection (preclinical macaque models), is below. These studies used combination ART rather than darunavir alone.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Preclinical animal study | PLoS Pathog | Highly intensified ART gave long-term viral suppression and restricted the viral reservoir in a simian AIDS model |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Preclinical animal study | PLoS One | Suppressive ART plus the HDAC inhibitor SAHA in SIV-infected Chinese rhesus macaques |
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | Preclinical animal study | AIDS Res Hum Retroviruses | Coformulated injectable ART regimens compared in SIV-infected rhesus macaques |
| [21505294](https://pubmed.ncbi.nlm.nih.gov/21505294/) | 2011 | Preclinical animal study | AIDS | Auranofin restricted the viral reservoir in the monkey AIDS model |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 10329P | Prezista | Tablet 600 mg (as ethanolate) | Not available in the data compiled for this report |

## Safety Considerations

Key warnings and contraindication text from the product information were not available. Please refer to the TGA-approved Product Information (PI) for these details.

- **Disease-level cautions (from the knowledge graph, not label text)**: liver failure, liver disease, cirrhosis, chronic hepatitis B or C infection, gallbladder disease, hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, hypertriglyceridaemia and haemophilia.
- **Drug Interactions**: 100 interactions were identified. The main ones listed are:
  - **Major**: cisapride.
  - **Moderate**: antidiabetic agents (acarbose, metformin, pioglitazone, alogliptin, saxagliptin, albiglutide, canagliflozin, dapagliflozin, chlorpropamide, acetohexamide); corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone); aprepitant; and clarithromycin.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is a veterinary indication with no trials or literature, and the mechanistic link is uncertain because FIV protease differs from HIV-1 protease. It offers no direct human repurposing value, and the evidence level is L5.

**To proceed, the following is needed:**
- Confirmation of whether a veterinary indication is within the intended scope. If not, redirect evaluation to a human indication.
- In vitro FIV protease inhibition data for darunavir.
- Detailed mechanism of action data (MOA).
- Product Information (PI) warnings and contraindications for Prezista, and the approved indication text for the ARTG entry.
- If a human-relevant direction is preferred, consider the CNS-focused question under AIDS related complex (darunavir brain penetration with cobicistat vs ritonavir boosting) or pregnancy pharmacokinetics under congenital HIV. Both would need properly powered studies.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

