---
layout: default
title: Dulaglutide
parent: 僅模型預測 (L5)
nav_order: 172
evidence_level: L5
indication_count: 10
---

# Dulaglutide
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

# Dulaglutide: From Type 2 Diabetes to Opsismodysplasia

## One-Sentence Summary

Dulaglutide is a long-acting GLP-1 receptor agonist established globally for the management of Type 2 Diabetes Mellitus and cardiovascular risk reduction. The TxGNN model predicts it may be effective for **Opsismodysplasia**, an ultra-rare skeletal dysplasia caused by INPPL1 (SHIP2) gene mutations. Currently, **no clinical trials** and **no published literature** support this predicted direction, placing the evidence at Level 5 — model prediction only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus (globally established; no ARTG record retrieved in this data pull) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 97.05% |
| Evidence Level | L5 |
| Australia Market Status | No records retrieved — ARTG verification required |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Dulaglutide is a GLP-1 receptor agonist (GLP-1RA) that works by stimulating glucose-dependent insulin secretion, suppressing glucagon release, slowing gastric emptying, and reducing appetite via central GLP-1 receptor activation. Its proven role in Type 2 Diabetes and cardiovascular risk reduction (REWIND trial) is well-recognised internationally, though no approved indication record was retrieved in this data pull.

Opsismodysplasia is an ultra-rare autosomal recessive skeletal dysplasia caused by loss-of-function mutations in INPPL1 (SHIP2), a phosphatase that regulates the phosphoinositide signalling cascade. This disruption impairs chondrocyte differentiation and delays ossification, resulting in severe short-limb dwarfism, hypomineralisation, and frequently fatal respiratory compromise in infancy. The speculative mechanistic bridge to Dulaglutide lies in the fact that GLP-1RA signalling can modestly activate PI3K/Akt pathways downstream — pathways that partially overlap with the SHIP2-regulated phosphoinositide network.

This link is, however, mechanistically tenuous. The repurposing rationale embedded in this Evidence Pack explicitly flags that no clinical or preclinical data supports GLP-1RA use in skeletal developmental disorders. The high TxGNN score (97.05%) most likely reflects a structural artefact of the knowledge graph, where rare disease nodes with few connections can yield inflated prediction scores. This prediction should not be interpreted as a genuine therapeutic signal without further mechanistic validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

No ARTG entries for Dulaglutide were retrieved in this data pull. Clinicians should note that Dulaglutide (Trulicity®) has TGA registration status in other data sources; the absence of records here reflects a data gap rather than confirmed non-availability. Please verify current listing directly via the [TGA ARTG Public Summary](https://www.tga.gov.au/resources/artg).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Dulaglutide in this report are rated L5, supported by zero clinical trials and zero published literature. The top-ranked prediction — Opsismodysplasia — is a structurally rare disease node in the knowledge graph with no biologically plausible or empirically tested connection to GLP-1RA pharmacology; the high prediction score is almost certainly a graph topology artefact rather than a genuine therapeutic opportunity.

**To proceed, the following is needed:**

- **Confirm ARTG status**: Retrieve and verify Dulaglutide's current TGA registration and approved Australian indications directly from the ARTG database
- **Obtain MOA data**: Query DrugBank (DB09045) to populate the missing mechanism of action — required before any mechanistic plausibility analysis can proceed
- **Retrieve TGA Product Information (PI)**: Download and parse the PI to populate key warnings and contraindications (currently blocking safety pre-screening)
- **Preclinical literature scoping**: Commission a targeted search on GLP-1RA effects in phosphoinositide signalling disorders and skeletal dysplasia animal models before progressing this hypothesis
- **Rare disease specialist review**: Any further investigation of Opsismodysplasia as a target indication requires input from a clinical geneticist or paediatric metabolic bone disease specialist
- **Reassess all 10 candidates**: Three candidates in the lipodystrophy cluster (drug-induced, centrifugal, idiopathic — Ranks 5, 7, 9) carry a "Research Question" recommendation rather than "Hold" and may represent a more scientifically tractable cluster for further exploration, given GLP-1RA's known effects on adipose tissue metabolism
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

