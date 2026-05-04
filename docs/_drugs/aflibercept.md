---
layout: default
title: Aflibercept
parent: 僅模型預測 (L5)
nav_order: 26
evidence_level: L5
indication_count: 10
---

# Aflibercept
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

# Aflibercept: From Wet Age-Related Macular Degeneration to Esotropia

## One-Sentence Summary

Aflibercept is a recombinant fusion protein (VEGF trap) broadly recognised for treating neovascular (wet) age-related macular degeneration, diabetic macular edema, and metastatic colorectal cancer, acting by blocking VEGF-A, VEGF-B, and placental growth factor (PlGF).
The TxGNN model assigns its highest prediction score to **Esotropia (inward convergent strabismus)** at **99.38%**,
however **zero clinical trials** and **zero publications** currently support this specific repurposing direction, and the mechanistic rationale is considered biologically weak.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Neovascular (wet) AMD, diabetic macular edema, macular edema following retinal vein occlusion, metastatic colorectal cancer (general knowledge; no ARTG entry data available in current evidence pack) |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| Australia Market Status | No ARTG registration found — **data requires manual TGA verification** |
| Number of ARTG Entries | 0 (per current dataset — see note below) |
| Recommended Decision | Hold |

> ⚠️ **Data Quality Note:** This evidence pack carries candidate ID `TW-DB08885-multi` and appears to contain Taiwan regulatory data rather than Australian TGA/ARTG data. Aflibercept (Eylea®) is widely understood to hold regulatory approval in multiple high-income countries. Australian healthcare professionals should independently verify current ARTG registration status at [TGA ARTG Public Summary](https://www.tga.gov.au/resources/artg).

---

## Why is This Prediction Reasonable?

Aflibercept functions as a recombinant "VEGF trap" — a fusion protein combining the ligand-binding domains of VEGFR-1 and VEGFR-2 with the Fc portion of human IgG1. By acting as a high-affinity decoy receptor, it binds and neutralises VEGF-A, VEGF-B, and PlGF, thereby blocking downstream angiogenesis signalling. This mechanism underlies its efficacy across neovascular retinal diseases and VEGF-dependent tumours.

Esotropia, by contrast, is a form of strabismus characterised by inward deviation of one or both eyes. The primary aetiology involves imbalance of the extraocular muscles or aberrant neuromuscular innervation — neither of which has a recognised direct connection to the VEGF signalling axis. The repurposing rationale analysis in this evidence pack concludes that the TxGNN high score most likely reflects an **indirect knowledge graph connection through shared "ophthalmic disease" nodes**, rather than genuine mechanistic overlap.

The sole theoretical bridge between Aflibercept and esotropia comes from an **adverse event observation**: premature infants who develop retinopathy of prematurity (ROP) and receive intravitreal anti-VEGF therapy (including Aflibercept) have a documented higher rate of subsequent strabismus development. This represents a **treatment complication**, not a therapeutic mechanism — and it argues against, not for, using Aflibercept to treat esotropia.

---

## Clinical Trial Evidence

No clinical trials specifically investigating Aflibercept for esotropia are currently registered.

> Currently no related clinical trials registered.

---

## Literature Evidence

No publications specifically investigating Aflibercept for esotropia are currently indexed.

> Currently no related literature available.

---

## Australia Market Information

No ARTG registration data was retrieved for Aflibercept in this evidence pack. Manual verification against the TGA ARTG is required before any clinical or regulatory decision-making.

> Currently no ARTG entries available in this dataset. Please verify directly at [www.tga.gov.au/resources/artg](https://www.tga.gov.au/resources/artg).

---

## Cytotoxicity

Aflibercept (as Zaltrap®) is approved for use in metastatic colorectal cancer (mCRC) in combination with FOLFIRI chemotherapy. It meets the antineoplastic criteria (antiangiogenic mechanism; oncology-approved indication).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — antiangiogenic VEGF trap (biologic; not a conventional cytotoxic agent) |
| Myelosuppression Risk | Low as monotherapy; **High** when combined with FOLFIRI (neutropenia and leukopenia are dose-limiting in the mCRC regimen — monitor closely) |
| Emetogenicity Classification | Low |
| Monitoring Items | Full blood count (FBC) with differential, liver function tests, renal function, urinalysis (proteinuria), blood pressure |
| Handling Protection | As a biologic agent, standard aseptic preparation precautions apply; not classified as a conventional cytotoxic requiring specialised cytotoxic handling suite, but facility-specific policies should be followed |

---

## Safety Considerations

No safety data (key warnings, contraindications, or drug interactions) was available in this evidence pack. All fields returned as data gaps.

> Please refer to the TGA-approved Product Information (PI) for Eylea® (ophthalmic use) and/or Zaltrap® (oncology use) for complete safety information. PI documents are available via the TGA website.

---

## Predicted Indication Summary: All Candidates

The TxGNN model generated 10 candidate repurposing indications for Aflibercept. All carry an **L5 evidence level** (model prediction only) with no supporting clinical or preclinical studies retrieved. A brief mechanistic quality assessment is provided below:

| Rank | Indication | Score | Mechanistic Rationale Quality | Recommendation |
|------|-----------|-------|-------------------------------|----------------|
| 1 | Esotropia | 99.38% | ❌ No VEGF link — likely KG artefact | Hold |
| 2 | Esophageal varices (without bleeding) | 97.56% | ✅ Biologically plausible — VEGF drives portal hypertension neovascularisation | Research Question |
| 3 | Esophageal varices (with bleeding) | 97.56% | ⚠️ Plausible mechanism but acute haemorrhage setting raises serious safety concerns | Hold |
| 4 | Varicose disease | 96.95% | ⚠️ Partial match — VEGF-A/B role in venous remodelling; VEGF-C/D (via VEGFR3) not blocked by Aflibercept | Research Question |
| 5 | Urethral calculus | 95.97% | ❌ No VEGF link — likely KG artefact | Hold |
| 6 | Adenosine deaminase deficiency | 95.76% | ❌ Metabolic/genetic disease; no VEGF connection | Hold |
| 7 | Hemorrhagic disease of newborn | 95.56% | ❌ Vitamin K deficiency mechanism; no VEGF connection | Hold |
| 8 | Ectomesenchymoma | 94.52% | ✅ Tumour angiogenesis VEGF mechanism applicable (ultra-rare tumour) | Research Question |
| 9 | Malignant cutaneous granular cell skin tumour | 94.51% | ✅ Soft tissue sarcoma — VEGF/PlGF mechanism plausible | Research Question |
| 10 | Middle ear neuroendocrine tumour | 94.42% | ✅ Highly vascular NET; consistent with anti-VEGF class mechanism | Research Question |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (esotropia at 99.38%) lacks any credible mechanistic basis, has zero supporting clinical trials or publications, and the biological connection most likely reflects a knowledge graph artefact rather than genuine pharmacological insight. A "Hold" decision is appropriate for the primary predicted indication.

**Before this candidate can progress, the following is needed:**

- **Verify Australian market status:** Confirm current ARTG registration for Eylea® and Zaltrap® directly via TGA ARTG to resolve the data gap in this evidence pack
- **Retrieve Aflibercept MOA data from DrugBank (DG002):** Required to complete mechanistic rationale analysis across all 10 predicted indications
- **Retrieve TGA Product Information warnings and contraindications (DG001):** Blocking data gap that prevents safety pre-screening
- **Re-evaluate Rank 2 (Esophageal Varices without Bleeding):** This is the most biologically plausible indication — a targeted literature search and exploratory review of portal hypertension animal model data is recommended as a priority next step
- **Prioritise oncology candidates (Ranks 8–10):** Ectomesenchymoma, malignant granular cell tumour, and middle ear NET all share mechanistic overlap with Aflibercept's approved oncology mechanism; rare disease orphan pathways may be worth exploring

---

*This report is generated for research purposes only and does not constitute medical advice. All repurposing candidates require prospective clinical validation before therapeutic application. For clinical decisions, refer to TGA-approved Product Information.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

