---
layout: default
title: Romiplostim
parent: Moderate Evidence (L3-L4)
nav_order: 647
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-13
description: "Romiplostim: predicted new indication Primary release disorder of platelets (evidence level L4). Approved use: Autoimmune thrombocytopenia (ITP)"
---

# Romiplostim
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Romiplostim: From Immune Thrombocytopenia to Primary Release Disorder of Platelets

## One-Sentence Summary

Romiplostim is a thrombopoietin receptor (MPL) agonist, originally used to raise platelet counts in autoimmune thrombocytopenia (immune thrombocytopenia, ITP) and related bone marrow failure conditions.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**,
but there are currently **0 clinical trials** and only **1 publication** (a basic laboratory study of ITP, not of the predicted condition), so the prediction rests almost entirely on the model score.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Autoimmune thrombocytopenia (ITP); the knowledge graph also lists aplastic anaemia (the ARTG entry contains no indication text) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.9998% |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Romiplostim is a thrombopoietin receptor (MPL) agonist. It stimulates megakaryocyte proliferation and platelet production. Detailed mechanism data were not available in the data compiled for this report, so this description is based on pharmacology reference information on the target (MPL).

The only publication retrieved (PMID 25682608) shows that antiplatelet autoantibodies in ITP inhibit proplatelet formation by megakaryocytes. This supports the general idea of stimulating megakaryopoiesis in platelet disorders. However, it concerns ITP, which is already an established use, and not platelet release (secretion) disorders.

The mechanistic fit is weak. Platelet release disorders are mainly defects of platelet function (granule secretion and signalling). Raising the platelet count would not be expected to correct a qualitative defect. The very high TxGNN score most likely reflects closeness to ITP and other platelet disorders in the knowledge graph. It is not independent clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25682608](https://pubmed.ncbi.nlm.nih.gov/25682608/) | 2015 | Basic/mechanistic (in vitro) | Haematologica | In ITP, antiplatelet autoantibodies from patient serum and IgG inhibit proplatelet formation by megakaryocytes and impair platelet production in vitro. Does not address platelet release disorders. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 9696H | Nplate | Powder for injection 375 micrograms | Not stated in the data compiled for this report |

## Cytotoxicity

Not applicable. Romiplostim is not an antineoplastic drug, so this section is omitted.

## Safety Considerations

- **Drug Interactions**: Two entries were returned.
  - **Carfilzomib**: Major interaction (DDInter).
  - **Thrombopoietin receptor (MPL)**: This is the drug's pharmacological target, not an interaction with another drug.

For warnings, contraindications and other safety information, please refer to the TGA-approved Product Information (PI).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a knowledge-graph score and one laboratory study of ITP. A TPO-receptor agonist increases platelet number but would not be expected to correct a platelet secretion defect. Evidence is at L4 at best (model prediction plus mechanistic work in a different disease).

**To proceed, the following is needed:**
- Clear clinical definition of "primary release disorder of platelets", and evidence that low platelet count, rather than platelet function, drives patient harm
- Mechanistic or preclinical data showing that MPL agonism could benefit a platelet secretion defect
- Any case series or clinical study in qualitative platelet disorders
- Detailed mechanism of action data
- Review of the TGA-approved PI for warnings and contraindications, including the Major interaction with carfilzomib
- Approved indication wording for the ARTG entry, to confirm the original indication in Australia

**Other predictions (not recommended at this stage):** Pseudo-von Willebrand disease (score 99.9998%) and Glanzmann thrombasthenia (score 99.9995%) have no supporting trials or literature (L5, Hold). In both, the underlying defect (platelet GPIb gain-of-function; missing integrin αIIbβ3) would not be corrected by raising platelet counts. In pseudo-von Willebrand disease, a higher platelet mass could in principle worsen depletion of von Willebrand factor.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

