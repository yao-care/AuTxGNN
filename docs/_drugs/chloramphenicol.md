---
layout: default
title: Chloramphenicol
parent: Model Prediction Only (L5)
nav_order: 152
evidence_level: L5
indication_count: 9
monitor_inn: "Chloramphenicol"
predicted_indications: ["conjunctivitis", "diffuse scleroderma", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "punctate epithelial keratoconjunctivitis"]
last_modified_at: 2026-10-30
description: "Chloramphenicol: predicted new indication conjunctivitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Chloramphenicol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Chloramphenicol: broad-spectrum bacteriostatic antibiotic (50S ribosomal subunit inhibitor) → conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Chloramphenicol is a broad-spectrum antibiotic that blocks bacterial protein synthesis. The TxGNN model predicts it may be effective for **conjunctivitis**, but no clinical trials are registered for this indication; the direction is supported by **19 publications**, mostly reviews, commentaries and older comparative studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | conjunctivitis |
| TxGNN Prediction Score | 0.9966 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Chloramphenicol is a bacteriostatic antibiotic that inhibits the 50S ribosomal subunit and so stops bacterial protein synthesis. Detailed mechanism of action data was not available in the data compiled for this report, so this description reflects general pharmacological knowledge about the drug.

Bacterial conjunctivitis is a superficial eye infection, and a broad-spectrum antibiotic given topically is mechanistically plausible. The publications describe topical chloramphenicol as widely used for conjunctivitis in the UK and some other countries, and rarely used in the US. In practice this prediction is closer to an extension of its existing anti-infective use than a true repurposing based on a new mechanism.

An important caveat on the evidence level: the publications discuss conjunctivitis directly, but none provides a registered trial, and the studies are mostly older comparisons, reviews and commentaries. They do not firmly establish efficacy in a modern trial setting. The evidence level has therefore been set conservatively at L5 (model prediction with no registered trial support), although the publications are consistent with the prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3300139](https://pubmed.ncbi.nlm.nih.gov/3300139/) | 1987 | Open randomised comparison | Acta Ophthalmol | In acute conjunctivitis in Tanzania, fusidic acid had a higher clinical success rate (93%) than chloramphenicol (48%) and framycetin (74%); in vitro resistance was a likely factor |
| [3554881](https://pubmed.ncbi.nlm.nih.gov/3554881/) | 1987 | Single-blind randomised comparison | Acta Ophthalmol | In acute purulent conjunctivitis, clinical success was 84% with fusidic acid versus 81% with chloramphenicol; more minor side effects (stinging) with chloramphenicol (14% vs 5%) |
| [38511104](https://pubmed.ncbi.nlm.nih.gov/38511104/) | 2024 | Comparative clinical study | Curr Ther Res Clin Exp | Compares moxifloxacin with chloramphenicol for bacterial eye infections |
| [1448311](https://pubmed.ncbi.nlm.nih.gov/1448311/) | 1992 | Comparative clinical study | Pediatr Infect Dis J | Oral rifampin compared with topical chloramphenicol for eradicating conjunctival carriage of *Haemophilus influenzae* biogroup aegyptius; some children treated with topical chloramphenicol still developed Brazilian purpuric fever |
| [32959365](https://pubmed.ncbi.nlm.nih.gov/32959365/) | 2020 | Cochrane systematic review | Cochrane Database Syst Rev | Interventions for preventing ophthalmia neonatorum |
| [11270936](https://pubmed.ncbi.nlm.nih.gov/11270936/) | 2001 | Review | Drugs | Comparative review of 16 topical ophthalmic antibacterial preparations |
| [10589371](https://pubmed.ncbi.nlm.nih.gov/10589371/) | 1999 | Review | Clin Pharmacokinet | Treatment of ocular infections with topical antibacterials |
| [8800624](https://pubmed.ncbi.nlm.nih.gov/8800624/) | 1996 | Safety review | Drug Saf | Examines the debated link between ocular chloramphenicol and aplastic anaemia |
| [7498557](https://pubmed.ncbi.nlm.nih.gov/7498557/) | 1995 | Commentary | Eye (Lond) | Topical chloramphenicol: use or abuse? |
| [25833086](https://pubmed.ncbi.nlm.nih.gov/25833086/) | 2015 | Commentary | Clin Exp Ophthalmol | Over-the-counter chloramphenicol |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11112W | Chlorsig | Eye drops 5 mg per mL, 10 mL | Not recorded in the local data |

## Safety Considerations

- **Safety concerns in the literature**: A review in the data compiled for this report discusses a debated association between topical ocular chloramphenicol and aplastic anaemia. This is the main reason for recommending guardrails.
- **Conditions flagged as cautions for chloramphenicol** (from drug-disease contraindication records, not label text): kidney disease, liver disease, gallbladder disease, thrombocytopenia, anaemia (including macrocytic anaemia and aplastic anaemia), agranulocytosis, neutropenia and related congenital neutropenia syndromes, paroxysmal nocturnal haemoglobinuria, acute intermittent porphyria, optic neuritis, peripheral neuropathy and other peripheral nervous system disease.
- **Drug interactions**: 100 interactions were found. Examples with a Major rating are cisapride and naloxegol. Moderate-rated examples include sulfonylureas (glimepiride, glipizide, glyburide, chlorpropamide, acetohexamide), repaglinide, saxagliptin, simvastatin, rosuvastatin, metronidazole, aprepitant, eliglustat, nitisinone, iron, budesonide and balsalazide. Systemic exposure from eye drops is low, so the clinical relevance of these interactions for topical use is likely limited, but this should be confirmed.

Please also refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Topical chloramphenicol is already marketed in Australia as eye drops, and the publications consistently describe its use in bacterial conjunctivitis, but no registered trial supports it and the comparative studies are mostly dated. The haematological safety debate warrants guardrails.

**To proceed, the following is needed:**
- Review of the TGA-approved Product Information for the approved indication, warnings and contraindications
- Contemporary comparative data against current topical antibiotics, including resistance patterns in Australia
- A clear position on the aplastic anaemia concern and criteria for patient selection and treatment duration
- Detailed mechanism of action data to complete the mechanistic assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

