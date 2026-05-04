---
layout: default
title: Blinatumomab
parent: 僅模型預測 (L5)
nav_order: 94
evidence_level: L5
indication_count: 10
---

# Blinatumomab
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

# Blinatumomab: From B-cell Precursor Acute Lymphoblastic Leukaemia to Primary Release Disorder of Platelets

## One-Sentence Summary

Blinatumomab (Blincyto) is a bispecific T-cell engager (BiTE) antibody originally developed for relapsed or refractory B-cell precursor acute lymphoblastic leukaemia (ALL), redirecting cytotoxic T cells to destroy CD19-positive malignant B cells.
The TxGNN model predicts it may have activity in **Primary Release Disorder of Platelets**, with **2 clinical trials** identified but **no publications** directly supporting this repurposing direction.
Critically, both retrieved trials are for B-ALL rather than the predicted platelet indication, and current mechanistic analysis places the theoretical relevance below 5%.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Relapsed or refractory B-cell precursor acute lymphoblastic leukaemia (ALL) — based on clinical trial context; no TGA-approved indication on file |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 95.20% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed (no TGA registration) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on known information, blinatumomab is a bispecific T-cell engager (BiTE) that simultaneously binds CD19 on B lymphocytes and CD3 on T lymphocytes, forming an immunological synapse that activates cytotoxic T cells to kill CD19-positive B cells. This mechanism has established efficacy in B-cell precursor ALL, where malignant B-cell clones are selectively eliminated without conventional cytotoxic chemotherapy.

Primary release disorder of platelets — encompassing conditions such as δ-storage pool disease and α-granule deficiency — arises from intrinsic congenital defects in platelet granule biogenesis or content. These are non-immune disorders with no established B-cell–mediated pathogenesis. Blinatumomab's CD19-targeting mechanism has no known pathway to correct granule structural deficiencies, restore granule content, or improve platelet release function.

The only plausible indirect connection is that patients with ALL frequently develop secondary thrombocytopenia and platelet dysfunction due to bone marrow suppression. Treating the underlying ALL with blinatumomab may incidentally restore normal platelet production as haematopoietic recovery occurs — but this represents treatment of the primary oncological disease, not a genuine repurposing for a congenital platelet granule disorder as a distinct indication. The high TxGNN prediction score most likely reflects statistical co-occurrence of nodes in the knowledge graph (e.g., B-cell malignancy → thrombocytopenia → platelet release pathway) rather than a true mechanistic relationship.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT04524455](https://clinicaltrials.gov/study/NCT04524455) | Phase 1b | Completed | 17 | Safety and tolerability of blinatumomab combined with AMG 404 (anti-PD-1) in adults with relapsed/refractory B-ALL; evaluated MTD and recommended Phase 2 dose of AMG 404. Platelet-related findings, if any, reflect haematological safety monitoring rather than therapeutic intent for platelet disorders. |
| [NCT03476239](https://clinicaltrials.gov/study/NCT03476239) | Phase 3 | Completed | 121 | Efficacy and safety of blinatumomab in Chinese adults with relapsed/refractory B-precursor ALL; primary endpoint was haematological response (CR/CRh). Any platelet parameters reported are safety endpoints, not therapeutic targets for primary platelet release disorders. |

> **Important caveat:** Both trials carry Grade C relevance to the predicted indication. They were designed and powered for B-cell precursor ALL, not for primary release disorder of platelets. Neither trial addresses platelet granule function as an efficacy endpoint.

---

## Literature Evidence

Currently no related literature is available for blinatumomab in primary release disorder of platelets.

---

## Australia Market Information

Blinatumomab is not currently registered with the Therapeutic Goods Administration (TGA) and has no ARTG entries as of the data cut-off (5 April 2026).

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|-------------|--------------|-------------|---------------------|
| — | No ARTG entries | — | Not TGA-registered |

Healthcare professionals seeking access may wish to consider:
- **Special Access Scheme (SAS) Category B** — for individual patients with serious conditions
- **Clinical trial enrolment** — blinatumomab trials are active in Australia through global multicentre studies
- **International reference**: Blinatumomab is approved by the FDA (USA) and EMA (EU/UK) under the brand name **Blincyto** (Amgen) for B-cell precursor ALL, including relapsed/refractory disease and MRD-positive disease

---

## Cytotoxicity

Blinatumomab is an antineoplastic immunotherapy used in the treatment of leukaemia. The following applies to its established oncological use.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted immunotherapy — BiTE (bispecific T-cell engager) antibody; **not** a conventional cytotoxic agent |
| Myelosuppression Risk | Low to moderate (indirect); does not directly suppress haematopoiesis, but febrile neutropenia and infection are common adverse events; in ALL patients, underlying bone marrow disease contributes significantly |
| Emetogenicity Classification | Low (biologic/immunotherapy; not classified as emetogenic by standard chemotherapy emetogenicity scales) |
| Monitoring Items | Full blood count with differential (FBC), liver function tests (LFTs), renal function, neurological assessment at each cycle, vital signs and oxygen saturation during infusion (CRS monitoring), serum electrolytes |
| Handling Protection | Standard biologic/monoclonal antibody preparation and handling; conventional cytotoxic chemotherapy safe-handling protocols (closed-system transfer devices, cytotoxic PPE) are **not** mandated for this agent |

---

## Safety Considerations

Detailed safety data (TGA-approved warnings and contraindications) are not available in the current Evidence Pack. As blinatumomab is not TGA-registered, please refer to the **FDA Prescribing Information or EMA Summary of Product Characteristics (SmPC) for Blincyto** for full safety information.

The following key safety signals are documented in international prescribing information and are relevant to clinical consideration:

- **Cytokine Release Syndrome (CRS)**: Potentially life-threatening; requires standardised monitoring protocols, treatment algorithms (antipyretics, corticosteroids, tocilizumab for severe cases), and a minimum 9-day hospitalisation at treatment initiation
- **Neurotoxicity**: Encephalopathy, speech disorders, seizures, and confusion have been reported; may require temporary or permanent discontinuation; prophylactic dexamethasone is recommended
- **Infections**: Serious and opportunistic infections (including bacterial sepsis, fungal infections, viral reactivation); patients should be screened for active infections before treatment
- **Administration complexity**: Requires continuous intravenous infusion (cIV) via programmable infusion pump over 28-day cycles; medication preparation errors have caused patient harm and carry a specific FDA/EMA safety communication

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a TxGNN prediction score of 95.20%, mechanistic analysis demonstrates a very low theoretical basis (<5%) for blinatumomab activity in primary release disorder of platelets. The two retrieved clinical trials are Grade C (indirect) relevance — designed for B-cell precursor ALL — and no supporting literature exists for the predicted indication. The predicted disease involves congenital platelet granule defects that are mechanistically unrelated to CD19-targeted B-cell depletion.

**To proceed, the following is needed:**

- **MOA documentation**: Formally retrieve and document blinatumomab's mechanism of action from DrugBank or FDA/EMA product information to enable full mechanistic plausibility assessment
- **Knowledge graph pathway audit**: Investigate why the TxGNN model generated a 95.20% score for this drug-disease pair; determine whether the prediction reflects a genuine biological hypothesis or a statistical artefact from the ALL-thrombocytopenia co-occurrence pattern in the graph
- **TGA registration pathway assessment**: Evaluate whether blinatumomab is under active TGA consideration; note that FDA and EMA approvals exist for B-ALL and may support a TGA application under the established clinical framework
- **Redirect to higher-plausibility prediction**: Among all 10 predictions in this pack, **Glanzmann thrombasthenia (acquired autoimmune form, Rank #2, score 95.02%)** represents the most mechanistically credible repurposing candidate. Acquired Glanzmann thrombasthenia is driven by B-cell–produced anti-GPIIb/IIIa autoantibodies — directly within blinatumomab's therapeutic rationale. This direction is recommended for priority feasibility review, with a full separate Evidence Pack generated for that indication
- **Full safety data acquisition**: Obtain complete warnings, contraindications, and DDI profile from the Blincyto FDA label or EMA SmPC before any clinical access pathway is initiated

---

*This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. Data cut-off: 5 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

