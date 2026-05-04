---
layout: default
title: Donepezil
parent: 僅模型預測 (L5)
nav_order: 164
evidence_level: L5
indication_count: 10
---

# Donepezil
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

# Donepezil: From Alzheimer's Disease to Psychogenic Movement Disorders

## One-Sentence Summary

Donepezil is a selective acetylcholinesterase inhibitor (AChEI) widely used for the symptomatic treatment of Alzheimer's disease and other dementias. The TxGNN model predicts it may have utility in **Psychogenic Movement Disorders**, however **no clinical trials** and **no supporting publications** have been identified for this specific indication to date, yielding minimal confidence in this repurposing direction.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Alzheimer's disease (symptomatic treatment of dementia) |
| Predicted New Indication | Psychogenic Movement Disorders |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 |
| Australia Market Status | No ARTG entries found in dataset — verify directly via TGA database |
| Number of ARTG Entries | 0 (data gap — see Australia Market Information below) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, Donepezil inhibits acetylcholinesterase (AChE) — the enzyme responsible for breaking down acetylcholine at the synapse — thereby enhancing cholinergic neurotransmission throughout the central nervous system. This mechanism underpins its well-established clinical efficacy in Alzheimer's disease, where progressive loss of cholinergic neurons in the basal forebrain is a defining pathological feature.

Psychogenic movement disorders (also referred to as functional movement disorders, or classified under functional neurological symptom disorder) are characterised by involuntary movements arising in the absence of a structural neurological lesion or clearly defined neurotransmitter deficiency. Unlike organic movement disorders — where disrupted dopaminergic or cholinergic balance is well characterised — psychogenic movement disorders are driven by maladaptive neuroplasticity, psychological factors, and central sensitisation mechanisms. No established pathophysiological link between the cholinergic system and psychogenic movement disorders has been identified in the current literature.

The high TxGNN prediction score (99.23%) is most likely an artefact of knowledge graph topology — specifically, indirect proximity between Donepezil's drug node and the broad "movement disorder" disease cluster — rather than a reflection of any specific mechanistic relationship. The model's prediction for this indication should be interpreted with caution, as graph-based predictions for functionally heterogeneous disease categories can yield spuriously high scores.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

No ARTG entries were retrieved for Donepezil in this dataset. This is likely a data retrieval gap rather than a true absence from the Australian market — Donepezil (e.g., brand name Aricept and multiple generics) is a well-established medicine that has regulatory approval in comparable markets globally. Clinicians and researchers should verify current ARTG registration status directly via the [TGA ARTG Public Summary](https://www.tga.gov.au/resources/artg) before drawing conclusions about Australian market availability.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

> **Note:** Safety data (key warnings, contraindications, and drug–drug interactions) could not be retrieved in this evidence pack. Before clinical consideration, the full TGA PI should be reviewed, with particular attention to: cholinergic side effects (bradycardia, GI disturbance, syncope), interactions with anticholinergic agents, and use in patients with cardiac conduction abnormalities.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical or preclinical evidence supporting the use of Donepezil in psychogenic movement disorders, and no plausible mechanistic link exists between cholinergic enhancement and the pathophysiology of functional neurological symptoms. The high TxGNN score reflects knowledge graph structure, not therapeutic signal.

**To proceed, the following is needed:**

- **Regulatory data gap resolution:** Confirm Australian TGA/ARTG registration status for Donepezil directly via the TGA database; this evidence pack shows 0 entries, which likely reflects a query retrieval issue
- **MOA data retrieval:** Query DrugBank (DB00843) to formally document Donepezil's full pharmacological profile, including receptor targets beyond AChE
- **Safety data gap resolution:** Download and parse the TGA Product Information to obtain approved warnings, contraindications, and drug interaction profiles
- **Targeted literature search:** Conduct a focused search for any cholinergic or neuroplasticity mechanisms proposed in functional neurological disorder research to reassess biological plausibility
- **Consider pivoting to higher-evidence indications:** Within the same TxGNN prediction run, two indications — **lingual-facial-buccal dyskinesia (tardive dyskinesia)** (rank 8, L3, Proceed with Guardrails) and **glaucoma** (rank 10, L3, Proceed with Guardrails) — have stronger evidentiary support and more clearly defined mechanistic rationales; these may warrant prioritisation over psychogenic movement disorders for any repurposing investment

---

> **Disclaimer:** This report is intended for research purposes only and does not constitute medical advice. Drug repurposing candidates identified by computational models require clinical validation before any therapeutic application. All information should be verified against current TGA-approved Product Information.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

