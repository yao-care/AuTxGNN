---
layout: default
title: Etonogestrel
parent: 僅模型預測 (L5)
nav_order: 206
evidence_level: L5
indication_count: 10
---

# Etonogestrel
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

# Etonogestrel: From Contraception to Amenorrhea

## One-Sentence Summary

Etonogestrel is a potent synthetic progestogen — the active component in long-acting hormonal contraceptive implants (Implanon NXT / Nexplanon) — used globally for highly effective reversible contraception.
The TxGNN model predicts it may be clinically applicable for the management of **Amenorrhea**,
with **1 completed Phase 3 clinical trial** and **1 directly relevant RCT publication** providing supporting evidence.

> **Clinical Framing Note**: The predicted "amenorrhea" relationship should be interpreted as *therapeutically induced amenorrhoea* (a known pharmacodynamic outcome in conditions such as endometriosis and heavy menstrual bleeding), not the treatment of pathological amenorrhoea. These are clinically opposite therapeutic objectives.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Contraception (long-acting reversible contraceptive implant) |
| Predicted New Indication | Amenorrhea (Disease) |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L3 |
| Australia Market Status | Not Marketed (0 ARTG entries returned — see note below) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

> **⚠️ Data Verification Required**: The ARTG query returned 0 entries for Etonogestrel. This likely reflects a data gap rather than true non-registration — Etonogestrel-containing implants (e.g., Implanon NXT) are known TGA-listed products. Clinicians should verify the current ARTG status directly at [search.tga.gov.au](https://www.tga.gov.au/resources/artg) before relying on this field.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this Evidence Pack. Based on established clinical pharmacology, Etonogestrel is a third-generation synthetic progestogen and the active metabolite of desogestrel. It exerts potent progestogenic effects by suppressing the hypothalamic-pituitary-ovarian (HPO) axis — specifically inhibiting the mid-cycle LH surge — which prevents follicular maturation and ovulation. This sustained progestogenic environment is the core pharmacodynamic basis of its contraceptive efficacy and underpins the TxGNN prediction.

The mechanistic link to amenorrhoea is direct and well-characterised. HPO axis suppression by Etonogestrel leads to anovulatory amenorrhoea as a known pharmacodynamic consequence, not a toxic side effect. Clinical data from implant trials consistently document amenorrhoea incidence of 22–30% among users over a 90-day reference period. In conditions where *induced* amenorrhoea represents a therapeutic goal — such as endometriosis, adenomyosis, or chronic heavy menstrual bleeding — this progestogenic mechanism is highly applicable and clinically meaningful.

This distinction is critical for clinical interpretation: the TxGNN model is identifying a *causative* relationship between Etonogestrel and amenorrhoea states, which translates to therapeutic utility in women where menstrual suppression is desired. This must be carefully distinguished from any notion of treating women who already have pathological amenorrhoea (e.g., hypothalamic or ovarian failure), where Etonogestrel would be contraindicated.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT04626596](https://clinicaltrials.gov/study/NCT04626596) | Phase 3 | Completed | 498 | Extended-use ENG implant (years 4–5 post-insertion) in women ≤35 years: primary endpoint is contraceptive efficacy; amenorrhoea documented as a secondary outcome and known consequence of sustained HPO suppression. Confirms that ENG implant maintains anovulatory/amenorrhoeic effect beyond the currently approved 3-year duration. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [10549446](https://pubmed.ncbi.nlm.nih.gov/10549446/) | 1999 | RCT | *Contraception* | Multicentre RCT in China comparing single-rod Implanon (ENG) vs six-capsule Norplant over up to 4 years (n=200 women; 341.6 and 329.1 woman-years respectively). Zero pregnancies in both arms. Amenorrhoea and bleeding pattern data collected per 90-day reference period — foundational comparative dataset for ENG implant-induced cycle suppression and tolerability. |

> **Note**: PMID 33430924 (BIO101 in COVID-19 pneumonia) was retrieved by the automated evidence pipeline but is not relevant to amenorrhoea or Etonogestrel pharmacology. It has been excluded from this table.

---

## Australia Market Information

No ARTG entries were returned for Etonogestrel in the current Evidence Pack query (data cutoff: 5 April 2026).

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|------------|-------------|-------------|---------------------|
| — | No entries found | — | — |

> **Action Required**: This result is inconsistent with known TGA registration history. Etonogestrel-containing products (Implanon NXT, subdermal implant) are expected to hold current ARTG registration for contraceptive use. Before progressing to any regulatory pathway for new indications, the actual ARTG number(s), approved indication text, and current market status must be confirmed directly from the TGA ARTG public summary.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for Implanon NXT for complete safety information. No formal safety data (warnings, contraindications, or drug interactions) was available in this Evidence Pack.

As a class-level reminder for prescribers, progestogen-only implants carry the following well-known clinical considerations that should be reviewed in the current TGA PI:
- **Thromboembolism**: Lower risk than combined hormonal contraceptives, but history of VTE warrants caution
- **Irregular bleeding**: Most common reason for early removal; relevant when counselling patients on induced amenorrhoea
- **Bone mineral density**: Monitor with prolonged use, particularly in adolescents
- **Drug interactions**: CYP3A4 inducers (e.g., rifampicin, certain anticonvulsants) may reduce efficacy

---

## Additional Predicted Indications — Summary

The TxGNN model identified 10 predicted indications for Etonogestrel in this multi-candidate analysis. An overview of all predictions is provided below for completeness.

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|------------|----------------|---------------|
| 1 | Amenorrhea (disease) | 99.84% | L3 | Proceed with Guardrails |
| 2 | Breast fibrocystic disease | 99.61% | L5 | Hold |
| 3 | Apocrine adenosis of breast | 99.29% | L5 | Hold |
| 4 | Blunt duct adenosis of breast | 99.29% | L5 | Hold |
| 5 | Benign mammary dysplasia | 99.21% | L5 | Hold |
| 6 | Breast abscess | 98.99% | L5 | Hold |
| 7 | Fat necrosis of breast | 98.99% | L5 | Hold |
| **8** | **Lactation disease** | **98.93%** | **L2** | **Proceed with Guardrails** |
| 9 | Breast adenosis | 98.86% | L5 | Hold |
| 10 | Acne (disease) | 98.69% | L4 | Hold ⚠️ |

---

### Notable Secondary Finding: Lactation Disease (Rank 8, L2 Evidence)

Rank 8 (Lactation Disease) carries the second-strongest evidence level (L2), supported by 2 completed Phase 4 clinical trials directly examining the effect of Etonogestrel implant timing on breastfeeding outcomes, plus a systematic review and an ACOG clinical practice guideline. This may represent a more immediately actionable repurposing pathway than the top-ranked amenorrhoea prediction.

**Clinical Context**: The therapeutic "repurposing" angle here concerns optimising postpartum contraceptive management while minimising interference with lactation establishment — specifically, determining whether immediate vs. delayed postpartum implant insertion affects breastfeeding initiation and continuation. This is a defined unmet clinical need in opioid-dependent postpartum women and the broader postpartum population.

#### Clinical Trials — Lactation Disease

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT02657148](https://clinicaltrials.gov/study/NCT02657148) | N/A (Phase IV) | Completed | 200 | Prospective observational study: immediate postpartum Nexplanon placement vs standard care in opioid-dependent women. Evaluates consistent contraceptive use, rapid repeat pregnancy rates, and breastfeeding outcomes at 12 months postpartum. |
| [NCT03978598](https://clinicaltrials.gov/study/NCT03978598) | Phase 4 | Completed | 150 | RCT: ENG implant placed within 24 hours of birth vs at 4–6 weeks postpartum. Primary outcome is breastfeeding status at 8 weeks — highest-quality design for evaluating ENG impact on lactation establishment. |

#### Literature Evidence — Lactation Disease

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [26410174](https://pubmed.ncbi.nlm.nih.gov/26410174/) | 2016 | Systematic Review | *Contraception* | Systematic review of progestogen-only contraceptives (POCs) in breastfeeding women; examines evidence on breastfeeding performance and infant health outcomes, providing the highest-level synthesis of evidence in this area. |
| [21691183](https://pubmed.ncbi.nlm.nih.gov/21691183/) | 2011 | Clinical Practice Guideline | *Obstetrics and Gynecology* | ACOG Practice Bulletin No. 121: Long-acting reversible contraception — includes guidance on timing of postpartum implant insertion in breastfeeding women, serving as a key reference for clinical practice in this setting. |

> Note: PMID 33430924 (COVID-19 study) is not relevant to lactation disease and has been excluded.

---

### ⚠️ Acne (Rank 10) — Reverse Direction Warning

The existing literature for acne (PMIDs 11861056, 17763263) documents Etonogestrel as a **cause** of acne, attributed to its weak androgenic activity (low SHBG-binding affinity, partial androgen receptor agonism leading to increased sebaceous gland activity). The TxGNN high score for this indication likely reflects a co-morbidity or adverse-effect association in the knowledge graph, not a therapeutic relationship. **This predicted indication should not be pursued for drug repurposing.**

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(Primary recommendation for Amenorrhea — Rank 1)*

**Rationale:**
The pharmacological rationale for Etonogestrel-induced amenorrhoea is mechanistically sound and clinically well-recognised, supported by consistent data from contraceptive trials (L3 evidence). However, current evidence derives from trials where amenorrhoea is a secondary outcome rather than the primary therapeutic objective. A clearly defined target population and indication scope are needed before this represents a formal repurposing pathway.

**To proceed, the following is needed:**

- **ARTG verification**: Confirm TGA registration status, current approved indication text, and ARTG number(s) for Implanon NXT before any regulatory strategy is developed
- **TGA Product Information review**: Obtain current TGA-approved PI to complete the safety and contraindication profile (currently a data gap)
- **Indication scoping**: Define the specific clinical target (e.g., endometriosis-associated menstrual suppression, heavy menstrual bleeding) where induced amenorrhoea is the intended therapeutic endpoint — this will determine whether a new indication or label extension pathway applies
- **Mechanistic documentation**: Retrieve full MOA data from DrugBank (DB00294) to support regulatory and clinical dossier
- **Dedicated clinical trial design**: Current amenorrhoea data is all derived from contraceptive trials; a purpose-designed trial with induced amenorrhoea as the primary endpoint in the target indication is required for any TGA submission
- **Lactation Disease pathway evaluation**: Separately assess Rank 8 (Lactation Disease, L2 evidence, 2 completed Phase 4 RCTs) as a potentially more direct and evidence-ready repurposing opportunity

---

*This report is generated for research reference purposes only and does not constitute medical advice. All predicted repurposing candidates require clinical validation before therapeutic application. Data cutoff: 5 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

