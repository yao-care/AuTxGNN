---
layout: default
title: Cortisone
parent: 僅模型預測 (L5)
nav_order: 130
evidence_level: L5
indication_count: 10
---

# Cortisone
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

# Cortisone: From Adrenal Insufficiency to Primary Cutaneous T-Cell Lymphoma

## One-Sentence Summary

Cortisone is a naturally occurring glucocorticoid hormone, historically the first steroid used in clinical medicine, most closely associated with adrenal insufficiency and inflammatory disease management.
The TxGNN model predicts it may be effective for **Primary Cutaneous T-Cell Lymphoma (CTCL)**,
with **1 clinical trial** (indirectly related, currently suspended) and **no published literature** directly supporting this indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Australia — no TGA-approved indication available |
| Predicted New Indication | Primary Cutaneous T-Cell Lymphoma |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this evidence pack. Based on known pharmacological information, cortisone is an endogenous glucocorticoid that is metabolically converted to active cortisol (the biologically active form) primarily in the liver via 11β-hydroxysteroid dehydrogenase type 1. Cortisol, in turn, binds to intracellular glucocorticoid receptors in lymphoid cells, triggering apoptotic pathways — providing a theoretical basis for activity against T-cell malignancies.

Primary cutaneous T-cell lymphoma is a heterogeneous group of non-Hodgkin lymphomas arising from skin-homing T lymphocytes. The mechanistic rationale for the TxGNN prediction centres on this glucocorticoid-receptor–mediated lympholytic effect. This is supported by a well-established class effect: prednisone is a standard component of CHOP and EPOCH chemotherapy regimens used for systemic T-cell lymphomas, demonstrating that glucocorticoids contribute meaningfully to lymphoma cytotoxicity.

However, it is important to note that for primary CTCL specifically, systemic glucocorticoid therapy is not standard practice. Topical corticosteroids are commonly used for localised disease, while systemic options for advanced CTCL include skin-directed therapies, retinoids, histone deacetylase inhibitors, and targeted biologics. Cortisone's indirect mechanism (requiring hepatic conversion to cortisol) and its lack of any direct CTCL clinical data mean this prediction remains theoretical at this stage.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT04799275](https://clinicaltrials.gov/study/NCT04799275) | Phase 2/3 | Suspended | 422 | R-MiniCHOP ± oral azacitidine (CC-486) in patients aged ≥75 years with newly diagnosed diffuse large B-cell lymphoma and related high-grade B-cell lymphomas. MiniCHOP contains prednisone, not cortisone. Trial is currently suspended, substantially reducing evidence value. No CTCL patients included. |

---

## Literature Evidence

Currently no related literature available for cortisone specifically in primary cutaneous T-cell lymphoma.

---

## Australia Market Information

Cortisone is currently **not registered** on the Australian Register of Therapeutic Goods (ARTG). There are no TGA-approved products listing cortisone as a primary active ingredient, and the drug has no approved indications in Australia.

---

## Safety Considerations

As cortisone holds no TGA registration in Australia, no local Product Information (PI) is available. Please refer to standard glucocorticoid prescribing references and international PI documents for safety information. Key considerations known from the glucocorticoid class include:

- **Immunosuppression risk**: All evidence in the candidiasis literature (rank 5 of this report) confirms cortisone functions as an immunosuppressant, predisposing patients to opportunistic infections including oral and invasive candidiasis. This is a known safety concern for the entire glucocorticoid class.
- **Adrenal suppression**: Long-term use may suppress the hypothalamic-pituitary-adrenal (HPA) axis; abrupt withdrawal can precipitate acute adrenocortical insufficiency.
- **Drug interactions**: No DDI data was identified for cortisone specifically in this evidence pack. Class-level interactions with CYP3A4 inducers/inhibitors and drugs affecting 11β-HSD activity (e.g., posaconazole, as documented in the myelodysplastic syndrome literature) should be considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.67%), there is no direct clinical or preclinical evidence supporting cortisone for primary cutaneous T-cell lymphoma. The only identified clinical trial is suspended and does not study cortisone in CTCL. The mechanistic link is indirect (class effect via glucocorticoid-mediated T-cell apoptosis), and cortisone is not registered in Australia, creating additional regulatory barriers.

**To proceed, the following is needed:**
- Preclinical data (in vitro or in vivo) demonstrating cortisone or cortisol activity specifically in CTCL models
- Assessment of whether class-effect evidence from prednisone and dexamethasone in systemic T-cell lymphoma can be extrapolated to primary CTCL
- Mechanism of action data (DrugBank) to confirm cortisone's glucocorticoid receptor pharmacodynamics relative to modern agents
- Regulatory pathway assessment: TGA registration or Special Access Scheme (SAS) requirements before any clinical use in Australia
- Clarification of whether topical cortisone formulations — more appropriate for localised CTCL — may represent a more clinically rational application than systemic administration

---

> **⚠️ Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All predictions should be interpreted in the context of current clinical guidelines and individual patient circumstances.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

