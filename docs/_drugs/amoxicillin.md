---
layout: default
title: Amoxicillin
parent: 僅模型預測 (L5)
nav_order: 45
evidence_level: L5
indication_count: 10
---

# Amoxicillin
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

# Amoxicillin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Amoxicillin is a broad-spectrum penicillin-class antibiotic with well-established use in treating a wide range of bacterial infections, including respiratory tract, urinary tract, and skin infections.
The TxGNN model predicts it may be effective for **Polyclonal Hyperviscosity Syndrome**,
however, this prediction is currently supported by **0 clinical trials** and **0 publications**, representing a purely model-driven finding with no direct clinical evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (no ARTG records found) |
| Predicted New Indication | Polyclonal Hyperviscosity Syndrome |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed (per current data) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, amoxicillin is a beta-lactam antibiotic that inhibits bacterial cell wall synthesis by irreversibly binding to penicillin-binding proteins (PBPs), blocking peptidoglycan cross-linking and triggering bacterial cell lysis. It is active against a wide range of Gram-positive and selected Gram-negative organisms.

Polyclonal hyperviscosity syndrome is characterised by elevated plasma viscosity due to a marked rise in polyclonal immunoglobulins, most commonly arising in the context of chronic inflammatory states, autoimmune disease, or recurrent infection rather than as a primary bacterial illness. There is a narrow indirect rationale: if a sustained or recurrent bacterial infection is driving chronic immune stimulation and polyclonal hypergammaglobulinaemia, effective antibiotic treatment could theoretically reduce antigenic load, thereby dampening immunoglobulin production and lowering viscosity.

However, no clinical trials or peer-reviewed publications have directly examined amoxicillin for this condition. The TxGNN score likely reflects topological proximity within the knowledge graph (e.g., shared disease nodes linking infectious aetiology to immune dysregulation) rather than a validated causal mechanism. This prediction should be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a model-only prediction (Evidence Level L5) with no registered clinical trials and no published literature directly supporting the use of amoxicillin for polyclonal hyperviscosity syndrome. The proposed mechanistic link is indirect, speculative, and lacks any clinical validation.

**To proceed, the following is needed:**
- Retrieve confirmed mechanism of action (MOA) data from DrugBank (DB01060) to support mechanistic plausibility assessments
- Download and parse the TGA-approved Product Information (PI) to establish approved indications, key warnings, and contraindications
- Verify ARTG registration status directly via the TGA ARTG public portal, as the current data shows zero entries despite amoxicillin's known clinical availability
- Commission a targeted systematic literature review focusing on amoxicillin and hyperviscosity, polyclonal hypergammaglobulinaemia, or chronic infection-associated immunoglobulin elevation
- Consider prioritising **Monoclonal Gammopathy / IPSID (Rank 6, Evidence Level L3)** as a more actionable repurposing candidate: multiple published case series (PMIDs 9030995, 20300878, 8988128, 16253033) document regression of immunoproliferative small intestinal disease (IPSID / alpha heavy-chain disease) following *Helicobacter pylori* eradication therapy that includes amoxicillin, establishing a biologically plausible and partially evidenced mechanistic link

---

> **Disclaimer:** This report is produced for research purposes only and does not constitute medical advice. All drug repurposing candidates require prospective clinical validation before any therapeutic application can be considered.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

