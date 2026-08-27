---
layout: default
title: Ivermectin
parent: 僅模型預測 (L5)
nav_order: 372
evidence_level: L5
indication_count: 10
---

# Ivermectin
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

# Ivermectin: From Parasitic Infections to Vulvovaginal Candidiasis

## One-Sentence Summary

Ivermectin is a broad-spectrum antiparasitic agent widely used for conditions including scabies, strongyloidiasis, and onchocerciasis.
The TxGNN model's top prediction is **Vulvovaginal Candidiasis** (score 99.95%), however all 10 predicted indications across this candidate cluster around fungal and vulvovaginal conditions — none of which are mechanistically linked to Ivermectin's pharmacology.
**Zero clinical trials and zero supportive publications** were identified; all predictions are rated **L5 (model prediction only)**, and the high TxGNN scores most likely reflect Knowledge Graph topology artefacts rather than genuine therapeutic signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No ARTG registration data found; Ivermectin is a well-established antiparasitic agent |
| Predicted New Indication | Vulvovaginal Candidiasis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Australia Market Status | Not detected in ARTG data pipeline (0 entries — see note below) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

> **⚠️ ARTG Data Note:** The automated pipeline returned 0 ARTG entries for Ivermectin. This is likely a data pipeline gap — Ivermectin-containing products are known to exist in the Australian market (e.g., for scabies treatment). Clinicians should verify current TGA registration status directly via the [ARTG public search](https://www.tga.gov.au/resources/artg) or the [TGA Product Information repository](https://www.ebs.tga.gov.au/).

---

## Why is This Prediction Reasonable?

Ivermectin acts by binding to glutamate-gated chloride ion channels (GluCl) in invertebrate nerve and muscle tissue, causing hyperpolarisation, paralysis, and death of susceptible parasites (nematodes, arthropods). This target is biologically unique to invertebrates and is entirely absent in vertebrates, bacteria, and fungi. *Candida* species — the pathogen implicated in 7 of the 10 predicted indications — do not express GluCl channels and offer no known cellular target through which Ivermectin could exert antifungal activity.

All 10 TxGNN-predicted indications involve either fungal infections (candidiasis), HPV, or non-specific vulvovaginal inflammation. None carry mechanistic plausibility. The evidence pipeline's own repurposing rationale field for each indication explicitly identifies a probable **Knowledge Graph (KG) co-occurrence artefact**: immunocompromised patients who are susceptible to parasitic infections (Ivermectin's established therapeutic target) are simultaneously at elevated risk of candidiasis and HPV — creating spurious KG proximity between Ivermectin nodes and these fungal/viral disease nodes, without any causal treatment pathway.

The two literature results retrieved by the evidence pipeline (see Literature Evidence below) further confirm this interpretation. Both describe Ivermectin being used for its **known indications** (strongyloidiasis, crusted scabies) in immunocompromised patients who coincidentally had concurrent candidiasis. These publications provide no evidence whatsoever of Ivermectin antifungal efficacy; they are textbook examples of co-indication literature mismatch within a KG-based prediction model.

---

## Clinical Trial Evidence

No clinical trials investigating Ivermectin for any of the 10 predicted indications were identified across ClinicalTrials.gov, ICTRP, or ANZCTR registries.

---

## Literature Evidence

Two publications were retrieved. Neither supports the predicted indications; both represent KG co-indication artefacts.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35835488](https://pubmed.ncbi.nlm.nih.gov/35835488/) | 2022 | Case Report | BMJ Case Reports | Disseminated strongyloidiasis following prolonged corticosteroid therapy — Ivermectin used for strongyloidiasis (its known antiparasitic indication). Oesophageal candidiasis was a concurrent opportunistic infection in an immunocompromised host, not treated by Ivermectin. Retrieved for Rank 2 (Esophageal Candidiasis). |
| [10098288](https://pubmed.ncbi.nlm.nih.gov/10098288/) | 1999 | Case Report | Australasian Journal of Dermatology | Two immunocompromised children with crusted scabies treated successfully with oral Ivermectin 200 µg/kg. One child had chronic mucocutaneous candidiasis as an underlying immune condition — this was not the treatment target. Retrieved for Rank 6 (Congenital Candidiasis). |

> **Interpretation for clinical readers:** These are the only two publications the evidence pipeline could associate with Ivermectin and any of the 10 predicted indications. Neither describes antifungal use of Ivermectin. They should not be cited as evidence of efficacy for candidiasis or any related indication.

---

## Australia Market Information

No ARTG entries were returned by the automated data pipeline for Ivermectin. As noted above, this is likely a data collection gap rather than a true regulatory absence. Healthcare professionals requiring prescribing information should consult:

- [TGA ARTG Public Summary](https://www.tga.gov.au/resources/artg) — search by active ingredient "ivermectin"
- [TGA Product Information](https://www.ebs.tga.gov.au/) — for approved indications and full PI documents
- PBS Schedule — Ivermectin is listed on the PBS for scabies

---

## All Predicted Indications — Summary

Given that all 10 predicted indications carry the same evidence level and recommendation, the following table provides a consolidated view to assist clinical prioritisation.

| Rank | Indication | TxGNN Score | Trials | Literature | Evidence | Decision | KG Artefact Assessment |
|------|-----------|-------------|--------|-----------|----------|----------|----------------------|
| 1 | Vulvovaginal Candidiasis | 99.95% | 0 | 0 | L5 | Hold | Yes — no antifungal mechanism |
| 2 | Esophageal Candidiasis | 99.73% | 0 | 1* | L5 | Hold | Yes — cited paper treats strongyloidiasis, not candidiasis |
| 3 | Anogenital HPV Infection | 99.48% | 0 | 0 | L5 | Hold | Yes — no anti-HPV mechanism; geographic KG co-occurrence |
| 4 | Vulvovaginitis | 99.36% | 0 | 0 | L5 | Hold | Yes — minimal isolated preclinical signal (*Trichomonas*); no clinical data |
| 5 | Candida glabrata | 99.25% | 0 | 0 | L5 | Hold | Yes — no antifungal mechanism for this azole-resistant species |
| 6 | Congenital Candidiasis | 99.25% | 0 | 1* | L5 | Hold | Yes — cited paper treats scabies, not candidiasis |
| 7 | Neonatal Candidiasis | 99.25% | 0 | 0 | L5 | Hold | Yes — no mechanism; Ivermectin generally avoided in neonates (<15 kg) |
| 8 | Postmenopausal Atrophic Vaginitis | 99.18% | 0 | 0 | L5 | Hold | Yes — non-infectious; no plausible mechanism |
| 9 | Candidiasis, Invasive | 99.16% | 0 | 0 | L5 | Hold | Yes — no systemic antifungal mechanism; plasma levels far below any antifungal threshold |
| 10 | Vulvitis | 98.98% | 0 | 0 | L5 | Hold | Yes — lowest score; no mechanism or evidence |

*\* Literature retrieved is a KG co-indication mismatch (see Literature Evidence section)*

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for complete safety information.

One safety point is directly relevant to evaluating the lower-ranked predictions: Ivermectin is **generally contraindicated or requires extreme caution in neonates and children weighing less than 15 kg**, which substantially increases the risk profile for the Rank 7 prediction (Neonatal Candidiasis) and adds clinical implausibility beyond the mechanistic concerns already identified.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN predictions lack mechanistic plausibility, clinical trial support, and peer-reviewed efficacy evidence; the prediction cluster is consistent with a Knowledge Graph co-occurrence artefact arising from the epidemiological overlap between parasitic infections and opportunistic fungal/viral infections in immunocompromised populations, not a genuine therapeutic signal.

**For this candidate to be reconsidered, the following would be required:**

- Demonstration of in vitro antifungal or anti-HPV activity for Ivermectin at **clinically achievable plasma concentrations** (general oral dosing achieves ~30–50 ng/mL Cmax; any putative antifungal activity would need to be active at this range)
- A mechanistically coherent hypothesis — distinct from GluCl channel binding — linking Ivermectin to fungal or viral pathobiology
- At minimum, a pilot Phase 2 clinical trial showing efficacy in any of the predicted indications
- Resolution of the ARTG data gap: manual verification of Ivermectin's current TGA registration status and approved indications to inform the regulatory baseline for any repurposing pathway
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

