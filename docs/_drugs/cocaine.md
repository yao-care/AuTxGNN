---
layout: default
title: Cocaine
parent: 僅模型預測 (L5)
nav_order: 126
evidence_level: L5
indication_count: 10
---

# Cocaine
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

# Cocaine: From Local Anaesthesia (Historical) to Cauda Equina Syndrome

## One-Sentence Summary

Cocaine is a naturally derived tropane alkaloid historically deployed as the world's first clinical local anaesthetic (1880s–1930s), primarily in ENT and ophthalmic procedures; it is not currently registered for any therapeutic indication in Australia.
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**,
with **0 clinical trials** and **1 publication** currently supporting this direction — none of which relate to cocaine as a treatment.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No current TGA-approved indication; historical use as topical local anaesthetic in ENT/ophthalmic surgery |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for this candidate. Based on established pharmacology, cocaine is a naturally occurring tropane alkaloid with two principal pharmacodynamic mechanisms: (1) reversible voltage-gated Na⁺ channel blockade, which halts axonal conduction and underpins its local anaesthetic properties; and (2) inhibition of monoamine (norepinephrine, dopamine, serotonin) reuptake transporters, producing sympathomimetic and CNS stimulant effects.

The TxGNN knowledge graph prediction most likely reflects cocaine's well-documented historical use in **spinal and epidural anaesthesia** (1884 onward), during which it was instilled intrathecally to produce lumbosacral sensory and motor blockade — anatomically overlapping with the cauda equina territory. The knowledge graph may have encoded this anatomical association without distinguishing between "anaesthetic applied near the cauda equina" and "treatment of cauda equina syndrome."

However, this distinction is clinically critical. Cauda equina syndrome (CES) is an acute neurosurgical emergency caused by mechanical compression of the L2–S5 nerve roots, manifesting as bladder/bowel dysfunction, saddle anaesthesia, and lower limb weakness. The definitive treatment is urgent surgical decompression. Cocaine's Na⁺ channel blockade would temporarily mask sensory symptoms without addressing the underlying compression, actively endangering the patient by delaying surgery. There is no mechanistic pathway by which cocaine would decompress, reduce oedema, or otherwise reverse the structural pathology of CES. The single identified publication is an unrelated case report on lumbosacral disc pathology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for cocaine in cauda equina syndrome.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31528422](https://pubmed.ncbi.nlm.nih.gov/31528422/) | 2019 | Case Report | Surgical Neurology International | Case report of distal cauda equina syndrome secondary to lumbosacral disc pathology. Describes the full symptom complex of CES (urinary retention, saddle hypoanaesthesia, lower limb weakness) and reviews the diagnostic literature. No connection to cocaine as treatment. |

---

## Australia Market Information

Cocaine is not registered on the Australian Register of Therapeutic Goods (ARTG). There are no current TGA-approved products, licensed indications, or ARTG entries. In Australia, cocaine is a **Schedule 8 Controlled Drug** under the *Poisons Standard (Compendia)* and the *Therapeutic Goods Act 1989*. Any clinical or research use requires state/territory authority approval and relevant Commonwealth permits.

---

## Safety Considerations

All structured safety data (key warnings, contraindications, drug interactions) were not retrievable for this candidate. Please refer to the TGA-approved Product Information and Schedule 8 prescribing regulations for applicable safety guidance.

Notable safety considerations from published literature relevant to evaluating this candidate include:

- **Cardiovascular toxicity**: Coronary artery vasospasm, ventricular arrhythmias, QTc prolongation, and hypertensive crisis are well-documented risks at clinical doses.
- **CNS toxicity**: Seizure threshold lowering, sympathetic hyperactivation.
- **Dependence and abuse liability**: Cocaine carries high addiction potential; Schedule 8 classification reflects significant misuse risk in Australia.
- **Local tissue toxicity**: Chronic exposure causes mucosal ischaemia and necrosis (cocaine-induced midline destructive lesions), particularly relevant to intranasal/topical routes.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for this repurposing candidate is at the lowest possible tier (L5 — model prediction only), with zero supporting clinical trials and a single unrelated case report. More importantly, the mechanistic rationale is fundamentally incompatible with the disease biology: cauda equina syndrome is an anatomical emergency requiring surgical decompression, and any symptom-masking effect from cocaine would constitute an active clinical harm by delaying definitive treatment.

**To proceed, any further consideration would require:**
- A formal mechanistic justification demonstrating a disease-modifying (not symptom-masking) pathway for cocaine in CES — none currently exists
- Regulatory feasibility assessment under Schedule 8 controlled substance legislation in Australia, including TGA clinical trials authorisation and state/territory permits
- A comparative safety analysis against standard-of-care (urgent surgical decompression), acknowledging cocaine's cardiovascular and addiction risk profile
- Review of all 10 TxGNN-predicted indications for this candidate: notably, all 10 return a **Hold** or **Research Question only** recommendation, suggesting no viable near-term repurposing pathway exists for cocaine across the predicted indication set

> ⚠️ **YMYL Disclaimer**: This report is generated by a predictive AI model (TxGNN) and is intended for **research reference only**. It does not constitute medical advice, clinical guidance, or a recommendation to administer any substance. All drug repurposing candidates require independent clinical validation before any therapeutic application. The use of Schedule 8 substances in Australia is subject to strict regulatory controls.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

