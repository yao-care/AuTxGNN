---
layout: default
title: Encorafenib
parent: Model Prediction Only (L5)
nav_order: 250
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Encorafenib: predicted new indication Non-cutaneous melanoma (evidence level L5). Approved use: Metastatic melanoma"
monitor_inn: "Encorafenib"
predicted_indications: ["choroideremia", "non-cutaneous melanoma", "epithelioid cell melanoma", "eyelid melanoma", "scrotum melanoma", "choroidal dystrophy, central areolar", "amelanotic skin melanoma", "superficial spreading melanoma", "lentigo maligna melanoma", "acral lentiginous melanoma (disease)"]
---

# Encorafenib
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

# Encorafenib: From Metastatic Melanoma to Non-Cutaneous Melanoma

## One-Sentence Summary

Encorafenib is an oral BRAF kinase inhibitor, originally used to treat metastatic melanoma.
The TxGNN model predicts it may be effective for **non-cutaneous melanoma** (the highest-ranked prediction with supporting evidence), with **3 clinical trials** and **1 publication** (a case report) currently supporting this direction.

Note: the top-ranked TxGNN prediction overall was choroideremia, which has no plausible mechanistic link and no supporting evidence. This report therefore focuses on the best-supported prediction, non-cutaneous melanoma. Other predictions are summarised briefly below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic melanoma |
| Predicted New Indication | Non-cutaneous melanoma (rank 2 of 10; rank 1, choroideremia, was set aside as a likely graph artefact) |
| TxGNN Prediction Score | 96.55% |
| Evidence Level | L2 (no completed Phase 2/3 RCT; the Phase 2 trial is ongoing and population-indirect, so this level is generous) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, encorafenib is a BRAF V600 kinase inhibitor, usually combined with the MEK inhibitor binimetinib to block MAPK pathway signalling. Its efficacy in BRAF V600-mutant metastatic melanoma is established.

Non-cutaneous melanomas (for example mucosal and other non-skin sites) can carry BRAF V600 mutations, although less often than cutaneous melanoma. In those cases the mechanism is directly relevant. BRAF status must be confirmed first. Uveal melanoma, for instance, is mostly driven by GNAQ/GNA11 rather than BRAF, so benefit should not be assumed.

The existing evidence is a Phase 2 trial and a broader Phase 1 trial, not a Phase 3 RCT specific to this population.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04045691](https://clinicaltrials.gov/study/NCT04045691) | N/A (non-interventional) | Recruiting | 750 | BERING-MELANOMA: real-world effectiveness, quality of life and safety of encorafenib plus binimetinib in unresectable or metastatic BRAF V600-mutant melanoma (Germany, Austria, Switzerland); mainly cutaneous melanoma |
| [NCT03235245](https://clinicaltrials.gov/study/NCT03235245) | Phase 2 | Active, not recruiting | 271 | EBIN: encorafenib plus binimetinib followed by ipilimumab plus nivolumab versus immunotherapy alone in BRAF V600-mutant melanoma; primarily cutaneous population |
| [NCT02857270](https://clinicaltrials.gov/study/NCT02857270) | Phase 1 | Completed | 210 | ERK1/2 inhibitor LY3214996 alone or combined with other agents in advanced cancer; encorafenib is only one possible partner, so relevance is low |

No ANZCTR trial identifiers were available in the data compiled for this report.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41774417](https://pubmed.ncbi.nlm.nih.gov/41774417/) | 2025 | Case report | Pigment Cell & Melanoma Research | Molecular profiling diagnosed epidermotropic metastatic melanoma presenting as eruptive primary melanomas; indirect relevance to encorafenib |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11937G | Braftovi | Capsule 50 mg (oral) | Not available in the data compiled for this report |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (BRAF kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI. Skin examination is advisable, as BRAF inhibitors can cause new cutaneous malignancies |
| Handling Protection | Please refer to the PI and local handling policies |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the DDI screen (20 shown in the data compiled for this report). Major-level interactions include:
  - Aprepitant
  - Dexamethasone
  - Clarithromycin
  - Dolasetron
  - Cisapride

  Moderate-level interactions include:
  - Famotidine
  - Metformin
  - Loperamide
  - Bisacodyl
  - Saxagliptin
  - Empagliflozin
  - Linagliptin
  - Glyburide
  - Granisetron
  - Eliglustat
  - Fidaxomicin
  - Several laxatives and bowel-preparation agents
- **Paradoxical MAPK activation signal**: Case reports describe new melanomas arising during BRAF inhibitor therapy (PMIDs 41774417, 40878071, 31804055). This supports regular skin surveillance and confirmation of BRAF status.

For warnings and contraindications, please refer to the TGA-approved Product Information (PI).

## Other Predicted Indications (Brief Summary)

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Choroideremia | 97.10% | L5 | No plausible mechanistic link; likely graph artefact. Hold |
| Epithelioid cell melanoma | 96.45% | L4 | Indirect evidence only (case report). Research question |
| Eyelid melanoma | 96.40% | L4 | Review only. Research question |
| Scrotum melanoma | 96.09% | L5 | No trials or literature. Hold |
| Choroidal dystrophy, central areolar | 96.07% | L5 | No plausible mechanistic link. Hold |
| Amelanotic skin melanoma | 95.59% | L4 | One case report with a durable response to encorafenib plus binimetinib. Research question |
| Superficial spreading melanoma | 95.59% | L4 | Largely covered by the existing indication. Case reports raise a safety signal. Research question |
| Lentigo maligna melanoma | 95.59% | L5 | Lower BRAF V600 rate; no evidence. Hold |
| Acral lentiginous melanoma | 95.59% | L2 | Randomised Phase 2 [NCT04511013](https://clinicaltrials.gov/study/NCT04511013) (n=112, recruiting) in BRAF V600-mutant melanoma with brain metastases; not subtype-specific |

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for non-cutaneous melanoma, restricted to BRAF V600-mutant disease)

**Rationale:**
The mechanism is directly relevant where BRAF V600 is mutated, and the ongoing Phase 2 and real-world studies support the regimen's feasibility. However, none of the studies is specific to non-cutaneous melanoma, and the one literature item is a case report. Evidence is therefore indirect and no completed Phase 2/3 RCT supports this population.

**To proceed, the following is needed:**
- Confirmation of BRAF V600 status in each patient before consideration
- Subtype-specific efficacy data in non-cutaneous melanoma (mucosal and other sites)
- Mechanism of action data from DrugBank
- TGA-approved PI warnings and contraindications, which are currently missing and block formal safety screening
- A DDI management plan, particularly for the Major-level interactions
- A skin surveillance plan for new cutaneous lesions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

