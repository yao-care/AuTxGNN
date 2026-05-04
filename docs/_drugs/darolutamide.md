---
layout: default
title: Darolutamide
parent: 僅模型預測 (L5)
nav_order: 140
evidence_level: L5
indication_count: 10
---

# Darolutamide
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

# Darolutamide: From Non-Metastatic Castration-Resistant Prostate Cancer to Homozygous Familial Hypercholesterolaemia

## One-Sentence Summary

Darolutamide (Nubeqa) is an androgen receptor (AR) antagonist approved internationally for non-metastatic castration-resistant prostate cancer (nmCRPC), though it does not appear in the Australian ARTG database based on available data. The TxGNN model assigns a high algorithmic confidence score to **Homozygous Familial Hypercholesterolaemia (HoFH)** as its top predicted new indication, however this is supported by **no clinical trials** and **no published literature**, and faces significant biological plausibility challenges specific to HoFH genetics.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Non-metastatic castration-resistant prostate cancer (nmCRPC) — based on international regulatory approvals; original indication data unavailable in this Evidence Pack |
| Predicted New Indication | Homozygous Familial Hypercholesterolaemia |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on publicly available information, Darolutamide is a competitive androgen receptor (AR) antagonist that blocks androgens — testosterone and dihydrotestosterone — from binding to the AR. This prevents AR nuclear translocation and suppresses downstream transcriptional activity that drives prostate tumour growth in the castration-resistant setting.

The theoretical pathway linking AR antagonism to homozygous familial hypercholesterolaemia (HoFH) rests on observations that androgen/AR signalling can modulate hepatic low-density lipoprotein receptor (LDLR) expression. If AR antagonism were to upregulate LDLR gene transcription, this could theoretically enhance LDL-cholesterol clearance from the circulation — a mechanistically plausible cholesterol-lowering pathway in settings where the LDLR gene retains at least partial function.

However, this hypothesis breaks down specifically in HoFH. Unlike heterozygous FH or polygenic hypercholesterolaemia, HoFH is defined by **biallelic loss-of-function mutations in the LDLR gene** — both copies are non-functional or severely truncated. Even if AR antagonism were to successfully upregulate LDLR gene transcription, the resulting protein would remain non-functional or absent at the cell surface. AR antagonism cannot rescue a structurally defective receptor. There is no clinical trial or published literature to support this direction for Darolutamide, and the prediction is most likely a false positive arising from knowledge graph topology rather than a genuine therapeutic opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Darolutamide in homozygous familial hypercholesterolaemia.

---

## Literature Evidence

Currently no related literature available for Darolutamide in homozygous familial hypercholesterolaemia.

---

## Australia Market Information

Darolutamide is not currently listed on the Australian Register of Therapeutic Goods (ARTG) based on the data available to this system. There are no ARTG entries for this drug.

Clinicians wishing to prescribe Darolutamide in Australia for any indication would need to apply through the TGA's **Special Access Scheme (SAS Category B or C)** or seek **Authorised Prescriber** status. Australian prescribers should verify the current TGA registration status directly via the [TGA website](https://www.tga.gov.au).

> **Note:** Darolutamide (Nubeqa®, Bayer) has received regulatory approval from the US FDA (July 2019), European EMA, and multiple other jurisdictions for nmCRPC treatment.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — androgen receptor (AR) antagonist; **not** a conventional cytotoxic agent |
| Myelosuppression Risk | Low — bone marrow suppression is not a primary toxicity of AR antagonists |
| Emetogenicity Classification | Minimal to low |
| Monitoring Items | Liver function tests (LFTs), cardiovascular status, blood pressure, fatigue/asthenia; vigilance for thromboembolic events (DVT/PE) |
| Handling Protection | Standard oral solid dosage form handling applies; dedicated cytotoxic handling precautions (biological safety cabinet, chemotherapy gowning) are not required under standard protocols |

---

## Safety Considerations

TGA-approved Product Information and formal safety data are not available in this Evidence Pack. Please refer to the TGA-approved Product Information (PI) or the international Summary of Product Characteristics (SmPC) for complete safety information.

> **Important signal for clinicians:** Based on international prescribing information, Darolutamide is associated with an **increased risk of venous thromboembolism**, including deep vein thrombosis (DVT) and pulmonary embolism (PE). This is particularly relevant because the TxGNN model also predicts Darolutamide as a candidate for "thrombotic disease" (rank 8 in this Evidence Pack). This signal represents a **known adverse effect**, not a therapeutic opportunity, and clinicians should be cautious not to misinterpret it as such.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite the TxGNN model assigning a high algorithmic prediction score (99.11%), repurposing Darolutamide for homozygous familial hypercholesterolaemia lacks both biological plausibility and empirical support. The biallelic LDLR loss-of-function that defines HoFH cannot be meaningfully addressed by AR antagonism-mediated upregulation of a structurally non-functional receptor protein. Importantly, across all 10 top-ranked TxGNN predictions for Darolutamide in this Evidence Pack, every candidate is rated **Hold** or **Research Question** at evidence level L5 or L4 — indicating that the model is currently generating predictions outside Darolutamide's established biological domain. Several predictions refer to veterinary or non-human diseases (infectious bovine rhinotracheitis, feline acquired immunodeficiency syndrome, malignant catarrh, simian immunodeficiency virus), which further reduces confidence in the overall prediction set.

**To proceed, the following is needed:**

- Obtain full mechanism of action (MOA) data from DrugBank API or primary pharmacology literature
- Obtain TGA-approved (or international) Product Information to complete safety and contraindication assessment
- Commission preclinical work to determine whether AR antagonism produces any measurable cholesterol-lowering effect in LDLR-null or LDLR-deficient cell or animal models, before advancing this hypothesis
- Conduct independent scientific review of all 10 predicted indications to identify whether any candidate has a sufficiently plausible and testable biological rationale — **HIV infectious disease (rank 3)** may warrant a focused exploratory review given preliminary literature linking AR signalling to HIV latent reservoir dynamics
- Verify current Darolutamide ARTG registration status directly with TGA, as the drug holds international approvals and local registration may have occurred after this data cutoff
- If progressing to any clinical exploration, ensure a comprehensive thromboembolic risk management plan is in place given Darolutamide's known DVT/PE risk profile

---

*This report is generated for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require rigorous clinical validation before any therapeutic application. Please refer to the TGA-approved Product Information for prescribing guidance.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

