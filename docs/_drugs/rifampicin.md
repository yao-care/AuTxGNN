---
layout: default
title: Rifampicin
parent: Moderate Evidence (L3-L4)
nav_order: 632
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-28
description: "Rifampicin: predicted new indication Conjunctivitis (evidence level L4). Approved use: Pulmonary tuberculosis"
monitor_inn: "Rifampicin"
predicted_indications: ["conjunctivitis", "multiple endocrine neoplasia", "acne (disease)", "conjunctivitis (disease)", "HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "rheumatoid arthritis", "acute contagious conjunctivitis", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome"]
---

# Rifampicin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

## Rifampicin: From Pulmonary Tuberculosis to Conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Rifampicin is a broad-spectrum antibiotic originally used to treat pulmonary tuberculosis.
The TxGNN model predicts it may be effective for **conjunctivitis**, but there are **no registered clinical trials** and only **indirect literature** (mainly older topical trachoma and chlamydial eye studies and susceptibility surveys) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary tuberculosis |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L4 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, rifampicin is a broad-spectrum antibacterial that inhibits bacterial RNA polymerase. It has activity against Gram-positive bacteria, *Staphylococcus* and *Chlamydia*, and its efficacy in tuberculosis is established.

Bacterial conjunctivitis is commonly caused by *Staphylococcus*, *Streptococcus*, *Haemophilus* and *Chlamydia trachomatis*. An antibacterial with activity against these organisms could plausibly be applied. The evidence is indirect, however: older studies used **topical (eye ointment)** rifampicin, whereas the only Australian product is an **oral capsule**. A topical ocular formulation and antimicrobial resistance (tuberculosis stewardship) concerns remain unresolved.

Note that the model also returned a near-duplicate entry, "conjunctivitis (disease)" (score 0.9960), which should be merged with this one. Their literature largely overlaps.

## Clinical Trial Evidence

Currently no related clinical trials registered for conjunctivitis.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1096630](https://pubmed.ncbi.nlm.nih.gov/1096630/) | 1975 | Controlled clinical study | Am J Ophthalmol | 1% rifampicin or 1% tetracycline ointment vs boric acid ointment in endemic trachoma in Tunisian schoolchildren (10 weeks' treatment) |
| [322700](https://pubmed.ncbi.nlm.nih.gov/322700/) | 1977 | Open trial | Br J Ophthalmol | 1% rifampicin eye ointment vs chloramphenicol in 63 patients with chlamydial eye infection; 3 weeks was insufficient, 6-7 weeks gave about 90% clinical and microbiological cure |
| [33457332](https://pubmed.ncbi.nlm.nih.gov/33457332/) | 2020 | Cross-sectional | Adv Biomed Res | Bacterial causes and antibiotic susceptibility of conjunctivitis isolates in Kashan, Iran |
| [21191558](https://pubmed.ncbi.nlm.nih.gov/21191558/) | 2010 | In vitro study | Rev Esp Quimioter | Antibiotic susceptibility of *Corynebacterium macginleyi* strains causing conjunctivitis |
| [30347565](https://pubmed.ncbi.nlm.nih.gov/30347565/) | 2018 | Susceptibility study | Zhonghua Yan Ke Za Zhi | Genetic typing and susceptibility of *S. aureus* from keratitis or conjunctivitis |
| [8363150](https://pubmed.ncbi.nlm.nih.gov/8363150/) | 1993 | Microbiology study | An Esp Pediatr | Organisms and antibiotic sensitivity in 50 neonatal conjunctivitis samples |
| [3191080](https://pubmed.ncbi.nlm.nih.gov/3191080/) | 1988 | Case series | Br J Ophthalmol | Marginal corneal abscesses in adult chlamydial ophthalmia |
| [39336466](https://pubmed.ncbi.nlm.nih.gov/39336466/) | 2024 | Case report | Medicina (Kaunas) | Parinaud oculoglandular syndrome with Bartonella DNA detected in cornea and conjunctiva |
| [1247775](https://pubmed.ncbi.nlm.nih.gov/1247775/) | 1976 | Report | BMJ | Ocular toxicity due to rifampicin (a safety signal) |
| [5005929](https://pubmed.ncbi.nlm.nih.gov/5005929/) | 1971 | Review | Ann Ophthalmol | General review of rifampicin |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12189M | Rimycin 300 | Capsule 300 mg (oral) | Not available in the data compiled for this report |

## Cytotoxicity

Rifampicin is an antibacterial, not an antineoplastic, so this section does not apply.

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these are drug-disease associations, not product label text): liver failure, acute liver failure, hepatitis and other liver disease; porphyria; gallbladder disease; blood disorders (thrombocytopenia, neutropenia, agranulocytosis, anaemia, pancytopenia, aplastic anaemia); diabetes mellitus and diabetic ketoacidosis; gout; peripheral neuropathy; substance abuse/dependence; slow acetylator status; non-infectious meningitis; anxiety and related disorders.
- **Drug Interactions**: The interaction screen returned 100 interactions, and the 20 listed were all rated Moderate. These include rabeprazole, omeprazole, doxycycline, clarithromycin, metronidazole, metformin, pioglitazone, canagliflozin, chlorpropamide, bupropion, aprepitant, morphine, and several corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone) and vitamin D analogues (cholecalciferol, calcifediol, calcitriol). Rifampicin is a strong enzyme inducer, so co-medications need review.
- **Ocular safety**: Early reports describe ocular toxicity associated with rifampicin (PMIDs 1247775 and 1260294).

Please also refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Support for conjunctivitis rests on a high model score, in vitro susceptibility data and a few 1970s topical-ointment studies, with no registered trials. The only Australian product is an oral capsule, and there are antimicrobial stewardship concerns.

**To proceed, the following is needed:**
- Product Information warnings and contraindications for the Australian product
- Mechanism of action data
- A topical ocular formulation, or a justification for the oral route
- Modern controlled trials against current standard-of-care eye antibiotics
- A stewardship assessment on resistance risk for tuberculosis treatment
- Merging of the duplicate "conjunctivitis" entries

### Other predicted indications (for reference)

| Rank | Predicted Indication | Score | Evidence Level | Comment | Decision |
|---|---|---|---|---|---|
| 2 | Multiple endocrine neoplasia | 0.9986 | L5 | Prediction only | Hold |
| 3 | Acne (disease) | 0.9974 | L4 | Evidence mostly concerns hidradenitis suppurativa (clindamycin + rifampicin), not acne vulgaris | Hold |
| 5 | HIV infectious disease | 0.9959 | L4 | Phase 2/3 trials are TB/HIV co-infection and interaction studies, not anti-HIV efficacy | Research Question |
| 7 | Rheumatoid arthritis | 0.9945 | L3 | Small 1980s-90s studies with limited, inconsistent benefit; one Phase 1 PK trial | Research Question |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

