---
layout: default
title: Glimepiride
parent: 僅模型預測 (L5)
nav_order: 314
evidence_level: L5
indication_count: 10
---

# Glimepiride
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

# Glimepiride: From Type 2 Diabetes Mellitus to Type 1 Diabetes Mellitus

## One-Sentence Summary

Glimepiride is a third-generation sulfonylurea established for Type 2 Diabetes Mellitus, acting as a SUR1/KATP channel closer to stimulate residual β-cell insulin secretion. TxGNN's raw output ranks several unrelated conditions (e.g. stiff person syndrome, various lipodystrophies) as top candidates, but the evidence pack's own mechanistic review flags these as likely knowledge-graph artefacts with **zero supporting trials or literature**. The only prediction with substantive evidence is **Type 1 Diabetes Mellitus**, supported by **1 RCT, 2 preclinical animal studies, and 2 monogenic-diabetes case reports** among 17 retrieved publications — this report focuses on that candidate.

> **Note on selection**: TxGNN's #1–#9 ranked predictions (stiff person syndrome, opsismodysplasia, various lipodystrophies, pancreatic agenesis) all carry Evidence Level **L5** with **zero** clinical trials or literature, and the evidence pack's own rationale explicitly labels them as graph-embedding spurious correlations ("偽相關") with no biological plausibility. Presenting one of these as the headline finding would be misleading, so this report instead evaluates rank #10, Type 1 Diabetes Mellitus, the only candidate with real supporting evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (established sulfonylurea use; not captured in this evidence pack's regulatory license data, which is empty) |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 98.86% |
| Evidence Level | L2 |
| Australia Market Status | Not Marketed (per this evidence pack) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the drug-level fields in this evidence pack (`original_moa` is a data gap). Based on information referenced throughout the evidence pack itself, glimepiride is a third-generation sulfonylurea that closes the SUR1 subunit of the pancreatic β-cell KATP channel, triggering insulin release — a mechanism that only works if functional β-cells remain.

Classic autoimmune Type 1 Diabetes Mellitus involves near-total β-cell destruction, so a pure insulin secretagogue would seem mechanistically limited. However, the retrieved evidence points to a narrower and more defensible rationale: two case reports (PMID 21992555, PMID 38513803) describe glimepiride successfully treating diabetes caused by activating **ABCC8/SUR1** mutations (i.e. monogenic diabetes, including a MODY12 case initially labelled Type 1), which is a direct, mechanistically coherent match to glimepiride's known target. Separately, two preclinical BB-rat studies (PMID 7475982, PMID 8539908) and one small placebo-controlled RCT in adolescents with Type 1 Diabetes (PMID 12663616) suggest a possible immunomodulatory or β-cell-preserving effect beyond simple insulin secretion, particularly in newly diagnosed patients with residual C-peptide.

Taken together, the plausible niche is **not** broad first-line Type 1 Diabetes therapy, but rather (a) SUR1/ABCC8-mediated monogenic diabetes misclassified as Type 1, and (b) adjunctive use in patients with residual β-cell function. Outside these subgroups, glimepiride carries real risk (hypoglycaemia, and no evidence of efficacy in β-cell-absent patients).

## Clinical Trial Evidence

No clinical trials with a confirmed classic Type 1 Diabetes Mellitus population were identified. The automated search returned 50 trials tagged to this indication, but review of their titles and summaries shows nearly all enrol Type 2 Diabetes populations, with glimepiride used only as an active comparator — this reflects a likely search/database keyword mismatch rather than genuine Type 1 Diabetes trial evidence. One Phase 2 RCT (NCT00309608, n=333) was auto-flagged as possibly relevant, but its brief summary explicitly describes a Type 2 Diabetes, metformin add-on population, so it is excluded here as unreliable evidence for this indication.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12663616](https://pubmed.ncbi.nlm.nih.gov/12663616/) | 2003 | RCT | Diabetes Care | Prospective, randomised, double-blind, placebo-controlled trial of glimepiride in adolescents with Type 1 Diabetes, assessing IGF-I effects — the only trial directly dosing glimepiride in a classic T1DM population |
| [21992555](https://pubmed.ncbi.nlm.nih.gov/21992555/) | 2012 | Case report | Diabetic Medicine | Diabetes caused by an activating ABCC8/SUR1 mutation effectively treated with glimepiride |
| [38513803](https://pubmed.ncbi.nlm.nih.gov/38513803/) | 2024 | Case report | Clinical Medicine (London) | ABCC8 mutation causing MODY12, initially diagnosed as Type 1 Diabetes; good glycaemic control achieved with glimepiride |
| [7475982](https://pubmed.ncbi.nlm.nih.gov/7475982/) | 1995 | Preclinical (animal) | Life Sciences | Glimepiride prevented onset of diabetes and autoimmune events in BB rats (T1DM model) |
| [8539908](https://pubmed.ncbi.nlm.nih.gov/8539908/) | 1995 | Preclinical (animal) | Transplantation Proceedings | Glimepiride combined with islet allotransplantation prevented/cured T1D in BB rats |
| [32935446](https://pubmed.ncbi.nlm.nih.gov/32935446/) | 2021 | Review/Case report | Journal of Diabetes | Spectrum of glucose dysmetabolism from KCNJ11 (KATP channel) mutations, mechanistically linking channel-mediated diabetes to SU responsiveness |
| [11460577](https://pubmed.ncbi.nlm.nih.gov/11460577/) | 2001 | Review | Exp Clin Endocrinol Diabetes | Reviews oral hypoglycaemic agents; notes glimepiride's relative KATP-channel selectivity and lower hypoglycaemia risk versus older sulfonylureas |
| [15955587](https://pubmed.ncbi.nlm.nih.gov/15955587/) | 2005 | Case report | Diabetes Res Clin Pract | Type 1 Diabetes developing in a Type 2 patient with severe insulin resistance, managed with insulin plus glimepiride |
| [32268860](https://pubmed.ncbi.nlm.nih.gov/32268860/) | 2020 | Review | Current Pharmaceutical Design | Safety/efficacy comparison of sulfonylureas vs DPP-4 inhibitors as second-line therapy — background pharmacology, Type 2 Diabetes focus |
| [15013454](https://pubmed.ncbi.nlm.nih.gov/15013454/) | 2004 | Review/Commentary | The American Journal of Medicine | General discussion of basal insulin initiation alongside sulfonylurea/metformin therapy — background context only |

## Australia Market Information

No ARTG entries are recorded in this evidence pack, and market status is listed as Not Marketed. This may reflect a data-collection gap rather than confirmed absence from the Australian market — glimepiride-containing products are widely available generically in other jurisdictions. Current ARTG status should be verified directly against the TGA database before this field is relied upon.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. This evidence pack carries a **Blocking** data gap (DG001) for TGA/TFDA label warnings and contraindications, and drug interaction data was not found — obtaining the official Product Information is a prerequisite before any safety assessment can proceed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A Blocking data gap (missing PI warnings/contraindications, DG001) means safety pre-assessment cannot be completed, and ARTG status is currently unverified (0 entries on record).
- The supporting evidence for Type 1 Diabetes Mellitus, while real, is limited to one small paediatric RCT, two preclinical animal studies, and case reports of a narrow monogenic-diabetes subgroup — not classic autoimmune Type 1 Diabetes broadly.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications, drug interactions)
- Formal mechanism of action data via DrugBank API
- Clarification of target subpopulation — SUR1/ABCC8-mediated monogenic diabetes vs. residual-β-cell autoimmune Type 1 Diabetes — since these have very different risk/benefit profiles
- Direct TGA/ARTG database confirmation of current Australian market status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

