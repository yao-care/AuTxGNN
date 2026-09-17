---
layout: default
title: Zanubrutinib
parent: Model Prediction Only (L5)
nav_order: 730
evidence_level: L5
indication_count: 10
---

# Zanubrutinib
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

Using the drug-repurposing evaluation report template to produce this report directly from the evidence pack (no additional skill applies — this is a self-contained content-generation task with an explicit spec already in the prompt).

# Zanubrutinib: From B-Cell Malignancies to Myeloid Leukaemia

## One-Sentence Summary

> Zanubrutinib (Brukinsa) is a next-generation Bruton's Tyrosine Kinase (BTK) inhibitor whose established evidence base — reflected throughout this evidence pack's literature — is in **B-cell malignancies** (CLL/SLL, mantle cell lymphoma, Waldenström's macroglobulinaemia, marginal zone and follicular lymphoma).
> TxGNN predicts possible activity in **Myeloid Leukaemia**, but the supporting evidence in this pack is indirect: **2 clinical trials** (neither testing zanubrutinib monotherapy for myeloid leukaemia) and **9 publications**, none of which directly studies zanubrutinib in a myeloid leukaemia population.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Australia; literature in this pack indicates overseas approval for B-cell malignancies (CLL/SLL, MCL, WM, MZL, FL) |
| Predicted New Indication | Myeloid Leukaemia |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not supplied in this evidence pack (flagged as a High-severity data gap). Based on information within the supporting literature, zanubrutinib is a highly selective, next-generation BTK inhibitor, first approved in the US in November 2019 for relapsed/refractory mantle cell lymphoma, with subsequent expansion into CLL/SLL, Waldenström's macroglobulinaemia, marginal zone lymphoma and follicular lymphoma — all B-cell receptor (BCR) signalling-driven, lymphoid-lineage malignancies.

BTK is predominantly expressed in the B-lymphoid lineage rather than the myeloid lineage, so a direct mechanistic rationale for activity in myeloid leukaemia (e.g., AML, CML) is not well supported by canonical BTK biology. The high TxGNN score likely reflects knowledge-graph proximity (e.g., shared "leukaemia" disease-class connections, co-occurrence in combination trials, or general kinase-inhibitor drug-class links) rather than a validated pathway-level mechanism in myeloid disease.

Critically, the two clinical trials linked to this prediction do not provide direct evidence: NCT04477291 tests a *different* drug (CG-806/luxeptinib, a dual FLT3/BTK inhibitor) in AML/MDS, and NCT05665530 uses zanubrutinib only as a combination partner alongside a CDK9 inhibitor in broadly defined relapsed/refractory haematologic malignancies — not myeloid leukaemia specifically. None of the nine associated publications reports zanubrutinib activity in a myeloid leukaemia population; they instead document its established role in CLL/SLL, MCL and WM.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04477291](https://clinicaltrials.gov/study/NCT04477291) | Phase 1a/1b | Terminated | 45 | Tests CG-806 (luxeptinib), a *different* dual FLT3/BTK inhibitor, in relapsed/refractory AML or higher-risk MDS — does **not** evaluate zanubrutinib |
| [NCT05665530](https://clinicaltrials.gov/study/NCT05665530) | Phase 1 | Completed | 86 | Dose-escalation study of PRT2527 (CDK9 inhibitor) as monotherapy and in combination with zanubrutinib or venetoclax in relapsed/refractory haematologic malignancies broadly; zanubrutinib is a combination partner only, not the primary study agent, and the indication is not myeloid-leukaemia-specific |

**Neither trial provides direct efficacy evidence for zanubrutinib monotherapy in myeloid leukaemia.**

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39647999](https://pubmed.ncbi.nlm.nih.gov/39647999/) | 2025 | RCT (5-year follow-up) | J Clin Oncol | SEQUOIA trial: zanubrutinib vs bendamustine+rituximab in treatment-naïve CLL/SLL (not myeloid leukaemia) |
| [40334067](https://pubmed.ncbi.nlm.nih.gov/40334067/) | 2025 | Phase 2 single-arm | Blood Advances | Zanubrutinib well tolerated/effective in CLL/SLL patients intolerant of ibrutinib/acalabrutinib |
| [40829104](https://pubmed.ncbi.nlm.nih.gov/40829104/) | 2026 | Pooled analysis | Blood Advances | Pooled efficacy/safety of zanubrutinib in del(17p)/TP53-mutated CLL/SLL across SEQUOIA and ALPINE trials |
| [36400069](https://pubmed.ncbi.nlm.nih.gov/36400069/) | 2023 | Phase 2 single-arm | Lancet Haematology | Zanubrutinib in BTKi-intolerant B-cell malignancies |
| [34959482](https://pubmed.ncbi.nlm.nih.gov/34959482/) | 2021 | Review | Pharmaceutics | TKI era in chronic leukaemias — notes BCR-ABL1 (not BTK) as the driver in CML |
| [36402930](https://pubmed.ncbi.nlm.nih.gov/36402930/) | 2023 | Review | Leukemia | BTK inhibitors, including zanubrutinib, in Waldenström's macroglobulinaemia |
| [36325357](https://pubmed.ncbi.nlm.nih.gov/36325357/) | 2022 | Case report | Frontiers in Immunology | Coexisting Waldenström's macroglobulinaemia and B-cell ALL |
| [37150651](https://pubmed.ncbi.nlm.nih.gov/37150651/) | 2023 | Retrospective cohort | Clin Lymphoma Myeloma Leuk | Hepatitis B reactivation in patients receiving BTK inhibitors (ibrutinib/acalabrutinib/zanubrutinib) |
| [38288815](https://pubmed.ncbi.nlm.nih.gov/38288815/) | 2024 | Review | Anti-cancer Agents Med Chem | Synthesis review of FDA-approved anticancer drugs 2018–2021 |

**None of these publications directly studies zanubrutinib in myeloid leukaemia**; they reflect the drug's established evidence base in lymphoid B-cell malignancies.

---

## Australia Market Information

Zanubrutinib is **not currently registered on the ARTG** (0 licences, market status "not marketed"). No Australian product listing, dosage form, or approved-indication text is available in this evidence pack.

---

## Cytotoxicity

Zanubrutinib is an oral, targeted small-molecule kinase inhibitor used in the treatment of B-cell malignancies (cancer), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (BTK inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Low–Moderate (BTK inhibitors are generally less myelosuppressive than conventional cytotoxic chemotherapy; class-level neutropenia/thrombocytopenia reported, but no drug-specific toxicity data is included in this pack) |
| Emetogenicity Classification | Low (typical of oral targeted kinase inhibitors) |
| Monitoring Items | FBC (neutrophils, platelets), liver function including HBV serology (reactivation reported in BTK-inhibitor class — PMID 37150651), renal function, cardiac monitoring (class-associated arrhythmia risk) |
| Handling Protection | Standard oral oncology handling precautions; not classified as conventional cytotoxic chemotherapy — confirm against local cytotoxic drug handling policy |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information — key warnings, contraindications and drug–drug interaction data were not available in this evidence pack (flagged as a Blocking data gap).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score, no clinical trial or publication in this evidence pack directly evaluates zanubrutinib in myeloid leukaemia — the associated trials involve either a different drug or use zanubrutinib only as a combination partner in broadly defined haematologic malignancy studies. Combined with a Blocking gap in TFDA/TGA safety data and zanubrutinib's unmarketed status in Australia (0 ARTG entries), this candidate does not currently meet the bar to proceed.

**To proceed, the following is needed:**
- TGA-approved Product Information / PI (safety warnings, contraindications) — currently blocking
- Confirmed mechanism of action (DrugBank query) — currently a High-severity gap
- Preclinical or mechanistic evidence linking BTK inhibition to myeloid leukaemia biology
- Direct clinical trials evaluating zanubrutinib monotherapy in AML/CML/myeloid leukaemia patients
- Confirmation of Australian regulatory pathway/status if market entry is being considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

