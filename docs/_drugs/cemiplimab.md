---
layout: default
title: Cemiplimab
parent: 僅模型預測 (L5)
nav_order: 136
evidence_level: L5
indication_count: 10
---

# Cemiplimab
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

# Cemiplimab: From Cutaneous Squamous Cell Carcinoma to Gallbladder Adenosquamous Carcinoma

## One-Sentence Summary

Cemiplimab is an anti-PD-1 immune checkpoint inhibitor; its original indication is not captured in this evidence pack (data gap), though it is publicly known to be approved for advanced cutaneous squamous cell carcinoma and related tumours. The TxGNN model predicts it may be effective for **gallbladder adenosquamous carcinoma**, but this is currently supported only by **0 clinical trials** and **0 publications** specific to this indication — the rationale rests entirely on indirect, class-level evidence from a related checkpoint inhibitor (durvalumab) approved in biliary tract cancer.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (see note below) |
| Predicted New Indication | Gallbladder adenosquamous carcinoma |
| TxGNN Prediction Score | 99.99% (model rank 335) |
| Evidence Level | L4 (mechanism/class-level evidence only, no drug-specific trials or literature) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

**Note on Original Indication:** The evidence pack's `original_indications` and `original_moa` fields are both empty/data-gap. Based on published, publicly available information (not sourced from this pack), cemiplimab (REGN2810, Libtayo) is an anti-PD-1 monoclonal antibody first approved for locally advanced or metastatic cutaneous squamous cell carcinoma, with subsequent approvals in basal cell carcinoma and non-small cell lung cancer. This background is provided for clinical context only and should be verified against the TGA-approved Product Information before use in any assessment.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for cemiplimab is not available in this evidence pack. Based on known pharmacological class information, cemiplimab is an anti-PD-1 immune checkpoint inhibitor that restores T-cell-mediated antitumour activity by blocking PD-1/PD-L1-mediated immune evasion. This mechanism is not tumour-specific and has demonstrated activity across multiple malignancies with sufficient immunogenicity or PD-L1 expression.

The predicted indication, gallbladder adenosquamous carcinoma, falls within the broader biliary tract cancer category. The rationale supplied in this pack notes that durvalumab (an anti-PD-L1 antibody) plus chemotherapy is already approved for biliary tract cancer — including gallbladder cancer — based on the TOPAZ-1 trial, demonstrating that this tumour group can respond to checkpoint blockade. This constitutes indirect, drug-class-level evidence rather than direct evidence for cemiplimab itself.

Adenosquamous carcinoma is a mixed histological subtype (glandular and squamous components), and no cemiplimab-specific trial or publication addresses this tumour or this histology. The prediction should therefore be read as a mechanistically plausible research hypothesis rather than a clinically validated finding.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Cemiplimab has no ARTG entries and is not currently marketed in Australia (`market_status: Not marketed`, `total_licenses: 0`). No product, dosage form, or approved-indication data is available from this evidence pack.

---

## Cytotoxicity

Cemiplimab is an antineoplastic agent (anti-PD-1 immune checkpoint inhibitor), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (immune checkpoint inhibitor, not a conventional cytotoxic agent) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions — no toxicity data available in this evidence pack; checkpoint inhibitors as a class typically carry low direct myelosuppressive risk but notable immune-related adverse event risk (e.g., colitis, pneumonitis, endocrinopathies, hepatitis) |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Thyroid function, liver and renal function, FBC, and clinical monitoring for immune-related adverse events |
| Handling Protection | Standard precautions for parenteral monoclonal antibody administration; classic cytotoxic drug handling regulations (as applied to conventional chemotherapy) are not typically required for this drug class, but institutional biologic-handling protocols should be followed |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate indication is supported only by indirect, class-level mechanistic reasoning (L4) — there are no cemiplimab-specific trials or publications for gallbladder adenosquamous carcinoma, and the drug is not currently registered or marketed in Australia. A blocking data gap on TFDA/TGA product information also prevents a preliminary safety assessment.

**To proceed, the following is needed:**
- TGA-approved Product Information / warnings and contraindications (resolves blocking data gap)
- Confirmed mechanism of action documentation for cemiplimab (currently a data gap)
- Preclinical or translational data on PD-L1 expression/immunogenicity in gallbladder adenosquamous carcinoma specifically
- Any emerging case reports, basket trials, or biliary tract cancer trial subgroup data including cemiplimab
- If prioritising a candidate from this same evidence pack with stronger support, note that **external ear basal cell carcinoma** (rank 4, evidence level L3, one case report, decision stage S2 "Proceed with Guardrails") currently has the most direct supporting evidence among the 10 indications predicted for this drug.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

