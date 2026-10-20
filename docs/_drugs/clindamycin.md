---
layout: default
title: Clindamycin
parent: Model Prediction Only (L5)
nav_order: 170
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Clindamycin: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Acne, streptococcal and staphylococcal infections…"
monitor_inn: "Clindamycin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "exposure keratitis", "non-human animal disease", "neurotrophic keratopathy", "epidemic keratoconjunctivitis", "postmenopausal atrophic vaginitis", "superior limbic keratoconjunctivitis", "toxic maculopathy due to antimalarial drugs", "keratomalacia", "ophthalmia nodosa"]
---

# Clindamycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Clindamycin: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Clindamycin is a lincosamide antibiotic, originally used for acne, streptococcal and staphylococcal infections, anaerobic infections, bacterial vaginosis and aspiration pneumonia.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but there are currently **no clinical trials** and **no publications** supporting this prediction. It rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne, streptococcal and staphylococcal infections, anaerobic bacterial infections, bacterial vaginosis, aspiration pneumonia (the Australian ARTG entry has no approved indication text recorded) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, clindamycin is a lincosamide antibiotic that inhibits bacterial protein synthesis. Its efficacy in Gram-positive and anaerobic bacterial infections is established.

The mechanistic fit with punctate epithelial keratoconjunctivitis is weak. This condition is usually viral or toxic/inflammatory, so any benefit would be limited to a bacterial component. The high score likely reflects network associations with the drug's existing infection and inflammation-related indications rather than a direct biological rationale. Topical ophthalmic clindamycin is also not an established standard.

Other lower-ranked predictions were reviewed. They were mostly eye conditions and none had trial support:

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Exposure keratitis | 99.80% | L4 | Plausible only for secondary Gram-positive bacterial infection. The retrieved papers cover microbial keratitis in general, not this condition or clindamycin. |
| 3 | Non-human animal disease | 99.69% | L5 | Non-specific category. The papers concern *C. difficile* epidemiology in animals, and clindamycin is a risk factor for that infection. |
| 4 | Neurotrophic keratopathy | 99.49% | L5 | Caused by impaired corneal nerve supply. Antibiotic mechanism not relevant. |
| 5 | Epidemic keratoconjunctivitis | 99.49% | L5 | Adenoviral. Clindamycin has no antiviral activity. Retrieved papers concern bovine disease. |
| 6 | Postmenopausal atrophic vaginitis | 99.03% | L5 | Driven by oestrogen deficiency, not infection. |
| 7 | Superior limbic keratoconjunctivitis | 98.97% | L5 | Chronic inflammatory and mechanical, not bacterial. |
| 8 | Toxic maculopathy due to antimalarial drugs | 98.28% | L5 | Drug-induced retinal toxicity that clindamycin would not treat. |
| 9 | Keratomalacia | 98.28% | L5 | Caused by vitamin A deficiency. Antibiotics address only secondary infection. |
| 10 | Ophthalmia nodosa | 98.28% | L5 | Granulomatous reaction to caterpillar hairs, not bacterial. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for punctate epithelial keratoconjunctivitis.

For the second-ranked prediction (exposure keratitis), the retrieved literature is indirect and none of it studies clindamycin:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24244625](https://pubmed.ncbi.nlm.nih.gov/24244625/) | 2013 | Retrospective review | PLoS One | Characteristics, antibiotic susceptibility and outcomes of *S. aureus* keratitis, comparing MRSA and MSSA |
| [22880135](https://pubmed.ncbi.nlm.nih.gov/22880135/) | 2012 | Retrospective cohort | PLoS One | Prevalence, clinical features and antibiotic susceptibility of MRSA vs MSSA ocular infections |
| [11581057](https://pubmed.ncbi.nlm.nih.gov/11581057/) | 2001 | Case report | Ophthalmology | Contact lens-related *Bacillus cereus* keratitis linked to a contaminated lens case |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 3138E | APO-Clindamycin | Capsule 150 mg (as hydrochloride) | Not recorded in the data compiled for this report |

Only an oral formulation is registered. No ophthalmic formulation is listed.

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: liver failure, Crohn's disease, ulcerative colitis and other inflammatory bowel disease, *Clostridium difficile* colitis, diarrhoeal disease, perinatal necrotising enterocolitis, atopic and exfoliative dermatitis, sunburn, and vulvovaginal candidiasis.
- **Drug Interactions**: 100 interactions were identified. Those rated Moderate include balsalazide, clarithromycin, picosulfuric acid, attapulgite and kaolin. Others in the list, such as amphotericin B, aspirin, amoxicillin, doxycycline, vancomycin, metformin, morphine and proton pump inhibitors, have an unrated severity.

Please also refer to the TGA-approved Product Information (PI) for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported by model output only, with no trials or literature, and the mechanism fits poorly with a largely viral or inflammatory eye condition. None of the other nine predicted indications has stronger support.

**To proceed, the following is needed:**
- Detailed mechanism of action data
- Evidence that a bacterial component contributes to punctate epithelial keratoconjunctivitis, followed by preclinical or clinical studies
- Assessment of a suitable ophthalmic route and formulation, since only an oral capsule is registered in Australia
- Full safety review from the TGA Product Information, including gastrointestinal risk (*C. difficile*)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

