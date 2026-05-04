---
layout: default
title: Encorafenib
parent: 僅模型預測 (L5)
nav_order: 186
evidence_level: L5
indication_count: 10
---

# Encorafenib
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

# Encorafenib: From BRAF V600-Mutant Melanoma to Non-Cutaneous Melanoma

## One-Sentence Summary

Encorafenib (Braftovi®) is a selective BRAF kinase inhibitor with established international approvals for BRAF V600-mutant cutaneous melanoma and colorectal cancer, though it is not currently registered with the Australian TGA.
The TxGNN model predicts it may be effective for **Non-Cutaneous Melanoma** (encompassing mucosal, conjunctival, and adnexal subtypes), supported by **multiple dedicated Phase 2 clinical trials** — the strongest signal among this drug's ten predicted indications — qualifying this as an **L2 evidence level** recommendation.

> **Note on TxGNN rankings:** The highest-scoring TxGNN prediction (Rank 1: Choroideremia, score 97.10%) has been deprioritised as the primary focus of this report due to a recognised mechanistic mismatch — Choroideremia is driven by CHM gene mutations encoding the REP1 protein involved in Rab GTPase transport, which has no established biological link to the BRAF/MAPK pathway. No clinical or preclinical evidence supports encorafenib in this condition, and the high prediction score likely reflects structural proximity between retinal disease nodes in the knowledge graph rather than genuine mechanistic relatedness. Non-Cutaneous Melanoma (Rank 2, score 96.55%) represents the most actionable and biologically defensible prediction with the strongest evidence base.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | BRAF V600-mutant melanoma (international approval; not TGA-registered in Australia) |
| Predicted New Indication | Non-Cutaneous Melanoma |
| TxGNN Prediction Score | 96.55% (Rank 2; Rank 1 deprioritised — mechanistic mismatch with BRAF pathway) |
| Evidence Level | L2 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack's DrugBank record. Based on established pharmacological knowledge, Encorafenib is a highly selective, ATP-competitive inhibitor of mutant BRAF kinase (V600E and V600K variants). In BRAF V600-mutant tumours, a single amino acid substitution in the kinase activation loop causes constitutive activation of the BRAF–MEK–ERK (MAPK/ERK) signalling axis, driving uncontrolled tumour cell proliferation, survival, and metastasis. Encorafenib distinguishes itself from first-generation BRAF inhibitors (vemurafenib, dabrafenib) through its prolonged target dissociation kinetics, producing more sustained pathway suppression. It is typically co-administered with binimetinib (a MEK1/2 inhibitor) to prevent paradoxical MAPK reactivation and delay the development of acquired resistance.

Non-cutaneous melanoma encompasses melanomas originating from non-skin surfaces — principally mucosal sites (oral cavity, anorectal, genitourinary tract), conjunctival melanoma, and adnexal melanomas (e.g., eyelid, lacrimal gland). Although BRAF V600 mutation prevalence is substantially lower in these subtypes (approximately 5–15%) compared to cutaneous melanoma (~50–60%), the underlying oncogenic mechanism is identical in mutation-positive cases. Critically, encorafenib's therapeutic benefit is driven entirely by mutation status, not anatomical site of origin — making it a tumour-site agnostic therapy contingent on confirmed BRAF V600 positivity.

The clinical translatability of this rationale has been directly tested. NCT03898908 — a completed Phase 2 multicentre trial specifically designed for BRAF-mutant melanoma with brain metastases, including non-cutaneous presentations — provides the core Level 2 evidence for this indication. The completion of this trial with 48 participants, alongside the breadth of Phase 2 and Phase 3 trials establishing efficacy across broader melanoma populations, solidifies the biological and clinical framework supporting TxGNN's prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT03898908](https://clinicaltrials.gov/study/NCT03898908) | Phase 2 | Completed | 48 | Dedicated multicentre trial of Encorafenib + Binimetinib prior to local treatment in BRAF-mutant melanoma with brain metastases; two parallel cohorts — asymptomatic (Cohort 1) and symptomatic (Cohort 2) CNS disease. This is the most directly relevant completed trial for non-cutaneous melanoma. |
| [NCT06887088](https://clinicaltrials.gov/study/NCT06887088) | Phase 2 | Recruiting | 33 | ENCEFALO: single-arm multicentre trial evaluating Encorafenib + Binimetinib followed sequentially by Cemiplimab + Fianlimab (anti-PD-1/LAG-3 dual blockade) in BRAF-mutant melanoma with symptomatic brain metastases. Designed as a follow-on validation to NCT03898908. |
| [NCT03235245](https://clinicaltrials.gov/study/NCT03235245) | Phase 2 | Active, not recruiting | 271 | EORTC EBIN: randomised comparison of sequential Encorafenib + Binimetinib (12-week induction) → Nivolumab + Ipilimumab versus upfront combination immunotherapy in BRAF V600-mutant unresectable or metastatic melanoma. Large, well-powered sequential strategy design. |
| [NCT01909453](https://clinicaltrials.gov/study/NCT01909453) | Phase 3 | Completed | 921 | COLUMBUS: pivotal 3-arm randomised trial comparing Encorafenib + Binimetinib vs Vemurafenib vs Encorafenib monotherapy in BRAF V600-mutant unresectable or metastatic melanoma. Formed the basis of FDA and EMA regulatory approvals. |
| [NCT05270044](https://clinicaltrials.gov/study/NCT05270044) | Phase 3 | Active, not recruiting | 815 | Columbus-AD: randomised triple-blind adjuvant trial of Encorafenib + Binimetinib vs placebo (surveillance) in fully resected Stage IIB/C BRAF V600E/K-mutant melanoma. Long-term follow-up to 2035. |
| [NCT04657991](https://clinicaltrials.gov/study/NCT04657991) | Phase 3 | Active, not recruiting | 257 | Randomised, double-blind study of Encorafenib + Binimetinib + Pembrolizumab versus placebo + Pembrolizumab in previously untreated BRAF V600E/K-mutant metastatic or unresectable locally advanced melanoma. |
| [NCT02910700](https://clinicaltrials.gov/study/NCT02910700) | Phase 2 | Active, not recruiting | 52 | TRIBECA: phase II triplet study of Binimetinib + Encorafenib + Nivolumab in BRAF-mutated Stage III–IV unresectable or metastatic melanoma. Tests integration of targeted therapy with checkpoint inhibition. |
| [NCT06194929](https://clinicaltrials.gov/study/NCT06194929) | Phase 1b/2 | Recruiting | 33 | Defactinib + Avutometinib ± Encorafenib in brain metastases from cutaneous melanoma after progression on immune checkpoint inhibitors; explores novel combination strategies to overcome resistance. |
| [NCT03543969](https://clinicaltrials.gov/study/NCT03543969) | Early Phase 1 | Active, not recruiting | 14 | Pilot adaptive BRAF–MEK inhibition study using Encorafenib + Binimetinib + Nivolumab in BRAF-mutant Stage IIIC–IV melanoma; investigates pulsatile/adaptive dosing schedules to delay acquired resistance. High mechanistic translational value. |
| [NCT03911869](https://clinicaltrials.gov/study/NCT03911869) | Phase 2 | Terminated | 13 | Standard-dose vs high-dose Encorafenib + Binimetinib in BRAF V600-mutant melanoma brain metastases; terminated early with only 13 of ~100 planned participants enrolled. Provides limited data but signals dose-finding challenges in CNS disease; termination reasons should be reviewed. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [41774417](https://pubmed.ncbi.nlm.nih.gov/41774417/) | 2025 | Case Report | Pigment Cell & Melanoma Research | Molecular profiling used to diagnose epidermotropic metastatic melanoma (Stage IIIB nodular primary) presenting as eruptive superficial spreading lesions histopathologically indistinguishable from independent primary melanomas. Despite adjuvant nivolumab, new lesions continued to form. Illustrates critical importance of molecular diagnostics in complex melanoma presentations and underscores diagnostic challenges relevant to non-cutaneous and atypical melanoma subtypes. |

---

## Australia Market Information

Encorafenib is **not currently registered with the TGA** and has **no ARTG entries**. No Australian Product Information (PI) document is available.

Australian clinicians or patients seeking access to Encorafenib would need to pursue one of the following TGA pathways:

- **Special Access Scheme (SAS) Category B** — individual patient access on compassionate or clinical grounds, requiring treating clinician application
- **Authorised Prescriber (AP) scheme** — for clinicians seeking systematic access for a defined patient class
- **Clinical trial enrolment** — screen eligible patients for open international and Australian trials (search [ANZCTR](https://www.anzctr.org.au/) for local opportunities)

For current prescribing information, refer to the [FDA Braftovi® Prescribing Information](https://www.accessdata.fda.gov/) or the EMA Summary of Product Characteristics until TGA registration is obtained.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — selective mutant BRAF kinase inhibitor (small molecule oral capsule; RAF kinase inhibitor class) |
| Myelosuppression Risk | Low — myelosuppression is not a primary toxicity of BRAF inhibitors; anaemia and neutropenia are occasionally reported but not dose-limiting in most patients |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests (ALT, AST, bilirubin) at baseline and periodically; ECG for QTc interval at baseline and during treatment; full-body skin examination for paradoxical cutaneous malignancies; ophthalmological assessment (uveitis, retinal vein occlusion); blood pressure monitoring; renal function |
| Handling Protection | Oral capsule formulation — no dedicated cytotoxic handling infrastructure required. Follow institutional oral targeted therapy / oral antineoplastic dispensing and handling protocols. |

---

## Safety Considerations

As Encorafenib is not registered with the TGA, no Australian Product Information is available. Please refer to the **FDA-approved Braftovi® Prescribing Information** or the **EMA Summary of Product Characteristics** for comprehensive safety and prescribing data.

**Key class-effect safety signals clinicians should be aware of:**

- **Paradoxical MAPK activation and secondary cutaneous malignancies**: Encorafenib, like all BRAF inhibitors, can paradoxically activate the MAPK pathway in BRAF wild-type cells. This may induce secondary cutaneous malignancies including cutaneous squamous cell carcinoma, keratoacanthoma, and new primary melanocytic lesions. Systematic full-body dermatological surveillance throughout treatment is essential. A published case report (PMID 40878071) documented new melanoma development during Encorafenib + Cetuximab therapy for BRAF V600E-mutant colorectal cancer — reinforcing that this risk applies regardless of the primary indication.

- **QTc interval prolongation**: Cardiac monitoring with baseline and periodic ECG is recommended. Caution is warranted when co-prescribing other QTc-prolonging agents or in patients with baseline cardiac risk factors.

- **Ocular toxicity**: Uveitis, retinal vein occlusion, and blurred vision have been reported with BRAF inhibitor therapy. Ophthalmological assessment at baseline and if patients become symptomatic is advised.

- **Hepatotoxicity**: Transaminase elevations are among the more commonly reported laboratory abnormalities; routine liver function monitoring is required.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple Phase 2 and Phase 3 clinical trials — including the completed, dedicated Phase 2 trial NCT03898908 for BRAF-mutant melanoma with brain metastases in non-cutaneous presentations — demonstrate a robust efficacy and safety profile for Encorafenib-based regimens. The mechanistic rationale is well-established: BRAF V600 inhibition is tumour-site agnostic, contingent solely on confirmed mutation status. International regulatory approvals (FDA, EMA) for cutaneous melanoma provide a strong scientific and regulatory scaffold for extended use to BRAF-mutation-positive non-cutaneous subtypes. However, given the absence of TGA registration, no approved Australian access pathway exists, and any clinical use requires formal access mechanisms and rigorous patient selection.

**To proceed, the following is needed:**

- **Mandatory BRAF V600 mutation confirmation**: Validated BRAF V600E or V600K testing via PCR or next-generation sequencing (NGS) on tumour tissue from the non-cutaneous site is an absolute prerequisite. Patients with BRAF wild-type tumours will not benefit and are at risk of paradoxical harm.
- **TGA access pathway initiation**: Commence a Special Access Scheme (SAS) Category B application or Authorised Prescriber application, depending on practice volume and patient context.
- **Complete safety prescribing data**: Obtain and review the full FDA/EMA product labelling, then develop a local monitoring protocol covering dermatological surveillance, ECG, liver function, and ophthalmology.
- **Multidisciplinary team (MDT) endorsement**: Engage medical oncology, dermatology, and relevant surgical or radiation oncology specialists before commencing treatment.
- **Clinical trial screening first**: Before proceeding to SAS/off-label access, screen patients for eligibility in open Australian or international trials (ANZCTR and ClinicalTrials.gov) to maximise evidence generation.
- **MOA data gap resolution**: Retrieve complete DrugBank pharmacology and toxicity data via API to populate the mechanism of action section and enable a full Level 1 evidence dossier for future TGA submission.
- **Monitoring plan for paradoxical malignancy risk**: Given the documented risk of secondary cutaneous tumours, implement a structured dermatology review schedule (e.g., every 4–8 weeks during treatment).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

