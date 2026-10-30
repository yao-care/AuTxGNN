---
layout: default
title: Clarithromycin
parent: Model Prediction Only (L5)
nav_order: 168
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-30
description: "Clarithromycin: predicted new indication Hyperamylasemia (evidence level L4). Approved use: Bacterial infections, including otitis media…"
monitor_inn: "Clarithromycin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "punctate epithelial keratoconjunctivitis", "blood group incompatibility"]
---

# Clarithromycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Clarithromycin: From Bacterial Infections to Hyperamylasemia
{: .text-alpha }

## One-Sentence Summary

Clarithromycin is a macrolide antibiotic, originally used for respiratory and ear, nose and throat infections such as pneumonia, sinusitis and otitis media.
The TxGNN model predicts it may be effective for **hyperamylasemia**, but the only supporting evidence is **1 case report** and **no registered clinical trials**.
The high model score is not backed by clinical evidence for this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections, including otitis media, streptococcal and staphylococcal infections, bacterial pneumonia (including Mycoplasma and Chlamydia), and maxillary sinusitis |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 0.9935 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

The original indications are not described in the Australian licence record, which has no approved indication text.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Clarithromycin is a macrolide antibiotic, and its efficacy in bacterial respiratory and ENT infections is established. No direct mechanism linking it to hyperamylasemia (raised blood amylase) has been identified.

The only literature is a 2004 Japanese case report of a *Mycobacterium abscessus* lung infection in a patient who also had primary macroamylasemia. Clarithromycin was used there as an antimicrobial for the infection, not to treat the raised amylase. The report therefore does not show that the drug affects the amylase abnormality.

The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15228140](https://pubmed.ncbi.nlm.nih.gov/15228140/) | 2004 | Case report | Nihon Kokyuki Gakkai Zasshi | A 76-year-old man with *M. abscessus* lung infection, who had previously had pulmonary tuberculosis, also had primary macroamylasemia. Clarithromycin was used as an antimicrobial, and no effect on amylase is established. |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 8318T | Klacid | Tablet 250 mg (oral) | Not stated in the data compiled for this report |

---

## Safety Considerations

The data compiled for this report contain no label-based warnings or contraindications. Please refer to the TGA-approved Product Information (PI) for these.

- **Knowledge graph contraindication signals** (these come from the TxGNN knowledge graph, not from label text):
  - Cardiac rhythm: long QT syndrome, torsades de pointes, ventricular tachycardia (including catecholaminergic and infant forms).
  - Liver and biliary: liver failure, liver disease, cholestasis (including benign recurrent and familial intrahepatic forms), gallbladder disease.
  - Metabolic: inherited porphyria and other porphyrin metabolism disorders.
  - Kidney: kidney disease, pyoureter.
  - Bone: osteoporosis (including postmenopausal) and bone fracture.
  - Gut: *Clostridium difficile* colitis, perinatal necrotising enterocolitis.
  - Neuromuscular: myasthenia gravis and neuromuscular junction disease.
  - Viral: infectious mononucleosis and chronic Epstein-Barr virus infection syndrome.
- **Drug interactions:** The interaction search returned 100 entries, and 20 are shown in the data compiled for this report.
  - **Major:** abemaciclib, fentanyl, acalabrutinib.
  - **Moderate:** paclitaxel, tramadol, famotidine, formoterol, nifedipine, adenosine, trastuzumab emtansine, flunisolide, afatinib, ethinylestradiol, hydrocortisone, abiraterone, acarbose, abametapir (topical).
  - **Minor:** dolutegravir, zidovudine, loratadine.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The only evidence for hyperamylasemia is a single case report in which clarithromycin treated an infection, not the amylase abnormality. No trials are registered and no mechanism is established, so the high TxGNN score is not supported.

**Other predictions worth noting:**
  - It has a completed Phase 2 trial (NCT00006219, DHEA versus clarithromycin in MGUS).
  - It also has extensive literature on clarithromycin combined with immunomodulatory drugs and dexamethasone in multiple myeloma and Waldenström's macroglobulinemia, including a Phase 3 randomised trial (PMID 34021118).
  - Most of this literature concerns related but different conditions, and the pack rates the indication L2 with a "Research Question" recommendation.
  - If the team wants to progress a lead, this one deserves a separate full evaluation.

**To proceed, the following is needed:**
- Mechanism of action data for clarithromycin.
- Evidence of any effect on amylase, for example cohort data or a rationale beyond the single case report.
- The TGA Product Information for Klacid, to confirm approved indications, warnings and contraindications.
- A QT, hepatic and drug-interaction safety plan if any new use is pursued.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

