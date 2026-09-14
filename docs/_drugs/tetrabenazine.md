---
layout: default
title: Tetrabenazine
parent: 僅模型預測 (L5)
nav_order: 666
evidence_level: L5
indication_count: 10
---

# Tetrabenazine
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

# Tetrabenazine: From Huntington's Disease Chorea to Polycystic Kidney Disease 3

## One-Sentence Summary

> Tetrabenazine is a VMAT2 inhibitor conventionally used overseas to control chorea associated with Huntington's disease and tardive dyskinesia; it is not currently marketed in Australia.
> The TxGNN model predicts it may be effective for **Polycystic Kidney Disease 3 (with or without polycystic liver disease)**, with a very high similarity score (99.90%),
> but this is currently supported by **zero clinical trials** and **no drug-specific literature** — the evidence pack itself flags this as a likely knowledge-graph topology artefact rather than a genuine mechanistic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Huntington's disease chorea (based on known international pharmacology; no ARTG-approved indication text is available as the drug is not currently marketed in Australia) |
| Predicted New Indication | Polycystic Kidney Disease 3, with or without Polycystic Liver Disease |
| TxGNN Prediction Score | 99.90% (rank 1,760 of all candidate pairs) |
| Evidence Level | L5 — model prediction only, no supporting studies |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured drug record for this candidate. Based on known pharmacology, tetrabenazine is a **VMAT2 (vesicular monoamine transporter 2) inhibitor** — it depletes striatal dopamine and other monoamines to control hyperkinetic movement disorders such as Huntington's disease chorea and tardive dyskinesia.

Polycystic Kidney Disease 3 (PKD3) is a genetic ciliopathy in which mutations affecting primary cilia signalling drive progressive renal and hepatic cyst formation. There is no established pharmacological or pathophysiological overlap between monoamine depletion in the central nervous system and ciliary dysfunction/cystogenesis in the kidney and liver — these are mechanistically unrelated disease processes affecting entirely different organ systems.

Given this, the high TxGNN score most likely reflects **proximity within the knowledge graph's embedding space** rather than a validated biological relationship. This interpretation is explicitly echoed in the evidence pack's own rationale, and is reinforced by the fact that no clinical trials and no drug-specific publications support this indication. The same pattern holds across nearly all of the top-10 predicted indications for this drug (ranks 2–10), where literature and trial evidence is either absent or represents clear retrieval mismatches (e.g., a Huntington's disease gait trial and an unrelated torticollis case report appearing under "thoracic malformation").

---

## Clinical Trial Evidence

Currently no related clinical trials registered for tetrabenazine in Polycystic Kidney Disease 3.

*(Note: a single trial, NCT01451463, appears elsewhere in this evidence pack under a different predicted indication — it evaluates tetrabenazine's effect on gait in Huntington's disease and is unrelated to PKD3.)*

---

## Literature Evidence

None of the following publications mention tetrabenazine directly — they are background reviews/guidelines on polycystic kidney/liver disease itself, retrieved on disease-term relevance rather than drug-specific evidence.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38958301](https://pubmed.ncbi.nlm.nih.gov/38958301/) | 2024 | Guideline | Am J Gastroenterol | ACG guideline on focal liver lesions, including management of polycystic liver disease |
| [30819518](https://pubmed.ncbi.nlm.nih.gov/30819518/) | 2019 | Review | Lancet | Overview of ADPKD clinical manifestations, genetics and systemic complications |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clin Liver Dis | Notes tolvaptan (not tetrabenazine) slows renal decline and cyst growth in ADPKD |
| [29038287](https://pubmed.ncbi.nlm.nih.gov/29038287/) | 2018 | Review | J Am Soc Nephrol | Genetic overlap between ADPKD and autosomal dominant polycystic liver disease |
| [38097330](https://pubmed.ncbi.nlm.nih.gov/38097330/) | 2023 | Review | Adv Kidney Dis Health | PKD1/PKD2 genetic spectrum and resulting phenotypes |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Guideline | J Hepatol | EASL guidelines on diagnosis/management of cystic liver diseases |
| [34034501](https://pubmed.ncbi.nlm.nih.gov/34034501/) | 2022 | Review | Rev Esp Enferm Dig | Differential diagnosis of hepatic cystic lesions (hydatid cyst) |
| [40081770](https://pubmed.ncbi.nlm.nih.gov/40081770/) | 2025 | Review | Biochem Pharmacol | ECM/matrix metalloprotease dynamics as therapeutic targets in ADPKD/ARPKD |
| [37208103](https://pubmed.ncbi.nlm.nih.gov/37208103/) | 2023 | Review | J Hepatol | Considerations for combined liver-kidney transplantation in polycystic disease |
| [36047551](https://pubmed.ncbi.nlm.nih.gov/36047551/) | 2022 | Review | Rev Med Suisse | General overview of polycystic liver disease subtypes and clinical course |

---

## Australia Market Information

Tetrabenazine is **not currently marketed in Australia** — there are no ARTG entries on record for this drug.

---

## Safety Considerations

As tetrabenazine is not currently registered in Australia, no TGA-approved Product Information exists locally. Structured safety data (warnings, contraindications, drug interactions) are also unavailable in this evidence pack. Prescribers and evaluators should refer to overseas regulatory documentation (e.g., FDA-approved labelling for tetrabenazine-containing products) as an interim reference until local safety data can be obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has an L5 evidence level — the prediction rests entirely on TxGNN's model score, with zero clinical trials and no drug-specific literature supporting use in PKD3. The evidence pack's own mechanistic analysis concludes there is no known pathological link between VMAT2 inhibition and ciliopathy-driven cystogenesis, and the same lack of support extends across nearly all other top-10 predicted indications for this drug.

**To proceed, the following is needed:**
- Confirmed mechanism of action data for tetrabenazine (currently a data gap)
- TGA product information / overseas label data covering warnings and contraindications (currently blocking — no safety data available)
- Preclinical or mechanistic studies specifically linking VMAT2/monoamine pathways to ciliary or cystogenic processes
- Any drug-specific (not disease-background) clinical or observational evidence before this candidate can be reconsidered beyond Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

