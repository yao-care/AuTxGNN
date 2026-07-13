---
layout: default
title: Carbimazole
parent: 僅模型預測 (L5)
nav_order: 124
evidence_level: L5
indication_count: 10
---

# Carbimazole
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

# Carbimazole: From Hyperthyroidism to Resistance to Thyroid Hormone Receptor Beta

## One-Sentence Summary

Carbimazole is an established thionamide antithyroid drug used for managing hyperthyroidism and Graves' disease, acting by inhibiting thyroid peroxidase (TPO) to suppress thyroid hormone synthesis — though it is not currently registered on the Australian Register of Therapeutic Goods (ARTG).
The TxGNN model ranks **resistance to thyroid hormone due to a THRB mutation (RTH-β)** as its highest predicted new indication (score 99.71%), yet this is supported by only **1 case report**, and mechanistic analysis raises serious concerns about potential harm in this setting.
Across all 10 indications evaluated in this evidence pack, **neonatal thyrotoxicosis** (L3) and **autoimmune thyroid disease** (L2) emerge as more evidence-supported and clinically actionable repurposing candidates.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hyperthyroidism / Graves' disease (established antithyroid use; no Australian ARTG registration) |
| Predicted New Indication (Rank 1) | Resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta (RTH-β) |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, carbimazole is a prodrug that is rapidly converted in vivo to methimazole (its active metabolite). Methimazole inhibits thyroid peroxidase (TPO), blocking the organification of iodine and the coupling of iodotyrosine residues on thyroglobulin, thereby reducing the synthesis of both thyroxine (T4) and triiodothyronine (T3). Beyond this antithyroid effect, carbimazole also exerts immunomodulatory actions — including downregulation of TSH receptor antibodies (TRAb) and thyroid microsomal antibodies (TPOAb), and modulation of CD4+ T-cell responses — an effect that appears to be partially independent of thyroid hormone control.

Resistance to thyroid hormone receptor beta (RTH-β) is caused by heterozygous loss-of-function mutations in the *THRB* gene. Because pituitary thyrotrophs retain (or even heighten) sensitivity to TRβ-mediated negative feedback, they compensate by elevating TSH secretion, which in turn drives excessive thyroid hormone production. The result is the paradoxical biochemical signature of elevated free T4 alongside non-suppressed TSH — a pattern that can be mistaken for primary hyperthyroidism. TxGNN likely identified this biochemical and nodal overlap between RTH-β and hyperthyroidism as the basis for its prediction.

However, the mechanistic link breaks down critically in clinical practice. Peripheral tissues in RTH-β patients are resistant to thyroid hormone and *require* supraphysiological T4/T3 concentrations simply to maintain normal metabolic function. Suppressing thyroid hormone synthesis with carbimazole would worsen peripheral tissue hypothyroidism while doing nothing to correct the underlying receptor defect. The single relevant publication in this pack (PMID 24165508) documents exactly this clinical pitfall — a patient misdiagnosed as hyperthyroid and treated intermittently with carbimazole for a decade, with the drug providing no benefit and likely causing harm. **RTH-β should be treated as a potential contraindication for carbimazole, not a new indication.**

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [24165508](https://pubmed.ncbi.nlm.nih.gov/24165508/) | 2013 | Case Report | BMJ Case Reports | Young man with persistently elevated fT4 (25–35.7 pmol/L) and non-suppressed TSH (6.78–22.1 mIU/L) treated with carbimazole for 10 years under a misdiagnosis of hyperthyroidism; ultimately confirmed as RTH-β — highlights carbimazole as both ineffective and potentially harmful in this condition |

---

## Australia Market Information

Carbimazole is **not registered** on the Australian Register of Therapeutic Goods (ARTG). No TGA-approved Product Information is currently available for this drug. If carbimazole is required clinically (e.g., for neonatal thyrotoxicosis), prescribers should consult the TGA Special Access Scheme (SAS) and refer to international prescribing information — such as the UK BNF or New Zealand Medsafe PI — for dosing and safety guidance.

---

## Safety Considerations

Please refer to international prescribing information for full safety details, as carbimazole has no TGA-approved Product Information in Australia.

---

## Conclusion and Next Steps

**Decision: Hold** (for RTH-β as a new indication)

**Rationale:**
- RTH-β is a differential diagnosis that mimics hyperthyroidism biochemically; carbimazole addresses neither the receptor defect nor the underlying pathophysiology, and is likely to cause peripheral hypothyroidism — making it a potential contraindication rather than a candidate for repurposing in this condition.

**To proceed, the following is needed:**

This evidence pack evaluated 10 predicted indications for carbimazole. While the top TxGNN-ranked prediction (RTH-β) warrants no further clinical development, two other indications carry materially stronger evidence and actionable recommendations:

| Indication | Evidence Level | Recommendation |
|-----------|---------------|----------------|
| Autoimmune thyroid disease (Graves' disease) | L2 | Proceed with Guardrails |
| Neonatal thyrotoxicosis | L3 | Proceed with Guardrails |
| Hashimoto thyroiditis | L3 | Research Question |
| Hyperthyroxinemia | L4 | Research Question |
| Prinzmetal angina | L5 | Hold |
| Raynaud disease | L5 | Hold |
| Migraine with brainstem aura | L5 | Hold |
| Kyphoscoliotic heart disease | L5 | Hold |
| Migraine disorder | L5 | Hold |

For the two **Proceed with Guardrails** indications, the following steps are recommended:

- **TGA regulatory pathway**: Carbimazole is not ARTG-listed; a Special Access Scheme (SAS) Category B or TGA registration application would be required before formal clinical use in Australia
- **Safety data gap remediation**: Obtain warnings, contraindications, and DDI profile from the UK/NZ/EU Product Information to complete the S1 safety pre-assessment (currently blocking)
- **Neonatal thyrotoxicosis**: Engage paediatric endocrinology and neonatology expertise to establish weight-based dosing protocols; given ethical constraints on conducting RCTs in neonates, evidence from case series and observational data must be systematically synthesised
- **Autoimmune thyroid disease**: Commission a formal systematic review of carbimazole's immunomodulatory effects (particularly PMID 6247656 and related controlled studies) to determine whether evidence is sufficient to escalate from L2 toward L1
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

