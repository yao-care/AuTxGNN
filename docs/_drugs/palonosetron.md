---
layout: default
title: Palonosetron
parent: 僅模型預測 (L5)
nav_order: 508
evidence_level: L5
indication_count: 10
---

# Palonosetron
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

Using the drug-repurposing report template from the system prompt to produce the evaluation. I did not find any project skill that overrides this — it's a direct content-generation task from the provided Evidence Pack.

A note before the report: the evidence pack for **rank 1 (migraine disorder)** is unusual — its only literature citation (PMID 21132477) is a case report of the drug *causing* migraine-type headache as a side effect, not treating it. I've reported this faithfully rather than smoothing it over, since that distinction is critical for a prescriber-facing report.

---

# Palonosetron: From Chemotherapy-Induced Nausea and Vomiting to Migraine Disorder

## One-Sentence Summary

Palonosetron is a second-generation 5-HT3 receptor antagonist, established as an antiemetic for chemotherapy- and post-operative-induced nausea and vomiting (CINV/PONV). The TxGNN model predicts a possible link to **Migraine Disorder** with a very high score (**99.74%**), but this is currently supported by only **0 clinical trials** and **1 case report** — and that case report actually describes the drug *inducing* headache, not treating it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Australian regulatory data; based on known pharmacology, palonosetron is an antiemetic used for prevention of chemotherapy-induced and post-operative nausea and vomiting (CINV/PONV) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (marked as a High-severity data gap in this evidence pack). Based on known information, palonosetron is a second-generation 5-HT3 (serotonin) receptor antagonist, and its efficacy in preventing chemotherapy- and post-operative-induced nausea and vomiting is well established and supported by multiple Phase 3 RCTs (see the related "headache disorder" candidate below, which draws on the same trial base).

There is no established pharmacological pathway linking 5-HT3 receptor antagonism to migraine treatment. Migraine therapies (e.g. triptans) work through 5-HT1B/1D receptor **agonism**, a different receptor subtype and opposite pharmacological action to palonosetron's 5-HT3 **antagonism**. The single literature citation available for this candidate (PMID 21132477) is a case report titled *"Palonosetron-induced migraine-type headache"* — describing headache as an adverse drug reaction, which is a recognised class effect of 5-HT3 antagonists, not a therapeutic signal.

Taken together, the very high TxGNN score most likely reflects the knowledge graph picking up a drug–disease **co-occurrence** (palonosetron appearing near "headache/migraine" nodes because it can *cause* headache) rather than a genuine treatment relationship. This candidate should be interpreted with caution rather than treated as a promising repurposing lead.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21132477](https://pubmed.ncbi.nlm.nih.gov/21132477/) | 2011 | Case Report | Canadian Journal of Anaesthesia | Describes a case of migraine-type headache **induced by** palonosetron administration — an adverse drug reaction, not evidence of therapeutic benefit for migraine |

## Australia Market Information

No ARTG entries are recorded for this drug in the current data set (0 licences; market status: not marketed). This should be confirmed directly against the TGA/ARTG database, as this remains a Blocking-severity data gap in the evidence pack (TFDA/TGA product information could not be retrieved).

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No key warnings, contraindications, or drug interaction data were retrievable for this evaluation (drug interaction query returned "not found").

## Other TxGNN-Predicted Candidates (Not Recommended)

This evidence pack scored 10 candidate indications for palonosetron; all received a "Hold" recommendation. For transparency:

- **Headache disorder** (rank 6, score 97.9%) has the most supporting data of the batch — 3 clinical trials and 4 publications — but all of these are existing PONV/CINV prophylaxis trials in which headache was, at most, an incidental observation, not the treatment target.
- **Migraine with brainstem aura, migraine susceptibility, trigeminal autonomic cephalalgia, open-angle glaucoma, primary hereditary glaucoma, sciatic neuropathy, atrophoderma vermiculata, and ulerythema ophryogenesis** (ranks 2–5, 7–10) have no clinical trial or literature evidence at all, or literature that is topically unrelated (e.g. epilepsy genetics papers picked up via disease-node proximity in the knowledge graph rather than genuine drug relevance). None have a plausible mechanistic link to palonosetron's pharmacology.

None of these candidates currently justify further investment.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only literature evidence for the top-ranked candidate (migraine disorder) describes headache as a drug-induced adverse event rather than a treatment effect, and there is no clinical trial evidence, no mechanistic rationale, and no supporting data for any of the other nine predicted indications in this batch. The TxGNN score alone, without corroborating clinical or mechanistic evidence, is insufficient to progress this candidate.

**To proceed, the following is needed:**
- Confirmed TGA/ARTG registration status and Product Information (currently a Blocking data gap)
- Verified mechanism of action data from DrugBank or another authoritative source (currently a High-severity data gap)
- Any preclinical or mechanistic studies establishing a plausible link between 5-HT3 antagonism and migraine pathophysiology, if this candidate is to be reconsidered
- Re-evaluation should this data gap be resolved and new clinical or mechanistic evidence emerge
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

