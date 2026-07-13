---
layout: default
title: Cefaclor
parent: 僅模型預測 (L5)
nav_order: 131
evidence_level: L5
indication_count: 10
---

# Cefaclor
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

# Cefaclor: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Cefaclor is a second-generation oral cephalosporin antibiotic with established global use for treating bacterial infections including respiratory tract infections, urinary tract infections, and skin infections — though it currently holds no TGA registration in Australia.

The TxGNN model ranks **Hyperamylasemia** as the top predicted new indication; however, with **no supporting clinical trials or publications**, confidence in this prediction is very low (Evidence Level L5).

> **Analyst Note:** The highest-evidence predicted indication within this evaluation pack is **Gonococcal Urethritis** (Rank 3, L3, 6 published studies). Clinicians reviewing this report for research prioritisation should refer to the gonococcal urethritis rationale in the Conclusion section.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (no TGA-approved indication; not registered in Australia) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 97.70% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, Cefaclor is a second-generation cephalosporin that inhibits bacterial cell wall synthesis by covalently binding to penicillin-binding proteins (PBPs), blocking peptidoglycan cross-linking. Its chloro-substituted side chain — modified from cephalexin — provides improved Gram-negative coverage while retaining good oral bioavailability and gastrointestinal absorption.

Hyperamylasemia is a laboratory finding (elevated serum amylase) rather than a primary bacterial disease. Its most common causes — acute pancreatitis, salivary gland disorders, and intestinal injury — are non-infectious or metabolic in nature, with bacterial pathogens playing no direct causal role in amylase physiology. Cefaclor's β-lactam mechanism has no pathway by which it could suppress amylase secretion, accelerate amylase clearance, or modify pancreatic enzyme activity.

The high TxGNN score (97.70%) is most plausibly explained by knowledge graph topology: acute infection is a recognised trigger of pancreatitis, placing the two concept nodes in close proximity within the knowledge graph. This graph adjacency does not constitute mechanistic or clinical rationale. Notably, the second-ranked prediction (polyclonal hyperviscosity syndrome) carries an **identical score** (0.9770268…), strongly suggesting a batch-computation artefact rather than genuine signal. This prediction should be treated as a graph false positive.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

> Cefaclor has no current TGA registration in Australia. For class-level safety reference, clinicians should consult prescribing information from an approved jurisdiction (e.g., FDA labelling or UK SPC). Well-established cephalosporin class considerations include: hypersensitivity reactions (including possible cross-reactivity in penicillin-allergic patients), *Clostridioides difficile*-associated diarrhoea with prolonged use, and dose adjustment requirements in renal impairment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for hyperamylasemia has no supporting clinical evidence and no credible pharmacological mechanism. Cefaclor's β-lactam mode of action cannot influence amylase secretion or clearance, and the identical scores across the top two predictions indicate this is a knowledge graph computation artefact rather than a genuine repurposing signal.

**To proceed with any Cefaclor repurposing programme in Australia, the following is needed:**

- **TGA registration pathway assessment:** Cefaclor currently has zero ARTG entries. Any clinical use in Australia would require either a full ARTG submission or access via the TGA Special Access Scheme (SAS) or Authorised Prescriber pathway.
- **Redirect evaluation effort to Gonococcal Urethritis (Rank 3):** This is the only indication with biologically credible mechanism and actual evidence in this pack — *Neisseria gonorrhoeae* expresses PBP1/PBP2 targets, and six published studies (including controlled clinical trials, 1979–1997) documented Cefaclor efficacy. Before any clinical consideration, **current local antimicrobial resistance patterns must be assessed**: WHO and CDC guidelines now recommend ceftriaxone 500 mg IM as standard of care due to widespread oral cephalosporin resistance.
- **Local MIC surveillance:** Current minimum inhibitory concentration (MIC) data for Australian *N. gonorrhoeae* strains is essential before any contemplation of Cefaclor for gonococcal infection.
- **Full MOA data retrieval:** Retrieve complete mechanism of action, pharmacokinetic, and target data from DrugBank (DB00833) to support formal mechanistic analysis.
- **Safety data:** Source TGA-equivalent warnings, contraindications, and drug interaction data from an approved jurisdiction's Product Information (PI) prior to any prescribing or research protocol development.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

