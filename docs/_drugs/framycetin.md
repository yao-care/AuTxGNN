---
layout: default
title: Framycetin
parent: Model Prediction Only (L5)
nav_order: 320
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-28
monitor_inn: "Framycetin"
predicted_indications: ["sclerosing cholangitis", "urinary tract infection (disease)", "congenital prothrombin deficiency", "Ureaplasma urethritis", "gonococcal urethritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis"]
description: "Framycetin: predicted new indication Sclerosing cholangitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Framycetin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Framycetin: Sclerosing cholangitis
{: .text-alpha }

## One-Sentence Summary

Framycetin is an aminoglycoside antibiotic, marketed in Australia as eye or ear drops (Soframycin).
The TxGNN model predicts it may be effective for **sclerosing cholangitis**,
but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 0.9966 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Framycetin belongs to the aminoglycoside class, which is bactericidal against many Gram-negative bacteria. Its efficacy is established for topical eye and ear infections, but it has not been shown to be effective for sclerosing cholangitis.

The only plausible link is the gut-liver axis. Framycetin is poorly absorbed systemically, so a gut-restricted antibiotic could in theory alter the gut microbiome, which is implicated in primary sclerosing cholangitis. This is speculative. The aminoglycoside class is not an established treatment for this disease, and the high score is a computational prediction only.

The Australian product is an ophthalmic/otic preparation. Whether any route of administration compatible with the predicted indication is available has not been assessed.

Other top-ranked predictions are also unsupported by evidence:
- **Plausible at class level (antibacterial):** urinary tract infection, gonococcal urethritis, uterine inflammatory disease, xanthogranulomatous pyelonephritis, Ureaplasma urethritis. Framycetin's poor systemic absorption makes it a poor fit, and established agents are preferred.
- **Implausible:** congenital prothrombin deficiency, genital herpes (viral) and vitamin deficiency disorder show no credible mechanistic link and likely reflect TxGNN model (deep learning) artefacts. Oral aminoglycosides may even worsen vitamin K status.

## Clinical Trial Evidence

Currently no related clinical trials registered for sclerosing cholangitis or any of the other nine predicted indications.

## Literature Evidence

No literature is available for sclerosing cholangitis.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [13316238](https://pubmed.ncbi.nlm.nih.gov/13316238/) | 1956 | Historical clinical report (design unclear) | Bruxelles Medical | "Trial therapy with new antibiotic framycetin in pneumology". No abstract available; likely an uncontrolled observation that does not meet modern evidence standards |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1440T | Soframycin | Eye or ear drops containing framycetin sulfate 5 mg per mL, 8 mL | Not available in the data compiled for this report |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

No drug interactions were found in the data compiled for this report. As an aminoglycoside, framycetin carries class-level concerns (for example ototoxicity and nephrotoxicity with systemic exposure) that should be checked against the PI before any use outside its approved route.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for sclerosing cholangitis is based only on a model score, with no trials, no literature and no clear mechanistic support (Evidence Level L5). The approved Australian product is an eye/ear drop, which is unlikely to be suitable for a hepatobiliary indication.

**To proceed, the following is needed:**
- Mechanism of action data for framycetin
- Safety information from the TGA-approved PI, including warnings and contraindications
- Original approved indication text for the ARTG entry
- Preclinical or mechanistic evidence for gut-microbiome modulation in sclerosing cholangitis
- Assessment of route and formulation compatibility (an oral or gut-restricted formulation would be needed)
- A targeted literature search, and a review of ANZCTR and other trial registries, for any relevant studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

