---
layout: default
title: Acarbose
parent: Model Prediction Only (L5)
nav_order: 17
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Acarbose: predicted new indication Focal stiff limb syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "Acarbose"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis", "type 1 diabetes mellitus"]
---

# Acarbose
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Acarbose: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome

## One-Sentence Summary

Acarbose is an oral medicine used to lower blood sugar in type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **focal stiff limb syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction.
The prediction rests on the model alone and has no pharmacological support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (from the knowledge graph; no approved indication text is available for the Australian entry) |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Acarbose is known to be an intestinal alpha-glucosidase inhibitor. It delays carbohydrate digestion and reduces blood sugar rises after meals, with minimal absorption into the bloodstream. Its efficacy in type 2 diabetes is well established.

Focal stiff limb syndrome belongs to the stiff-limb and stiff-person spectrum. These conditions involve central nervous system or autoimmune disturbance of GABA-mediated and glycine-mediated signalling. Acarbose acts in the gut and does not modulate GABA signalling, nerve excitability or autoimmunity, so no plausible mechanistic link can be identified.

The high score is most likely a knowledge-graph artefact. Stiff-person-type disorders are epidemiologically associated with diabetes and autoimmunity, and the model may have picked up this shared link rather than any real treatment effect. The same applies to the closely related prediction, classic stiff person syndrome, which had an identical score.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13869Y | GLYBOSAY | Tablet 100 mg (oral) | Not stated in the data compiled for this report |

---

## Safety Considerations

Product-label warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for the authoritative safety information.

- **Conditions linked to acarbose in the knowledge graph as contraindications** (inferred from graph relationships, not from label text): kidney disease, pyoureter, liver disease, gallbladder disease, cirrhosis of the liver, inflammatory bowel disease, hypoglycaemia and injury.
- **Drug interactions:** 100 interactions were found. Only 20 were returned, and the rest need to be checked against a full interaction database.
  - **Moderate:** acetazolamide, salbutamol, aloe vera leaf, alpelisib, amprenavir, aripiprazole, asenapine, asparaginase (Erwinia chrysanthemi and E. coli), atazanavir, bedaquiline, bendroflumethiazide, benzphetamine, benzthiazide and betamethasone.
  - **Minor:** albiglutide, alclometasone (topical), lipoic acid, amcinonide and anisindione.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no literature and no identifiable mechanism, so it sits at the lowest evidence level (L5). The high score appears to come from diabetes-related links in the knowledge graph rather than pharmacology.

**To proceed, the following is needed:**
- Any mechanistic or clinical rationale linking alpha-glucosidase inhibition to stiff limb syndromes, which is unlikely to exist.
- Retrieval of the Australian Product Information (PI) for warnings and contraindications. The Australian approved indication text is also missing.
- A review of other predictions for this drug. Adjunctive use in **type 1 diabetes mellitus** has the best support in the data compiled (L2). It is backed by a placebo-controlled, double-blind trial (PMID 10227568) and several adjunct-therapy studies. These studies are dated and small, and full-text verification of trial design is needed before any decision.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

