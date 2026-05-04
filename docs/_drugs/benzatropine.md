---
layout: default
title: Benzatropine
parent: 僅模型預測 (L5)
nav_order: 79
evidence_level: L5
indication_count: 10
---

# Benzatropine
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

# Benzatropine: From Parkinson's Disease to PLA2G6-Associated Neurodegeneration

## One-Sentence Summary

Benzatropine is an established anticholinergic and dopamine reuptake inhibitor, historically used as adjunct therapy for Parkinson's disease and drug-induced extrapyramidal symptoms, though it holds no current TGA registration in Australia.
The TxGNN model predicts it may be effective for **PLA2G6-Associated Neurodegeneration (PLAN)**,
however only **1 case report** is available in the literature — and this document describes a treatment *complication* rather than any therapeutic benefit in PLAN.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No TGA registration; known historical use: Parkinson's disease adjunct therapy / drug-induced extrapyramidal symptoms |
| Predicted New Indication | PLA2G6-Associated Neurodegeneration (PLAN) |
| TxGNN Prediction Score | 99.17% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, Benzatropine acts as both an **anticholinergic agent** (blocking muscarinic acetylcholine receptors in the striatum) and a **dopamine transporter (DAT) inhibitor** (increasing synaptic dopamine levels). These dual properties underpin its established clinical role in managing the motor symptoms of Parkinson's disease and drug-induced extrapyramidal syndromes such as acute dystonia and pseudo-parkinsonism.

PLA2G6-Associated Neurodegeneration (PLAN) is caused by loss-of-function mutations in the *PLA2G6* gene, leading to defective lysosomal membrane phospholipid remodelling and pathological iron deposition in the basal ganglia and cerebellum — a condition classified under Neurodegeneration with Brain Iron Accumulation (NBIA). The primary disease driver (aberrant phospholipase A2 activity and downstream lipid metabolic failure) is mechanistically **distinct** from the cholinergic or dopaminergic pathways that Benzatropine targets. While anticholinergic therapy may offer modest symptomatic palliation of motor rigidity or tremor in affected patients, this is entirely symptomatic management and does not address the underlying iron accumulation or phospholipid metabolism defect.

The TxGNN high prediction score (99.17%) most likely reflects topological proximity between PLAN and other basal-ganglia / movement disorder nodes within the knowledge graph, rather than genuine biological plausibility. In the absence of any mechanistic evidence linking Benzatropine to iron homeostasis or PLA2G6 pathway modulation, the biological rationale for this prediction remains unsubstantiated at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [2486013](https://pubmed.ncbi.nlm.nih.gov/2486013/) | 1989 | Case Report | Acta Gastro-Enterologica Belgica | A 12-year-old with Hallervorden-Spatz syndrome (an NBIA subtype historically overlapping with PLAN) developed superior mesenteric artery syndrome — an intestinal obstruction — **during** benztropine treatment. Predisposing factors included opisthotonos and benztropine-induced duodenal hypotonia. This report documents a **drug complication**, not evidence of therapeutic efficacy in PLAN. |

---

## Australia Market Information

Benzatropine is currently **not marketed in Australia** and holds no ARTG registrations. As of the data cut-off (2026-04-05), no licensed product exists on the Australian Register of Therapeutic Goods. Healthcare professionals seeking access to Benzatropine for a patient in Australia would need to consider the TGA Special Access Scheme (SAS) or Authorised Prescriber pathways before any clinical use.

---

## Safety Considerations

No TGA-approved Product Information (PI) is available as the product is not registered in Australia. Please refer to international regulatory sources (e.g., US FDA label, EMA SmPC) for comprehensive safety data. Key considerations based on Benzatropine's known pharmacological class include:

- **Anticholinergic adverse effects**: Dry mouth, urinary retention, constipation, blurred vision, tachycardia
- **Central nervous system effects**: Confusion, hallucinations, memory impairment — risk elevated in elderly and paediatric populations
- **Hyperthermia risk**: Impaired thermoregulation in hot environments
- **Contraindication considerations**: Narrow-angle glaucoma, prostatic hypertrophy, myasthenia gravis, megacolon

Please refer to TGA-approved PI or international product information for complete warnings and contraindications before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence base for Benzatropine in PLA2G6-associated neurodegeneration sits at the lowest tier (L5 — model prediction only, no supporting studies). The sole identified literature reference documents a serious treatment complication rather than any therapeutic benefit, and there is no established mechanistic pathway by which Benzatropine could address the core PLAN pathology (PLA2G6 mutation, lysosomal phospholipid dysfunction, brain iron accumulation).

**To proceed, the following would be needed:**
- Formal mechanistic evidence linking anticholinergic or DAT-inhibitory pathways to PLA2G6 function, lysosomal lipid metabolism, or brain iron homeostasis
- Preclinical data (e.g., *PLA2G6*-knockout cell or animal models) assessing Benzatropine's effects on iron deposition or phospholipid remodelling
- A reassessment once DrugBank MOA data and TGA/international PI safety data are obtained (currently flagged as data gaps DG001 and DG002)
- **Note for reviewers**: The **ADHD indication (Rank 2, L4 evidence)** presents a substantially more pharmacologically plausible repurposing hypothesis — Benzatropine's DAT inhibition mirrors the core mechanism of methylphenidate — and may warrant a dedicated separate evaluation report with a Research Question recommendation

---

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. All content should be interpreted in light of the data gaps identified in this evidence pack.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

