---
layout: default
title: Amifampridine
parent: 僅模型預測 (L5)
nav_order: 39
evidence_level: L5
indication_count: 10
---

# Amifampridine
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

# Amifampridine: From Lambert-Eaton Myasthenic Syndrome to Glaucoma

## One-Sentence Summary

Amifampridine (3,4-diaminopyridine; 3,4-DAP) is a voltage-gated potassium channel (VGKC) blocker approved in the US and Europe for Lambert-Eaton Myasthenic Syndrome (LEMS) — a rare autoimmune paraneoplastic neuromuscular disorder — but is not currently registered in Australia.
The TxGNN model ranks **Glaucoma** as the highest-priority repurposing candidate with a prediction score of **99.71%**; however, this is an **L5 (model-only) prediction** with **no supporting clinical trials or published literature** identified.
Across all 10 predicted indications in this multi-indication Evidence Pack, three paraneoplastic conditions (ranks 7, 8, and 10) carry indirect mechanistic plausibility (L4) and are flagged as **Research Questions**, with Paraneoplastic Cerebellar Degeneration (rank 10) representing the most scientifically grounded candidate.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Australia; internationally approved for Lambert-Eaton Myasthenic Syndrome (LEMS) |
| Predicted New Indication | Glaucoma (Rank 1 of 10 predicted) |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 — model prediction only, no supporting studies identified |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on established pharmacological literature, Amifampridine (3,4-DAP) acts as a **voltage-gated potassium channel (VGKC) blocker**. By blocking presynaptic K⁺ channels, it prolongs the depolarisation phase of the action potential, enhances calcium (Ca²⁺) influx at the nerve terminal, and thereby increases acetylcholine release at the neuromuscular junction — the mechanism underlying its efficacy in LEMS.

For glaucoma, the theoretical connection rests on the known presence of VGKC in the **ciliary body epithelium** and **trabecular meshwork**, two structures that regulate aqueous humour production and drainage, and thus intraocular pressure (IOP). In principle, pharmacological VGKC modulation in these tissues could influence IOP. However, there is currently **no direct preclinical, laboratory, or clinical evidence** linking Amifampridine to glaucoma outcomes. The high TxGNN prediction score most likely reflects indirect connectivity between ion channel-related nodes in the Knowledge Graph rather than a validated therapeutic pathway.

This glaucoma prediction should therefore be treated as a **computational hypothesis only**, pending dedicated preclinical investigation. Among the 10 predictions in this pack, the three paraneoplastic indications (ranks 7, 8, 10) carry substantially more mechanistic weight, as they share the VGKC/VGCC autoimmune pathophysiology already established in LEMS.

---

## Clinical Trial Evidence

Currently no clinical trials investigating Amifampridine for glaucoma have been registered in ClinicalTrials.gov or the ICTRP registry (as of 4 April 2026).

---

## Literature Evidence

Currently no published literature investigating Amifampridine for glaucoma has been identified in PubMed (as of 4 April 2026).

---

## Australia Market Information

Amifampridine is not registered with the Therapeutic Goods Administration (TGA) and holds **no ARTG entries**. It is currently not marketed in Australia in any dosage form.

For context, the drug is approved internationally under the following frameworks:

| Jurisdiction | Product | Approval | Indication |
|-------------|---------|----------|-----------|
| USA (FDA) | Firdapse® (amifampridine phosphate) | November 2018 | LEMS in adults |
| USA (FDA) | Ruzurgi® (amifampridine) | May 2019 | LEMS in patients aged 6 and older |
| Europe (EMA) | Firdapse® | December 2009 | LEMS in adults |

Healthcare professionals seeking to prescribe Amifampridine in Australia for LEMS or for investigational purposes may consider the TGA **Special Access Scheme (SAS Category B)** or the **Authorised Prescriber** pathway. The existing FDA and EMA approvals will support any such application.

---

## Summary of All 10 Predicted Indications

This Evidence Pack covers 10 TxGNN-predicted indications. The table below provides a complete overview to support prioritisation decisions:

| Rank | Indication | TxGNN Score | Evidence Level | Decision | Mechanistic Notes |
|------|-----------|-------------|---------------|----------|------------------|
| 1 | Glaucoma | 99.71% | L5 | Hold | Theoretical VGKC in ciliary body/trabecular meshwork; no direct evidence |
| 2 | Acute Intermittent Porphyria | 99.32% | L5 | Hold | No mechanistic link; KG artefact via neurological symptom co-occurrence |
| 3 | Esophageal Varices with Bleeding | 98.77% | L5 | Hold | Portal hypertension pathology unrelated to VGKC |
| 4 | Esophageal Varices without Bleeding | 98.77% | L5 | Hold | Identical score to Rank 3; duplicate KG nodes |
| 5 | Porphyria | 98.51% | L5 | Hold | Haem synthesis pathway unrelated to VGKC |
| 6 | Primary Immunodeficiency (p14 Deficiency) | 98.39% | L5 | Hold | Ultra-rare disease (<20 cases globally); mechanism unrelated; likely KG artefact |
| 7 | **Paraneoplastic Limbic Encephalitis** | 98.31% | **L4** | **Research Question** | Indirect: LGI1/CASPR2/VGCC antibody subtype overlaps with LEMS autoimmune mechanism |
| 8 | **Paraneoplastic Polyneuropathy** | 98.26% | **L4** | **Research Question** | Indirect: LEMS can co-present with sensorimotor neuropathy; anti-VGCC/Hu antibody overlap |
| 9 | Varicose Disease | 98.08% | L5 | Hold | Venous valve/wall structural pathology unrelated to VGKC; no supporting evidence |
| 10 | **Paraneoplastic Cerebellar Degeneration** | 97.99% | **L4** | **Research Question** | Strongest candidate: SCLC-associated, shared P/Q-type VGCC autoimmunity with LEMS; 2 contextual publications identified |

### L4 Highlight: Paraneoplastic Cerebellar Degeneration (Rank 10)

Among all 10 predictions, **Paraneoplastic Cerebellar Degeneration (PCD)** represents the most scientifically grounded repurposing hypothesis in this batch:

1. **High co-morbidity with LEMS**: In small cell lung cancer (SCLC) patients, PCD and LEMS frequently co-occur, with reported co-morbidity rates approaching 25%.
2. **Shared autoimmune mechanism**: Both conditions are associated with anti-**P/Q-type VGCC** (voltage-gated calcium channel) antibodies. Cerebellar Purkinje cells are particularly rich in P/Q-type VGCC (CACNA1A), making them vulnerable to the same antibody-mediated Ca²⁺ signalling impairment implicated in LEMS.
3. **Translational rationale**: Amifampridine's mechanism of enhancing Ca²⁺-dependent neurotransmitter release could theoretically provide partial compensation for antibody-mediated VGCC signal loss in cerebellar circuits — though direct evidence is absent.
4. **Indirect supporting literature**: Two LEMS-focused publications (see below) describe Amifampridine use in SCLC-associated, anti-VGCC-positive LEMS cases that are pathophysiologically contiguous with PCD.

### Literature Evidence — Paraneoplastic Cerebellar Degeneration Context

The following publications were identified in relation to Paraneoplastic Cerebellar Degeneration (rank 10). Note: both address LEMS directly rather than PCD, and are cited as **indirect contextual evidence** only.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [15034474](https://pubmed.ncbi.nlm.nih.gov/15034474/) | 2004 | Review | Revue neurologique | Comprehensive LEMS review: ~60% paraneoplastic (SCLC-associated); anti-VGCC antibody role in both peripheral and central nervous system involvement; 3,4-DAP efficacy in symptomatic LEMS management established |
| [29386498](https://pubmed.ncbi.nlm.nih.gov/29386498/) | 2018 | Retrospective Cohort | Rinsho shinkeigaku (Clinical Neurology) | Retrospective study of 9 LEMS patients treated with 3,4-DAP; 8/9 showed improvement in activities of daily living (primarily limb weakness); 5/9 had SCLC; anti-VGCC antibody positive in 7/9; provides real-world evidence for 3,4-DAP in SCLC-associated, antibody-positive LEMS |

---

## Safety Considerations

Please refer to the TGA Special Access Scheme documentation and the relevant international Product Information (PI) — particularly the FDA Firdapse® PI and EMA SmPC — for complete safety information. Safety data specific to the Australian context is not available in the current Evidence Pack.

> **Note for prescribers**: Based on international regulatory documents (to be verified against current PI before use), key safety considerations include a **lowered seizure threshold** (use with extreme caution or avoid in patients with epilepsy or a history of seizures), monitoring for **hypersensitivity reactions**, and periodic review of **hepatic enzyme levels**. These are provided as general orientation only and do not substitute for a full PI review.

---

## Conclusion and Next Steps

**Decision: Hold** (for Glaucoma, the top-ranked TxGNN prediction)

**Rationale:**
The highest-ranked prediction (Glaucoma, 99.71%) is a purely computational finding with no mechanistic evidence, no registered clinical trials, and no supporting literature. Across all 10 predictions in this multi-indication pack, only three paraneoplastic conditions (ranks 7, 8, 10) demonstrate indirect mechanistic plausibility at L4 — most notably Paraneoplastic Cerebellar Degeneration, which shares the core VGCC autoimmune mechanism already validated in LEMS. None of the 10 predicted indications are currently registered in Australia, and no ARTG entries exist for this drug.

**To proceed, the following is needed:**

- **Glaucoma (Rank 1 — current top prediction):** Preclinical studies evaluating VGKC blockade effects on aqueous humour dynamics and intraocular pressure in validated animal models before any clinical consideration is warranted.
- **Paraneoplastic Cerebellar Degeneration (Rank 10 — highest priority for clinical translation):** Systematic chart review of SCLC patients with co-morbid LEMS and PCD who have received Amifampridine, assessing cerebellar symptom response as a secondary endpoint; prospective pilot study design in collaboration with neuro-oncology centres.
- **Paraneoplastic Limbic Encephalitis and Polyneuropathy (Ranks 7–8):** Structured literature review targeting LGI1/CASPR2/VGCC antibody subtype cases; specialist consultation with autoimmune neurology teams to assess feasibility of observational case series.
- **Australian access pathway:** Evaluate TGA SAS Category B application for LEMS treatment — the established FDA and EMA approvals provide a strong basis for a compassionate access submission.
- **Safety documentation:** Obtain and formally document the complete contraindication, warning, and drug interaction profile from FDA/EMA product information; assess applicability to the Australian patient population.
- **MOA documentation:** Complete DrugBank API query to formally register the VGKC blocking mechanism in the evidence system and enable automated mechanistic linkage analysis.

---

> **Disclaimer**: This report is intended for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All predictions are generated by the TxGNN computational model and must be interpreted in the context of supporting evidence. Always consult the TGA-approved or relevant Product Information before clinical use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

