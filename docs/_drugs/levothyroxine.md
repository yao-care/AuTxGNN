---
layout: default
title: Levothyroxine
parent: 僅模型預測 (L5)
nav_order: 395
evidence_level: L5
indication_count: 10
---

# Levothyroxine
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

# Levothyroxine: From Hypothyroidism to Endemic Goiter

## One-Sentence Summary

Levothyroxine (LT4) is a synthetic thyroid hormone used as replacement therapy in hypothyroidism (deficient thyroid hormone production). The TxGNN model predicts it may also be effective for **Endemic Goiter**, with **1 clinical trial** and **20 publications** currently identified — though the trial does not test levothyroxine directly, and most of the literature is decades-old observational/cohort data on iodine-deficiency goitre rather than dedicated LT4 efficacy trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypothyroidism (thyroid hormone replacement) — inferred from the drug's established pharmacology cited across this evidence pack; a formal TFDA/regulator-approved indication text was not available in this dataset (see Data Gap DG001) |
| Predicted New Indication | Endemic Goiter |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L3 (Observational studies / review-level evidence) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this candidate is not available in the evidence pack (Data Gap DG002, High severity). Based on the information that is available, levothyroxine is a thyroid hormone replacement agent whose efficacy in hypothyroidism is well established; mechanistically this may extend to endemic goiter.

Endemic goiter is most commonly caused by chronic iodine deficiency, leading to compensatory thyroid enlargement and, in more severe cases, hypothyroidism. Levothyroxine's physiological role as thyroid hormone replacement gives it a direct and biologically plausible mechanistic link to this condition — supplementing circulating thyroxine can normalise the hypothalamic-pituitary-thyroid axis and reduce TSH-driven glandular hyperplasia.

However, the evidence pack's own rationale flags an important caveat: **the first-line prevention and treatment for endemic goiter is iodine repletion (iodized salt/oil), not levothyroxine monotherapy.** LT4 alone does not correct the underlying intrathyroidal iodine deficiency and relapse after LT4-only therapy has been reported (PMID 8147031). This means the mechanistic plausibility is real, but levothyroxine would likely play a supportive/adjunct role rather than a primary repurposing indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04482907](https://clinicaltrials.gov/study/NCT04482907) | Phase NA | Completed | 68 | Randomised placebo-controlled study of *Anethum graveolens* (dill) extract — not levothyroxine — in thyroiditis and nodular goiter patients; evaluated hormone levels and nodule size over 90 days. Evidence-pack relevance grading: **C (low)** — tests a different agent, not a direct LT4 trial for endemic goiter. |

No trial in this dataset directly tests levothyroxine in endemic goiter.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24393641](https://pubmed.ncbi.nlm.nih.gov/24393641/) | 1998 | Cohort | Asia Pacific J Clin Nutr | Longitudinal study of 100 µg/day levothyroxine in an iodine-deficient indigenous population (Malaysia) with endemic goitre, followed for 1.5 years (n=311 at baseline) |
| [3278876](https://pubmed.ncbi.nlm.nih.gov/3278876/) | 1988 | Multicenter trial (not classified) | Dtsch Med Wochenschr | 74 patients with diffuse endemic goitre randomised to 150 µg LT4 alone vs. 100 µg LT4 + iodide over 6 months; both regimens reduced goitre volume |
| [25629792](https://pubmed.ncbi.nlm.nih.gov/25629792/) | 2015 | RCT/Cohort | Curr Med Res Opin | Maternal iodine supplementation study (n=460) comparing goitre-endemic vs. non-endemic areas; assessed thyroid function and birth outcomes |
| [4312017](https://pubmed.ncbi.nlm.nih.gov/4312017/) | 1969 | Cohort (iodized oil) | Am J Clin Nutr | Prophylaxis/treatment of endemic goiter with iodized oil in rural Ecuador and Peru |
| [263304](https://pubmed.ncbi.nlm.nih.gov/263304/) | 1978 | Cohort | J Clin Endocrinol Metab | Maternal-newborn thyroid function in a severe endemic goitre area (Zaïre); iodine correction via iodized oil compared with untreated mothers |
| [8147031](https://pubmed.ncbi.nlm.nih.gov/8147031/) | 1993 | Not classified | Z Gesamte Inn Med | Reviews drug therapy of goiter (iodine vs. thyroid hormone vs. combined); notes LT4 alone fails to correct intrathyroidal iodine deficiency and relapse is common |
| [2031356](https://pubmed.ncbi.nlm.nih.gov/2031356/) | 1991 | Review | World J Surg | Establishes iodine deficiency as the primary cause of endemic goiter; iodine supplementation remains the mainstay of prevention/treatment |
| [7704809](https://pubmed.ncbi.nlm.nih.gov/7704809/) | 1994 | Review | Curr Ther Endocrinol Metab | General review of endemic goiter (abstract not available in source) |
| [6309889](https://pubmed.ncbi.nlm.nih.gov/6309889/) | 1983 | Not classified | J Clin Endocrinol Metab | Iodized-oil injection in 58 goitrous patients from a mildly iodine-deficient area (Greece); goitre size decreased post-treatment |
| [3090091](https://pubmed.ncbi.nlm.nih.gov/3090091/) | 1986 | Not classified | J Clin Endocrinol Metab | Cross-sectional study (n=1218) of thyroid function in an endemic goitre area of northern Italy |

---

## Australia Market Information

Levothyroxine is currently recorded as **not marketed** in this dataset, with **0 ARTG entries**. No product-level licence information was available to summarise in this evidence pack.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between levothyroxine and endemic goiter is biologically plausible (thyroid hormone replacement for iodine-deficiency-related hypothyroidism/glandular hyperplasia) and is supported by decades of cohort/observational data. However, no clinical trial in this dataset directly tests LT4 for endemic goiter (the single retrieved trial studies a dill extract), and the literature itself indicates iodine repletion — not LT4 monotherapy — is the recognised first-line approach, with LT4-only therapy prone to relapse.

**To proceed, the following is needed:**
- TFDA/TGA-approved Product Information, including warnings and contraindications (Data Gap DG001 — currently blocking safety pre-assessment)
- Confirmed mechanism-of-action documentation (Data Gap DG002)
- A direct clinical trial or comparative study of levothyroxine (alone or with iodine) specifically in endemic goitre populations
- Confirmation of the drug's regulator-approved original indication text
- Clarification of levothyroxine's role as adjunct vs. primary therapy relative to iodine repletion in this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

