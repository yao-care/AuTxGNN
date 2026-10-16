---
layout: default
title: Estradiol
parent: Model Prediction Only (L5)
nav_order: 270
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Estradiol: predicted new indication Symptomatic form of fragile X syndrome in female carrier (evidence level L5). Approved use: Primary ovarian failure, postmenopausal osteoporosis…"
monitor_inn: "Estradiol"
predicted_indications: ["symptomatic form of fragile X syndrome in female carrier", "anovulation", "ovarian remnant syndrome", "partial trisomy/tetrasomy of the short arm of chromosome 18", "partial trisomy/tetrasomy of the short arm of chromosome 12", "partial trisomy/tetrasomy of the short arm of chromosome 5", "blepharophimosis-epicanthus inversus-ptosis due to 3q23 rearrangement syndrome", "luteoma of pregnancy", "partial autosomal trisomy/tetrasomy", "ovarian ectopic pregnancy"]
---

# Estradiol
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

# Estradiol: From Primary Ovarian Failure and Menopausal Conditions to Anovulation

## One-Sentence Summary

Estradiol is a natural oestrogen, originally used for primary ovarian failure, postmenopausal osteoporosis and postmenopausal atrophic vaginitis, among other conditions.
The TxGNN model ranks **symptomatic form of fragile X syndrome in female carrier** as its top prediction, but this has no supporting studies. The best-supported prediction is **anovulation**, with **2 clinical trials** and **20 publications** (mostly physiology reviews) currently supporting this direction.

---

## Quick Overview

The top-ranked prediction (rank 1) has no trials or literature. The table therefore shows both the top-ranked prediction and the best-evidenced prediction (anovulation, rank 2), which is the focus of the rest of this report.

| Item | Content |
|------|------|
| Original Indication | Primary ovarian failure, postmenopausal osteoporosis, postmenopausal atrophic vaginitis (the ARTG entries in the data compiled for this report carry no indication text) |
| Predicted New Indication (top-ranked) | Symptomatic form of fragile X syndrome in female carrier |
| Predicted New Indication (best evidenced) | Anovulation |
| TxGNN Prediction Score | 98.76% (top-ranked); 98.58% (anovulation) |
| Evidence Level | L5 (top-ranked); L3 (anovulation) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 3 |
| Recommended Decision | Hold (top-ranked); Research Question (anovulation) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Based on known information, estradiol is the principal endogenous oestrogen. Its efficacy in oestrogen-deficiency states such as primary ovarian failure and menopausal symptoms is established.

**Fragile X female carrier (top-ranked).** Female FMR1 premutation carriers can develop FMR1-related primary ovarian insufficiency. Estradiol is an established replacement therapy for hypo-oestrogenism, which is consistent with its approved use in primary ovarian failure. The high score is a model prediction only, and no trials or literature were found.

**Anovulation (best evidenced).** Estradiol takes part in hypothalamic-pituitary-ovarian feedback and follicular development. Adjunctive estradiol has been tested alongside clomiphene citrate, to counter clomiphene's anti-oestrogenic effects on the endometrium and cervical mucus during ovulation induction. The mechanism is biologically plausible. However, the evidence is limited to small trials or trials of uncertain status, and the retrieved literature is mostly physiology and review work rather than treatment outcomes. In this setting estradiol is an adjunct to ovulation induction, not a standalone treatment for anovulation.

**Other predictions.** Several other predictions are unlikely to be genuine therapeutic opportunities:
- Partial trisomy/tetrasomy disorders (chromosomes 18p, 12p, 5p and the broad autosomal category) show no identifiable mechanistic link. The scores probably reflect knowledge-graph proximity.
- Ovarian remnant syndrome, luteoma of pregnancy and ovarian ectopic pregnancy involve estradiol mainly as a diagnostic or monitoring marker. Exogenous estradiol is not expected to be therapeutic and could be counterproductive.
- Blepharophimosis-ptosis-epicanthus inversus syndrome (BPES) is associated with premature ovarian insufficiency, so estradiol could provide hormone replacement for the ovarian component only. It would not treat the defining craniofacial features.

---

## Clinical Trial Evidence

Trials for **anovulation** (the only prediction with registered trials):

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02186782](https://clinicaltrials.gov/study/NCT02186782) | Phase 4 | Unknown | 600 | Randomised trial of clomiphene citrate plus concomitant estradiol versus clomiphene alone for ovulation induction in infertile women. No results provided. |
| [NCT07398924](https://clinicaltrials.gov/study/NCT07398924) | Not applicable | Completed | 90 | Randomised trial comparing vaginal estradiol and oral guaifenesin, alone or combined, on endometrial thickness, cervical mucus and clinical pregnancy rate in women on clomiphene ovulation induction. No results provided. |

No related clinical trials are registered for the other nine predicted indications. No ANZCTR identifiers were found in the data compiled for this report.

---

## Literature Evidence

Publications for **anovulation**. The retrieved literature is dominated by narrative reviews and physiology or animal work, with no randomised treatment outcomes. The most relevant items are shown:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27566840](https://pubmed.ncbi.nlm.nih.gov/27566840/) | 2016 | Review | Hum Reprod Update | Interactions of androgens, FSH, anti-Müllerian hormone and estradiol in folliculogenesis in normal and polycystic ovaries |
| [22283375](https://pubmed.ncbi.nlm.nih.gov/22283375/) | 2012 | Review | Gynecol Endocrinol | Neuroendocrine control of ovulation. Hypothalamic failure leads to anovulation or amenorrhoea. |
| [22442260](https://pubmed.ncbi.nlm.nih.gov/22442260/) | 2012 | Review | Hum Reprod Update | How neuropeptides integrate the reproductive and energy-balance axes in ovulation and anovulation |
| [16782289](https://pubmed.ncbi.nlm.nih.gov/16782289/) | 2006 | Review | Maturitas | Role of oestrogens in ovarian stimulation |
| [15196714](https://pubmed.ncbi.nlm.nih.gov/15196714/) | 2004 | Review | Eur J Obstet Gynecol Reprod Biol | FSH and LH together in ovarian stimulation for anovulatory disorders |
| [40723795](https://pubmed.ncbi.nlm.nih.gov/40723795/) | 2025 | Review | Biomolecules | Granulosa cell dysfunction in infertility associated with polycystic ovary syndrome (PCOS) and obesity |
| [34975540](https://pubmed.ncbi.nlm.nih.gov/34975540/) | 2021 | Review | Front Physiol | Mechanisms linking PCOS and abnormal endometrium |

For the other predictions, the literature is veterinary case reports and animal models (ovarian remnant syndrome, luteoma of pregnancy) or hormone-measurement and risk-factor studies (ovarian ectopic pregnancy). None shows a therapeutic benefit of estradiol. No literature was found for the fragile X carrier and chromosomal predictions.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10203B | Vagifem Low | Pessary (modified release), 10 micrograms (as hemihydrate) | Not available in the data compiled for this report |
| ARTG 13932G | Estalis sequi 50/140 | Pack of 4 transdermal patches 780 micrograms and 4 patches 620 micrograms estradiol (as hemihydrate) with 2.7 mg norethisterone acetate | Not available in the data compiled for this report |
| ARTG 10146B | Femoston 1/10 | Pack of 14 tablets estradiol 1 mg and 14 tablets estradiol 1 mg with dydrogesterone 10 mg | Not available in the data compiled for this report |

All three entries are currently valid. Routes of administration are vaginal, transdermal and oral.

---

## Safety Considerations

**Contraindications flagged in the knowledge graph.** These are drug-disease contraindication links from the TxGNN knowledge graph, not label text. They should be verified against the Product Information (PI):
- Cardiovascular and metabolic: hypertension, congestive heart failure, diabetes mellitus, hyperglycaemia
- Hepatic, biliary and renal: liver failure, liver disease, gallbladder disease, kidney disease
- Neurological and psychiatric: epilepsy, anxiety disorder, neurotic disorder, dysthymic disorder
- Endocrine: hypothyroidism (including myxedema and congenital hypothyroidism), adrenocortical insufficiency (Addison disease), humoral hypercalcaemia of malignancy
- Other: porphyria, systemic lupus erythematosus, asthma, osteoporosis (listed in the graph, although osteoporosis is also an original indication, so this link should be treated with caution)

**Drug interactions.** The interaction screen returned 100 records; the first 20 are summarised here. Most are of moderate severity:
- Antidiabetic agents: acarbose, alogliptin, albiglutide, metformin, pioglitazone, acetohexamide, chlorpropamide, canagliflozin and dapagliflozin
- Corticosteroids: hydrocortisone, betamethasone, budesonide and dexamethasone
- Others: amoxicillin, aprepitant, clarithromycin, clotrimazole, chenodeoxycholic acid and topical calcitriol (moderate); cimetidine (minor)

Please refer to the TGA-approved Product Information (PI) for full warnings, contraindications and interaction management.

---

## Conclusion and Next Steps

**Decision: Hold**

For the top-ranked prediction (symptomatic fragile X female carrier), the decision is **Hold**. For anovulation, the best-evidenced prediction, the appropriate status is **Research Question**, not a recommendation to proceed.

**Rationale:**
- The top-ranked prediction has a high score (98.76%) but no trials or literature, so it rests on model output alone (L5).
- Anovulation has biological plausibility and two randomised trials of estradiol as an adjunct to clomiphene. One has unknown status and the other is small. Neither has results, and the literature is mainly physiology reviews (L3).
- The remaining predictions are either L5 with no identifiable mechanism, or L4 with estradiol relevant only as a marker rather than a treatment.

**To proceed, the following is needed:**
- Results from NCT02186782 and NCT07398924, or a systematic review of estradiol as an adjunct to clomiphene on endometrial thickness and pregnancy outcomes
- A clearly defined target population and role for estradiol (adjunct to ovulation induction versus standalone)
- For the fragile X carrier prediction, clinical evidence of benefit from hormone replacement in FMR1-related primary ovarian insufficiency
- Mechanism of action data and ARTG approved-indication text, which were not available in the data compiled for this report
- The TGA Product Information safety review (warnings and contraindications), which is missing and needed before any safety screening
- Assessment of route and formulation fit against the three current ARTG products (vaginal, transdermal and oral)
- Review of the knowledge-graph contraindications, particularly cardiovascular, hepatic and thromboembolic risks, for the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

