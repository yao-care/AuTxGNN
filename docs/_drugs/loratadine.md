---
layout: default
title: Loratadine
parent: 僅模型預測 (L5)
nav_order: 405
evidence_level: L5
indication_count: 10
---

# Loratadine
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

# Loratadine: From Antihistamine Therapy to Allergic Urticaria

## One-Sentence Summary

Loratadine is a second-generation H1-antihistamine. The TxGNN model's top prediction for this drug is **Allergic Urticaria**, which — based on the evidence pack's own mechanistic analysis — is best understood as a *known-use reconfirmation* of the antihistamine class rather than a novel repurposing hypothesis. This is supported by **3 clinical trials** and **18 publications** currently on file, though none directly test Loratadine itself against allergic urticaria as a primary efficacy endpoint.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not returned by the regulatory data sources in this evidence pack (see note below) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 98.98% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed (per available registry data) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available as a structured field for this drug (flagged as a data gap, DG002). Based on the evidence supplied with this candidate, Loratadine is a second-generation H1-histamine receptor antagonist. Allergic urticaria is primarily driven by mast-cell degranulation and histamine release acting on H1 receptors, so the mechanistic link between drug and indication is direct.

Importantly, the evidence pack itself notes this is **not a genuinely novel repurposing signal**: second-generation antihistamines, including loratadine, are an established drug class for urticaria internationally, so this prediction largely reconfirms already-known pharmacology rather than surfacing a new therapeutic hypothesis.

No Taiwan/TGA regulatory license records were returned for this drug in this evidence pack (`market_status: 未上市`, 0 ARTG entries), so the original approved indication could not be extracted from local regulatory sources. This should be treated as a data gap rather than evidence that no original indication exists.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00762983](https://clinicaltrials.gov/study/NCT00762983) | N/A (post-marketing survey) | Completed | 1,003 | Claritin (loratadine) tablet/RediTabs/dry syrup pediatric drug-use investigation; collected ADR frequency and safety/effectiveness factors in children |
| [NCT00757562](https://clinicaltrials.gov/study/NCT00757562) | Phase 3 | Completed | 97 | Multiple-dose safety/tolerance of desloratadine (loratadine's active metabolite) in atopic children and children with chronic idiopathic urticaria who are poor metabolizers |

*Note: a third hit (NCT07101445, motixafortide premedication study) was excluded — it was flagged in the evidence pack as unrelated to loratadine/urticaria (keyword-matching noise).*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35396016](https://pubmed.ncbi.nlm.nih.gov/35396016/) | 2022 | Review | Profiles of Drug Substances, Excipients and Related Methodology | Comprehensive profile of loratadine; notes its use in allergic rhinitis, chronic urticaria and asthma |
| [7528133](https://pubmed.ncbi.nlm.nih.gov/7528133/) | 1994 | Review | Drugs | Reappraisal of loratadine's pharmacology and therapeutic use, including urticaria; superior to placebo, comparable to other antihistamines |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Review | Annals of Pharmacotherapy | Reviews oral antihistamines (loratadine class) for allergic rhinitis and chronic idiopathic urticaria management |
| [16329713](https://pubmed.ncbi.nlm.nih.gov/16329713/) | 2005 | Review | Drug Safety | Safety/efficacy of desloratadine (active metabolite) across allergic disease including chronic idiopathic urticaria |
| [18336052](https://pubmed.ncbi.nlm.nih.gov/18336052/) | 2008 | Review | Clinical Pharmacokinetics | Comparative PK/PD of desloratadine, fexofenadine and levocetirizine in allergic rhinitis/chronic idiopathic urticaria |
| [9951950](https://pubmed.ncbi.nlm.nih.gov/9951950/) | 1999 | Review | Drugs | Comparative review of second-generation antihistamines, including loratadine |
| [7530629](https://pubmed.ncbi.nlm.nih.gov/7530629/) | 1994 | Review | Drugs | General review of urticaria recognition, causes and antihistamine-based treatment |
| [39549290](https://pubmed.ncbi.nlm.nih.gov/39549290/) | 2024 | Cohort | Iranian Journal of Allergy, Asthma, and Immunology | Dose-comparison of desloratadine combined with nasal steroid in allergic rhinitis; notes higher antihistamine doses recommended for urticaria control |
| [12113226](https://pubmed.ncbi.nlm.nih.gov/12113226/) | 2002 | Review | Clinical Allergy and Immunology | H1-antihistamine use in children, primarily allergic rhinoconjunctivitis |
| [40490797](https://pubmed.ncbi.nlm.nih.gov/40490797/) | 2025 | Mechanistic study | Chinese Medicine | Network pharmacology study of a TCM formula in chronic urticaria; mast-cell/immune mechanism context |

---

## Australia Market Information

No ARTG entries were returned for Loratadine in this evidence pack (`total_licenses: 0`, `market_status: 未上市`). This should be confirmed directly against the TGA ARTG database, as it may reflect a data collection gap rather than true absence from the Australian market.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Structured warnings, contraindications and drug-interaction data were not available in this evidence pack (flagged as a **Blocking** data gap — DG001: TFDA/TGA label warnings and contraindications must be sourced before this candidate can complete initial safety screening).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link is strong and well-supported by the antihistamine literature, and one completed Phase 3 trial plus a large completed post-marketing survey exist — but the underlying data pack also indicates this is largely a reconfirmation of already-established antihistamine use rather than a new discovery, and a blocking safety data gap (PI warnings/contraindications) prevents formal safety sign-off.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications) — currently blocking
- Confirmed mechanism-of-action documentation (currently a data gap)
- Verification of ARTG registration status for loratadine-containing products in Australia
- Drug-drug interaction data (current query returned no results)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

