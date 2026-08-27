---
layout: default
title: Lamotrigine
parent: 僅模型預測 (L5)
nav_order: 380
evidence_level: L5
indication_count: 10
---

# Lamotrigine
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

Using no additional skill — this is a direct report-authoring task with an explicit template already supplied in the prompt, not a coding or TxGNN-pipeline engineering task.

Before drafting, one judgement call worth flagging: the evidence pack's own `predicted_indications[0]` ("trigeminal nerve neoplasm", TxGNN top rank) carries a rationale that explicitly identifies it as a likely lexical-confusion artefact (no oncology trials/literature, and the two attached papers are about trigeminal *neuralgia* pain management, not tumour treatment). Presenting that as the headline "new indication" would be misleading for a clinical audience. I have therefore built the report around **trigeminal neuralgia** (rank 2 — the best drug-specific, trial-supported candidate in this pack) and kept the top TxGNN hit as a clearly-labelled data-quality caveat, with the remaining eight lower-confidence candidates summarised in an appendix table for transparency. Below is the report.

---

# Lamotrigine: From Epilepsy to Trigeminal Neuralgia

## One-Sentence Summary

> Lamotrigine is a well-established anticonvulsant used for epilepsy and, in some markets, as maintenance therapy for bipolar I disorder.
> The TxGNN model predicts it may also be effective for **Trigeminal Neuralgia**, a severe facial neuropathic pain condition,
> with **4 clinical trials** (2 of them direct, completed head-to-head studies) and **19 publications** currently supporting this direction.

**Data quality note:** TxGNN's single highest-scoring prediction for this drug ("trigeminal nerve neoplasm", 99.97%) is not covered further in this report. The evidence reviewers flagged it as a likely lexical-confusion artefact — no cancer-related trials or literature were retrieved, and the two attached papers concern trigeminal *neuralgia* pain management, not tumours. Trigeminal neuralgia (rank 2) is the highest-scoring candidate with genuine, drug-specific supporting evidence and is therefore the focus of this evaluation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (partial and generalised seizures); adjunctive/maintenance therapy in bipolar I disorder (established indication; not sourced from an Australian regulatory record — see Market Information below) |
| Predicted New Indication | Trigeminal Neuralgia |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data for lamotrigine was not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on well-established pharmacology cited in the supporting literature, lamotrigine is a voltage-gated sodium-channel blocker that also suppresses presynaptic glutamate release. This stabilises neuronal membranes and reduces repetitive high-frequency firing — the same broad mechanism that underlies its efficacy in epilepsy.

Trigeminal neuralgia is caused by aberrant, high-frequency discharges in the trigeminal nerve root/ganglion, most often from neurovascular compression. The first-line treatments (carbamazepine, oxcarbazepine) work through an essentially identical sodium-channel-blocking mechanism, which is why anticonvulsants as a class have been the mainstay of medical management for this condition for decades.

Because lamotrigine shares this mechanistic class with carbamazepine, the extension from epilepsy to trigeminal neuralgia is pharmacologically coherent rather than speculative. This is reinforced by two small but methodologically direct completed studies comparing lamotrigine against carbamazepine or placebo specifically in trigeminal neuralgia patients (see Clinical Trial Evidence), and by consistent inclusion of lamotrigine as a second-line/adjunct option in multiple neurology guidelines and reviews.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00913107](https://clinicaltrials.gov/study/NCT00913107) | Phase 2/3 | Completed | 21 | Direct head-to-head comparison of lamotrigine vs carbamazepine for efficacy and safety in trigeminal neuralgia. |
| [NCT00203229](https://clinicaltrials.gov/study/NCT00203229) | N/A | Completed | 20 | Double-blind, placebo-controlled add-on study of Lamictal (lamotrigine) in trigeminal neuralgia (tic douloureux). |
| [NCT00243152](https://clinicaltrials.gov/study/NCT00243152) | N/A | Completed | 6 | fMRI study evaluating the effect of lamotrigine on neuropathic facial pain; mechanistic, not a primary efficacy endpoint trial. |

*Note: a fourth trial in this indication (NCT04996199) was excluded from this table — it compares carbamazepine with oxcarbazepine and does not test lamotrigine, so it provides disease-context only, not drug-specific evidence.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21621166](https://pubmed.ncbi.nlm.nih.gov/21621166/) | 2011 | Comparative clinical study | Journal of the Chinese Medical Association | Direct evaluation of lamotrigine vs carbamazepine for efficacy and side-effect profile in trigeminal neuralgia patients. |
| [37892981](https://pubmed.ncbi.nlm.nih.gov/37892981/) | 2023 | Systematic Review | Biomedicines | Umbrella review of drug therapies for trigeminal neuralgia, evaluating efficacy and side effects across published reviews. |
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Guideline | European Journal of Neurology | European Academy of Neurology guideline on trigeminal neuralgia management. |
| [34108244](https://pubmed.ncbi.nlm.nih.gov/34108244/) | 2021 | Review | Practical Neurology | Practical diagnostic and treatment guide for trigeminal neuralgia. |
| [31908187](https://pubmed.ncbi.nlm.nih.gov/31908187/) | 2020 | Review | Molecular Pain | Pathophysiology-to-pharmacotherapy overview of trigeminal neuralgia. |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Review of Neurotherapeutics | Update on pharmacotherapy for trigeminal neuralgia, contextualising older and newer anticonvulsants. |
| [30081317](https://pubmed.ncbi.nlm.nih.gov/30081317/) | 2018 | Case Report | Multiple Sclerosis and Related Disorders | Refractory trigeminal neuralgia successfully treated with combination pregabalin plus lamotrigine. |
| [29114270](https://pubmed.ncbi.nlm.nih.gov/29114270/) | 2017 | Review | Asian Journal of Neurosurgery | Overview of trigeminal neuralgia pathophysiology and treatment options. |
| [25299564](https://pubmed.ncbi.nlm.nih.gov/25299564/) | 2014 | Review | BMJ Clinical Evidence | Evidence review of trigeminal neuralgia treatments. |
| [19445753](https://pubmed.ncbi.nlm.nih.gov/19445753/) | 2009 | Review | BMJ Clinical Evidence | Earlier evidence review of trigeminal neuralgia treatments. |

---

## Australia Market Information

Lamotrigine currently has **no ARTG entries** in this dataset (market status: **Not Marketed**), so no Australian product/indication text is available to cite. Given lamotrigine's long-standing global use, this is worth double-checking directly against the current TGA/ARTG register before relying on it operationally — the "not marketed" status recorded here should be treated as unconfirmed rather than definitive.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No structured key warnings, contraindications, or drug–drug interaction data were returned for this drug in the current evidence pack (the TFDA/PI warning and contraindication data gap, DG001, is flagged as **Blocking severity** — it must be resolved before this candidate can proceed to a Stage 1 safety assessment).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Two completed, direct comparative/placebo-controlled studies (albeit small, n=20–21) and a consistent body of neurology guideline and review literature support lamotrigine's mechanistic and clinical plausibility in trigeminal neuralgia, corresponding to Evidence Level L2.
- The pathway cannot advance past initial safety screening until the Blocking-severity label/warning data gap (DG001) is resolved, and the drug's Australian market status needs independent confirmation.

**To proceed, the following is needed:**
- TFDA/TGA-approved Product Information (warnings, contraindications, drug interactions) to clear the Blocking data gap (DG001)
- Formal DrugBank/mechanism-of-action documentation (DG002)
- Independent confirmation of current ARTG/market status in Australia
- Consideration of a larger or pooled trial given the small sample sizes (n=20–21) in the existing direct evidence

---

## Appendix: Other TxGNN-Predicted Indications for Lamotrigine (Not Prioritised)

These candidates scored highly in the same TxGNN run but were not carried forward as the primary recommendation, either due to weak/absent drug-specific evidence or explicit reviewer concern about spurious model associations.

| Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|---------|------|------|------|------|
| Trigeminal nerve neoplasm | 99.97% | L5 | Hold | Likely lexical-confusion artefact; no oncology-relevant evidence |
| Startle epilepsy | 99.38% | L3 | Research Question | Rare reflex epilepsy subtype; supported by 2 small case series |
| Restless legs syndrome | 98.90% | L3 | Research Question | Supported by 1 pilot trial and several case reports |
| Eating seizures | 99.38% | L4 | Hold | No indication-specific efficacy evidence found |
| Thinking seizures | 99.38% | L4 | Hold | Evidence is generic AED/epilepsy data, not specific to this seizure subtype |
| Reading seizures | 99.30% | L4 | Hold | Directly relevant literature favours levetiracetam, not lamotrigine |
| Audiogenic seizures | 99.38% | L3 | Hold | Evidence largely from animal models; one human case series (startle-induced) |
| Micturition-induced seizures | 99.38% | L5 | Hold | No literature specific to this seizure subtype identified |
| Orgasm-induced seizures | 99.38% | L5 | Hold | No supporting trials or literature; score driven by disease-node clustering |

*This appendix is supplementary context beyond the standard report template, included to keep the evaluation transparent about the full set of model outputs for this drug.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

