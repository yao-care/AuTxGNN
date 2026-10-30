---
layout: default
title: Mechlorethamine
parent: Model Prediction Only (L5)
nav_order: 451
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-30
monitor_inn: "Mechlorethamine"
predicted_indications: ["lymph node cancer", "relapsing-remitting multiple sclerosis", "follicular lymphoma"]
description: "Mechlorethamine: predicted new indication Lymph node cancer (evidence level L5). Approved use: Not recorded in the local data"
---

# Mechlorethamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Mechlorethamine: Lymph node cancer
{: .text-alpha }

## One-Sentence Summary

Mechlorethamine is a nitrogen mustard alkylating agent, originally used for mycosis fungoides (cutaneous T-cell lymphoma), Hodgkin lymphoma and non-Hodgkin lymphoma.
The TxGNN model predicts it may be effective for **lymph node cancer**, but this is largely a broader label for its existing lymphoma uses rather than a new indication.
The data compiled for this report show **no registered clinical trials** and **20 publications**, mostly historical, supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Lymph node cancer |
| TxGNN Prediction Score | 0.9943 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Mechlorethamine is a nitrogen mustard alkylating agent. Drugs of this class cross-link DNA and trigger cell death in rapidly dividing cells such as lymphoid cells. Its efficacy in Hodgkin lymphoma (as part of the MOPP regimen) and in mycosis fungoides (topical use) is long established.

"Lymph node cancer" is a broad category that overlaps heavily with the original indications. The prediction is therefore mostly a re-labelling of existing use, not a true repurposing opportunity. The retrieved literature is mainly from the 1980s to 2000s and includes randomised MOPP comparisons and cohort studies. It also includes a recent retrospective study of mechlorethamine gel as maintenance therapy in mycosis fungoides.

Other predicted indications were also screened:
- **Follicular lymphoma and lymphoid neoplasm (broad):** class-level alkylator rationale only. The evidence is indirect, such as bendamustine reviews and combination regimens. Modern care has largely moved to other regimens.
- No data were identified.
- **Relapsing-remitting multiple sclerosis, chronic lymphocytic leukaemia/small lymphocytic lymphoma subtypes, interdigitating dendritic cell sarcoma, chest wall lymphoma, and acute lymphoblastic leukaemia:** no direct evidence. The rationale is computational only, and the toxicity profile argues against use in several of these.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7509381](https://pubmed.ncbi.nlm.nih.gov/7509381/) | 1994 | RCT | J Clin Oncol | Randomised comparison of alternating MOPP/ABVD versus standard MOPP in stage IIIB and IV Hodgkin's disease |
| [3352775](https://pubmed.ncbi.nlm.nih.gov/3352775/) | 1988 | RCT/Comparative | NCI Monogr | EORTC H5 study comparing total nodal irradiation with mantle irradiation plus MOPP in stage I-II Hodgkin's disease |
| [35393251](https://pubmed.ncbi.nlm.nih.gov/35393251/) | 2022 | Cohort | Clin Lymphoma Myeloma Leuk | Single-centre retrospective study of mechlorethamine 0.016% gel as maintenance in mycosis fungoides patients in remission |
| [31894937](https://pubmed.ncbi.nlm.nih.gov/31894937/) | 2020 | Review | Am Fam Physician | Overview of lymphoma diagnosis and treatment |
| [9923777](https://pubmed.ncbi.nlm.nih.gov/9923777/) | 1999 | Cohort | Arch Dermatol | Long-term outcomes in generalised patch/plaque (T2) mycosis fungoides |
| [6809030](https://pubmed.ncbi.nlm.nih.gov/6809030/) | 1982 | Cohort | Br J Dermatol | Therapy and survival in 92 cutaneous T-cell lymphoma patients, including topical mechlorethamine |
| [2462943](https://pubmed.ncbi.nlm.nih.gov/2462943/) | 1989 | Trial series | Blood | EORTC controlled trials 1964-1987 tailoring treatment to prognostic factors in stage I-II Hodgkin's disease |
| [2354411](https://pubmed.ncbi.nlm.nih.gov/2354411/) | 1990 | Clinical series | Cancer | Radiation with or without adjuvant MOPP in lower torso stage I-II Hodgkin's disease |
| [3392562](https://pubmed.ncbi.nlm.nih.gov/3392562/) | 1988 | Clinical series | J Clin Oncol | Total skin electron beam plus chemotherapy (mechlorethamine-based) in tumour-stage mycosis fungoides, 10-year follow-up |
| [10473086](https://pubmed.ncbi.nlm.nih.gov/10473086/) | 1999 | Laboratory/mechanistic | Clin Cancer Res | O6-alkylguanine-DNA alkyltransferase in cutaneous T-cell lymphoma and implications for alkylating agent treatment |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14658L | Ledaga | Topical gel, 160 micrograms (as hydrochloride) per g, 60 g | Indication text not available in the data compiled |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (nitrogen mustard alkylating agent) |
| Myelosuppression Risk | Please refer to the Product Information (PI). Systemic mechlorethamine (as in MOPP) is myelosuppressive; the topical gel has far lower systemic exposure |
| Emetogenicity Classification | Please refer to the Product Information (PI) |
| Monitoring Items | Please refer to the PI. Haematological parameters (FBC) are relevant if systemic exposure is a concern |
| Handling Protection | Follow local cytotoxic drug handling requirements; refer to the PI for gel-specific precautions |

## Safety Considerations

- **Contraindications (knowledge graph, not label text):** The knowledge graph links mechlorethamine to thrombocytopenia, anaemia, leukopenia, neutropenia (including agranulocytosis and congenital neutropenia syndromes), blood coagulation disease, hyperuricaemia and amyloidosis. These are not confirmed label contraindications.
- **Drug Interactions:** The data compiled for this report list 100 interactions; the first 20 reviewed include:
  - **Major:** deferiprone, samarium (153Sm) lexidronam, adalimumab, baricitinib
  - **Moderate:** palifermin, strontium chloride Sr-89, mercaptopurine, roflumilast, chloramphenicol, zidovudine, aldesleukin, alefacept, alemtuzumab, anakinra, azathioprine, tetanus toxoid and anthrax vaccines
  - **Minor:** levofloxacin, warfarin
- **Literature-derived safety signals:** Mechlorethamine-containing regimens (MOPP) are associated with leukopenia and an increased risk of secondary leukaemia.

Please refer to the TGA-approved Product Information (PI) for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted "lymph node cancer" indication overlaps with mechlorethamine's established lymphoma uses and is supported by Level 3 evidence (randomised and cohort studies, mostly historical). It is not a distinct new indication. The other predicted indications lack direct evidence and are not recommended for further pursuit at this stage.

**To proceed, the following is needed:**
- The TGA Product Information for Ledaga (warnings, contraindications, approved indication wording)
- Clarification of which lymph node malignancies are in scope, as the only Australian product is a topical gel, which is not suited to nodal or systemic disease
- Mechanism of action data
- A systemic safety and handling plan if any non-topical use is considered (myelosuppression, secondary malignancy, tissue vesicant effects)
- Review of current standard of care to confirm any role compared with modern regimens
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

