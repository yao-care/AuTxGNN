---
layout: default
title: Griseofulvin
parent: 僅模型預測 (L5)
nav_order: 221
evidence_level: L5
indication_count: 10
---

# Griseofulvin
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

# Griseofulvin: From Dermatophytosis to Myiasis

## One-Sentence Summary

Griseofulvin is a classic narrow-spectrum antifungal agent, established since the 1950s for treating dermatophyte infections including tinea capitis (scalp ringworm), tinea corporis, and onychomycosis.
The TxGNN model predicts it may be effective for **Myiasis** (dipteran larval tissue infestation), with **0 clinical trials** and **1 veterinary literature reference** identified — a reference that provides no mechanistic support whatsoever.

> ⚠️ **Important context for clinicians:** All 10 of Griseofulvin's top TxGNN predictions were assessed as mechanistically unsound or unsubstantiated, each receiving a **Hold** recommendation. This report documents the findings and explains why the model predictions are most likely systematic false positives arising from knowledge graph topology rather than genuine pharmacological relationships.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Dermatophytosis (tinea capitis, tinea corporis, tinea pedis, onychomycosis) |
| Predicted New Indication | Myiasis (fly larval tissue infestation) |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed — no ARTG registration |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not retrieved from DrugBank during this analysis. Based on established pharmacological knowledge, Griseofulvin is a natural product derived from *Penicillium griseofulvum* that acts by binding to polymerised fungal tubulin, disrupting microtubule assembly and thereby blocking mitosis in fungal cells. Crucially, its activity is **selective for dermatophytes** (*Trichophyton*, *Microsporum*, and *Epidermophyton* species). It has no clinically relevant activity against *Candida* species, dimorphic fungi, bacteria, or parasites.

Myiasis is a parasitic infestation caused by dipteran (fly) larvae invading living tissue — an entomological condition with no fungal component. There is no known biochemical target shared between fly larvae and the fungal tubulin pathway that Griseofulvin exploits. The single literature reference retrieved (a 1970 veterinary review on parasitic skin diseases in dogs and cats) does not describe or suggest any use of Griseofulvin for myiasis; its retrieval reflects overlapping MeSH indexing under "skin disease" and "parasitic disease" subject headings rather than any pharmacological relationship.

The TxGNN score of 99.41% most likely reflects indirect connections through shared "skin disease" and "dermatology" nodes within the knowledge graph, rather than a genuine drug–disease pharmacological link. This pattern — very high model scores with no mechanistic support and no clinical evidence — is consistent across all 10 top predictions for this drug, which span insect larval diseases, tapeworm infections, a protozoan infection (toxoplasmosis), a yeast infection where Griseofulvin is known to be **ineffective** (cutaneous candidiasis), and even a gram-negative anaerobic bacterial infection (Bacteroidaceae). Together, these results indicate the model is producing systematic false positives for Griseofulvin outside its well-defined antifungal class.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Griseofulvin in myiasis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [4098614](https://pubmed.ncbi.nlm.nih.gov/4098614/) | 1970 | Veterinary Review | The Veterinary Record | General review of parasitic skin diseases in dogs and cats; no data on Griseofulvin for myiasis treatment — retrieved due to shared dermatological MeSH indexing |

> **Note:** This single reference is not supportive evidence. Its retrieval is a search artefact, not a clinical signal.

---

## Overview of All Predicted Indications

For transparency, all 10 TxGNN predictions are summarised below with their mechanistic assessment:

| Rank | Disease | TxGNN Score | Evidence Level | Mechanistic Assessment |
|------|---------|-------------|----------------|----------------------|
| 1 | Myiasis | 99.41% | L5 | ❌ Dipteran larvae — antifungal mechanism irrelevant |
| 2 | Wound myiasis | 99.34% | L5 | ❌ Same as above; no literature |
| 3 | Creeping myiasis | 99.34% | L5 | ❌ Same as above; no literature |
| 4 | Furuncular myiasis | 99.34% | L5 | ❌ Same as above; physical removal is standard care |
| 5 | Echinococcus granulosus infection | 99.32% | L5 | ❌ Tapeworm disease — Albendazole/surgery is standard; Griseofulvin has no anthelmintic activity |
| 6 | Cutaneous candidiasis | 98.71% | L4 | ❌ **Reverse evidence** — Griseofulvin is pharmacologically inactive against *Candida*; 20 retrieved references use it as a negative comparator |
| 7 | Toxoplasmosis | 98.69% | L5 | ❌ Protozoan infection — standard therapy is Pyrimethamine + Sulfadiazine; no mechanistic link |
| 8 | Alveolar echinococcosis | 98.36% | L5 | ❌ *Echinococcus multilocularis* tapeworm — same false positive pattern as rank 5 |
| 9 | Blastomycosis | 97.08% | L4 | ❌ Dimorphic fungus — Griseofulvin has minimal in vitro activity; IDSA 2008 guidelines recommend Itraconazole or Amphotericin B; references are 1960–70s historical reviews only |
| 10 | Bacteroidaceae infectious disease | 95.57% | L5 | ❌ Gram-negative anaerobic bacteria — Griseofulvin has no antibacterial activity; most egregious cross-domain model error |

---

## Australia Market Information

Griseofulvin is **not currently registered on the Australian Register of Therapeutic Goods (ARTG)**. There are no TGA-approved products available on the Australian market.

Clinicians who need to prescribe Griseofulvin for its established indication (most commonly tinea capitis in children, where it remains a guideline-recommended option in some settings) would need to access it through one of the following TGA pathways:

- **Special Access Scheme – Category B (SAS-B)**: For individual patients with a legitimate clinical need
- **Authorised Prescriber**: For practitioners who regularly treat a particular condition requiring the drug

---

## Safety Considerations

No TGA-approved Product Information (PI) document is available for Griseofulvin in Australia. For prescribing safety information, refer to overseas-approved PI documents (FDA, EMA, or UK SMC). Key known safety considerations from the established pharmacological literature include:

- **Teratogenicity**: Contraindicated in pregnancy (FDA Category X / ADEC Category D); embryotoxic and teratogenic in animal studies
- **Hepatotoxicity**: Contraindicated in hepatocellular failure and porphyria
- **Photosensitivity**: Patients should be advised to avoid excessive sun exposure
- **Drug interactions**: Reduces efficacy of warfarin (CYP enzyme induction); may reduce efficacy of combined oral contraceptives; potentiates effects of alcohol
- **Haematological**: Rare agranulocytosis and leucopenia reported — monitoring of FBC may be appropriate with prolonged therapy

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN top predictions for Griseofulvin are mechanistically unsupported. The predictions span organisms (fly larvae, tapeworms, protozoa, gram-negative bacteria) and drug class boundaries that Griseofulvin cannot plausibly cross. Notably, the rank 6 prediction (cutaneous candidiasis) represents a case where existing pharmacological evidence actively contradicts the prediction — Griseofulvin's activity against *Candida* is well established as negligible. The pattern strongly suggests the model is assigning high scores based on shared knowledge graph neighbourhood (dermatological and infectious disease nodes) rather than true pharmacological relatedness.

**To proceed, the following would be needed:**

- Retrieve complete DrugBank MOA, toxicity, and interaction data to fulfil identified data gaps (DG001, DG002)
- Review lower-ranked TxGNN predictions beyond the top 10 to identify any dermatophyte-adjacent indications (e.g., specific tinea variants, Majocchi's granuloma, or onychomycosis subtypes) where a genuine mechanistic case could be made
- If considering access for established indications (tinea capitis), initiate TGA Special Access Scheme (SAS-B) assessment and confirm current international guideline positioning against newer alternatives (Terbinafine, Itraconazole)
- No repurposing investment is recommended on the basis of the current top 10 predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

