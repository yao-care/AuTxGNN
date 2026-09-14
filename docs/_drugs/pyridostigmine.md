---
layout: default
title: Pyridostigmine
parent: 僅模型預測 (L5)
nav_order: 571
evidence_level: L5
indication_count: 10
---

# Pyridostigmine
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

# Pyridostigmine: From Generalised Myasthenia Gravis to Myasthenia Gravis with Thymus Hyperplasia

## One-Sentence Summary

Pyridostigmine is a cholinesterase inhibitor whose established use, as referenced in the evidence pack, is symptomatic treatment of generalised myasthenia gravis (MG). The TxGNN model predicts a strong association with **myasthenia gravis with thymus hyperplasia**, a clinical subtype of the same disease, supported by **3 publications** and **no dedicated clinical trials** identified for this specific subtype. This is best understood as a label-extension signal within an already-established indication rather than a genuinely novel repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Generalised myasthenia gravis (symptomatic treatment)¹ |
| Predicted New Indication | Myasthenia gravis with thymus hyperplasia |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

¹ Not captured in the ARTG licence data (0 entries — drug is not marketed in Australia). This is drawn from the evidence pack's own mechanistic rationale, since the `original_moa` field is a recorded data gap (DG002).

## Why is This Prediction Reasonable?

Detailed, independently-sourced mechanism-of-action data is not currently available (data gap DG002). However, the evidence pack's own repurposing rationale identifies pyridostigmine as an acetylcholinesterase (AChE) inhibitor that raises acetylcholine concentration at the neuromuscular junction — the standard symptomatic mechanism by which it treats generalised myasthenia gravis, a mechanism confirmed clinically over many years.

Myasthenia gravis with thymus hyperplasia is not a distinct disease but a well-recognised clinical subtype of generalised MG, in which thymic hyperplasia commonly accompanies acetylcholine-receptor-antibody-positive disease. Because pyridostigmine's mechanism acts downstream of the autoimmune/thymic process — directly at the neuromuscular junction — its applicability to this subtype follows logically from its already-established use in generalised MG. The prediction therefore reflects strong mechanistic continuity, but it should be read as an indication-extension/subtype confirmation rather than a novel therapeutic application, as flagged directly in the evidence pack's rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25683765](https://pubmed.ncbi.nlm.nih.gov/25683765/) | 2015 | Cohort | Journal of Neurology | Retrospective analysis of 39 patients with non-thymomatous, AChR-antibody-positive, late-onset generalised MG; evaluated 2-year outcomes of thymectomy, providing subtype-specific clinical context relevant to thymic-hyperplasia MG management. |
| [34225443](https://pubmed.ncbi.nlm.nih.gov/34225443/) | 2021 | Review | Molecular Medicine Reports | Reviews MG pathology, genomics and autoimmunity; describes MG as a heterogeneous disorder with neonatal, ocular and generalised subtypes and autoantibodies against the acetylcholine receptor, supporting the mechanistic basis for AChE-inhibitor therapy. |
| [18053719](https://pubmed.ncbi.nlm.nih.gov/18053719/) | 2008 | Case Report | Neuromuscular Disorders (NMD) | Case of MuSK-positive MG with thymus hyperplasia presenting as dropped head syndrome; illustrates clinical heterogeneity within the thymus-hyperplasia MG subtype. |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic basis for pyridostigmine's efficacy in this MG subtype is well established (it is already a standard-of-care agent in generalised MG), but evidence specific to the thymus-hyperplasia subtype consists only of one cohort study, one review and one case report (Evidence Level L3), with no dedicated clinical trials. The drug is also not currently marketed in Australia (0 ARTG entries), and a Blocking data gap on TGA-equivalent warnings/contraindications (DG001) means the safety pre-screen (S1) cannot yet be completed.

**To proceed, the following is needed:**
- TGA-approved Product Information covering warnings, precautions and contraindications (Blocking gap, DG001)
- Verified mechanism-of-action documentation from DrugBank or an equivalent source (High-priority gap, DG002)
- Confirmation of whether this candidate should be framed as a subtype-level label clarification of an existing indication rather than a new repurposing opportunity, before further resourcing is allocated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

