---
layout: default
title: Metoclopramide
parent: 僅模型預測 (L5)
nav_order: 439
evidence_level: L5
indication_count: 10
---

# Metoclopramide
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

# Metoclopramide: From Antiemetic/Prokinetic Use to Gastric Ulcer

## One-Sentence Summary

> Metoclopramide is a dopamine D2-receptor antagonist used clinically as an antiemetic and gastrointestinal prokinetic (nausea, vomiting, delayed gastric emptying) — this description is drawn from supporting literature in this evidence pack, as the drug's registered original indication and mechanism-of-action fields are not populated in the source data.
> The TxGNN model predicts it may be effective for **Gastric Ulcer**, with **2 clinical trials** and **20 publications** currently associated with this direction — however, the supporting evidence is mechanistically weak and largely preclinical.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in registry data; literature in this pack describes metoclopramide as an antiemetic / GI prokinetic (nausea, vomiting, delayed gastric emptying) |
| Predicted New Indication | Gastric Ulcer |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for metoclopramide is not available from DrugBank in this evidence pack (data gap DG002, severity: High). Based on literature included in this pack, metoclopramide is a dopamine D2-receptor antagonist that increases gastric emptying and lower oesophageal sphincter tone, and is used clinically as a prokinetic agent and antiemetic (including for chemotherapy-induced nausea and vomiting).

Gastric ulcer healing is driven by acid suppression, mucosal protection, and (where relevant) *H. pylori* eradication or removal of an offending agent such as an NSAID — none of which are mechanisms metoclopramide possesses. The evidence pack's own mechanistic assessment states this directly: metoclopramide has "no acid-suppressive or mucosal-protective mechanism" and is "not directly related to the pathophysiology of ulcer healing."

Some preclinical (animal) studies show a modest ulcer-protective effect, plausibly attributable to improved gastric emptying and reduced pyloric reflux rather than a direct antiulcer action, but this has not been translated into a demonstrated clinical treatment effect. The prediction should therefore be read as a plausible mechanistic hypothesis worth monitoring, not as evidence of clinical efficacy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05746377](https://clinicaltrials.gov/study/NCT05746377) | Phase 4 | Unknown | 60 | Tests whether metoclopramide premedication before endoscopy for upper GI bleeds reduces the need for repeat endoscopy/IR/surgery and improves endoscopic visibility — a periprocedural aid, not a gastric ulcer treatment trial (relevance grade B). |
| [NCT03747107](https://clinicaltrials.gov/study/NCT03747107) | N/A | Completed | 19 | Primary-care prescribing safety quality-improvement study (P-DQIP); metoclopramide appears only as one of several monitored drug therapy risks, not as a gastric ulcer intervention (relevance grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16807979](https://pubmed.ncbi.nlm.nih.gov/16807979/) | 2006 | RCT | Yonsei Med J | Double-blind RCT of IV metoclopramide vs ranitidine on preoperative gastric contents before day-case laparoscopic surgery — not a treatment-of-ulcer study. |
| [19225](https://pubmed.ncbi.nlm.nih.gov/19225/) | 1977 | Review | Drugs | Review of drug treatment options for gastric and duodenal ulcer. |
| [6336644](https://pubmed.ncbi.nlm.nih.gov/6336644/) | 1983 | Review | Ann Intern Med | General pharmacology and clinical applications of metoclopramide (antiemetic, GI prokinetic); no ulcer-specific data. |
| [775822](https://pubmed.ncbi.nlm.nih.gov/775822/) | 1976 | Unclassified | ZFA | "Therapy of gastric and duodenal ulcer with Metoclopramide" — title directly on-topic; abstract not available in this pack. |
| [2730234](https://pubmed.ncbi.nlm.nih.gov/2730234/) | 1989 | Animal | Arch Int Pharmacodyn Ther | Rat study: metoclopramide showed an ulcer-protective effect in aspirin-induced and pylorus-ligated gastric ulcer models, without affecting acid secretion. |
| [6436177](https://pubmed.ncbi.nlm.nih.gov/6436177/) | 1984 | Animal | Indian J Physiol Pharmacol | Guinea-pig study: metoclopramide protected against experimentally induced gastric ulceration via improved gastric drainage, not acid suppression. |
| [4779253](https://pubmed.ncbi.nlm.nih.gov/4779253/) | 1973 | Unclassified | Curr Med Res Opin | "Bile reflux in gastric ulcer: the effect of smoking, metoclopramide and carbenoxolone sodium" — title on-topic; abstract not available. |
| [6106882](https://pubmed.ncbi.nlm.nih.gov/6106882/) | 1980 | Unclassified | Medizinische Klinik | "[Conservative treatment of gastric ulcer]" — title on-topic; abstract not available. |
| [8095331](https://pubmed.ncbi.nlm.nih.gov/8095331/) | 1993 | Unclassified | Postgrad Med | Review of therapeutic strategies for peptic lesions refractory to standard H2-antagonist/sucralfate regimens; metoclopramide not central. |
| [797497](https://pubmed.ncbi.nlm.nih.gov/797497/) | 1976 | Unclassified | Clin Pharmacokinet | General discussion of drugs and diseases (including gastric ulcer) that alter gastric emptying. |

---

## Australia Market Information

Metoclopramide has **0 ARTG entries** in this evidence pack — it is not currently marketed in Australia, so no product-level ARTG table is available.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic case is weak — metoclopramide has no acid-suppressive or mucosal-protective action relevant to ulcer healing — and clinical trial support is indirect (periprocedural endoscopy use, not ulcer treatment). Evidence level is L4 (preclinical/mechanistic), insufficient to progress past initial screening (decision stage S1).

**To proceed, the following is needed:**
- TFDA/TGA product-label warnings and contraindications (data gap DG001, Blocking — currently prevents any S1 safety assessment)
- Confirmed mechanism of action from DrugBank (data gap DG002, High)
- A registered original indication/regulatory history for metoclopramide, since none is populated in the current evidence pack
- A dedicated, ulcer-specific clinical trial (rather than periprocedural or unrelated studies) before reconsidering this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

