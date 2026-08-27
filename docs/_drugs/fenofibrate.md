---
layout: default
title: Fenofibrate
parent: 僅模型預測 (L5)
nav_order: 269
evidence_level: L5
indication_count: 10
---

# Fenofibrate
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

# Fenofibrate: From Dyslipidaemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Fenofibrate is a fibrate-class lipid-regulating agent conventionally used for dyslipidaemia and hypertriglyceridaemia.
The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**,
but this direction is currently supported by only **1 clinical trial** (not involving fenofibrate itself) and **11 publications**, most of which are historical case-level data.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in this data source (no TGA/ARTG licence records available). Fenofibrate is generically known as a fibrate-class agent for dyslipidaemia/mixed hyperlipidaemia. |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, fenofibrate is a peroxisome proliferator-activated receptor alpha (PPARα) agonist belonging to the fibrate class, which lowers triglycerides and modestly raises HDL cholesterol, and has historically been used in dyslipidaemia and mixed hyperlipidaemia.

HoFH, however, results from near-complete loss of LDL-receptor function and typically requires aggressive LDL-lowering strategies — high-intensity statins, PCSK9 inhibitors, or LDL apheresis. Fenofibrate does not correct the LDL-receptor defect and has no established role as a primary HoFH therapy; the drug-disease link identified by TxGNN appears to be driven mainly by shared lipid-disorder terminology rather than a validated pharmacological mechanism.

The only supporting clinical evidence is limited to small, decades-old case series (e.g. a 1984 cohort in which one HoFH patient showed the largest cholesterol reduction among a broader type II hyperlipoproteinaemia population) — not a dedicated HoFH trial. This is consistent with the low evidence level (L4) and "Hold" recommendation assigned to this candidate.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Evaluated alirocumab (a PCSK9 inhibitor, not fenofibrate) in children/adolescents with HoFH on background therapy; assessed LDL-C reduction at 12–48 weeks. Included here only for disease overlap — no fenofibrate arm. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6593751](https://pubmed.ncbi.nlm.nih.gov/6593751/) | 1984 | Cohort | Pharmacological Research Communications | 22 type II hyperlipoproteinaemia patients on fenofibrate 300 mg/day; one HoFH patient showed the largest total/LDL-cholesterol reduction in the cohort. |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Review | Annals of the New York Academy of Sciences | Reviews pharmacologic/surgical treatment of dyslipidaemic children, noting fenofibrate among agents used in familial hypercholesterolaemia. |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | PK study | Pharmacotherapy | Characterises pharmacokinetic interactions between lomitapide (an approved HoFH adjunct) and lipid-lowering agents including fenofibrate. |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart Journal | Notes fenofibrate's most definite indication is fasting triglyceride >500 mg/dL to reduce pancreatitis risk, not LDL-driven disease like HoFH. |
| [24946816](https://pubmed.ncbi.nlm.nih.gov/24946816/) | 2014 | Review | Internal Medicine Journal | Discusses liver transplantation for HoFH in an era of emerging lipid-lowering therapies (contextual, not fenofibrate-specific). |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocrine Practice | AACE/ACE dyslipidaemia management and cardiovascular prevention guideline (general context). |
| [26432726](https://pubmed.ncbi.nlm.nih.gov/26432726/) | 2015 | Review | Indian Heart Journal | Reviews LDL-C reduction strategies including statins and PCSK9 inhibitors for severe hypercholesterolaemia. |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | Review | Drugs | Pharmacology and therapeutic potential of atorvastatin in hyperlipidaemia (comparator class, not fenofibrate). |
| [9627539](https://pubmed.ncbi.nlm.nih.gov/9627539/) | 1998 | Review | The Canadian Journal of Cardiology | Advances in dyslipidaemia drug treatment focused on atorvastatin. |
| [35499807](https://pubmed.ncbi.nlm.nih.gov/35499807/) | 2022 | Review | Current Atherosclerosis Reports | Reviews dyslipidaemia management in pregnancy (general context, not HoFH-specific). |

## Australia Market Information

No ARTG entries were found for Fenofibrate in this data source (0 of 0 licences on record).

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Fenofibrate has no established mechanistic link to the LDL-receptor defect underlying HoFH, and the supporting evidence is a single unrelated (non-fenofibrate) trial plus mostly indirect, decades-old literature — evidence level L4 is insufficient to advance this candidate.

**To proceed, the following is needed:**
- Fenofibrate mechanism of action (MOA) data from DrugBank (currently marked as a data gap, high impact on mechanistic assessment)
- TGA-approved Product Information — warnings, contraindications and drug interactions (currently marked as a blocking data gap for safety screening)
- Confirmation of Australian market/ARTG status, since 0 licences is unusual for a long-marketed generic and should be verified against the TGA database directly
- A dedicated fenofibrate-in-HoFH trial or registry data, rather than reliance on historical case-level cohorts

**Note:** Among the other TxGNN-predicted indications in this evidence pack, **hyperlipoproteinemia** (rank 2, score 99.65%) has substantially stronger evidence — 34 clinical trials (several graded A, directly testing fenofibrate) and evidence level L1 — with a "Proceed with Guardrails" recommendation. This may be a more promising candidate for near-term evaluation than HoFH.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

