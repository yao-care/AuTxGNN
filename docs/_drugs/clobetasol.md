---
layout: default
title: Clobetasol
parent: 僅模型預測 (L5)
nav_order: 117
evidence_level: L5
indication_count: 10
---

# Clobetasol
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

# Clobetasol: From Inflammatory Dermatoses to Primary Cutaneous T-Cell Lymphoma

## One-Sentence Summary

Clobetasol is a superpotent (Class I) topical corticosteroid widely used in dermatology for severe inflammatory and immune-mediated skin conditions such as psoriasis and eczema, though it is currently not registered on the Australian Register of Therapeutic Goods (ARTG).
The TxGNN model predicts it may be effective for **Primary Cutaneous T-Cell Lymphoma (CTCL)**,
with **0 registered clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Superpotent topical corticosteroid for inflammatory skin conditions (no current ARTG registration) |
| Predicted New Indication | Primary cutaneous T-cell lymphoma |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the DrugBank record for Clobetasol. Based on well-established pharmacology, Clobetasol is a superpotent glucocorticoid receptor (GR) agonist. It works by binding to intracellular glucocorticoid receptors, modulating gene transcription to broadly suppress inflammatory cytokine production and local immune cell activity in the skin. This mechanism is relevant far beyond simple inflammation.

In the context of Primary Cutaneous T-Cell Lymphoma (CTCL) — particularly Mycosis Fungoides (MF), which accounts for the majority of CTCL cases — Clobetasol's mechanism maps directly onto disease biology. GR agonism is thought to induce apoptosis in malignant T cells, suppress pro-inflammatory cytokines within the tumour microenvironment (including IL-2 and IFN-γ), and reduce the infiltration of CD4+ malignant T cells into the skin. Because early-stage MF is largely confined to the skin, topical delivery provides targeted action precisely where it is needed.

This biological rationale is firmly embedded in clinical practice: topical clobetasol is recognised as a first-line skin-directed therapy for early-stage MF in the NCCN (National Comprehensive Cancer Network) clinical guidelines. A landmark UCSF series of approximately 200 patch-stage MF patients treated with high-potency topical corticosteroids reported response rates exceeding 90%, with only minor adverse effects. This breadth of observational evidence supports the TxGNN prediction as mechanistically sound and clinically plausible, rather than purely model-driven.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Clobetasol in primary cutaneous T-cell lymphoma.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39741016](https://pubmed.ncbi.nlm.nih.gov/39741016/) | 2025 | Comparative Study | Anais brasileiros de dermatologia | One of few published head-to-head comparisons of topical treatments; directly evaluates clobetasol propionate vs bexarotene in early-stage MF, addressing a gap in the topical therapy evidence base |
| [32603400](https://pubmed.ncbi.nlm.nih.gov/32603400/) | 2020 | Retrospective Cohort | Cutis | Observational study of clobetasol propionate 0.05% cream in early-stage MF patients; confirmed clinical utility and characterised the risk profile of cutaneous adverse effects during long-term treatment |
| [14686970](https://pubmed.ncbi.nlm.nih.gov/14686970/) | 2003 | Expert Review | Dermatologic therapy | UCSF series of ~200 patch-stage MF patients treated with high-potency topical corticosteroids; response rate >90%; established topical clobetasol as first-line therapy for early MF |
| [30677799](https://pubmed.ncbi.nlm.nih.gov/30677799/) | 2018 | Review | Dermatology online journal | Review of lymphomatoid papulosis, a low-grade CTCL variant; discusses long-term prognosis and monitoring-based management consistent with recent consensus guidelines |
| [17083888](https://pubmed.ncbi.nlm.nih.gov/17083888/) | 2006 | Review | Dermatology online journal | Outlines diagnostic and therapeutic algorithms for CD30+ primary cutaneous anaplastic large T-cell lymphoma; contextualises the indolent end of the CTCL spectrum |
| [25027222](https://pubmed.ncbi.nlm.nih.gov/25027222/) | 2014 | Case Report | Nederlands tijdschrift voor geneeskunde | Hypopigmented MF in a 9-year-old girl successfully treated with clobetasol 0.05% ointment 4 days per week; demonstrates paediatric applicability |
| [28031140](https://pubmed.ncbi.nlm.nih.gov/28031140/) | 2016 | Case Report | Skinmed | Angioimmunoblastic T-cell lymphoma initially managed with clobetasol for presumed psoriasis; illustrates diagnostic challenges in CTCL and consequences of delayed diagnosis |
| [23773745](https://pubmed.ncbi.nlm.nih.gov/23773745/) | 2013 | Case Report/Review | Annales de dermatologie et de venereologie | Papular MF — a newly described incipient variant of the most common CTCL subtype; reviews current literature on clinical features and management |
| [36846176](https://pubmed.ncbi.nlm.nih.gov/36846176/) | 2023 | Case Report | Clinical case reports | MF presenting with psoriasiform plaques misdiagnosed and treated with topical steroids for 12 years; highlights the dual role of steroids as both treatment and diagnostic confounder in CTCL |
| [39803735](https://pubmed.ncbi.nlm.nih.gov/39803735/) | 2024 | Case Report | Acta dermatovenerologica Croatica | Ultra-high-frequency ultrasound used to objectively monitor chlormethine gel efficacy in MF; contextualises the evolving landscape of topical therapies for CTCL |

---

## Australia Market Information

Clobetasol is currently **not registered on the Australian Register of Therapeutic Goods (ARTG)**. There are no ARTG entries as of the data cutoff date (April 2026).

Australian clinicians wishing to access clobetasol for use in CTCL would need to do so through one of the following regulatory pathways:

- **Special Access Scheme (SAS) Category B** — for individual patients on a case-by-case basis
- **Authorised Prescriber** — for clinicians who regularly treat this patient population

Note: Clobetasol propionate 0.05% cream and ointment are commercially available in many international markets (including the US, UK, and New Zealand) under brand names such as Temovate and Dermovate, and product information from those jurisdictions may assist with local prescribing decisions pending formal TGA approval.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

> **Note for clinical use in CTCL:** Given that MF is a chronic, relapsing condition typically requiring prolonged topical therapy, clinicians should be particularly vigilant regarding known class-effect risks associated with long-term superpotent corticosteroid use — including skin atrophy, telangiectasia, hypothalamic-pituitary-adrenal (HPA) axis suppression, and secondary candidal infection. Published observational data specific to clobetasol in MF (PMID 32603400) describe a generally manageable adverse effect profile; however, formal TGA prescribing information should be consulted when available.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple observational studies, expert series, and current international clinical guidelines (NCCN) collectively support topical clobetasol as a first-line skin-directed therapy for early-stage MF, with consistently high response rates (>90% in patch-stage disease) and a well-characterised risk profile. The TxGNN prediction of 99.51% aligns with this established clinical use, making this a compelling — and arguably already evidence-supported — repurposing candidate.

**To proceed, the following is needed:**

- **Regulatory access pathway**: Identify suitable TGA mechanism (SAS Category B or Authorised Prescriber) to enable formal prescribing in Australia for this indication
- **Pharmacological documentation**: Obtain complete DrugBank MOA data to formally document the GR-agonist mechanism and support regulatory submissions
- **TGA Product Information**: Retrieve the TGA PI (or equivalent international PI) to populate formal warnings, contraindications, and precaution documentation
- **Prospective Australian data**: Establish a clinical registry or prospective observational study to capture real-world outcomes in Australian CTCL patients treated with topical clobetasol
- **Long-term safety monitoring protocol**: Develop a structured monitoring plan for HPA axis suppression, cutaneous adverse effects, and secondary infections in the context of chronic CTCL therapy
- **Health economic assessment**: Evaluate cost-effectiveness in the Australian healthcare context relative to registered alternatives (e.g., chlormethine gel, phototherapy)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

