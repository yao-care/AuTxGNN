---
layout: default
title: Glatiramer
parent: 僅模型預測 (L5)
nav_order: 312
evidence_level: L5
indication_count: 10
---

# Glatiramer
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

# Glatiramer: From Multiple Sclerosis to Hemoglobinopathy

## One-Sentence Summary

Glatiramer (as glatiramer acetate) is an immunomodulatory therapy established for relapsing-remitting multiple sclerosis. The TxGNN model predicts it may be effective for **Hemoglobinopathy**, but this direction is currently supported by **0 clinical trials** and only **1 tangentially related publication**, and the evidence pack's own mechanistic review found no plausible biological link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple Sclerosis (inferred from literature evidence in this pack; not formally recorded in regulatory data — `original_indications` is empty) |
| Predicted New Indication | Hemoglobinopathy |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for glatiramer is not available in this evidence pack (flagged as a High-severity data gap). Based on the literature evidence collected here, glatiramer acetate is an established immunomodulatory therapy for relapsing-remitting multiple sclerosis, understood to act by inducing a Th1-to-Th2 immune deviation and expanding regulatory T-cell populations.

Hemoglobinopathies (including thalassaemias and related red-cell enzyme/membrane disorders) are structural or metabolic disorders of haemoglobin synthesis or red-cell proteins, with no established immune-mediated pathophysiology that a T-cell-modulating agent like glatiramer could plausibly address.

The evidence pack's own mechanistic assessment explicitly concludes there is **no reasonable mechanistic link** between glatiramer and hemoglobinopathy. The single supporting literature reference is a case report of a patient with a *past history* of beta-thalassaemia who developed immune complications after discontinuing **natalizumab** (a different MS therapy, not glatiramer) — this is an incidental clinical detail in an unrelated case report, not evidence of a therapeutic effect. This prediction should be treated as a statistical association produced by the TxGNN knowledge-graph embedding rather than a biologically grounded hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28372806](https://pubmed.ncbi.nlm.nih.gov/28372806/) | 2017 | Case Report | Revue neurologique | Describes a 35-year-old woman with a past history of beta-thalassaemia who developed multiple immune disorders after stopping **natalizumab** (not glatiramer) for MS. Glatiramer is not the drug under study, and the beta-thalassaemia history is incidental to the case, not a treatment outcome. |

---

## Australia Market Information

Glatiramer is not currently registered on the ARTG and has no marketed products in Australia (0 ARTG entries; market status: Not Marketed).

---

## Safety Considerations

No warnings, contraindications, or drug interaction data are available for glatiramer in this evidence pack, and the drug is not currently marketed in Australia, so no TGA-approved Product Information exists locally (Blocking data gap: TFDA/TGA label warnings and contraindications). Prescribers considering this drug should consult an overseas-approved Product Information (e.g. the originator's Copaxone PI) as an interim reference until local safety data is obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction is supported only by L5 evidence (model prediction only), the evidence pack's own mechanistic review found no plausible biological rationale, and the sole literature citation concerns a different drug and is incidental to hemoglobinopathy. With no TGA-approved PI available (drug not marketed in Australia), an S1 safety assessment cannot proceed.

**To proceed, the following is needed:**
- TGA/overseas Product Information (warnings, contraindications, drug interactions) — currently a Blocking data gap
- Confirmed mechanism of action data for glatiramer — currently a High-severity data gap
- Direct preclinical or clinical evidence specifically linking glatiramer to hemoglobinopathy pathophysiology
- Given the weakness of this top-ranked candidate, consider re-reviewing predicted indication #3 (female breast carcinoma, L4 evidence, 9 literature citations) as a comparison — though note that evidence there is epidemiological cancer-risk surveillance in MS cohorts, not efficacy data, and also does not currently support a "Go" decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

