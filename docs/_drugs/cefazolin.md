---
layout: default
title: Cefazolin
parent: Moderate Evidence (L3-L4)
nav_order: 141
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Cefazolin: predicted new indication Infectious otitis media (evidence level L4). Approved use: Bacterial pneumonia, cholangitis, endocarditis, bacterial arthritis"
monitor_inn: "Cefazolin"
predicted_indications: ["infectious otitis media", "bronchitis", "middle ear disease", "chronic otitis media", "suppurative otitis media", "otosalpingitis", "non-suppurative otitis media", "allergic otitis media", "middle ear cholesterol granuloma", "urinary tract infection (disease)"]
---

# Cefazolin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Cefazolin: From Bacterial Pneumonia to Infectious Otitis Media

## One-Sentence Summary

Cefazolin is a first-generation cephalosporin antibiotic, originally used for bacterial infections such as bacterial pneumonia, endocarditis, bacterial arthritis and cholangitis.
The TxGNN model predicts it may be effective for **infectious otitis media**, but there are **no registered clinical trials** and only **2 publications** (a case report and an unrelated review), so the prediction rests mainly on the model score and mechanistic plausibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial pneumonia, cholangitis, endocarditis, bacterial arthritis (from the knowledge graph; no approved indication text available for the Australian licence) |
| Predicted New Indication | Infectious otitis media |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, cefazolin is a first-generation cephalosporin that inhibits bacterial cell wall synthesis by binding penicillin-binding proteins. It is active against Gram-positive organisms such as streptococci and staphylococci.

Its established uses (staphylococcal and streptococcal pneumonia, endocarditis, bacterial arthritis) involve the same Gram-positive pathogens that can cause bacterial otitis media. This is the mechanistic bridge behind the prediction.

There are important limits. Cefazolin has weak activity against *Haemophilus influenzae* and *Moraxella catarrhalis*, the other major otitis media pathogens, and it does not cover *Pseudomonas*. The only directly relevant clinical item is a 2025 case report of ceftazidime-cefazolin empiric therapy for Gradenigo syndrome (a rare complication of otitis media). The model's other high-scoring predictions (for example allergic otitis media and middle ear cholesterol granuloma) are non-bacterial conditions, which suggests the score partly reflects network proximity to ear-related terms rather than a specific mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for infectious otitis media.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Case report/series | Ann Otol Rhinol Laryngol | Ceftazidime-cefazolin empiric therapy in paediatric Gradenigo syndrome, a complication of acute otitis media. Case-level observation only. |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Review | Clin Pharm | Management of Stevens-Johnson syndrome. Otitis media is mentioned only as the patient's initial illness; not relevant to cefazolin efficacy. |

**Related indications (context only):**
- Suppurative otitis media: a 1982 Japanese comparative study (PMID [6752467](https://pubmed.ncbi.nlm.nih.gov/6752467/)) used cefazolin as the comparator against cefmetazole in 172 evaluable patients. It is the strongest signal in the otitis media group, but it is dated and not a cefazolin-focused trial.
- Other related terms (middle ear disease, chronic otitis media) yielded mostly veterinary reports, susceptibility surveys and studies of other cephalosporins.
- Otosalpingitis, non-suppurative otitis media, allergic otitis media and middle ear cholesterol granuloma have no trials or literature.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12115P | Cephazolin Viatris | Powder for injection 2 g (as sodium) | Not available in the data compiled for this report |

Cefazolin is available in Australia as an injectable only. Most otitis media is managed in the community with oral agents, so route compatibility is a practical barrier.

---

## Safety Considerations

Safety data from the product information were not available. Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

**Contraindication signals from the knowledge graph (not label text):** blood coagulation disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, congenital prothrombin deficiency.

**Drug interactions:** 100 interactions were identified; the main ones rated Moderate are:
- Kanamycin
- Neomycin
- Streptomycin
- Picosulfuric acid

Many others are listed with an unknown severity level (for example amphotericin B, acetylsalicylic acid, metformin and omeprazole). Check these against the PI and an interaction reference before use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (99.44%), but the evidence is L4 at best for this specific indication: no registered trials, and the only direct literature is a single case report. Cefazolin's spectrum misses key otitis media pathogens, it is injectable only, and established oral agents exist.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank
- Approved indication text and safety information (warnings, contraindications) from the TGA Product Information
- A structured review of cefazolin's activity against current Australian otitis media isolates, including *H. influenzae* and *M. catarrhalis*
- Comparative data against current first-line otitis media treatments
- Clarification of where a parenteral agent would fit (for example complicated or hospitalised cases)

**Other candidates:** Of the ten predictions in the data, **urinary tract infection** (scored at stage S1 as a Research Question) and **suppurative otitis media** (L3 at best) are more promising directions for follow-up. Cefazolin is already used for urinary tract infection in practice and has high urinary concentrations. For that indication the open question is formal positioning, such as parenteral step-down or susceptibility-guided use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

