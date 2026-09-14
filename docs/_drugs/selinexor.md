---
layout: default
title: Selinexor
parent: 僅模型預測 (L5)
nav_order: 622
evidence_level: L5
indication_count: 10
---

# Selinexor
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

# Selinexor: From an Undocumented Original Indication to Progesterone-Receptor Negative Breast Cancer

*Note on scope: this Evidence Pack (`TW-DB11942-multi`) contains 10 TxGNN-predicted candidate indications for Selinexor. The highest raw TxGNN score (drug-induced osteoporosis, 99.22%) has zero supporting trials or literature, and its own rationale text flags it as likely graph-connectivity noise. This report therefore focuses on the candidate with the strongest actual evidence — progesterone-receptor negative breast cancer, which overlaps with triple-negative breast cancer (TNBC) — and summarises the other nine candidates in an appendix table for transparency.*

## One-Sentence Summary

Selinexor's original approved indication is not captured in this evidence pack — the DrugBank query returned no listed original indications, and Selinexor is currently **Not Marketed** in Australia (0 ARTG entries). Of the ten TxGNN-predicted new indications reviewed, **progesterone-receptor negative breast cancer** has the most substantive support, backed by **1 completed Phase 2 clinical trial** (n=10, uncontrolled) and a plausible XPO1/CRM1 mechanistic rationale — though the evidence remains hypothesis-generating rather than confirmatory.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (no original indications on file; MOA flagged as Data Gap DG002) |
| Predicted New Indication | Progesterone-Receptor Negative Breast Cancer (overlaps with Triple-Negative Breast Cancer) |
| TxGNN Prediction Score | 97.20% |
| Evidence Level | L2 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Selinexor's original indication is not available in this evidence pack. Based on the mechanistic information that is available, Selinexor is a Selective Inhibitor of Nuclear Export (SINE) that blocks XPO1 (CRM1)-mediated nuclear export of tumour-suppressor proteins such as p53, FOXO3a and IκB. Trapping these proteins in the nucleus is proposed to trigger apoptosis in malignant cells.

XPO1 overexpression has been reported across multiple solid tumour types, including breast cancer, which provides a plausible mechanistic basis for evaluating Selinexor in hormone-receptor-negative, more proliferative breast cancer subtypes. This is reinforced by the fact that five of the ten TxGNN-predicted indications in this pack are breast cancer subtypes (HER2-positive, PR-negative, PR-positive, normal-like, luminal A/B), suggesting the model has picked up a genuine breast-cancer-related signal rather than an isolated artefact.

However, the only indication-specific evidence directly testing this hypothesis is a single small, uncontrolled Phase 2 trial in metastatic triple-negative breast cancer (10 patients). This supports the biological plausibility of the prediction but is far from sufficient to establish clinical efficacy in progesterone-receptor negative breast cancer specifically.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02402764](https://clinicaltrials.gov/study/NCT02402764) | Phase 2 | Completed | 10 | Investigator-initiated, single-arm study of Selinexor (KPT-330) in metastatic triple-negative breast cancer, assessing safety, tolerability and preliminary efficacy. No comparator arm; small sample size limits conclusions to hypothesis generation. |

No ANZCTR-registered trials were identified for this indication in the evidence pack.

## Literature Evidence

No directly related literature is currently indexed for progesterone-receptor negative breast cancer in this evidence pack.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — Selective Inhibitor of Nuclear Export (SINE), XPO1/CRM1 antagonist (not a conventional cytotoxic chemotherapy agent) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the Product Information (PI) warnings and precautions |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

## Other Screened Indications (Same Evidence Pack)

For transparency, the remaining nine candidates evaluated for Selinexor in this pack are listed below. None currently meet the threshold for a "Research Question" recommendation.

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-------------|-----------------|-----------------|
| 1 | Drug-induced osteoporosis | 99.22% | L5 | Hold — no supporting trials/literature; likely model noise |
| 2 | HER2 positive breast carcinoma | 98.13% | L4 | Hold — only indirect literature, no direct trial evidence |
| 4 | Normal breast-like subtype of breast carcinoma | 97.18% | L5 | Hold — no trials or literature |
| 5 | Progesterone-receptor positive breast cancer | 97.18% | L5 | Hold — no trials or literature |
| 6 | Breast tumor luminal A or B | 97.11% | L5 | Hold — literature returned is an unrelated keyword-matching artefact ("B cell" topics), flagged as a data quality issue |
| 7 | Squamous cell lung carcinoma | 96.91% | L3 | Hold — two relevant trials, both terminated/withdrawn without usable data |
| 8 | Gestational trophoblastic neoplasm | 96.54% | L5 | Hold — no trials or literature; pregnancy-related safety concerns unaddressed |
| 9 | Cervical neuroblastoma | 96.33% | L4 | Hold — no direct evidence; only literature is an unrelated drug-synthesis review |
| 10 | Schwannoma of jugular foramen | 96.32% | L5 | Hold — no trials or literature; typically benign tumour, unclear risk-benefit rationale |

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The single completed trial supporting progesterone-receptor negative breast cancer is a small (n=10), uncontrolled, investigator-initiated Phase 2 study — sufficient to generate a research hypothesis but not to justify clinical use or a "Proceed with Guardrails" pathway. Core drug-level data (mechanism of action, TGA/PI warnings and contraindications) are also missing from this evidence pack, and Selinexor is not currently marketed in Australia.

**To proceed, the following is needed:**
- TGA/PI-sourced warnings and contraindications (currently a Blocking data gap, DG001)
- Confirmed mechanism-of-action documentation from DrugBank (currently a High-severity data gap, DG002)
- A larger, controlled trial specifically in progesterone-receptor negative / triple-negative breast cancer
- Documentation of Selinexor's currently approved (original) indication and existing safety profile, for baseline comparison
- Assessment of the TGA/ARTG registration pathway given the current "Not Marketed" status

---
*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

