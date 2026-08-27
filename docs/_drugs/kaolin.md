---
layout: default
title: Kaolin
parent: 僅模型預測 (L5)
nav_order: 375
evidence_level: L5
indication_count: 10
---

# Kaolin
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

# Kaolin: From Topical Haemostatic/Diagnostic Reagent to Thrombotic Disease

## One-Sentence Summary

Kaolin (DB01575) has no confirmed therapeutic indication on record in this evidence pack; it is best known clinically as a mineral activator reagent in coagulation testing (kaolin clotting time, kaolin‑activated thromboelastography) and as the active ingredient in topical haemostatic trauma dressings (e.g. QuikClot Combat Gauze). The TxGNN model's top-ranked prediction is **Thrombotic Disease** (score **94.70%**), but on review this prediction is **not mechanistically or clinically supported** — kaolin is a procoagulant, not an anticoagulant, and nearly all of the **3 clinical trials** and **20 publications** identified describe kaolin only as a laboratory reagent used to monitor other patients' coagulation status, not as a treatment for thrombotic disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No confirmed original indication on record (Kaolin has no historical indication text captured in this evidence pack; its documented non-registered uses are as a coagulation-test reagent and topical haemostatic dressing) |
| Predicted New Indication | Thrombotic Disease |
| TxGNN Prediction Score | 94.70% |
| Evidence Level | L4 (mechanistic/preclinical signal only; direction of effect is contradictory) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Kaolin is not available from DrugBank in this evidence pack. Based on the totality of the collected trial and literature evidence, Kaolin is a naturally occurring aluminosilicate clay mineral whose principal pharmacological property is **contact activation of Factor XII**, which triggers the intrinsic coagulation cascade. This is precisely why kaolin is used as the standard activating reagent in kaolin-activated thromboelastography (TEG) and the kaolin clotting time (KCT) assay, and why kaolin-impregnated dressings (e.g. QuikClot Combat Gauze) are used to control external traumatic haemorrhage.

This mechanism runs **in the opposite direction** to what would be required to treat thrombotic disease: a drug that promotes clot formation is not a rational candidate to prevent or treat pathological thrombosis. Reviewing the underlying evidence confirms this — essentially every clinical trial and article "linking" Kaolin to thrombotic disease does so because kaolin was the **background assay reagent** used to measure coagulation status in patients being investigated for unrelated conditions (ECMO anticoagulation monitoring, liver transplant haemostasis, lupus anticoagulant testing, COVID-19 coagulopathy, etc.), not because kaolin itself was administered as a therapeutic agent for thrombosis.

Taken together, this indicates the TxGNN knowledge-graph prediction most likely arose from Kaolin's dense connectivity to coagulation-pathway nodes (through its role as a laboratory reagent) rather than from any genuine therapeutic signal. The mechanism, if anything, points toward a **safety concern** (procoagulant effect) rather than a repurposing opportunity for a prothrombotic disease.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02271126](https://clinicaltrials.gov/study/NCT02271126) | Phase 1 | Completed | 42 | Compared kaolin-activated thromboelastography (TEG) with aPTT for anticoagulation monitoring during ECMO. Kaolin used solely as the TEG activation reagent — a diagnostic tool study, not a kaolin treatment trial. |
| [NCT04246307](https://clinicaltrials.gov/study/NCT04246307) | N/A | Unknown | 50 | Compared ClotPro® with kaolin-activated TEG for assessing haemostasis during liver transplantation. Diagnostic method comparison only. |
| [NCT02887820](https://clinicaltrials.gov/study/NCT02887820) | N/A | Terminated | 15 | Pilot feasibility study of a kaolin-TEG-guided transfusion algorithm in ECMO patients. Trial was terminated early; no treatment-outcome data generated. |

**Note:** None of the identified trials test Kaolin as a therapeutic intervention for thrombotic disease. All three use kaolin exclusively as a coagulation-assay activator.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9624740](https://pubmed.ncbi.nlm.nih.gov/9624740/) | 1997 | Review | British Journal of Biomedical Science | Reviews laboratory diagnosis of lupus anticoagulant, listing the kaolin clotting time (KCT) as one of several diagnostic assays — kaolin as reagent, not therapy. |
| [26633836](https://pubmed.ncbi.nlm.nih.gov/26633836/) | 2016 | RCT/Cohort | Thrombosis and Haemostasis | Randomised, double-blind study of dabigatran's effects on coagulation in CAD patients on dual antiplatelet therapy; kaolin-activated assays used only as an outcome measurement tool. |
| [38396728](https://pubmed.ncbi.nlm.nih.gov/38396728/) | 2024 | Cohort | International Journal of Molecular Sciences | Prospective paired-measurement study comparing kaolin-activated TEG and conventional coagulation markers between COPD exacerbation and stable phases. |
| [32496878](https://pubmed.ncbi.nlm.nih.gov/32496878/) | 2020 | Cohort | Clinical and Applied Thrombosis/Hemostasis | Compared kaolin-activated TEG with conventional coagulation tests in patients with severe chronic liver disease — a diagnostic correlation study. |
| [34861681](https://pubmed.ncbi.nlm.nih.gov/34861681/) | 2022 | Cohort | Blood Advances | Investigated Factor XII (the same contact pathway kaolin activates) and fibrin clot dysregulation in severe COVID-19-associated thrombosis; mechanistic study, not a kaolin intervention. |
| [3931480](https://pubmed.ncbi.nlm.nih.gov/3931480/) | 1985 | — | American Journal of Obstetrics and Gynecology | Classic paper identifying lupus anticoagulant via aPTT/kaolin clotting time as a marker of thrombosis risk in pregnancy. |
| [32342930](https://pubmed.ncbi.nlm.nih.gov/32342930/) | 2020 | — | Malaysian Journal of Pathology | Single-centre review of lupus anticoagulant testing practice and performance, including kaolin-based assays. |
| [15821825](https://pubmed.ncbi.nlm.nih.gov/15821825/) | 2005 | — | Clinical and Applied Thrombosis/Hemostasis | Retrospective analysis of clinicohaematologic features in lupus anticoagulant patients, using kaolin clotting time among other assays. |
| [39067844](https://pubmed.ncbi.nlm.nih.gov/39067844/) | 2025 | — | Annals of Vascular Surgery | Explored the association between HbA1c and coagulation parameters (including kaolin-based TEG) in peripheral artery disease patients. |
| [41051078](https://pubmed.ncbi.nlm.nih.gov/41051078/) | 2026 | — | Journal of the American College of Surgeons | Evaluated objective coagulation assays, including kaolin-based TEG platelet mapping, for predicting thrombosis after PAD revascularisation. |

**Note:** All ten publications use kaolin as a coagulation-assay reagent or discuss thrombosis pathophysiology in populations unrelated to kaolin exposure. None report kaolin administered as a treatment for thrombotic disease.

## Australia Market Information

Kaolin is not currently registered on the Australian Register of Therapeutic Goods (ARTG). No marketed products, licences, or approved indications were identified for this ingredient in the Australian regulatory dataset.

## Safety Considerations

No formal TGA Product Information warnings, contraindications, or drug–drug interaction data are recorded for Kaolin in the safety database queried; the DDI query returned no results.

**Evidence-derived safety signal (identified during this review, not from the formal safety database):** The literature review for a related TxGNN-predicted indication (bronchitis, rank 2) surfaced a consistent body of occupational-medicine literature showing that chronic inhalation of kaolin dust causes **kaolinosis** (kaolin pneumoconiosis) and chronic bronchitis. This is a toxicity signal rather than supporting evidence for any respiratory indication, and it should be factored into any future risk assessment of Kaolin, particularly for inhaled or aerosolised formulations.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (thrombotic disease, 94.70%) is not supported on mechanistic or clinical grounds — Kaolin is a procoagulant (Factor XII contact activator), and virtually all "supporting" evidence reflects its use as a laboratory reagent rather than a therapeutic agent, meaning the direction of the predicted effect is inconsistent with the proposed indication. Reviewing the remaining nine TxGNN-ranked candidates for Kaolin reinforces this conclusion: most (ranks 3, 4, 5, 8, 9) have no clinical trial or literature support at all (L5, Hold), rank 2 (bronchitis) reflects a **toxicity signal** (occupational lung disease from kaolin dust inhalation) rather than a therapeutic opportunity, and the two candidates with more substantive evidence (rank 6 – vein disease; rank 10 – heart disease, both L3/Research Question) actually correspond to **topical haemostatic dressing use in traumatic vascular injury or cardiac surgery**, not systemic treatment of the labelled disease — an indication-label mismatch that requires manual clarification before it can be considered a genuine repurposing hypothesis.

**To proceed, the following is needed:**
- TFDA/TGA Product Information (PI) warnings, precautions and contraindications for Kaolin (currently a blocking data gap preventing safety screening)
- Confirmed DrugBank mechanism-of-action and pharmacological classification data
- Manual re-labelling and clinical review of the "vein disease" and "heart disease" candidates to determine whether the underlying application (topical/intraoperative haemostasis in trauma or cardiac surgery) should be evaluated as a distinct, narrowly-scoped device/product use case rather than as a systemic disease-treatment candidate
- No further action is recommended on the "thrombotic disease" or "bronchitis" predictions; both should be flagged and excluded from active repurposing consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

