---
layout: default
title: Filgrastim
parent: Model Prediction Only (L5)
nav_order: 297
evidence_level: L5
indication_count: 10
---

# Filgrastim
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

# Filgrastim: From Severe Congenital Neutropenia to Primary Release Disorder of Platelets

## One-Sentence Summary

Filgrastim (G-CSF) was originally used to treat neutrophil disorders such as constitutional neutropenia, severe congenital neutropenia, cyclic haematopoiesis and chronic familial neutropenia.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but **no clinical trials and no publications** currently support this prediction. It is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Constitutional neutropenia, severe congenital neutropenia, cyclic haematopoiesis, chronic familial neutropenia (the ARTG entry carries no indication text) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, filgrastim is a granulocyte colony-stimulating factor (G-CSF) that acts on the neutrophil lineage through G-CSF receptor signalling. Its efficacy in neutrophil disorders is established.

A primary release disorder of platelets is an intrinsic defect in platelet granule release, a different cell lineage and a different pathway. No established mechanism connects G-CSF to this condition. The high TxGNN score reflects a computational association only and is not supported by trials or literature.

The same pattern applies to the other top-ranked predictions (pseudo-von Willebrand disease, Glanzmann thrombasthenia, Scott syndrome, collagen receptor defects and others). They are intrinsic platelet or protein-regulation defects that G-CSF is not known to correct.

The only plausible indirect role is supportive use in haematopoietic stem cell transplantation, which can be curative for some inherited platelet disorders. In that setting filgrastim mobilises stem cells and speeds neutrophil engraftment. It would not act on the platelet defect itself.

## Clinical Trial Evidence

No trials were registered for the top-ranked prediction. The trials below were matched to a lower-ranked prediction, "platelet-type bleeding disorder" (rank 10), and are included for context. All are transplant studies in which filgrastim is likely a supportive component, and none tests filgrastim for a bleeding disorder.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00296023](https://clinicaltrials.gov/study/NCT00296023) | NA | Completed | 25 | Low-dose allogeneic peripheral blood stem cell transplant for high-risk low-grade haematologic malignancies |
| [NCT00004232](https://clinicaltrials.gov/study/NCT00004232) | Phase 1 | Completed | Not reported | CD34-enriched peripheral blood stem cells to augment bone marrow in allogeneic transplant for haematologic cancer |
| [NCT00054236](https://clinicaltrials.gov/study/NCT00054236) | Phase 1 | Completed | 55 | Multiple cord blood unit transplant after non-myeloablative conditioning (haematologic cancer or severe aplastic anaemia) |
| [NCT00301912](https://clinicaltrials.gov/study/NCT00301912) | Phase 2 | Withdrawn | 0 | Busulfan and fludarabine conditioning before matched unrelated donor transplant; no data generated |
| [NCT00295997](https://clinicaltrials.gov/study/NCT00295997) | NA | Unknown | 35 | Non-myeloablative matched unrelated donor transplant for haematologic malignancies, renal cell carcinoma and aplastic anaemia |
| [NCT00080925](https://clinicaltrials.gov/study/NCT00080925) | Phase 1 | Completed | 20 | T-cell depleted, reduced-intensity haploidentical transplant for haematologic malignancies |
| [NCT00004904](https://clinicaltrials.gov/study/NCT00004904) | Phase 1 | Completed | Not reported | T-cell depleted partially matched related donor transplant with CD34 "veto" cells |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 2733W | Zarzio | Injection 480 micrograms in 0.5 mL single-use pre-filled syringe | Not available in the data compiled for this report |

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 potential interactions, and the first 20 are all rated Moderate. The main ones are:
  - Radiopharmaceuticals and radioimmunotherapies: iobenguane (I-131), fludeoxyglucose (18F), ibritumomab tiuxetan, tositumomab and tositumomab (I-131).
  - Cytotoxic and antineoplastic agents: paclitaxel, mercaptopurine, trimetrexate, azacitidine, bendamustine, altretamine, arsenic trioxide, asparaginase *Escherichia coli* and abemaciclib.
  - Other agents: levamisole, acalabrutinib, aldesleukin, alemtuzumab, avapritinib and belantamab mafodotin.

Warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for these.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score (L5). No trials or publications address filgrastim for primary release disorder of platelets, and there is no plausible mechanistic link between G-CSF and this platelet function defect. The only trials found concern transplant conditioning and do not test filgrastim for the condition.

**To proceed, the following is needed:**
- Detailed mechanism of action data, to assess any biological link to platelet function
- Targeted literature review and preclinical data on G-CSF in platelet granule release disorders
- The TGA-approved PI, including approved indications, warnings and contraindications for Zarzio
- Assessment of whether any role is limited to supportive use in stem cell transplantation, rather than direct treatment of the platelet disorder
- Route compatibility assessment for the predicted indication, which has not yet been done
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

