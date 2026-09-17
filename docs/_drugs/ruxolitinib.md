---
layout: default
title: Ruxolitinib
parent: High Evidence (L1-L2)
nav_order: 610
evidence_level: L2
indication_count: 10
---

# Ruxolitinib
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Ruxolitinib: From JAK1/2-Driven Myeloproliferative Disease to Infection-Associated Hemophagocytic Syndrome

## One-Sentence Summary

Ruxolitinib is a JAK1/2 inhibitor; the specific TGA-approved original indication is not recorded in this evidence pack, but the drug class is best known for myelofibrosis and related myeloproliferative disorders. Across ten TxGNN-predicted indications for this drug, the model's single highest-scoring hits (rare mTOR-driven tumours such as PEComa, LAM, and rhabdoid tumour) carry **no clinical or mechanistic support**, while **hemophagocytic syndrome associated with an infection** — a lower-ranked but mechanistically coherent candidate — is backed by **2 clinical trials** and **20 publications**, including consensus critical-care guidelines. This report focuses on that best-evidenced candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (data gap). Ruxolitinib is a JAK1/2 inhibitor generally associated with myelofibrosis and polycythaemia vera in other jurisdictions. |
| Predicted New Indication | Hemophagocytic syndrome associated with an infection |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

**Note on other candidates:** Nine other TxGNN-predicted indications for ruxolitinib were screened (see "Other Screened Candidates" below). All scored higher on raw TxGNN rank but lack clinical trial or literature support, and several are explicitly flagged in the evidence pack as mechanistically implausible (driven by mTOR or SWI/SNF pathways rather than JAK-STAT). They remain at **Hold**.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for ruxolitinib is not available in this evidence pack. Based on known pharmacology, ruxolitinib is a JAK1/2 inhibitor whose established efficacy in myeloproliferative disease relies on blocking cytokine-receptor signalling through the JAK-STAT pathway.

Hemophagocytic lymphohistiocytosis (HLH), including forms triggered by infection, is a hyperinflammatory cytokine-storm syndrome driven substantially by interferon-gamma (IFN-γ) signalling through the same JAK-STAT axis that ruxolitinib inhibits. This is a much closer mechanistic fit than most of the other TxGNN hits for this drug: the model's top-ranked predictions (PEComa family tumours, lymphangioleiomyomatosis, familial rhabdoid tumour) are driven by TSC1/TSC2-mTOR or SMARCB1/SWI-SNF pathways with no known connection to JAK-STAT signalling, and the evidence pack itself flags these as likely reflecting knowledge-graph topological proximity rather than true biology.

By contrast, the JAK-STAT/IFN-γ link to infection-associated HLH is supported by published murine mechanistic work and has already led to real-world and guideline-level use of ruxolitinib as salvage or first-line adjunct therapy in HLH, making this a substantially stronger repurposing hypothesis than the drug's highest raw TxGNN score would suggest on its own.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04424056](https://clinicaltrials.gov/study/NCT04424056) | Phase 3 | Unknown | 216 | Open randomised trial of anakinra/tocilizumab ± ruxolitinib in severe stage 2b–3 COVID-19–associated disease with severe inflammatory syndrome; completion status unclear. |
| [NCT07424222](https://clinicaltrials.gov/study/NCT07424222) | Phase 1 | Not yet recruiting | 16 | Pilot study of ruxolitinib for immune effector cell-associated HLH-like syndrome (IEC-HS) after CAR-T therapy; assessing safety, optimal duration, and immunological biomarkers of response. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34605776](https://pubmed.ncbi.nlm.nih.gov/34605776/) | 2022 | Review/Consensus Guideline | Critical Care Medicine | Consensus guidelines for recognition, diagnosis, and management of HLH in critically ill children and adults. |
| [37702780](https://pubmed.ncbi.nlm.nih.gov/37702780/) | 2023 | Review | Innere Medizin | Overview of HLH treatment in ICU patients; distinguishes hereditary vs. acquired/secondary forms including infection- and malignancy-triggered disease. |
| [31943120](https://pubmed.ncbi.nlm.nih.gov/31943120/) | 2020 | Review | QJM | Review of adult HLH, a life-threatening hyperimmune disorder with high mortality despite diagnostic and treatment progress. |
| [35344583](https://pubmed.ncbi.nlm.nih.gov/35344583/) | 2022 | Cohort | Blood | Ruxolitinib response-based stratified treatment as first-line agent in 50+ paediatric HLH patients (ChiCTR2000031702). |
| [40665481](https://pubmed.ncbi.nlm.nih.gov/40665481/) | 2025 | Cohort | British Journal of Haematology | Retrospective comparison of ruxolitinib-based regimen (n=53) vs. adjusted HLH-94 chemotherapy (n=42) in paediatric EBV-associated HLH. |
| [32732367](https://pubmed.ncbi.nlm.nih.gov/32732367/) | 2021 | Cohort (pilot) | Haematologica | Pilot study of ruxolitinib as front-line therapy in 12 children with secondary HLH. |
| [37787838](https://pubmed.ncbi.nlm.nih.gov/37787838/) | 2023 | Cohort (compassionate use, n=12) | Annals of Hematology | Sintilimab combined with ruxolitinib as compassionate therapy for adults with EBV-associated HLH. |
| [31015190](https://pubmed.ncbi.nlm.nih.gov/31015190/) | 2019 | Preclinical/Mechanistic | Blood | Mechanistic study showing ruxolitinib dampens IFN-γ signalling and T-cell activation in a murine HLH model. |
| [37228616](https://pubmed.ncbi.nlm.nih.gov/37228616/) | 2023 | Preclinical/Mechanistic | Frontiers in Immunology | Cellular/transcriptional effects of JAK and/or IFN-γ inhibition in a mouse model of primary HLH. |
| [34353999](https://pubmed.ncbi.nlm.nih.gov/34353999/) | 2021 | Review | Current Opinion in Critical Care | Review of JAK inhibitors, including their established HLH use, repurposed for hospitalised COVID-19 patients. |

---

## Other Screened Candidates (Lower Priority — Hold)

For completeness, nine other TxGNN-predicted indications were evaluated for ruxolitinib but do not currently support progression:

| Disease | TxGNN Score | Evidence Level | Status |
|---|---|---|---|
| Uterine corpus PEComa | 99.73% | L5 | Hold — no trials/literature; mTOR-driven, not JAK-STAT |
| Benign PEComa | 99.73% | L5 | Hold — same as above |
| Lymphangiomyoma | 99.72% | L5 | Hold — same as above |
| Lymphangioleiomyomatosis | 99.64% | L5 | Hold — standard therapy is mTOR inhibitor (sirolimus), not JAK-STAT-linked |
| Liposarcoma (myxoid) | 99.52% | L4 | Research Question — preclinical JAK-STAT link only (PMIDs 35186752, 30650179), no clinical data |
| Familial rhabdoid tumour | 99.49% | L5 | Hold — SMARCB1/SWI-SNF driven, no JAK-STAT link |
| Lung PEComa | 99.44% | L5 | Hold — same mTOR-family rationale |
| Ovarian myxoid liposarcoma | 99.39% | L5 | Hold — extrapolated from general liposarcoma hypothesis, no direct data |
| Acquired HLH associated with malignant disease | 99.32% | L3 | Research Question — supported by general HLH guidelines, no malignancy-specific trials |

---

## Australia Market Information

Ruxolitinib currently has **no ARTG entries** and is **not marketed** in Australia according to this evidence pack. No product, dosage form, or approved indication information is available.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Key warnings, contraindications, and drug interaction data are not available in this evidence pack (flagged as a Blocking data gap — DG001).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Infection-associated HLH has a clear mechanistic rationale (JAK-STAT/IFN-γ blockade) that is already reflected in critical-care consensus guidelines and multiple cohort studies, but the two directly relevant trials are either of unknown completion status (NCT04424056) or not yet recruiting (NCT07424222), so no completed controlled trial confirms efficacy in this specific infection-triggered subgroup.

**To proceed, the following is needed:**
- Resolve DG001 (TGA/PI warnings and contraindications) before any safety assessment can proceed — currently blocking.
- Obtain confirmed mechanism-of-action and original-indication documentation (DG002) to properly ground the repurposing rationale.
- Monitor completion of NCT04424056 and recruitment status of NCT07424222.
- Confirm drug-drug interaction profile (DDI query currently returned "not found").
- If pursuing the malignancy-associated HLH subgroup (L3, Research Question) or myxoid liposarcoma (L4, Research Question), commission subgroup-specific trial data before advancing beyond exploratory status.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

