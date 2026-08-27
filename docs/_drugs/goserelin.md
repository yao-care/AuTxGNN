---
layout: default
title: Goserelin
parent: 僅模型預測 (L5)
nav_order: 319
evidence_level: L5
indication_count: 10
---

# Goserelin
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

# Goserelin: From Unspecified Original Indication to Amenorrhoea

## One-Sentence Summary

> Goserelin's original approved indication is not recorded in this Evidence Pack (data gap — `original_indications` is empty and MOA is flagged as a data gap), though the pack confirms it as a GnRH agonist.
> The TxGNN model predicts it may be effective for **Amenorrhoea** (specifically, GnRH-agonist–induced ovarian suppression for chemotherapy-related ovarian protection),
> with **7 clinical trials** and **19 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this Evidence Pack (no licences or `original_indications` on file — drug is not currently marketed) |
| Predicted New Indication | Amenorrhoea |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, a structured mechanism-of-action record is not available for Goserelin in this Evidence Pack (flagged as data gap DG002). However, the indication-specific rationale supplied with the top prediction confirms Goserelin is a **GnRH (gonadotropin-releasing hormone) agonist**: sustained use desensitises the pituitary, suppressing LH/FSH release, which in turn suppresses ovarian steroidogenesis and induces a hypo-oestrogenic, amenorrhoeic state.

This is not an incidental association — inducing amenorrhoea is a **direct pharmacological extension of Goserelin's known class effect**, not a novel or unexpected mechanism. The clinical trial and literature evidence in this pack overwhelmingly relate to using Goserelin during chemotherapy for premenopausal, hormone-sensitive breast cancer to preserve ovarian function — i.e., deliberately inducing reversible amenorrhoea to protect the ovaries from cytotoxic damage. Because this reflects the drug's core, well-established pharmacology rather than an off-target effect, the mechanistic plausibility of this prediction is very strong, even though the original approved indication itself is not documented in this pack.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00068601](https://clinicaltrials.gov/study/NCT00068601) | Phase 3 | Completed | 257 | LHRH analogue (goserelin) plus chemotherapy vs chemotherapy alone to reduce ovarian failure in early-stage, hormone-receptor-negative breast cancer |
| [NCT00427245](https://clinicaltrials.gov/study/NCT00427245) | Phase 3 | Completed | 400 | OPTION trial: goserelin vs no goserelin for preventing early menopause in premenopausal women undergoing chemotherapy for stage I–III breast cancer |
| [NCT02483767](https://clinicaltrials.gov/study/NCT02483767) | Phase 3 | Completed | 98 | Randomised trial of GnRH agonist goserelin added to chemotherapy vs chemotherapy alone for preserving ovarian function in premenopausal breast cancer |
| [NCT01218581](https://clinicaltrials.gov/study/NCT01218581) | Phase 2/3 | Completed | 32 | Aromatase inhibitor vs GnRH agonist for managing uterine adenomyosis in women wishing to preserve fertility |
| [NCT03475758](https://clinicaltrials.gov/study/NCT03475758) | Phase 2 | Unknown | 100 | Goserelin for ovarian protection during cyclophosphamide-containing chemotherapy; menstruation outcome endpoint |
| [NCT02132390](https://clinicaltrials.gov/study/NCT02132390) | Phase 3 | Unknown | 300 | Adjuvant toremifene ± goserelin in premenopausal hormone-receptor-positive breast cancer, with/without chemotherapy-induced amenorrhoea |
| [NCT00488722](https://clinicaltrials.gov/study/NCT00488722) | Not applicable | Unknown | N/A | Single-arm study of Zoladex 3.6 mg plus CEF chemotherapy as neoadjuvant therapy in hormone-responsive premenopausal breast cancer, inducing reversible amenorrhoea |

*No ANZCTR-registered trial identifiers were found in this Evidence Pack.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28472240](https://pubmed.ncbi.nlm.nih.gov/28472240/) | 2017 | RCT | Ann Oncol | OPTION trial: GnRH agonist during chemotherapy reduced risk of chemotherapy-induced premature ovarian insufficiency in early breast cancer |
| [26951320](https://pubmed.ncbi.nlm.nih.gov/26951320/) | 2016 | Cohort | J Clin Oncol | Clinical guidance discussion on whether oestradiol monitoring is necessary during goserelin-induced ovarian suppression in breast cancer |
| [25187267](https://pubmed.ncbi.nlm.nih.gov/25187267/) | 2015 | Cohort | Cancer Res Treat | Goserelin-induced ovarian ablation improved survival in stage II/III hormone-receptor-positive breast cancer patients without chemotherapy-induced amenorrhoea |
| [17159194](https://pubmed.ncbi.nlm.nih.gov/17159194/) | 2007 | RCT | J Clin Oncol | IBCSG Trial VIII: chemotherapy followed by goserelin vs either alone — effects on amenorrhoea, hot flashes, and quality of life in premenopausal patients |
| [14679153](https://pubmed.ncbi.nlm.nih.gov/14679153/) | 2003 | RCT | J Natl Cancer Inst | IBCSG Trial VIII: chemotherapy followed by goserelin vs either modality alone in premenopausal node-negative breast cancer |
| [12734855](https://pubmed.ncbi.nlm.nih.gov/12734855/) | 2003 | Review | Br J Surg | Review of ovarian ablation methods, including GnRH agonists, in adjuvant treatment of pre/perimenopausal breast cancer |
| [12488406](https://pubmed.ncbi.nlm.nih.gov/12488406/) | 2002 | RCT | J Clin Oncol | ZEBRA study: goserelin vs CMF chemotherapy as adjuvant therapy in node-positive premenopausal breast cancer |
| [12353820](https://pubmed.ncbi.nlm.nih.gov/12353820/) | 2002 | Review | Breast Cancer Res Treat | Overview of LHRH agonists in early breast cancer, highlighting benefits of reversible ovarian ablation |
| [8513962](https://pubmed.ncbi.nlm.nih.gov/8513962/) | 1993 | RCT | Fertil Steril | Goserelin vs low-dose oral contraceptive for endometriosis-related pelvic pain, demonstrating induced-amenorrhoea mechanism |
| [1533675](https://pubmed.ncbi.nlm.nih.gov/1533675/) | 1992 | Review | J R Army Med Corps | Historical review of therapeutic amenorrhoea induction, including goserelin as a highly effective GnRH-analogue method |

---

## Australia Market Information

No ARTG entries were found for Goserelin in this Evidence Pack — market status is recorded as **Not Marketed**, with 0 licences on file. No product name, dosage form, or approved indication text is available to summarise.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No key warnings, contraindications, or drug interaction data were available in this Evidence Pack (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The top-ranked prediction (amenorrhoea, as ovarian protection during chemotherapy) is backed by three completed Phase 3 RCTs and multiple supporting Phase 2/3 and observational studies, all directly testing Goserelin's core pharmacological action rather than an off-target effect — meeting Evidence Level L1. However, Goserelin is not currently marketed locally and core drug-level safety data (MOA, PI warnings/contraindications) are missing, so this should not proceed without guardrails.

**To proceed, the following is needed:**
- TGA/TFDA-equivalent Product Information (warnings, contraindications) — currently a Blocking data gap (DG001)
- Structured mechanism-of-action record for Goserelin — currently a High-severity data gap (DG002)
- Confirmation of local regulatory pathway, given the drug is not currently marketed in this jurisdiction
- Drug interaction (DDI) data, currently unavailable
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

