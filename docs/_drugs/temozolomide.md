---
layout: default
title: Temozolomide
parent: 僅模型預測 (L5)
nav_order: 658
evidence_level: L5
indication_count: 10
---

# Temozolomide
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

# Temozolomide: From Malignant Glioma to Adult Astrocytic Tumour

## One-Sentence Summary

Temozolomide is an oral alkylating chemotherapy agent internationally indicated for glioblastoma multiforme and refractory anaplastic astrocytoma, but it is **not currently registered in Australia** (no ARTG entry). The TxGNN model predicts it is effective for **Adult Astrocytic Tumour**, with a **99.36% prediction score**, supported by **2 clinical trials** and **20 publications**, including the landmark Stupp et al. (2005) Phase 3 trial that established TMZ as the global standard of care for this tumour type.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Australia; internationally indicated for glioblastoma multiforme and refractory anaplastic astrocytoma (WHO grade III/IV glioma) |
| Predicted New Indication | Adult Astrocytic Tumour |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Temozolomide is an oral imidazotetrazine alkylating agent that crosses the blood-brain barrier and methylates DNA at the O6-guanine position, triggering tumour cell apoptosis. This mechanism underpins its established role as the standard chemotherapy backbone for astrocytic tumours (including glioblastoma), with MGMT promoter methylation status acting as a well-recognised predictor of response.

Because "Adult Astrocytic Tumour" is the broader disease category that already encompasses glioblastoma and anaplastic astrocytoma, this TxGNN prediction largely **reconfirms an existing, well-established international indication** rather than identifying a novel mechanistic repurposing signal. The convergence is reinforced by several closely related TxGNN predictions in the same evidence run — high grade astrocytic tumour, low grade astrocytic tumour, and brain astrocytoma — all scoring in a similar range and all supported by L1-level evidence (multiple Phase 2/3 RCTs).

The practical significance for Australia is therefore less about mechanistic novelty and more about **registration status**: temozolomide is not on the ARTG, so this evidence pack effectively documents a strong, internationally mature case for local registration or structured access, rather than an early-stage hypothesis requiring proof-of-concept work.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00052455](https://clinicaltrials.gov/study/NCT00052455) | Phase 3 | Completed | 500 | Randomised comparison of temozolomide alone versus procarbazine/lomustine/vincristine (PCV) in recurrent WHO grade III/IV astrocytic tumours — direct population match for this indication (Relevance grade A) |
| [NCT00960492](https://clinicaltrials.gov/study/NCT00960492) | Phase 1 | Completed | 26 | Dose-finding study of XL184 combined with temozolomide and radiotherapy in newly diagnosed glioblastoma; temozolomide is a co-administered background agent rather than the primary study drug (Relevance grade C) |

No ANZCTR-registered trials were identified for this indication in the current evidence pack.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15758009](https://pubmed.ncbi.nlm.nih.gov/15758009/) | 2005 | RCT | N Engl J Med | Landmark Stupp trial establishing concomitant and adjuvant temozolomide plus radiotherapy as superior to radiotherapy alone for newly diagnosed glioblastoma |
| [26670971](https://pubmed.ncbi.nlm.nih.gov/26670971/) | 2015 | RCT | JAMA | Tumour-treating fields plus maintenance temozolomide versus temozolomide alone improved outcomes in glioblastoma |
| [30782343](https://pubmed.ncbi.nlm.nih.gov/30782343/) | 2019 | RCT | Lancet | CeTeG/NOA-09 Phase 3 trial: lomustine-temozolomide combination versus standard temozolomide in MGMT-methylated glioblastoma |
| [39480453](https://pubmed.ncbi.nlm.nih.gov/39480453/) | 2024 | RCT | JAMA Oncology | Randomised trial of veliparib added to temozolomide in MGMT-methylated glioblastoma |
| [22578793](https://pubmed.ncbi.nlm.nih.gov/22578793/) | 2012 | RCT | Lancet Oncology | NOA-08 Phase 3 trial: temozolomide alone versus radiotherapy alone in elderly patients with malignant astrocytoma |
| [24552317](https://pubmed.ncbi.nlm.nih.gov/24552317/) | 2014 | RCT | N Engl J Med | Randomised trial evaluating bevacizumab added to standard temozolomide chemoradiotherapy in newly diagnosed glioblastoma |
| [40779733](https://pubmed.ncbi.nlm.nih.gov/40779733/) | 2025 | RCT | J Clin Oncol | NRG Oncology BN007 randomised Phase II/III trial of dual immune checkpoint blockade in MGMT-unmethylated glioblastoma |
| [36809318](https://pubmed.ncbi.nlm.nih.gov/36809318/) | 2023 | Review | JAMA | Overview of glioblastoma and other primary brain malignancies in adults, including standard temozolomide-based treatment |
| [10914698](https://pubmed.ncbi.nlm.nih.gov/10914698/) | 2000 | Review | Clin Cancer Res | Early review establishing temozolomide's promise in malignant glioma (glioblastoma and anaplastic astrocytoma) |
| [25920709](https://pubmed.ncbi.nlm.nih.gov/25920709/) | 2015 | Cohort/Trial | J Neurooncol | Exploratory Phase 2 cohort of concurrent radiotherapy and temozolomide schedules in anaplastic astrocytic gliomas |

---

## Australia Market Information

Temozolomide currently has **no ARTG entry** and no marketed product in Australia. As it is not TGA-registered, clinical access would rely on alternative pathways such as the TGA Special Access Scheme (SAS) or Authorised Prescriber pathway, importing an overseas-approved product (e.g. Temodal®/Temodar®). No local Product Information (PI) exists to reference at this time.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — alkylating agent (imidazotetrazine class; spontaneously converts to MTIC, methylates DNA at O6-guanine) |
| Myelosuppression Risk | Not characterised in this evidence pack (safety data flagged as a Blocking data gap — DG001). Internationally, myelosuppression (particularly thrombocytopenia and neutropenia) is the recognised dose-limiting toxicity for temozolomide — confirm against the overseas Product Information |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Full blood count with differential (platelets and neutrophils in particular), liver function, renal function — to be confirmed against official PI once obtained |
| Handling Protection | Cytotoxic drug handling precautions apply as an oral alkylating chemotherapy agent, pending confirmation via official PI |

---

## Safety Considerations

Temozolomide is not currently registered in Australia, and this evidence pack does not contain TGA/local Product Information warnings, contraindications, or drug interaction data — this is flagged as a **Blocking** data gap (DG001). Please obtain and review the overseas-approved Product Information (e.g. Temodal®/Temodar®) and complete a formal S1 safety pre-assessment before any clinical use is considered.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Evidence is strong (L1) for temozolomide's efficacy in adult astrocytic tumours, anchored by multiple completed Phase 3 RCTs including the practice-defining Stupp et al. (2005) trial, and reinforced by convergent TxGNN predictions across related astrocytoma subtypes.
- However, this candidate cannot progress past initial safety triage because the Product Information/warnings data is a **Blocking** gap (DG001), and structured mechanism-of-action data is a **High**-severity gap (DG002).

**To proceed, the following is needed:**
- Download and parse the overseas TFDA/manufacturer Product Information PDF to complete the S1 safety pre-assessment (resolves DG001)
- Query the DrugBank API for structured mechanism-of-action data (resolves DG002)
- Clarify the applicable Australian access pathway (ARTG registration vs. SAS/Authorised Prescriber) given temozolomide's current unmarketed status
- Note for reviewers: because "Adult Astrocytic Tumour" substantially overlaps with temozolomide's existing international oncology indication, this should be treated as a local registration/access opportunity rather than a genuinely novel repurposing hypothesis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

