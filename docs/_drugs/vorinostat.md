---
layout: default
title: Vorinostat
parent: Model Prediction Only (L5)
nav_order: 785
evidence_level: L5
indication_count: 10
---

# Vorinostat
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

# Vorinostat: From Cutaneous T-Cell Lymphoma to Primary Cutaneous B-Cell Lymphoma

## One-Sentence Summary

Vorinostat is an oral histone deacetylase (HDAC) inhibitor, originally used to treat primary cutaneous T-cell lymphoma.
The TxGNN model predicts it may be effective for **primary cutaneous B-cell lymphoma**.
Support for this is weak: **4 early-phase clinical trials** that are not specific to this disease, and **1 preclinical publication**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Primary cutaneous T-cell lymphoma (including primary cutaneous T-cell non-Hodgkin lymphoma) |
| Predicted New Indication | Primary cutaneous B-cell lymphoma |
| TxGNN Prediction Score | 99.21% |
| Evidence Level | L4 (preclinical and mechanistic data only; no disease-specific clinical studies) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the source database. Vorinostat is nonetheless a known HDAC inhibitor. Blocking HDAC enzymes increases acetylation of histones and other proteins, which can switch on cell-death pathways and slow the growth of cancer cells.

Both the original and the predicted indications are lymphomas that arise in the skin, so a shared biology is plausible. Preclinical work in mantle cell lymphoma, an aggressive B-cell cancer, shows vorinostat can trigger apoptosis by acetylating pro-apoptotic BH3-only gene promoters. This suggests the mechanism may extend to B-cell lymphomas in general.

However, none of this evidence is specific to primary cutaneous B-cell lymphoma. The prediction is therefore a hypothesis, not an established finding.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00045006](https://clinicaltrials.gov/study/NCT00045006) | Phase 1 | Completed | Not reported | Oral vorinostat (SAHA) in advanced solid tumours and haematological malignancies. Safety and pharmacokinetic data, not specific to cutaneous B-cell lymphoma. |
| [NCT01789255](https://clinicaltrials.gov/study/NCT01789255) | Phase 2 | Completed | 12 | Pilot of vorinostat with tacrolimus and methotrexate to prevent graft-versus-host disease after stem cell transplant. Different indication. |
| [NCT01567709](https://clinicaltrials.gov/study/NCT01567709) | Phase 1 | Completed | 34 | Alisertib (Aurora A inhibitor) plus vorinostat in relapsed Hodgkin, B-cell non-Hodgkin and peripheral T-cell lymphoma. Combination design, indirect relevance. |
| [NCT00499811](https://clinicaltrials.gov/study/NCT00499811) | Phase 1 | Completed | 15 | Dose and pharmacokinetics of vorinostat in solid tumours and lymphoma with liver dysfunction. Safety and pharmacokinetics only. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21652541](https://pubmed.ncbi.nlm.nih.gov/21652541/) | 2011 | Preclinical | Clin Cancer Res | Vorinostat induced apoptosis in mantle cell lymphoma through acetylation of pro-apoptotic BH3-only gene promoters. |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11138F | Zolinza | Capsule 100 mg (oral) | Indication text not available in the data compiled for this report |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted (epigenetic) therapy: HDAC inhibitor |
| Myelosuppression Risk | Please refer to the Product Information (PI). Thrombocytopenia and anaemia appear among the conditions linked to vorinostat in the knowledge graph. |
| Emetogenicity Classification | Please refer to the Product Information (PI) |
| Monitoring Items | Full blood count (including platelets), serum glucose, electrolytes (potassium, calcium, phosphate), renal and liver function, and ECG (QT interval), consistent with the associated conditions listed below |
| Handling Protection | Follow local cytotoxic and hazardous drug handling procedures. Please refer to the PI. |

---

## Safety Considerations

The following information comes from the TxGNN knowledge graph. It is not taken from approved label text.

- **Conditions linked to contraindication or caution in the knowledge graph:** long QT syndrome (including familial), liver disease, gallbladder disease, thrombocytopenia, anaemia (including macrocytic), hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, potassium deficiency, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disorders, pulmonary embolism, and diarrhoeal disease.
- **Drug Interactions:** 61 interactions were identified. The ones listed are all rated Moderate, and most are with glucose-lowering agents. These include metformin, pioglitazone, sulfonylureas (glimepiride, glipizide, glyburide), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), GLP-1 agonists (semaglutide, dulaglutide, exenatide), DPP-4 inhibitors (alogliptin, linagliptin), acarbose and insulins. Blood glucose should be monitored closely if vorinostat is used alongside these drugs.

Please refer to the TGA-approved Product Information (PI) for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there are no disease-specific clinical studies. The only supporting material is early-phase trials in other cancers and one preclinical paper in a different B-cell lymphoma. The mechanistic argument is plausible but unproven for primary cutaneous B-cell lymphoma.

For context, other predicted indications for vorinostat have much stronger support. Sézary syndrome, a leukaemic variant of cutaneous T-cell lymphoma, is effectively a near-label use. It is backed by the pivotal Phase 2b trial (NCT00091559) and the Phase 3 MAVORIC trial (NCT01728805), in which vorinostat was the comparator. If the aim is to prioritise candidates, that indication is a more evidence-ready starting point.

**To proceed, the following is needed:**
- Disease-specific preclinical data (for example, cell-line or patient-sample studies) in primary cutaneous B-cell lymphoma
- Case series or a small exploratory trial in cutaneous B-cell lymphoma
- Detailed mechanism of action data
- The approved indication wording and the safety sections (warnings and contraindications) from the TGA Product Information for ARTG 11138F
- A monitoring plan covering platelets, glucose, electrolytes and QT interval
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

