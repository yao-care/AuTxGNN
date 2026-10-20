---
layout: default
title: Tolnaftate
parent: Model Prediction Only (L5)
nav_order: 736
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Tolnaftate: predicted new indication Majocchi granuloma (evidence level L5). Approved use: Tinea pedis, tinea corporis, tinea infection, pityriasis versicolor…"
monitor_inn: "Tolnaftate"
predicted_indications: ["Majocchi granuloma", "ectothrix infectious disease", "endothrix infectious disease", "ophthalmic herpes zoster", "orbital cellulitis", "skin disease caused by infection", "infectious mononucleosis"]
---

# Tolnaftate
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

# Tolnaftate: From Tinea Infections to Superficial Mycosis

## One-Sentence Summary

Tolnaftate is a topical antifungal originally used for dermatophyte infections of the skin such as tinea pedis, tinea corporis and pityriasis versicolor.
The TxGNN model's top-ranked prediction is **Majocchi granuloma** (score 98.6%), but this has no supporting studies. The best-supported prediction is **Superficial Mycosis**, which is essentially an on-label or near-label category, with **15 publications** (mostly 1960s to 1970s clinical studies) and **no registered clinical trials**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tinea pedis, tinea corporis, tinea infection, pityriasis versicolor, dermatophytosis of the groin and perianal area, tinea manuum, tinea barbae, dermatophytosis of the scalp or beard (the approved indication text on the ARTG entry was not available) |
| Predicted New Indication | Majocchi granuloma (rank 1, no evidence); the best-supported prediction is superficial mycosis (rank 5) |
| TxGNN Prediction Score | 98.59% (Majocchi granuloma); 98.48% (superficial mycosis) |
| Evidence Level | L5 for Majocchi granuloma; L3 for superficial mycosis |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold (Majocchi granuloma); Research Question for superficial mycosis |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the supporting literature, tolnaftate is a thiocarbamate antifungal that inhibits fungal squalene epoxidase, reducing ergosterol production. Its efficacy in dermatophyte infections of the skin is established.

**Majocchi granuloma** (the top prediction) is a deep follicular and perifollicular dermatophyte infection, most commonly caused by *Trichophyton rubrum*. The causative organisms overlap with tolnaftate's approved tinea indications, so the prediction is biologically plausible. However, topical tolnaftate penetrates poorly into hair follicles and the dermis, and deep folliculitis generally needs systemic antifungal therapy. The same limitation applies to ectothrix and endothrix infections and to tinea profunda. No clinical evidence was found for any of these.

**Superficial mycosis** covers dermatophytosis and related skin infections, which is the core of tolnaftate's existing use. This is therefore closer to confirmation of known use than to true repurposing.

Several other high-ranking predictions are unlikely to be genuine. Ophthalmic herpes zoster and infectious mononucleosis are viral diseases, and orbital cellulitis is usually bacterial. Tolnaftate has no known antiviral or antibacterial activity, so these look like network artefacts. The cutaneous candidiasis prediction (score 98.5%) is also doubtful, because tolnaftate has poor and inconsistent activity against *Candida* species, which are usually treated with azoles or polyenes.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Literature for the best-supported prediction, superficial mycosis:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10398626](https://pubmed.ncbi.nlm.nih.gov/10398626/) | 1999 | Systematic review | BMJ | Efficacy and cost-effectiveness of topical treatments for fungal infections of the skin and nails of the feet |
| [1090684](https://pubmed.ncbi.nlm.nih.gov/1090684/) | 1975 | Placebo-controlled trial | J Invest Dermatol | Griseofulvin, tolnaftate and placebo compared in topical therapy of superficial dermatophytoses |
| [4619464](https://pubmed.ncbi.nlm.nih.gov/4619464/) | 1974 | Double-blind comparative trial | Postgrad Med J | Clotrimazole compared with tolnaftate in superficial dermatophytoses |
| [1379146](https://pubmed.ncbi.nlm.nih.gov/1379146/) | 1992 | Review | Drugs | Diagnosis and treatment recommendations for superficial fungal skin infections |
| [778288](https://pubmed.ncbi.nlm.nih.gov/778288/) | 1976 | Review | J Invest Dermatol | Tolnaftate described as a major advance in treating dermatophytosis |
| [16989127](https://pubmed.ncbi.nlm.nih.gov/16989127/) | 2006 | Review | Therapie | Overview of topical antifungal agents |
| [5844107](https://pubmed.ncbi.nlm.nih.gov/5844107/) | 1965 | Clinical study | Am J Dis Child | Tolnaftate in superficial fungal infections |
| [14288003](https://pubmed.ncbi.nlm.nih.gov/14288003/) | 1964 | Clinical study | Antimicrob Agents Chemother | Effect of tolnaftate in superficial fungal infections |
| [14288002](https://pubmed.ncbi.nlm.nih.gov/14288002/) | 1964 | Clinical study | Antimicrob Agents Chemother | Effect of tolnaftate on superficial mycotic infections |
| [4563192](https://pubmed.ncbi.nlm.nih.gov/4563192/) | 1972 | Clinical study | Southeast Asian J Trop Med Public Health | Tolnaftate in superficial mycotic infections |

These studies are older and vary in quality. They support clinical activity, but phase and full design details cannot be confirmed from the titles alone.

**Other predictions:**
- **Skin disease caused by infection:** Recent reviews of tinea pedis (PMID [37415917](https://pubmed.ncbi.nlm.nih.gov/37415917/), 2023) and dermatomycoses (PMID [38874607](https://pubmed.ncbi.nlm.nih.gov/38874607/), 2024) list tolnaftate among topical antifungals active against dermatophytes. An in vitro study ([32653607](https://pubmed.ncbi.nlm.nih.gov/32653607/), 2020) found tolnaftate inhibits ergosterol production in *Leishmania*. This is a preclinical lead only. Many other papers concern different antifungals and are indirect.
- **Cutaneous candidiasis:** The literature is indirect, consisting of topical antifungal reviews and old clotrimazole comparisons. PMID [6459255](https://pubmed.ncbi.nlm.nih.gov/6459255/) (1981) compared two combination creams, one of which contained tolnaftate, and does not show efficacy of tolnaftate alone.
- **Majocchi granuloma, ectothrix infection, endothrix infection, tinea profunda, ophthalmic herpes zoster, orbital cellulitis, infectious mononucleosis:** Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 4481W | Tinaderm | Spray aerosol 0.7 mg per g (0.07%), 100 g | Not available in the data compiled for this report |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No drug interactions were identified in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold** for Majocchi granuloma and the other novel predictions. **Research Question** for superficial mycosis.

**Rationale:**
- The top-ranked prediction, Majocchi granuloma, has only model support (L5). Topical tolnaftate is unlikely to reach the site of infection, and systemic antifungals are the standard of care.
- Superficial mycosis has the strongest support (L3), but it largely restates tolnaftate's existing use, so it offers little true repurposing value.
- The viral and bacterial predictions (ophthalmic herpes zoster, infectious mononucleosis, orbital cellulitis) have no plausible mechanism and should not be pursued.

**To proceed, the following is needed:**
- The TGA-approved Product Information, including the approved indication text, warnings and contraindications
- Detailed mechanism of action data (for example, from DrugBank)
- For deep dermatophyte infections, data on skin and follicular penetration, or a systemic or combination formulation
- A critical appraisal of the older controlled studies (PMIDs 1090684 and 4619464) to confirm their design and quality
- For *Leishmania*-related skin disease, confirmatory preclinical work before any clinical consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

