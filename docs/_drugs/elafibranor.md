---
layout: default
title: Elafibranor
parent: 僅模型預測 (L5)
nav_order: 180
evidence_level: L5
indication_count: 10
---

# Elafibranor
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

# Elafibranor: From Primary Biliary Cholangitis to Amenorrhea

## One-Sentence Summary

Elafibranor is a dual PPAR-α/δ agonist that has received regulatory approval in the United States (FDA-approved as IQIRVO in June 2024 for Primary Biliary Cholangitis) but is not currently registered with the TGA in Australia. The TxGNN model predicts it may have application in **Amenorrhea**, with a high computational prediction score — however, this prediction is supported by **zero clinical trials** and **zero published publications**, placing it firmly at the lowest evidence tier. At this stage, the prediction should be regarded as a computational hypothesis only, requiring substantial biological and clinical validation before any further consideration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not TGA-registered; FDA-approved (US) for Primary Biliary Cholangitis (PBC) in adults |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.86% (Prediction Rank #2,321 — note: rank is the more meaningful indicator) |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in the current Evidence Pack. However, based on published pharmacological literature, Elafibranor is a dual agonist of Peroxisome Proliferator-Activated Receptors alpha and delta (PPAR-α/δ) — nuclear receptors that play central roles in regulating fatty acid β-oxidation, lipid homeostasis, mitochondrial biogenesis, and anti-inflammatory signalling in the liver and peripheral tissues. Its approved clinical indication (PBC) reflects its capacity to modulate hepatic bile acid metabolism and reduce cholestatic inflammation, providing proof that the drug meaningfully engages metabolic-inflammatory pathways in vivo.

The proposed connection to amenorrhea rests on an indirect, multi-step mechanistic hypothesis: PPAR-α/δ activation influences fatty acid oxidation and systemic energy sensing, which may in turn affect the hypothalamic-pituitary-ovarian (HPO) axis. There is epidemiological literature suggesting that impaired lipid oxidation and negative energy balance — as seen in functional hypothalamic amenorrhea associated with athletic overtraining or severe dietary restriction — can suppress gonadotrophin-releasing hormone (GnRH) pulsatility. However, this represents a very distal biological chain, with no direct pharmacological evidence specifically linking Elafibranor to the reproductive endocrine axis at any level.

It is critical to contextualise the TxGNN score correctly. While the raw score is 99.86%, the **prediction rank of 2,321** indicates this is far from a top-priority repurposing candidate for this drug — TxGNN scores tend to cluster at high values across thousands of drug-disease pairs, making raw score alone an unreliable comparator. The rank is the operative metric. The prediction most likely reflects knowledge graph topological proximity (shared metabolic or inflammatory network nodes) rather than a direct, biologically plausible causal mechanism, and should be treated with considerable scepticism at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for Elafibranor in amenorrhea (search conducted across ClinicalTrials.gov and ICTRP on 9 March 2026).

---

## Literature Evidence

Currently no related literature is available for Elafibranor in amenorrhea (PubMed search conducted 9 March 2026).

---

## Australia Market Information

Elafibranor is not currently registered with the Therapeutic Goods Administration (TGA) and holds no ARTG entries as of April 2026.

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|-------------|--------------|-------------|---------------------|
| — | Not registered | — | No TGA registration exists |

For reference, Elafibranor is marketed in the United States as **IQIRVO** (Ipsen), approved by the FDA in June 2024 for the treatment of Primary Biliary Cholangitis (PBC) in adults. Australian clinicians or researchers seeking access would need to explore the TGA's Special Access Scheme (SAS) or Authorised Prescriber (AP) pathway. ARTG registration status should be monitored for future regulatory updates.

---

## Safety Considerations

No TGA-approved Product Information (PI) exists for Elafibranor in Australia, and no drug interaction data was identified in this Evidence Pack. Please refer to the US FDA-approved prescribing information for **IQIRVO** as an interim reference for safety, contraindications, and drug interaction data. Any Australian clinical use would need to proceed through the TGA's unapproved therapeutic goods framework, with full risk documentation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction rests entirely on a computational TxGNN model output (Evidence Level L5), with no registered clinical trials, no supporting published literature, and no direct pharmacological mechanism linking Elafibranor to amenorrhea. The prediction rank of 2,321 — combined with a biologically indirect mechanistic hypothesis spanning multiple pathway steps — does not meet the threshold for any form of clinical or translational investment at this time.

**To proceed, the following is needed:**
- Retrieval and review of the full MOA data from DrugBank (DB05187) and published PPAR-α/δ pharmacology literature
- Identification of any preclinical data (animal models or in vitro studies) examining PPAR agonist effects on GnRH pulsatility or HPO axis function
- Safety profile review from the FDA-approved IQIRVO prescribing information, covering hepatic, cardiovascular, and endocrine adverse events
- At minimum one hypothesis-generating publication (case series or observational cohort) linking PPAR-α/δ pathway modulation to menstrual cycle function before further repurposing work is warranted
- Assessment of whether a more biologically plausible predicted indication (e.g., gallbladder adenosquamous carcinoma at Rank #7, where Elafibranor's known biliary activity provides a traceable mechanistic basis) should be prioritised for deeper evaluation ahead of amenorrhea

> **Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

