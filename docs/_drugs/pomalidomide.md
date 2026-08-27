---
layout: default
title: Pomalidomide
parent: 僅模型預測 (L5)
nav_order: 542
evidence_level: L5
indication_count: 10
---

# Pomalidomide
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

# Pomalidomide: From Multiple Myeloma to Indolent Plasma Cell Myeloma

## One-Sentence Summary

Pomalidomide is a second-generation immunomodulatory drug (IMiD) whose established use internationally is relapsed/refractory multiple myeloma; this is not captured as a structured field in the supplied dataset. The TxGNN model predicts activity in **indolent plasma cell myeloma** — a subtype within the same disease spectrum — supported by **1 completed clinical trial** and **2 review publications** currently identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this dataset (`original_indications`/`original_moa` = data gap); externally known as multiple myeloma, relapsed/refractory |
| Predicted New Indication | Indolent plasma cell myeloma |
| TxGNN Prediction Score | 93.96% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Structured mechanism-of-action data is not available in this dataset (`original_moa` = data gap). Based on the supporting rationale accompanying this prediction (flagged explicitly as external pharmacological knowledge, not a local database field), pomalidomide is a cereblon (CRBN) E3 ubiquitin ligase modulator that drives degradation of IKZF1/IKZF3, giving it anti-angiogenic and immune-activating (T/NK cell) effects alongside TNF-α suppression.

Indolent plasma cell myeloma sits within the same disease spectrum as multiple myeloma — the malignancy pomalidomide is already used to treat internationally. This means the TxGNN prediction is best read as extending an established, on-target mechanism to a related disease stage/subtype, rather than proposing a genuinely novel therapeutic hypothesis. That narrows the uncertainty around biological plausibility, but it does not substitute for disease-specific trial evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02046915](https://clinicaltrials.gov/study/NCT02046915) | Phase 2 | Completed | 60 | Multicentre, single-arm study of pomalidomide + dexamethasone (with response-adapted cyclophosphamide) in relapsed/refractory myeloma; aimed to balance efficacy against the substantial risk of critical myelosuppression seen with alkylator-containing regimens. |

No ANZCTR-registered trials were identified for this indication.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22180161](https://pubmed.ncbi.nlm.nih.gov/22180161/) | 2012 | Review | American Journal of Hematology | 2012 update on multiple myeloma diagnosis, risk-stratification and management. |
| [21181954](https://pubmed.ncbi.nlm.nih.gov/21181954/) | 2011 | Review | American Journal of Hematology | 2011 update on multiple myeloma diagnosis, risk-stratification and management; notes myeloma accounts for ~10% of haematologic malignancies. |

## Australia Market Information

Pomalidomide is currently **not marketed** in this dataset's jurisdiction, with **0 ARTG-equivalent entries** on file. No product listings, dosage forms, or approved indication text are available to summarise.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted/Immunomodulatory therapy (IMiD; not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | High — the completed Phase 2 trial (NCT02046915) explicitly flags patients as being at "substantial risk of critical myelosuppression" |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Full blood count (with differential) given documented myelosuppression risk; please refer to PI for full monitoring schedule |
| Handling Protection | Please refer to the Product Information (PI) and applicable hazardous-drug handling guidance |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Key warnings, contraindications, and drug interaction data are not available in this dataset (drug interaction query returned "not found").

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A single completed Phase 2 trial (n=60) plus a mechanistically plausible extension of pomalidomide's established myeloma-spectrum activity supports cautious progression, but a blocking safety-data gap and the drug's current unmarketed status in this jurisdiction preclude a full "Go".

**To proceed, the following is needed:**
- TFDA/PI-sourced warnings and contraindications (flagged as a **blocking** gap — required before safety-stage evaluation can proceed)
- Confirmed mechanism-of-action and DrugBank categorisation (currently a data gap)
- Drug interaction data (current query status: not found)
- An Australian regulatory pathway assessment, since the drug has zero ARTG-equivalent entries at present
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

