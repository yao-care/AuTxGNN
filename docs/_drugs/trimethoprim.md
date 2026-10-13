---
layout: default
title: Trimethoprim
parent: Model Prediction Only (L5)
nav_order: 756
evidence_level: L5
indication_count: 10
---

# Trimethoprim
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

# Trimethoprim: From Urinary Tract Infection to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Trimethoprim is an antibacterial originally used for urinary tract infections, as well as ear, eye and other infections.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**,
but **no clinical trials or publications** currently support this specific prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection, infectious otitis media, pneumocystosis, shigellosis, conjunctivitis (indication text is not recorded in the Australian licence data) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, trimethoprim is a dihydrofolate reductase (DHFR) inhibitor antibacterial. Its efficacy in bacterial infections, including conjunctivitis (usually as a topical combination with polymyxin B), is established.

Punctate epithelial keratoconjunctivitis is often viral (for example adenoviral) or inflammatory in origin. An antibacterial would not be expected to act on those causes. The high TxGNN score likely reflects network proximity to the approved conjunctivitis indications rather than a distinct mechanism. Only a possible role against secondary bacterial infection is plausible.

## Clinical Trial Evidence

Currently no related clinical trials registered for punctate epithelial keratoconjunctivitis.

## Literature Evidence

Currently no related literature available for this predicted indication.

For context, the data compiled for this report include literature on the already-established indication of conjunctivitis, which is not new evidence for the predicted indication:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19043945](https://pubmed.ncbi.nlm.nih.gov/19043945/) | 2008 | RCT | J Pediatr Ophthalmol Strabismus | Polymyxin B/trimethoprim ophthalmic solution compared with moxifloxacin for speed of clinical efficacy in bacterial conjunctivitis |
| [30007329](https://pubmed.ncbi.nlm.nih.gov/30007329/) | 2018 | Systematic review/Meta-analysis | J Pediatric Infect Dis Soc | Antibiotic treatments, including trimethoprim, for neonatal chlamydial conjunctivitis |
| [6204534](https://pubmed.ncbi.nlm.nih.gov/6204534/) | 1984 | Clinical study | Am J Ophthalmol | Trimethoprim-containing ophthalmic solutions in bacterial conjunctivitis or blepharitis |
| [8595639](https://pubmed.ncbi.nlm.nih.gov/8595639/) | 1995 | Survey | Clin Ther | Children with acute bacterial conjunctivitis treated with trimethoprim-polymyxin B ophthalmic solution |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10785P | Alprim | Tablet 300 mg (oral) | Not recorded in the data compiled for this report |

The only listed Australian product is an oral tablet. The predicted ocular indication would likely need a topical ophthalmic formulation, and no route compatibility assessment is available.

## Cytotoxicity

Not applicable. Trimethoprim is not an antineoplastic drug, so this section is omitted.

## Safety Considerations

Product Information warnings and contraindications were not available. The following come from the drug's knowledge-graph relationships and from interaction screening, and should be confirmed against the TGA-approved Product Information (PI).

- **Disease-level contraindications (knowledge graph, not label text)**: porphyria (including inherited porphyria and other porphyrin metabolism disorders), kidney disease, liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, G6PD deficiency, folic acid deficiency anaemia, *Clostridium difficile* colitis, perinatal necrotising enterocolitis, glycogen storage disease, cystinuria, galactosaemia and pyoureter.
- **Drug Interactions** (100 interactions identified; selected examples):
  - **Major**: potassium citrate, potassium bicarbonate, potassium chloride, potassium gluconate (hyperkalaemia risk).
  - **Moderate**: metformin, pioglitazone, rosiglitazone, repaglinide, balsalazide, picosulfuric acid, sapropterin.
- **Other considerations from the prediction analysis**: trimethoprim-sulfamethoxazole is a recognised cause of drug-induced vasculitis and hypersensitivity, and carries a risk of hyperkalaemia and renal effects.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials or literature behind it (L5). The proposed indication is often viral or inflammatory, so a DHFR-inhibiting antibacterial has no clear mechanistic role. The only Australian product is an oral tablet.

**To proceed, the following is needed:**
- Mechanism of action data and a clear causal link (bacterial versus viral or inflammatory aetiology) for punctate epithelial keratoconjunctivitis
- Evidence from clinical studies in this condition, including any registered trials (ClinicalTrials.gov or ANZCTR)
- Route and formulation assessment (a topical ophthalmic product versus the registered oral tablet)
- TGA Product Information warnings and contraindications to complete the safety review

## Other Predicted Indications (Brief Notes)

| Rank | Predicted Indication | Score | Evidence Level | Decision | Note |
|---|---|---|---|---|---|
| 2 | Conjunctivitis | 99.17% | L3 | Research Question | Already an original indication, so not a true repurposing candidate |
| 3 | Exposure keratitis | 98.95% | L4 | Hold | Indirect literature only. Primary management is lubrication and lid protection |
| 4 | Postinfectious vasculitis | 98.42% | L5 | Hold | Immune-mediated, and trimethoprim-sulfamethoxazole can cause vasculitis |
| 5 | Post-bacterial disorder | 98.39% | L4 | Research Question | Trials involve the trimethoprim-sulfamethoxazole combination, none meets Phase 2/3 criteria |
| 6 | Post-infectious syndrome | 98.31% | L5 | Hold | Only trial was withdrawn with no participants |
| 7 | Infective urethral stricture | 98.25% | L4 | Hold | Could address related urinary infection only, not the stricture |
| 8 | Otitis externa | 98.14% | L4 | Hold | Pseudomonas is generally resistant, with no direct human clinical evidence for trimethoprim alone |
| 9 | Chagas cardiomyopathy | 98.07% | L5 | Hold | No evidence, theoretical folate pathway rationale only |
| 10 | Infection-related haemolytic uraemic syndrome | 98.05% | L5 | Hold | Antibiotics are generally avoided in Shiga toxin-producing *E. coli* infection, which raises a safety concern |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

