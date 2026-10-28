---
layout: default
title: Leflunomide
parent: Model Prediction Only (L5)
nav_order: 417
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
monitor_inn: "Leflunomide"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
description: "Leflunomide: predicted new indication Brachydactyly-syndactyly syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Leflunomide
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

## Leflunomide: Brachydactyly-syndactyly syndrome
{: .text-alpha }

## One-Sentence Summary

Leflunomide is an oral immunomodulatory drug originally used to treat rheumatoid arthritis and psoriatic arthritis.
The TxGNN model predicts it may be effective for **brachydactyly-syndactyly syndrome**, a congenital developmental malformation syndrome.
This prediction has **no clinical trials** and **no publications** behind it, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Leflunomide's active metabolite (A771726, also called teriflunomide) is known to inhibit dihydroorotate dehydrogenase (DHODH). This depletes pyrimidine pools and dampens the proliferation of rapidly dividing immune cells. That mechanism explains its efficacy in rheumatoid and psoriatic arthritis.

The link to brachydactyly-syndactyly syndrome is weak. It is a developmental malformation syndrome, and an antimetabolite-type immunomodulator is unlikely to correct a congenital limb malformation. The very high TxGNN score (0.9993) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Leflunomide is also teratogenic, which raises safety concerns for any use in a developmental context.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 13940Q | Arava | Tablet 10 mg (oral) | Not stated in the data compiled |

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text). These include:
  - Liver: liver failure, liver disease, gallbladder disease, chronic hepatitis B and C virus infection.
  - Kidney: kidney disease.
  - Blood: thrombocytopenia, neutropenia (including congenital forms), agranulocytosis, pancytopenia, anaemia.
  - Nerves: peripheral neuropathy.
  - Lung and infection: interstitial lung disease, pneumocystosis, aspergillosis.
- **Drug Interactions**: The interaction query returned 100 records; 20 are shown in the data compiled. Most listed interactions are rated Major, including:
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide.
  - Antidiabetics: acarbose, pioglitazone.
  - Others: acetylsalicylic acid, bupropion, clarithromycin, minocycline, naltrexone, oxandrolone, oxymetholone, chenodeoxycholic acid.
  - Moderate: metronidazole, chlorpropamide, acetohexamide.
  - Minor: zinc sulfate, zinc acetate.
- **Teratogenicity**: Leflunomide is teratogenic, a particular concern for developmental disorders.

Please also refer to the TGA-approved Product Information (PI) for full warnings and contraindications, as label-based data were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials, no literature, and no plausible mechanism for a congenital malformation syndrome. Leflunomide's teratogenicity adds a safety concern.


**To proceed, the following is needed:**
- A credible mechanistic rationale linking DHODH inhibition to this disorder
- Preclinical or case-level evidence of benefit
- Mechanism of action data from DrugBank
- TGA PI warnings and contraindications, with a pregnancy and reproductive risk assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

