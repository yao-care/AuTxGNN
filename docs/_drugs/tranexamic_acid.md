---
layout: default
title: Tranexamic Acid
parent: Moderate Evidence (L3-L4)
nav_order: 694
evidence_level: L4
indication_count: 10
---

# Tranexamic Acid
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

Using no specific skill here — this is a direct content-generation task with a fully specified template already in the prompt, not a coding/build/debug task.

A few notes before the report: `original_indications` and `original_moa` are empty/gap in this evidence pack, and `taiwan_regulatory.licenses` is empty (0 ARTG entries, market status "not marketed"). I've represented these as genuine data gaps rather than inventing values. I've also kept the evidence pack's own critical assessment intact — the pack's `repurposing_rationale` explicitly flags the top prediction as a likely knowledge-graph label mismatch, and ranks 2–4 as potential *contraindications* (thrombophilia) rather than opportunities. That's safety-relevant, so I've added a short supplementary table for ranks 2–10 rather than silently dropping it.

---

# Tranexamic Acid: From Unspecified Original Indication to Amenorrhea

## One-Sentence Summary

> Tranexamic acid (DrugBank DB00302) is an antifibrinolytic agent, but its formally documented original indication and mechanism of action are not available in this evidence pack.
> The TxGNN model's top prediction is **Amenorrhea (disease)**, supported by **0 clinical trials** and **2 review articles**.
> The evidence pack's own mechanistic analysis flags this specific prediction as likely reflecting a knowledge-graph labelling mismatch rather than a genuine therapeutic signal — the supporting literature actually concerns *reducing* menstrual bleeding, not treating its absence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack |
| Predicted New Indication | Amenorrhea (disease) — flagged as likely data/label mismatch (see below) |
| TxGNN Prediction Score | 99.19% |
| Evidence Level | L4 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for tranexamic acid was not returned in this evidence pack (drug-level data gap, DrugBank query pending). However, the pack's mechanistic rationale for this specific prediction describes tranexamic acid as a lysine analogue that reversibly binds the lysine-binding site of plasminogen, inhibiting plasmin generation — i.e. it is an antifibrinolytic that **reduces** bleeding. Its established clinical role (per the supporting literature) is in *heavy* menstrual bleeding (abnormal uterine bleeding) and menses suppression in patients with treatment-related cytopenias.

This creates a directional inconsistency with the predicted indication of **amenorrhea** (absence of menstruation). Both cited papers discuss managing excessive or unwanted bleeding, not restoring absent menstruation — the opposite clinical problem. The evidence pack's own analysis concludes this is most likely a knowledge-graph node/ontology mismatch, where the TxGNN disease node labelled "amenorrhea" may actually cluster with "abnormal uterine bleeding / menorrhagia" concepts. This should be verified against the disease ontology ID before this candidate is treated as a genuine repurposing signal, rather than accepted at face value from the model score alone.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Review | Menopause (New York, N.Y.) | Evidence-based review of pharmacological therapies for abnormal uterine bleeding; concerns *reducing* bleeding, not treating amenorrhea |
| [39043214](https://pubmed.ncbi.nlm.nih.gov/39043214/) | 2024 | Review | J Oncol Pharm Pract | Systematic approach to menses prophylaxis and suppression in pre-menopausal haematologic cancer patients; again concerns bleeding *suppression* |

## Australia Market Information

Tranexamic acid has no ARTG entries recorded in this evidence pack (market status: Not Marketed, 0 licenses). No product/dosage form data is available to summarise.

## Other Predicted Indications (Ranks 2–10) — Supplementary Safety Context

All remaining predictions also carry a **Hold** recommendation. Several are noted in the evidence pack as *directionally contraindicated* rather than therapeutic opportunities, which is important context for anyone reviewing this candidate:

| Rank | Disease | Score | Evidence Level | Note |
|------|---------|-------|-----------------|------|
| 2 | Heparin cofactor II deficiency | 96.50% | L5 | Thrombophilia — antifibrinolytic could theoretically *increase* thrombotic risk; cited literature is a safety-signal paper, not efficacy evidence |
| 3 | Factor V excess with spontaneous thrombosis | 95.21% | L5 | Thrombophilia; no literature; same directionality concern as above |
| 4 | Antithrombin deficiency type 2 | 94.32% | L5 | Thrombophilia; no literature; same directionality concern as above |
| 5 | Hypospadias 3, autosomal | 68.38% | L5 | No plausible mechanistic link; likely KG noise |
| 6 | Sella turcica, bridged | 68.38% | L5 | No plausible mechanistic link; likely KG noise |
| 7 | Triphalangeal thumb, nonopposable | 68.38% | L5 | No plausible mechanistic link; likely KG noise |
| 8 | Hypercarotenemia and vitamin A deficiency (AR) | 68.35% | L5 | No plausible mechanistic link; likely KG noise |
| 9 | Primary hyperparathyroidism (water clear cell hyperplasia) | 68.01% | L5 | No plausible mechanistic link; likely KG noise |
| 10 | Glaucoma with elevated episcleral venous pressure | 66.78% | L5 | Weak, unverified mechanistic hypothesis; no supporting evidence |

## Safety Considerations

The blocking data gap for TGA/local product safety information (warnings, contraindications) has not yet been resolved for tranexamic acid in this evidence pack, and a drug interaction search returned no results. Please refer to the TGA-approved Product Information (PI) for safety information once tranexamic acid's registration status in Australia is confirmed. Note that ranks 2–4 above (thrombophilia-related conditions) should be treated as potential **safety red flags**, not efficacy leads, pending pharmacological review.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A blocking data gap (local product warnings/contraindications) currently prevents this candidate from entering safety pre-screening (S1).
- The top-ranked prediction (amenorrhea) is mechanistically inconsistent with the supporting literature and is flagged by the pack's own analysis as a probable knowledge-graph label mismatch rather than a genuine signal.
- Several lower-ranked predictions represent thrombophilic conditions where an antifibrinolytic is more plausibly contraindicated than therapeutic, and the remainder are low-score, biologically implausible outputs consistent with model noise.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/TGA-equivalent PI warnings and contraindications) before any safety pre-screening
- Resolve DG002 (confirmed mechanism of action and documented original indication) from DrugBank
- Verify the disease ontology ID behind the "amenorrhea (disease)" TxGNN node against the source knowledge graph, to confirm whether the intended target is actually abnormal uterine bleeding / menorrhagia
- Pharmacological/thrombosis-risk review before any further consideration of ranks 2–4
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

