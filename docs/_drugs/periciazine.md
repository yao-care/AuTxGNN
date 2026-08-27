---
layout: default
title: Periciazine
parent: 僅模型預測 (L5)
nav_order: 525
evidence_level: L5
indication_count: 10
---

# Periciazine
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

# Periciazine: From Antipsychotic Therapy to Anxiety Disorders

## One-Sentence Summary

> Periciazine (DrugBank DB01608) is a piperidine-class phenothiazine with dopamine D2/serotonin 5-HT2A antagonist activity, historically used as an antipsychotic; the original approved indication is not captured in this evidence pack and TxGNN's top-ranked prediction (migraine disorder, score 99.9%) is unsupported by any trial or literature evidence.
> Among the ten candidates returned, **Anxiety** is the only indication combining a plausible class-level mechanism with actual supporting literature — **0 clinical trials** and **3 relevant publications** (including one specific to periciazine).
> Evidence remains preclinical/observational only (L3), and periciazine is **not currently marketed in Australia**, so this is a research question rather than a near-term clinical option.

*Note: This report deviates from strict rank order. TxGNN's rank-1 prediction (migraine disorder, score 99.9%) has zero supporting trials or literature and its own rationale states there is "no clinical or trial evidence whatsoever" for periciazine in this indication — it is flagged in the evidence pack as likely prediction noise. Anxiety (rank 8) is the only candidate the evidence pack itself elevates to decision stage S1 ("Research Question"), so it is used as the headline indication below for clinical relevance.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (no `original_indications` or ARTG data returned) — known pharmacologically as a phenothiazine antipsychotic |
| Predicted New Indication | Anxiety |
| TxGNN Prediction Score | 97.65% (rank 21,369 of all candidates) |
| Evidence Level | L3 (observational/PK cohort study) |
| Australia Market Status | Not marketed (0 ARTG entries) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on known pharmacological class information cited in the evidence pack's own rationale, periciazine is a **piperidine-class phenothiazine** acting via dopamine D2 and serotonin 5-HT2A receptor antagonism — the same mechanism underlying sedative and anxiolytic effects seen across the phenothiazine class.

This class-level sedative/anxiolytic effect is not merely theoretical: the evidence pack notes that periciazine is already approved in France (as *Neuleptil*) for anxiety/agitation as an adjunctive indication, and several other phenothiazines (e.g. chlorpromazine, prochlorperazine) have established anxiolytic and antiemetic uses outside their primary antipsychotic indication. This gives the anxiety prediction a defensible mechanistic and real-world regulatory basis, unlike several other TxGNN outputs in this pack (e.g. migraine disorder, atrophoderma vermiculata, open-angle glaucoma) which the evidence pack's own rationale explicitly labels as mechanistically unrelated or lacking any supporting evidence.

Because `original_indications` was returned empty, the relationship between periciazine's original approved use and the anxiety prediction cannot be formally established here — this should be confirmed against a primary regulatory source (TFDA/TGA-equivalent product information) before further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35361275](https://pubmed.ncbi.nlm.nih.gov/35361275/) | 2022 | Cohort/PK (Tier 2) | J Pharm Health Care Sci | Case report/cohort evaluating periciazine (with brotizolam and sulpiride) transfer into cord blood and breast milk in pregnancy/lactation, in the context of high prevalence of anxiety and mood disorders during pregnancy |
| [12563525](https://pubmed.ncbi.nlm.nih.gov/12563525/) | 2003 | Animal (Tier 3) | Braz J Med Biol Res | Dose-related effects of propericiazine on anxiety and memory models in rats, compared against diazepam |
| [16860706](https://pubmed.ncbi.nlm.nih.gov/16860706/) | 2006 | Review/Case (Tier 3) | Eur Psychiatry | Discusses antipsychotic-induced hypersensitivity of visual perception; general antipsychotic class context, abstract not available |

*One additional PubMed hit returned for this query (PMID 20132509, a syncope/implantable loop recorder case report) was excluded as clinically unrelated to periciazine or anxiety and appears to be a search artifact.*

---

## Australia Market Information

Periciazine is **not currently marketed in Australia** — no ARTG entries were returned for this drug, so no product/dosage-form table is available.

---

## Safety Considerations

Periciazine is not registered on the ARTG, so no TGA-approved Product Information exists for this drug in Australia. Key warnings, contraindications, and drug interaction data were not available in this evidence pack (flagged as a **Blocking** data gap — TFDA/equivalent regulatory label data must be obtained before any safety pre-assessment can proceed). Safety evaluation should draw on an overseas regulatory source (e.g. the French or UK product label for periciazine, given its approved anxiolytic use) until local data can be sourced.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The strongest candidate indication (Anxiety) is supported only by preclinical/observational evidence (L3) with no clinical trials, and a Blocking-severity data gap in safety/label information means the candidate cannot yet clear an initial safety pre-assessment. Periciazine is also not currently marketed in Australia, so any repurposing pathway would first require establishing a regulatory presence.

**To proceed, the following is needed:**
- TFDA/TGA-equivalent product information (warnings, contraindications, DDI) to clear the Blocking data gap
- Confirmed original approved indication(s) for periciazine (currently missing from this evidence pack)
- Detailed mechanism of action data from DrugBank
- Confirmation of ARTG/TGA registration status or a pathway assessment if unregistered
- Prospective or controlled clinical evidence for periciazine (or class-level phenothiazines) specifically in anxiety, beyond the current animal and pharmacokinetic studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

