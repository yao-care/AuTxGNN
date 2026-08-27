---
layout: default
title: Omeprazole
parent: 僅模型預測 (L5)
nav_order: 491
evidence_level: L5
indication_count: 10
---

# Omeprazole
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

# Omeprazole: From Peptic Ulcer Disease to Duodenogastric Reflux

## One-Sentence Summary

Omeprazole is a proton pump inhibitor (PPI), well established for treating peptic ulcer disease and gastro-oesophageal reflux disease by suppressing gastric acid secretion. The TxGNN model predicts it may also be effective for **duodenogastric reflux**, but this direction is currently supported by only **1 clinical trial** (an imaging-diagnosis study, not a treatment trial) and **20 publications**, several of which raise a conflicting safety signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease / gastro-oesophageal reflux disease (well-established PPI indication; no local market-authorisation text is available in this dataset) |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for this candidate is not available in the Evidence Pack. Based on well-established pharmacological knowledge, omeprazole is a proton pump inhibitor that irreversibly binds the H+/K+-ATPase ("proton pump") on gastric parietal cells, blocking the final step of acid secretion. Its efficacy in peptic ulcer disease and acid-reflux disorders is well proven.

Duodenogastric reflux (DGR) is mechanistically different from classic acid-reflux disease: it is driven primarily by **bile and duodenal content** refluxing into the stomach, rather than by gastric acid itself. Acid suppression with omeprazole could plausibly alter gastric emptying and reflux dynamics, which is the rationale behind the TxGNN prediction linking it to DGR.

However, the supporting evidence is mixed rather than reassuring. Several animal studies (e.g. PMID 10389684, PMID 33027361, PMID 8943968) suggest that acid blockade with omeprazole may *increase* mucosal exposure to bile and even promote gastric carcinogenesis in DGR models — a class effect also reported for other PPIs such as lansoprazole (PMID 15052437). Clinical studies in Barrett's oesophagus patients (PMID 9824338, PMID 10994616) show omeprazole's effect on DGR is inconsistent. This mechanistic uncertainty is the main reason the evidence level remains low (L3) despite the very high TxGNN score.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02685150](https://clinicaltrials.gov/study/NCT02685150) | N/A | Completed | 157 | Evaluated endoscopic Tri-Modal Imaging (NBI/AFI/WLI) to distinguish functional dyspepsia from reflux disease (acid or bile). This is a diagnostic-imaging study, not an omeprazole treatment trial — graded C relevance (indirect). |

No dedicated treatment trial of omeprazole in duodenogastric reflux was identified.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9824338](https://pubmed.ncbi.nlm.nih.gov/9824338/) | 1998 | RCT | Gut | Omeprazole 20 mg twice daily and its effect on duodenogastric and duodenogastro-oesophageal bile reflux in Barrett's oesophagus. |
| [10994616](https://pubmed.ncbi.nlm.nih.gov/10994616/) | 2000 | Cohort | Scand J Gastroenterol | Effect of omeprazole on antral duodenogastric reflux in Barrett oesophagus; suggests DGR may be reduced by omeprazole. |
| [10389684](https://pubmed.ncbi.nlm.nih.gov/10389684/) | 1999 | Animal study | Dig Dis Sci | Gastric acid blockade with omeprazole promotes gastric carcinogenesis induced by duodenogastric reflux in rats — key safety signal. |
| [33027361](https://pubmed.ncbi.nlm.nih.gov/33027361/) | 2020 | Animal study | Acta Cir Bras | Investigated omeprazole and nitrites on gastric mucosa in a rat DGR model, examining a possible protective vs. carcinogenic effect. |
| [8943968](https://pubmed.ncbi.nlm.nih.gov/8943968/) | 1996 | Animal study | Dig Dis Sci | DGR causes growth stimulation of foregut mucosa, potentiated by gastric acid blockade (omeprazole arm included). |
| [15052437](https://pubmed.ncbi.nlm.nih.gov/15052437/) | 2004 | Animal study | Gastric Cancer | Lansoprazole (same PPI class) promotes gastric carcinogenesis in rats with duodenogastric reflux — supports a possible class effect. |
| [16641575](https://pubmed.ncbi.nlm.nih.gov/16641575/) | 2006 | Prospective study | J Pediatr Gastroenterol Nutr | Prospective study of PPI (omeprazole) therapy for oesophageal bile reflux in children. |
| [11552908](https://pubmed.ncbi.nlm.nih.gov/11552908/) | 2001 | Clinical study | Aliment Pharmacol Ther | Influence of pantoprazole (same PPI class) on oesophageal motility and bile/acid reflux in oesophagitis patients. |
| [12836018](https://pubmed.ncbi.nlm.nih.gov/12836018/) | 2003 | Case series | Eur J Pediatr | Describes primary duodenogastric reflux in six children/adolescents unresponsive to classical antacid therapy. |
| [19491829](https://pubmed.ncbi.nlm.nih.gov/19491829/) | 2009 | Clinical study | Am J Gastroenterol | Compares degree of duodenogastroesophageal and acid reflux between PPI responders and non-responders. |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only clinical trial identified is a diagnostic-imaging study, not a treatment trial, and the literature base is dominated by preclinical/animal work — some of which raises a specific concern that acid suppression with omeprazole may worsen mucosal exposure to bile or promote gastric carcinogenesis in duodenogastric reflux models. Combined with the fact that DGR is primarily a bile-driven (not acid-driven) condition, the mechanistic rationale is uncertain and the evidence level (L3) does not support proceeding at this time.

**To proceed, the following is needed:**
- A dedicated mechanism-of-action (MOA) profile for omeprazole to properly assess mechanistic relevance to DGR
- TFDA/PI-sourced safety data (key warnings, contraindications, drug interactions) — currently a blocking data gap
- Resolution of the conflicting preclinical carcinogenesis signal (PMID 10389684, PMID 33027361, PMID 15052437) before any clinical development is considered
- A prospective clinical trial evaluating omeprazole specifically as a treatment for duodenogastric reflux, rather than for acid-reflux or Barrett's oesophagus as a secondary endpoint
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

