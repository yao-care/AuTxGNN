---
layout: default
title: Ivermectin
parent: Model Prediction Only (L5)
nav_order: 400
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
monitor_inn: "Ivermectin"
predicted_indications: ["vulvovaginal candidiasis", "esophageal candidiasis", "anogenital human papillomavirus infection", "vulvovaginitis", "candida glabrata", "congenital candidiasis", "neonatal candidiasis", "postmenopausal atrophic vaginitis", "candidiasis, invasive"]
description: "Ivermectin: predicted new indication Vulvovaginal candidiasis (evidence level L5). Approved use: Not recorded in the local data"
---

# Ivermectin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Ivermectin: Vulvovaginal candidiasis
{: .text-alpha }

## One-Sentence Summary

Ivermectin is an antiparasitic drug, originally used to treat strongyloidiasis and onchocerciasis.
The TxGNN model predicts it may be effective for **vulvovaginal candidiasis**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction. It is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Vulvovaginal candidiasis |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. In general, ivermectin is an antiparasitic that acts on glutamate-gated chloride channels in invertebrates. Fungal cells have no clear equivalent target.

Strongyloidiasis and onchocerciasis are parasitic infections, whereas vulvovaginal candidiasis is a fungal infection. No credible mechanistic link between the two can be established from the available data. The prediction may be a TxGNN model (deep learning) artefact, for example from co-occurring immunosuppression and opportunistic infections.

Other candidiasis-related predictions in the top 10 (oesophageal, congenital, neonatal and invasive candidiasis, and *Candida glabrata*) share the same weakness, as do the other vulvovaginal predictions (vulvovaginitis, vulvitis, postmenopausal atrophic vaginitis) and anogenital human papillomavirus infection. None has supporting trial evidence in the data compiled for this report.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for vulvovaginal candidiasis.

For context, two papers were linked to other predicted candidiasis indications, but neither addresses candidiasis:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35835488](https://pubmed.ncbi.nlm.nih.gov/35835488/) | 2022 | Case report | BMJ Case Reports | Disseminated strongyloidiasis after prolonged corticosteroid treatment. This concerns the approved antiparasitic use, not candidiasis. |
| [10098288](https://pubmed.ncbi.nlm.nih.gov/10098288/) | 1999 | Case report | Australasian Journal of Dermatology | Oral ivermectin (200 micrograms/kg) successfully treated crusted scabies in two immunocompromised children, with no side effects reported. One child had chronic mucocutaneous candidiasis. Not evidence for candidiasis treatment. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 2868Y | Stromectol | Tablet 3 mg | Not available in the data compiled for this report |

## Safety Considerations

- **Knowledge-graph contraindications (not label text)**: loiasis and filariasis.
- **Drug Interactions**: 100 interactions were identified in the interaction database. Those classed as **Moderate** include:
  - Aprepitant
  - Clarithromycin
  - Ethanol
  - Cobicistat
  - Deferasirox
  - Iodide I-123 and Iodide I-131
  - Dicoumarol
  - Fostamatinib
  - Warfarin
  - Abametapir (topical)

  Others, such as the proton pump inhibitors omeprazole and lansoprazole, the H2 blockers ranitidine and famotidine, the corticosteroids prednisone, prednisolone and dexamethasone, ursodeoxycholic acid and heparin, have an unclassified severity level.
- **Neonatal and paediatric use**: ivermectin is generally not recommended in very young or low-weight children. This is relevant to the predicted neonatal and congenital candidiasis indications.

Label warnings and contraindications were not available. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. No clinical trials or relevant publications were found, and there is no plausible antifungal mechanism in the data compiled for this report. The evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) and evidence of in vitro activity against *Candida* species
- Preclinical studies showing antifungal efficacy, and a justification for the route of administration (oral versus vaginal)
- The TGA-approved Product Information, including warnings, contraindications and approved indications for ARTG 2868Y
- A formal safety screening, including interaction review for co-prescribed medicines such as warfarin
- Consideration of whether another predicted indication has stronger supporting evidence, since none of the top 10 currently does
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

