---
layout: default
title: Miconazole
parent: Moderate Evidence (L3-L4)
nav_order: 475
evidence_level: L4
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "Miconazole"
predicted_indications: ["acne (disease)"]
description: "Miconazole: predicted new indication Acne (disease) (evidence level L4). In Australia: 3 PBS items (3 currently listed)"
---

# Miconazole
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

## Miconazole: Acne (disease)
{: .text-alpha }

## One-Sentence Summary

Miconazole is a topical imidazole antifungal marketed in Australia as a cream. The TxGNN model predicts it may be relevant to **acne (disease)**, but the supporting evidence is limited: **no registered clinical trials** and **4 publications**, none of which is a controlled clinical study of miconazole in acne. The evidence level is **L4**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 0.9954 |
| Evidence Level | L4 |
| Australia Market Status | Listed on the PBS Schedule (3 of 3 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for miconazole: "Miconazole is an antifungal drug. […] Miconazole inhibits the enzyme cytochrome P450 14α-demethylase which leads to inhibition of ergosterol synthesis, an essential component of the fungal cell membrane. Miconazole also affects the synthesis of triglycerides and fatty acids and inhibits oxidative and peroxidative enzymes, increasing the amount of reactive oxygen species within the cell." ([DailyMed: Oravig (miconazole) prescribing information, Galt Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=dc2427ff-e566-4b48-b289-9e51c011250a), label version 2026-01-08; accessed 2026-11-19.) Based on known information, miconazole is an imidazole antifungal, a class that inhibits fungal ergosterol synthesis and is used on the skin.

Several lines of indirect evidence link it to acne:
- **Antibacterial activity:** an in vitro study found that azole antifungals, including imidazoles, are active against *Propionibacterium acnes*, the bacterium implicated in acne vulgaris (PMID 20045949).
- **Malassezia overlap:** *Malassezia* (Pityrosporum) folliculitis is often misdiagnosed as acne vulgaris. An antifungal such as miconazole may therefore help in acne-like lesions that are in fact fungal (PMID 8593718).
- **Anti-inflammatory effects:** a review describes antibacterial and anti-inflammatory effects of miconazole on skin disorders (PMID 18627330).

These observations support a plausible hypothesis, but they do not show that miconazole treats acne itself.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18627330](https://pubmed.ncbi.nlm.nih.gov/18627330/) | 2008 | Review | Expert Opin Pharmacother | Review of miconazole's multifaceted effects on skin disorders, including antibacterial and anti-inflammatory actions |
| [15536660](https://pubmed.ncbi.nlm.nih.gov/15536660/) | 2004 | Cohort | Skin Res Technol | Split-face clinical and bioinstrumental assessment in mild inflammatory catamenial acne; limited human data |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Cohort | Clin Exp Dermatol | 62 patients with Pityrosporum folliculitis, a condition frequently misdiagnosed as acne vulgaris; diagnosis and therapeutic trials |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | In vitro | Biol Pharm Bull | Azole antifungals tested in vitro against *P. acnes* isolated from patients with acne vulgaris |

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 9027D | Daktarin | Miconazole | Cream containing miconazole nitrate 20 mg per g, 30 g | Valid |
| 9028E | Daktarin | Miconazole | Cream containing miconazole nitrate 20 mg per g, 70 g | Valid |
| 9029F | Daktarin | Miconazole | Powder containing miconazole nitrate 20 mg per g, 30 g | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions:** 100 potential interactions were identified in the interaction data compiled for this report. Examples rated Moderate include paclitaxel, fentanyl, alfentanil, acalabrutinib, nifedipine, amlodipine, amiodarone, amitriptyline, alprazolam, ethinylestradiol, estradiol and hydrocodone. Examples rated Minor include dolutegravir, loratadine and amphotericin B. Only the first 20 entries were reviewed, so this list is partial.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L4. The only literature directly on miconazole's skin effects is a review (PMID 18627330), and no clinical study has tested miconazole in acne. The other supporting papers are a small split-face study, a study of a different condition (Pityrosporum folliculitis) and an in vitro study. The prediction score is high (0.9954), but the clinical evidence is not yet enough to support progression.

**To proceed, the following is needed:**
- Controlled clinical studies of topical miconazole in acne vulgaris, ideally randomised and against standard therapy
- Mechanism of action data to support the anti-inflammatory and antibacterial hypothesis
- Review of the TGA-approved Product Information for warnings, contraindications and interactions relevant to the topical route

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Oravig (miconazole) prescribing information, Galt Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=dc2427ff-e566-4b48-b289-9e51c011250a) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

