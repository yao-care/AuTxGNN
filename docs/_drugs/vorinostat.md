---
layout: default
title: Vorinostat
parent: 僅模型預測 (L5)
nav_order: 728
evidence_level: L5
indication_count: 10
---

# Vorinostat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Vorinostat: From Cutaneous T-Cell Lymphoma to Primary Cutaneous B-Cell Lymphoma

## One-Sentence Summary

> Vorinostat (Zolinza) is a pan-histone deacetylase (HDAC) inhibitor with an established overseas indication for cutaneous T-cell lymphoma (CTCL); it is **not currently registered with the TGA** and has no ARTG entries in Australia.
> The TxGNN model predicts it may be effective for **Primary Cutaneous B-Cell Lymphoma**,
> with **8 clinical trials** and **1 publication** currently supporting this direction — largely indirect evidence drawn from related T-cell and B-cell lymphoma populations rather than trials specific to this exact disease entity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cutaneous T-cell lymphoma (CTCL) — approved overseas (US FDA, brand Zolinza); not TGA-registered |
| Predicted New Indication | Primary Cutaneous B-Cell Lymphoma |
| TxGNN Prediction Score | 99.21% |
| Evidence Level | L2 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data (structured MOA field) is not available in this evidence pack. Based on the supporting evidence collected, vorinostat is a **pan-HDAC inhibitor (Class I/II)**, and its efficacy in cutaneous T-cell lymphoma has been established overseas, forming the basis of its original approval as Zolinza.

The mechanistic rationale for repurposing centres on the fact that B-cell and T-cell lymphomas share aberrant histone deacetylation as a common epigenetic driver. HDAC inhibition can induce apoptosis and differentiation in malignant lymphocytes regardless of lineage, which supports biological plausibility for activity in B-cell lymphoma subtypes. However, the evidence pack's own reasoning is explicit that this is a **mechanistic extrapolation, not confirmation in the same disease entity** — the great majority of supporting trials and literature involve CTCL, mycosis fungoides, Sézary syndrome, mantle cell lymphoma or diffuse large B-cell lymphoma rather than primary cutaneous B-cell lymphoma specifically.

Because Vorinostat is not TGA-registered, there is no Australian regulatory record of an original approved indication to compare against; all indication information above is drawn from the global evidence base (trial descriptions and literature) rather than local licensing data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00007345](https://clinicaltrials.gov/study/NCT00007345) | Phase 2 | Completed | 131 | Depsipeptide (same HDAC-inhibitor class) in cutaneous/peripheral T-cell lymphoma; supportive class-effect evidence, not vorinostat-specific |
| [NCT00499811](https://clinicaltrials.gov/study/NCT00499811) | Phase 1 | Completed | 15 | Vorinostat PK study in solid tumours/lymphoma with hepatic dysfunction; direct vorinostat use in a lymphoma population |
| [NCT02943642](https://clinicaltrials.gov/study/NCT02943642) | Phase 2 | Unknown | 162 | Resimmune fusion protein vs oral vorinostat in mycosis fungoides; vorinostat as active comparator, not the study drug |
| [NCT00005634](https://clinicaltrials.gov/study/NCT00005634) | Phase 1 | Completed | N/A | First-in-class SAHA (vorinostat) dose-finding study in advanced solid tumours |
| [NCT01567709](https://clinicaltrials.gov/study/NCT01567709) | Phase 1 | Completed | 34 | Alisertib + vorinostat combination in Hodgkin, B-cell NHL and peripheral T-cell lymphoma |
| [NCT00045006](https://clinicaltrials.gov/study/NCT00045006) | Phase 1 | Completed | N/A | Oral SAHA (vorinostat) in advanced solid tumours and haematologic malignancies |
| [NCT01500538](https://clinicaltrials.gov/study/NCT01500538) | Phase 2 | Terminated | 1 | Vorinostat + eltrombopag pilot study in lymphoma to offset vorinostat-induced thrombocytopenia; terminated early |
| [NCT01789255](https://clinicaltrials.gov/study/NCT01789255) | Phase 2 | Completed | 12 | Vorinostat + tacrolimus/methotrexate for GVHD prevention after stem cell transplant in haematological malignancies |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21652541](https://pubmed.ncbi.nlm.nih.gov/21652541/) | 2011 | Mechanistic/Preclinical | Clinical Cancer Research | Vorinostat induces apoptosis in mantle cell lymphoma (a B-cell neoplasm) via acetylation of proapoptotic BH3-only gene promoters, providing mechanistic support for HDAC-inhibitor activity in B-cell malignancies |

---

## Australia Market Information

Vorinostat is currently **not registered with the TGA** — there are no ARTG entries and no marketed product in Australia.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Histone deacetylase [HDAC] inhibitor) |
| Myelosuppression Risk | Moderate — thrombocytopenia is a recognised early treatment-emergent effect (supported by NCT01500538, which paired vorinostat with eltrombopag specifically to manage this) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Full blood count (with platelets), electrolytes (including potassium/magnesium), renal and liver function, ECG monitoring (QT interval) |
| Handling Protection | Cytotoxic/antineoplastic drug handling precautions should be followed pending confirmation via local Product Information once registered |

---

## Safety Considerations

Vorinostat is not currently TGA-registered, so no Australian Product Information exists. Safety data in this evidence pack (key warnings, contraindications, drug interactions) were not able to be sourced. Please refer to overseas regulatory labelling (e.g., US FDA Zolinza PI) as an interim reference, pending TGA registration and local Product Information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN model gives a high prediction score (99.21%) and there is a biologically plausible shared HDAC-driven mechanism between T- and B-cell lymphomas, but almost all supporting clinical trial and literature evidence relates to CTCL, mycosis fungoides, Sézary syndrome or other lymphoma subtypes rather than primary cutaneous B-cell lymphoma specifically — this is class-effect and mechanistic extrapolation rather than direct proof of efficacy in the target disease.

**To proceed, the following is needed:**
- TGA Product Information / warnings and contraindications (currently a Blocking data gap — DG001)
- Structured mechanism of action data from DrugBank (High priority gap — DG002)
- Confirmation of any pathway to TGA registration, since Vorinostat is not currently marketed in Australia
- Trials or case series specific to primary cutaneous B-cell lymphoma (rather than T-cell lymphoma populations) to substantiate the predicted indication
- A defined safety monitoring plan (FBC, ECG/QT, electrolytes) suitable for local clinical use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

