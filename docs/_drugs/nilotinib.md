---
layout: default
title: Nilotinib
parent: Model Prediction Only (L5)
nav_order: 502
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-17
description: "Nilotinib: predicted new indication Dermatofibrosarcoma protuberans (evidence level L5). Approved use: Chronic myelogenous leukaemia, BCR-ABL1 positive"
monitor_inn: "Nilotinib"
predicted_indications: ["dermatofibrosarcoma protuberans"]
---

# Nilotinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Nilotinib: From Chronic Myelogenous Leukaemia (BCR-ABL1 Positive) to Dermatofibrosarcoma Protuberans
{: .text-alpha }

## One-Sentence Summary

Nilotinib is a kinase inhibitor originally used to treat BCR-ABL1-positive chronic myelogenous leukaemia.
The TxGNN model predicts it may be effective for **dermatofibrosarcoma protuberans (DFSP)**,
but currently only **1 review article** supports this direction, with **no registered clinical trials** for this specific disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic myelogenous leukaemia, BCR-ABL1 positive |
| Predicted New Indication | Dermatofibrosarcoma protuberans |
| TxGNN Prediction Score | 0.9931 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (7 of 7 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 7 (valid: 7) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for nilotinib: "Nilotinib is an inhibitor of the BCR-ABL kinase. Nilotinib binds to and stabilizes the inactive conformation of the kinase domain of ABL protein. In vitro, nilotinib inhibited BCR-ABL mediated proliferation of murine leukemic cell lines and human cell lines derived from patients with Ph+ CML." ([DailyMed: Cavhanza (nilotinib) prescribing information, Cycle Pharmaceuticals Ltd](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98b197ea-bca4-427e-8737-97f70a3262bc), label version 2026-07-20; accessed 2026-11-19.) Based on the known pharmacology of nilotinib, it inhibits BCR-ABL and also inhibits platelet-derived growth factor receptors (PDGFR).

DFSP is driven by the COL1A1-PDGFB gene fusion, which causes autocrine activation of PDGFRB. Because nilotinib inhibits PDGFR in addition to BCR-ABL, there is a plausible mechanistic link between its action in leukaemia and in DFSP.

However, the only supporting item is a 2018 review of small-molecule PDGFR inhibitors. Clinical evidence in DFSP relates mainly to imatinib, and no nilotinib-specific trial is listed. The prediction is therefore mechanistically reasonable but clinically unproven.

## Clinical Trial Evidence

Currently no related clinical trials registered for dermatofibrosarcoma protuberans.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02587169](https://clinicaltrials.gov/study/NCT02587169) | Phase 1/2 | Unknown | 40 | Nilotinib plus doxorubicin as neoadjuvant treatment in retroperitoneal liposarcoma and leiomyosarcoma (GEIS-27); not specific to DFSP |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Review | Pharmacological Research | Reviews small-molecule PDGFR inhibitors in neoplastic disorders, supporting the PDGFR-targeting rationale |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12858R | Tasigna | Capsule 200 mg (as hydrochloride monohydrate) | Not available in the compiled data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor) |
| Myelosuppression Risk | Medium (neutropenia, thrombocytopenia and anaemia are listed as contraindication-related conditions in the knowledge graph) |
| Emetogenicity Classification | Low |
| Monitoring Items | FBC, liver function, electrolytes (potassium, magnesium, calcium, phosphate), blood glucose, ECG (QT interval) |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

## Safety Considerations

- **Conditions flagged in the knowledge graph (not label text):** hypertension, long QT syndrome and torsades de pointes, liver disease, gallbladder disease, pancreatitis, thrombocytopenia, neutropenia, anaemia, hyperglycaemia and diabetes, hypokalaemia, hypercalcaemia, hypophosphataemia, and hyperbilirubinaemia (including Gilbert syndrome).
- **Drug Interactions:** 100 interactions were identified. Major interactions include:
  - Dexamethasone
  - Clarithromycin
  - Picosulfuric acid
  - Polyethylene glycol (3350 with electrolytes)

  Moderate interactions include acid-suppressing drugs (famotidine, ranitidine, cimetidine, omeprazole, rabeprazole), other corticosteroids (hydrocortisone, betamethasone, budesonide, triamcinolone), pioglitazone, loperamide, bupropion, aprepitant, bisacodyl and saxagliptin.
- **Literature safety signal:** A case report describes pancreatic carcinoma developing after nilotinib therapy for CML. This is a single case and does not establish causation.

Please refer to the TGA-approved Product Information (PI) for authoritative warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale (PDGFRB activation in DFSP) is strong, but the evidence consists only of a general review, with no nilotinib-specific trials in DFSP. Clinical support for PDGFR inhibition in DFSP comes from imatinib, so nilotinib's role remains a research question.

**To proceed, the following is needed:**
- Nilotinib-specific clinical data in DFSP (case series or trials), and comparison with imatinib
- Detailed mechanism of action data
- TGA Product Information warnings and contraindications, including the approved indication text for ARTG 12858R
- A cardiac safety plan (QT monitoring and interaction management) for any oncology use outside CML

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Cavhanza (nilotinib) prescribing information, Cycle Pharmaceuticals Ltd](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98b197ea-bca4-427e-8737-97f70a3262bc) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

