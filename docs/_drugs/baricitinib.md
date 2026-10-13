---
layout: default
title: Baricitinib
parent: Model Prediction Only (L5)
nav_order: 81
evidence_level: L5
indication_count: 10
---

# Baricitinib
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

# Baricitinib: From Rheumatoid Arthritis to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Baricitinib is an oral JAK inhibitor originally used to treat rheumatoid arthritis.
The TxGNN model predicts it may be effective for **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, an ultra-rare developmental condition.
However, there are currently **no clinical trials** and **no publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis |
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, baricitinib is a Janus kinase (JAK1/JAK2) inhibitor class medicine. Its efficacy in rheumatoid arthritis is established, but a mechanistic link to the predicted condition has not been demonstrated.

Colobomatous microphthalmia-rhizomelic dysplasia syndrome is an ultra-rare developmental syndrome. JAK-STAT-mediated inflammation is not an evident driver of this type of disease, so the very high score is best read as a computational prediction, and possibly a knowledge-graph artefact, rather than a biologically supported lead.

### Other Predicted Indications (for context)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Brachydactyly-syndactyly syndrome | 99.94% | L5 | Congenital limb malformation; no plausible JAK link |
| 3 | Indolent plasma cell myeloma | 93.31% | L5 | JAK/STAT3 (IL-6) pathway gives a theoretical rationale; no studies |
| 4 | WHIM syndrome | 93.12% | L5 | CXCR4-driven; established therapies target CXCR4 directly |
| 5 | Plasma cell myeloma | 91.83% | L4 | Single case report, indirect evidence only |
| 6 | Myeloid leukaemia | 91.01% | L4 | One GVHD-prevention trial; supportive care, not antileukaemic |

Of these, myeloid leukaemia and plasma cell myeloma have the most data and are the more biologically plausible directions for follow-up.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked predicted indication.

For context, the only trial found among the top-ranked predictions relates to rank 6 (myeloid leukaemia):

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT06475820](https://clinicaltrials.gov/study/NCT06475820) | Phase 2/3 | Active, not recruiting | 150 | Pilot study of GVHD prevention using post-transplant cyclophosphamide with abatacept, vedolizumab and baricitinib in children and young adults with haematological malignancies after stem cell transplant. Targets GVHD, not leukaemia treatment. |

## Literature Evidence

Currently no related literature available for the top-ranked predicted indication.

For context, the following items relate to lower-ranked predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34856779](https://pubmed.ncbi.nlm.nih.gov/34856779/) | 2021 | Case report | Minerva Med | Concurrent treatment of critical COVID-19 and newly diagnosed high-risk myeloma (thalidomide, methylprednisolone, tocilizumab, baricitinib). Baricitinib was likely used for COVID-19, so antimyeloma efficacy cannot be inferred. |
| [36569952](https://pubmed.ncbi.nlm.nih.gov/36569952/) | 2022 | Review | Front Immunol | Repurposing BCL-2 and JAK1/2 inhibitors for HIV-1 and other viral infections. Not relevant to efficacy in leukaemia. |
| [34730109](https://pubmed.ncbi.nlm.nih.gov/34730109/) | 2021 | Preclinical | J Clin Invest | Antibody-drug conjugates plus JAK inhibitors enabled MHC-mismatched allogeneic stem cell transplantation in experimental models. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11437Y | Olumiant | Tablet 2 mg | Not available in the data compiled for this report |

Note: the registered ARTG entry is a single-ingredient oral tablet. Approved indication text was not available in the data compiled for this report.

## Safety Considerations

**Drug Interactions** (100 interactions identified from DDInter; main examples below):

- **Major:** Corticosteroids (hydrocortisone, prednisolone, prednisone, dexamethasone, betamethasone, budesonide, triamcinolone including ophthalmic), deferiprone, ibritumomab tiuxetan, iobenguane (I-131), tositumomab (I-131)
- **Moderate:** Morphine (including liposomal), opium, acetylsalicylic acid, nitisinone
- **Minor:** Zinc salts (acetate, gluconate, sulfate)

Please also refer to the TGA-approved Product Information (PI) for warnings and contraindications. For context, the rationale for heparin cofactor 2 deficiency (rank 9) noted that baricitinib carries a thrombosis/VTE warning.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The very high TxGNN score (99.94%) is not backed by any clinical trials, publications or plausible mechanistic link, and the condition is an ultra-rare developmental syndrome with no evident JAK-STAT involvement. Evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Mechanism of action data (MOA) and a documented biological link between JAK1/2 inhibition and the predicted condition
- Preclinical or case-level evidence in the predicted condition
- TGA Product Information safety data (warnings and contraindications), as well as approved indication text for the ARTG entry
- If a haematological direction is preferred, a focused evidence review for plasma cell myeloma or myeloid leukaemia, where the JAK/STAT rationale is more plausible
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

