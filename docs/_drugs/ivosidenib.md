---
layout: default
title: Ivosidenib
parent: Model Prediction Only (L5)
nav_order: 401
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
monitor_inn: "Ivosidenib"
predicted_indications: ["bulbar polio"]
description: "Ivosidenib: predicted new indication Bulbar polio (evidence level L5). Approved use: Not recorded in the local data"
---

# Ivosidenib
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

## Ivosidenib: Bulbar polio
{: .text-alpha }

## One-Sentence Summary

Ivosidenib is an oral mutant IDH1 inhibitor, originally used to treat acute myeloid leukaemia (AML) and related myeloid conditions.
The TxGNN model's top-ranked prediction is **bulbar polio**, but there are **no clinical trials** and **no publications** supporting it, and the biology does not support a link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Bulbar polio |
| TxGNN Prediction Score | 0.9931 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

**Note:** The top-ranked prediction is almost certainly a TxGNN model (deep learning) artefact.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Ivosidenib is, however, a known inhibitor of mutant isocitrate dehydrogenase 1 (IDH1). Blocking the mutant enzyme lowers the oncometabolite 2-hydroxyglutarate (2-HG) and can relieve the block on cell differentiation seen in IDH1-mutant myeloid cancers.

**Bulbar polio (rank 1):** There is no plausible mechanistic link. Poliovirus infection of motor neurons does not involve IDH1 mutation. The high score of 0.9931 comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

**Other predictions in the list:**
- *Radiation-related and alkylating-agent-related AML/MDS (ranks 2–3):* Biologically plausible, because these are close relatives of the approved AML indications and IDH1 mutations occur in AML/MDS. They are likely near-duplicates of existing indications, and benefit would depend on IDH1 mutation status. No disease-specific evidence was provided.
- Supporting trials are early-phase and ongoing, and enrol mainly AML or MDS populations, so the evidence for this specific condition is indirect.
- These are likely artefacts.

---

## Clinical Trial Evidence

There are no registered trials for bulbar polio.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03471260](https://clinicaltrials.gov/study/NCT03471260) | Phase 1/2 | Recruiting | 96 | Ivosidenib plus venetoclax, with or without azacitidine, in IDH1-mutated haematologic malignancies. Examines side effects and best dose. No results provided. |
| [NCT04493164](https://clinicaltrials.gov/study/NCT04493164) | Phase 2 | Recruiting | 30 | CPX-351 plus ivosidenib in IDH1-mutated AML or high-risk MDS. Small, ongoing, no results provided. |
| [NCT04250051](https://clinicaltrials.gov/study/NCT04250051) | Phase 1 | Terminated | 2 | Ivosidenib plus FLAG chemotherapy in relapsed/refractory IDH1-mutant AML. Terminated with only 2 participants, so there is essentially no usable evidence. |

No ANZCTR identifiers were available in the data compiled.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14868M | Tibsovo | Tablet 250 mg (oral) | Not available in the data compiled |

The licence number is reproduced as it appears in the data compiled, and it should be verified against the ARTG before it is cited.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mutant IDH1 inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the Product Information (PI) warnings and precautions. Haematological parameters, liver and renal function are generally monitored in oncology practice. |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

---

## Safety Considerations

Warning and contraindication text was not available in the data compiled. Please refer to the TGA-approved Product Information (PI) for these.

**Drug Interactions:** The interaction screen returned 100 interacting drugs, and 20 are listed in the data compiled. Several are rated **Major**:
- Aprepitant
- Clarithromycin
- Dolasetron
- Palonosetron
- Granisetron
- Cisapride
- Levofloxacin

Several of these are antiemetics and QT-prolonging agents, so this is relevant to supportive care in oncology patients. Many others are rated **Moderate**, including:
- Famotidine
- Loperamide
- Bisacodyl
- Picosulfuric acid
- Polyethylene glycol with electrolytes
- Saxagliptin
- Linagliptin
- Eliglustat
- Sodium sulfate
- Castor oil
- Glycerin
- Lactitol
- Lactulose

The full list of 100 should be reviewed before any use in practice.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top prediction, bulbar polio, has no trials, no literature and no plausible mechanism, so it should not be pursued.
- Predictions that are near-duplicates of existing AML indications are better handled as label extensions than as new repurposing opportunities.

**To proceed, the following is needed:**
- Review of the TGA-approved Product Information, including the approved indication text, warnings and contraindications
- Detailed mechanism of action data
- Trial results from NCT03471260 and NCT04493164 once available
- IDH1 mutation testing strategy for any myeloid indication being considered
- Full review of the 100 flagged drug interactions, especially the Major ones
- Verification of the ARTG licence number against the register
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

