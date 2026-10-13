---
layout: default
title: Amoxicillin
parent: Model Prediction Only (L5)
nav_order: 48
evidence_level: L5
indication_count: 10
---

# Amoxicillin
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

# Amoxicillin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Amoxicillin is a beta-lactam antibiotic originally used for bacterial infections such as urinary tract infection, otitis media, pharyngitis and bacterial pneumonia.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but there are **0 clinical trials** and **0 publications** supporting this prediction. It rests on a knowledge-graph score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection, infectious otitis media, streptococcal infection, bacterial pneumonia, pharyngitis and other bacterial infections (the ARTG entry has no indication text, so these come from the knowledge graph) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Amoxicillin is a beta-lactam antibacterial, a class that inhibits bacterial cell wall synthesis. Its efficacy in bacterial infections is well established.

For polyclonal hyperviscosity syndrome, no plausible mechanistic link is apparent. The condition is driven by elevated immunoglobulin levels and has no antibacterial target. The high score (99.63%) is a knowledge-graph prediction only and is likely a graph-topology artefact.

Other predictions in the list show the same pattern. The ones with some biological plausibility are:
- **Epiglottitis** (L4, Research Question): a bacterial upper-airway infection close to amoxicillin's existing uses. It is effectively an extension of existing indications and not a novel repurposing. Beta-lactamase-producing *H. influenzae* and standard parenteral cephalosporin management limit the role of plain amoxicillin.
- **Septicaemic plague** (L4, Research Question): supported only by in vitro and animal work, and beta-lactams are not standard therapy.

## Clinical Trial Evidence

Currently no related clinical trials registered for polyclonal hyperviscosity syndrome.

## Literature Evidence

Currently no related literature available for polyclonal hyperviscosity syndrome.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11947T | AMILOXYN | Capsule 500 mg (as trihydrate) | Not available in the data compiled for this report |

The route of administration is oral.

## Safety Considerations

- **Conditions linked to contraindication or caution in the knowledge graph** (these are not label text and should be verified against the Product Information): long QT syndrome, torsades de pointes, ventricular tachycardia, liver failure, liver disease, cholestasis, kidney disease, porphyria, *Clostridium difficile* colitis, myasthenia gravis, osteoporosis, bone fracture, gallbladder disease, and infectious mononucleosis.
- **Drug Interactions** (100 interactions recorded; examples):
  - **Major**: methotrexate; live oral cholera vaccine (*Vibrio cholerae* CVD 103-HgR)
  - **Moderate**: doxycycline, minocycline, demeclocycline, ethinylestradiol, estradiol, anisindione, dicoumarol, mycophenolate mofetil, entecavir, balsalazide, and probiotics (*Lactobacillus acidophilus*, *Bifidobacterium longum infantis*)
  - **Minor**: allopurinol, amiloride, azithromycin, clarithromycin, erythromycin

Please refer to the TGA-approved Product Information (PI) for the authoritative warnings and contraindications, as these were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no clinical trials, no literature and no plausible mechanism. Evidence is at L5 (model prediction only). Across the other predicted indications, only epiglottitis and septicaemic plague show any biological plausibility, and both remain at L4 with no trials.

**To proceed, the following is needed:**
- Mechanism of action data, to assess any link to hyperviscosity or immunoglobulin biology
- TGA Product Information for warnings and contraindications (safety screening cannot proceed without it)
- Any supporting preclinical or clinical evidence for polyclonal hyperviscosity syndrome
- If a lower-risk direction is wanted, review epiglottitis separately, given its closeness to existing labelled respiratory and ENT uses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

