---
layout: default
title: Empagliflozin
parent: 僅模型預測 (L5)
nav_order: 184
evidence_level: L5
indication_count: 10
---

# Empagliflozin
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

# Empagliflozin: From Type 2 Diabetes to Focal Stiff Limb Syndrome

## One-Sentence Summary

Empagliflozin is a Sodium-Glucose Cotransporter-2 (SGLT2) inhibitor used internationally for type 2 diabetes mellitus, heart failure, and chronic kidney disease, though it currently holds no TGA registration in Australia.
The TxGNN model predicts it may be effective for **Focal Stiff Limb Syndrome**, however there are **no clinical trials** and **no directly relevant publications** supporting this specific indication.
The evidence base is limited to a computational model prediction only, and the predicted mechanistic link is considered biologically implausible at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no ARTG registration; internationally used for Type 2 Diabetes, Heart Failure, CKD) |
| Predicted New Indication | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this Evidence Pack. Based on contextual information within the supporting literature, Empagliflozin is an SGLT2 inhibitor that promotes urinary glucose excretion via an insulin-independent mechanism. Its known pharmacological actions include AMPK activation, NF-κB inhibition, and reduction in visceral adiposity — effects that underpin its established cardiovascular and renal protective benefits in cardiometabolic disease.

Focal stiff limb syndrome is a rare autoimmune neurological disorder driven by anti-GAD65 (glutamic acid decarboxylase 65) antibodies, which disrupt GABAergic inhibition in the spinal cord, resulting in focal muscle rigidity. The underlying pathophysiology involves specific neuroimmune mechanisms that are mechanistically distinct from the metabolic and glucose transport pathways targeted by SGLT2 inhibition. There is no known biological bridge between SGLT2 blockade and GABAergic dysfunction.

The TxGNN model's high prediction score of 99.06% for this indication most likely reflects indirect graph traversal through shared metabolic and inflammatory nodes in the knowledge graph, rather than a genuine biological relationship. This pattern — where scores cluster tightly across mechanistically unrelated rare diseases — is a recognised behaviour of knowledge graph-based models and should be interpreted with caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Empagliflozin in focal stiff limb syndrome.

---

## Literature Evidence

Currently no related literature available for Empagliflozin in focal stiff limb syndrome.

---

## Australia Market Information

Empagliflozin currently has **no ARTG (Australian Register of Therapeutic Goods) entries**. The drug is not registered or marketed in Australia as at the data cutoff date of 4 April 2026.

Clinicians seeking product information should consult international regulatory sources (e.g., EMA, FDA, or Health Canada product information for Jardiance®) as a reference pending any future TGA submission.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. As Empagliflozin currently has no ARTG registration, clinicians should consult the publicly available international product information for safety guidance until a local PI is available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or literature evidence supporting the use of Empagliflozin in focal stiff limb syndrome, and the mechanistic link between SGLT2 inhibition and this anti-GAD65-mediated autoimmune neurological disorder is not biologically plausible based on current pharmacological understanding. The high TxGNN score is likely an artefact of knowledge graph node clustering across rare disease categories rather than a reflection of true therapeutic potential.

**To proceed, the following is needed:**

- Confirmed mechanism of action (MOA) data for Empagliflozin via DrugBank API query (remediation identified in data gap DG002)
- Preclinical evidence demonstrating any plausible biological connection between SGLT2 inhibition and GABAergic or neuroimmune dysfunction
- TGA Product Information (PI) or equivalent international PI review to establish a comprehensive safety baseline (remediation identified in data gap DG001)
- Monitoring of ARTG registration submissions, as Empagliflozin may be lodged for TGA approval in future given its international regulatory standing
- Reassessment of lower-ranked predicted indications (e.g., pancreatic agenesis, Rank 9) where a theoretical insulin-independent glucose-lowering mechanism offers more biologically coherent rationale, pending generation of indication-specific preclinical data

---

> **Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

