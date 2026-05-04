---
layout: default
title: Alogliptin
parent: 僅模型預測 (L5)
nav_order: 33
evidence_level: L5
indication_count: 10
---

# Alogliptin
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

# Alogliptin: From Type 2 Diabetes to Classic Stiff Person Syndrome

## One-Sentence Summary

Alogliptin is a selective dipeptidyl peptidase-4 (DPP-4) inhibitor approved internationally for the management of Type 2 Diabetes Mellitus (T2DM), working by slowing the degradation of incretin hormones to enhance glucose-dependent insulin secretion.
The TxGNN model predicts it may have potential utility in **Classic Stiff Person Syndrome**, a rare progressive autoimmune neurological disorder, with a prediction score of **98.01%**.
This prediction is currently supported by **no clinical trials and no directly relevant literature**, placing the evidence firmly at Level 5 — model prediction only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus |
| Predicted New Indication | Classic Stiff Person Syndrome |
| TxGNN Prediction Score | 98.01% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on established international pharmacology, Alogliptin (brand names: Nesina [USA], Vipidia [EU]) is a highly selective, non-covalent DPP-4 inhibitor. It prevents the enzymatic breakdown of glucagon-like peptide-1 (GLP-1) and glucose-dependent insulinotropic polypeptide (GIP), thereby amplifying glucose-dependent insulin secretion and suppressing inappropriate glucagon release in patients with T2DM.

The proposed mechanistic bridge to Classic Stiff Person Syndrome (SPS) rests on the immunomodulatory role of DPP-4, also known as the surface antigen CD26. DPP-4/CD26 is widely expressed on CD4+ T cells, regulatory T cells, and other immune effector cells. Inhibiting DPP-4 theoretically dampens Th1 predominance, reduces pro-inflammatory cytokines including IL-6 and TNF-α, and may help modulate autoimmune dysregulation. Classic SPS is characterised by high-titre anti-GAD65 (glutamic acid decarboxylase 65) autoantibodies, progressive muscle rigidity, and painful spasms mediated by disrupted GABAergic inhibition driven by an immune-mediated process.

It is critical to note that this mechanistic link is entirely theoretical and based on indirect pathway reasoning within the TxGNN knowledge graph. There is no published animal model, preclinical study, or clinical report exploring alogliptin — or any DPP-4 inhibitor — in Stiff Person Syndrome or related GABAergic autoimmune conditions. The high TxGNN score (98.01%) reflects a structural connection between the DPP-4 inhibition node and the autoimmune disease cluster within the knowledge graph, not biological or clinical validation.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for Alogliptin in Classic Stiff Person Syndrome (searched ClinicalTrials.gov and ICTRP as of 2026-04-04).

---

## Literature Evidence

Currently no related literature is available for Alogliptin in Classic Stiff Person Syndrome (PubMed search returned 0 results as of 2026-04-04).

---

## Australia Market Information

Alogliptin is **not currently registered on the Australian Register of Therapeutic Goods (ARTG)**. There are no TGA-approved products, no Product Information (PI) documents, and no Consumer Medicines Information (CMI) documents available for this drug in Australia.

For safety and prescribing reference, clinicians should consult the FDA-approved US Prescribing Information (Nesina) or the EMA Summary of Product Characteristics (Vipidia) until Australian registration is sought.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. As Alogliptin is not currently registered in Australia, the relevant reference documents are the FDA Prescribing Information (Nesina) or EMA SmPC (Vipidia).

No warnings, contraindications, or drug interaction data were available in the current Evidence Pack. Of particular note from international labelling that Australian prescribers should be aware of before any off-label consideration:

- **Pancreatitis**: A known class risk for DPP-4 inhibitors; post-marketing cases have been reported
- **Heart failure**: The US label carries a warning based on the EXAMINE trial signal; use with caution in patients with existing cardiac disease
- **Hypersensitivity reactions**: Including anaphylaxis, angioedema, and Stevens-Johnson Syndrome — reported post-marketing

These points require formal verification against current authorised Product Information before any clinical decision-making.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten TxGNN-predicted indications for Alogliptin are rated Evidence Level L5 — pure model predictions with no supporting clinical trials or relevant literature. For the top-ranked indication (Classic Stiff Person Syndrome), the mechanistic rationale, while conceptually coherent, is purely speculative. Additionally, Alogliptin has zero Australian market presence, creating a significant regulatory hurdle before any clinical use could be contemplated.

**To proceed, the following is needed:**

- **Preclinical validation**: In vivo studies in a recognised SPS animal model (e.g., GAD65-immunised Lewis rat or NOD mouse) to test whether DPP-4 inhibition meaningfully alters disease markers
- **Mechanism of action documentation**: Formal DrugBank/literature query to confirm and document the complete MOA profile of Alogliptin
- **Broad DPP-4i literature sweep**: Systematic review of DPP-4 inhibitors in autoimmune neurological conditions more broadly (e.g., multiple sclerosis, myasthenia gravis) to establish the class immunomodulatory evidence base
- **Safety data retrieval**: Full extraction of TGA-equivalent safety data from FDA PI and EMA SmPC, including pancreatitis, cardiac, and hypersensitivity risks
- **Regulatory pathway assessment**: Evaluation of options for use in Australia under the Special Access Scheme (SAS) Category B or C, or as part of a registered clinical trial (CTN/CTA pathway)
- **Rare disease feasibility assessment**: Given the extreme rarity of Classic SPS (estimated prevalence ~1–2 per million), a patient recruitment feasibility assessment would be required before any trial design is considered

> **Disclaimer:** This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All content should be interpreted in conjunction with TGA-approved Product Information and current clinical practice guidelines.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

