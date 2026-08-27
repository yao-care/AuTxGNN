---
layout: default
title: Phenobarbital
parent: 僅模型預測 (L5)
nav_order: 530
evidence_level: L5
indication_count: 10
---

# Phenobarbital
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

# Phenobarbital: From Epilepsy (Seizure Disorders) to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Phenobarbital is a barbiturate classically used to treat epilepsy and seizure disorders (this evidence pack contains no formal Australian regulatory indication text, as the drug is not currently marketed here). The TxGNN model's top-ranked prediction suggests possible relevance to **Trigeminal Nerve Neoplasm**, but this is currently supported by **0 clinical trials** and only **1 loosely related publication**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy / seizure disorders (established pharmacological classification; no ARTG indication text available — see below) |
| Predicted New Indication | Trigeminal Nerve Neoplasm |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available in this evidence pack (flagged as a High-severity data gap). Based on well-established pharmacological classification, phenobarbital is a barbiturate-class anticonvulsant and sedative-hypnotic; its efficacy in seizure disorders is long established in clinical practice, even though no formal original-indication text or MOA record was returned by this evidence pull.

The TxGNN model's top-ranked candidate, Trigeminal Nerve Neoplasm, is not well explained by the supporting evidence retrieved here. The single associated publication is a 25-year case series on Sturge-Weber syndrome (a neurocutaneous disorder involving facial/trigeminal-distribution vascular anomalies and seizures) — it does not directly study phenobarbital's use in a nerve neoplasm, and does not establish a clear mechanistic or clinical rationale for this specific indication. This pattern is consistent with a knowledge-graph-level association (e.g. shared anatomical or seizure-related terminology) rather than a pharmacologically grounded repurposing signal.

By contrast, several lower-ranked but textually closer predictions in this same evidence pack — including reflex/situational seizure types (thinking, audiogenic, eating, startle, micturition-induced, reading seizures) and trigeminal neuralgia (rank 9, 17 literature hits) — have much more direct and mechanistically plausible support, since phenobarbital is an established anticonvulsant. These may warrant separate evaluation alongside or instead of the top-ranked candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case Series | Anales españolas de pediatría | Retrospective review of 14 Sturge-Weber syndrome cases over 25 years, evaluating clinical characteristics, evolution, and treatment response. Does not directly address phenobarbital use in trigeminal nerve neoplasm. |

---

## Australia Market Information

Phenobarbital currently has **0 ARTG entries** and is **not marketed** in Australia. No product listing, dosage form, or approved-indication data is available from this evidence pack.

---

## Safety Considerations

No safety data (key warnings, contraindications, or drug interactions) were returned in this evidence pack — flagged as a **Blocking** data gap (DG001). Because phenobarbital is not currently marketed in Australia, there is no TGA-approved Product Information to reference. Any safety evaluation for this indication would need to draw on an overseas regulatory label (e.g. FDA, EMA) or a direct TFDA/TGA data request before proceeding to clinical assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Trigeminal Nerve Neoplasm) has no clinical trial support and only one tangentially related publication, giving an evidence level of L5. Combined with a Blocking-severity gap in safety/label data and phenobarbital's unmarketed status in Australia, there is insufficient basis to advance this specific candidate.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/TGA product information — warnings, contraindications) before any S1 safety screening
- Resolve DG002 (DrugBank mechanism of action) to support mechanistic-link analysis
- Clarify or re-verify the KG match quality for "Trigeminal Nerve Neoplasm," as the retrieved literature does not directly support this disease label
- Consider evaluating the better-supported alternative candidates in this same prediction set — particularly trigeminal neuralgia (rank 9, 17 publications) and the reflex-seizure indications (ranks 2–8), which align more directly with phenobarbital's established anticonvulsant mechanism
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

