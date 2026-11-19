---
layout: default
title: Phenoxymethylpenicillin
parent: Model Prediction Only (L5)
nav_order: 569
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-20
monitor_inn: "Phenoxymethylpenicillin"
predicted_indications: ["epiglottitis", "laryngitis"]
description: "Phenoxymethylpenicillin: predicted new indication Epiglottitis (evidence level L5). In Australia: 18 PBS items (18 currently listed)"
---

# Phenoxymethylpenicillin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Phenoxymethylpenicillin: Epiglottitis
{: .text-alpha }

## One-Sentence Summary

Phenoxymethylpenicillin (penicillin V) is an oral penicillin antibiotic, originally used for streptococcal and staphylococcal infections, pharyngitis, otitis media, erysipelas and scarlet fever.
The TxGNN model predicts it may be effective for **epiglottitis**, but there are **no clinical trials** and **no publications** supporting this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (18 of 18 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 18 (valid: 18) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for phenoxymethylpenicillin: "Penicillin V exerts a bactericidal action against penicillin-sensitive microorganisms during the stage of active multiplication. It acts through the inhibition of biosynthesis of cell-wall mucopeptide. It is not active against the penicillinase-producing bacteria, which include many strains of staphylococci." ([DailyMed: penicillin v potassium prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ceddc406-4a17-471f-917e-63b4b03779ea), label version 2026-11-12; accessed 2026-11-19.) Based on known information, phenoxymethylpenicillin is a penicillin-class antibiotic with proven activity against streptococci. Mechanistically it may apply to bacterial infections of the upper airway.

Epiglottitis is often caused by *Haemophilus influenzae* type b, *Streptococcus pneumoniae*, group A *Streptococcus* and *Staphylococcus aureus*. Penicillin V covers the streptococcal causes, which fits its original use in throat and respiratory infections.

The fit is weak, however. Penicillin V is an oral agent with limited activity against beta-lactamase-producing *H. influenzae* and *S. aureus*. Epiglottitis is an airway emergency usually treated with intravenous broad-spectrum agents such as third-generation cephalosporins, so oral penicillin V is not a plausible primary therapy. The high score likely reflects the drug's general antibacterial class association rather than specific evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for epiglottitis.

For context, the second-ranked prediction (laryngitis) had one paper, a 1992 erythromycin study (PMID [1632252](https://pubmed.ncbi.nlm.nih.gov/1632252/)). It noted that phenoxymethylpenicillin had no effect on the clinical course of acute laryngitis. The third-ranked prediction (urinary tract infection) returned mostly off-topic papers. The one directly relevant item is [2497823](https://pubmed.ncbi.nlm.nih.gov/2497823/) (BMJ, 1989), on phenoxymethylpenicillin and erythromycin in asymptomatic bacteriuria in girls. None of this supports a new penicillin V indication.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13968E | Cilicaine VK | Capsule 250 mg phenoxymethylpenicillin (as potassium), oral | Not listed in the data compiled for this report |

---

## Safety Considerations

**Contraindication-related conditions (from the knowledge graph, not label text):** kidney disease, pyoureter, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, infectious mononucleosis, and chronic Epstein-Barr virus infection syndrome.

**Drug Interactions:** 32 interactions were identified. The main moderate-level ones are:
- Tetracyclines (doxycycline, minocycline, tetracycline)
- Warfarin and dicoumarol
- Neomycin
- Balsalazide
- Picosulfuric acid
- Radioactive iodide (I-123, I-131)

Clarithromycin is rated minor. Several others (for example omeprazole, simvastatin, prednisolone, aspirin, clopidogrel, heparin and ibuprofen) have an unknown severity level.

Please refer to the TGA-approved Product Information (PI) for warnings and full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The epiglottitis prediction has no trials or literature behind it and conflicts with standard practice. Epiglottitis is an airway emergency treated with intravenous broad-spectrum therapy, and oral penicillin V has limited coverage of the key pathogens.

**To proceed, the following is needed:**
- Mechanism of action data
- Product Information warnings and contraindications for the Australian product (currently missing)
- The approved indication text for the ARTG entry
- Clinical or microbiological evidence for penicillin V in epiglottitis, which is unlikely to be justified given current treatment standards
- Consideration of other predicted indications that are better aligned with the drug's known spectrum, supported by direct evidence

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: penicillin v potassium prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ceddc406-4a17-471f-917e-63b4b03779ea) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

