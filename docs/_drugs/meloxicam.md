---
layout: default
title: Meloxicam
parent: 僅模型預測 (L5)
nav_order: 423
evidence_level: L5
indication_count: 10
---

# Meloxicam
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

# Meloxicam: From NSAID Symptomatic Therapy to Juvenile Idiopathic Arthritis (RF-Positive Polyarticular)

## One-Sentence Summary

> Meloxicam is an oxicam-class NSAID used for symptomatic relief of osteoarthritis, rheumatoid arthritis and related inflammatory joint conditions.
> Among 10 TxGNN-predicted indications in this evidence pack, the only one supported by actual clinical literature is **rheumatoid factor–positive polyarticular Juvenile Idiopathic Arthritis (JIA)**,
> backed by **1 Phase 4 registry cohort study**; the model's raw top-ranked hits (rare skeletal dysplasias) carry no clinical or mechanistic support and are not viable leads.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (TFDA/ARTG licence data unavailable — data gap DG001) |
| Predicted New Indication | Rheumatoid factor–positive polyarticular Juvenile Idiopathic Arthritis |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed (per this evidence pack) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

**Note on candidate selection:** TxGNN's raw #1-ranked prediction for meloxicam is *acromesomelic dysplasia, Hunter-Thompson type* (score 99.92%) — a GDF5-related skeletal developmental disorder. Its own repurposing rationale states this has **no mechanistic or clinical support** ("與 NSAID 消炎鎮痛機轉無關聯，純預測結果無臨床或機轉支持") and is scored Evidence Level L5 / Hold. The same applies to ranks 2, 3, 4, 9 and 10 (brachyolmia variants, myosclerosis, WHIM syndrome, colobomatous microphthalmia-rhizomelic dysplasia) — all structural or genetic disorders with no inflammatory component and no evidence trail. This report therefore focuses on the only candidate that reached an evidence-supported decision stage (S2): rank 8, JIA.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (data gap DG002). Based on general pharmacological knowledge, meloxicam is an oxicam-class NSAID that preferentially inhibits cyclooxygenase-2 (COX-2), reducing prostaglandin synthesis and producing anti-inflammatory, analgesic and antipyretic effects. This mechanism underlies its established use in adult inflammatory joint disease.

Juvenile Idiopathic Arthritis, including the RF-positive polyarticular subtype, shares the same core pathology — synovial inflammation driven by prostaglandin-mediated pathways — as the adult arthritides meloxicam already treats. NSAIDs (including nonselective agents and celecoxib) are an established symptomatic-control option in JIA management guidelines, so the mechanistic leap from "adult inflammatory arthritis" to "paediatric inflammatory arthritis" is small and clinically plausible, rather than speculative.

It's worth noting three further candidates reached "Research Question" status (L4/S1) on mechanistic grounds alone, without direct evidence: *spondyloarthropathy susceptibility* (strong mechanistic fit — NSAIDs are first-line in spondyloarthropathies, but this entry denotes genetic susceptibility rather than confirmed disease), *pseudoachondroplasia* (NSAID relevant only for secondary joint pain, not the underlying disorder), and *rheumatoid nodulosis* (symptom control only, not disease-modifying). These may warrant monitoring but are not yet actionable.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25057265](https://pubmed.ncbi.nlm.nih.gov/25057265/) | 2014 | Cohort (Phase 4 registry) | Pediatric Rheumatology Online Journal | Long-term safety and developmental outcomes in JIA patients treated with celecoxib or non-selective NSAIDs in routine clinical practice. This is a **safety** dataset for the NSAID drug class in the JIA population, not a meloxicam-specific efficacy trial. |

---

## Australia Market Information

No ARTG entries are recorded for meloxicam in this evidence pack. Market status is listed as **not marketed** in Australia (total licences: 0). This should be independently verified against the current ARTG register, as it may reflect a data-collection gap rather than genuine market absence.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Note: TFDA/PI warning and contraindication data could not be retrieved for this evidence pack (data gap DG001, flagged as **Blocking** — this prevents progression to the S1 safety screening stage).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(applies specifically to the JIA indication, rank 8)*

**Rationale:**
The mechanistic link between meloxicam's COX-2 inhibition and JIA's inflammatory pathology is strong, and one Phase 4 registry cohort supports the safety of the NSAID class (including a COX-2-preferential agent) in this paediatric population. However, this is class-level safety evidence, not a meloxicam-specific efficacy trial, and it does not substitute for a full PI safety review.

**To proceed, the following is needed:**
- TFDA/TGA Product Information (warnings, contraindications, DDI) — currently a **Blocking** data gap (DG001)
- Confirmed mechanism-of-action documentation (DG002)
- A meloxicam-specific (not class-level) efficacy/safety study in the paediatric JIA population
- Independent verification of Australian ARTG market status, which currently shows zero entries
- If pursuing secondary leads, dedicated evidence generation for spondyloarthropathy susceptibility and rheumatoid nodulosis before they can move beyond "Research Question" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

