---
layout: default
title: Tofacitinib
parent: Model Prediction Only (L5)
nav_order: 683
evidence_level: L5
indication_count: 10
---

# Tofacitinib
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

# Tofacitinib: From Rheumatoid Arthritis to Plasma Cell Myeloma (Lead Candidate Among 10 TxGNN Predictions)

## One-Sentence Summary

> Tofacitinib is a pan-JAK inhibitor (JAK1/JAK3, partial JAK2 activity) referenced in the literature as FDA-approved for rheumatoid arthritis — regulatory confirmation of the original indication is not available in this evidence pack (data gap DG001).
> TxGNN screened **10 candidate indications**; only two are supported by any literature, with **Plasma Cell Myeloma** the most credible candidate (**3 publications**, no clinical trials) and **Myeloid Leukemia** carrying a conflicting safety signal (**8 publications**, including a case report of new-onset CML during tofacitinib treatment).
> The remaining 8 candidates (rank 1–3, 6–10) have **zero supporting evidence** — the model's own rationale flags several of these as likely false positives from knowledge-graph node sparsity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed in this evidence pack (data gap DG001). Literature (PMID 29622655) describes tofacitinib as "FDA approved for rheumatoid arthritis." |
| Predicted New Indication (lead candidate) | Plasma Cell Myeloma |
| TxGNN Prediction Score (lead candidate) | 96.09% (rank 32,460) |
| Evidence Level | L4 (best-supported candidate) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

**Note:** The single highest TxGNN score among the 10 candidates (98.96%, "colobomatous microphthalmia-rhizomelic dysplasia syndrome") has **no supporting literature or trials** and is explicitly flagged by the model rationale as a probable artefact of graph sparsity, not a genuine signal. It is not used as the headline prediction.

---

## Full List of Predicted Indications

| Rank | Disease | TxGNN Score | Evidence Level | Stage | Recommendation |
|------|---------|-------------|-----------------|-------|-----------------|
| 1 | Colobomatous microphthalmia–rhizomelic dysplasia syndrome | 98.96% | L5 | S0 | Hold |
| 2 | Brachydactyly–syndactyly syndrome | 98.88% | L5 | S0 | Hold |
| 3 | Indolent plasma cell myeloma | 96.66% | L5 | S0 | Hold |
| 4 | **Plasma cell myeloma** | 96.09% | **L4** | **S1** | **Research Question** |
| 5 | Myeloid leukemia | 95.43% | L4 | S0 | Hold (safety signal) |
| 6 | Ganglioneuroblastoma | 79.55% | L5 | S0 | Hold |
| 7 | Macrothrombocytopenia with mitral valve insufficiency | 76.17% | L5 | S0 | Hold |
| 8 | Hereditary thrombocytopenia with normal platelets | 75.76% | L5 | S0 | Hold |
| 9 | Vertebral anomalies with variable endocrine and T-cell dysfunction | 75.34% | L5 | S0 | Hold |
| 10 | Retroperitoneal neoplasm | 75.26% | L5 | S0 | Hold |

Only rows 4 and 5 have any literature evidence; rows 1–3 and 6–10 are model output alone.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is flagged as a data gap in this evidence pack (DG002). Based on the literature captured, tofacitinib is a pan-JAK inhibitor (JAK1/JAK3, with partial JAK2 activity) originally developed for rheumatoid arthritis, working by blocking cytokine-driven JAK-STAT signalling in immune cells.

For **Plasma Cell Myeloma**, the mechanistic case is the strongest of the 10 candidates: myeloma cell proliferation is highly dependent on the bone marrow microenvironment's IL-6/JAK/STAT3 signalling axis. A preclinical repurposing screen (PMID 29622655) specifically identified tofacitinib as capable of reversing the growth-promoting effects of bone marrow stromal cells on myeloma cells. Two observational cohort studies (PMID 38071595, PMID 39819734) provide indirect, population-level context on JAK-inhibitor exposure and myeloma-related outcomes, but neither is a direct interventional trial.

For **Myeloid Leukemia**, the evidence is mechanistically plausible but directionally mixed. In vitro work shows JAK-STAT pathway involvement in myeloid leukemia (particularly JAK2-mutant disease) and JAK3 inhibition can enhance imatinib activity against CML cells (PMID 29458040). However, a case report (PMID 31263618) documents a patient developing chronic myeloid leukemia *while on* tofacitinib for rheumatoid arthritis — this is a potential safety signal, not supporting evidence, and must be weighed against any therapeutic hypothesis.

The other 8 candidates are rare genetic/developmental syndromes or heterogeneous tumour categories with no described JAK-STAT pathogenic link and no supporting literature; per the model's own rationale, several likely reflect knowledge-graph sparsity rather than genuine biological signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the 10 predicted indications (including Plasma Cell Myeloma and Myeloid Leukemia).

---

## Literature Evidence

### Plasma Cell Myeloma

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29622655](https://pubmed.ncbi.nlm.nih.gov/29622655/) | 2018 | Preclinical (in vitro/mechanistic) | Haematologica | Tofacitinib identified in a repurposing screen as reversing bone-marrow-microenvironment-driven growth promotion of myeloma cells |
| [39819734](https://pubmed.ncbi.nlm.nih.gov/39819734/) | 2025 | Cohort (retrospective, US Veterans) | BMC Rheumatology | Examines whether b/ts-DMARD use (including JAK inhibitors) affects multiple myeloma incidence in RA patients |
| [38071595](https://pubmed.ncbi.nlm.nih.gov/38071595/) | 2024 | Cohort/Observational (pharmacovigilance) | J Eur Acad Dermatol Venereol | FAERS study linking immunosuppressive/immunomodulatory drug exposure (incl. myeloma population) to sebaceous carcinoma reporting odds — indirect safety context, not efficacy evidence |

### Myeloid Leukemia (safety signal — not purely supportive)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29458040](https://pubmed.ncbi.nlm.nih.gov/29458040/) | 2018 | Preclinical (in vitro synergy) | Eur J Pharmacol | JAK3 inhibition enhances imatinib antitumour activity against CML leukemic stem cells |
| [26300391](https://pubmed.ncbi.nlm.nih.gov/26300391/) | 2015 | Preclinical (in vitro) | Eur J Pharmacol | JAK inhibitors alter gene expression and cell cycle in AML cell lines with JAK2 mutation |
| [34693224](https://pubmed.ncbi.nlm.nih.gov/34693224/) | 2021 | Preclinical (mechanistic) | iScience | Tofacitinib reduces SLFN11 expression in JAK-pathway gain-of-function leukemia cells |
| [38992456](https://pubmed.ncbi.nlm.nih.gov/38992456/) | 2024 | Preclinical (mechanistic) | Arch Biochem Biophys | Tofacitinib modulates aryl hydrocarbon receptor activity; discusses repurposing in CML context |
| [22777068](https://pubmed.ncbi.nlm.nih.gov/22777068/) | 2012 | Review | Z Rheumatol | General review of new kinase inhibitors including tofacitinib |
| [37352275](https://pubmed.ncbi.nlm.nih.gov/37352275/) | 2023 | Preclinical (screening methodology) | Blood Advances | Co-culture drug-screening methodology in haematological malignancies |
| [31816725](https://pubmed.ncbi.nlm.nih.gov/31816725/) | 2020 | Methodology (analytical/PK assay) | Talanta | LC-MS/MS therapeutic drug monitoring method covering tofacitinib among TKIs |
| **[31263618](https://pubmed.ncbi.nlm.nih.gov/31263618/)** | 2019 | **Case Report** | Case Rep Rheumatol | **Patient developed chronic myeloid leukemia while receiving tofacitinib for RA — safety signal, not efficacy evidence** |

---

## Australia Market Information

Tofacitinib is currently **not marketed in Australia** under this evidence pack — 0 ARTG entries were returned. No product/dosage form/indication table can be generated.

---

## Safety Considerations

No structured PI-derived safety data (key warnings, contraindications, DDI) is available in this evidence pack (all fields marked as data gaps, DG001).

> Please refer to the TGA-approved Product Information (PI) for safety information.

**Literature-derived safety signal (not from PI):** A published case report (PMID 31263618) describes chronic myeloid leukemia developing in a patient during tofacitinib treatment for rheumatoid arthritis. This does not establish causation but should be treated as a flag requiring clarification before any myeloid leukemia repurposing hypothesis is pursued.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No candidate indication has clinical trial support. The best-evidenced candidate, Plasma Cell Myeloma, sits at L4/S1 ("Research Question") — sufficient to justify further investigation but not to proceed toward clinical development. Myeloid Leukemia carries a documented adverse safety signal that must be resolved before consideration. The remaining 8 candidates have no supporting evidence and several are flagged by the model itself as likely false positives.

**To proceed, the following is needed:**
- TGA-equivalent Product Information / warnings and contraindications (DG001, Blocking)
- Confirmed mechanism of action and original approved indication from DrugBank (DG002, High)
- Prospective or at minimum larger retrospective data specifically on tofacitinib in plasma cell myeloma (current evidence is preclinical + indirect cohort only)
- Pharmacovigilance review to clarify the CML case-report signal before any myeloid leukemia hypothesis is advanced
- Re-screening or graph-density review of the L5 candidates (ranks 1–3, 6–10) before allocating further evaluation resources to them
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

