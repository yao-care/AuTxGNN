---
layout: default
title: Sulthiame
parent: 僅模型預測 (L5)
nav_order: 645
evidence_level: L5
indication_count: 10
---

# Sulthiame
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

# Sulthiame: From Anticonvulsant Therapy to Cauda Equina Syndrome

## One-Sentence Summary

Sulthiame is a carbonic anhydrase inhibitor with GABAergic activity, used as an anticonvulsant; it is not currently marketed in Australia and no approved indication text is available in this evidence pack. The TxGNN model's top prediction is **Cauda Equina Syndrome**, but this is supported by **zero clinical trials and zero publications**, and the model's own mechanistic assessment flags the result as a likely false positive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (DrugBank record contains no listed indication; sulthiame is generally classified as an anticonvulsant) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for sulthiame is not available in this evidence pack. Based on the information that is available (drawn from the model's own rationale), sulthiame is a carbonic anhydrase inhibitor with GABAergic anticonvulsant activity, used historically for seizure disorders.

Cauda equina syndrome, however, is an acute surgical emergency caused by mechanical compression of the lumbosacral nerve roots — it is a structural/compressive condition, not one driven by GABAergic or carbonic-anhydrase-related pathways. There is no established pharmacological or clinical rationale linking sulthiame's mechanism to this condition.

Importantly, the evidence pack's own repurposing rationale concludes that the high TxGNN score for this indication "likely reflects a spurious association from knowledge-graph node proximity (nervous system cluster) rather than genuine mechanistic evidence." In other words, the model's own output actively cautions against treating this top-ranked score as clinically meaningful.

For context, TxGNN generated nine further candidate indications for sulthiame (ranks 2–10, scores 99.3–99.9%), including irritable bowel syndrome, neurogenic bladder, and several cardiac/allergic conditions. All carry the same L5 evidence level (no trials, no literature), and several are flagged in the source rationale as obsolete disease terms (e.g. "obsolete neurogenic bladder," "MVP1," "neurocirculatory asthenia") or mechanistically implausible (e.g. anaphylaxis, mitral valve prolapse). None currently rises above the top-ranked candidate in credibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Sulthiame has no ARTG entries and is not currently marketed in Australia. No product information (PI) exists locally for this drug.

---

## Safety Considerations

No safety data (key warnings, contraindications, or drug interactions) were available in this evidence pack, and no DDI records were found for sulthiame. This is flagged in the evidence pack as a **Blocking data gap** (missing TFDA/regulatory PI warnings and contraindications), which by itself prevents this candidate from advancing to the S1 safety pre-screening stage.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (cauda equina syndrome) has no supporting clinical trials or literature and is assessed — by the model's own mechanistic rationale — as a probable knowledge-graph artefact rather than a genuine pharmacological signal. The drug is also unregistered in Australia, and a Blocking data gap in safety/PI information prevents any safety pre-screening.

**To proceed, the following is needed:**
- Confirmed mechanism of action data for sulthiame (DrugBank/primary literature) — currently a data gap (DG002)
- TFDA/TGA-equivalent product information covering warnings and contraindications — currently a Blocking data gap (DG001)
- Independent pharmacological or preclinical evidence connecting sulthiame to cauda equina syndrome (or any of the other 9 candidate indications) before this moves beyond model-prediction-only status
- Ongoing monitoring for any new trial registrations or publications, given none currently exist for any of the 10 predicted indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

