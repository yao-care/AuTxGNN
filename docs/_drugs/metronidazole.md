---
layout: default
title: Metronidazole
parent: Model Prediction Only (L5)
nav_order: 473
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Metronidazole: predicted new indication Pneumocystosis (evidence level L5). Approved use: Anaerobic bacterial infections, giardiasis, bacterial vaginosis…"
monitor_inn: "Metronidazole"
predicted_indications: ["pneumocystosis", "punctate epithelial keratoconjunctivitis", "ulcerative proctosigmoiditis", "nocardiosis", "postmenopausal atrophic vaginitis", "Cryptococcal meningitis", "papillary conjunctivitis", "myiasis", "cap polyposis", "ulceration of vulva"]
---

# Metronidazole
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

## Metronidazole: From Anaerobic and Protozoal Infections to Pneumocystosis
{: .text-alpha }

## One-Sentence Summary

Metronidazole is an antibacterial and antiprotozoal drug, originally used for anaerobic infections, giardiasis, bacterial vaginosis, rosacea and similar conditions.
The TxGNN model predicts it may be effective for **pneumocystosis**, but there are **no registered clinical trials** and only **10 publications**, none of which shows metronidazole efficacy against *Pneumocystis*.
The prediction is therefore best viewed as a model signal with a weak mechanistic basis, not an evidence-backed lead.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anaerobic bacterial infections, giardiasis, bacterial vaginosis, rosacea, peritonitis, intracranial abscess and others (approved indication text for the Australian product is not available) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Metronidazole is a nitroimidazole that is active against anaerobic bacteria and protozoa. Reduction of its nitro group produces DNA-damaging radicals.

*Pneumocystis* is now classified as a fungus, and the nitro-reduction mechanism does not give an established link to it. The retrieved literature is made up of general antiparasitic drug reviews and AIDS opportunistic infection reports. In these, metronidazole was used for coexisting infections such as amoebiasis, not for *Pneumocystis*. The standard treatment mentioned in the literature is trimethoprim-sulfamethoxazole.

The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1545596](https://pubmed.ncbi.nlm.nih.gov/1545596/) | 1992 | Review | Mayo Clin Proc | Overview of antiparasitic agents, including resistance and toxicity issues |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Review | Am Fam Physician | Drugs of choice: metronidazole for amoebic colitis and trichomoniasis; trimethoprim-sulfamethoxazole for pneumocystis pneumonia |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Review | Clin Pharmacokinet | Pharmacokinetic rationale for antiprotozoal therapy in normal and immunocompromised hosts |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Review | Clin Pharm | Therapies for infectious complications of AIDS, with *P. carinii* pneumonia the most common |
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Review | Top Antivir Med | HIV-related opportunistic infections remain relevant; no metronidazole benefit shown |
| [9 others] | – | – | – | Case reports and reviews are not listed individually because they do not address metronidazole use in pneumocystosis |

Note: [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) (1982, case report) and [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) (1990, case report) describe patients treated with metronidazole for other conditions who then developed *Pneumocystis* pneumonia. They do not support efficacy.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1621H | METRONIDAMED | Tablet 400 mg | Not available in the data compiled for this report |

## Safety Considerations

**Contraindications / conditions of concern (not label text):** liver failure and liver disease, epilepsy, kidney disease, haematological disease, neutropenia, leukopenia, agranulocytosis, blood coagulation disease, congestive heart failure, diabetes mellitus and diabetic ketoacidosis, gout, gallbladder disease, peripheral neuropathy and other peripheral nervous system disease, brain disease, optic nerve and visual pathway disease, non-infectious meningitis, dermatitis, pyoureter, and substance abuse/dependence.

**Drug Interactions:** 100 interactions were identified. Among those reviewed:
- **Major:** Ethanol (avoid concurrent use)
- **Moderate:** Paclitaxel, adalimumab, trastuzumab emtansine, ethinylestradiol, estradiol, butalbital, amobarbital, amiodarone, celecoxib, loperamide
- **Minor:** Abiraterone, tramadol, famotidine, salbutamol, alfuzosin, amisulpride, amitriptyline, anagrelide, propofol

Please also refer to the TGA-approved Product Information (PI) for the full warnings and contraindications, as label text was not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials and no supporting literature, and *Pneumocystis* is a fungus against which metronidazole has no known mechanism. Effective, established treatment already exists, so there is no clear unmet need to justify further investigation.

**To proceed, the following is needed:**
- Mechanistic or in vitro evidence of metronidazole activity against *Pneumocystis*
- Mechanism of action data for the drug
- Review of the TGA Product Information for approved indications, warnings and contraindications
- Comparison with the other predicted indications, as ulcerative proctosigmoiditis, cap polyposis, myiasis and vulvar ulceration have more biologically plausible, though still indirect, support (L4)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

