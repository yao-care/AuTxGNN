---
layout: default
title: Edaravone
parent: 僅模型預測 (L5)
nav_order: 178
evidence_level: L5
indication_count: 10
---

# Edaravone
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

# Edaravone: From Acute Cerebral Infarction to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Edaravone is a free radical scavenger originally developed in Japan as a neuroprotective agent for acute cerebral infarction, and subsequently approved internationally for amyotrophic lateral sclerosis (ALS).
The TxGNN model's top prediction is **Heparin Cofactor 2 Deficiency** (score: 99.47%), however **no clinical trials or published literature** currently support this specific indication.
Importantly, the model also predicts efficacy in **ALS susceptibility** (rank 6, score: 98.79%), supported by **5 publications** — a clinically significant finding given Edaravone's established international approval for ALS.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute cerebral infarction; Amyotrophic lateral sclerosis (ALS) |
| Predicted New Indication (Rank 1) | Heparin Cofactor 2 Deficiency |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available from the regulatory data source. However, published literature confirms that Edaravone (MCI-186; 3-methyl-1-phenyl-2-pyrazolin-5-one) is a potent free radical scavenger. It works by quenching hydroxyl radicals (•OH) and inhibiting both •OH-dependent and •OH-independent lipid peroxidation, thereby protecting cells — particularly neurons and vascular endothelium — from oxidative damage. This mechanism underpins its established clinical use in acute cerebral infarction and ALS.

Heparin Cofactor II (HCII) deficiency is a hereditary coagulation disorder characterised by insufficient inhibition of thrombin and elastase, caused by a defect in the HCII protein itself. The core pathology is a protein-level coagulation defect rather than an oxidative stress-driven condition. While Edaravone's free radical scavenging activity may theoretically reduce pro-coagulant states triggered by endothelial oxidative stress, it cannot directly compensate for HCII functional loss.

The TxGNN high score (99.47%) for this indication most likely reflects indirect network connections in the knowledge graph — for instance, shared comorbidities involving vascular endothelial dysfunction and the "thrombosis ← oxidative stress" topology — rather than a causally supported therapeutic hypothesis. This prediction should be regarded as a mathematical correlation, not a clinically actionable finding at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Heparin Cofactor 2 Deficiency.

---

## Literature Evidence

Currently no related literature available for Heparin Cofactor 2 Deficiency.

---

## ⚠️ Clinically Important Finding: ALS Indications (Ranks 6–7)

> While the top-ranked TxGNN prediction has no supporting evidence, the model also predicts efficacy for **ALS susceptibility** (rank 6, score: 98.79%) and **ALS type 22** (rank 7, score: 98.77%). Edaravone is **already approved by the US FDA (2017) and Japan PMDA for ALS treatment**, with a completed Phase 3 RCT (Japan, n=137). The ALS indication is supported by 5 publications in this dataset and carries the strongest mechanistic rationale. **For Australian clinical consideration, the ALS indication is the most actionable candidate from this Evidence Pack.**

### ALS Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38474192](https://pubmed.ncbi.nlm.nih.gov/38474192/) | 2024 | Systematic/Narrative Review | Int J Mol Sci | Reviews Edaravone's •OH-quenching and anti-lipid peroxidation mechanisms; confirms clinical application in ALS and expanding use across neurodegenerative diseases |
| [32241621](https://pubmed.ncbi.nlm.nih.gov/32241621/) | 2020 | Pharmacology/Chemistry Review | Bioorg Med Chem | Chemical characterisation of Edaravone as a free radical scavenger; confirms regulatory approvals for both stroke and ALS; documents stable adduct formation relevant to bioactivity |
| [37565261](https://pubmed.ncbi.nlm.nih.gov/37565261/) | 2023 | Animal Study | Eur J Transl Myol | Proteomic profiling of wobbler ALS mouse model; elevated GFAP confirmed as astrogliosis marker; provides insight into neuroinflammatory components of ALS pathology |
| [36595221](https://pubmed.ncbi.nlm.nih.gov/36595221/) | 2023 | In vitro Mechanistic Study | FEBS Open Bio | Motor neurons susceptible to ferroptosis via GPx4-linked lipid peroxide accumulation — directly relevant to Edaravone's anti-lipid peroxidation mechanism of action |
| [40672281](https://pubmed.ncbi.nlm.nih.gov/40672281/) | 2025 | Animal Study (Preprint) | bioRxiv | TDP-43 overexpression in zebrafish motor neurons triggers MND-like phenotypes via gain-of-function mechanism; supports ROS-TDP-43 bidirectional relationship as target for Edaravone |

---

## Australia Market Information

Edaravone is currently **not registered with the TGA** and has no ARTG entries. No TGA-approved products are available in Australia.

For international regulatory context: Edaravone is approved by the US FDA (trade name *Radicava*) and Japan PMDA (trade name *Radicut*) for ALS treatment. Available formulations include intravenous infusion and oral suspension. Any supply in Australia would currently require either a TGA registration application or access via the Special Access Scheme (SAS Category B) or Authorised Prescriber pathway.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. As no TGA-approved product exists, clinicians should consult the FDA-approved Prescribing Information (*Radicava*) or Japan PMDA *Radicut* package insert for comprehensive safety data.

---

## Conclusion and Next Steps

### For Heparin Cofactor 2 Deficiency (Rank 1)

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction has no supporting clinical trials or published literature, and the mechanistic link between Edaravone's antioxidant mechanism and a primary coagulation protein deficiency is indirect at best. This is likely a knowledge-graph topology artefact rather than a clinically meaningful signal.

**To justify further investigation, the following would be needed:**
- Preclinical studies demonstrating any direct or indirect effect of Edaravone on HCII activity or thrombin inhibition
- Identification of an oxidative stress-mediated mechanism specific to HCII deficiency pathophysiology
- At minimum one published case report or mechanistic study

---

### For ALS / Motor Neuron Disease Indications (Ranks 6–7) — Recommended Priority

**Decision: Proceed with Guardrails**

**Rationale:**
Edaravone is already FDA- and PMDA-approved for ALS treatment, underpinned by a completed Phase 3 RCT (Japan, n=137). The mechanistic rationale — free radical scavenging targeting oxidative stress in motor neurons, with relevance to SOD1 mutation, TDP-43 pathology, and ferroptosis pathways — is well-established. The ALS indication should be prioritised for any Australian regulatory or clinical pathway consideration arising from this Evidence Pack.

**To proceed with the ALS indication in Australia, the following is needed:**
- Full TGA Product Information retrieval (via Special Access Scheme or import documentation) for complete local safety profiling
- Review of Australian ALS patient population size, unmet clinical need, and current standard-of-care landscape
- Assessment of available formulations (IV infusion and oral suspension) against Australian clinical infrastructure
- Pharmacoeconomic evaluation for potential PBS listing under the Life Saving Drugs Programme or equivalent pathway
- Confirmation of DDI profile in the Australian ALS population (polypharmacy context)

---

*⚠️ This report is intended for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. Evidence Pack version: v4 | Data cut-off: 4 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

