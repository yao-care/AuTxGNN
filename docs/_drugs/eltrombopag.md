---
layout: default
title: Eltrombopag
parent: Model Prediction Only (L5)
nav_order: 245
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Eltrombopag: predicted new indication HIV infectious disease (evidence level L5). Approved use: Autoimmune thrombocytopenia"
monitor_inn: "Eltrombopag"
predicted_indications: ["HIV infectious disease", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "female breast carcinoma", "obsolete familial combined hyperlipidemia", "homozygous familial hypercholesterolemia", "AIDS", "rheumatoid arthritis", "cholecystolithiasis"]
---

# Eltrombopag
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

# Eltrombopag: From Autoimmune Thrombocytopenia to HIV Infection

## One-Sentence Summary

Eltrombopag is an oral thrombopoietin receptor (TPO-R) agonist, originally used to treat autoimmune thrombocytopenia.
The TxGNN model predicts it may be useful for **HIV infectious disease**, with **1 clinical trial** (terminated, and of uncertain HIV relevance) and **8 publications** (mainly case reports and reviews) currently supporting this direction.
The likely benefit is supportive, correcting HIV-related low platelet counts, and not antiviral.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Autoimmune thrombocytopenia (the ARTG indication text is not available in the data compiled for this report) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L1 as scored, but I would treat this as weaker (see below) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

**Note on evidence level:** The L1 rating rests on one terminated Phase 3 trial in chronic liver disease. It does not clearly enrol people with HIV, and L1 normally requires at least two completed Phase 3 RCTs. The HIV-specific evidence is really case-level (L3 at best).

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Eltrombopag is a known TPO-R agonist. By stimulating TPO-R it increases megakaryocyte development and platelet production, which is why it works in autoimmune thrombocytopenia.

People with HIV can develop low platelet counts through immune-mediated platelet destruction or bone marrow suppression, including refractory immune reconstitution thrombocytopenia. Raising platelet production is mechanistically plausible in these settings. The benefit would be correcting thrombocytopenia, not treating the virus or the underlying immunodeficiency.

One in vitro screen of FDA-approved drugs (PMID 32977702) suggests eltrombopag may modulate HIV-1 proviral transcription. This is hypothesis-generating only. One case report (PMID 25333665) also describes an immunomodulatory effect, with a shift in T-helper cell balance, in a patient with HIV-associated aplastic anaemia.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00678587](https://clinicaltrials.gov/study/NCT00678587) | Phase 3 | Terminated | 292 | Randomised, double-blind, placebo-controlled trial of eltrombopag to reduce platelet transfusion in thrombocytopenic patients with chronic liver disease undergoing elective invasive procedures. Terminated early. The record does not confirm an HIV-specific population. |

No HIV-specific clinical trials were identified, and no ANZCTR identifiers were available in the data compiled for this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25504472](https://pubmed.ncbi.nlm.nih.gov/25504472/) | 2015 | Case series | J Int Assoc Provid AIDS Care | Thrombopoietin receptor agonists (eltrombopag, romiplostim) in refractory HIV-associated immune thrombocytopenic purpura |
| [22992580](https://pubmed.ncbi.nlm.nih.gov/22992580/) | 2012 | Case report | AIDS | Eltrombopag used successfully without splenectomy in refractory HIV-related immune reconstitution thrombocytopenia |
| [25333665](https://pubmed.ncbi.nlm.nih.gov/25333665/) | 2014 | Case report | AIDS | Eltrombopag treated HIV-associated aplastic anaemia with a trilineage response and possible immunomodulatory effect |
| [19932434](https://pubmed.ncbi.nlm.nih.gov/19932434/) | 2009 | Review | Hematol Oncol Clin North Am | Chronic infections (HCV, HIV, H. pylori) as causes of persistent thrombocytopenia |
| [19245929](https://pubmed.ncbi.nlm.nih.gov/19245929/) | 2009 | Review | Semin Hematol | Therapeutic strategies for hepatitis- and other infection-related immune thrombocytopenias |
| [32977702](https://pubmed.ncbi.nlm.nih.gov/32977702/) | 2020 | In vitro screen | Viruses | FDA-approved drug library screen for modulators of HIV-1 proviral transcription |
| [24128106](https://pubmed.ncbi.nlm.nih.gov/24128106/) | 2013 | Case report | Farm Hosp | Eltrombopag for thrombocytopenia in chronic hepatitis C (two cases) |
| [28043314](https://pubmed.ncbi.nlm.nih.gov/28043314/) | 2016 | Case report | J Coll Physicians Surg Pak | Hepatitis B leading to megaloblastic anaemia and severe thrombocytopenia (not eltrombopag-specific) |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14107L | Revolade | Tablet 50 mg (as olamine) | Not available in the data compiled for this report |

---

## Safety Considerations

- **Hepatobiliary and haematological conditions flagged in the knowledge graph:** The drug-disease contraindication data link eltrombopag to liver disease, acute liver failure, hepatitis, gallbladder disease, hyperbilirubinemia (including Gilbert syndrome), kidney disease, anaemia, leukopenia, myelodysplastic syndrome, thrombocytosis, and hepatic vein thrombosis (Budd-Chiari syndrome). These come from a knowledge graph, not from label text, and should be checked against the Product Information. Hepatic monitoring is particularly relevant in people with HIV who have viral hepatitis co-infection.
- **Drug interactions:** 100 interactions were found. Most of those listed are moderate and involve polyvalent cation products (calcium, magnesium and aluminium antacids or supplements, iron, kaolin, attapulgite), which can reduce eltrombopag absorption, so dosing should be separated. Glyburide is also listed as moderate. **Eluxadoline** is the one major interaction listed. Antiretroviral interactions were not included in the data reviewed and should be checked separately.

Please refer to the TGA-approved Product Information (PI) for the full warnings and contraindications, which were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The mechanistic rationale for treating HIV-associated thrombocytopenia is sound and supported by consistent case reports and a case series. The only trial is terminated, is in a liver disease population, and does not clearly enrol people with HIV. Any use should be framed as supportive care for thrombocytopenia, not as HIV treatment.

**To proceed, the following is needed:**
- Confirmation of the population and endpoints of NCT00678587, or identification of HIV-specific trials
- Prospective studies of eltrombopag in HIV-associated thrombocytopenia
- TGA Product Information review for warnings, contraindications and approved indications (the safety screening data are currently missing)
- Detailed mechanism of action data
- Interaction review against antiretroviral regimens, and a hepatic monitoring plan, especially with hepatitis co-infection

**Other predicted indications (for context):** AIDS (same supportive rationale and same trial, so not independent evidence) is also rated Proceed with Guardrails. Breast carcinoma and rheumatoid arthritis are research questions based on preclinical work or case reports of comorbid thrombocytopenia only. The remaining predictions (simian and feline immunodeficiency, familial hyperlipidaemias, cholecystolithiasis and a neurodevelopmental disorder) have no supporting evidence and are on Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

