---
layout: default
title: Terbinafine
parent: 僅模型預測 (L5)
nav_order: 660
evidence_level: L5
indication_count: 10
---

# Terbinafine
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

# Terbinafine: From Fungal Skin Infections to Creeping Myiasis

## One-Sentence Summary

Terbinafine is an allylamine antifungal historically used to treat dermatophyte infections of the skin and nails (e.g. tinea corporis, tinea pedis, onychomycosis). The TxGNN model's top-ranked prediction for this drug is **Creeping Myiasis**, a parasitic skin condition caused by migrating fly larvae — but this prediction is supported by **zero clinical trials** and **zero publications**, and the evidence pack's own mechanistic analysis flags it as pharmacologically implausible.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Fungal skin/nail infections (dermatophytosis, onychomycosis) — inferred from literature in this evidence pack; no ARTG licence record is available to confirm the TGA-approved wording |
| Predicted New Indication | Creeping Myiasis |
| TxGNN Prediction Score | 96.74% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Terbinafine's original mechanism of action is not recorded in the drug-level field of this evidence pack (`original_moa: [Data Gap]`), but it can be reconstructed from the supporting literature: terbinafine is an allylamine that inhibits fungal squalene epoxidase, blocking ergosterol biosynthesis in the fungal cell membrane, producing a fungicidal effect against dermatophytes and some yeasts (PMID [2689015](https://pubmed.ncbi.nlm.nih.gov/2689015/), PMID [1372222](https://pubmed.ncbi.nlm.nih.gov/1372222/)).

Creeping myiasis is not a fungal disease — it is a parasitic skin condition caused by the subcutaneous migration of fly larvae (an arthropod infestation). It has no ergosterol-dependent biology and no known sensitivity to squalene-epoxidase inhibitors. There is no shared pathophysiology between the original indication (fungal infection) and the predicted new indication (larval infestation), so the mechanism does not transfer.

This assessment matches the evidence pack's own rationale: the mechanistic link is described as "purely a knowledge-graph embedding similarity artefact," with no literature, no clinical trials, and no biologically plausible pathway connecting terbinafine to creeping myiasis. Among the ten candidates generated for this drug, this top-ranked one is one of several (creeping/furuncular/wound myiasis, toxoplasmosis, echinococcosis) that share this pattern — high TxGNN similarity score but no mechanistic or evidentiary support, most likely driven by incidental literature co-occurrence rather than a real pharmacological relationship. By contrast, the lower-ranked candidates in this pack with actual trial/literature support (e.g. tinea manuum, superficial mycosis) largely reflect terbinafine's *already-established* antifungal role rather than a genuine new indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

No ARTG entries were found for terbinafine in this evidence pack (`total_licenses: 0`, market status: Not marketed). This should be verified directly against the TGA/ARTG public register, since terbinafine-containing products (e.g. topical/oral formulations) are known to exist in other markets — the absence here may reflect a data-source gap rather than confirmed non-registration.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (creeping myiasis) has no clinical trial or literature support and no plausible mechanistic basis — myiasis is a parasitic larval infestation, not a target of terbinafine's antifungal (ergosterol synthesis inhibition) activity. This is an L5, prediction-only candidate and does not warrant progression.

**To proceed, the following is needed:**
- TGA/ARTG registration status for terbinafine should be independently verified (this evidence pack found none, which is unexpected for a globally marketed antifungal)
- TGA-approved Product Information (warnings, contraindications, DDI) to close the Blocking data gap (DG001) before any safety assessment
- Confirmed mechanism-of-action documentation (DG002), even though partially reconstructable from literature in this pack
- If further repurposing evaluation of terbinafine is desired, the lower-ranked candidates in this pack with L2–L3 evidence (e.g. superficial mycosis, tinea manuum, cutaneous candidiasis, blastomycosis) should be assessed separately — noting that several of these likely represent terbinafine's existing approved antifungal use rather than a novel repurposing opportunity, so their incremental value should be scrutinised before investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

