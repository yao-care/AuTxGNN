---
layout: default
title: Fludarabine
parent: 僅模型預測 (L5)
nav_order: 282
evidence_level: L5
indication_count: 10
---

# Fludarabine
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

# Fludarabine: From Haematological Malignancy Treatment to Plasma Cell Myeloma

## One-Sentence Summary

Fludarabine is a purine nucleoside antimetabolite established in haematology, most commonly used as a lymphodepletion/conditioning agent ahead of stem cell transplant or CAR-T cell therapy (the specific TGA-approved indication is not documented in this evidence pack).
The TxGNN model predicts it may be effective for **Plasma Cell Myeloma (Multiple Myeloma)**, with **50+ clinical trials** and **20 publications** currently associated with this direction — though most of this evidence reflects fludarabine's role as a conditioning agent rather than a direct anti-myeloma therapy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (drug not currently registered in Australia) |
| Predicted New Indication | Plasma Cell Myeloma (Multiple Myeloma) |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action data is not available for Fludarabine in this evidence pack (flagged as a High-severity data gap). Based on information drawn from the supporting trial and literature records, Fludarabine is a purine nucleoside analogue that resists adenosine deaminase degradation, inhibiting DNA synthesis and repair and producing strong lymphotoxicity. This property underpins its well-established role in haematology as a lymphodepleting/conditioning agent used before allogeneic stem cell transplantation and, more recently, before CAR-T cell infusion.

The overwhelming majority of clinical trials linking Fludarabine to plasma cell myeloma use it in this conditioning capacity (e.g., Fludarabine/Busulfan, Fludarabine/Melphalan, Fludarabine/Cyclophosphamide regimens) rather than as a direct anti-myeloma treatment. Only one preclinical study in this evidence pack (PMID 17976186) reports direct cytotoxic activity of Fludarabine against a myeloma cell line in vitro and in vivo, associated with reduced Akt phosphorylation. No clinical trial in the evidence pack isolates this direct anti-myeloma effect from Fludarabine's conditioning role, so the TxGNN signal is plausible mechanistically but is likely confounded by the drug's ubiquitous presence in transplant/CAR-T regimens for myeloma patients (indication confounding).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05257083](https://clinicaltrials.gov/study/NCT05257083) | Phase 3 | Active, not recruiting | 759 | DVRd + ciltacabtagene autoleucel vs DVRd + ASCT in transplant-eligible newly diagnosed MM; fludarabine used for lymphodepletion in the CAR-T arm |
| [NCT00134004](https://clinicaltrials.gov/study/NCT00134004) | Phase 2 | Completed | 210 | Non-myeloablative HLA-mismatched marrow transplant conditioning (fludarabine + cyclophosphamide) for haematologic malignancies including MM; fludarabine is conditioning, not primary anti-myeloma treatment |
| [NCT03303950](https://clinicaltrials.gov/study/NCT03303950) | Phase 2 | Terminated | 6 | Busulfan/fludarabine conditioning plus donor stem cell transplant and cyclophosphamide in MM or myelofibrosis |
| [NCT04093596](https://clinicaltrials.gov/study/NCT04093596) | Phase 1 | Active, not recruiting | 132 | ALLO-715 allogeneic anti-BCMA CAR-T following fludarabine ± cyclophosphamide lymphodepletion in relapsed/refractory MM (UNIVERSAL trial) |
| [NCT03070327](https://clinicaltrials.gov/study/NCT03070327) | Phase 1 | Active, not recruiting | 20 | BCMA-targeted CAR-T cells with or without lenalidomide in MM |
| [NCT00793572](https://clinicaltrials.gov/study/NCT00793572) | Phase 2 | Completed | 32 | Tandem autologous/non-myeloablative allogeneic transplant plus bortezomib maintenance for high-risk MM; fludarabine-based conditioning |
| [NCT01251575](https://clinicaltrials.gov/study/NCT01251575) | Phase 2 | Completed | 77 | Sirolimus/cyclosporine/MMF for GVHD prevention after non-myeloablative mismatched donor transplant, cohort includes MM patients on fludarabine-based conditioning |
| [NCT02507479](https://clinicaltrials.gov/study/NCT02507479) | Phase 2 | Unknown | 24 | Fludarabine plus IV thiotepa conditioning and allogeneic HSCT for lymphoid malignancies including MM, NHL, HL and CLL |
| [NCT00781170](https://clinicaltrials.gov/study/NCT00781170) | Phase 2 | Completed | 20 | Autologous HSCT followed by Melphalan/Fludarabine dose-reduced allograft in MM stage II/III |
| [NCT05998928](https://clinicaltrials.gov/study/NCT05998928) | Phase 2 | Recruiting | 10 | BCMA-GPRC5D CAR-T in relapsed/refractory MM after ≥3 prior therapy lines; fludarabine likely used for pre-CAR-T lymphodepletion |

No ANZCTR-registered trial identifiers were found in the supplied evidence pack for this indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7781758](https://pubmed.ncbi.nlm.nih.gov/7781758/) | 1995 | Case report/commentary | European Journal of Haematology | "Fludarabine and plasma cell leukemia" — early report directly linking fludarabine to the plasma cell malignancy spectrum |
| [17976186](https://pubmed.ncbi.nlm.nih.gov/17976186/) | 2007 | Preclinical (in vitro/in vivo) | European Journal of Haematology | Fludarabine inhibited growth of the RPMI8226 myeloma cell line in vitro and in vivo, associated with reduced Akt phosphorylation — direct mechanistic evidence |
| [38483213](https://pubmed.ncbi.nlm.nih.gov/38483213/) | 2024 | Phase 1 | American Journal of Clinical Oncology | Bortezomib + fludarabine + melphalan, with/without total marrow irradiation, as allogeneic conditioning for high-risk/relapsed MM |
| [33784005](https://pubmed.ncbi.nlm.nih.gov/33784005/) | 2021 | Phase 1 | Clinical and Translational Medicine | Anti-BCMA CAR-T therapy in relapsed/refractory MM and plasma cell leukaemia; fludarabine-based lymphodepletion regimen |
| [31378662](https://pubmed.ncbi.nlm.nih.gov/31378662/) | 2019 | Phase 2 | The Lancet Haematology | Combination anti-CD19/anti-BCMA CAR-T therapy in relapsed/refractory MM |
| [36690811](https://pubmed.ncbi.nlm.nih.gov/36690811/) | 2023 | Phase 1 | Nature Medicine | ALLO-715 allogeneic anti-BCMA CAR-T after ALLO-647 + fludarabine lymphodepletion — UNIVERSAL trial interim results |
| [38659046](https://pubmed.ncbi.nlm.nih.gov/38659046/) | 2024 | Cohort (5-year follow-up) | Journal of Hematology & Oncology | Long-term outcomes of LCAR-B38M (ciltacabtagene autoleucel) BCMA CAR-T in relapsed/refractory MM (LEGEND-2) |
| [39365257](https://pubmed.ncbi.nlm.nih.gov/39365257/) | 2025 | Cohort | Blood | Standard-of-care ciltacabtagene autoleucel outcomes in 255 relapsed/refractory MM patients; lymphodepletion regimen includes fludarabine |
| [37833271](https://pubmed.ncbi.nlm.nih.gov/37833271/) | 2023 | Cohort | Blood Cancer Journal | Bendamustine vs fludarabine/cyclophosphamide lymphodepletion prior to BCMA CAR-T in MM — direct comparison of fludarabine-based regimen effectiveness |
| [37701906](https://pubmed.ncbi.nlm.nih.gov/37701906/) | 2023 | Phase 2 pilot | Leukemia Research Reports | Split-dose busulfan/fludarabine plus post-transplant cyclophosphamide allogeneic transplant for MM and myelofibrosis |

---

## Australia Market Information

Fludarabine currently has **no ARTG entries** and is **not marketed in Australia** based on the data available in this evidence pack.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside analogue/antimetabolite) — classification inferred from mechanistic description in the evidence pack; formal DrugBank category data was not available (data gap) |
| Myelosuppression Risk | High — purine analogues characteristically cause profound and prolonged lymphopenia, with associated neutropenia and thrombocytopenia; this is the basis of its use as a lymphodepleting agent |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | FBC with differential (monitor for prolonged lymphopenia), renal function (fludarabine is renally cleared), infection surveillance given profound immunosuppression |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Detailed warnings, contraindications, and drug interaction data were not available in this evidence pack (flagged as a Blocking-severity data gap).

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The L3 evidence base is substantial in volume but structurally confounded — the overwhelming majority of trials and publications reflect Fludarabine's established role as a transplant/CAR-T conditioning agent for myeloma patients, not a direct anti-myeloma therapy. Only one preclinical study provides direct mechanistic support, and no clinical trial isolates this effect from the conditioning context, so the TxGNN signal cannot yet be distinguished from indication confounding.

**To proceed, the following is needed:**
- TGA-approved Product Information / warnings and contraindications (currently a Blocking data gap)
- Formal DrugBank mechanism-of-action and drug category data (currently a High-severity data gap)
- A clinical trial or pharmacoepidemiological study designed to isolate Fludarabine's direct anti-myeloma activity from its conditioning/lymphodepletion role
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

