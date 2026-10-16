---
layout: default
title: Avelumab
parent: Model Prediction Only (L5)
nav_order: 74
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Avelumab: predicted new indication Human herpesvirus 8-related tumour (evidence level L5). Approved use: Cutaneous neuroendocrine carcinoma (Merkel cell carcinoma)"
monitor_inn: "Avelumab"
predicted_indications: ["human herpesvirus 8-related tumor", "middle ear neuroendocrine tumor", "malignant cutaneous granular cell skin tumor", "ectomesenchymoma", "adenosine deaminase deficiency", "reticular dysgenesis", "Immunoerythromyeloid hypoplasia", "non-severe combined immunodeficiency", "prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma"]
---

# Avelumab
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

# Avelumab: From Cutaneous Neuroendocrine Carcinoma to Human Herpesvirus 8-Related Tumour

## One-Sentence Summary

Avelumab is an anti-PD-L1 antibody, originally used to treat cutaneous neuroendocrine carcinoma (Merkel cell carcinoma).
The TxGNN model predicts it may be effective for **human herpesvirus 8-related tumours**, but **no clinical trials and no publications** were found in the data compiled for this report, so the prediction currently rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cutaneous neuroendocrine carcinoma (Merkel cell carcinoma) |
| Predicted New Indication | Human herpesvirus 8-related tumour |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Avelumab is known to be an anti-PD-L1 antibody, which blocks the PD-L1/PD-1 inhibitory pathway and may restore T-cell anti-tumour activity.

HHV-8-related tumours (for example Kaposi sarcoma and primary effusion lymphoma) involve viral immune evasion and upregulation of the PD-L1/PD-1 axis, so checkpoint blockade is biologically plausible. Related checkpoint inhibitors have been explored in Kaposi sarcoma. Merkel cell carcinoma is also a virus-associated skin cancer in many cases, which gives a loose conceptual link between the two settings.

This is a model prediction only. The very high score does not replace clinical evidence, and no trial or literature data were supplied to confirm it.

### Other Predicted Indications

The model also ranked the following. None has trial or literature support in the data compiled.

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Middle ear neuroendocrine tumour | 99.97% | L5 | Shared neuroendocrine lineage, but extremely rare and biologically different; PD-L1 dependence unestablished |
| 3 | Malignant cutaneous granular cell skin tumour | 99.97% | L5 | No demonstrated PD-L1 dependence |
| 4 | Ectomesenchymoma | 99.97% | L5 | No known mechanistic basis |
| 5-8 | Adenosine deaminase deficiency, reticular dysgenesis, immunoerythromyeloid hypoplasia, non-severe combined immunodeficiency | 99.91-99.95% | L5 | Mechanistically implausible; likely graph artefacts; immune activation could be harmful |
| 9 | Prostatic urethra urothelial carcinoma | 99.92% | L4 | Indirect support from approved urothelial carcinoma use (JAVELIN Bladder 100, Phase 3) |
| 10 | Kidney pelvis sarcomatoid transitional cell carcinoma | 99.91% | L4 | Indirect support from urothelial histology; site-specific data lacking |

Ranks 9 and 10 (urothelial tumours) have the most biologically credible extrapolation from avelumab's established urothelial carcinoma use, and may merit a closer look as research questions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for human herpesvirus 8-related tumour in the data compiled for this report.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11671G | Bavencio | Solution concentrate for I.V. infusion, 200 mg in 10 mL | Not available in the data compiled |

Australian approval status is based on the single entry above. Approved indication wording should be confirmed against the TGA-approved Product Information.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-L1 monoclonal antibody) |
| Myelosuppression Risk | Low; not a conventional cytotoxic. Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Low. Please refer to the PI |
| Monitoring Items | Please refer to the PI; typically includes thyroid, liver and renal function, and signs of immune-related adverse events |
| Handling Protection | Please refer to the PI and local institutional policy; not a conventional cytotoxic agent |

---

## Safety Considerations

- **Drug Interactions**: Three Major-level interactions were identified (source: DDInter):
  - Lenalidomide
  - Pomalidomide
  - Thalidomide

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has only model-based support (L5), with no registered trials or publications. The mechanistic link is plausible but unproven, and label safety information was not available for review.

**To proceed, the following is needed:**
- A systematic literature and trial registry search (including ANZCTR) for avelumab or PD-L1 blockade in HHV-8-related tumours such as Kaposi sarcoma
- Detailed mechanism of action data
- Review of the TGA-approved Product Information for warnings, contraindications and approved indications
- Evaluation of the urothelial sub-site predictions (ranks 9 and 10) using subgroup data from JAVELIN Bladder 100
- Assessment of the immunomodulatory drug interactions (lenalidomide, pomalidomide, thalidomide), particularly given the immunocompromised populations typical of HHV-8-related disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

