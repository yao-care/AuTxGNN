---
layout: default
title: Mercaptopurine
parent: Model Prediction Only (L5)
nav_order: 459
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Mercaptopurine: predicted new indication Myeloid leukaemia (evidence level L5). Approved use: Acute lymphoblastic leukaemia (the approved indication text for the A…"
monitor_inn: "Mercaptopurine"
predicted_indications: ["myeloid leukemia", "pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma", "chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation", "pulmonary blastoma", "Hodgkins lymphoma", "primary pulmonary lymphoma", "small cell lung carcinoma", "well-differentiated fetal adenocarcinoma of the lung"]
---

# Mercaptopurine
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

## Mercaptopurine: From Acute Lymphoblastic Leukaemia to Myeloid Leukaemia
{: .text-alpha }

## One-Sentence Summary

Mercaptopurine is a purine antimetabolite originally used to treat acute lymphoblastic leukaemia (ALL).
The TxGNN model predicts it may be effective for **myeloid leukaemia**,
with **15 registered clinical trials** and **20 publications** retrieved. However, mercaptopurine is mostly a component of multi-agent regimens in these trials, so direct evidence of its own efficacy in myeloid disease is limited.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute lymphoblastic leukaemia (the approved indication text for the Australian listing was not available) |
| Predicted New Indication | Myeloid leukaemia |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L2 (as scored for this prediction; see note below) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold (research question) |

**Note on the evidence level and decision:** The Phase 3 trials listed for myeloid leukaemia are multi-agent protocols, and mercaptopurine's contribution cannot be isolated from the available information. I have therefore treated this as a research question rather than a candidate ready to proceed.

Other predictions in the data compiled for this report:
- **Acute lymphoblastic leukaemia** and **precursor lymphoblastic lymphoma/leukaemia** are existing label-type indications (L1, Proceed with Guardrails), so they serve as benchmarks rather than true repurposing.
- **Small cell lung carcinoma** has an L3 rating based on a 1985 Phase 2 study, plus preclinical work. Hold.
- **Hodgkin lymphoma** (L4), **primary pulmonary lymphoma** (L4), and four other predictions (L5) have little to no supporting evidence. Hold.

## Why is This Prediction Reasonable?

Mercaptopurine is a purine antimetabolite. Its thioguanine nucleotide (TGN) metabolites are incorporated into DNA and RNA and inhibit de novo purine synthesis, so it acts against rapidly dividing leukaemic cells. Detailed mechanism of action data was not available from the original source, so this description draws on the mechanistic summary and the literature retrieved for this report.

ALL and myeloid leukaemia are both malignancies of blood-forming cells, and antimetabolite chemotherapy is plausible in both. In myeloid disease, mercaptopurine appears mainly within combination regimens. Examples are oral 6-MP/methotrexate maintenance in AML patients ineligible for transplant (a Korean cohort study) and maintenance in acute promyelocytic leukaemia (APL). Its role in these regimens is hard to separate from the other drugs.

The trial list should be read with that caution. Several of the Phase 3 trials (for example NCT02521493, NCT00492856, NCT00136084, NCT02688140, NCT00002701) are multi-agent protocols where mercaptopurine's role is unclear from the titles. These are not direct evidence of its efficacy.

## Clinical Trial Evidence

The table lists the trials most relevant to mercaptopurine. Relevance grades come from the review of each trial's description.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00003934](https://clinicaltrials.gov/study/NCT00003934) | Phase 3 | Completed | 420 | APL: maintenance with intermittent tretinoin vs tretinoin plus mercaptopurine and methotrexate; also tests arsenic trioxide in consolidation. Mercaptopurine is a named arm component. |
| [NCT06199557](https://clinicaltrials.gov/study/NCT06199557) | Phase 1/2 | Recruiting | 48 | 6-mercaptopurine plus valproic acid (or hydroxyurea plus valproic acid) in AML or high-risk MDS unfit for standard therapy. Safety and preliminary efficacy. |
| [NCT05506332](https://clinicaltrials.gov/study/NCT05506332) | Phase 1 | Recruiting | 10 | Venetoclax with 6-mercaptopurine in relapsed/refractory AML (ApoAML). |
| [NCT00492856](https://clinicaltrials.gov/study/NCT00492856) | Phase 3 | Completed | 105 | S0521: maintenance vs observation in low/intermediate-risk APL. Mercaptopurine's role not confirmed from the title. |
| [NCT00002701](https://clinicaltrials.gov/study/NCT00002701) | Phase 3 | Unknown | 750 | ATRA with idarubicin and intensive consolidation, then randomised maintenance in APL. The specific arm needs confirming. |
| [NCT02688140](https://clinicaltrials.gov/study/NCT02688140) | Phase 3 | Completed | 133 | ATO + ATRA + idarubicin vs AIDA in high-risk APL. Mercaptopurine not the focus. |
| [NCT02521493](https://clinicaltrials.gov/study/NCT02521493) | Phase 3 | Active, not recruiting | 280 | Risk-stratified AML therapy in Down syndrome. Mercaptopurine's contribution unclear. |
| [NCT00136084](https://clinicaltrials.gov/study/NCT00136084) | Phase 3 | Completed | 238 | AML/MDS: two cytarabine dose regimens. Mercaptopurine's role unspecified. |
| [NCT00551460](https://clinicaltrials.gov/study/NCT00551460) | Phase 2 | Completed | 78 | ATRA, arsenic trioxide and gemtuzumab in high-risk APL. Mercaptopurine involvement unclear. |
| [NCT00482833](https://clinicaltrials.gov/study/NCT00482833) | Phase 3 | Completed | 276 | ATO + ATRA vs AIDA in non-high-risk APL. Open label, randomised. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26425037](https://pubmed.ncbi.nlm.nih.gov/26425037/) | 2015 | Cohort | J Korean Med Sci | Oral 6-MP and methotrexate maintenance for 2 years in AML patients ineligible for transplant, after first complete remission. |
| [27275453](https://pubmed.ncbi.nlm.nih.gov/27275453/) | 2016 | Prospective pilot | South Asian J Cancer | Metronomic oral 6-MP as palliative therapy in elderly AML. |
| [32459546](https://pubmed.ncbi.nlm.nih.gov/32459546/) | 2020 | Retrospective | Pediatr Hematol Oncol | Sequential cytarabine and 6-MP in juvenile myelomonocytic leukaemia. |
| [38828002](https://pubmed.ncbi.nlm.nih.gov/38828002/) | 2024 | Cohort | Ther Adv Hematol | Intensive chemotherapy with dual induction and ALL-like consolidation for childhood AML (multicentre, China). |
| [22715121](https://pubmed.ncbi.nlm.nih.gov/22715121/) | 2012 | Phase 2 cohort | Blood | ATRA, idarubicin and arsenic trioxide in APL (APML4). |
| [12057059](https://pubmed.ncbi.nlm.nih.gov/12057059/) | 2000 | Review | Curr Treat Options Oncol | APL treatment overview: ATRA is essential to induction. |
| [2676034](https://pubmed.ncbi.nlm.nih.gov/2676034/) | 1989 | Review | Blood Rev | Purine metabolism as a target in leukaemia chemotherapy, including 6-MP. |
| [33183436](https://pubmed.ncbi.nlm.nih.gov/33183436/) | 2021 | Review | J Nanosci Nanotechnol | 6-MP nanomedicine for leukaemia, addressing poor solubility and toxicity. |
| [34442422](https://pubmed.ncbi.nlm.nih.gov/34442422/) | 2021 | Review | J Pers Med | NUDT15 polymorphisms and thiopurine toxicity. |
| [3513537](https://pubmed.ncbi.nlm.nih.gov/3513537/) | 1986 | Clinical study | Am J Clin Oncol | Hydroxyurea with 6-MP in chronic granulocytic leukaemia. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10214N | Allmercap | Oral suspension containing mercaptopurine monohydrate 20 mg per mL, 100 mL | Not available in the compiled data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine antimetabolite) |
| Myelosuppression Risk | High. Neutropenia, leukopenia, thrombocytopenia and anaemia are listed among the contraindicated conditions in the knowledge graph. Genetic variation in TPMT and NUDT15 strongly affects risk. |
| Emetogenicity Classification | Please refer to the Product Information (PI) |
| Monitoring Items | Full blood count with differential, liver function, renal function; TPMT/NUDT15 genotyping before treatment; metabolite monitoring where used |
| Handling Protection | Follow local cytotoxic drug handling requirements. Please refer to the PI. |

## Safety Considerations

No label-based warnings or contraindications were available. The following come from the knowledge graph and drug interaction databases, not from the Australian label.

- **Conditions flagged in the knowledge graph as contraindications:** kidney disease, liver disease, pancreatitis, gallbladder disease, cholestasis (including benign recurrent and familial intrahepatic forms), hyperbilirubinaemia (including hereditary), Gilbert syndrome, thrombocytopenia, neutropenia, agranulocytosis, leukopenia, anaemia (including macrocytic), pyoureter, and hepatosplenic T-cell lymphoma.
- **Drug interactions:** 100 interactions were recorded. Moderate-level interactions include mesalazine, balsalazide, olsalazine, sulfasalazine and naltrexone. Levofloxacin is Minor. Others (for example allopurinol-type xanthine oxidase effects, covered in the literature) should be checked in the PI.
- **Pharmacogenomics:** The retrieved literature links TPMT and NUDT15 variants to myelosuppression, and 6-MMP metabolites to hepatotoxicity.

Please refer to the TGA-approved Product Information (PI) for authoritative safety information.

## Conclusion and Next Steps

**Decision: Hold (research question)**

**Rationale:**
The predicted indication of myeloid leukaemia is supported mainly by multi-agent protocols where mercaptopurine's own contribution is unclear. The most direct evidence is small and early: a Phase 1/2 trial with valproic acid, a Phase 1 trial with venetoclax, and cohort studies of 6-MP/methotrexate maintenance. APL protocols that use mercaptopurine are increasingly arsenic-based. This does not yet justify moving forward.

**To proceed, the following is needed:**
- Confirmation of mercaptopurine's role in the multi-agent trials listed above
- Results from NCT06199557 and NCT05506332
- Australian approved indication text and the PI warnings and contraindications
- Detailed mechanism of action data
- A TPMT/NUDT15 testing and monitoring plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

