---
layout: default
title: Kaolin
parent: Model Prediction Only (L5)
nav_order: 403
evidence_level: L5
indication_count: 10
---

# Kaolin
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

# Kaolin: From an Unspecified Original Indication to Thrombotic Disease

## One-Sentence Summary

Kaolin is a naturally occurring clay mineral that is listed on the Australian market, but the data compiled for this report contain no approved indication text for it.
The TxGNN model predicts it may be effective for **thrombotic disease**, but there are **no registered clinical trials** and the **18 publications** retrieved mostly use kaolin as a laboratory assay reagent rather than as a treatment.
Kaolin is pro-coagulant, so this prediction is mechanistically implausible and is most likely a knowledge-graph artefact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 94.70% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Kaolin is known to activate the contact (factor XII) pathway of coagulation. It is widely used in vitro as a reagent in activated partial thromboplastin time (aPTT), kaolin clotting time and kaolin-activated thromboelastography.

This is the opposite of what a thrombosis treatment needs. A pro-coagulant agent would be expected to be unhelpful, or to worsen thrombosis. The retrieved literature uses kaolin only as a laboratory assay tool (for example in thromboelastography and lupus anticoagulant testing), and none of it tests kaolin as a therapy.

The high TxGNN score most likely reflects a graph association between kaolin and coagulation, not a therapeutic signal. The same applies to the other top predictions:

- **Bronchitis:** the literature describes kaolin dust inhalation causing pneumoconiosis, which is a harm signal rather than a benefit.
- **Heparin cofactor 2 deficiency:** one basic biochemistry paper where kaolin is only an assay activator.
- **Antithrombin deficiency type 2, factor 5 excess with spontaneous thrombosis, interventricular septum aneurysm, Jeune syndrome situs inversus:** no literature or trials were found.
- **Vein disease and heart disease:** there is limited indirect evidence for topical kaolin-based haemostatic dressings in animal vascular injury models and a small surgical experience report. This concerns bleeding control, not treatment of the disease itself.
- **Thrombophilia:** kaolin appears as an assay activator for measuring hypercoagulability, not as a treatment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The retrieved publications are listed below. None assesses kaolin as a treatment for thrombotic disease. The studies are chosen to show the type of evidence available, with reviews and cohort studies prioritised. No RCT of kaolin was identified.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9624740](https://pubmed.ncbi.nlm.nih.gov/9624740/) | 1997 | Review | Br J Biomed Sci | Reviews lupus anticoagulant pathogenesis and diagnosis, including the kaolin clotting time as a laboratory test |
| [38142487](https://pubmed.ncbi.nlm.nih.gov/38142487/) | 2024 | Systematic review / meta-analysis | Thromb Res | Whole blood viscoelastic testing parameters and mortality in COVID-19 pneumonia (diagnostic use) |
| [38396728](https://pubmed.ncbi.nlm.nih.gov/38396728/) | 2024 | Cohort | Int J Mol Sci | Thrombelastography and coagulation markers in COPD exacerbation versus stable phase |
| [34861681](https://pubmed.ncbi.nlm.nih.gov/34861681/) | 2022 | Cohort | Blood Adv | Altered fibrin clot structure and fibrinolysis contribute to thrombosis risk in severe COVID-19 |
| [32342930](https://pubmed.ncbi.nlm.nih.gov/32342930/) | 2020 | Cohort | Malays J Pathol | Performance of lupus anticoagulant tests in a single centre |
| [3931480](https://pubmed.ncbi.nlm.nih.gov/3931480/) | 1985 | Review | Am J Obstet Gynecol | Lupus anticoagulant in pregnancy, detected by aPTT or kaolin clotting time |
| [8578480](https://pubmed.ncbi.nlm.nih.gov/8578480/) | 1995 | Review | Thromb Haemost | Clinical presentations of antiphospholipid-protein antibodies; kaolin clotting time is one detection test |
| [39067844](https://pubmed.ncbi.nlm.nih.gov/39067844/) | 2025 | Observational | Ann Vasc Surg | HbA1c and coagulation profiles in peripheral artery disease after revascularisation |
| [41051078](https://pubmed.ncbi.nlm.nih.gov/41051078/) | 2026 | Observational | J Am Coll Surg | Coagulation assays for predicting thrombosis in peripheral artery disease |
| [26633836](https://pubmed.ncbi.nlm.nih.gov/26633836/) | 2016 | RCT | Thromb Haemost | Dabigatran effects on coagulation in coronary artery disease patients on dual antiplatelet therapy (kaolin used only as an assay; not a kaolin trial) |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 7348R | Not available | Not available | Not available |

---

## Safety Considerations

**Drug Interactions:** The data compiled for this report list 84 interactions. The first 20 retrieved include:

- **Major:** dolutegravir, bictegravir
- **Moderate:** doxycycline, tetracycline, alendronic acid, risedronic acid, ibandronate, allopurinol, proguanil, atropine, baloxavir marboxil, and opioids (codeine, dihydrocodeine, morphine, benzhydrocodone, butorphanol)
- **Minor:** beta-blockers (acebutolol, atenolol, betaxolol, bisoprolol)

Kaolin is an adsorbent, which is consistent with reduced absorption of co-administered oral drugs. This is an inference, not stated in the data. Separating administration times is therefore worth considering.

**Other safety signals from the retrieved literature:**
- Inhaled kaolin dust is associated with pneumoconiosis (kaolinosis).
- A 1971 report describes coagulation defects after intravenous kaolin.
- Because kaolin is pro-coagulant, use in a thrombotic or hypercoagulable condition could be harmful.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications, as none were available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction rests on a graph score alone, with no clinical trials and no literature testing kaolin as a treatment. Its pro-coagulant mechanism points away from benefit in thrombotic disease, and possibly towards harm.

**To proceed, the following is needed:**
- A plausible therapeutic mechanism, which currently appears absent for the thrombotic predictions
- Mechanism of action data and the original approved indication for ARTG entry 7348R
- TGA Product Information warnings and contraindications, which are needed before any safety screening
- A review of the interaction profile, particularly the two major interactions with the HIV integrase inhibitors dolutegravir and bictegravir
- Consideration of whether the topical haemostatic use of kaolin dressings (vein disease, heart disease) is a more credible line of inquiry. This would be a bleeding-control use, not treatment of the predicted diseases themselves.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

