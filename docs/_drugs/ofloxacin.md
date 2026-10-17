---
layout: default
title: Ofloxacin
parent: Model Prediction Only (L5)
nav_order: 520
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ofloxacin: predicted new indication Polyclonal hyperviscosity syndrome (evidence level L5). Approved use: Typhoid fever, salmonellosis, urinary tract infection, bronchitis…"
monitor_inn: "Ofloxacin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder"]
---

# Ofloxacin
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

# Ofloxacin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Ofloxacin is a fluoroquinolone antibacterial, originally used for infections such as typhoid fever, urinary tract infection, bronchitis and bacterial pneumonia.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but there are **0 clinical trials** and **0 publications** supporting this prediction. It is a model-only prediction with no mechanistic rationale.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Typhoid fever, salmonellosis, urinary tract infection, bronchitis, bacterial pneumonia and other bacterial infections (the ARTG entry does not state an approved indication) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Ofloxacin is a fluoroquinolone, a class that inhibits bacterial DNA gyrase and topoisomerase IV, and its efficacy in bacterial infections is well established.

Polyclonal hyperviscosity syndrome is a plasma protein/immunoglobulin disorder, and there is no plausible link between antibacterial DNA gyrase inhibition and this condition. The high TxGNN score appears to be a graph-based prediction artefact rather than a pharmacologically meaningful signal. This prediction is not considered reasonable on current evidence.

**Other predictions reviewed**

Nine other predictions were reviewed. Most are also model-only (L5) with no mechanistic link: hyperamylasemia, congenital analbuminemia, blood group incompatibility, premalignant haematological disease, monoclonal gammopathy, a haematological disease associated with acquired peripheral neuropathy, and congenital haematological disorder. For the neuropathy-related prediction, fluoroquinolones are themselves associated with peripheral neuropathy, which argues against use.

Two predictions have somewhat more substance:

- **Septicaemic plague (rank 8, L4):** This is biologically plausible. *Yersinia pestis* is highly susceptible to ofloxacin in vitro, and mouse and primate models show benefit for prophylaxis and treatment. However, no human trials were identified, and this is better viewed as an extension of ofloxacin's antibacterial spectrum than true repurposing.
- **Punctate epithelial keratoconjunctivitis (rank 10, L4):** Ofloxacin is available as an ophthalmic antibacterial, so a loose link exists if a bacterial component is present. The only retrieved paper is a case report on a vernal shield ulcer healed by surgical debridement, which does not support ofloxacin efficacy. The condition is often viral or inflammatory.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the top-ranked prediction (polyclonal hyperviscosity syndrome), currently no related literature available.

Literature for the other predictions is limited and indirect. The most relevant items are for septicaemic plague:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16127904](https://pubmed.ncbi.nlm.nih.gov/16127904/) | 2002 | Animal study | Antibiot Khimioter | Ofloxacin was effective in experimental plague prophylaxis and treatment in mice; efficacy was lower against strains lacking fraction I and mouse toxin |
| [8203841](https://pubmed.ncbi.nlm.nih.gov/8203841/) | 1994 | Animal study | Antimicrob Agents Chemother | Ofloxacin and other antibiotics compared with streptomycin in a murine *Y. pestis* systemic infection model |
| [9517950](https://pubmed.ncbi.nlm.nih.gov/9517950/) | 1998 | Animal study | Antimicrob Agents Chemother | Mouse model of pneumonic plague used to compare antibiotic treatments with streptomycin |
| [11871319](https://pubmed.ncbi.nlm.nih.gov/11871319/) | 2001 | Animal study | Antibiot Khimioter | Primate model of bubonic plague developed to evaluate antibacterial efficacy |
| [10987101](https://pubmed.ncbi.nlm.nih.gov/10987101/) | 2000 | Animal study | Antibiot Khimioter | Combined fluoroquinolone and specific plague prevention evaluated in mice; fluoroquinolones, including ofloxacin, interfered with post-vaccine immunity |
| [8540736](https://pubmed.ncbi.nlm.nih.gov/8540736/) | 1995 | In vitro | Antimicrob Agents Chemother | Ofloxacin was highly active against 78 *Y. pestis* strains (ceftriaxone and ciprofloxacin most active) |
| [8913481](https://pubmed.ncbi.nlm.nih.gov/8913481/) | 1996 | In vitro | Antimicrob Agents Chemother | Ofloxacin was highly active against 100 human *Y. pestis* isolates (MIC90 <0.03 µg/mL) |
| [11858365](https://pubmed.ncbi.nlm.nih.gov/11858365/) | 2002 | Case report | Joint Bone Spine | *S. lugdunensis* discitis in a patient with multiple myeloma treated with ofloxacin and pristinamycin; unrelated to treating monoclonal gammopathy |
| [16670489](https://pubmed.ncbi.nlm.nih.gov/16670489/) | 2006 | Case report | Cornea | Vernal shield ulcer healed after surgical debridement; does not establish ofloxacin efficacy |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 5567B | Ocuflox | Eye drops 3 mg per mL, 5 mL | Not stated in the data compiled |

The only listed product is an ophthalmic formulation. Its route is unlikely to suit a systemic condition such as polyclonal hyperviscosity syndrome.

## Safety Considerations

**Contraindications flagged in the knowledge graph (not label text)**

The TxGNN knowledge graph links ofloxacin to many contraindicated conditions. The main groups are:

- **Cardiac:** long QT syndrome (including familial), torsades de pointes
- **Neurological and neuromuscular:** epilepsy, myasthenia gravis, peripheral neuropathy and other peripheral nervous system disease
- **Liver and kidney:** liver failure, liver disease, drug-induced liver injury, kidney disease, impaired renal function
- **Musculoskeletal:** tendinitis, periarthritis, rhabdomyolysis
- **Metabolic:** diabetes mellitus, diabetic ketoacidosis, potassium deficiency
- **Haematological:** thrombocytopenia, anaemia, leukopenia
- **Gastrointestinal:** *Clostridium difficile* colitis

**Drug Interactions**

Interaction screening returned 100 interactions. Examples of those classed as **Major** are:

- Corticosteroids: hydrocortisone, dexamethasone, betamethasone and triamcinolone
- Bupropion
- Chlorpropamide

Examples of those classed as **Moderate** include:

- Antidiabetic agents: metformin, pioglitazone, acarbose, canagliflozin, alogliptin and albiglutide
- Famotidine
- Loperamide
- Acetylsalicylic acid
- Calcium and potassium salts

For ofloxacin, the corticosteroid combinations raise tendon-injury concerns, and the antidiabetic combinations raise concerns about blood glucose disturbance.

Please also refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is supported only by a graph-based score. There are no trials or literature, and no plausible mechanism links an antibacterial DNA gyrase inhibitor to a plasma protein disorder. The only locally registered product is an eye drop, and the safety profile includes numerous flagged contraindications.

**To proceed, the following is needed:**
- Mechanism of action data and a credible biological rationale for polyclonal hyperviscosity syndrome
- Any preclinical or clinical evidence for the predicted indication
- The TGA Product Information, including warnings and contraindications, to support safety screening
- If pursuing a more plausible direction, such as plague, a review of existing guidelines and human data, noting that this is an antibacterial spectrum extension and not true repurposing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

