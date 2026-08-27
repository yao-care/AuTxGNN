---
layout: default
title: Febuxostat
parent: 僅模型預測 (L5)
nav_order: 266
evidence_level: L5
indication_count: 10
---

# Febuxostat
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

# Febuxostat: From Gout/Chronic Hyperuricaemia to Renal Hypouricemia

## One-Sentence Summary

Febuxostat is a selective xanthine oxidase (XO) inhibitor established for lowering serum urate in gout/chronic hyperuricaemia. The TxGNN model's top prediction points to **Renal Hypouricemia** — but this is a directionally counter-intuitive target (urate *under*-excretion, not excess), with the real proposed clinical link being **prevention of exercise-induced acute kidney injury (EIAKI)** in this population rather than "treating" the low urate itself. Evidence is currently limited: **1 clinical trial** (relevance uncertain) and **2 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed by regulatory data in this pack (no ARTG licence records returned). Known clinical use: gout / chronic hyperuricaemia via xanthine oxidase inhibition — corroborated indirectly by this pack's own rationale for related candidates, not by a primary MOA field (see below). |
| Predicted New Indication | Renal Hypouricemia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not returned for this drug (`original_moa: [Data Gap]`, DG002), and no original-indication text is available because there are zero ARTG licence records. Based on well-established pharmacology corroborated within this evidence pack's own rationale for related candidates, febuxostat is a **selective xanthine oxidase inhibitor** that blocks the terminal step of purine-to-urate conversion, and is used clinically to lower serum urate in gout/chronic hyperuricaemia.

The top-ranked prediction requires an important caveat that the evidence pack itself flags: **renal hypouricemia is a urate under-reabsorption disorder, not an excess-urate state** — pharmacologically, further inhibiting urate production with febuxostat does not correct the underlying defect. The genuine clinical rationale in the literature is different: patients with renal hypouricemia (often URAT1 mutation carriers) are prone to **exercise-induced acute kidney injury (EIAKI)**, thought to be driven by XO-generated reactive oxygen species during anaerobic exercise; XO inhibitors are being explored as **EIAKI prophylaxis** in this group, not as treatment of the hypouricemia itself. This distinction should be resolved before this candidate advances — the disease-model target and the actual mechanistic hypothesis are not the same entity.

Notably, two lower-ranked candidates in this pack — **HPRT partial deficiency** (rank 2) and **Lesch-Nyhan syndrome** (rank 3) — have a materially cleaner mechanistic fit: both are purine-salvage-pathway defects causing genuine urate overproduction, where XO inhibition is directly disease-modifying and already has off-label precedent in allopurinol-intolerant/renally-impaired patients. These may warrant equal or higher priority alongside the top-ranked target.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Phase 4 | Unknown | 100 | Prospective controlled study of uric acid control on stone recurrence and renal function in patients with hyperuricaemia-associated calculi. **Relevance: Grade C** — registered title shows only the sponsoring institution (Dept. of Urology, Shanghai Xu-hui Central Hospital); direct link to renal hypouricemia/EIAKI is unconfirmed pending full registry review. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Review | Internal Medicine (Tokyo) | Discusses non-purine selective XO inhibitors, including febuxostat, for prevention of EIAKI in patients with renal hypouricemia (URAT1 mutation case reported). Most directly relevant reference for this candidate. |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | Narrative review of hypouricemia definition, aetiology and classification for rheumatologists; background context, not febuxostat-specific. |

---

## Australia Market Information

Currently no ARTG entries — febuxostat is not marketed in Australia per this evidence pack (`total_licenses: 0`).

---

## Safety Considerations

Key warnings, contraindications and drug-interaction data were not returned for this drug. **Note:** the missing product-label warnings/contraindications (DG001) are classified as a **Blocking** data gap that prevents this candidate from entering safety triage (S1) — this must be resolved before any further evaluation.

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A blocking data gap (missing label warnings/contraindications) prevents safety triage, and the mechanistic rationale for the top-ranked target is internally flagged as ambiguous — it is unclear whether the intended target is renal hypouricemia itself or its EIAKI complication. The drug is also not currently marketed in Australia (0 ARTG entries), adding regulatory lead time regardless.

**To proceed, the following is needed:**
- TFDA/TGA-equivalent product label (warnings, contraindications) to resolve DG001
- Clarification of whether the TxGNN target is renal hypouricemia itself or EIAKI prophylaxis in this population, with re-scoping of the candidate definition if needed
- DrugBank-sourced MOA and original-indication documentation (DG002)
- Consideration of prioritising the mechanistically cleaner HPRT partial deficiency / Lesch-Nyhan syndrome candidates (ranks 2–3) alongside or ahead of this one
- ARTG/TGA marketing-pathway assessment if this candidate is pursued further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

