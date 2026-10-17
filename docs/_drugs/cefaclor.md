---
layout: default
title: Cefaclor
parent: Model Prediction Only (L5)
nav_order: 140
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Cefaclor: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Not stated in the Australian licence data. The knowledge graph lists…"
monitor_inn: "Cefaclor"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "gonococcal urethritis", "Ureaplasma urethritis", "congenital analbuminemia", "blood group incompatibility", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "premalignant hematological system disease", "monoclonal gammopathy"]
---

# Cefaclor
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Cefaclor: From Bacterial Infections to Hyperamylasemia (Top Prediction) and Gonococcal Urethritis (Best-Supported Prediction)

## One-Sentence Summary

Cefaclor is an oral second-generation cephalosporin antibiotic, originally used for respiratory, urinary tract and other bacterial infections.
The TxGNN model's top-ranked prediction is **hyperamylasemia**, but it has **no clinical trials and no publications**, and no plausible mechanism.
The best-supported prediction in the list is **gonococcal urethritis** (rank 3), with **6 publications** (1979-1997) but **no registered clinical trials**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Australian licence data. The knowledge graph lists urinary tract infection, tonsillitis, pharyngitis, pneumonia and other bacterial infections |
| Predicted New Indication | Hyperamylasemia (top-ranked); gonococcal urethritis (best-supported) |
| TxGNN Prediction Score | Hyperamylasemia 97.70%; gonococcal urethritis 97.48% |
| Evidence Level | L5 for hyperamylasemia; L3 for gonococcal urethritis |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold (hyperamylasemia); Hold, historical research question only (gonococcal urethritis) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Cefaclor is known to be a beta-lactam cephalosporin that inhibits bacterial cell-wall synthesis by binding penicillin-binding proteins.

**Hyperamylasemia (rank 1):** No plausible mechanistic link to a cell-wall synthesis inhibitor is evident. The score appears to be a graph-based computational artefact. The same applies to the other non-infectious predictions (polyclonal hyperviscosity syndrome, congenital analbuminemia, blood group incompatibility, premalignant haematological disease, monoclonal gammopathy).

**Gonococcal urethritis (rank 3):** This is the only prediction with strong biological plausibility. *Neisseria gonorrhoeae* is a susceptible organism class, and it is closely related to cefaclor's existing urinary and genitourinary infection indications. However, current guidelines prefer ceftriaxone-based therapy and resistance trends limit modern applicability, so the evidence is historical rather than actionable.

**Other predictions of note:**
- *Ureaplasma urethritis* (rank 4): Ureaplasma lacks a cell wall, so beta-lactams are expected to be ineffective. The prediction is mechanistically contradicted.
- *Uterine inflammatory disease* (rank 7) and *xanthogranulomatous pyelonephritis* (rank 8): Some indirect plausibility for bacterial causes, but no supporting data, and cefaclor's spectrum is narrow for polymicrobial and anaerobic infections.

## Clinical Trial Evidence

Currently no related clinical trials registered, for either hyperamylasemia or gonococcal urethritis.

## Literature Evidence

No literature is available for hyperamylasemia. For the best-supported prediction, gonococcal urethritis:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6225482](https://pubmed.ncbi.nlm.nih.gov/6225482/) | 1983 | Comparative clinical study (randomised allocation) | Br J Vener Dis | 400 men randomised to four regimens. Cure rates: spectinomycin 98.9%, cefaclor 3 g + probenecid 95.8%, cefaclor 3 g alone 89.6%, cefamandole + probenecid 70.8% |
| [116373](https://pubmed.ncbi.nlm.nih.gov/116373/) | 1979 | Randomised trial / case series | Sex Transm Dis | Cefaclor 2, 3 and 4 g daily for 3 days, with or without probenecid, in men with uncomplicated gonococcal urethritis |
| [121455](https://pubmed.ncbi.nlm.nih.gov/121455/) | 1979 | Clinical study | Postgrad Med J | 40 men with uncomplicated gonococcal urethritis treated with a 1 g cefaclor loading dose regimen; good in vitro activity against *N. gonorrhoeae* |
| [9582471](https://pubmed.ncbi.nlm.nih.gov/9582471/) | 1997 | Clinical study | Genitourin Med | Reassessed in vivo and in vitro efficacy of cefaclor as an alternative to third-generation cephalosporins in the developing world |
| [6400040](https://pubmed.ncbi.nlm.nih.gov/6400040/) | 1984 | Clinical study | Med J Malaysia | Single-dose oral cefaclor in men with uncomplicated gonococcal urethritis (no abstract available) |
| [2673664](https://pubmed.ncbi.nlm.nih.gov/2673664/) | 1989 | Clinical experience report (different drug) | Curr Med Res Opin | Primarily about cefetamet pivoxil; cefaclor used as a comparator. Indirect relevance only |

Study designs were not fully verified; these are small, older studies.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1169M | Ceclor CD | Tablet (sustained release) 375 mg (as monohydrate) | Not available in the data compiled for this report |

## Safety Considerations

- **Contraindications (from knowledge graph, not label text):** Clostridium difficile colitis; perinatal necrotizing enterocolitis.
- **Drug Interactions:** 69 interactions were identified. Moderate-level interactions include balsalazide, picosulfuric acid, magnesium hydroxide and aluminium hydroxide. Other listed interactions (severity unknown) include calcitriol, pantoprazole, mesalazine, doxycycline, morphine, metformin, omeprazole, lansoprazole, cimetidine and several corticosteroids.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (hyperamylasemia) rests on a graph score alone, with no trials, no literature and no plausible mechanism. Gonococcal urethritis has historical clinical reports, but they are small and old, and current guidelines favour ceftriaxone, so it is not an actionable repurposing opportunity.

**To proceed, the following is needed:**
- Mechanism of action data (currently a data gap)
- Approved indication text and PI warnings and contraindications for the Australian product
- For gonococcal urethritis: contemporary Australian susceptibility data and a comparison with current guideline therapy
- For hyperamylasemia: any clinical or mechanistic rationale; otherwise, deprioritise
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

