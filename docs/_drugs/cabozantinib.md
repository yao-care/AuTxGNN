---
layout: default
title: Cabozantinib
parent: 僅模型預測 (L5)
nav_order: 115
evidence_level: L5
indication_count: 10
---

# Cabozantinib
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

The data-report skill applies to CLI output and database queries — not applicable here. The Evidence Pack JSON was supplied directly, so I'll proceed to synthesise the report per the system prompt format.

---

# Cabozantinib: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

> Cabozantinib (Cabometyx) is an oral multi-kinase inhibitor targeting VEGFR2, MET, and AXL, with global approvals for advanced renal cell carcinoma, differentiated thyroid cancer, and hepatocellular carcinoma — though it is not currently registered in Australia.
> The TxGNN model predicts it may also be effective for **Liposarcoma**, with **1 clinical trial** and **1 publication** currently supporting this direction.
> Evidence at this stage is preliminary (Level L3), and dedicated liposarcoma-specific trial data are still pending.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Australia (TGA). Globally approved for advanced renal cell carcinoma, differentiated thyroid cancer, and hepatocellular carcinoma |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, Cabozantinib is a potent oral inhibitor of multiple receptor tyrosine kinases — primarily VEGFR2, MET (c-MET), and AXL — each implicated in tumour growth, angiogenesis, immune evasion, and the development of resistance to anti-angiogenic therapies.

In liposarcoma — particularly the dedifferentiated and pleomorphic subtypes — MET overexpression and AXL activation have been documented as important oncogenic drivers. The characteristic MDM2/CDK4 co-amplification at the 12q13-15 chromosomal locus, a hallmark of dedifferentiated liposarcoma, has been shown to interact with MET signalling pathways. VEGFR2 inhibition may additionally disrupt tumour angiogenesis, which is critical for the growth of these often large and highly vascularised tumours.

While the mechanistic link is scientifically plausible, all existing clinical trials have enrolled broad soft tissue sarcoma (STS) cohorts rather than liposarcoma-specific populations. Liposarcoma subgroup analyses from ongoing trials are required to confirm whether this TxGNN prediction translates to clinically meaningful patient outcomes.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|------|--------|----------|-------------|
| [NCT05836571](https://clinicaltrials.gov/study/NCT05836571) | Phase 2 | Active, Not Recruiting | 66 | Randomised Phase 2 comparing Cabozantinib + Ipilimumab + Nivolumab versus Ipilimumab + Nivolumab alone in advanced soft tissue sarcoma. Liposarcoma is included as a subgroup — not a primary endpoint. Results are pending; a liposarcoma-specific subgroup analysis will be required to interpret the efficacy signal |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|-------------|
| [41770651](https://pubmed.ncbi.nlm.nih.gov/41770651/) | 2026 | Phase 1 Neoadjuvant Study | American Journal of Clinical Oncology | Phase 1 safety study of Cabozantinib combined with concurrent radiation therapy as neoadjuvant treatment in extremity soft tissue sarcoma. Cabozantinib demonstrated activity across multiple STS subtypes; the study addressed concerns about fistula and perforation risk with concurrent radiotherapy |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — oral multi-kinase inhibitor (VEGFR2 / MET / AXL) |
| Myelosuppression Risk | Low to Moderate (thrombocytopenia and neutropenia have been reported; less pronounced than conventional cytotoxic chemotherapy) |
| Emetogenicity Classification | Low to Moderate |
| Monitoring Items | Full blood count (FBC with differential), liver function tests (LFTs), renal function (eGFR/creatinine), thyroid function tests (TFTs), urine protein (dipstick or protein:creatinine ratio), blood pressure |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions. Cabozantinib is an oral targeted therapy — confirm institutional pharmacy protocols for safe handling classification prior to dispensing |

---

## Safety Considerations

Please refer to the manufacturer's Product Information (PI) or FDA/EMA prescribing information for full safety information. Cabozantinib is not currently registered with the TGA in Australia; therefore, no TGA-approved Australian PI is available. Individual patient access may be possible via the TGA Special Access Scheme (SAS) or Authorised Prescriber pathway.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Current evidence for Cabozantinib in liposarcoma is limited to a single ongoing Phase 2 trial in broad soft tissue sarcoma and one Phase 1 safety study — neither provides liposarcoma-specific efficacy data. The drug is also not registered with the TGA, meaning there is no established Australian access pathway at present.

**To proceed, the following is needed:**
- Liposarcoma-specific subgroup analysis results from NCT05836571
- Phase 2 efficacy data with liposarcoma as a primary or pre-specified secondary endpoint
- Biomarker confirmation of MET/AXL overexpression in the target patient population
- Assessment of TGA registration pathway or Special Access Scheme (SAS) eligibility for Australian patients
- Full mechanism of action data (MOA) retrieved from DrugBank (DG002 remediation)
- Review of FDA/EMA prescribing information for complete safety, contraindication, and drug interaction profile (DG001 remediation)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

