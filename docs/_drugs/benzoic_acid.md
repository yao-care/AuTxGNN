---
layout: default
title: Benzoic Acid
parent: 僅模型預測 (L5)
nav_order: 81
evidence_level: L5
indication_count: 10
---

# Benzoic Acid
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

# Benzoic Acid: From Antiseptic/Preservative to Bronchitis

## One-Sentence Summary

Benzoic acid is a simple aromatic organic acid with known weak antimicrobial and preservative properties, used historically in combination topical antifungal preparations (e.g., Whitfield's ointment), but with no approved systemic therapeutic indication on the Australian Register of Therapeutic Goods (ARTG).
The TxGNN model predicts it may be effective for **Bronchitis**, with **0 clinical trials** and **2 publications** (both indirect) currently identified in support of this direction.
The overall evidence base is extremely limited, and this prediction is considered model-generated speculation at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved therapeutic indication in Australia |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank (recorded as a data gap). Based on general pharmacological knowledge, benzoic acid is a simple aromatic carboxylic acid that exhibits weak broad-spectrum antimicrobial activity, primarily by disrupting microbial cell membrane function and inhibiting cellular metabolic enzymes under acidic conditions. It is classified as a food preservative (E210) and has historically been used in topical combination preparations (e.g., Whitfield's ointment with salicylic acid) for superficial fungal skin infections. Some limited anti-inflammatory properties have been attributed to the benzoic acid scaffold through indirect structural relationships.

The theoretical rationale linking benzoic acid to bronchitis relies on two speculative pathways: (1) its weak antimicrobial properties could theoretically reduce the bacterial pathogen burden in bacterial bronchitis; and (2) putative mild anti-inflammatory effects might attenuate airway mucosal inflammation. However, both pathways remain entirely theoretical — no direct mechanistic studies in airway cells or animal models have been conducted with benzoic acid itself.

It is important to note that the two publications retrieved by the search algorithm are both tangentially related at best. One reviews repaglinide (a *carbamoylmethyl benzoic acid derivative*), and the other investigates soluble epoxide hydrolase inhibitors in COPD. Neither provides direct evidence for benzoic acid activity in bronchitis. The high TxGNN score (99.98%) likely reflects structural and network proximity in the knowledge graph rather than accumulated clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11577798](https://pubmed.ncbi.nlm.nih.gov/11577798/) | 2001 | Review | *Drugs* | Review of repaglinide — a **carbamoylmethyl benzoic acid derivative** — for type 2 diabetes mellitus. Connection to bronchitis is indirect; the benzoic acid scaffold is noted only as part of the parent molecule's chemical description. |
| [22180869](https://pubmed.ncbi.nlm.nih.gov/22180869/) | 2012 | Animal/Preclinical | *Am J Respir Cell Mol Biol* | Soluble epoxide hydrolase inhibitor (sEHI) demonstrated anti-inflammatory effects in a tobacco smoke-induced COPD rat model encompassing bronchitis pathology. Benzoic acid is not the study drug; this paper is disease-context evidence only. |

> **Note:** Neither publication provides direct evidence for benzoic acid efficacy in bronchitis. Both are rated as indirect/tangential references (relevance pending formal assessment).

---

## Australia Market Information

Benzoic acid (DB03793) has **no current ARTG registrations** in Australia. It is not a marketed therapeutic product on the TGA register.

> For general compound safety reference, consult international regulatory databases such as the FDA GRAS (Generally Recognised As Safe) list and European Food Safety Authority (EFSA) dossiers, where benzoic acid is assessed primarily as a food additive.

---

## Safety Considerations

Safety data specific to benzoic acid as a therapeutic agent is not available through the standard Australian regulatory channels, as the compound holds no ARTG registration and no TGA-approved Product Information (PI) document exists.

Please refer to international safety databases (e.g., DrugBank, WHO, FDA) for available compound-level safety information. Key considerations based on general chemical knowledge include:

- **Known sensitivities**: Benzoic acid and benzoates can provoke hypersensitivity reactions (urticaria, asthma exacerbation) in susceptible individuals, particularly those with aspirin sensitivity
- **Interactions**: No drug–drug interaction data was returned from the DDI query (result: not found, 0 interactions identified)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Benzoic acid has no approved therapeutic indication in Australia, no ARTG registrations, no clinical trials in bronchitis, and no direct preclinical evidence supporting its use for this condition. The two publications retrieved are peripheral references only. The TxGNN prediction score of 99.98% reflects network-level proximity in the knowledge graph — not clinical evidence — and is consistent with an L5 evidence classification (model prediction only). Proceeding to drug repurposing development is not justified at this stage.

**To proceed, the following would be needed:**

- **MOA characterisation**: Obtain full DrugBank mechanism of action data and conduct a targeted literature review on benzoic acid's pharmacodynamic effects in airway biology
- **Preclinical validation**: In vitro and in vivo studies specifically evaluating benzoic acid antimicrobial and anti-inflammatory effects in bronchitis models before any clinical translation is considered
- **Formulation feasibility assessment**: Determine whether a viable systemic or inhaled dosage form of benzoic acid is achievable (benzoic acid is currently used only topically or as a food preservative)
- **Safety profile clarification**: Retrieve and review TGA and international regulatory dossiers for safety data pertinent to therapeutic (non-food) use
- **KG artefact investigation**: Evaluate whether the TxGNN bronchitis prediction reflects genuine pharmacological signal or a knowledge graph clustering artefact (similar to the fibromatosis cluster observed at ranks 5–7)

---

> **Disclaimer:** This report is intended for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require rigorous clinical validation before application. This prediction was generated by the TxGNN model and has not been independently verified through clinical study.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

