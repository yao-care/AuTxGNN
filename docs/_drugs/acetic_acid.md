---
layout: default
title: Acetic Acid
parent: Model Prediction Only (L5)
nav_order: 20
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Acetic Acid: predicted new indication Post-bacterial disorder (evidence level L5). Approved use: Otitis externa"
---

# Acetic Acid
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

# Acetic Acid: From Otitis Externa to Post-Bacterial Disorder

## One-Sentence Summary

Acetic acid is a topical antiseptic and acidifying agent, originally used for otitis externa and external ear disease.
The TxGNN model predicts it may be effective for **post-bacterial disorder**, but there are **0 clinical trials** and **0 publications** supporting this specific prediction.
The prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Otitis externa; external ear disease |
| Predicted New Indication | Post-bacterial disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, acetic acid is a weak organic acid used topically as an antiseptic. It acidifies the local environment and has antibacterial and antifungal activity, which is the basis for its use in otitis externa.

Post-bacterial disorders are generally immune-mediated or post-infectious sequelae, rather than active infections. A local antibacterial and acidifying action has no clear link to these conditions, and the category is also vague. The high model score probably reflects the drug's association with bacterial infection in the knowledge graph rather than a demonstrated therapeutic mechanism. This prediction is therefore weak.

Of the other nine predictions, **tinea corporis** has the most supporting material. Topical acetic acid has plausible antifungal activity against dermatophytes. That evidence is indirect and of low quality, as described below.

## Clinical Trial Evidence

Currently no related clinical trials registered for post-bacterial disorder. No trials were found for any of the ten predicted indications.

## Literature Evidence

Currently no related literature available for post-bacterial disorder.

For the top-ranked prediction, nothing is available. The two predictions with literature are summarised below for context.

**Tinea corporis (rank 9, evidence level L4)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20256868](https://pubmed.ncbi.nlm.nih.gov/20256868/) | 1947 | Historical case series | Urol Cutaneous Rev | Larger series of tinea capitis treated with iodine and dilute acetic acid; uncontrolled, combination treatment |
| [20996178](https://pubmed.ncbi.nlm.nih.gov/20996178/) | 1946 | Historical clinical report | JAMA | Tinea capitis treated with iodine and dilute acetic acid |
| [20983383](https://pubmed.ncbi.nlm.nih.gov/20983383/) | 1946 | Historical clinical report | Arch Dermatol Syphilol | Tinea capitis treated with iodine and dilute acetic acid |
| [13616002](https://pubmed.ncbi.nlm.nih.gov/13616002/) | 1958 | Historical clinical report | Vestn Dermatol Venerol | Foot epidermophytosis treated with graded acetic acid concentrations |
| [31049344](https://pubmed.ncbi.nlm.nih.gov/31049344/) | 2019 | Clinical report | Skin Appendage Disord | Chemical peeling as an alternative to oral antifungals for onychomycosis in special circumstances |
| [26857689](https://pubmed.ncbi.nlm.nih.gov/26857689/) | 2016 | In vitro study | Mycoses | Topical antifungal products compared in an in vitro onychomycosis model |
| [16233325](https://pubmed.ncbi.nlm.nih.gov/16233325/) | 2002 | In vitro study | J Biosci Bioeng | Fermented herb product showed antifungal activity against tinea, likely via organic acids at low pH |
| [33625606](https://pubmed.ncbi.nlm.nih.gov/33625606/) | 2021 | In vitro study | World J Microbiol Biotechnol | Lactobacillus plantarum strain inhibited Trichophyton rubrum growth |
| [37256034](https://pubmed.ncbi.nlm.nih.gov/37256034/) | 2023 | Case series | Arch Plast Surg | Burns caused by Korean folk remedies; a safety signal for unsupervised skin use |

One further retrieved paper (PMID 30941788) is an analytical chemistry study unrelated to efficacy and is not listed.

**Post-infectious syndrome (rank 3, evidence level L5)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20848144](https://pubmed.ncbi.nlm.nih.gov/20848144/) | 2011 | Systematic review | J Gastroenterol | Animal models of post-infectious IBS; background only, does not involve acetic acid as therapy |

## Australia Market Information

Three valid single-ingredient licence entries are recorded (102J, 710J and 101H). Product names, dosage forms and approved indication text were not available in the data compiled for this report, so a product table cannot be provided.

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: inherited porphyria, porphyrin metabolism disease, porphyria, herpes simplex infection, and geniculate herpes zoster. These should be checked against the TGA-approved Product Information (PI).
- **Skin safety signal**: a 2023 case series reports burns from folk remedies, which indicates a risk with unsupervised or concentrated acetic acid on skin.
- **Eye use**: use near the eye at non-ophthalmic concentrations carries irritation and corneal injury risk.
- **Drug Interactions**: no interactions were found in the queried database.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is supported by model output only (evidence level L5), with no trials or literature, and no plausible mechanistic link between a topical antiseptic and a post-infectious or immune-mediated sequela. All ten predictions are rated L5 except tinea corporis (L4), which is a research question rather than a candidate for adoption.

**To proceed, the following is needed:**
- Mechanism of action data for acetic acid
- A clearer definition of "post-bacterial disorder" and a credible biological rationale
- Product names, dosage forms, routes and approved indications for the three ARTG entries
- TGA PI warnings and contraindications
- For tinea corporis, controlled studies of defined acetic acid concentrations, with a safety assessment of skin irritation and burns
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

