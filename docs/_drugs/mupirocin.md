---
layout: default
title: Mupirocin
parent: Moderate Evidence (L3-L4)
nav_order: 490
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-13
description: "Mupirocin: predicted new indication Staphylococcal scalded skin syndrome (SSSS) (evidence level L3). Approved use: Impetigo"
---

# Mupirocin
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Mupirocin: From Impetigo to Staphylococcal Scalded Skin Syndrome

## One-Sentence Summary

Mupirocin is a topical antibiotic originally used to treat impetigo, including bullous impetigo.
The TxGNN model predicts it may be useful for **Staphylococcal Scalded Skin Syndrome (SSSS)**, with **no registered clinical trials** and **13 publications** (mostly epidemiology and case reports, plus one retrospective cohort study) supporting this direction.

> **Note on indication selection:** The top-ranked TxGNN prediction (pleural empyema, score 99.49%) has no supporting evidence and a weak biological rationale for a topical agent. This report therefore focuses on the best-supported prediction, SSSS (rank 9), and summarises the other predictions briefly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Impetigo; bullous impetigo (from the TxGNN knowledge graph, as no approved indication text is available for the ARTG entry) |
| Predicted New Indication | Staphylococcal scalded skin syndrome (SSSS) |
| TxGNN Prediction Score | 95.57% |
| Evidence Level | L3 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, mupirocin inhibits bacterial isoleucyl-tRNA synthetase and is active against *Staphylococcus aureus*, including many methicillin-susceptible strains.

SSSS is caused by exfoliative toxins produced by *S. aureus*. It is closely related to bullous impetigo, which is also toxin-mediated and caused by the same organism. Because mupirocin is already used for bullous impetigo, its use as a topical adjunct in SSSS is biologically plausible.

There are important limits. Mupirocin does not neutralise the toxin and cannot replace systemic antibiotics in SSSS. Resistance is also a concern: Greek studies (PMID 30418106, 28592549) describe emerging mupirocin- and fusidic acid-resistant *S. aureus* clones, including an ST121 clone causing SSSS.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No RCTs were found. The most relevant publications are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37404367](https://pubmed.ncbi.nlm.nih.gov/37404367/) | 2023 | Retrospective cohort | Clin Cosmet Investig Dermatol | Compared treatment duration, influencing factors and costs among different IV antibiotics combined with 2% mupirocin ointment in paediatric SSSS |
| [15482208](https://pubmed.ncbi.nlm.nih.gov/15482208/) | 2004 | Review | Expert Rev Anti Infect Ther | Treatment of bullous impetigo and SSSS in infants; bullous impetigo and SSSS lie on the same toxin-mediated spectrum |
| [8435912](https://pubmed.ncbi.nlm.nih.gov/8435912/) | 1993 | Review | Dermatol Clin | Staphylococcal control in skin disease; topical mupirocin described as a valuable addition for impetigo |
| [35901469](https://pubmed.ncbi.nlm.nih.gov/35901469/) | 2022 | Case report series | Adv Neonatal Care | SSSS identification and wound care in neonates with MSSA |
| [30418106](https://pubmed.ncbi.nlm.nih.gov/30418106/) | 2019 | Epidemiology | J Med Microbiol | SSSS increase linked to a mupirocin- and fusidic acid-resistant MSSA clone (ST121) |
| [28592549](https://pubmed.ncbi.nlm.nih.gov/28592549/) | 2017 | Epidemiology | J Clin Microbiol | Emergence of a mupirocin- and fusidic acid-resistant *S. aureus* clone causing mainly skin infections |
| [31725120](https://pubmed.ncbi.nlm.nih.gov/31725120/) | 2020 | Epidemiology/Cohort | Pediatr Infect Dis J | Increasing SSSS cases caused by ST121 in Houston, Texas |
| [42509990](https://pubmed.ncbi.nlm.nih.gov/42509990/) | 2026 | Retrospective cohort | Children (Basel) | 11-year review of paediatric SSSS: epidemiology, microbiology, management and resistance |
| [16009455](https://pubmed.ncbi.nlm.nih.gov/16009455/) | 2005 | Outbreak investigation | J Hosp Infect | Nosocomial SSSS outbreak in neonates and its control |
| [27047925](https://pubmed.ncbi.nlm.nih.gov/27047925/) | 2014 | Case report | Dermatopathology (Basel) | SSSS in an adult receiving chemotherapy |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11822F | Mupirocin Nasal (Medsurge) | Nasal ointment 20 mg (as calcium) per g, 5 g | Not available in the data compiled for this report |

The single registered product is a nasal ointment. This is a different formulation from the skin ointment used in the SSSS literature (2% mupirocin), so route and formulation compatibility with the predicted indication is unconfirmed.

---

## Safety Considerations

- **Knowledge-graph contraindication signal:** dermatitis is listed as a contraindicated condition in the TxGNN knowledge graph. This is not label text and should be verified against the Product Information.
- **Drug interactions:** The interaction query returned 100 records, all with an unclassified severity level, so no clinically meaningful interaction can be highlighted. Examples include calcitriol, clotrimazole, morphine, metformin, omeprazole and vancomycin.
- **Resistance:** Mupirocin-resistant *S. aureus* has been reported in SSSS-related literature (see above).
- **Ocular use:** An in vitro study (PMID 8222720) raised a corneal epithelial toxicity concern, which is relevant to any ocular use.

For other warnings and contraindications, please refer to the TGA-approved Product Information (PI).

---

## Other Predicted Indications (Summary)

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 1 | Pleural empyema | 99.49% | L5 | Prediction only; topical agent has no meaningful pleural exposure |
| 2 | Punctate epithelial keratoconjunctivitis | 99.10% | L5 | Often viral or non-infectious; no evidence |
| 3 | Neurotrophic keratopathy | 98.48% | L5 | Neurodegenerative, not primarily infectious |
| 4 | Cutaneous candidiasis | 98.27% | L4 | Single 1991 report of unclear design (PMID 1678836); mechanism unclear; a research question only |
| 5 | Vaginal discharge | 96.01% | L5 | Non-specific symptom; no evidence |
| 6 | Exposure keratitis | 95.89% | L4 | In vitro data only, with a corneal toxicity concern |
| 7 | Leukoplakia of vagina | 95.81% | L5 | No mechanistic link |
| 8 | Non-human animal disease | 95.66% | L5 | Non-specific ontology category; exclude |
| 10 | Bacterial vaginosis | 95.19% | L4 | Polymicrobial anaerobic condition; one MRSA vaginitis case report only |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for SSSS only; all other predictions: Hold)

**Rationale:**
SSSS shares its toxin-mediated, *S. aureus*-driven pathophysiology with bullous impetigo, an original indication, and observational data support topical mupirocin as an adjunct to systemic antibiotics. The evidence is limited to observational studies and case reports (L3), so use should stay adjunctive and not a stand-alone treatment.

**To proceed, the following is needed:**
- Product Information warnings and contraindications (the package insert data were not available, which blocks formal safety screening)
- Mechanism of action data confirmed from DrugBank
- Confirmation of the approved indication text and of formulation suitability (the only ARTG entry is a nasal ointment)
- Prospective or comparative studies of topical mupirocin as an adjunct in SSSS
- Local Australian *S. aureus* mupirocin resistance surveillance data
- Review of the dermatitis contraindication signal against the PI
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

