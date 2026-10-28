---
layout: default
title: Romiplostim
parent: Model Prediction Only (L5)
nav_order: 647
evidence_level: L5
indication_count: 10
monitor_inn: "Romiplostim"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "fetal and neonatal alloimmune thrombocytopenia", "Scott syndrome", "hemorrhagic disorder due to a constitutional thrombocytopenia", "bleeding diathesis due to a collagen receptor defect", "platelet-type bleeding disorder", "autosomal dominant macrothrombocytopenia", "Ehlers-Danlos syndrome, fibronectinemic type"]
last_modified_at: 2026-10-28
description: "Romiplostim: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Relations recorded in the knowledge graph: idiopathic aplastic anaemi…"
---

# Romiplostim
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Romiplostim: From Immune Thrombocytopenia to Primary Release Disorder of Platelets
{: .text-alpha }

## One-Sentence Summary

Romiplostim (Nplate) is a thrombopoietin receptor agonist whose recorded uses in the knowledge graph include aplastic anaemia and autoimmune thrombocytopenia. The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but **no clinical trials** and only **1 mechanistic publication** (on immune thrombocytopenia, a different disease) are available. This prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relations recorded in the knowledge graph: idiopathic aplastic anaemia, aplastic anaemia, autoimmune thrombocytopenia (the local ARTG record contains no indication text) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From the pharmacology record, romiplostim is a peptide agonist of the thrombopoietin receptor (MPL), which stimulates megakaryocyte maturation and platelet production.

Primary release disorder of platelets is a qualitative defect in platelet function. Raising the platelet count would not be expected to correct a defect in how platelets function, so the mechanistic link is weak. The only linked paper (PMID 25682608) describes autoantibodies inhibiting proplatelet formation in immune thrombocytopenia, which is a different disease mechanism. The very high model score is not backed by clinical evidence.

Other predicted conditions follow a similar pattern. Pseudo-von Willebrand disease, Glanzmann thrombasthenia, Scott syndrome, collagen receptor defects and platelet-type bleeding disorders are mostly function defects, where a platelet-count-raising drug has no clear rationale. Fetal and neonatal alloimmune thrombocytopenia (rank 4) is the most plausible hypothesis, because it is an immune-mediated thrombocytopenia related to the immune thrombocytopenia setting. The evidence for it is indirect, however (see below).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The one publication linked to the top-ranked prediction:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25682608](https://pubmed.ncbi.nlm.nih.gov/25682608/) | 2015 | Basic/mechanistic research | Haematologica | Antiplatelet autoantibodies from immune thrombocytopenia patients inhibited proplatelet formation by megakaryocytes in vitro. This concerns a different disease. |

For the fourth-ranked prediction (fetal and neonatal alloimmune thrombocytopenia), only indirect literature exists and no study addresses that disease directly:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31239245](https://pubmed.ncbi.nlm.nih.gov/31239245/) | 2019 | Review | Blood Advances | Romiplostim in paediatric immune thrombocytopenia: drug development and current practice |
| [34711622](https://pubmed.ncbi.nlm.nih.gov/34711622/) | 2021 | Case report | BMJ Case Reports | Management of refractory immune thrombocytopenia in pregnancy |
| [23822831](https://pubmed.ncbi.nlm.nih.gov/23822831/) | 2013 | Case report | Eur J Haematol | Complete remission of refractory immune thrombocytopenia after a short course of romiplostim |
| [20410910](https://pubmed.ncbi.nlm.nih.gov/20410910/) | 2010 | Review/commentary | J Perinatol | Whether novel thrombopoietic agents should be introduced in neonatal care |
| [27605856](https://pubmed.ncbi.nlm.nih.gov/27605856/) | 2016 | Case report | Asian J Transfus Sci | Refractory immune thrombocytopenia in pregnancy managed with eltrombopag (not romiplostim) |
| [23257464](https://pubmed.ncbi.nlm.nih.gov/23257464/) | 2012 | Review | Zhongguo Shi Yan Xue Ye Xue Za Zhi | Advances in thrombopoietic drugs for childhood immune thrombocytopenia |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 9696H | Nplate | Powder for injection 375 micrograms | Not stated in the available record |

## Safety Considerations

- **Drug Interactions**:
  - Carfilzomib: Major interaction (DDInter).
  - Thrombopoietin receptor (MPL): the pharmacological target of romiplostim, listed in the pharmacology record rather than as a clinical interaction.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications. Placental transfer and fetal or neonatal safety remain unresolved for the alloimmune thrombocytopenia hypothesis.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or publication directly studies primary release disorder of platelets, so the evidence level is L5. The mechanism (raising platelet count) does not match a qualitative platelet function defect. The model score alone is not enough to justify progression.

**To proceed, the following is needed:**
- Mechanism of action data and TGA PI warnings and contraindications (currently missing)
- Direct clinical or mechanistic evidence in the predicted disease
- For the more plausible fetal and neonatal alloimmune thrombocytopenia hypothesis: disease-specific studies and a dedicated safety assessment covering placental transfer and neonatal platelet response
- For inherited thrombocytopenias: subtype-specific evidence, since the category is too heterogeneous to assess
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

