---
layout: default
title: Entacapone
parent: 僅模型預測 (L5)
nav_order: 189
evidence_level: L5
indication_count: 10
---

# Entacapone
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

# Entacapone: From Parkinson's Disease to PLA2G6-Associated Neurodegeneration

## One-Sentence Summary

Entacapone is a selective, reversible COMT (catechol-O-methyltransferase) inhibitor, used internationally as adjunct therapy for Parkinson's disease to prolong the dopaminergic effect of levodopa/carbidopa.
The TxGNN model ranks **PLA2G6-Associated Neurodegeneration (PLAN)** as its top predicted new indication, however **no clinical trials or published literature** currently support this direction.
Across all 10 predicted indications, evidence is uniformly limited (L4–L5); the most clinically plausible candidates are **Lewy body dementia** (rank 7) and **juvenile Parkinsonism** (rank 4), both designated Research Questions pending further investigation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Parkinson's disease (adjunct to levodopa/carbidopa) |
| Top Predicted Indication | PLA2G6-Associated Neurodegeneration |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, Entacapone is a peripheral COMT inhibitor — it blocks catechol-O-methyltransferase to reduce the peripheral breakdown of levodopa, thereby sustaining dopamine availability in the nigrostriatal pathway. Its efficacy as an adjunct in Parkinson's disease is well established internationally, and its mechanism is fundamentally dopaminergic.

PLA2G6-Associated Neurodegeneration (PLAN) is a form of Neurodegeneration with Brain Iron Accumulation (NBIA), caused by loss-of-function mutations in the *PLA2G6* gene encoding phospholipase A2 group VI. The core pathological mechanism involves disrupted phospholipid membrane homeostasis and secondary iron accumulation in the brain — pathways that do not directly intersect with COMT inhibition or dopamine metabolism.

The high TxGNN score (99.76%) most likely reflects graph-level proximity between neurodegenerative disease nodes in the knowledge graph, rather than a genuine biological connection. This is a recognised limitation of graph neural network models: topological similarity can produce high prediction scores without direct mechanistic rationale. The evidence pack's own mechanistic analysis explicitly notes that PLAN and the COMT/dopamine pathway "have no direct intersection." The recommendation for this indication accordingly remains **Hold**.

---

## Predicted Indications — Full Landscape

This evidence pack covers 10 TxGNN-predicted indications. Since Entacapone is not marketed in Australia and all predictions lack Phase 2+ clinical evidence, the full landscape is presented below to support prioritisation decisions:

| Rank | Indication | TxGNN Score | Evidence Level | Decision | Mechanistic Plausibility |
|------|-----------|------------|----------------|----------|--------------------------|
| 1 | PLA2G6-associated neurodegeneration | 99.76% | L5 | **Hold** | Low — phospholipase/iron accumulation pathway, no dopaminergic link |
| 2 | Rasmussen subacute encephalitis | 99.73% | L5 | **Hold** | Very Low — autoimmune T-cell mediated neuronal destruction |
| 3 | Myelitis | 99.63% | L5 | **Hold** | Low — spinal cord inflammation, no established dopaminergic bridge |
| 4 | Paralysis agitans, juvenile, of Hunt | 99.60% | L5 | Research Question | **High** — juvenile Parkinsonism shares core nigrostriatal dopamine deficiency mechanism |
| 5 | Transaldolase deficiency | 99.43% | L5 | **Hold** | Very Low — pentose phosphate pathway metabolic disorder |
| 6 | Lethal infantile mitochondrial myopathy | 99.28% | L5 | **Hold** | ⚠️ Potentially harmful — Entacapone has in vitro mitochondrial Complex I inhibition signal |
| 7 | Lewy body dementia | 99.25% | L4 | Research Question | **Moderate** — significant dopaminergic deficit; preclinical evidence available |
| 8 | Fructose-1,6-bisphosphatase deficiency | 99.22% | L5 | **Hold** | Very Low — gluconeogenesis metabolic disorder |
| 9 | Polymicrogyria, perisylvian (with cerebellar hypoplasia and arthrogryposis) | 99.06% | L5 | **Hold** | None — congenital structural brain abnormality, not amenable to pharmacological repair |
| 10 | Progressive supranuclear palsy–corticobasal syndrome | 99.04% | L4 | Research Question | Low–Moderate — tauopathy; levodopa response generally poor (<20%) |

---

## Clinical Trial Evidence

### Top Prediction: PLA2G6-Associated Neurodegeneration

Currently no related clinical trials registered.

---

### Lewy Body Dementia (Rank 7 — Most Evidence Available)

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04246437](https://clinicaltrials.gov/study/NCT04246437) | Phase 1 | Recruiting | 40 | [¹⁸F]F-DOPA PET imaging study in autonomic failure patients with alpha-synucleinopathies (PD, MSA, DLB). Characterises dopaminergic neuronal integrity in LBD — imaging/biomarker study only, not an interventional treatment trial for Entacapone. Provides biological context for dopaminergic deficits in LBD. |

> **Note:** This trial does not evaluate Entacapone as a treatment. It cannot be used to infer therapeutic efficacy.

---

### Progressive Supranuclear Palsy–Corticobasal Syndrome (Rank 10)

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02994719](https://clinicaltrials.gov/study/NCT02994719) | Observational | Recruiting | 120 | Gait pattern analysis in neurological conditions including parkinsonian disorders (PSP-CBS). Pure observational study with no pharmacological intervention — provides phenotypic characterisation of PSP-CBS gait but cannot support any efficacy claim for Entacapone. |

---

## Literature Evidence

### Lewy Body Dementia (Rank 7)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23913715](https://pubmed.ncbi.nlm.nih.gov/23913715/) | 2013 | In vitro mechanistic study | Journal of Neuroscience Research | Examined effects of antiparkinsonian agents on β-amyloid and α-synuclein oligomer formation in vitro. Class-level relevance: COMT inhibitor-class agents may potentially modulate α-synuclein aggregation, a hallmark of LBD pathology. Indirect mechanistic evidence only. |
| [39259788](https://pubmed.ncbi.nlm.nih.gov/39259788/) | 2024 | iPSC organoid study | Science Advances | Modelled LBD pathology using SNCA-triplication iPSC-derived cortical organoids and identified candidate therapeutic compounds. Establishes a novel mechanistic framework for LBD cortical pathology but does not specifically test Entacapone. |
| [11268898](https://pubmed.ncbi.nlm.nih.gov/11268898/) | 2001 | Review | Presse Médicale | General Parkinson's disease review. Limited direct relevance to LBD repurposing; historical context for the clinical role of COMT inhibition. |

> No literature was identified for any other predicted indication, including the top-ranked PLA2G6-Associated Neurodegeneration.

---

## Australia Market Information

Entacapone is **not registered on the Australian Register of Therapeutic Goods (ARTG)**. There are no ARTG entries for this product.

Entacapone is approved internationally — available as Comtan® (standalone) and as part of Stalevo® (levodopa/carbidopa/entacapone) via EMA and FDA approval — but has not been approved by the Therapeutic Goods Administration (TGA). Any clinical use in Australia would require a **Special Access Scheme (SAS) Category B or C** application, or enrolment within a TGA-approved clinical trial.

---

## Safety Considerations

No TGA-approved Product Information is available, as Entacapone is not marketed in Australia. No drug interaction or contraindication data was retrievable via this evidence pack.

Please refer to the **EMA or FDA Product Information** for complete safety details. The following safety signals are specifically relevant to the repurposing candidates in this report:

- **Lewy body dementia (rank 7):** Increased dopaminergic stimulation via COMT inhibition may exacerbate hallucinations and psychiatric symptoms — a clinically significant safety-critical concern before any LBD repurposing trial is designed.
- **Lethal infantile mitochondrial myopathy (rank 6):** Entacapone has demonstrated mitochondrial Complex I inhibition in vitro at high doses, raising a plausible risk of worsening disease. This indication should be treated as a **potential harm signal** and excluded from further research planning.

---

## Conclusion and Next Steps

**Decision: Hold (portfolio-level)**

**Rationale:**
Entacapone has no TGA registration and no ARTG entries. Across all 10 TxGNN-predicted indications, no direct interventional clinical trial evidence for any new indication was identified. Seven of 10 predictions are assessed as Hold due to absent or implausible mechanistic rationale; one (lethal infantile mitochondrial myopathy) carries an active potential harm signal. The top-ranked prediction, PLA2G6-associated neurodegeneration, is most likely a graph proximity artefact and should not proceed.

**To advance Lewy body dementia (rank 7) as a Research Question, the following is needed:**
- Obtain EMA or FDA Product Information to complete the safety baseline assessment
- Identify or commission preclinical studies specifically testing Entacapone (not levodopa alone) in validated LBD animal or organoid models
- Address the safety-critical question of hallucination and psychosis risk with COMT inhibition in LBD patients before any clinical protocol is developed
- Define a target patient subgroup (e.g., early-stage LBD with documented dopaminergic deficit and retained levodopa sensitivity)

**To advance juvenile Parkinsonism (rank 4) as a Research Question, the following is needed:**
- Paediatric pharmacokinetic and safety data for Entacapone — currently absent from the published literature
- Assessment of long-term developmental consequences of sustained COMT inhibition in a paediatric central nervous system
- Review of existing case reports or international paediatric neurology registry data from centres treating juvenile Parkinsonism

**For the remaining 8 predictions (Hold):** No further investigation is recommended at this stage. Lethal infantile mitochondrial myopathy (rank 6) should be explicitly flagged as a potential harm signal and removed from any future candidate shortlisting.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

