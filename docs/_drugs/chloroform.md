---
layout: default
title: Chloroform
parent: 僅模型預測 (L5)
nav_order: 145
evidence_level: L5
indication_count: 10
---

# Chloroform
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

# Chloroform: From Historical General Anaesthetic Use to Insomnia

## One-Sentence Summary

Chloroform (DrugBank DB11387) is a chlorinated solvent with a long history as an inhalational general anaesthetic, though it has no current registered therapeutic indication and no product licence in Australia. The TxGNN model predicts a possible association with **Insomnia**, with a very high similarity score (**98.87%**), but this is currently supported only by **0 clinical trials** and **2 publications**, neither of which directly studies chloroform's effect on sleep. Given the near-total absence of direct evidence and chloroform's known toxicity profile, this candidate should be treated with significant caution.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No current registered indication on file; historically used as an inhalational general anaesthetic (mechanism of action and formal indication data are gaps — see below) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 98.87% |
| Evidence Level | L5 (model prediction only, no supportive clinical studies) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for chloroform is not available in this evidence pack (flagged as a High-severity data gap). Based on known historical use, chloroform is a central nervous system depressant that was used as a general anaesthetic through the 19th and 20th centuries before being withdrawn from clinical anaesthetic practice due to hepatotoxicity, cardiac arrhythmogenicity, and carcinogenicity concerns. The TxGNN model's rationale for this prediction is that CNS-depressant agents may share knowledge-graph connections with sedative/hypnotic drugs used for insomnia (e.g., via a hypothesised GABA-ergic pathway), which is a plausible topological reason for a high similarity score even without direct study evidence.

However, this mechanistic link is theoretical only. Of the two publications retrieved, neither is a direct pharmacological study of chloroform for sleep: one is a docking/bioactivity study of an unrelated plant-derived compound (dinaphthodiospyrol G) where chloroform's role is unclear, and the other is a hepatoprotection study of *Ziziphus jujuba* root bark that mentions insomnia only as one of many traditional folk uses of the plant itself — not as a chloroform-specific finding. Neither publication constitutes evidence that chloroform treats insomnia.

It is also worth noting that chloroform's other TxGNN-predicted associations (not the focus of this report) include several that read as **toxicity signals rather than treatment opportunities** — for example, the literature most closely tied to the "enterocolitis" prediction describes a chloroform ingestion poisoning case with severe gastrointestinal injury and hepatotoxicity. This reinforces that the knowledge graph is, in places, picking up harm-related associations, and supports a cautious interpretation of the insomnia signal as well.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32711536](https://pubmed.ncbi.nlm.nih.gov/32711536/) | 2020 | Preclinical/Docking review | BMC Complementary Medicine and Therapies | Evaluated analgesic, anti-inflammatory and sedative activity of a *Diospyros lotus*-derived compound; chloroform appears only incidentally (likely as an extraction solvent), not as the studied therapeutic agent |
| [27656145](https://pubmed.ncbi.nlm.nih.gov/27656145/) | 2016 | Preclinical (animal) | Frontiers in Pharmacology | Studied hepatoprotective effects of *Ziziphus jujuba* root bark fractions; insomnia is mentioned only as one of the plant's traditional folk uses, with no chloroform-specific efficacy data |

Neither publication provides direct evidence that chloroform is effective for insomnia.

---

## Australia Market Information

Chloroform currently has no ARTG entries and is **not marketed** in Australia. There is no TGA-approved Product Information for chloroform as a therapeutic good to reference.

---

## Safety Considerations

Formal safety data (key warnings, contraindications, drug interactions) is not currently available for chloroform in this evidence pack, and the TGA/regulatory warning data needed for an initial safety screen (S1) is a **Blocking** data gap. Please refer to the TGA-approved Product Information for safety information once available.

Separately, literature captured elsewhere in this evidence pack (outside the formal safety dataset) is worth flagging for clinical awareness:
- A published case report ([PMID 27788591](https://pubmed.ncbi.nlm.nih.gov/27788591/)) documents chloroform ingestion causing severe gastrointestinal injury, hepatotoxicity, and dermatitis.
- Chloroform's historical withdrawal from anaesthetic practice was driven by known hepatotoxicity and cardiac arrhythmia risk (myocardial sensitisation to catecholamines).

These are not part of the structured safety dataset but are directly relevant to any risk-benefit assessment of this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The insomnia prediction is supported only by TxGNN's knowledge-graph score (L5, model prediction only) — there are no clinical trials and no literature that directly studies chloroform for sleep. Combined with the absence of mechanism-of-action data, the absence of any current Australian market presence, and chloroform's documented toxicity profile (hepatotoxic, cardiac arrhythmogenic, historically withdrawn from clinical use), the evidence does not currently support progressing this candidate.

**To proceed, the following is needed:**
- TGA/regulatory Product Information, warnings and contraindications (currently a Blocking data gap preventing initial safety screening)
- Confirmed mechanism of action data (High-severity data gap)
- Dedicated pharmacological or clinical studies of chloroform itself (not as an incidental extraction solvent) for insomnia or related sleep disorders
- A formal toxicological risk-benefit assessment given chloroform's known hepatotoxicity and cardiotoxicity, before any further repurposing consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

