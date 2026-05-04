---
layout: default
title: Dabrafenib
parent: 僅模型預測 (L5)
nav_order: 137
evidence_level: L5
indication_count: 10
---

# Dabrafenib
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

# Dabrafenib: From BRAF V600 Mutation-Positive Melanoma to Choroideremia

## One-Sentence Summary

Dabrafenib is a selective BRAF V600 kinase inhibitor with established international use in BRAF mutation-positive melanoma and other solid tumours, but currently holds no Australian Register of Therapeutic Goods (ARTG) registration.
The TxGNN model assigns it the highest repurposing prediction score for **Choroideremia** — a rare X-linked inherited retinal dystrophy — at **98.63%**,
however there are currently **no clinical trials** and **no published literature** supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Australian ARTG registration data found (internationally approved for BRAF V600 mutation-positive melanoma and NSCLC) |
| Predicted New Indication | Choroideremia |
| TxGNN Prediction Score | 98.63% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available within this Evidence Pack. Based on known pharmacology, Dabrafenib (DB08912) is a potent selective inhibitor of mutant BRAF kinase — principally the V600E and V600K variants — that drives aberrant hyperactivation of the MAPK (RAS–RAF–MEK–ERK) signalling cascade. Internationally, Dabrafenib is approved (often combined with the MEK inhibitor trametinib) for unresectable or metastatic BRAF V600 mutation-positive melanoma, adjuvant melanoma, and BRAF-mutant non-small cell lung cancer. Its therapeutic principle is blockade of a specific oncogenic driver mutation, making it a mutation-selective rather than broadly cytotoxic agent.

Choroideremia is a rare X-linked recessive retinal degeneration caused by loss-of-function mutations in the *CHM* gene encoding Rab escort protein 1 (REP-1). REP-1 is critical for geranylgeranylation of Rab GTPases, which regulate intracellular membrane trafficking. Its deficiency causes progressive degeneration of the choroid, retinal pigment epithelium (RPE), and photoreceptors, typically leading to complete blindness in affected males by their 40s–50s. There is no established direct connection between the BRAF/MAPK pathway and CHM-related pathogenesis.

The TxGNN model's high prediction score (98.63%) most likely reflects indirect associations within the knowledge graph — such as shared apoptotic signalling or oxidative stress nodes in RPE cells — rather than a direct mechanistic rationale for BRAF inhibition in choroideremia. This is a speculative network-inference signal and should be regarded as a hypothesis-generating finding only, requiring substantial preclinical validation before any clinical consideration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy (selective BRAF V600 kinase inhibitor; not a conventional cytotoxic agent) |
| Myelosuppression Risk | Low — targeted mechanism does not primarily affect haematopoietic progenitors; myelosuppression is uncommon |
| Emetogenicity Classification | Low |
| Monitoring Items | Full blood count; liver function tests; renal function; fasting blood glucose (hyperglycaemia risk); skin assessment (cutaneous squamous cell carcinoma and keratoacanthoma); cardiac function (LVEF — cardiomyopathy risk); ophthalmology review (uveitis and retinal vein occlusion) |
| Handling Protection | Handle as per institutional oral anticancer drug policy; standard oral targeted therapy precautions apply |

---

## Safety Considerations

Please refer to the manufacturer's Product Information (PI) and relevant international regulatory authority documentation (e.g., FDA, EMA) for complete safety information, as Dabrafenib does not currently hold an Australian TGA registration. No drug interaction data or local PI warnings were retrievable from this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's top-ranked prediction for Dabrafenib is choroideremia (score 98.63%), but this is a purely computational inference with no established biological plausibility, no supporting clinical trials, and no published literature. The disease mechanism — CHM gene-related disruption of Rab GTPase prenylation — is biologically distant from Dabrafenib's known target (BRAF V600 kinase), and no preclinical data exists to bridge this gap.

> **Note for reviewers:** While choroideremia ranks first in the TxGNN model, the second-ranked prediction — **non-cutaneous melanoma** (score 98.48%, Evidence Level L2, *Proceed with Guardrails*) — is supported by over 40 registered clinical trials including completed Phase II and Phase III studies of Dabrafenib ± trametinib in BRAF V600-mutant melanoma subtypes (mucosal, conjunctival, acral lentiginous). Clinicians investigating Dabrafenib repurposing opportunities may find the non-cutaneous melanoma indication substantially more actionable.

**To proceed with choroideremia investigation, the following is needed:**

- Preclinical studies (in vitro and in vivo) to determine whether BRAF/MAPK inhibition produces any measurable biological effect in CHM-deficient RPE or photoreceptor cell models
- Mechanistic characterisation of potential cross-talk between MAPK signalling and Rab GTPase prenylation pathways in retinal tissue
- Complete MOA documentation retrieved from DrugBank (DB08912) to finalise the pharmacological profile
- Formal YMYL safety and ethical review prior to any clinical consideration in a progressive vision-loss patient population
- Assessment of Australian TGA Named Patient Program or Clinical Trial Notification (CTN) pathways should preclinical evidence emerge
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

