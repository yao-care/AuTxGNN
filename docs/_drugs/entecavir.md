---
layout: default
title: Entecavir
parent: Model Prediction Only (L5)
nav_order: 254
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Entecavir: predicted new indication Chronic hepatitis C virus infection (evidence level L5). Approved use: Chronic hepatitis B virus infection"
monitor_inn: "Entecavir"
predicted_indications: ["chronic hepatitis C virus infection", "HIV infectious disease", "hepatitis C virus infection", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "hepatitis, viral, animal", "hepatitis E virus infection", "hepatitis A virus infection"]
---

# Entecavir
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

# Entecavir: From Chronic Hepatitis B to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

Entecavir is a nucleoside analogue originally used to treat chronic hepatitis B virus infection.
The TxGNN model ranks **chronic hepatitis C virus infection** as its top predicted new indication, but the data compiled for this report show **no trial evidence of anti-HCV activity** (2 trials, both judged not directly relevant) and only indirect literature on HBV/HCV co-infection.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis B virus infection (the ARTG entry carries no indication text, so this comes from the TxGNN knowledge graph) |
| Predicted New Indication | Chronic hepatitis C virus infection |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 (L5 would apply if only the model prediction is counted; no HCV efficacy studies were found) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on known pharmacology, entecavir is a guanosine nucleoside analogue. Once phosphorylated to its triphosphate form, it competes with dGTP and inhibits all three activities of the HBV polymerase (priming, reverse transcription and DNA synthesis).

The prediction is **not mechanistically convincing**. HCV is an RNA virus replicated by the NS5B RNA-dependent RNA polymerase, and entecavir has no known activity against it. The high score most likely reflects the closeness of HBV and HCV in the knowledge graph (shared hepatotropic viral hepatitis biology) and the frequent HBV/HCV co-infection seen in practice. In co-infected patients entecavir is used to manage HBV, for example to prevent HBV reactivation during direct-acting antiviral (DAA) therapy for HCV. HCV itself is treated by the DAAs.

Other predictions for this drug are also weak. The only prediction with direct, on-label evidence is hepatitis B virus infection (rank 2, L1), which is the original indication rather than a new one. The remaining predictions (HIV, feline and simian immunodeficiency, hepatitis A and E, a neurodevelopmental disorder) have no supporting evidence of anti-pathogen activity.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | DAAs in HCV/HBV co-infection; studies HBV reactivation during anti-HCV treatment. Not evidence of anti-HCV activity by entecavir. |
| [NCT04405011](https://clinicaltrials.gov/study/NCT04405011) | N/A | Unknown | 60 | Nucleoside analogue prophylaxis (12 vs 24 weeks) against HBV reactivation in HCV/HBV co-infected patients on DAAs. The endpoint is HBV reactivation, not HCV clearance. |

Both trials were graded as not directly relevant to entecavir treating HCV. No ANZCTR-registered trials appear in the data compiled for this report.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34864158](https://pubmed.ncbi.nlm.nih.gov/34864158/) | 2022 | Randomised trial | Clin Gastroenterol Hepatol | Entecavir prevents HBV reactivation during DAA therapy in HCV/HBV dual infection (an HBV outcome, not HCV treatment) |
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Cohort | Viruses | HCV reactivation and viral load in anti-HCV-positive chronic hepatitis B patients on nucleos(t)ide analogues |
| [28230928](https://pubmed.ncbi.nlm.nih.gov/28230928/) | 2017 | Observational | J Gastroenterol Hepatol | HBV reactivation risk in chronic hepatitis C patients with HBV infection treated with DAAs |
| [35108715](https://pubmed.ncbi.nlm.nih.gov/35108715/) | 2022 | Observational | Dig Dis | Incidence and course of HBV reactivation in patients receiving DAAs for HCV |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Review | Expert Opin Pharmacother | Advances in treating HBV/HCV coinfection |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | Antivirals for hepatitis B and C and their effects on kidney function |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wien Med Wochenschr | Current treatment and future prospects in chronic hepatitis B and C |

The literature concerns HBV/HCV co-infection management. None of it shows entecavir treating HCV.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10279B | ENTECAVIR RBX | Tablet 0.5 mg (as monohydrate) | Not stated in the data compiled for this report |

The one entry is a valid, single-ingredient, oral product.

## Safety Considerations

Specific warnings and contraindications from the product label were not available. Please refer to the TGA-approved Product Information (PI) for safety information.

- **Knowledge graph contraindication signals** (not label text): impaired renal function, fatty liver disease, non-alcoholic steatohepatitis and lactic acidosis.
- **Drug interactions:** 44 interactions were identified, and the 20 listed in the data are all rated Moderate. Many involve agents that may affect renal function or are renally cleared: amphotericin B (including lipid, cholesteryl sulfate and liposomal forms), vancomycin, kanamycin, neomycin, polymyxin B, levofloxacin and amoxicillin. Others include metformin, the H2 blockers famotidine, ranitidine (including ranitidine bismuth citrate) and cimetidine, aminosalicylates (mesalazine, balsalazide, olsalazine, sulfasalazine) and orlistat.
- **Literature signals:** a case report describes entecavir-associated thrombocytopenia (PMID 34823407). A review notes class effects of oral nucleos(t)ide analogues, including myopathy, neuropathy and lactic acidosis (PMID 28261380).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (99.98%), but there is no plausible direct antiviral mechanism against HCV and no trial showing HCV efficacy. The related trials and papers address HBV reactivation in co-infected patients, which is a use within entecavir's existing HBV role. Current HCV treatment relies on DAAs.

**To proceed, the following is needed:**
- In vitro evidence of anti-HCV activity, or a mechanistic rationale beyond network proximity
- Detailed mechanism of action data (MOA)
- TGA Product Information warnings and contraindications (the label review is currently a blocking gap)
- Clarification of the approved indication wording on the ARTG entry
- For HBV/HCV co-infected patients, a separate evaluation as an HBV reactivation prophylaxis use, which is better supported by the trial and literature data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

