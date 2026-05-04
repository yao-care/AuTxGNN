---
layout: default
title: Aprepitant
parent: 僅模型預測 (L5)
nav_order: 54
evidence_level: L5
indication_count: 10
---

# Aprepitant
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

# Aprepitant: From Chemotherapy-Induced Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis

---

## One-Sentence Summary

Aprepitant (brand name Emend) is a selective neurokinin 1 (NK1) receptor antagonist globally approved for the prevention of chemotherapy-induced nausea and vomiting (CINV) and post-operative nausea and vomiting (PONV), although it is not currently registered on the Australian Register of Therapeutic Goods (ARTG).
The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, an ultra-rare X-linked condition involving constitutive V2 vasopressin receptor activation and dilutional hyponatraemia.
Currently, **no clinical trials** and **no publications** specifically support this repurposing direction, placing this prediction at Evidence Level 5 — model inference only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prevention of chemotherapy-induced and post-operative nausea and vomiting (CINV/PONV) — globally approved, not registered in Australia |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 — Model prediction only, no supporting clinical studies |
| Australia Market Status | Not marketed (no ARTG registration) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack (Data Gap DG002). Based on established pharmacology, Aprepitant is a selective, high-affinity antagonist of the human substance P/neurokinin 1 (NK1) receptor. It prevents substance P (SP) — a neuropeptide involved in the vomiting reflex — from binding to NK1 receptors in the central nervous system. This antiemetic mechanism is well validated in clinical use for CINV/PONV. Notably, Aprepitant also demonstrates meaningful central nervous system penetration, with a cerebrospinal fluid to plasma ratio of approximately 26%, which is relevant to any CNS or neurogenic repurposing application.

Nephrogenic Syndrome of Inappropriate Antidiuresis is a rare condition caused by gain-of-function mutations in the *AVPR2* gene (encoding the vasopressin V2 receptor), leading to constitutive receptor activation and water retention despite low or undetectable plasma arginine vasopressin (AVP) levels. Preclinical literature suggests that substance P and NK1 receptors are expressed in the renal collecting duct and in hypothalamic nuclei regulating vasopressin release; NK1 receptor signalling has been proposed to modulate aquaporin-2 (AQP2) trafficking and water reabsorption. This provides a theoretical basis for NK1 antagonism influencing water homeostasis, although no studies have specifically tested this hypothesis.

Importantly, the mechanistic link for this indication remains unvalidated and was flagged as "pending" in the current Evidence Pack. The high TxGNN score (99.97%) reflects graph-based model inference derived from known molecular interactions rather than direct experimental evidence. Until pharmacological studies confirm NK1R involvement in AVPR2-constitutive signalling pathways, this prediction should be treated as a hypothesis-generating signal requiring preclinical confirmation before any clinical development consideration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Aprepitant is not currently registered on the Australian Register of Therapeutic Goods (ARTG) and has no approved product entries. Healthcare professionals in Australia wishing to access Aprepitant would need to do so via the TGA Special Access Scheme (SAS Category B or C) or through the Authorised Prescriber pathway. Clinicians should consult the approved Product Information from a comparable regulatory jurisdiction (FDA or EMA) for prescribing guidance and safety information.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. As Aprepitant is not registered in Australia, clinicians should consult the FDA or EMA Product Information and apply to the TGA Special Access Scheme if use is being considered. Full safety data including warnings, contraindications, and drug interaction data were not available in the current Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is based solely on TxGNN model inference (Evidence Level L5) with no supporting clinical trials, observational studies, or published literature specifically linking Aprepitant to nephrogenic syndrome of inappropriate antidiuresis. Aprepitant is not registered in Australia, and both the mechanistic rationale and safety profile require substantial further evaluation before this candidate can progress.

**To proceed, the following is needed:**

- **Mechanistic validation:** Conduct targeted preclinical studies to determine whether NK1R/substance P signalling interacts with constitutively active AVPR2 or AQP2 trafficking in renal collecting duct models; confirm whether Aprepitant produces measurable effects on vasopressin-independent water reabsorption in animal models of NSIAD
- **Literature review:** Perform a systematic search (PubMed, EMBASE) combining NK1 antagonist terms with vasopressin, AVPR2, aquaporin-2, and hyponatraemia to characterise any existing mechanistic evidence
- **Safety data completion:** Obtain the FDA/EMA-approved Product Information to address the blocking Data Gap (DG001) — particularly regarding use in paediatric male patients, who are the predominant NSIAD-affected population
- **MOA data completion:** Complete DrugBank API query (DG002) to formally document Aprepitant's mechanism of action and receptor binding profile for the repurposing dossier
- **Regulatory pathway scoping:** If preclinical evidence is supportive, assess whether a TGA Special Access Scheme Category B application or an orphan drug designation pathway is appropriate given the ultra-rare nature of NSIAD (estimated prevalence <1:1,000,000)
- **Other high-priority candidates:** Note that the TxGNN run also flagged **subarachnoid haemorrhage** (Rank 9, score 99.85%) as having the strongest mechanistic rationale among all 10 predicted indications, given SP-mediated neurogenic inflammation and cerebral vasospasm post-SAH, combined with Aprepitant's demonstrated CNS penetration. This candidate may warrant parallel investigation.

---

> **Disclaimer:** This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates identified by TxGNN require clinical validation before therapeutic application. All information should be interpreted in accordance with TGA regulatory requirements and applicable clinical guidelines.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

