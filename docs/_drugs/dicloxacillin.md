---
layout: default
title: Dicloxacillin
parent: Model Prediction Only (L5)
nav_order: 214
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Dicloxacillin: predicted new indication Bacterial arthritis (evidence level L5). Approved use: Staphylococcus aureus infection, staphylococcal infection…"
---

# Dicloxacillin
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

# Dicloxacillin: From Staphylococcal Infections to Bacterial Arthritis

## One-Sentence Summary

Dicloxacillin is a penicillinase-resistant penicillin, originally used to treat staphylococcal infections, including *Staphylococcus aureus* infection and staphylococcal pneumonia.
The TxGNN model predicts it may be effective for **bacterial arthritis**, with **1 clinical trial** and **9 publications** currently linked to this direction. Note that this is largely an extension of existing staphylococcal use to a specific infection site rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Staphylococcus aureus infection, staphylococcal infection, staphylococcal pneumonia (the Australian licence entry has no approved indication text) |
| Predicted New Indication | Bacterial arthritis |
| TxGNN Prediction Score | 97.08% |
| Evidence Level | L2 (see note in the Conclusion) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, dicloxacillin is a penicillinase-resistant beta-lactam antibiotic that inhibits bacterial cell wall synthesis. It is active against methicillin-susceptible *Staphylococcus aureus* (MSSA).

*Staphylococcus aureus* is the leading cause of bacterial (septic) arthritis and of bone and joint infections. Because dicloxacillin is already used for staphylococcal infections, the prediction is mechanistically consistent. It extends an existing use to a specific infection site. Pharmacokinetic work in children has also measured synovial fluid concentrations after oral dicloxacillin, among other oral antibiotics.

Other predictions in the top 10 are weaker. Several (polyclonal hyperviscosity syndrome, hyperamylasemia, congenital analbuminemia, blood group incompatibility, premalignant haematological disease, monoclonal gammopathy and an acquired peripheral neuropathy-associated haematological disease) have no plausible mechanism and no clinical evidence. They most likely reflect knowledge-graph proximity rather than biology. Streptococcal pneumonia is biologically plausible, but dicloxacillin's staphylococcal-focused spectrum makes it a poor choice compared with penicillin or amoxicillin. Staphylococcal toxaemia is only indirectly supported, because dicloxacillin does not neutralise preformed toxins.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04563325](https://clinicaltrials.gov/study/NCT04563325) | Phase 4 | Completed | 180 | Nationwide randomised, non-inferiority trial in children with bone and joint infections. Oral-only antibiotics were compared with initial intravenous therapy followed by oral therapy, with identical total duration. It tests an oral versus IV strategy, not dicloxacillin specifically. |

No ANZCTR trial identifiers were found in the data compiled for this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39025092](https://pubmed.ncbi.nlm.nih.gov/39025092/) | 2024 | RCT | Lancet Child Adolesc Health | Danish nationwide non-inferiority trial of initial oral versus intravenous empirical antibiotics in children and adolescents with uncomplicated bone and joint infections. |
| [12362608](https://pubmed.ncbi.nlm.nih.gov/12362608/) | 2002 | Review | Ugeskr Laeger | Review of *S. aureus* infections in Denmark. Penicillinase-stable penicillins remain the drug of choice, and dicloxacillin is usually chosen. |
| [14632104](https://pubmed.ncbi.nlm.nih.gov/14632104/) | 2003 | Review | Paediatr Drugs | Review of acute bacterial skin infections in children, including complications such as arthritis if treatment is delayed. |
| [23599360](https://pubmed.ncbi.nlm.nih.gov/23599360/) | 2013 | Cohort | J Antimicrob Chemother | Retrospective analysis comparing penicillin, dicloxacillin and cefuroxime for penicillin-susceptible *S. aureus* bacteraemia, using 30-day mortality. |
| [619055](https://pubmed.ncbi.nlm.nih.gov/619055/) | 1978 | Pharmacokinetic study | J Pediatr | Measured synovial fluid and serum antibiotic levels after oral doses of several agents, including dicloxacillin, in children with pyogenic arthritis. |
| [7356349](https://pubmed.ncbi.nlm.nih.gov/7356349/) | 1980 | Observational study | Arch Dermatol | Recurrent staphylococcal infection in families. Participants were treated with oral oxacillin or dicloxacillin. |
| [7839849](https://pubmed.ncbi.nlm.nih.gov/7839849/) | 1994 | Case series | Acta Orthop Scand | 145 hospitalisations of intravenous drug users with soft tissue infections, including one purulent arthritis. |
| [940031](https://pubmed.ncbi.nlm.nih.gov/940031/) | 1976 | Case report | J Pediatr | Subtherapeutic oral dicloxacillin levels in a neonate, linked to high urinary excretion. |
| [1287818](https://pubmed.ncbi.nlm.nih.gov/1287818/) | 1992 | Case report | Scand J Infect Dis | Acquired bisalbuminaemia in a patient with staphylococcal endocarditis treated with dicloxacillin. |

Only the 2024 RCT is directly relevant to bone and joint infection, and it does not isolate dicloxacillin.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10790X | Distaph 500 | Capsule 500 mg (as sodium) | Not stated in the data compiled for this report |

The only registered product is an oral capsule. Any use for bone and joint infection in children would need a suitable paediatric formulation.

---

## Safety Considerations

No label-based warnings or contraindications are available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for these.

- **Knowledge-graph contraindication associations** (these are not label text): kidney disease, pyoureter, *Clostridium difficile* colitis, perinatal necrotising enterocolitis, infectious mononucleosis, and chronic Epstein-Barr virus infection syndrome.
- **Drug interactions**: 41 interactions were identified in total. The most notable are rated Moderate:
  - Tetracyclines: doxycycline, tetracycline, minocycline
  - Balsalazide
  - Picosulfuric acid
  - Iodide I-131
- **Minor**: clarithromycin.
- **Unknown severity**: several others, including proton pump inhibitors (omeprazole, pantoprazole, lansoprazole), ranitidine, corticosteroids (prednisone, dexamethasone, triamcinolone), morphine, loperamide, ondansetron, metronidazole, misoprostol and rosuvastatin.
- **Pharmacokinetic note**: dicloxacillin is highly albumin-bound, so conditions affecting albumin may alter free-drug levels. A published case also describes subtherapeutic levels in a neonate.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Bacterial arthritis is a plausible, largely on-label-adjacent extension of dicloxacillin's staphylococcal use. The evidence is indirect, however: the one completed randomised trial is Phase 4 and tests an oral-versus-IV strategy rather than dicloxacillin itself. The L2 grade is therefore generous, and the supporting evidence is closer to L3. The other nine predictions in the top 10 should stay on Hold or be treated as research questions.

**To proceed, the following is needed:**
- The TGA Product Information, to confirm approved indications, warnings and contraindications. The product has no indication text on record, and the lack of label safety data is a blocking gap.
- Mechanism of action data from DrugBank.
- Drug-specific evidence on dicloxacillin for bone and joint infection, including the antibiotics used in the trial arms.
- Dosing and formulation guidance for paediatric and adult bone and joint infection, given the single capsule product and the reported variable absorption.
- Review of the moderate interactions (particularly tetracyclines) and renal function considerations before use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

