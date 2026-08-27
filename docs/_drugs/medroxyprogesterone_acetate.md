---
layout: default
title: Medroxyprogesterone Acetate
parent: 僅模型預測 (L5)
nav_order: 420
evidence_level: L5
indication_count: 10
---

# Medroxyprogesterone Acetate
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

# Medroxyprogesterone Acetate: From Hormonal Contraception/Menstrual Disorder Management to Amenorrhoea

## One-Sentence Summary

Medroxyprogesterone acetate (MPA) is a synthetic progestogen long used as a contraceptive (oral and depot injection) and for managing menstrual disorders. The TxGNN model predicts it may be effective for **amenorrhoea**, a use that is largely already recognised in existing pharmacology rather than a novel discovery, with **10 clinical trials** and **20 publications** currently identified as supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from this Evidence Pack (0 ARTG entries); MPA is generally known for contraception (oral/depot injection) and management of secondary amenorrhoea/abnormal uterine bleeding |
| Predicted New Indication | Amenorrhoea (disease) |
| TxGNN Prediction Score | 99.9994% |
| Evidence Level | L2 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not returned by DrugBank for this drug. Based on well-established pharmacology, medroxyprogesterone acetate is a synthetic progestogen (progesterone-receptor agonist), available as an oral tablet and as a long-acting depot injection (DMPA). It suppresses the hypothalamic–pituitary–ovarian axis (inhibiting GnRH/LH pulsatility) and induces endometrial atrophy/decidualisation — the basis for its long-standing clinical use in inducing withdrawal bleeding, treating secondary amenorrhoea and abnormal uterine bleeding, and providing long-acting contraception.

Amenorrhoea is therefore not a truly novel indication for MPA: it is mechanistically continuous with the drug's known progestogenic effects. MPA is used therapeutically to manage amenorrhoea/abnormal bleeding, and at contraceptive doses (DMPA) commonly *causes* amenorrhoea as an expected on-therapy effect. The evidence pack's own rationale flags this directly — describing the mechanism as "textbook-level" for MPA and closer to reinforcement of an existing indication than a new repurposing hypothesis.

The strongest single trial (NCT02449161, Phase 3) directly tested post-ablation MPA for endometrial amenorrhoea rates, but it was terminated with a small sample (n=60), limiting definitive conclusions. Supporting literature spans DMPA-induced amenorrhoea management and endometrial/hormonal correlates, consistent with this mechanistic picture.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02792153](https://clinicaltrials.gov/study/NCT02792153) | Phase 1 | Withdrawn | 0 | Estradiol and fear extinction for calorie-dense foods in weight-restored anorexia nervosa; withdrawn, no enrolment — limited relevance |
| [NCT07020429](https://clinicaltrials.gov/study/NCT07020429) | N/A | Not yet recruiting | 276 | Chinese herbal formula (Huanjingjian decoction) for premature ovarian insufficiency; no MPA arm |
| [NCT03309176](https://clinicaltrials.gov/study/NCT03309176) | Phase 4 | Completed | 42 | Tested whether progesterone-induced withdrawal bleeding is necessary before ovulation induction in women with oligo-/amenorrhoea |
| [NCT00808132](https://clinicaltrials.gov/study/NCT00808132) | Phase 3 | Completed | 1886 | Large RCT of bazedoxifene/conjugated estrogens for menopausal symptoms, endometrial protection and osteoporosis prevention |
| [NCT03018366](https://clinicaltrials.gov/study/NCT03018366) | Phase 2 | Completed | 29 | Functional hypothalamic amenorrhoea and cardiovascular risk markers associated with low-estrogen states |
| [NCT00392093](https://clinicaltrials.gov/study/NCT00392093) | Phase 4 | Completed | 108 | HRT effects on disease activity, menopausal symptoms and bone mineral density in peri/postmenopausal women with SLE |
| [NCT02449161](https://clinicaltrials.gov/study/NCT02449161) | Phase 3 | Terminated | 60 | Direct test of post-ablation MPA on endometrial amenorrhoea rates — most directly relevant trial, but terminated early with small sample |
| [NCT01300676](https://clinicaltrials.gov/study/NCT01300676) | Phase 2/3 | Completed | 79 | Tualang honey vs HRT safety profile in postmenopausal women |
| [NCT06671548](https://clinicaltrials.gov/study/NCT06671548) | Phase 3 | Recruiting | 120 | Relugolix vs placebo for heavy menstrual bleeding associated with uterine fibroids |
| [NCT01463202](https://clinicaltrials.gov/study/NCT01463202) | Phase 4 | Completed | 184 | Timing of postpartum DMPA administration and its effect on breastfeeding continuation, contraceptive continuation and postpartum depression |

No ANZCTR (Australian New Zealand Clinical Trials Registry) entries were identified for this indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38530848](https://pubmed.ncbi.nlm.nih.gov/38530848/) | 2024 | RCT | PLoS One | WHICH randomised trial comparing DMPA-IM and NET-EN effects on estradiol levels, mood, sexual activity and menstrual patterns relevant to HIV risk |
| [9554247](https://pubmed.ncbi.nlm.nih.gov/9554247/) | 1998 | RCT | Contraception | Women with DMPA-induced amenorrhoea randomised to switch to Cyclofem or continue DMPA; 82% resumed bleeding on Cyclofem vs 10% on DMPA |
| [23641480](https://pubmed.ncbi.nlm.nih.gov/23641480/) | 2013 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Review of combination injectable contraceptives' efficacy and acceptability |
| [842303](https://pubmed.ncbi.nlm.nih.gov/842303/) | 1977 | Comparative Study | Acta Obstet Gynecol Scand | Endometrial histology and circulating MPA/estradiol/gonadotropin levels compared between MPA-induced and secondary amenorrhoea |
| [8725701](https://pubmed.ncbi.nlm.nih.gov/8725701/) | 1996 | Review | J Reprod Med | Counselling framework and management of DMPA side effects, including amenorrhoea |
| [6141923](https://pubmed.ncbi.nlm.nih.gov/6141923/) | 1984 | Review | Drug Intell Clin Pharm | Review of drug-induced infertility via hypothalamic-pituitary-gonadal axis effects, including progestogens |
| [6119259](https://pubmed.ncbi.nlm.nih.gov/6119259/) | 1981 | Review | Int J Gynaecol Obstet | Postpartum contraception review, including timing relative to postpartum amenorrhoea |
| [120837](https://pubmed.ncbi.nlm.nih.gov/120837/) | 1979 | Review | IARC Monographs | Pharmacological/toxicological monograph on medroxyprogesterone acetate |
| [8492647](https://pubmed.ncbi.nlm.nih.gov/8492647/) | 1993 | Review | MCN Am J Matern Child Nurs | Overview of Depo-Provera (DMPA) clinical use |
| [12222332](https://pubmed.ncbi.nlm.nih.gov/12222332/) | 1991 | Review | Entre Nous | Overview of once-a-month estrogen/progestogen injectable contraceptives |

---

## Australia Market Information

MPA currently has no ARTG (Australian Register of Therapeutic Goods) entries in this Evidence Pack — market status is recorded as **Not Marketed**, with 0 registered licences.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No key warnings, contraindications or drug interaction data were available in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic case is strong and well-established (MPA's progestogenic suppression of the HPO axis and endometrial effects already underpin its known role in amenorrhoea/abnormal bleeding management), and evidence level reaches L2. However, this is offset by the absence of Australian market presence (0 ARTG entries), missing MOA confirmation, and a Blocking data gap on TFDA/PI warnings and contraindications, which prevents a full safety assessment.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications) — currently a Blocking data gap
- Confirmed mechanism of action detail from DrugBank
- Clarification of MPA's current registration status in Australia, given 0 ARTG entries
- Follow-up on the terminated NCT02449161 trial or a replacement adequately powered study, since it is the only trial directly testing MPA for amenorrhoea
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

