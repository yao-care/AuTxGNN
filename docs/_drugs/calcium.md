---
layout: default
title: Calcium
parent: Model Prediction Only (L5)
nav_order: 125
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Calcium: predicted new indication Thrombotic disease (evidence level L5). Approved use: Not available"
---

# Calcium
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

# Calcium: From Calcium Supplementation to Thrombotic Disease

## One-Sentence Summary

Calcium (Cal-500 chewable tablets, calcium carbonate) is registered in Australia as an oral product, but no approved indication text was available in the data compiled for this report.
The TxGNN model predicts it may be effective for **thrombotic disease**, but **none of the 2 clinical trials** listed tests calcium, and the literature is mostly mechanistic or tangential.
The high score appears to reflect network proximity rather than a therapeutic rationale, so this is effectively a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication text in the ARTG entry) |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 98.25% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Calcium is an essential cofactor in the coagulation cascade and in platelet activation, so a biological link to thrombosis exists.

However, this is a physiological role and does not imply that giving calcium would treat thrombosis. Supplemental calcium could plausibly be pro-thrombotic rather than therapeutic. The high TxGNN score most likely reflects closeness in the knowledge graph, not a therapeutic rationale.

Other predictions are no stronger. For example, hemoglobinopathy and female breast carcinoma have only supportive-care or observational links (bone health, epidemiology), and several lower-ranked predictions (such as hereditary pyropoikilocytosis and exostosis) have no supporting evidence at all.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04319627](https://clinicaltrials.gov/study/NCT04319627) | Phase 3 | Recruiting | 2700 | Statins added to anticoagulation to reduce recurrent venous events in VTE. Does not test calcium. |
| [NCT03692754](https://clinicaltrials.gov/study/NCT03692754) | Phase 2/3 | Unknown | 30 | Atorvastatin in newly diagnosed immune thrombocytopenia. Does not involve calcium. |

No ANZCTR identifiers were found in the data compiled for this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7648691](https://pubmed.ncbi.nlm.nih.gov/7648691/) | 1995 | Review | Circulation | Histological classification of advanced atherosclerotic lesions (AHA committee report). Background only. |
| [30530092](https://pubmed.ncbi.nlm.nih.gov/30530092/) | 2019 | Review | Cell Calcium | Store-operated calcium entry in thrombosis and thromboinflammation. Describes calcium signalling in blood cells. |
| [38880165](https://pubmed.ncbi.nlm.nih.gov/38880165/) | 2024 | Review | Life Sciences | Calcium fluxes and mitochondrial metabolism in platelet activation. Mechanistic. |
| [39796525](https://pubmed.ncbi.nlm.nih.gov/39796525/) | 2024 | Review | Nutrients | Vitamin D deficiency and thrombotic disease risk. Not about calcium therapy. |
| [41055696](https://pubmed.ncbi.nlm.nih.gov/41055696/) | 2026 | Preclinical | Blood | STK10 regulates platelet function in arterial thrombosis (mouse model). |
| [40540747](https://pubmed.ncbi.nlm.nih.gov/40540747/) | 2025 | Preclinical | Blood | LRRC8 channels regulate platelet activation and arterial thrombosis. |
| [38869951](https://pubmed.ncbi.nlm.nih.gov/38869951/) | 2024 | Preclinical | J Clin Invest | Neutrophil glucose flux as a target in antiphospholipid syndrome. |
| [34905596](https://pubmed.ncbi.nlm.nih.gov/34905596/) | 2022 | Preclinical | Blood | Platelet ACKR3/CXCR7 and thromboinflammation. |
| [35993516](https://pubmed.ncbi.nlm.nih.gov/35993516/) | 2022 | Review | Am J Physiol Cell Physiol | Procoagulant platelets as players in thromboinflammation. |
| [30574812](https://pubmed.ncbi.nlm.nih.gov/30574812/) | 2019 | Review | Expert Opin Drug Saf | Calciphylaxis as a drug-induced adverse event. Relevant as a safety signal, not an efficacy signal. |

None of these publications shows that calcium administration prevents or treats thrombosis.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11726E | Cal-500 | Tablet, chewable, 500 mg (as carbonate) | Not stated in the data compiled for this report |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

No drug interaction records were found in the data compiled for this report. Note that thrombotic disease is a population in which any calcium-related prothrombotic concern would need careful review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). The two listed trials test statins, not calcium, and the literature describes calcium's physiological role in clotting rather than any therapeutic benefit. Supplemental calcium could even be unhelpful or harmful in thrombosis.

**To proceed, the following is needed:**
- Approved indication text and Product Information (warnings and contraindications) for the ARTG entry
- Mechanism of action data
- Evidence from studies in which calcium itself is the tested intervention in thrombotic disease, including an assessment of any prothrombotic risk
- A clear clinical rationale showing that the prediction reflects more than network proximity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

