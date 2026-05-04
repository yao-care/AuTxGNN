---
layout: default
title: Clindamycin
parent: 僅模型預測 (L5)
nav_order: 116
evidence_level: L5
indication_count: 10
---

# Clindamycin
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

# Clindamycin: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Clindamycin is a lincosamide antibiotic with established activity against Gram-positive organisms and anaerobes, widely used for skin and soft tissue infections, anaerobic infections, and bacterial vaginosis.
The TxGNN model predicts it may have potential for **Punctate Epithelial Keratoconjunctivitis (PEK)**,
however, **no clinical trials** and **no publications** were identified to support this specific repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (skin and soft tissue, bone and joint, anaerobic infections, bacterial vaginosis) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Australia Market Status | No ARTG entries identified in current dataset |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Clindamycin is a lincosamide antibiotic that inhibits bacterial protein synthesis by binding to the 50S ribosomal subunit, thereby blocking peptide chain elongation. Its spectrum covers Gram-positive aerobes — particularly *Staphylococcus aureus*, *Streptococcus pyogenes*, and *S. pneumoniae* — as well as a broad range of anaerobic organisms. These properties have established its clinical role in skin and soft tissue infections, bone and joint infections, pelvic inflammatory disease, and bacterial vaginosis. Detailed mechanism of action data from DrugBank was not available at the time of this analysis; the above description is drawn from the published literature and standard pharmacological references.

Punctate epithelial keratoconjunctivitis (PEK) is characterised by fine punctate erosions of the corneal and conjunctival epithelium. Its most common aetiologies are viral (particularly adenovirus) and toxic reactions to topical ophthalmic medications — neither of which involves a bacterial pathogen susceptible to Clindamycin. While secondary bacterial superinfection of a compromised ocular surface remains a theoretical possibility, PEK itself is not a bacterially driven disease entity.

The mechanistic link between Clindamycin's antibacterial activity and PEK is therefore weak. The TxGNN knowledge graph prediction most likely reflects a broad topological proximity between Clindamycin and ocular surface disease nodes within the graph, rather than a direct pharmacological relationship. The high TxGNN score (99.97%) reflects the model's confidence in this graph-derived association but is not corroborated by any clinical or preclinical evidence specific to PEK. This pattern — high model score without supporting evidence — is a known characteristic of L5-level predictions and underscores the importance of downstream evidence validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for Punctate Epithelial Keratoconjunctivitis.

---

## Australia Market Information

No ARTG entries for Clindamycin were identified in the current dataset (0 registered products). This finding is unexpected given Clindamycin's global availability and established clinical use, and most likely reflects a data collection gap rather than true absence from the Australian market. Healthcare professionals should verify current registration status directly via the [TGA ARTG Public Summary](https://www.tga.gov.au/resources/artg) before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Full safety data — including warnings, contraindications, and drug interactions — was not available in this Evidence Pack and represents a blocking data gap for any formal safety evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Punctate epithelial keratoconjunctivitis is primarily a viral or medication-toxicity condition; Clindamycin's antibacterial mechanism does not address its underlying pathophysiology, and no clinical or preclinical evidence (L5) supports this repurposing direction. The same Hold status applies across all 10 TxGNN-predicted indications in this pack, several of which carry additional concerns: rank 3 ("non-human animal disease") is not a valid human therapeutic target; rank 8 ("toxic maculopathy due to antimalarial drugs") represents a directional paradox, as Clindamycin is itself used as an antimalarial partner drug rather than a remedy for antimalarial-induced retinal toxicity; and ranks 1, 4, 7, 9, and 10 lack any supporting evidence whatsoever.

**To proceed, the following is needed:**

- **Resolve ARTG data gap:** Manually verify current TGA registration status and obtain approved Product Information documents for Clindamycin via the TGA ARTG portal
- **Resolve safety data gap (blocking):** Extract full warnings, contraindications, and drug interaction profile from the TGA PI to enable S1 safety pre-screening
- **Obtain DrugBank MOA data:** Query the DrugBank API for detailed mechanism of action, pharmacological categories, and toxicity data to enable rigorous mechanistic linkage analysis
- **Re-evaluate indication ranking:** If pursuing an ophthalmic application, the secondary bacterial infection scenario in Exposure Keratitis (rank 2, L4) represents a modestly stronger biological rationale than PEK (rank 1) given existing literature on *S. aureus* keratitis — though this would represent adjunctive use rather than a novel repurposing claim
- **Assess route compatibility:** Any ophthalmic application of Clindamycin would require confirmation that a suitable topical ophthalmic formulation exists or is developable; systemic formulations are not appropriate for ocular surface conditions

> **Disclaimer:** This report is intended for research purposes only and does not constitute medical advice. Drug repurposing candidates require prospective clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

