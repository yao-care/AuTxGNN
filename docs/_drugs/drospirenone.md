---
layout: default
title: Drospirenone
parent: 僅模型預測 (L5)
nav_order: 171
evidence_level: L5
indication_count: 10
---

# Drospirenone
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

# Drospirenone: From Contraception/PMDD to Zinc, Elevated Plasma

## One-Sentence Summary

Drospirenone is a fourth-generation synthetic progestin, approved internationally as a component of combined oral contraceptives (including for premenstrual dysphoric disorder/PMDD), though it is not currently registered in Australia.
The TxGNN model predicts it may be effective for **Zinc, Elevated Plasma**,
however **no clinical trials** and **no published literature** currently support this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Contraception; premenstrual dysphoric disorder (PMDD) — approved internationally, not registered in Australia |
| Predicted New Indication | Zinc, Elevated Plasma |
| TxGNN Prediction Score | 98.74% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on published literature within the pack, Drospirenone is a synthetic progestin structurally derived from spironolactone (specifically 17α-spirolactone). It possesses progestogenic, antimineralocorticoid, and antiandrogenic properties. In combined oral contraceptive formulations (e.g., paired with ethinyl estradiol), it provides contraceptive efficacy alongside benefits for fluid retention, blood pressure, and androgen-related symptoms such as acne and hirsutism.

The antimineralocorticoid activity of Drospirenone — functioning analogously to spironolactone — modulates the aldosterone pathway and influences electrolyte homeostasis, including sodium and potassium balance. Zinc is a trace element whose plasma levels can be indirectly affected by hormonal and electrolyte regulatory systems, providing a theoretical, albeit tenuous, mechanistic basis for this prediction.

In practice, the high TxGNN score (98.74%) for "Zinc, Elevated Plasma" most likely reflects indirect connectivity through electrolyte metabolism nodes within the knowledge graph, rather than a direct or clinically validated relationship. There is currently no clinical trial evidence, no supporting literature, and no established biological plausibility for Drospirenone as a treatment for elevated plasma zinc. This prediction should be treated as a knowledge graph artefact until further mechanistic investigation is undertaken.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Drospirenone is not currently listed on the Australian Register of Therapeutic Goods (ARTG) as a standalone product. There are no ARTG entries for this drug at this time. Drospirenone-containing combination products (e.g., drospirenone/ethinyl estradiol) may be available under different active ingredient listings; a separate ARTG search for combination products is recommended.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

> **Note:** No TGA-registered product PI is currently available for standalone Drospirenone in Australia. For international safety reference, consult the approved PI for drospirenone-containing combination products (e.g., Yasmin, Yaz) approved in the US (FDA), Europe (EMA), or equivalent jurisdictions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is classified as L5 — model prediction only, with no supporting clinical trials, no published literature relevant to the target indication, and no established mechanistic link between Drospirenone and elevated plasma zinc. The high TxGNN score most likely reflects indirect knowledge graph connectivity through shared electrolyte/aldosterone pathway nodes rather than genuine therapeutic relevance.

**To proceed, the following is needed:**

- Retrieve Drospirenone mechanism of action (MOA) data from DrugBank API to enable rigorous mechanistic plausibility assessment
- Obtain TGA Product Information (PI) for an equivalent international product to document key warnings, contraindications, and drug interactions
- Conduct a targeted literature review examining any biological relationship between progestins, mineralocorticoid antagonism, and zinc metabolism
- Assess whether "Zinc, Elevated Plasma" represents a clinically meaningful disease target warranting further investigation, or whether this is a knowledge graph noise signal
- Consider whether a more clinically relevant repurposing target (e.g., PMDD, PCOS, acne, hypertension) exists and warrants a separate evidence-based evaluation using Drospirenone's established pharmacological profile

---

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

