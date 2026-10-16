---
layout: default
title: Progesterone
parent: Model Prediction Only (L5)
nav_order: 606
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Progesterone: predicted new indication Amenorrhoea (evidence level L5). Approved use: Endometriosis, endometrial carcinoma…"
---

# Progesterone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Progesterone: From Endometriosis to Amenorrhoea

## One-Sentence Summary

Progesterone is a natural steroid hormone, used for endometriosis, endometrial conditions and menopause-related indications, and in Australia it is marketed as a vaginal tablet and as a combination menopausal hormone therapy pack.
The TxGNN model predicts it may be effective for **amenorrhoea**,
with **4 clinical trials** (all indirect, with estrogen as the main tested agent) and **19 publications** (mostly reviews) currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Endometriosis, endometrial carcinoma, postmenopausal osteoporosis and postmenopausal atrophic vaginitis (from the knowledge graph; no ARTG indication text is available) |
| Predicted New Indication | Amenorrhoea |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 per the scoring in the data compiled for this report. However, the Phase 3 trial is only indirectly relevant, so the effective strength is lower (see Conclusion). |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 2 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, progesterone is the natural ovarian and placental progestogen. It is used in gynaecological conditions where the endometrium must be opposed or stabilised, and its efficacy in endometriosis is established.

Progesterone withdrawal induces endometrial shedding in an estrogen-primed uterus. A "progestin challenge" is used diagnostically in secondary amenorrhoea, and progestogen is given cyclically alongside estrogen in hypoestrogenic states (for example in athletes or anorexia nervosa) to protect the endometrium. A 2024 review describes oral micronised progesterone as already used in endocrinology for this purpose (PMID 38652231).

The trials listed below mainly test estrogen replacement, with progesterone as a supporting component. Progesterone's own contribution to treating amenorrhoea is therefore plausible but not directly demonstrated.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00946192](https://clinicaltrials.gov/study/NCT00946192) | Phase 3 | Completed | 121 | Young athletes with menstrual dysfunction. Tests whether transdermal or oral estrogen improves bone density; progesterone's specific role is unclear. |
| [NCT00088153](https://clinicaltrials.gov/study/NCT00088153) | Phase 2/3 | Completed | 110 | Adolescents with anorexia nervosa. Estrogen to maintain bone development; the outcome is bone mass, not menses restoration. |
| [NCT03740204](https://clinicaltrials.gov/study/NCT03740204) | Phase 2 | Active, not recruiting | 120 | Transdermal estradiol with cyclic progesterone versus placebo in eating disorders. Outcomes are cognitive and reward processing. |
| [NCT03018366](https://clinicaltrials.gov/study/NCT03018366) | Phase 2 | Completed | 29 | Functional hypothalamic amenorrhoea. Cardiovascular risk markers and inflammation in hypoestrogenaemia. |

No ANZCTR trial identifiers are available in the data compiled for this report.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38652231](https://pubmed.ncbi.nlm.nih.gov/38652231/) | 2024 | Review | Rev Endocr Metab Disord | Diagnostic and therapeutic use of oral micronised progesterone in endocrinology, including control of the cycle and endometrial effects |
| [33716979](https://pubmed.ncbi.nlm.nih.gov/33716979/) | 2021 | Review | Front Endocrinol | Aetiology, symptoms and treatment of premature ovarian insufficiency |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Review | Rev Endocr Metab Disord | Endocrine background of hormonal treatments for endometriosis |
| [32233689](https://pubmed.ncbi.nlm.nih.gov/32233689/) | 2020 | Review | Climacteric | Clinical management of vaginal bleeding in postmenopausal women |
| [8629565](https://pubmed.ncbi.nlm.nih.gov/8629565/) | 1996 | Review | Am Fam Physician | Evaluation of amenorrhoea; pregnancy must be excluded first |
| [22283375](https://pubmed.ncbi.nlm.nih.gov/22283375/) | 2012 | Review | Gynecol Endocrinol | Neuroendocrine control of ovulation and hypothalamic causes of amenorrhoea |
| [28257537](https://pubmed.ncbi.nlm.nih.gov/28257537/) | 2017 | Review | South Med J | Primary ovarian insufficiency; hormone replacement is needed for secondary amenorrhoea |
| [7457308](https://pubmed.ncbi.nlm.nih.gov/7457308/) | 1980 | Review | Am Fam Physician | Amenorrhoea work-up, including withdrawal bleeding after progesterone alone |

The retrieved literature is almost entirely review-level or descriptive. No randomised trial of progesterone for amenorrhoea was identified.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10116K | Endometrin | Vaginal tablet 100 mg | Not available in the data compiled for this report |
| ARTG 14720R | Estrogel Pro | Pack with 30 capsules of micronised progesterone 100 mg and estradiol transdermal gel 750 micrograms per 1.25 g dose (64 doses) | Not available in the data compiled for this report |

## Safety Considerations

- **Contraindications (from knowledge-graph associations, not label text):** hypertensive disorders, liver failure and liver disease, epilepsy, anxiety and neurotic disorders, porphyria, kidney disease, gallbladder disease, hyperglycaemia and diabetes mellitus (including diabetic ketoacidosis), hypothyroidism, osteoporosis, systemic lupus erythematosus, asthma, hypertriglyceridaemia, and substance abuse or dependence.
- **Drug interactions (100 recorded; all those shown are of Moderate level):** mainly antidiabetic agents, which may be affected by progesterone's effect on glucose, including acarbose, metformin, pioglitazone, glimepiride, repaglinide, chlorpropamide, canagliflozin, dapagliflozin, empagliflozin, alogliptin, saxagliptin, GLP-1 agonists (albiglutide, dulaglutide, liraglutide, semaglutide) and insulins (aspart, degludec, detemir). Others include aprepitant and clarithromycin.

Please refer to the TGA-approved Product Information (PI) for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is plausible, and progesterone challenge and cyclic progestogen are already established in clinical endocrinology. However, the supporting trials test estrogen and do not directly isolate progesterone for amenorrhoea. The L1 label overstates the strength, because the single Phase 3 trial is only indirectly relevant.

**To proceed, the following is needed:**
- Review of the PI for the ARTG products, including approved indications and contraindications
- Direct comparative evidence of progesterone for amenorrhoea (menses restoration), ideally by differentiating primary, secondary and hypothalamic causes
- Mechanism of action data
- Exclusion of pregnancy and assessment of the contraindication and glucose-lowering interaction profile before use
- Confirmation of a suitable route and formulation, since the registered Australian products are a vaginal tablet and a combined estradiol pack

**Other predicted indications (for context):**
The next-ranked predictions were cervical endometriosis, endometriosis of the rectovaginal septum and endometriosis in a cutaneous scar. These are extrapolations from the existing endometriosis indication. Breast fibrocystic disease and benign mammary dysplasia have observational or review-level evidence only. Renal hypoplasia, blunt duct adenosis and apocrine adenosis have no credible supporting evidence and are rated Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

