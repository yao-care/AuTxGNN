---
layout: default
title: Ferrous Sulfate Anhydrous
parent: 僅模型預測 (L5)
nav_order: 274
evidence_level: L5
indication_count: 10
---

# Ferrous Sulfate Anhydrous
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

# Ferrous Sulfate Anhydrous: From Iron-Deficiency Anaemia to Vitamin B12- and Folate-Independent Constitutional Megaloblastic Anemia

## One-Sentence Summary

Ferrous sulfate anhydrous (DrugBank DB13257) is conventionally used to treat iron-deficiency anaemia, though this evidence pack contains no documented original indication or mechanism-of-action data. The TxGNN model's top prediction is **vitamin B12- and folate-independent constitutional megaloblastic anemia**, but this is currently supported by **zero clinical trials** and **zero publications**, and the model's own mechanistic annotation flags the score as likely reflecting semantic similarity ("anemia") rather than a genuine pharmacological link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (`original_indications` is empty; drug is not registered in Australia). Ferrous sulfate is conventionally indicated for iron-deficiency anaemia, but this is background knowledge, not sourced from the pack. |
| Predicted New Indication | Vitamin B12- and folate-independent constitutional megaloblastic anemia |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available for ferrous sulfate anhydrous in this evidence pack (data gap DG002, severity: High). Based on general pharmacology, ferrous sulfate corrects iron deficiency by replenishing substrate for haemoglobin synthesis — a mechanism specific to microcytic, iron-deficient anaemias.

The predicted indication, however, is a **constitutional (typically genetic) megaloblastic anaemia that is explicitly independent of vitamin B12 and folate** — and by extension, unrelated to iron status. Megaloblastic anaemias of this type arise from defects in DNA synthesis (e.g., thiamine-responsive megaloblastic anaemia), not from a lack of iron. Supplementing iron would not correct this underlying defect.

The evidence pack's own repurposing rationale for this candidate acknowledges this mismatch directly: the high TxGNN score likely reflects the model associating the two conditions through the shared word "anemia" in the knowledge graph, rather than a real shared mechanism. Notably, a lower-ranked candidate in this same pack — **Plummer-Vinson syndrome** (rank 2, L4/S1) — has a much stronger mechanistic basis, since iron-deficiency anaemia is the textbook aetiology of that condition and iron repletion is standard treatment. That candidate currently lacks trial/literature evidence in this pack (a data gap, not a mechanistic gap) and may warrant separate follow-up.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Australia Market Information

Ferrous sulfate anhydrous currently has no ARTG entries — market status is "Not marketed" with 0 recorded licences in this evidence pack.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication lacks both clinical and literature support, and the model's own mechanistic annotation identifies the prediction as a probable knowledge-graph artefact (semantic overlap on "anemia") rather than a biologically plausible mechanism. Combined with the drug's non-marketed status in Australia and missing MOA/safety data, this candidate does not meet the threshold to proceed.

**To proceed, the following is needed:**
- Confirmed original indication and mechanism-of-action data for ferrous sulfate anhydrous (DG002)
- TGA/PI-sourced warnings and contraindications (DG001 — currently blocking safety review)
- If pursuing an iron-related repurposing angle, targeted evidence collection for Plummer-Vinson syndrome (rank 2) instead, given its stronger mechanistic rationale
- Independent expert review before treating any candidate in this pack as more than a preliminary signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

