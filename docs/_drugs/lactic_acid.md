---
layout: default
title: Lactic Acid
parent: 僅模型預測 (L5)
nav_order: 378
evidence_level: L5
indication_count: 10
---

# Lactic Acid
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

# Lactic Acid: From No Registered Indication to Multiple TxGNN‑Predicted Candidates (Screening Review)

## One-Sentence Summary

Lactic acid (DrugBank DB04398) has no approved indication on record in this evidence pack and is **not currently marketed in Australia**. TxGNN generated ten candidate new indications, but on evidence review the top-ranked candidates (structural cardiovascular and congenital malformations) appear to be **artefacts of knowledge-graph keyword co-occurrence rather than genuine mechanistic signals**, while two lower-ranked candidates — **dry eye syndrome/Sjögren's syndrome** and **eye disease** more broadly — are supported by real (but directionally inconsistent) mechanistic literature on lactate metabolism in ocular tissue.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication on record for this product |
| Predicted New Indication (TxGNN top rank) | Atypical coarctation of aorta |
| TxGNN Prediction Score (top rank) | 99.59% |
| Evidence Level (top rank) | L5 |
| Best-Supported Alternative Candidates | Dry eye syndrome (L3) / Eye disease (L3) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | **Hold** |

---

## Screening Summary — All Predicted Indications Reviewed

Because this evidence pack evaluates a *panel* of ten TxGNN candidates rather than a single indication, the table below summarises the full screening outcome before drilling into detail.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|-----------------|
| 1 | Atypical coarctation of aorta | 99.59% | L5 | S0 | Hold |
| 2 | Aortic malformation | 99.35% | L4 | S0 | Hold |
| 3 | Non-syndromic esophageal malformation | 99.23% | L5 | S0 | Hold |
| 4 | Amenorrhea (disease) | 99.16% | L4 | S0 | Hold |
| 5 | **Dry eye syndrome** | 99.13% | **L3** | **S1** | **Research Question** |
| 6 | Esophageal disease | 98.94% | L5 | S0 | Hold |
| 7 | Double outlet right ventricle with AVSD, pulmonary stenosis, heterotaxy | 98.82% | L5 | S0 | Hold |
| 8 | Excretory apparatus of the lacrimal system anomaly | 98.77% | L5 | S0 | Hold |
| 9 | **Eye disease** | 98.68% | **L3** | **S1** | **Research Question** |
| 10 | Cauda equina syndrome | 98.67% | L5 | S0 | Hold |

**Key observation:** the top five TxGNN scores are clustered within a narrow band (99.59%–99.13%), yet evidence quality diverges sharply. Ranks 1, 3, 7, 8 and 10 are congenital/structural anatomical conditions requiring surgical correction, with **zero clinical trials or literature retrieved** — these are not diseases a small organic acid can plausibly treat. Ranks 2, 4 and 6 returned trial/literature hits, but manual review found these to be keyword coincidences (e.g., "aorta", "esophageal") unrelated to lactic acid pharmacology. Only ranks 5 and 9 (both eye/ocular-surface conditions) returned literature with a genuine, biologically active role for lactate in the relevant tissue.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for lactic acid is not available in this evidence pack (`original_moa: [Data Gap]`), and no original approved indication is recorded, so the usual "original indication → new indication" mechanistic bridge cannot be constructed here. Lactic acid is the terminal product of glycolysis and a systemic/tissue pH-modulating metabolite; it does not have a defined pharmacological mechanism for reversing anatomical malformations, which explains why ranks 1, 3, 6, 7, 8 and 10 (all structural/congenital conditions) are assessed as prediction noise — TxGNN's knowledge graph appears to have linked lactic acid to these diseases through indirect metabolic/cardiovascular node co-occurrence rather than a causal treatment relationship.

The more scientifically interesting signal sits with **dry eye syndrome** (rank 5) and **eye disease** (rank 9). Multiple mechanistic studies show lactate and its post-translational modification "lactylation" are biologically active in ocular tissues — in the lacrimal glands (Sjögren's syndrome), sclera (myopia), and choroid/retina (neovascularisation, diabetic retinopathy). However, in essentially all of these studies **lactate acts as a pathological/pro-inflammatory driver**, not a therapeutic agent: it promotes cGAS-STING inflammatory signalling in Sjögren's acinar cells, drives histone lactylation that accelerates scleral remodelling in myopia, and upregulates VEGF to promote choroidal neovascularisation. This is the opposite direction to what a "repurposing for treatment" hypothesis requires, so while the biology is real, it does not currently support using lactic acid *therapeutically* for these conditions — it flags a research question, not a treatment opportunity.

No clinical trial in this pack administers lactic acid as an investigational treatment for any of the ten predicted indications; all clinical trial hits are coincidental keyword matches (e.g., perioperative lactate monitoring, unrelated drugs tested in cardiac/ocular populations).

---

## Clinical Trial Evidence

**Currently no clinical trials registered that test lactic acid as a treatment for any of the ten predicted indications.** All retrieved trials (across ranks 2, 4, 5, 6 and 9) were manually graded and found to be coincidental keyword matches — studies of unrelated drugs, surgical techniques, or devices in patient populations that happen to share disease-name keywords with the predicted indication (e.g., "aorta," "esophageal," "eye"). No ANZCTR identifiers were present in the source data.

Representative examples of why trials were excluded as irrelevant:

| Trial Number | Phase | Status | Enrolment | Why Excluded |
|---------|------|------|------|---------|
| [NCT01920594](https://clinicaltrials.gov/study/NCT01920594) | Phase 2 | Completed | 57 | Tests GSK1278863 (HIF-PH inhibitor) for aortic aneurysm repair — no pharmacological link to lactic acid |
| [NCT03237312](https://clinicaltrials.gov/study/NCT03237312) | Phase 2 | Completed | 50 | PCOS ovarian drilling study; amenorrhoea keyword match only |
| [NCT03544281](https://clinicaltrials.gov/study/NCT03544281) | Phase 1/2 | Completed | 153 | Antibody-drug conjugate for multiple myeloma; matched to "dry eye" only via unrelated adverse-event terminology |
| [NCT01791595](https://clinicaltrials.gov/study/NCT01791595) | Phase 1 | Completed | 53 | Tests AZD3965 (a monocarboxylate transporter/lactate-transport inhibitor) in advanced cancer — mechanistically the *inverse* of lactic acid administration |
| [NCT02511613](https://clinicaltrials.gov/study/NCT02511613) | Phase 2 | Withdrawn | 0 | Tests squalamine lactate (an unrelated aminosterol salt), not lactic acid itself, for macular degeneration |

---

## Literature Evidence

No literature directly tests lactic acid as a therapeutic agent for any predicted indication. The table below lists the most relevant **mechanistic** literature — concentrated on ranks 5 and 9 — describing lactate/lactylation biology in ocular and lacrimal tissue. This evidence explains *why* the disease nodes are connected to lactic acid in the knowledge graph, but points toward lactate as a disease driver rather than a treatment.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39054226](https://pubmed.ncbi.nlm.nih.gov/39054226/) | 2025 | Review | Trends in Molecular Medicine | Reviews lactate/lactylation signalling in eye morphogenesis and disease, including myopia, intraocular malignancy, and retinal angiogenesis |
| [37786436](https://pubmed.ncbi.nlm.nih.gov/37786436/) | 2023 | Basic/Mechanistic | International Journal of Medical Sciences | Lactate-induced mitochondrial DNA accumulation activates cGAS-STING signalling and inflammation in Sjögren's syndrome (a major cause of dry eye) |
| [40759752](https://pubmed.ncbi.nlm.nih.gov/40759752/) | 2025 | Basic/Mechanistic | Nature Metabolism | Lactate signalling aggregates immune-inflammatory hotspots in autoimmune tissue; SLC5A12 (lactate transporter) blockade resolves them |
| [38232735](https://pubmed.ncbi.nlm.nih.gov/38232735/) | 2024 | Basic/Mechanistic | Cell Metabolism | Increased scleral glycolysis/lactate promotes myopia via histone lactylation in animal models |
| [30046816](https://pubmed.ncbi.nlm.nih.gov/30046816/) | 2018 | Basic/Mechanistic | Investigative Ophthalmology & Visual Science | Lactic acid upregulates VEGF in macrophages and facilitates choroidal neovascularisation |
| [34251320](https://pubmed.ncbi.nlm.nih.gov/34251320/) | 2021 | Metabolomics/Cohort | Clinical and Experimental Rheumatology | Serum metabolomics identifies disturbed lactate-related pathways as potential biomarkers in Sjögren's syndrome |
| [31491425](https://pubmed.ncbi.nlm.nih.gov/31491425/) | 2019 | Cohort/Biochemical | Experimental Eye Research | Vitreous pH and lactic acid concentration are elevated in patients with diabetes mellitus |
| [3367436](https://pubmed.ncbi.nlm.nih.gov/3367436/) | 1988 | Cohort/Mechanistic | Journal of Vascular Surgery | Aortic wall lactate/glycolytic metabolism differs proximal/distal to experimental coarctation — an indirect metabolic association only, not treatment evidence |

---

## Australia Market Information

Lactic acid has **no ARTG (Australian Register of Therapeutic Goods) entries** in this evidence pack (`total_licenses: 0`) and its market status is recorded as **not marketed** in Australia. No product/brand, dosage form, or approved indication text is available to summarise.

---

## Safety Considerations

Safety data for this product is currently a **blocking data gap**: TGA/TFDA-equivalent product label warnings and contraindications were not available (`key_warnings` and `contraindications` both return "[Data Gap]"), and a drug interaction (DDI) query returned no results. This gap is flagged in the evidence pack as **Blocking severity**, meaning it prevents the candidate from proceeding to an initial safety assessment (S1) regardless of predicted-indication evidence strength.

> Please refer to the TGA-approved Product Information (PI) for safety information once a marketed formulation and label are identified.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No predicted indication in this pack reaches a level of evidence that would justify progressing past initial screening. The TxGNN top-ranked candidates are structural/congenital conditions with no plausible drug-treatable mechanism and no supporting trials or literature — most likely knowledge-graph noise. The two candidates with genuine mechanistic literature (dry eye syndrome, eye disease) point to lactate as a **disease-promoting**, not therapeutic, metabolite, which runs counter to the repurposing hypothesis. Separately, a **Blocking data gap** (missing TFDA/TGA-equivalent product warnings) means this candidate cannot yet undergo a basic safety evaluation even if a promising indication were identified.

**To proceed, the following is needed:**
- TFDA/TGA product label (warnings, contraindications) — currently a Blocking gap preventing any S1 safety assessment
- Confirmed mechanism of action (MOA) data from DrugBank or another primary source
- Clarification of the original approved indication(s), if any, for this specific product/formulation
- If pursuing the dry eye/ocular research question further: preclinical or clinical evidence testing lactate modulation (e.g., lactate transporter inhibition) as a *treatment* strategy, rather than relying on evidence that characterises lactate as a pathological driver
- Re-run of TxGNN screening interpretation with disease-node specificity checks, given the apparent keyword-coincidence pattern seen across 6 of the 10 candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

