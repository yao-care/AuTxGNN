---
layout: default
title: Valaciclovir
parent: Model Prediction Only (L5)
nav_order: 765
evidence_level: L5
indication_count: 10
---

# Valaciclovir
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

# Valaciclovir: From Herpesvirus Infection (Original Indication Not Recorded) to Rheumatoid Arthritis

## One-Sentence Summary

Valaciclovir is an oral prodrug of acyclovir, an antiviral that inhibits herpesvirus DNA polymerase. The approved indication text was not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but there are **0 clinical trials** and only **5 retrieved publications**, all case reports or cohort-type papers that do not test valaciclovir as a treatment for the disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the ARTG entry has no indication text) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 98.95% |
| Evidence Level | L4 (as assigned in the compiled data; see note below) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

*Note: The retrieved literature consists of case reports and a cohort-type paper with no direct evidence for valaciclovir in rheumatoid arthritis. On the rules in this framework, the evidence is effectively model prediction only (L5). The compiled data assigns L4.*

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, valaciclovir is a prodrug of acyclovir, which inhibits herpesvirus DNA polymerase. Its established use is in herpesvirus infections.

The link to rheumatoid arthritis is weak. The retrieved papers describe herpes zoster, Ramsay Hunt syndrome and herpes simplex occurring in rheumatoid arthritis patients on immunosuppressants such as tofacitinib and infliximab. In these cases, antivirals were used to treat the infectious complication, not the arthritis itself. They do not show that valaciclovir treats rheumatoid arthritis.

The high TxGNN score (98.95%) is a model output only and is not backed by clinical evidence. Other predicted indications (sclerosing cholangitis, diabetic nephropathy, bronchitis, congestive heart failure and several rare genetic syndromes) also have no trials or supporting literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35236687](https://pubmed.ncbi.nlm.nih.gov/35236687/) | 2022 | Case report | BMJ Case Reports | Herpes zoster meningitis in a rheumatoid arthritis patient on tofacitinib; the drug was stopped and the infection treated |
| [24660085](https://pubmed.ncbi.nlm.nih.gov/24660085/) | 2014 | Case report | Case Reports in Rheumatology | Ramsay Hunt syndrome after infliximab in rheumatoid arthritis; treated with valaciclovir and hydrocortisone, with complete recovery at 6 months |
| [23211260](https://pubmed.ncbi.nlm.nih.gov/23211260/) | 2012 | Cohort | British Journal of General Practice | Prescription of antivirals after herpes zoster in general practice; not specific to rheumatoid arthritis |
| [14600805](https://pubmed.ncbi.nlm.nih.gov/14600805/) | 2003 | Case report | Intensive Care Medicine | Disseminated tuberculosis, aspergillosis and herpes simplex infection in a patient on infliximab and methotrexate |
| [10220730](https://pubmed.ncbi.nlm.nih.gov/10220730/) | 1999 | Case report | Klinische Monatsblätter für Augenheilkunde | Bilateral neuroretinitis with zoster infection; not specific to rheumatoid arthritis |

None of these papers evaluates valaciclovir as a treatment for rheumatoid arthritis.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 5480K | Valtrex | Tablet 500 mg (as hydrochloride), oral | Not available in the compiled data |

## Safety Considerations

- **Drug Interactions**: 100 potential interactions were identified in the interaction database searched. The main ones listed at Moderate level are:
  - Aminosalicylates: mesalazine, balsalazide, olsalazine, sulfasalazine
  - Aminoglycosides and related antibiotics: paromomycin, neomycin, streptomycin
  - Trospium

  Cimetidine is listed at Minor level. Several others (for example calcitriol, pantoprazole, glimepiride, doxycycline, metformin, omeprazole, morphine) are listed with unknown severity.
- **Renal considerations**: Valaciclovir/acyclovir requires renal dose adjustment, which is relevant to any future evaluation in patients with renal impairment.

For warnings and contraindications, please refer to the TGA-approved Product Information (PI).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no registered clinical trials, and the retrieved literature describes antiviral treatment of infections in rheumatoid arthritis patients, not treatment of the arthritis. No mechanistic link has been established.

**To proceed, the following is needed:**
- Mechanism of action data, and a plausible biological rationale for antiviral activity in rheumatoid arthritis (for example, a role for herpesvirus reactivation)
- Preclinical or clinical studies directly testing valaciclovir in rheumatoid arthritis
- The TGA Product Information, including approved indications, warnings and contraindications
- A safety review for rheumatoid arthritis populations, including renal function and interactions with immunosuppressants and other commonly co-prescribed drugs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

