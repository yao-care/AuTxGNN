---
layout: default
title: Testosterone
parent: 僅模型預測 (L5)
nav_order: 664
evidence_level: L5
indication_count: 10
---

# Testosterone
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

# Testosterone: From Androgen Deficiency to Primary Ovarian Failure and Testicular Regression Syndrome

## One-Sentence Summary

Testosterone (DrugBank DB00624) is the endogenous androgen used for over 60 years to treat male hypogonadism (androgen deficiency); detailed original-indication text and mechanism-of-action data were not captured in this dataset. TxGNN screened **10 candidate new indications** for this drug — of these, only two show credible supporting evidence: **Primary Ovarian Failure/Insufficiency (POI/POF)**, backed by **26 clinical trials and 20 publications** (including a Grade-A relevance Phase 1/2 RCT), and **Testicular Regression Syndrome (TRS)**, backed by **1 clinical trial and 19 publications**. The remaining eight candidates are either purely computational artifacts or, in one case (freemartinism), a veterinary-only concept with no human translational value, and are **not recommended** for further work.

---

## Screening Overview — All 10 Candidate Indications

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|-----------------|
| 1 | Polysomy of X chromosome | 94.88% | L4 | S1 | Research Question |
| 2 | Tetragametic chimerism | 94.66% | L4 | S1 | Research Question |
| 3 | Penile/testicular agenesis | 94.62% | L5 | S0 | Hold |
| 4 | **Testicular regression syndrome** | 94.46% | **L3** | **S2** | **Proceed with Guardrails** |
| 5 | Leydig cell hypoplasia due to LH resistance | 94.24% | L4 | S1 | Research Question |
| 6 | Urethral obstruction sequence | 94.18% | L5 | S0 | Hold |
| 7 | 46,XX DSD–anorectal anomalies syndrome | 94.15% | L4 | S1 | Research Question |
| 8 | Freemartinism | 94.03% | L5 | S0 | Hold |
| 9 | Arthrogryposis–epileptic seizures–migrational brain disorder | 93.84% | L5 | S0 | Hold |
| 10 | **Primary ovarian failure** | 93.73% | **L2** | **S2** | **Proceed with Guardrails** |

Note the counter-intuitive pattern: the raw TxGNN similarity score is highest for rank 1–3, but these have **no supporting clinical trials or literature at all** — they are pure knowledge-graph inferences. The two indications with real evidentiary support (ranks 4 and 10) sit lower in the raw score but are the only ones fit for further evaluation. The rest of this report focuses on those two.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in this dataset (no TGA/ARTG record); literature within this pack (PMID 15799128) confirms testosterone replacement is the established treatment of male hypogonadism |
| Lead Predicted Indication 1 | Primary Ovarian Failure (POI/POF) |
| Lead Predicted Indication 2 | Testicular Regression Syndrome (TRS) |
| TxGNN Prediction Score (POI) | 93.73% |
| TxGNN Prediction Score (TRS) | 94.46% |
| Evidence Level (POI) | L2 |
| Evidence Level (TRS) | L3 |
| Australia Market Status | Not Marketed (per this dataset — see caveat below) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails (both leads), Hold on all other 8 candidates |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Testosterone was not available in this dataset (flagged as a High-severity data gap). Based on the literature retrieved within this pack, Testosterone is the principal circulating androgen and the reference therapy for androgen replacement — "Testosterone therapy has been used for more than 60 years in the treatment of male hypogonadism... [including] Klinefelter's syndrome, anorchia, or acquired disturbances of testicular function" (PMID 15799128).

**Testicular Regression Syndrome** is, mechanistically, a subtype of primary hypogonadism: the testes form and function in early fetal life but subsequently regress, leaving a 46,XY phenotypic male with hypergonadotropic hypogonadism and absent endogenous testosterone. Since exogenous testosterone replacement is already the accepted standard for congenital anorchia (to induce and maintain puberty/virilisation), the TxGNN prediction reproduces an established clinical practice rather than proposing something novel — hence the more mature L3 evidence tier despite the absence of RCTs (rare-disease population makes RCTs impractical).

**Primary Ovarian Failure/Insufficiency** is mechanistically different: androgens (including testosterone) are physiologically produced by the ovarian stroma, and women with POI/POF have documented low circulating testosterone (PMID 17070197, PMID 22525963 systematic review/meta-analysis). The rationale here is androgen-replacement-as-adjunct — improving mood, quality of life, and ovarian/follicular responsiveness during fertility treatment — rather than treating the ovarian failure itself. This is an active, if still adjunctive, area of reproductive endocrinology research, reflected in the Grade-A relevance Phase 1/2 RCT (NCT01662466) and a completed Phase 2 hormone-replacement trial (NCT00001951).

---

## Clinical Trial Evidence

### Testicular Regression Syndrome

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05379556](https://clinicaltrials.gov/study/NCT05379556) | N/A | Recruiting | 100 | Andrological/reproductive/sexual function evaluation in Long-COVID survivors; relevance is indirect (Grade C) — not a TRS-treatment trial, may capture testicular-damage phenotypes overlapping with TRS assessment |

No dedicated interventional trial of testosterone specifically for TRS was found; management evidence is drawn from case series and practice-pattern reviews (below).

### Primary Ovarian Failure (POI/POF)

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01662466](https://clinicaltrials.gov/study/NCT01662466) | Phase 1/2 | Unknown (status not updated) | 180 | RCT, transdermal testosterone vs placebo in women with diminished ovarian reserve undergoing IVF; assesses follicular development, oocyte/embryo quality (Grade A relevance — needs verification of completion/publication) |
| [NCT00001951](https://clinicaltrials.gov/study/NCT00001951) | Phase 2 | Completed | 250 | Hormone replacement (including androgen) in young women with POF — first systematic evaluation of adding androgen to standard oestrogen-based HRT (Grade B) |
| [NCT06343870](https://clinicaltrials.gov/study/NCT06343870) | Phase 3 | Recruiting | 140 | Subdermal testosterone + oestradiol implants in natural/surgical menopause and POF; pharmacokinetic and clinical/hormonal outcomes |
| [NCT00650754](https://clinicaltrials.gov/study/NCT00650754) | Phase 2/3 | Terminated | 35 | DHEA (androgen precursor, not testosterone itself) for premature ovarian ageing; relevant mechanism but different molecule (Grade C) |
| [NCT00948857](https://clinicaltrials.gov/study/NCT00948857) | Phase 2/3 | Terminated | 5 | DHEA supplementation in POF couples; terminated with minimal enrolment |
| [NCT01129947](https://clinicaltrials.gov/study/NCT01129947) | Early Phase 1 | Withdrawn | 0 | DHEA in POF — withdrawn before enrolment (Grade C) |
| [NCT05737329](https://clinicaltrials.gov/study/NCT05737329) | Phase 1/2 | Unknown | 80 | Management-optimisation study for POI including serum total testosterone as an outcome measure |
| [NCT02922348](https://clinicaltrials.gov/study/NCT02922348) | Phase 3 | Withdrawn | 0 | Optimal hormone replacement (HRT vs COC) for POI — withdrawn before enrolment |
| [NCT06866119](https://clinicaltrials.gov/study/NCT06866119) | N/A | Not yet recruiting | 45 | Oestrogen (not testosterone) replacement, cardiometabolic endpoints in POI — included for context only |
| [NCT06841328](https://clinicaltrials.gov/study/NCT06841328) | N/A | Recruiting | 60 | Stem-cell/exosome therapy for gonadal failure incl. POF — different modality, included for landscape context |

---

## Literature Evidence

### Testicular Regression Syndrome

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31013155](https://pubmed.ncbi.nlm.nih.gov/31013155/) | 2019 | Review | Endocr Pract | Practice-pattern review across 57 patients — wide variation in diagnosis/management of TRS |
| [15799128](https://pubmed.ncbi.nlm.nih.gov/15799128/) | 2004 | Review | Aging Male | 60+ year history of testosterone therapy for male hypogonadism, including anorchia |
| [36631784](https://pubmed.ncbi.nlm.nih.gov/36631784/) | 2023 | Cohort/Case report | BMC Endocr Disord | 15-year follow-up: testosterone modulates growth pattern and IGF-1 in vanishing testis syndrome |
| [38359811](https://pubmed.ncbi.nlm.nih.gov/38359811/) | 2025 | Cohort | Horm Res Paediatr | DHX37 variant identified as a common genetic cause of TRS/partial gonadal dysgenesis in Japanese patients |
| [25489355](https://pubmed.ncbi.nlm.nih.gov/25489355/) | 2014 | Case series | Pan Afr Med J | Embryonic TRS: report of 6 cases |
| [122413](https://pubmed.ncbi.nlm.nih.gov/122413/) | 1978 | Case report | J Clin Endocrinol Metab | Anorchia and persistent Müllerian duct — variant of embryonic TRS, low testosterone with no hCG response |
| [18353](https://pubmed.ncbi.nlm.nih.gov/18353/) | 1977 | Case report | Eur Urol | Anorchia diagnosis protocol using testosterone response to hCG stimulation |
| [6143546](https://pubmed.ncbi.nlm.nih.gov/6143546/) | 1983 | Case series | Arch Fr Pediatr | 10 boys with anorchidism; androgen administration described as the only treatment option |
| [1941794](https://pubmed.ncbi.nlm.nih.gov/1941794/) | 1991 | Case report | J Reprod Med | TRS in a 46,XY phenotypic female — late embryonic testicular insult |
| [35035874](https://pubmed.ncbi.nlm.nih.gov/35035874/) | 2022 | Review | Ther Adv Endocrinol Metab | Recent advances in treating hypogonadism in boys/adolescents, including anorchia |

### Primary Ovarian Failure (POI/POF)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22525963](https://pubmed.ncbi.nlm.nih.gov/22525963/) | 2012 | Systematic review & meta-analysis | Hum Reprod Update | Testosterone concentrations across types of ovarian insufficiency — establishes the low-androgen rationale |
| [39647506](https://pubmed.ncbi.nlm.nih.gov/39647506/) | 2024 | Guideline/Review | Climacteric | Evidence-based international guideline on POI diagnosis and management |
| [39660328](https://pubmed.ncbi.nlm.nih.gov/39660328/) | 2024 | Guideline/Review | Hum Reprod Open | Companion publication of the same evidence-based POI guideline |
| [39652037](https://pubmed.ncbi.nlm.nih.gov/39652037/) | 2025 | Guideline/Review | Fertil Steril | Companion publication of the same evidence-based POI guideline |
| [24473536](https://pubmed.ncbi.nlm.nih.gov/24473536/) | 2014 | Interventional study | Menopause | Physiologic testosterone added to standard oestrogen/progestin therapy improved QoL, self-esteem and mood in POI |
| [35254428](https://pubmed.ncbi.nlm.nih.gov/35254428/) | 2022 | Review | J Clin Endocrinol Metab | Critical appraisal of DHEA (androgen precursor) administration in women |
| [17070197](https://pubmed.ncbi.nlm.nih.gov/17070197/) | 2006 | Observational | Fertil Steril | Confirmed lower free testosterone in young women with 46,XX spontaneous POF vs controls |
| [31327696](https://pubmed.ncbi.nlm.nih.gov/31327696/) | 2019 | Review | Best Pract Res Clin Endocrinol Metab | Primary gonadal failure across sexes, including androgen/oestrogen replacement strategies |
| [9526706](https://pubmed.ncbi.nlm.nih.gov/9526706/) | 1998 | Observational | Gynecol Endocrinol | Androgen biosynthesis and autoimmunity compared between POF patients and controls |
| [7782452](https://pubmed.ncbi.nlm.nih.gov/7782452/) | 1995 | Observational | Hum Reprod | Testosterone/androstenedione levels in POF pregnancies — evidence of ovarian androgen source |

---

## Australia Market Information

This dataset returned **Not Marketed** status with **0 ARTG entries** for Testosterone. This is an unexpected result for a decades-old, widely used therapeutic hormone and most likely reflects an incomplete ARTG data-extraction/matching step in this pipeline rather than genuine market absence. **Recommend verifying directly against the TGA ARTG public search** before treating Testosterone as unavailable in Australia — this also blocks the "Australia Market Information" table (no licenses to list).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. This dataset carries a **Blocking**-severity data gap (TGA/PI warnings and contraindications not retrieved), which prevents a formal S1 safety pre-assessment for any of the candidate indications above — treat both "Proceed with Guardrails" calls below as provisional on this gap being closed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (Primary Ovarian Failure and Testicular Regression Syndrome only) / **Hold** (remaining 8 candidates)

**Rationale:**
- POI (L2) and TRS (L3) are the only candidates with a coherent mechanism *and* corroborating clinical/literature evidence; both represent androgen-replacement-adjacent uses that already have precedent in clinical endocrinology.
- The other 8 candidates either have zero supporting trials/literature (pure KG-embedding artifacts, e.g. polysomy of X chromosome, urethral obstruction sequence) or, in the case of freemartinism, are exclusively a veterinary phenomenon with no human translational pathway.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications, DDI) — currently a Blocking data gap
- Verified Testosterone MOA detail from DrugBank/product literature (currently a High-severity data gap)
- Direct TGA ARTG search to confirm actual Australian market/registration status (the "0 entries / Not Marketed" result in this dataset is very likely incomplete)
- For POI: confirmation of current status/results for NCT01662466 (listed "Unknown" despite being the most directly relevant RCT)
- For TRS: given the rare-disease population, expect guideline/expert-consensus evidence rather than future RCTs — assess via specialist paediatric endocrinology input rather than awaiting trial data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

