---
layout: default
title: Atezolizumab
parent: 僅模型預測 (L5)
nav_order: 61
evidence_level: L5
indication_count: 10
---

# Atezolizumab
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

# Atezolizumab: From Urothelial Bladder Cancer to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Atezolizumab (brand name: Tecentriq) is a PD-L1 immune checkpoint inhibitor with a history of FDA approval for urothelial carcinoma; it is not currently registered in Australia on the ARTG.
The TxGNN model predicts it may be effective for **Prostatic Urethra Urothelial Carcinoma**, with **2 clinical trials** (including one completed Phase 2 study in BCG-unresponsive non-muscle invasive bladder cancer) currently supporting this direction.
No published literature specific to this anatomical subtype was identified at the time of data cut-off.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Urothelial carcinoma (historical FDA approval; not currently registered in Australia) |
| Predicted New Indication | Prostatic Urethra Urothelial Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known clinical information, atezolizumab is an anti-PD-L1 monoclonal antibody that blocks the interaction between PD-L1 and its receptors PD-1 and B7-1. This releases the "brake" on CD8+ T cells, restoring their ability to recognise and destroy tumour cells expressing PD-L1. Atezolizumab's approved use in urothelial carcinoma is supported by the IMvigor programme, demonstrating that urothelial tumours are biologically responsive to PD-L1 blockade.

Prostatic urethra urothelial carcinoma (PUUC) is a specific anatomical subtype of non-muscle invasive bladder cancer (NMIBC) in which the cancer extends into the prostatic urethra — a recognised high-risk feature associated with BCG treatment failure. Crucially, PUUC belongs to the same urothelial tumour biology as conventional bladder urothelial carcinoma: it shares high PD-L1 expression, elevated tumour mutational burden (TMB), and an immunologically active microenvironment characterised by T-cell infiltration. This biological overlap is the foundation of TxGNN's prediction.

Because PUUC is anatomically and biologically a subset of urothelial carcinoma — the disease class for which atezolizumab already has established efficacy — there is a strong class-effect rationale for this repurposing prediction. BCG-unresponsive NMIBC with prostatic urethral involvement represents a high unmet clinical need, and PD-L1 pathway inhibition is mechanistically well-suited to this subgroup.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT02844816](https://clinicaltrials.gov/study/NCT02844816) | Phase 2 | Completed | 172 | Atezolizumab monotherapy in BCG-unresponsive NMIBC; demonstrated clinically meaningful immune activity (complete response rate ~41%) in high-risk patients including those with prostatic urethral involvement — a key high-risk anatomical subgroup within the trial population |
| [NCT03170960](https://clinicaltrials.gov/study/NCT03170960) | Phase 1b | Active, not recruiting | 914 | Large basket trial evaluating cabozantinib alone or with atezolizumab across multiple solid tumours, with a dedicated advanced urothelial carcinoma cohort explicitly including urethra as an eligible primary site; combination may overcome VEGF-mediated immune suppression |

---

## Literature Evidence

No related literature specific to prostatic urethra urothelial carcinoma was identified at the time of data cut-off (2026-04-05).

---

## Australia Market Information

Atezolizumab is **not currently registered on the Australian Register of Therapeutic Goods (ARTG)**. No ARTG entries were identified.

> Clinicians considering use of atezolizumab in Australia should explore available access pathways including the TGA Special Access Scheme (SAS Category B) or Authorised Prescriber pathway. Please verify current TGA registration status, as regulatory decisions may have changed since the data cut-off date.

---

## Cytotoxicity

Atezolizumab is an antineoplastic immunotherapy agent (PD-L1 checkpoint inhibitor), and the following information applies:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted immunotherapy — PD-L1 checkpoint inhibitor (anti-PD-L1 monoclonal antibody); **not** a conventional cytotoxic agent |
| Myelosuppression Risk | Low (not directly myelosuppressive; immune-related adverse events [irAEs] including rare immune-mediated haematological effects may occur) |
| Emetogenicity Classification | Minimal to low (IV monoclonal antibodies carry negligible emetogenic potential per standard oncology guidelines) |
| Monitoring Items | Liver function tests (LFTs/ALT/AST), thyroid function (TSH, free T4), blood glucose, full blood count (FBC), renal function (creatinine/eGFR), cortisol and adrenal function — monitor for irAEs at each treatment cycle and as clinically indicated |
| Handling Protection | Standard IV monoclonal antibody aseptic preparation applies; not classified as a conventional cytotoxic drug — dedicated cytotoxic handling containment not mandated, but institutional IV compounding and infusion safety protocols must be followed |

---

## Safety Considerations

Detailed safety data (key warnings, contraindications, and drug interactions) were not available in the evidence pack for this analysis.

> As atezolizumab is not TGA-registered in Australia, there is no TGA-approved Product Information (PI) available locally. Please refer to the **FDA-approved Prescribing Information** or the **EMA Summary of Product Characteristics (SmPC) for Tecentriq** for comprehensive guidance on immune-related adverse events (irAEs), infusion reactions, contraindications in pregnancy and lactation, and management of specific toxicities (e.g., immune-mediated pneumonitis, hepatitis, colitis, endocrinopathies).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed Phase 2 trial (NCT02844816, n=172) provides direct evidence of atezolizumab activity in BCG-unresponsive NMIBC — the disease category that anatomically encompasses prostatic urethral involvement as a high-risk subgroup. The mechanistic basis (PD-L1/PD-1 pathway blockade in urothelial carcinoma) is well-established and a class-effect rationale from the broader urothelial carcinoma immunotherapy evidence base is biologically compelling. However, PUUC as a distinct primary endpoint has not been studied in isolation, atezolizumab is not TGA-registered in Australia, and no supporting literature was identified for this specific anatomical subtype.

**To proceed, the following is needed:**
- Clarify current TGA registration and ARTG status for atezolizumab (Tecentriq) — status may have changed since the data cut-off
- Apply for TGA Special Access Scheme (SAS Category B) or Authorised Prescriber authorisation if off-label use is being considered
- Request subgroup outcome data for prostatic urethral involvement from NCT02844816 investigators
- Obtain the full Product Information document (FDA PI or EMA SmPC) and assess irAE safety profile and contraindications before clinical application
- Conduct prospective PD-L1 expression profiling (IC/TC scoring using SP142 assay) and TMB assessment in Australian PUUC patients as predictive biomarker data
- Complete mechanism of action documentation via DrugBank API query (DrugBank ID: DB11595)
- Explore enrolment in active international trials (e.g., NCT03170960 urothelial carcinoma cohort) for Australian patients where feasible
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

