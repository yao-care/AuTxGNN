---
layout: default
title: Progesterone
parent: 僅模型預測 (L5)
nav_order: 563
evidence_level: L5
indication_count: 10
---

# Progesterone
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

# Progesterone: From Reproductive Hormone Therapy to Amenorrhea

## One-Sentence Summary

Progesterone (DrugBank DB00396) is an endogenous steroid hormone used broadly in reproductive endocrinology (e.g. luteal-phase support, endometrial protection); this evidence pack does not record a specific TGA-approved indication for it.
The TxGNN model predicts it may be effective for **Amenorrhea**, with **50 clinical trials** and **18 publications** identified in the search, though only a subset directly test progesterone as the therapeutic intervention.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established in this evidence pack — no ARTG-registered product or original indication was recorded (data gap) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.9996% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available — the DrugBank query for progesterone returned no populated MOA field (data gap DG002, High severity). Based on general pharmacological knowledge, progesterone is the endogenous steroid hormone that drives secretory transformation of the endometrium during the luteal phase; its withdrawal at the end of the cycle (or at the end of an exogenous course) triggers menstrual bleeding.

This is directly relevant to amenorrhea: the **progesterone (or "progestin") challenge test** — administering progesterone and observing whether withdrawal bleeding occurs — is a long-established clinical tool for differentiating hypoestrogenic (anovulatory/hypothalamic) causes of secondary amenorrhea from outflow-tract or other pathology, and is also used therapeutically to induce withdrawal bleeding. Several identified trials and reviews (e.g. progesterone-induced withdrawal bleeding before ovulation induction, medroxyprogesterone acetate for post-ablation amenorrhea rates, progesterone capsules for menstrual disorders) reflect this established clinical use pattern.

Because the mechanistic link is direct and clinically well-precedented, the evidence pack assigns Evidence Level **L2** (based on at least one completed Phase 2/3 RCT context) and a decision stage of S2, supporting a "Proceed with Guardrails" recommendation — with the guardrails driven mainly by the missing TGA safety/labelling data described below, not by mechanistic uncertainty.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01185782](https://clinicaltrials.gov/study/NCT01185782) | Phase 3 | Completed | 300 | Comparative study of a gonadotropin regimen (SJ-0021) vs. purified pituitary gonadotropin in women with Amenorrhea I or anovulatory cycles; confirms clinical trial infrastructure exists for amenorrhoea populations |
| [NCT01942668](https://clinicaltrials.gov/study/NCT01942668) | Phase 3 | Completed | 1845 | RCT of combined estradiol + progesterone vs. placebo for vasomotor symptoms in postmenopausal women with an intact uterus; progesterone used for endometrial protection alongside estrogen |
| [NCT03309709](https://clinicaltrials.gov/study/NCT03309709) | Phase 3 | Unknown | 90 | Multicentre RCT of subcutaneous progesterone (luteal days 18–25) vs. watch-and-wait for regression of endometrial polyps in premenopausal women |
| [NCT02449161](https://clinicaltrials.gov/study/NCT02449161) | Phase 3 | Terminated | 60 | RCT of post-ablation medroxyprogesterone acetate and its effect on endometrial amenorrhoea rates after ablation for heavy menstrual bleeding |
| [NCT03309176](https://clinicaltrials.gov/study/NCT03309176) | Phase 4 | Completed | 42 | RCT testing whether progesterone-induced endometrial withdrawal bleeding is necessary before ovulation induction with clomiphene citrate in women with oligo-/amenorrhoea |
| [NCT05312190](https://clinicaltrials.gov/study/NCT05312190) | N/A | Unknown | 330 | Multicentre RCT comparing a Chinese herbal formula, Progesterone Capsules, and their combination for menstrual disorders in adult women |
| [NCT06533865](https://clinicaltrials.gov/study/NCT06533865) | Phase 3 | Recruiting | 114 | RCT of romosozumab as an adjunct to estrogen (with cyclic progesterone) replacement for bone density in functional hypothalamic amenorrhea |
| [NCT00946192](https://clinicaltrials.gov/study/NCT00946192) | Phase 3 | Completed | 121 | Study of hormonal/body-composition changes distinguishing athletes with exercise-associated amenorrhoea from those with continued cycles, and estrogen's effect on bone |
| [NCT01300676](https://clinicaltrials.gov/study/NCT01300676) | Phase 2/3 | Completed | 79 | Safety profile study of hormone replacement therapy (with Tualang honey comparator) in postmenopausal women |
| [NCT00088153](https://clinicaltrials.gov/study/NCT00088153) | Phase 2/3 | Completed | 110 | Effects of estrogen administration on bone mass/hormone levels in adolescents with anorexia-nervosa-associated amenorrhoea |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38652231](https://pubmed.ncbi.nlm.nih.gov/38652231/) | 2024 | Review | Reviews in Endocrine & Metabolic Disorders | Diagnostic and therapeutic uses of oral micronized progesterone in endocrinology, including its role via hypothalamic kisspeptin/neurokinin B/dynorphin neurons |
| [35525789](https://pubmed.ncbi.nlm.nih.gov/35525789/) | 2022 | Review | Current Problems in Pediatric and Adolescent Health Care | Etiology and management of amenorrhoea in adolescent/young adult women, centred on hypothalamic-pituitary-ovarian axis dysfunction (estrogen/progesterone) |
| [33716979](https://pubmed.ncbi.nlm.nih.gov/33716979/) | 2021 | Review | Frontiers in Endocrinology | Etiology, symptomatology and treatment options in premature ovarian insufficiency, a common cause of secondary amenorrhoea |
| [35463307](https://pubmed.ncbi.nlm.nih.gov/35463307/) | 2022 | Meta-analysis | Frontiers in Oncology | Updated meta-analysis on chemotherapy-induced amenorrhoea and its prognostic significance in premenopausal breast cancer |
| [8629565](https://pubmed.ncbi.nlm.nih.gov/8629565/) | 1996 | Review | American Family Physician | Practical evaluation algorithm for amenorrhoea, including the progesterone challenge test to assess estrogen status |
| [28257537](https://pubmed.ncbi.nlm.nih.gov/28257537/) | 2017 | Review | Southern Medical Journal | Current concepts in primary ovarian insufficiency, noting secondary amenorrhoea and need for hormone replacement therapy |
| [945033](https://pubmed.ncbi.nlm.nih.gov/945033/) | 1976 | Clinical study | Annals of Internal Medicine | Original study of 15 patients with galactorrhoea-amenorrhoea syndromes, documenting disrupted LH/progesterone luteal patterns |
| [22283375](https://pubmed.ncbi.nlm.nih.gov/22283375/) | 2012 | Review | Gynecological Endocrinology | Neuroendocrine control of ovulation; failure of the GnRH–gonadotrophin–ovarian steroid axis resulting in anovulation/amenorrhoea |
| [18756412](https://pubmed.ncbi.nlm.nih.gov/18756412/) | 2008 | Review | Seminars in Reproductive Medicine | Review of intrauterine adhesions (Asherman's syndrome), which present across a spectrum from amenorrhoea to menstrual disturbance |
| [32233689](https://pubmed.ncbi.nlm.nih.gov/32233689/) | 2020 | Review | Climacteric | Clinical management of postmenopausal vaginal bleeding, discussing the estrogen/progesterone-driven endometrial atrophy underlying amenorrhoea at menopause |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No key warnings, contraindications, or drug–drug interaction data were available in this evidence pack (TFDA/TGA labelling query returned a blocking data gap, DG001; DDI query status: not found).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between progesterone and amenorrhoea is direct and clinically well-established (progesterone challenge/withdrawal testing is standard practice), and at least one completed Phase 2/3-equivalent RCT context supports this direction (Evidence Level L2). However, this evidence pack could not confirm progesterone's ARTG registration status, TGA-approved labelling, or safety warnings, so the recommendation cannot proceed without guardrails.

**To proceed, the following is needed:**
- TGA-approved Product Information (PI), including warnings/precautions and contraindications (currently a blocking data gap)
- Confirmed ARTG registration status for progesterone products in Australia (this evidence pack shows 0 entries, which should be independently verified given progesterone's common clinical use)
- Detailed mechanism of action data from DrugBank
- Drug–drug interaction data (current query returned no results)
- Targeted review of the trials/literature above with formal relevance grading, since most records in this pack are still marked "pending" review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

