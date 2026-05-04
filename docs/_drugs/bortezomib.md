---
layout: default
title: Bortezomib
parent: 僅模型預測 (L5)
nav_order: 95
evidence_level: L5
indication_count: 10
---

# Bortezomib
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

# Bortezomib: From Multiple Myeloma to Vertebral Anomalies with Endocrine and T-Cell Dysfunction

## One-Sentence Summary

Bortezomib (Velcade) is a first-in-class proteasome inhibitor globally approved for multiple myeloma and relapsed mantle cell lymphoma, though it is not currently registered in Australia.
The TxGNN model predicts it may have activity in **vertebral anomalies and variable endocrine and T-cell dysfunction**, a rare congenital developmental syndrome; however, with **0 clinical trials** and **0 publications** identified in this specific direction, support rests entirely on model inference.
This is a multi-indication Evidence Pack (candidate ID: TW-DB00188-multi) — additional predicted indications with stronger clinical evidence are summarised in the conclusion.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multiple myeloma / Mantle cell lymphoma (global approval; not registered in Australia — 0 ARTG entries) |
| Predicted New Indication | Vertebral anomalies and variable endocrine and T-cell dysfunction |
| TxGNN Prediction Score | 96.10% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this dataset. Based on well-established international pharmacology, Bortezomib is a selective and reversible inhibitor of the 26S proteasome — specifically its chymotrypsin-like β5 subunit. By blocking proteasomal degradation of key regulatory proteins, it stabilises pro-apoptotic factors (including IκBα, p53, and NOXA) and disrupts the NF-κB survival pathway. These properties underpin its globally validated efficacy in multiple myeloma and mantle cell lymphoma, confirmed across multiple Phase III trials and regulatory approvals (FDA 2003, EMA 2004).

The predicted condition — vertebral anomalies and variable endocrine and T-cell dysfunction — is a rare, heterogeneous developmental syndrome with features overlapping the VATER/CHARGE spectrum. It is characterised by structural spinal anomalies, variable endocrine dysfunction, and T-cell immune impairment. The TxGNN model's prediction likely reflects its sensitivity to the T-cell dysfunction phenotype: Bortezomib is known to modulate NF-κB signalling, which plays a regulatory role in thymic T-cell development and peripheral immune homeostasis. Proteasome inhibition could theoretically influence T-cell receptor signalling pathways that are disrupted in this syndrome.

However, this mechanistic link is highly speculative. The syndrome is principally a congenital structural and developmental disorder rather than a disease of aberrant protein homeostasis or malignant proliferation. There is no published clinical, preclinical, or biomarker evidence to support Bortezomib's therapeutic application here. This prediction should be treated as a model-generated hypothesis only, and does not constitute a clinically actionable repurposing opportunity at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Bortezomib is not registered on the Australian Register of Therapeutic Goods (ARTG) and has no approved indications in Australia. There are no current ARTG entries for any formulation.

> Internationally, Bortezomib (Velcade; Janssen-Cilag) is approved by the FDA and EMA for:
> - Newly diagnosed multiple myeloma (in combination regimens including VMP and VRd)
> - Relapsed or refractory multiple myeloma
> - Relapsed or refractory mantle cell lymphoma
>
> Australian clinicians wishing to access Bortezomib for an approved international indication may do so via the TGA Special Access Scheme (SAS Category B) or through participation in a registered clinical trial.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Proteasome inhibitor (first-generation boronic acid dipeptide; distinct mechanism from conventional cytotoxics) |
| Myelosuppression Risk | Moderate — thrombocytopenia is characteristic and cyclical (nadir typically Day 11 of a 21-day cycle, recovery by Day 21); neutropenia less pronounced than with conventional alkylating agents |
| Emetogenicity Classification | Low (consistent with MASCC/ESMO emetogenicity classification for IV proteasome inhibitors) |
| Monitoring Items | Full blood count (FBC) with differential and platelets prior to each dose; liver function tests; serum creatinine; blood glucose (endocrine effects reported); formal peripheral neuropathy assessment (e.g., NCI-CTCAE grading) at each clinic visit |
| Handling Protection | Cytotoxic drug handling precautions required throughout preparation and administration; subcutaneous (SC) injection is the preferred route in approved indications — reduces systemic peak exposure and peripheral neuropathy incidence compared with IV bolus; standard institutional cytotoxic PPE protocols apply |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. As Bortezomib is not currently registered in Australia, the FDA or EMA prescribing information (Velcade) should be consulted as the reference standard for clinical decision-making.

> **Key safety considerations from international labelling (for clinical awareness):**
> - **Peripheral neuropathy:** The primary dose-limiting toxicity; predominantly sensory, but motor neuropathy occurs; SC administration significantly reduces incidence and severity compared with IV; dose reduction or discontinuation required for Grade ≥3
> - **Thrombocytopenia:** Monitor platelet count before each dose; dose modifications apply per label; serious bleeding events reported
> - **Herpes zoster reactivation:** Antiviral prophylaxis (aciclovir 400 mg BD or valaciclovir equivalent) is strongly recommended for the duration of therapy
> - **Orthostatic hypotension:** Particularly in elderly patients; ensure adequate hydration; avoid concurrent antihypertensives where possible
> - **Posterior reversible encephalopathy syndrome (PRES):** Rare but serious; clinical vigilance required

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN model confidence score of 96.10%, there is no clinical or preclinical evidence supporting Bortezomib's use in vertebral anomalies with endocrine and T-cell dysfunction. The condition is a rare congenital developmental disorder, and the mechanistic link to proteasome inhibition is entirely speculative. Proceeding with any investigation of this prediction would require substantial foundational research before any clinical consideration could be warranted.

**To proceed, the following is needed:**
- Establish a biological rationale through in vitro studies using cell models relevant to the T-cell dysfunction or endocrine components of the syndrome
- Determine whether proteasome activity or NF-κB signalling plays a measurable and pathogenic role in the syndrome's T-cell or endocrine phenotype
- Conduct a comprehensive rare disease literature search beyond the current data cutoff (2026-04-10) for unpublished case data
- Engage a rare disease specialist or clinical geneticist to formally evaluate biological plausibility before committing any research resources
- Obtain formal MOA data from DrugBank API (Data Gap DG002) to enable more rigorous mechanistic analysis

---

> **Note for Australian clinicians — broader context from this multi-indication Evidence Pack:**
> This Evidence Pack (TW-DB00188-multi) contains 10 TxGNN-predicted indications. While the highest-scoring prediction is reported above, the following indications have substantially stronger clinical evidence and may be of greater practical relevance for repurposing consideration:
>
> | Rank | Predicted Indication | Evidence Level | Recommendation |
> |------|---------------------|---------------|----------------|
> | 4 | Neuroblastoma | L3 | Research Question |
> | 5 | Hodgkin's lymphoma | L2 | Research Question |
> | 6 | Myeloid leukaemia | L3 | Research Question |
> | 7 | Non-Hodgkin lymphoma (familial) | L2 | **Proceed with Guardrails** |
>
> Separate evidence reports for these indications are recommended for full evaluation.

---

*This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. Data cutoff: 2026-04-10.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

