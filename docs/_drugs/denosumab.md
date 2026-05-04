---
layout: default
title: Denosumab
parent: 僅模型預測 (L5)
nav_order: 146
evidence_level: L5
indication_count: 10
---

# Denosumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Denosumab: From Osteoporosis to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Denosumab is a fully human monoclonal antibody that inhibits RANKL (Receptor Activator of Nuclear factor Kappa-B Ligand), approved internationally for postmenopausal osteoporosis, cancer therapy–associated bone loss, prevention of skeletal-related events from bone metastases, and giant cell tumour of bone (marketed as Prolia and Xgeva).
The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy**,
with **no clinical trials** and **no publications** directly supporting this specific indication at present.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Osteoporosis; prevention of skeletal-related events in bone metastases; giant cell tumour of bone (international approvals) |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed (0 ARTG entries found in dataset) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

> **Data Quality Note:** The candidate identifier "TW-DB06643-multi" indicates this Evidence Pack was generated using a Taiwan (TFDA) regulatory dataset. Denosumab (Prolia/Xgeva) is understood to hold international approvals from the FDA, EMA, Health Canada, and TGA. Clinicians should independently verify current ARTG registration status via the TGA website before clinical use.

---

## Why is This Prediction Reasonable?

Denosumab is a targeted biological agent that works by binding and neutralising RANKL, a cytokine that drives osteoclast differentiation, activation, and survival. By blocking RANKL, denosumab halts osteoclast-mediated bone resorption. Beyond skeletal tissue, the RANKL/OPG (osteoprotegerin) signalling axis has been identified in various non-osseous tissues including the retina and retinal microvasculature, providing a biological rationale for this prediction.

The hypothesised mechanistic link to diabetic retinopathy rests on evidence that the RANKL/OPG pathway participates in retinal vascular inflammation and pericyte apoptosis — both central features of diabetic retinopathy. In people with diabetes, elevated circulating OPG (the endogenous RANKL decoy receptor) has been associated with retinal microvascular complications, suggesting dysregulation of this axis may contribute to disease progression. Since denosumab acts as a pharmacological mimic of OPG, it could theoretically dampen this pro-inflammatory retinal microenvironment.

However, for the specific subtype of **severe nonproliferative** diabetic retinopathy, this mechanism remains wholly hypothetical. The severity grading ("severe nonproliferative") does not represent a mechanistically distinct disease entity — it is a clinical staging classification. There is no direct preclinical (in vitro or animal) evidence and no clinical data targeting this subtype. The TxGNN global rank of 4,810 and the complete absence of any supporting studies firmly places this at the early exploratory hypothesis stage. Investigators interested in pursuing this hypothesis should first establish proof-of-concept in the broader diabetic retinopathy indication (TxGNN rank 2 in this pack, Evidence Level L4) before targeting the severity subtype specifically.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for severe nonproliferative diabetic retinopathy.

---

## Literature Evidence

Currently no related literature available for severe nonproliferative diabetic retinopathy.

---

## Australia Market Information

No ARTG entries were found in the current dataset for Denosumab.

> As noted above, this dataset reflects Taiwan TFDA registration data. For current Australian registration and full Product Information (PI), please search the [TGA ARTG Public Summary](https://www.tga.gov.au/resources/artg) directly using the search term "Denosumab".

---

## Cytotoxicity

Denosumab (Xgeva) is approved internationally for oncological indications including prevention of skeletal-related events from solid tumour bone metastases and unresectable giant cell tumour of bone. The cytotoxicity profile below applies when used in oncological contexts.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy (RANKL monoclonal antibody inhibitor — not a conventional cytotoxic agent) |
| Myelosuppression Risk | Low (myelosuppression is not a primary toxicity; serious infections including cellulitis have been reported due to immune modulation) |
| Emetogenicity Classification | Minimal (monoclonal antibody, not classified as emetogenic) |
| Monitoring Items | Serum calcium and phosphate (hypocalcaemia is the primary metabolic risk); renal function; dental assessment prior to initiation; bone markers if monitoring response |
| Handling Protection | Standard biohazard precautions for injectable biologics apply; cytotoxic handling regulations for antineoplastic chemotherapy agents do not apply |

---

## Safety Considerations

Detailed TGA-specific warnings and contraindications were not available in this dataset.

Please refer to the TGA-approved Product Information (PI) for Prolia and Xgeva for complete safety information. Key areas of known clinical importance include:

- **Hypocalcaemia:** Clinically significant hypocalcaemia has been reported, particularly in patients with renal impairment or inadequate calcium and vitamin D supplementation. Calcium levels must be corrected prior to initiating therapy.
- **Osteonecrosis of the jaw (ONJ):** Risk is increased with longer duration of therapy, concomitant corticosteroids, and poor oral hygiene. Dental review is recommended before starting treatment.
- **Atypical femoral fractures:** Reported with prolonged use, consistent with the broader antiresorptive drug class effect.
- **Serious infections:** Including skin infections (cellulitis, erysipelas) and endocarditis, due to the immunomodulatory effects of RANKL inhibition.
- **Rebound effect on discontinuation:** Rapid increase in bone turnover and risk of vertebral fractures has been documented following cessation; a transition plan to alternative antiresorptive therapy is recommended.

No drug–drug interaction data were available in this dataset. For DDI information, refer to the PI or consult an authorised drug interaction database.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.63%) to denosumab for severe nonproliferative diabetic retinopathy; however, there is currently no clinical trial data and no published literature directly examining this hypothesis for either this severity subtype or the broader diabetic retinopathy indication in the context of denosumab treatment. The mechanistic rationale (RANKL/OPG modulation of retinal microvasculature) is biologically plausible but entirely unvalidated at the preclinical level.

**To move this candidate forward, the following is needed:**

- **Step 1 — Preclinical validation:** Establish in vitro and animal model evidence confirming denosumab's effect on retinal pericyte survival, RANKL/OPG expression in diabetic retinal tissue, or vascular permeability in a diabetic retinopathy model.
- **Step 2 — Broaden the evidence search:** Conduct a systematic review on RANKL/OPG axis involvement in diabetic microvascular complications, including secondary analyses of existing real-world denosumab cohort studies (e.g., the PMID 38899553 cohort study on retinopathy outcomes in T2D patients receiving denosumab for osteoporosis).
- **Step 3 — Severity subtype justification:** If preclinical evidence is established for diabetic retinopathy broadly, a mechanistic or biomarker rationale for specifically targeting the severe nonproliferative subtype should be defined before designing a clinical trial.
- **Step 4 — Resolve data gaps:** Obtain full MOA details from DrugBank; retrieve TGA-approved PI for formal safety review; verify current ARTG registration status.
- **Step 5 — Safety profile review:** Given the known risks of denosumab (hypocalcaemia, ONJ, rebound fracture risk) and the immunomodulatory concern flagged in the dermatitis indication (rank 3 in this pack), a comprehensive benefit–risk assessment in the diabetic retinopathy population (who may have concurrent renal impairment) will be essential before any clinical translation.

---

*This report is generated for research evaluation purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. Refer to TGA-approved Product Information for prescribing guidance.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

