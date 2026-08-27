---
layout: default
title: Lansoprazole
parent: 僅模型預測 (L5)
nav_order: 383
evidence_level: L5
indication_count: 10
---

# Lansoprazole
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

Using the evidence pack as provided, here is the evaluation report.

# Lansoprazole: From Acid-Related Disorders to Duodenogastric Reflux

## One-Sentence Summary

Lansoprazole is a proton pump inhibitor (PPI) traditionally used for acid-related gastrointestinal conditions such as peptic ulcer disease and gastro-oesophageal reflux. The TxGNN model's highest-ranked prediction for this drug is **Duodenogastric Reflux**, but this direction is currently supported by only **0 clinical trials** and **2 publications** — one of which is a preclinical signal suggesting possible harm rather than benefit. On the strength of the available evidence, this candidate should be placed on **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in the structured data for this candidate (no ARTG license text or original-indication field populated) |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed (not currently registered) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured drug record (original MOA = Data Gap). Based on the literature captured in this evidence pack, lansoprazole is a benzimidazole-derived proton pump inhibitor that irreversibly blocks the gastric H⁺/K⁺-ATPase in parietal cells, reducing gastric acid secretion regardless of the triggering stimulus. This mechanism underlies its established use in acid-related conditions.

However, duodenogastric reflux is primarily driven by retrograde flow of alkaline duodenal contents (bile acids, pancreatic enzymes) into the stomach — a bile-mediated process, not an acid-hypersecretory one. Reducing gastric acid with a PPI does not address this underlying pathophysiology, and there is no mechanistic reason to expect lansoprazole to resolve the reflux itself.

More concerning, the single preclinical study identified for this candidate (PMID 15052437) found that lansoprazole *promoted* gastric carcinogenesis in a rat model of duodenogastric reflux — i.e., acid suppression combined with reflux may have accelerated malignant change rather than provided benefit. This is a potential negative signal, not supportive evidence, and it is the main reason this candidate does not currently meet the bar for progression.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15052437](https://pubmed.ncbi.nlm.nih.gov/15052437/) | 2004 | Animal study (negative signal) | Gastric Cancer | In rats, combined duodenogastric reflux and acid inhibition with lansoprazole was associated with promotion of gastric carcinogenesis — a cautionary preclinical finding, not a supportive one. |
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review (general PPI pharmacology) | European Journal of Clinical Pharmacology | General review of PPI clinical use and pharmacokinetics across peptic ulcer, *H. pylori* infection, GORD, NSAID-induced GI lesions, and Zollinger-Ellison syndrome; does not address duodenogastric reflux specifically. |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

*(Note: key warnings, contraindications, and drug–drug interaction data were not available in this evidence pack — this is logged as a Blocking data gap, see Next Steps.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (duodenogastric reflux) is not mechanistically well-matched to lansoprazole's acid-suppressive action, and the only direct preclinical evidence available raises a potential safety signal (promotion of gastric carcinogenesis in the reflux setting) rather than supporting efficacy. With no clinical trials and only one general review in the literature base, the evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- TFDA/TGA-approved product label (warnings, contraindications) — currently a **Blocking** data gap preventing any S1 safety assessment
- Confirmed mechanism of action data for this candidate record
- Any dedicated clinical or mechanistic studies evaluating PPI therapy specifically in duodenogastric (bile) reflux, ideally clarifying whether the rat carcinogenesis signal has human relevance
- Given the negative/weak evidence for this top-ranked prediction, consideration should be given to reviewing other candidates in the same evidence pack with comparatively stronger evidence levels (e.g., peptic ulcer perforation, duodenitis, and gastroduodenitis — all rated L3, "Research Question" stage) as potentially more promising repurposing directions for this drug.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

