---
layout: default
title: Clomifene
parent: 僅模型預測 (L5)
nav_order: 118
evidence_level: L5
indication_count: 10
---

# Clomifene
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

# Clomifene: From Anovulatory Infertility to 46,XY Disorder of Sex Development Due to Testicular Steroidogenesis Defect

---

## One-Sentence Summary

Clomifene citrate is a selective oestrogen receptor modulator (SERM) with a long-established global role in inducing ovulation in women with anovulatory infertility, most commonly polycystic ovary syndrome (PCOS). The TxGNN model's top-ranked new prediction is that it may be effective for **46,XY disorder of sex development (DSD) due to testicular steroidogenesis defect**, with **no clinical trials** and **no publications** currently identified to support this specific direction. Evidence is limited to model prediction only (L5), and the mechanistic rationale is considered weak.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anovulatory infertility / ovulation induction |
| Predicted New Indication | 46,XY disorder of sex development due to testicular steroidogenesis defect |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this Evidence Pack. Based on well-established pharmacology, clomifene acts as a selective oestrogen receptor modulator (SERM): by competitively blocking oestrogen receptors in the hypothalamus, it disrupts the normal negative feedback loop on GnRH secretion. The resulting increase in GnRH pulse frequency drives elevated FSH and LH release from the anterior pituitary — this is the basis for its use in ovulation induction, which remains its globally recognised primary indication.

The theoretical basis for repurposing clomifene in 46,XY DSD due to testicular steroidogenesis defect rests on its ability to raise serum LH. Elevated LH could, in principle, stimulate Leydig cells to produce more testosterone — a plausible-sounding hypothesis at first glance. However, this condition arises from enzyme-level failures, typically mutations in genes such as *StAR*, *CYP11A1*, or *HSD3B2*. The downstream enzymatic machinery required to convert cholesterol into androgens is intrinsically compromised, and amplifying an upstream hormonal signal does not repair a broken enzyme. This is fundamentally different from anovulatory infertility, where the target tissue (ovarian follicles) remains functionally intact and simply needs a gonadotropin stimulus.

In summary, the TxGNN model appears to have identified a superficial mechanistic bridge (clomifene → ↑LH → gonadal steroidogenesis) without accounting for the enzyme-level irreversibility of this disorder. Biological plausibility is low, and this prediction should be treated as a hypothesis-generating signal only, pending preclinical validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Clomifene is not currently listed on the Australian Register of Therapeutic Goods (ARTG). There are no TGA-approved products available in Australia, and no ARTG entries to reference. Clinicians requiring access would need to explore pathways such as the TGA Special Access Scheme (SAS) or Authorised Prescriber arrangements.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

> **Note:** No key warnings, contraindications, or drug interaction data were available in this Evidence Pack. Given clomifene is not currently ARTG-listed, prescribers should consult international product monographs (e.g., from the FDA, EMA, or UK MHRA) as a proxy until TGA-specific documentation is obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model assigns a high prediction score (99.90%), the mechanistic rationale is biologically implausible — increasing LH stimulation via hypothalamic oestrogen receptor blockade cannot correct an intrinsic enzyme deficiency in testicular steroidogenesis. There is no clinical trial or published literature evidence for this indication, clomifene is not currently marketed in Australia, and no safety data was retrievable for this evaluation.

**To proceed, the following is needed:**
- Preclinical evidence (in vitro enzyme activity assays or animal models) demonstrating any meaningful improvement in steroidogenesis in the context of *StAR*, *CYP11A1*, or *HSD3B2* deficiency
- Retrieval of full DrugBank MOA data to characterise any off-target receptor interactions that may be relevant to steroidogenesis beyond the classical hypothalamic–pituitary axis
- Assessment of whether any subpopulation within 46,XY DSD retains partial enzyme function that could theoretically benefit from elevated gonadotropin stimulation
- Full safety evaluation including acquisition of an applicable TGA-equivalent Product Information (PI) or regulatory monograph before any clinical consideration proceeds
- ARTG registration or SAS pathway assessment if the hypothesis gains preclinical support

---

> **Contextual note for clinicians:** While 46,XY DSD due to testicular steroidogenesis defect is the TxGNN model's highest-ranked novel prediction for clomifene, a review of all 10 predicted indications in this Evidence Pack reveals that **anovulation** (rank 10, TxGNN score 99.52%) carries an evidence level of **L1** with over 50 registered clinical trials and 20 publications — consistent with clomifene's well-established global clinical role. The model's high scores for ranks 1–9 (all L5/Hold) likely reflect learned associations in the knowledge graph rather than actionable repurposing candidates. Researchers should interpret TxGNN scores in conjunction with evidence levels and mechanistic plausibility assessments.

---

*This report is generated for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require prospective clinical validation before any patient application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

