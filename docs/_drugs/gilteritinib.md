---
layout: default
title: Gilteritinib
parent: 僅模型預測 (L5)
nav_order: 311
evidence_level: L5
indication_count: 10
---

# Gilteritinib
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

# Gilteritinib: From FLT3-mutated AML (not documented in this Evidence Pack) to Myelodysplastic/Myeloproliferative Disease

## One-Sentence Summary

Gilteritinib is an oral FLT3/AXL kinase inhibitor publicly known for treating relapsed/refractory FLT3-mutated acute myeloid leukaemia (AML) — though this original indication is not documented in the supplied Evidence Pack (a data gap). Of **10 TxGNN-predicted indications** reviewed for this drug, only **Myelodysplastic/Myeloproliferative Disease (MDS/MPN)** has any supporting clinical trial or literature evidence; the model's single highest-scoring prediction (bulbar polio) and most of the others are explicitly flagged in this Evidence Pack's own rationale as biologically implausible and are not carried forward in this report. Supporting evidence for MDS/MPN remains early-stage: **1 directly relevant, not-yet-completed Phase 1/2 trial** and **1 case report**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this Evidence Pack (`original_indications` is empty; publicly known to be relapsed/refractory FLT3-mutated AML, but this is not sourced from the supplied data) |
| Predicted New Indication | Myelodysplastic/Myeloproliferative Disease (MDS/MPN) |
| TxGNN Prediction Score | 97.0% (0.9700) |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (data gap DG002). Based on publicly known information, gilteritinib is a small-molecule inhibitor of FLT3 (including ITD and TKD mutations) and AXL, approved for relapsed/refractory FLT3-mutated AML — though this original-indication detail is likewise not sourced from the supplied data.

MDS/MPN overlap neoplasms arise from the same haematopoietic stem-cell lineage as AML, and a subset of MDS/MPN cases carry activating FLT3 mutations. This provides a plausible mechanistic rationale for extending FLT3-targeted therapy to FLT3-mutated MDS/MPN, even though MDS/MPN is not among gilteritinib's core approved AML subtypes.

By contrast, the other nine TxGNN-predicted indications in this Evidence Pack — including the model's own top-ranked prediction, bulbar polio, as well as unrelated congenital syndromes and neurogenic tumours — show no plausible mechanistic connection to FLT3/AXL inhibition. The Evidence Pack's own rationale explicitly describes these as likely knowledge-graph noise or spurious node co-occurrence, with zero supporting trials or literature for any of them. They are not discussed further in this report.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04140487](https://clinicaltrials.gov/study/NCT04140487) | Phase 1/2 | Recruiting | 97 | Gilteritinib + azacitidine + venetoclax in FLT3-mutated relapsed/refractory AML, CMML or high-risk MDS/MPN — the only trial directly testing gilteritinib for this indication; not yet completed |
| [NCT05564390](https://clinicaltrials.gov/study/NCT05564390) | Phase 2 | Recruiting | 2000 | NCI MyeloMATCH master screening/reassessment protocol for AML/MDS; a biomarker-driven intake platform feeding patients into sub-studies, not a gilteritinib-specific trial |
| [NCT03922100](https://clinicaltrials.gov/study/NCT03922100) | Phase 1/2 | Terminated | 63 | Tests NMS-03592088, a different FLT3/KIT/CSF1R inhibitor, in relapsed/refractory AML/CMML — same-class mechanistic support only, not gilteritinib itself |
| [NCT02115295](https://clinicaltrials.gov/study/NCT02115295) | Phase 2 | Recruiting | 508 | Cladribine + idarubicin + cytarabine (± venetoclax) in AML/high-risk MDS/CML blast phase — no gilteritinib arm; population overlap only |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33792628](https://pubmed.ncbi.nlm.nih.gov/33792628/) | 2021 | Case Report | Blood Advances | Infant with ETV6-FLT3 fusion-driven myeloid/lymphoid neoplasm with eosinophilia (a JMML-mimicking entity); ex vivo studies showed increased sensitivity to type I FLT3 inhibitors, supporting mechanistic plausibility of FLT3-targeted therapy in FLT3-fusion/mutation-driven myeloid neoplasms beyond classic AML |

---

## Australia Market Information

Gilteritinib is not currently marketed in Australia — the Evidence Pack records 0 ARTG entries.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (FLT3/AXL tyrosine kinase inhibitor) — based on known pharmacological class; not sourced from this Evidence Pack, as the MOA field is a data gap (DG002) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the Product Information (PI) warnings and precautions |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. This Evidence Pack has a **Blocking** data gap (DG001): TFDA/TGA-equivalent warnings and contraindications could not be sourced, and no drug interaction data was found (`ddi.query_status: not_found`).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A Blocking data gap (DG001) means no product warnings, contraindications, or interaction data are available, so this candidate cannot yet enter a safety pre-assessment. Gilteritinib is also not marketed in Australia (0 ARTG entries), and the only mechanistically credible new indication — MDS/MPN — is supported solely by one not-yet-completed Phase 1/2 combination trial and a single case report.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications, drug interactions) to resolve DG001
- A verified mechanism-of-action source to resolve DG002
- Mature (completed) results from NCT04140487 (gilteritinib + azacitidine + venetoclax)
- Confirmation of an import/access pathway for Australian patients given current non-marketed status
- No further action on the other nine TxGNN-ranked candidates for this drug — none have mechanistic or evidentiary support and none should be pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

