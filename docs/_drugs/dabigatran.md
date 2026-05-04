---
layout: default
title: Dabigatran
parent: 僅模型預測 (L5)
nav_order: 136
evidence_level: L5
indication_count: 10
---

# Dabigatran
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

# Dabigatran: From Atrial Fibrillation/VTE to Hemoglobinopathy

## One-Sentence Summary

Dabigatran is a direct oral thrombin inhibitor (DOAC) approved internationally for stroke prevention in non-valvular atrial fibrillation and the treatment and prevention of venous thromboembolism, with no current ARTG registration in Australia.
The TxGNN model predicts it may be effective for **Hemoglobinopathy** (including β-thalassemia and sickle cell disease),
currently supported by **0 registered clinical trials** and **2 publications**, placing this prediction at evidence level **L4** (preclinical/mechanistic studies only).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Atrial fibrillation (stroke/systemic embolism prevention); Venous thromboembolism treatment and prevention |
| Predicted New Indication | Hemoglobinopathy |
| TxGNN Prediction Score | 98.43% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Dabigatran is a competitive, reversible direct inhibitor of thrombin (Factor IIa), targeting both free-circulating and fibrin-bound forms. Thrombin is the central effector protease of the coagulation cascade, responsible for converting fibrinogen to fibrin, activating platelets via PAR-1/PAR-4 receptors, and amplifying coagulation through positive feedback on Factors V, VIII, and XI. While detailed MOA data is not available in this Evidence Pack, dabigatran's established pharmacology as a direct thrombin inhibitor provides a rational mechanistic foundation for exploring its use in conditions characterised by thrombin-driven pathology.

Patients with haemoglobinopathies — particularly β-thalassemia and sickle cell disease — exist in a state of chronic systemic hypercoagulability. This arises from continuous intravascular haemolysis, endothelial injury (from repeated vaso-occlusion or iron overload), and the release of procoagulant microparticles from phosphatidylserine-exposing damaged red cells. Elevated thrombin generation has been documented in both conditions and is thought to drive microvascular thrombosis and vascular inflammatory cascades — a pathological overlap with dabigatran's known mechanism of action.

A key preclinical study in a sickle cell disease mouse model (PMID 24449213, *Blood* 2014) directly compared the contributions of FXa and thrombin to vascular inflammation, demonstrating thrombin's dominant role and providing experimental evidence for the potential of direct thrombin inhibition in this setting. A small observational series (PMID 37106692, *Biology* 2023) further documented NOAC use — including dabigatran — in transfusion-dependent β-thalassemia patients with supraventricular arrhythmias, establishing preliminary clinical feasibility. Overall mechanistic plausibility is moderate; however, robust clinical trial evidence for this indication is currently absent.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Dabigatran in haemoglobinopathy.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [37106692](https://pubmed.ncbi.nlm.nih.gov/37106692/) | 2023 | Systematic Review / Observational | *Biology* | Enrolled transfusion-dependent β-thalassemia patients receiving NOACs (including dabigatran) for thromboembolic prophylaxis of supraventricular arrhythmias; provides early clinical safety and feasibility data on NOAC use in this haemoglobinopathy population |
| [24449213](https://pubmed.ncbi.nlm.nih.gov/24449213/) | 2014 | Animal Study (Mouse Model) | *Blood* | In sickle BERK mice, dabigatran-mediated thrombin inhibition attenuated vascular inflammation more effectively than FXa inhibition with rivaroxaban, demonstrating thrombin's dominant role in SCD vascular pathology; primary mechanistic rationale for this prediction |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

> As Dabigatran has no current ARTG registration in Australia, and TGA PI data, contraindications, and drug interaction data were not available in this Evidence Pack, clinicians should consult the most recent international prescribing information (EU SmPC or US Package Insert for Pradaxa®) for comprehensive safety guidance — particularly regarding bleeding risk, renal function requirements, and the risks of premature discontinuation — before any clinical or research application.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
Current evidence is limited to one animal model providing direct mechanistic support for thrombin inhibition in sickle cell disease, and one small observational series suggesting clinical feasibility in β-thalassemia. This L4 evidence base is insufficient to support a clinical repurposing programme at this stage but is adequate to justify structured mechanistic investigation and exploratory study design.

**To proceed, the following is needed:**
- Retrieve full TGA/global Product Information (PI) to complete the safety, contraindication, drug interaction, and special population assessment (DG001 — currently blocking entry to S1 safety evaluation)
- Obtain confirmed MOA data from DrugBank (DG002) to refine mechanistic rationale specific to haemoglobinopathy coagulation pathways
- Commission or identify prospective observational data in β-thalassemia or sickle cell disease patients already receiving anticoagulation, using validated coagulation biomarkers (D-dimer, thrombin–antithrombin complexes, prothrombin fragment 1+2) as surrogate endpoints
- Design a Phase 2 pilot study (case series or single-arm registry) before committing to a randomised controlled trial
- Engage Australian haematology and haemoglobinopathy specialist networks, and liaise with ANZCTR for trial registration if a clinical study proceeds domestically

---

> ⚠️ **Disclaimer:** This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require formal clinical validation before any therapeutic application. All predictions should be interpreted in the context of current approved prescribing information and applicable regulatory requirements.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

