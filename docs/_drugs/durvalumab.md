---
layout: default
title: Durvalumab
parent: 僅模型預測 (L5)
nav_order: 175
evidence_level: L5
indication_count: 10
---

# Durvalumab
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

# Durvalumab: From Urothelial Carcinoma to Prostatic Urethra Urothelial Carcinoma

---

## One-Sentence Summary

Durvalumab (Imfinzi) is an anti-PD-L1 immune checkpoint inhibitor with established clinical evidence in urothelial carcinoma, non-small cell lung cancer, small cell lung cancer, and biliary tract cancer, most notably validated in bladder urothelial carcinoma through the Phase 3 DANUBE trial.
The TxGNN model predicts it may be effective for **Prostatic Urethra Urothelial Carcinoma**, a rare anatomical subsite variant sharing the same urothelial tissue origin as bladder cancer.
Currently, **no clinical trials or publications** specifically addressing this subsite indication have been identified; the prediction rests entirely on mechanistic extrapolation from broader urothelial carcinoma data.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in current evidence pack |
| Predicted New Indication | Prostatic Urethra Urothelial Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed (per current data; independent TGA verification recommended) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on well-established pharmacological knowledge, Durvalumab is a human IgG1κ monoclonal antibody that selectively binds programmed death-ligand 1 (PD-L1), blocking its interactions with the PD-1 and CD80 (B7.1) receptors. This mechanism disables tumour-mediated immune suppression and restores cytotoxic T-cell activity against cancer cells. Durvalumab has demonstrated clinical benefit across multiple solid tumours with high PD-L1 expression, most notably in urothelial carcinoma (Phase 3 DANUBE trial) and unresectable Stage III NSCLC (PACIFIC trial), where it is considered a standard-of-care option.

Prostatic urethra urothelial carcinoma shares the same embryological tissue of origin and histological identity as bladder urothelial carcinoma — both arise from the transitional epithelium (urothelium) lining the lower urinary tract. This histological identity means the tumour cells are biologically expected to exhibit similar PD-L1 overexpression patterns, high tumour mutational burden (TMB), and immune microenvironment characteristics that have been exploited by Durvalumab in conventional bladder UC. The mechanistic bridge is therefore scientifically sound at a tissue and molecular level.

However, this prediction is an indirect anatomical extrapolation. The prostatic urethra occupies a microenvironment strongly influenced by the surrounding prostatic stroma, which may alter local immune cell infiltration, T-cell trafficking, and PD-L1 expression dynamics relative to the bladder wall. No direct clinical trials, case series, or laboratory data have examined Durvalumab in the prostatic urethral subsite specifically. The high TxGNN score (99.98%) most likely reflects the model recognising the strong biological similarity to bladder UC rather than subsite-specific clinical evidence. This prediction should be regarded as a hypothesis warranting targeted research rather than a clinically actionable signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for prostatic urethra urothelial carcinoma.

---

## Literature Evidence

Currently no related literature available for prostatic urethra urothelial carcinoma.

---

## Australia Market Information

Durvalumab has no ARTG entries recorded in the current evidence pack, and is listed as not marketed in Australia based on this dataset (data cutoff: 2026-04-04). Clinicians should independently verify the current registration status via the [TGA ARTG Public Summary](https://www.tga.gov.au/resources/artg), as Imfinzi (durvalumab) may hold TGA approvals not captured in this snapshot.

---

## Cytotoxicity

Durvalumab is classified as an antineoplastic agent (immunotherapy) and the following monitoring considerations apply:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunotherapy — PD-L1 immune checkpoint inhibitor (not a conventional cytotoxic agent) |
| Myelosuppression Risk | Low (conventional myelosuppression is uncommon; immune-mediated haematological adverse events, including immune thrombocytopenia and autoimmune haemolytic anaemia, are possible) |
| Emetogenicity Classification | Minimal (monoclonal antibody immunotherapies are not classified as emetogenic per MASCC/ASCO guidelines) |
| Monitoring Items | FBC with differential; liver function tests (AST, ALT, bilirubin); thyroid function (TSH, free T4); renal function (creatinine, eGFR); fasting blood glucose; cortisol (adrenal function). Routine monitoring for immune-related adverse events (irAEs) across organ systems is required |
| Handling Protection | Standard biological injectable precautions apply; cytotoxic drug handling protocols (closed-system transfer devices, PPE for hazardous drugs) are generally not required for monoclonal antibody immunotherapies per institutional and SHPA guidelines — confirm with local pharmacy |

---

## Safety Considerations

Detailed TGA-approved warnings, contraindications, and drug interaction data were not available in this evidence pack. Please refer to the **TGA-approved Product Information (PI) for Imfinzi (durvalumab)** for complete safety information, including immune-related adverse event management guidelines.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While PD-L1 blockade is mechanistically plausible in prostatic urethra urothelial carcinoma given its shared tissue origin and expected PD-L1 expression profile with bladder UC, the complete absence of any direct clinical, observational, or preclinical data for this specific subsite means this finding cannot progress beyond a hypothesis-generating research question at this stage.

**To proceed, the following is needed:**

- Verify current TGA/ARTG registration status for Durvalumab (Imfinzi) directly via the TGA website and confirm approved Australian indications
- Obtain the TGA-approved Product Information (PI) to confirm safety warnings, contraindications, and immune-related adverse event management requirements
- Commission a targeted literature review for PD-L1 expression profiles, TMB, and MSI/MMR status specifically in prostatic urethral urothelial carcinoma
- Audit existing broad urothelial carcinoma trial databases (e.g., DANUBE, EV-302 extension datasets) to determine whether any patients with prostatic urethral primary tumours were enrolled and analysed as a subgroup
- If clinical translation is pursued, prospective biomarker assessment (PD-L1 IHC by 22C3 or SP142 assay, TMB sequencing, MSI/MMR testing) would be required for patient selection
- Given the rarity of this subsite, enrolment into an existing rare urothelial carcinoma basket trial would be more feasible than standalone clinical development

---

> ⚠️ **Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require prospective clinical validation before application. All clinical decisions must be made in accordance with TGA-approved indications and current evidence-based guidelines.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

