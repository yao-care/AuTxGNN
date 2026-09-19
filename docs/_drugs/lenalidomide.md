---
layout: default
title: Lenalidomide
parent: Model Prediction Only (L5)
nav_order: 389
evidence_level: L5
indication_count: 10
---

# Lenalidomide
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

# Lenalidomide: From Multiple Myeloma/Myelodysplastic Syndrome with Deletion 5q to Myeloid Leukemia

## Summary in One Sentence

Lenalidomide is currently known to be used for treatment of multiple myeloma and myelodysplastic syndrome with deletion 5q (MDS del(5q)). 
The TxGNN model predicts it may be effective for **Myeloid Leukemia**,
with currently **0 dedicated clinical trials** and **20 related publications** supporting this direction, including 2 systematic reviews/meta-analyses.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No record in Taiwan drug approval database (Not marketed); per literature in the evidence package, lenalidomide is approved for treatment of multiple myeloma (combined with dexamethasone) and MDS with del(5q) abnormality |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L3 (systematic reviews/meta-analyses + early prospective clinical studies; no completed Phase 2/3 RCT for this indication found) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Mechanism of action data in this evidence package is marked as a data gap (DG002). However, the literature collected in the evidence package itself provides mechanistic clues: lenalidomide is an oral immunomodulatory drug (IMiD) derived from thalidomide; its anti-leukemia activity exerts its effect through binding to the cereblon (CRBN) E3 ubiquitin ligase complex, promoting ubiquitination and degradation of IKZF1/IKZF3 (PMID 23316859, 39881283). This mechanism is a molecular targeted type, not traditional cytotoxic chemotherapy.

Both multiple myeloma and del(5q) MDS are clonal diseases of the bone marrow hematopoietic stem cell compartment, and MDS itself has a substantial proportion that transforms to acute myeloid leukemia (AML). This makes the prediction of lenalidomide use for "Myeloid Leukemia" reasonable from a pathophysiological perspective — the evidence package has already collected multiple studies combining lenalidomide with azacitidine for high-risk MDS, AML, and chronic myelomonocytic leukemia (CMML) (e.g., PMID 31221030 meta-analysis, PMID 30271212 systematic review), demonstrating that this drug repurposing direction is not merely based on model inference; clinical exploration already has a solid foundation.

---

## Clinical Trial Evidence

Currently, there are no registered clinical trials directly related to "Myeloid Leukemia."

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|------------|
| [31221030](https://pubmed.ncbi.nlm.nih.gov/31221030/) | 2019 | Systematic review/meta-analysis | Hematology (Amsterdam) | Meta-analysis of efficacy and adverse events of azacitidine combined with lenalidomide for treatment of AML, high-risk MDS, and CMML |
| [30271212](https://pubmed.ncbi.nlm.nih.gov/30271212/) | 2018 | Systematic review/meta-analysis | Cancer Management and Research | Systematic review of efficacy and safety of lenalidomide for AML treatment |
| [37259567](https://pubmed.ncbi.nlm.nih.gov/37259567/) | 2023 | Prospective clinical trial (Azalena-Trial) | Haematologica | Azacitidine + lenalidomide + donor lymphocyte infusion for first-line salvage therapy in post-allogeneic transplant AML/MDS/CMML relapse |
| [37435080](https://pubmed.ncbi.nlm.nih.gov/37435080/) | 2023 | Prospective study | Frontiers in Immunology | Azacitidine + low-dose lenalidomide as maintenance therapy for post-allogeneic transplant AML relapse prevention |
| [34955443](https://pubmed.ncbi.nlm.nih.gov/34955443/) | 2022 | Phase Ib trial | Journal of Geriatric Oncology | Safety assessment of lenalidomide as maintenance therapy after remission in elderly AML patients |
| [34471239](https://pubmed.ncbi.nlm.nih.gov/34471239/) | 2021 | Phase I dose escalation study | Bone Marrow Transplantation | Safety and tolerability of lenalidomide maintenance therapy for post-transplant high-risk AML/MDS |
| [35512188](https://pubmed.ncbi.nlm.nih.gov/35512188/) | 2022 | Original research | Blood | Association analysis of lenalidomide with TP53-mutant therapy-related myeloid neoplasms (t-MN) development |
| [23316859](https://pubmed.ncbi.nlm.nih.gov/23316859/) | 2013 | Review | Expert Opinion on Investigational Drugs | Review of mechanism and clinical development of lenalidomide as a novel AML therapeutic option |
| [37874917](https://pubmed.ncbi.nlm.nih.gov/37874917/) | 2023 | Review | Blood | Update on MDS clinical decision-making and treatment strategies |
| [24656536](https://pubmed.ncbi.nlm.nih.gov/24656536/) | 2014 | Review | Lancet | Comprehensive review of myelodysplastic syndrome including description of AML transformation trajectory |

---

## Safety Considerations

Please refer to TGA-approved product information (PI) for complete safety information.

(This evidence package marks TFDA product information warnings/contraindications as a Blocking-level data gap DG001; DDI query returned no results; initial safety assessment S1 cannot currently be performed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Product information safety data is a Blocking-level gap (DG001), preventing completion of S1 initial safety assessment; the drug is currently not marketed in Australia (0 ARTG entries); this predicted indication "Myeloid Leukemia" is currently supported only by systematic reviews and early prospective studies, with no completed Phase 2/3 RCT found; evidence level is L3.

**To proceed, the following is needed:**
- Obtain TFDA/TGA-approved product information (warnings, contraindications, drug-drug interactions) — Blocking, priority completion required
- Supplement mechanism of action (MOA) structured data via DrugBank API
- Search for completed Phase 2/3 RCTs specifically targeting myeloid leukemia/AML indication (existing trials predominantly focus on MDS del(5q) or multiple myeloma populations)
- If considering application for new indication in the Australian market, need to evaluate ARTG registration pathway (current status: Not marketed)

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

