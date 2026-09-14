---
layout: default
title: Sulfasalazine
parent: 僅模型預測 (L5)
nav_order: 644
evidence_level: L5
indication_count: 10
---

# Sulfasalazine
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

# Sulfasalazine: From Rheumatoid Arthritis to Osteoarthritis

## One-Sentence Summary

Sulfasalazine is a long-established DMARD used to treat rheumatoid arthritis and inflammatory bowel disease-related arthropathies. Among 10 TxGNN-predicted indications, the model's top-ranked candidates are ultra-rare genetic syndromes with **no supporting evidence** (the model's own rationale states no biological link exists), so this report instead focuses on **Osteoarthritis**, the highest-ranked candidate with actual supporting data — **2 clinical trials** and **20 publications**, though evidence remains largely preclinical/animal-based rather than direct human OA trials.

> **Note on methodology**: TxGNN ranks 1, 2, 3, 4, 6, 7, 9 and 10 (all rare monogenic syndromes, scores >99.4%) returned zero clinical trials, zero literature, and the model's own generated rationale explicitly states "no known biological relationship" for each. These are not presented further below as they carry no actionable evidence. A second candidate, "spondyloarthropathy, susceptibility to" (Rank 8, L3, evidence pack recommendation "Proceed with Guardrails"), is noted separately below — it largely reinforces sulfasalazine's *already established* clinical use in spondyloarthritis rather than representing a genuinely new repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis / inflammatory bowel disease-associated arthropathy (established clinical use; not captured in this evidence pack's regulatory data) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data was not returned in this evidence pack (`original_moa: [Data Gap]`). However, the literature evidence collected for this candidate independently describes sulfasalazine's relevant pharmacology: its metabolites (sulfapyridine and 5-aminosalicylic acid) inhibit NF-κB signalling and suppress prostaglandin/leukotriene synthesis, giving the drug anti-inflammatory and disease-modifying activity that underlies its established use in rheumatoid arthritis.

Osteoarthritis and rheumatoid arthritis share overlapping joint-inflammation and cartilage-degradation pathways, even though OA is traditionally viewed as more mechanical/degenerative. Several preclinical studies in this pack show sulfasalazine directly protecting cartilage: it blocked cytokine-stimulated release of proteoglycan and collagen fragments from cartilage explants, reduced matrix metalloproteinase activity, and attenuated cartilage destruction in an MIA-induced rat OA model and an ACL-transection OA model via inhibition of the cystine/glutamate antiporter.

This gives a plausible mechanistic bridge from RA to OA. However, essentially all of this evidence is preclinical (in vitro, ex vivo, or animal models) — there is no completed human RCT establishing sulfasalazine's efficacy specifically for OA. The two clinical trials identified are only tangentially related (see below), so the prediction should be read as a research hypothesis rather than a validated clinical signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03975790](https://clinicaltrials.gov/study/NCT03975790) | N/A (retrospective) | Completed | 479 | US claims-database study comparing tofacitinib+MTX withdrawal vs continuation in RA — does not involve sulfasalazine directly; low relevance (Grade C) |
| [NCT00551707](https://clinicaltrials.gov/study/NCT00551707) | Phase 2 | Completed | 51 | Double-blind RCT of CRx-102 (dipyridamole + low-dose prednisolone) vs its components; brief summary references hand osteoarthritis proof-of-concept, but the title is truncated in source data and sulfasalazine's involvement could not be confirmed — needs manual verification (Grade B) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29548914](https://pubmed.ncbi.nlm.nih.gov/29548914/) | 2018 | Preclinical (in vitro/animal) | Int J Biol Macromol | Sulfasalazine-loaded hyaluronic acid reduced inflammation and cartilage degradation in an MIA-induced rat OA model |
| [26466556](https://pubmed.ncbi.nlm.nih.gov/26466556/) | 2016 | Animal model | J Orthop Res | Sulfasalazine inhibited the cystine/glutamate antiporter, attenuating ACL-transection/meniscectomy-induced cartilage destruction |
| [19690126](https://pubmed.ncbi.nlm.nih.gov/19690126/) | 2009 | Preclinical (ex vivo) | Rheumatology (Oxford) | Sulfasalazine blocked cytokine-stimulated cartilage matrix (GAG/collagen) release and downregulated MMPs/ADAMTS |
| [24329131](https://pubmed.ncbi.nlm.nih.gov/24329131/) | 2014 | Preclinical (proteomic) | Mod Rheumatol | Compared sulfasalazine and tofacitinib effects on articular chondrocyte protein profiles |
| [1673814](https://pubmed.ncbi.nlm.nih.gov/1673814/) | 1991 | Preclinical (ex vivo) | Wien Klin Wochenschr | Sulfasalazine and metabolites modulated prostaglandin/leukotriene release from synovial tissue in OA, RA and chondrocalcinosis patients |
| [35958605](https://pubmed.ncbi.nlm.nih.gov/35958605/) | 2022 | Review | Front Immunol | Reviewed ferroptosis pathways across inflammatory arthritis types, including OA and RA |
| [11478054](https://pubmed.ncbi.nlm.nih.gov/11478054/) | 2001 | Review | Hand Clin | Overview of pharmacologic treatment options for OA and RA |
| [9567207](https://pubmed.ncbi.nlm.nih.gov/9567207/) | 1998 | Review | Curr Opin Rheumatol | Reviewed clinical trials across rheumatic diseases, including OA |
| [35951003](https://pubmed.ncbi.nlm.nih.gov/35951003/) | 2022 | Cohort | Clin Exp Immunol | Compared TAM receptor tyrosine kinase levels in RA vs OA synovial fluid/tissue |
| [12205730](https://pubmed.ncbi.nlm.nih.gov/12205730/) | 2002 | Cohort | Yonsei Med J | Assessed bone collagen crosslink excretion in RA patients treated with sulphasalazine |

---

## Australia Market Information

Sulfasalazine is currently **not marketed** in Australia under this evidence pack's data (0 ARTG entries recorded). No product-level TGA information is available to summarise here.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. This evidence pack could not retrieve product-specific warnings, contraindications, or drug interaction data (TFDA/TGA label extraction is flagged as a blocking data gap — see Next Steps).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic case (cartilage-protective, anti-inflammatory activity) is supported by several preclinical/animal studies, but there is no confirmed human RCT evidence for sulfasalazine in osteoarthritis specifically, and neither identified clinical trial reliably tests this drug-disease pair. This does not yet meet the bar for "Proceed with Guardrails."

**To proceed, the following is needed:**
- TGA-approved Product Information (PI) — currently a blocking gap for any safety assessment
- Confirmation of whether NCT00551707 (CRx-102 study) actually involves sulfasalazine, and full-text review of its hand-OA outcomes
- A dedicated human proof-of-concept or pilot trial translating the animal/ex vivo cartilage-protection findings into OA patients
- Formal DrugBank MOA data to replace the current data gap

*Separate note: "spondyloarthropathy, susceptibility to" (Rank 8) carries the evidence pack's own "Proceed with Guardrails" recommendation (L3), but represents reinforcement of sulfasalazine's already-established use in spondyloarthritis rather than a new indication — worth tracking as supporting evidence for existing use, not as a new repurposing candidate.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

