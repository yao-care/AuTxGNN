---
layout: default
title: Mupirocin
parent: Model Prediction Only (L5)
nav_order: 490
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
monitor_inn: "Mupirocin"
predicted_indications: ["pleural empyema (disease)", "punctate epithelial keratoconjunctivitis"]
description: "Mupirocin: predicted new indication Pleural empyema (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Mupirocin
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

## Mupirocin: Pleural empyema (disease)
{: .text-alpha }

## One-Sentence Summary

Mupirocin is a topical antibiotic originally used to treat impetigo, including bullous impetigo.
The TxGNN model predicts it may be useful for **Pleural Empyema**, with **no registered clinical trials** and **13 publications** (mostly epidemiology and case reports, plus one retrospective cohort study) supporting this direction.

> **Note on indication selection:** The top-ranked TxGNN prediction (pleural empyema, score 0.9949) has no supporting evidence and a weak biological rationale for a topical agent. This report therefore focuses on the best-supported prediction, SSSS (rank 9), and summarises the other predictions briefly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pleural empyema (disease) |
| TxGNN Prediction Score | 0.9949 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
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
| 1 | Pleural empyema | 0.9949 | L5 | Prediction only; topical agent has no meaningful pleural exposure |
| 2 | Punctate epithelial keratoconjunctivitis | 0.9910 | L5 | Often viral or non-infectious; no evidence |

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

