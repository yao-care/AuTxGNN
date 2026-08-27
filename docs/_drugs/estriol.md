---
layout: default
title: Estriol
parent: 僅模型預測 (L5)
nav_order: 251
evidence_level: L5
indication_count: 10
---

# Estriol
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

# Estriol: From an Unrecorded Original Indication to a Predicted Role in Amenorrhea

## One-Sentence Summary

Estriol's original approved indication and mechanism of action are not documented in this evidence pack (data gap), and the drug is not currently marketed in Australia. The TxGNN model predicts it may be effective for **Amenorrhea**, with **3 registered clinical trials** and **13 publications** currently associated with this direction — though the relevance screening flags most of the trial evidence as likely referring to a different drug (Estetrol) or as withdrawn, leaving one directly relevant observational study as the strongest support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for Estriol in this evidence pack, and no original indication is on file. Based on the supporting literature gathered against this prediction, Estriol is described as a weak estrogen receptor agonist that exerts feedback modulation on the hypothalamic-pituitary-gonadal (HPG) axis.

Because the original indication is unrecorded, a direct comparison between "original" and "new" indication cannot be made. However, the strongest piece of direct evidence — a cohort/pilot study (PMID 22137494) — shows that Estriol administration modulates luteinizing hormone (LH) secretion in women with functional hypothalamic amenorrhea (FHA), and a companion review (PMID 37371858) discusses low-dose estrogens, including Estriol, as neuroendocrine modulators that may help trigger restoration of the positive-feedback mechanism underlying ovulatory cycles in FHA.

Mechanistically this is plausible: FHA is characterised by hypoestrogenism secondary to impaired GnRH pulsatility, so exogenous low-dose estrogen exposure could theoretically support HPG axis recovery. This remains a mechanistic/observational-level hypothesis rather than confirmed clinical benefit.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04090957](https://clinicaltrials.gov/study/NCT04090957) | Phase 3 | Completed | 1015 | E4Comfort Study II — evaluated Estetrol (E4) 15/20 mg vs placebo for vasomotor symptoms in postmenopausal women. Relevance screening flags this as a likely Estriol/Estetrol name mismatch; not amenorrhea-focused and not confirmed as Estriol data. |
| [NCT04209543](https://clinicaltrials.gov/study/NCT04209543) | Phase 3 | Completed | 1570 | E4Comfort Study I — companion trial, same Estetrol/Drospirenone vasomotor-symptom design. Same name-mismatch caution applies. |
| [NCT04487392](https://clinicaltrials.gov/study/NCT04487392) | Phase 2 | Withdrawn | 0 | Photobiomodulation for vulvovaginal atrophy in postmenopausal women; withdrawn with zero enrolment, no usable data, and not an amenorrhea study. |

**Caution:** None of the three registered trials constitute reliable, confirmed Estriol-specific evidence for amenorrhea — two are probable database mismatches with Estetrol, and one generated no data.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22137494](https://pubmed.ncbi.nlm.nih.gov/22137494/) | 2012 | Cohort/Pilot | Fertility and Sterility | Estriol administration modulates LH secretion in women with functional hypothalamic amenorrhea — the most direct Estriol-specific evidence for this indication. |
| [37371858](https://pubmed.ncbi.nlm.nih.gov/37371858/) | 2023 | Review | Biomedicines | Reviews low-dose estrogens (including Estriol) as neuroendocrine modulators in FHA, discussing a potential mechanism for restoring gonadotropin feedback. |
| [16526238](https://pubmed.ncbi.nlm.nih.gov/16526238/) | 2005 | Cohort | Medicinski pregled | Effects of estro-progestagens on lipid/hormonal profiles in premature primary ovarian failure (a hypergonadotropic amenorrhea state). |
| [7026111](https://pubmed.ncbi.nlm.nih.gov/7026111/) | 1981 | Review | Clinical Obstetrics and Gynecology | General review of hormonal contraception and neoplasia risk; not amenorrhea-specific. |
| [4254759](https://pubmed.ncbi.nlm.nih.gov/4254759/) | 1971 | Review | British Journal of Psychiatry | Historical review of anorexia nervosa, a recognised cause of secondary/functional amenorrhea; no Estriol intervention data. |
| [2949864](https://pubmed.ncbi.nlm.nih.gov/2949864/) | 1986 | Observational (non-English) | Zhong Xi Yi Jie He Za Zhi | Observational report on gonadal function changes in amenorrhea/oligomenorrhea patients. |
| [5935707](https://pubmed.ncbi.nlm.nih.gov/5935707/) | 1966 | Case series | American Journal of Obstetrics and Gynecology | Prolonged gynecologic/endocrine manifestations after medroxyprogesterone acetate in pregnancy; not Estriol-specific. |
| [4102186](https://pubmed.ncbi.nlm.nih.gov/4102186/) | 1971 | Case report | Lancet | Endocrinological findings in two patients with premature ovarian failure. |
| [979592](https://pubmed.ncbi.nlm.nih.gov/979592/) | 1976 | Methods/Assay | Die Medizinische Welt | Radioimmunoassay methodology for LH, FSH, progesterone, estrone, estradiol and estriol; assay technique, not therapeutic evidence. |
| [13931724](https://pubmed.ncbi.nlm.nih.gov/13931724/) | 1963 | Mechanistic Review | Journal of Clinical Endocrinology and Metabolism | Mechanistic review of anti-ovulatory compound action; background pharmacology only. |

## Australia Market Information

Estriol is **not currently marketed in Australia** — no ARTG entries were found (0 total). No product name, dosage form, or approved indication text is available from this evidence pack.

## Safety Considerations

- **Data gap:** No TFDA/TGA-sourced key warnings, contraindications, or drug-interaction data are available for Estriol in this evidence pack (flagged as a **Blocking** data gap — DG001 — meaning safety cannot yet be initially assessed).
- **Cross-candidate safety signal:** Rationale notes attached to other TxGNN-predicted indications for this same drug (e.g. breast fibrocystic disease, benign mammary dysplasia) flag that estrogens are generally regarded as a *risk factor* for breast tissue proliferation rather than a treatment — the opposite mechanistic direction. This is relevant background context when weighing any estrogenic therapy, including the amenorrhea indication above.

Please refer to the TGA-approved Product Information (PI) for definitive safety information once available; none currently exists given the drug's unmarketed status.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A blocking data gap on TFDA/TGA warnings and contraindications means safety cannot pass initial screening (S1), the drug is not marketed in Australia (0 ARTG entries), and the strongest clinical-trial evidence is compromised by a likely drug-identity mismatch (Estriol vs Estetrol). The supporting evidence base is Level L3 (observational/mechanistic), consistent with the underlying TxGNN scoring's own "Research Question" recommendation at decision stage S1.

**To proceed, the following is needed:**
- TFDA/TGA Product Information — warnings, contraindications, DDI (DG001, blocking)
- Confirmed mechanism of action from DrugBank (DG002)
- Manual verification of NCT04090957 and NCT04209543 drug identity before counting them as supporting evidence
- Original indication/regulatory history for Estriol (currently absent)
- A dedicated Estriol-specific interventional study in FHA/amenorrhea if this direction is pursued further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

