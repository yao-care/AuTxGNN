---
layout: default
title: Cefazolin
parent: Model Prediction Only (L5)
nav_order: 141
evidence_level: L5
indication_count: 8
monitor_inn: "Cefazolin"
predicted_indications: ["infectious otitis media", "bronchitis", "middle ear disease", "chronic otitis media", "suppurative otitis media", "otosalpingitis", "non-suppurative otitis media", "allergic otitis media"]
last_modified_at: 2026-11-24
description: "Cefazolin: predicted new indication infectious otitis media (evidence level L5). In Australia: 6 PBS items (6 currently listed)"
---

# Cefazolin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Cefazolin: first-generation cephalosporin (bacterial cell wall synthesis inhibitor) → infectious otitis media
{: .text-alpha }

## One-Sentence Summary

Cefazolin is a first-generation cephalosporin antibiotic that inhibits bacterial cell wall synthesis. The TxGNN model predicts it may be useful for **infectious otitis media**, but **no clinical trials** and only **2 publications** were retrieved for this disease, and neither directly tests cefazolin as a treatment for it. The prediction is currently supported mainly by the model score and a plausible antibacterial mechanism.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | infectious otitis media |
| TxGNN Prediction Score | 0.9944 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (6 of 6 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 6 (valid: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for cefazolin: "Cefazolin is an antibacterial drug. […] Cefazolin is a bactericidal agent that acts by inhibition of bacterial cell wall synthesis." ([DailyMed: Cefazolin (cefazolin sodium) prescribing information, Baxter Healthcare Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d91a8d13-99a0-4d87-88dc-71cbd37922b4), label version 2026-08-31; accessed 2026-11-19.) Cefazolin belongs to the first-generation cephalosporins, which bind penicillin-binding proteins and inhibit bacterial cell wall synthesis. It is active against Gram-positive organisms such as streptococci and staphylococci, which can cause otitis media.

There are important limits. Cefazolin has weak activity against *Haemophilus influenzae* and *Moraxella catarrhalis*, two of the other major otitis media pathogens. Established agents are also available for this condition. The mechanism is therefore plausible but only partly matched to the usual pathogens.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Case report/series | Annals of Otology, Rhinology & Laryngology | Ceftazidime-cefazolin empiric therapy in paediatric Gradenigo syndrome, a rare complication of acute otitis media; case-level observation only |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Review | Clinical Pharmacy | Management of Stevens-Johnson syndrome; otitis media appears only as a background illness in the case, so it is not relevant to this indication |

Neither publication studies cefazolin as a treatment of infectious otitis media itself. Neither therefore meets the standard for direct evidence, and the evidence level is L5.

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 1797N | Cefazolin-AFT | Cefazolin | Powder for injection 1 g (as sodium) | Valid |
| 1799Q | Cefazolin-AFT | Cefazolin | Powder for injection 1 g (as sodium) | Valid |
| 12115P | Cephazolin Viatris | Cefazolin | Powder for injection 2 g (as sodium) | Valid |
| 12118T | Cephazolin Viatris | Cefazolin | Powder for injection 2 g (as sodium) | Valid |
| 14694J | Cephazolin Viatris | Cefazolin | Powder for injection 2 g (as sodium) | Valid |
| 14698N | Cefazolin-AFT | Cefazolin | Powder for injection 1 g (as sodium) | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

The product is a single-ingredient injectable and its licence is valid.

## Safety Considerations

- **Drug Interactions**: Interaction screening returned 100 entries. Moderate-level interactions include the aminoglycosides kanamycin, neomycin and streptomycin, and picosulfuric acid. Other entries, such as amphotericin B, are of unknown severity.

For warnings and contraindications, please refer to the TGA-approved Product Information (PI).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The score is high (0.9944), but no trials exist and the only retrieved studies do not directly test cefazolin in this disease. The spectrum gap against *H. influenzae* and *M. catarrhalis*, together with existing standard therapy, argues against prioritising this indication now.

**To proceed, the following is needed:**
- Direct clinical data for cefazolin in infectious otitis media, such as comparative studies against standard therapy
- Local susceptibility data for the main otitis media pathogens
- Detailed mechanism of action data
- Review of the TGA Product Information for warnings and contraindications

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Cefazolin (cefazolin sodium) prescribing information, Baxter Healthcare Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d91a8d13-99a0-4d87-88dc-71cbd37922b4) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

