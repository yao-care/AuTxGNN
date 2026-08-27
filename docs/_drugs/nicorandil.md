---
layout: default
title: Nicorandil
parent: 僅模型預測 (L5)
nav_order: 466
evidence_level: L5
indication_count: 10
---

# Nicorandil
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

# Nicorandil: From Angina Pectoris to Benign Prostatic Hyperplasia

## One-Sentence Summary

Nicorandil is a potassium-channel opener with nitrate (NO-donor) activity, classically used for angina pectoris (this background is general pharmacological knowledge — the evidence pack's structured original-indication and MOA fields are flagged as data gaps, see below).
The TxGNN model predicts it may be effective for **Benign Prostatic Hyperplasia (BPH)**,
with **0 registered clinical trials** and **3 supporting publications** currently available — evidence is mechanistic/preclinical only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Angina pectoris (general pharmacological knowledge; not captured as structured data in this evidence pack) |
| Predicted New Indication | Benign Prostatic Hyperplasia |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Nicorandil is not available in the evidence pack (Data Gap DG002). Based on known pharmacological information, Nicorandil is a K_ATP channel opener combined with a nitrate-class NO donor, producing both systemic and local vasodilation — this mechanism is corroborated by the drug's own repurposing rationale text extracted from the literature review.

BPH pathogenesis is increasingly linked to the "prostatic ischemia/vascular dysfunction hypothesis": chronic reduction in prostatic blood flow is thought to promote stromal hyperplasia and worsen lower urinary tract symptoms (LUTS). Because Nicorandil's vasodilatory action could theoretically restore prostatic perfusion, there is a specific, drug-named mechanistic pathway proposed in the literature — not merely a generic "vasodilators might help" inference.

This makes the prediction mechanistically plausible, but it is important to note the supporting evidence is limited to one animal model study and two narrative reviews — there is no human clinical data confirming efficacy for BPH.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31735753](https://pubmed.ncbi.nlm.nih.gov/31735753/) | 2019 | Review | Nihon Yakurigaku Zasshi (Folia Pharmacologica Japonica) | Reviews evidence that impaired prostatic blood flow contributes to BPH/BPE pathogenesis, positioning prostatic blood flow as a therapeutic target |
| [26165338](https://pubmed.ncbi.nlm.nih.gov/26165338/) | 2015 | Review | Nihon Yakurigaku Zasshi (Folia Pharmacologica Japonica) | Proposes LUTS as a vascular dysfunction and discusses Nicorandil's vasodilator effect as a potential therapeutic approach (no abstract available in source) |
| [24448152](https://pubmed.ncbi.nlm.nih.gov/24448152/) | 2014 | Animal cohort study (SHR rat model) | Scientific Reports | Six weeks of Nicorandil treatment in spontaneously hypertensive rats improved prostatic blood flow and reduced oxidative stress markers, supporting the prostatic-ischemia mechanism of BPH |

---

## Australia Market Information

Nicorandil currently has no ARTG (Australian Register of Therapeutic Goods) entries — it is not marketed in Australia.

---

## Safety Considerations

No structured safety data (warnings, contraindications, or drug interactions) is available in this evidence pack (Data Gap DG001, Blocking). As Nicorandil is not TGA-registered, there is no local Product Information to reference — safety assessment would need to draw on overseas regulatory PI (e.g. EMA, MHRA) before any clinical use is considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The BPH prediction rests on a specific and biologically coherent mechanistic hypothesis, but is supported only by one animal-model study and two reviews (Evidence Level L4) — there are no registered clinical trials, and Nicorandil itself is not marketed in Australia. A blocking safety data gap (TFDA/TGA warnings and contraindications) also prevents any preliminary safety assessment.

**To proceed, the following is needed:**
- Resolve DG001: obtain TGA/overseas Product Information for warnings, contraindications, and DDI data
- Resolve DG002: confirm mechanism of action from a structured source (e.g. DrugBank record)
- Human proof-of-concept data for BPH/LUTS (even observational or small pilot studies) before considering Phase 2 investment
- Regulatory pathway assessment, since Nicorandil would need first-time TGA registration or Special Access Scheme approval to be used in Australia at all
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

