---
layout: default
title: Benzylpenicillin
parent: Model Prediction Only (L5)
nav_order: 89
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Benzylpenicillin: predicted new indication Pericoronitis (evidence level L5). Approved use: Bacterial infections, including streptococcal, meningococcal…"
monitor_inn: "Benzylpenicillin"
predicted_indications: ["pericoronitis", "gingival recession", "canker sore", "ulcerative stomatitis", "denture stomatitis", "chemotherapy-induced oral mucositis", "leukoplakia of gingiva", "conjunctivitis", "cat-scratch disease", "chronic ethmoidal sinusitis"]
---

# Benzylpenicillin
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

# Benzylpenicillin: From Bacterial Infections to Pericoronitis

## One-Sentence Summary

Benzylpenicillin (penicillin G) is an injectable penicillin antibiotic originally used for streptococcal, meningococcal, pneumococcal and staphylococcal infections, anthrax and endocarditis.
The TxGNN model predicts it may be effective for **pericoronitis**, but there are currently **no clinical trials and no publications** supporting this prediction. The result is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections, including streptococcal, meningococcal, pneumococcal and staphylococcal infections, anthrax, endocarditis and infectious otitis media (the ARTG entry in the data compiled for this report carries no indication text; these are from the knowledge graph) |
| Predicted New Indication | Pericoronitis |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, benzylpenicillin is a beta-lactam antibiotic whose efficacy against susceptible streptococci and many anaerobic organisms is well established. Mechanistically, it may be applicable to pericoronitis.

Pericoronitis is a polymicrobial infection (streptococci and anaerobes) around a partially erupted tooth. Benzylpenicillin's activity against these organisms is biologically plausible. However, the link currently rests only on a high TxGNN score. Oral penicillins (such as penicillin V or amoxicillin) are the agents used clinically, and parenteral benzylpenicillin is generally reserved for severe infection.

### Other Predicted Indications

The other top-ranked predictions are weaker and all carry a Hold recommendation:

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Gingival recession | 99.31% | L5 | Mainly mechanical and inflammatory; no clear antibacterial rationale |
| 3 | Canker sore | 99.27% | L5 | Immune-mediated; no defined bacterial driver |
| 4 | Ulcerative stomatitis | 99.26% | L5 | Relevant only with secondary bacterial infection |
| 5 | Denture stomatitis | 99.26% | L5 | Mostly Candida-associated; rationale weak or contradictory |
| 6 | Chemotherapy-induced oral mucositis | 99.26% | L5 | Does not target the primary pathology |
| 7 | Leukoplakia of gingiva | 99.06% | L5 | No plausible antibacterial mechanism |
| 8 | Conjunctivitis | 97.94% | L4 | Compatible with susceptible bacteria, but literature is off-target |
| 9 | Cat-scratch disease | 97.78% | L5 | *Bartonella* not reliably treated by penicillins |
| 10 | Chronic ethmoidal sinusitis | 97.63% | L5 | Polymicrobial, biofilm-associated, beta-lactamase producers |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for pericoronitis.

For the lower-ranked prediction of conjunctivitis, six publications were retrieved, but none provides clinical efficacy data in human conjunctivitis:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2936791](https://pubmed.ncbi.nlm.nih.gov/2936791/) | 1986 | Diagnostic/allergy test study | J Allergy Clin Immunol | Lymphocyte transformation test for occupational drug allergy (bacampicillin, alprenolol, quinidine) |
| [33789741](https://pubmed.ncbi.nlm.nih.gov/33789741/) | 2021 | Case series | J Med Case Rep | Congenital syphilis in seven infants in Lusaka, Zambia |
| [17496706](https://pubmed.ncbi.nlm.nih.gov/17496706/) | 2007 | Case report | Eye Contact Lens | Severe microbial keratitis in keratoglobus with vernal keratoconjunctivitis and atopic dermatitis |
| [453797](https://pubmed.ncbi.nlm.nih.gov/453797/) | 1979 | Microbiology study | Antibiotiki | Antibiograms of staphylococci from patients with eye diseases |
| [6364656](https://pubmed.ncbi.nlm.nih.gov/6364656/) | 1983 | Experimental animal study | Zh Mikrobiol Epidemiol Immunobiol | Neutrophil phagocytic activity in experimental keratoconjunctivitis |
| [2704058](https://pubmed.ncbi.nlm.nih.gov/2704058/) | 1989 | Veterinary pharmacokinetic study | J Vet Pharmacol Ther | Penicillin concentrations in bovine conjunctival sac fluid after topical application |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1775K | BenPen | Powder for injection 600 mg (as sodium) | Not specified in the data compiled for this report |

Only an injectable formulation is registered.

## Safety Considerations

- **Contraindications (from knowledge graph, not label text):** kidney disease, pyoureter, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, infectious mononucleosis and chronic Epstein-Barr virus infection syndrome. These should be confirmed against the TGA-approved Product Information (PI).
- **Drug Interactions:** 21 interactions were identified.
  - **Major:** methotrexate.
  - **Moderate:** doxycycline, minocycline, tetracycline, oxytetracycline, demeclocycline, chloramphenicol, warfarin, dicoumarol, ethinylestradiol, mycophenolic acid, picosulfuric acid, iodide I-123, iodide I-131.
  - **Minor:** clarithromycin, erythromycin.
  - **Unknown severity:** salbutamol, acyclovir, gentamicin, levothyroxine.
- Penicillin sensitisation is a particular concern for any new topical or local use.

Please refer to the TGA-approved Product Information (PI) for full warnings and precautions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for pericoronitis is supported only by a model score, with no clinical trials or publications. Established oral penicillins already cover this use, and parenteral benzylpenicillin is generally reserved for severe infection. The other predicted indications have weaker or contradictory mechanistic rationale.

**To proceed, the following is needed:**
- Clinical or observational evidence of benzylpenicillin in pericoronitis, or comparative data against oral penicillins
- Mechanism of action data and TGA PI warnings and contraindications to complete safety screening
- Approved indication text for the BenPen ARTG entry
- Route and formulation assessment, since only an injectable form is registered
- A review of the methotrexate interaction and other relevant interactions for the intended population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

