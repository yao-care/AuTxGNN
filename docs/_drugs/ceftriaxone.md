---
layout: default
title: Ceftriaxone
parent: Model Prediction Only (L5)
nav_order: 142
evidence_level: L5
indication_count: 10
---

# Ceftriaxone
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

# Ceftriaxone: From Bacterial Infections to Infectious Otitis Media

## One-Sentence Summary

Ceftriaxone is a third-generation cephalosporin antibiotic, originally used for bacterial infections such as pneumonia, meningitis, gonorrhoea and salmonellosis.
The TxGNN model's top-ranked prediction, polyclonal hyperviscosity syndrome, has no supporting evidence, so this report focuses on the first prediction with real evidence, **infectious otitis media** (score 99.26%). It is supported by **1 registered clinical trial (not testing ceftriaxone)** and **19 publications**, and it is best seen as an extension of an existing antibacterial use rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (streptococcal infection, bacterial pneumonia, bacterial meningitis, gonorrhoea, salmonellosis and others, per the knowledge graph). The ARTG entry has no indication text recorded. |
| Predicted New Indication | Top-ranked: polyclonal hyperviscosity syndrome (L5, Hold). Most evidence-supported: infectious otitis media |
| TxGNN Prediction Score | 99.39% (polyclonal hyperviscosity syndrome); 99.26% (infectious otitis media) |
| Evidence Level | L3 for infectious otitis media (L5 for the top-ranked prediction) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails (infectious otitis media); Hold (top-ranked prediction) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Ceftriaxone is a beta-lactam antibiotic that inhibits bacterial cell wall synthesis, and its efficacy in bacterial infections is established.

**Top-ranked prediction (polyclonal hyperviscosity syndrome):** No mechanistic link was identified. This is a haematological and immunological condition with no bacterial target. The high score is a model output only, with no trials or literature.

**Infectious otitis media:** The mechanistic case is strong. Ceftriaxone is active against the main pathogens of otitis media (*Streptococcus pneumoniae*, *Haemophilus influenzae*, *Moraxella catarrhalis*). Because these are bacteria already within its known spectrum, this is better viewed as an extension of the existing indication than as true repurposing.

**Other ear-related predictions:**
- **Suppurative otitis media and middle ear disease:** plausible for acute bacterial disease, but evidence is dated or overlaps with infectious otitis media.
- **Chronic otitis media:** weak support. It is dominated by *Pseudomonas aeruginosa*, *Staphylococcus aureus* and biofilm-forming organisms, where systemic ceftriaxone is not a standard option.
- **Otosalpingitis:** no evidence retrieved.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02567825](https://clinicaltrials.gov/study/NCT02567825) | N/A | Completed | 250 | Tympanostomy tubes versus non-surgical management for recurrent acute otitis media over 2 years. It does not test ceftriaxone, so it is contextual only. |

No ANZCTR trial identifiers were available in the data compiled for this report.

---

## Literature Evidence

Selected publications for infectious otitis media:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8989332](https://pubmed.ncbi.nlm.nih.gov/8989332/) | 1997 | Randomised trial | Pediatrics | Single-dose intramuscular ceftriaxone compared with 10 days of oral trimethoprim-sulfamethoxazole for acute otitis media |
| [11099083](https://pubmed.ncbi.nlm.nih.gov/11099083/) | 2000 | Clinical trial | Pediatr Infect Dis J | One-day versus three-day intramuscular ceftriaxone for nonresponsive acute otitis media in children |
| [9877360](https://pubmed.ncbi.nlm.nih.gov/9877360/) | 1998 | Clinical study | Pediatr Infect Dis J | Bacteriological efficacy of a three-day intramuscular ceftriaxone regimen in nonresponsive acute otitis media |
| [8151462](https://pubmed.ncbi.nlm.nih.gov/8151462/) | 1994 | Clinical study | J Pediatr | Intramuscular ceftriaxone versus oral amoxicillin to prevent meningitis and other bacterial sequelae in febrile children at risk of occult bacteraemia |
| [12166789](https://pubmed.ncbi.nlm.nih.gov/12166789/) | 2002 | Consensus | Clin Pediatr | Consensus recommendations for treating acute otitis media (industry-sponsored meeting) |
| [35841649](https://pubmed.ncbi.nlm.nih.gov/35841649/) | 2022 | Cohort | Int J Pediatr Otorhinolaryngol | Factors associated with ceftriaxone use for acute otitis media in US primary care, noted as a marker of antimicrobial resistance |
| [10688388](https://pubmed.ncbi.nlm.nih.gov/10688388/) | 2000 | Review | Clin Ther | Review of antimicrobial treatment recommendations for acute otitis media |
| [2523493](https://pubmed.ncbi.nlm.nih.gov/2523493/) | 1989 | Clinical study | Jpn J Antibiot | Ceftriaxone 1 g daily versus cefotiam in acute suppurative otitis media. Clinical efficacy was 71% for ceftriaxone and 86% for cefotiam. |
| [20802367](https://pubmed.ncbi.nlm.nih.gov/20802367/) | 2010 | Review | Otol Neurotol | Prevention and treatment of meningitis and acute otitis media in children with cochlear implants |
| [39361280](https://pubmed.ncbi.nlm.nih.gov/39361280/) | 2024 | Review | JAMA Netw Open | Optimal paediatric outpatient antibiotic prescribing |

The only evidence retrieved for the other predictions is as follows.
- **Hyperamylasemia:** a 1999 prophylaxis study (PMID 10458061) after endoscopic papillosphincterotomy, which is an indirect infection-prevention link.
- **Blood group incompatibility:** a fetal cholelithiasis paper (PMID 37761267), which is a safety signal rather than evidence of benefit.
- **Polyclonal hyperviscosity syndrome, congenital analbuminemia, premalignant haematological system disease and otosalpingitis:** no literature.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11169W | Ceftriaxone Viatris | Powder for injection 2 g (as sodium) | Not recorded in the data compiled for this report |

Only an injectable formulation is registered. This is compatible with the intramuscular and intravenous regimens studied for otitis media.

---

## Safety Considerations

**Knowledge-graph contraindication signals** (from drug-disease relationships, not label text):
- Liver disease
- Gallbladder disease
- Neonatal jaundice
- *Clostridium difficile* colitis
- Perinatal necrotising enterocolitis
- Haemolytic anaemia

**Drug interactions** (100 recorded in total; main ones listed):
- **Major:** calcium chloride, calcium glucoheptonate and calcium gluconate. Ceftriaxone must not be mixed or co-administered with calcium-containing intravenous products.
- **Moderate:** kanamycin, neomycin, streptomycin and picosulfuric acid.
- Many further interactions have an unclassified severity (for example amphotericin B, acetylsalicylic acid and pantoprazole).

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (infectious otitis media); Hold (polyclonal hyperviscosity syndrome and the other low-evidence predictions)**

**Rationale:**
- The top-ranked predictions have no clinical evidence and no plausible mechanism, so they should not be pursued.
- For infectious otitis media, ceftriaxone acts on the relevant bacteria and has randomised comparative data. Overall evidence is L3 (the available studies are older, there are no registered ceftriaxone trials, and the one registered trial does not test ceftriaxone). It is an extension of existing antibacterial use and should sit within antimicrobial stewardship.

**To proceed, the following is needed:**
- Confirmation of the ARTG-approved indications and PI warnings and contraindications. The safety data gap is flagged as blocking for formal safety screening.
- Mechanism of action data from DrugBank.
- Stewardship guardrails: reserve ceftriaxone for specific scenarios such as vomiting or failure of oral therapy, consider local resistance patterns, and prefer narrower-spectrum first-line agents.
- Review of current Australian guidelines for otitis media, since the retrieved evidence is mostly pre-2005.
- Chronic suppurative otitis media should not be pursued with systemic ceftriaxone, given the pathogen profile (*Pseudomonas*, biofilms) and the standard role of topical therapy.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

