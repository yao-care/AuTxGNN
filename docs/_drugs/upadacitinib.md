---
layout: default
title: Upadacitinib
parent: Model Prediction Only (L5)
nav_order: 761
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Upadacitinib: predicted new indication Colobomatous microphthalmia-rhizomelic dysplasia syndrome (evidence level L5). Approved use: Rheumatoid arthritis"
monitor_inn: "Upadacitinib"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "indolent plasma cell myeloma", "amyotrohpic lateral sclerosis type 22", "heparin cofactor 2 deficiency", "amyotrophic lateral sclerosis, susceptibility to", "plasma cell myeloma", "Mills syndrome", "amyotrophic lateral sclerosis", "axial spondylometaphyseal dysplasia"]
---

# Upadacitinib
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

# Upadacitinib: From Rheumatoid Arthritis to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Upadacitinib is an oral JAK inhibitor, originally used to treat rheumatoid arthritis.
The TxGNN model predicts it may be effective for **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, a rare developmental disorder,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction. It is a model-based signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis (from the TxGNN knowledge graph; no approved indication text is available in the ARTG data compiled for this report) |
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, upadacitinib belongs to the Janus kinase (JAK) inhibitor class (JAK1-preferential), and its efficacy in rheumatoid arthritis is established through modulation of inflammatory cytokine signalling.

The predicted indication is a rare congenital developmental dysplasia. No plausible link between JAK-STAT signalling and this condition is evident from the data compiled for this report. The high TxGNN score reflects a graph-based association only and should be treated as a hypothesis-generating signal, possibly a graph artefact, rather than evidence of benefit.

Other high-ranking predictions show the same pattern. These include brachydactyly-syndactyly syndrome (99.58%), several amyotrophic lateral sclerosis entries, plasma cell myeloma (92.58%) and indolent plasma cell myeloma (94.40%). Only the myeloma entries have even a theoretical rationale, via IL-6/JAK/STAT3 signalling in plasma cell survival, and none has supporting clinical data. The single publication found for plasma cell myeloma (PMID 42778764) concerns CAR-T-associated enterocolitis, not upadacitinib efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11979L | Rinvoq | Tablet 15 mg (oral) | Not available in the data compiled for this report |

## Safety Considerations

**Drug Interactions** (100 interactions identified; main examples shown):
- **Major:** systemic and inhaled corticosteroids (hydrocortisone, prednisone, prednisolone, dexamethasone, betamethasone, triamcinolone, budesonide, beclomethasone), clarithromycin, cobicistat, deferiprone, iobenguane (I-131)
- **Moderate:** aprepitant, cimetidine, miconazole, deferasirox
- **Minor:** zinc salts (sulfate, acetate, gluconate)

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications. Class-level concerns for JAK inhibitors include serious infection, malignancy and venous thromboembolism. These are relevant to the immunosuppression and thrombosis considerations raised for the myeloma and heparin cofactor 2 deficiency predictions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a model score, with no clinical trials, no literature and no identifiable mechanistic link to JAK inhibition. Evidence is at the lowest level (L5).

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA) and a biologically plausible link to the predicted disease
- Systematic literature and trial registry searches (including ANZCTR) for the predicted indication
- TGA Product Information warnings and contraindications for safety screening
- Review of the approved indication text for the ARTG entry
- If a repurposing direction is pursued, consider the myeloma-related predictions only as hypotheses, with a dedicated assessment of infection and malignancy risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

