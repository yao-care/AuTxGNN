---
layout: default
title: Piroxicam
parent: 僅模型預測 (L5)
nav_order: 539
evidence_level: L5
indication_count: 10
---

# Piroxicam
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

# Piroxicam: From Adult Rheumatoid/Osteoarthritis to Juvenile Idiopathic Arthritis

## One-Sentence Summary

> Piroxicam is a non-selective COX-1/COX-2 inhibiting NSAID established for adult rheumatoid arthritis and osteoarthritis.
> Among the ten TxGNN-ranked candidates in this evidence pack, **Juvenile Idiopathic Arthritis (JIA)** is the only one with real supporting evidence — the other nine top-ranked candidates (rare congenital/skeletal-dysplasia syndromes) have no mechanistic plausibility and no literature, and are assessed as knowledge-graph embedding noise rather than genuine signal.
> JIA is supported by **13 publications**, including two piroxicam-specific paediatric RCTs, but **0 registered clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis and related musculoskeletal inflammatory pain conditions (NSAID; formal TFDA/TGA-approved wording not available in evidence pack — see DG001) |
| Predicted New Indication | Juvenile Idiopathic Arthritis (JIA) |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

**Note on other predicted candidates:** The nine other TxGNN candidates in this pack (colobomatous microphthalmia-rhizomelic dysplasia syndrome, brachydactyly-syndactyly syndrome, acromesomelic dysplasia, brachyolmia-amelogenesis imperfecta syndrome, myosclerosis, brachyolmia, pseudoachondroplasia, WHIM syndrome, rheumatoid nodulosis) all scored **L5 / Hold** — no clinical trials, no supporting literature, and no plausible mechanistic link to piroxicam's COX-inhibition pathway. They are not discussed further in this report.

---

## Why is This Prediction Reasonable?

Piroxicam is a non-selective COX-1/COX-2 inhibitor of the oxicam class, reducing prostaglandin synthesis to achieve anti-inflammatory and analgesic effects. This is the mechanism underlying its established use in adult rheumatoid arthritis and osteoarthritis.

JIA (formerly termed juvenile rheumatoid arthritis / juvenile chronic arthritis) involves synovitis driven predominantly by the same prostaglandin pathway. NSAIDs as a drug class are already an established adjunctive standard-of-care for JIA, so the mechanistic rationale here is not purely a model artefact — it is grounded in a well-characterised, shared inflammatory pathway between the original and predicted indications.

Two piroxicam-specific paediatric RCTs (PMID 2957205, PMID 3510686) directly tested piroxicam against naproxen in juvenile arthritis populations in the 1980s, and a paediatric pharmacokinetic study (PMID 1782984) characterised piroxicam dosing in children with rheumatic disease. More recent network meta-analyses of NSAIDs in JIA (2021, 2024) provide contemporary class-level context, though they do not isolate piroxicam specifically.

Formal MOA documentation from DrugBank (DG002) is currently a data gap; the mechanistic description above is drawn from the evidence pack's rationale field, which reflects standard pharmacological classification of piroxicam.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2957205](https://pubmed.ncbi.nlm.nih.gov/2957205/) | 1987 | RCT | European Journal of Rheumatology and Inflammation | Piroxicam vs naproxen in 26 children with juvenile rheumatoid arthritis; significant reduction in painful/swollen joint counts |
| [3510686](https://pubmed.ncbi.nlm.nih.gov/3510686/) | 1986 | RCT | British Journal of Rheumatology | Multicentre double-blind crossover of piroxicam vs naproxen in 47 children with juvenile chronic arthritis; no significant difference between treatments |
| [1782984](https://pubmed.ncbi.nlm.nih.gov/1782984/) | 1991 | Pharmacokinetic study | European Journal of Clinical Pharmacology | Steady-state pharmacokinetics of piroxicam (0.4 mg/kg once daily) in 10 children with rheumatic disease |
| [38680254](https://pubmed.ncbi.nlm.nih.gov/38680254/) | 2024 | Meta-analysis/Network meta-analysis | World Journal of Clinical Cases | Network meta-analysis comparing NSAIDs for JIA; optimal agent/regimen not yet established |
| [33632948](https://pubmed.ncbi.nlm.nih.gov/33632948/) | 2021 | Meta-analysis/Systematic review | Indian Pediatrics | Systematic review and network meta-analysis of comparative efficacy/safety of nine NSAIDs in JIA |
| [2185374](https://pubmed.ncbi.nlm.nih.gov/2185374/) | 1990 | Review | Kinderärztliche Praxis | Overview of drug therapy for juvenile chronic arthritis, discussing piroxicam and sulfasalazine as newer options |
| [9890680](https://pubmed.ncbi.nlm.nih.gov/9890680/) | 1998 | Review (long-term toxicity cohort) | Clinical Rheumatology | Long-term toxicity of NSAIDs/DMARDs in 117 paediatric rheumatology patients (155 NSAID exposures) |
| [7797387](https://pubmed.ncbi.nlm.nih.gov/7797387/) | 1994 | Cohort | International Ophthalmology | Frequency/complications of chronic iridocyclitis in ANA-positive pauciarticular JCA (disease-complication context, not drug-specific) |
| [6753142](https://pubmed.ncbi.nlm.nih.gov/6753142/) | 1982 | Review | Schweizerische Medizinische Wochenschrift | Comparative review of newer NSAIDs' efficacy/tolerability, informing prescribing guidelines |
| [15456329](https://pubmed.ncbi.nlm.nih.gov/15456329/) | 2004 | Review | Drugs | General NSAID (nabumetone) pharmacology/safety review providing drug-class context |

---

## Safety Considerations

Piroxicam does not currently hold an active ARTG listing in Australia, and no TGA-approved Product Information is available in this evidence pack. Key warnings, contraindications and drug interaction data are flagged as a **Blocking data gap (DG001)** — sourcing the TFDA/TGA-equivalent product label is required before any formal safety assessment can be completed.

Please refer to the TGA-approved Product Information (PI), if and when available, for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two piroxicam-specific paediatric RCTs plus supporting pharmacokinetic and NSAID-class meta-analysis data give JIA a credible, mechanism-consistent evidence base (L1), distinguishing it clearly from the other nine TxGNN candidates in this pack, which are unsupported and likely embedding noise. However, piroxicam is not currently marketed in Australia and lacks TGA-approved labelling, so guardrails cannot yet be operationalised.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): source TFDA/TGA-equivalent Product Information for formal warnings, contraindications and DDI data
- Resolve DG002 (High): confirm formal DrugBank MOA record
- Determine regulatory pathway for Australian availability (piroxicam has no active ARTG entry) — likely via Special Access Scheme or new TGA registration if paediatric use is pursued
- Given the RCT evidence base is >30 years old, consider whether a contemporary paediatric trial or updated systematic review specific to piroxicam (not just the NSAID class) is warranted before clinical guardrails are finalised
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

