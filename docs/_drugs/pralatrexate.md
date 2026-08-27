---
layout: default
title: Pralatrexate
parent: 僅模型預測 (L5)
nav_order: 551
evidence_level: L5
indication_count: 10
---

# Pralatrexate
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

# Pralatrexate: From Antifolate Chemotherapy to Pleural Mesothelioma

## One-Sentence Summary

Pralatrexate (DrugBank DB06813) is a folate-antagonist chemotherapy agent; no approved indication is on record in this evidence pack and the drug is not currently marketed in Australia.
The TxGNN model's strongest-supported prediction points to **Pleural Mesothelioma**, backed by **1 completed Phase II trial** and **2 supporting literature reports** (preclinical and review), while nine other predicted indications — including several other mesothelioma subtypes — currently have little or no evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on record (no ARTG history; literature background notes prior investigational use in non-small cell lung cancer as an antifolate agent) |
| Predicted New Indication | Pleural Mesothelioma |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data is not available for pralatrexate in this evidence pack. Based on the literature captured, pralatrexate is a dihydrofolate reductase (DHFR) inhibitor and a 10-deazaaminopterin analogue structurally related to methotrexate (PMID 11595715, PMID 21301589). In preclinical work it showed 25–30-fold greater cytotoxic potency than methotrexate against mesothelioma cell lines.

Mesothelioma has long been recognised as an antifolate-responsive tumour — pemetrexed, another antifolate, is now standard first-line therapy for malignant pleural mesothelioma in combination with platinum agents. This class relationship is the pharmacological basis for the TxGNN prediction: a drug with a proven DHFR-inhibitor mechanism being flagged for a disease where the same drug class is already standard of care is mechanistically plausible.

Notably, TxGNN independently flagged pralatrexate for six related mesothelioma presentations (epithelioid, sarcomatoid, biphasic, peritoneal, well-differentiated papillary and lymphohistiocytoid subtypes), which reinforces this as a class-level signal rather than a single coincidental hit. However, only the general "pleural mesothelioma" and "epithelioid" entries have any literature support, and that support comes from a single 2007 Phase II trial that has not been followed up — pralatrexate's clinical development in mesothelioma appears to have been superseded once pemetrexed became the established antifolate of choice. Three other predictions in this pack (pleural adenomatoid tumor, relapsing-remitting multiple sclerosis, pericardium cancer) have no clinical, preclinical or literature support and are assessed separately as **Hold** with no further action warranted at this time.

## Clinical Trial Evidence

Currently no related clinical trials registered (the supporting Phase II study, PMID 17409804, predates mandatory trial registry indexing and appears in the literature evidence below rather than the trials registry).

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17409804](https://pubmed.ncbi.nlm.nih.gov/17409804/) | 2007 | Phase II single-arm trial | J Thorac Oncol | Phase II trial of pralatrexate (PDX) in unresectable malignant pleural mesothelioma; favorable toxicity profile primarily limited to stomatitis; significant antitumour activity shown in mesothelioma cell lines and xenografts, building on prior evidence that mesothelioma is antifolate-responsive |
| [21301589](https://pubmed.ncbi.nlm.nih.gov/21301589/) | 2010 | Review | Cancer Manag Res | Review of antifolate chemotherapy targeting folate synthesis; contextualises pralatrexate within the DHFR-inhibitor drug class alongside methotrexate |
| [11595715](https://pubmed.ncbi.nlm.nih.gov/11595715/) | 2001 | Preclinical/experimental therapeutics | Clin Cancer Res | Preclinical study showing PDX (pralatrexate) 25–30-fold more potent than methotrexate against human mesothelioma cell lines, with added activity when combined with platinum agents |

## Australia Market Information

Pralatrexate currently has no ARTG entries and is not marketed in Australia.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antifolate / DHFR inhibitor class, structurally related to methotrexate) |
| Myelosuppression Risk | Not fully characterised in this evidence pack; the available Phase II trial (PMID 17409804) describes toxicity as "favorable...primarily limited to stomatitis," but this is from a single small trial and should not be relied on for a definitive risk rating |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Full blood count, oral mucosa/stomatitis assessment, renal and hepatic function — standard for antifolate agents |
| Handling Protection | Cytotoxic drug handling precautions required |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. This evidence pack's TFDA warning/contraindication data is flagged as a **Blocking** data gap (DG001), so no independent safety assessment can be made at this stage.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The best-supported prediction (pleural mesothelioma) rests on a single non-randomised Phase II trial from 2007 with no subsequent trials, and pralatrexate's mesothelioma development appears to have been overtaken by pemetrexed, now the antifolate standard of care. The drug is not marketed in Australia, and safety/PI data required for any clinical evaluation are currently unavailable (Blocking gap DG001).

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications, drug interactions)
- ARTG registration or import-pathway confirmation, since pralatrexate is currently unmarketed in Australia
- An updated literature/trial search to check whether any mesothelioma studies have occurred since pemetrexed became standard therapy
- DrugBank-sourced original indication and mechanism-of-action documentation to complete the mechanistic assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

