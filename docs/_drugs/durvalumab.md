---
layout: default
title: Durvalumab
parent: Model Prediction Only (L5)
nav_order: 236
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Durvalumab: predicted new indication Prostatic urethra urothelial carcinoma (evidence level L5). Approved use: Transitional cell carcinoma"
---

# Durvalumab
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

# Durvalumab: From Transitional Cell Carcinoma to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Durvalumab is an anti-PD-L1 antibody originally used to treat transitional cell (urothelial) carcinoma.
The TxGNN model predicts it may be effective for **prostatic urethra urothelial carcinoma**, but the data compiled for this report contain **no clinical trials and no publications** for this specific indication, so support currently rests on the model prediction alone.

Note: several lower-ranked predictions have some trial evidence (for example, sarcomatoid and variant-histology urothelial carcinoma). These are summarised in the sections below as context.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Transitional cell carcinoma (the Australian licence entry has no indication text) |
| Predicted New Indication | Prostatic urethra urothelial carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Durvalumab is known to be an anti-PD-L1 antibody. It is approved in urothelial (transitional cell) carcinoma, so blocking PD-L1 is a plausible strategy in other tumours of urothelial origin.

The prostatic urethra is lined by urothelium, so prostatic urethra urothelial carcinoma shares its lineage with the original indication. This shared histology is the main reason the prediction is biologically reasonable. However, no trial or literature evidence for this specific site was found, and the prediction should be treated as a hypothesis only.

Other predicted indications in the same family show a similar pattern:
- **Kidney pelvis sarcomatoid transitional cell carcinoma** (rank 2) and **infiltrating bladder urothelial carcinoma, sarcomatoid variant** (rank 3): the same urothelial lineage, with small early-stage trials described below.
- **Endocervical carcinoma** (rank 6): a different tumour type, with a completed Phase 1 trial and indirect literature.
- Ranks 4 and 5 and ranks 7-10 (renal pelvis papillary urothelial carcinoma, uterine ligament adenocarcinoma, and rare cervical adenocarcinoma variants) have no supporting studies in the data compiled.

## Clinical Trial Evidence

There are no registered trials for the top-ranked indication (prostatic urethra urothelial carcinoma). The trials below relate to lower-ranked predictions and are shown for context.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02812420](https://clinicaltrials.gov/study/NCT02812420) | Early Phase 1 | Active, not recruiting | 54 | Pre-surgical pilot of durvalumab plus tremelimumab in muscle-invasive, high-risk urothelial carcinoma in patients ineligible for cisplatin. No outcome results in the data compiled; suited to feasibility and biomarker signals. |
| [NCT03912818](https://clinicaltrials.gov/study/NCT03912818) | Phase 2 | Terminated | 7 | Durvalumab with neoadjuvant chemotherapy in variant-histology bladder cancer. Terminated with only 7 patients, so no efficacy conclusions can be drawn. |
| [NCT03452332](https://clinicaltrials.gov/study/NCT03452332) | Phase 1 | Completed | 20 | Hypofractionated radiotherapy with durvalumab and tremelimumab in recurrent or metastatic cervical, vaginal or vulvar cancer. Provides safety and feasibility information only. |

## Literature Evidence

There is no literature for the top-ranked indication. The publications below relate to endocervical carcinoma (rank 6) and are indirect.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42518016](https://pubmed.ncbi.nlm.nih.gov/42518016/) | 2026 | Nonrandomized clinical trial | Oncology and Therapy | Phase 1 study of ceralasertib plus durvalumab in Chinese patients with advanced solid tumours refractory to prior anti-PD-(L)1 therapy or without standard options. Examines safety, pharmacokinetics and antitumour activity; not specific to cervical or urothelial cancer. |
| [37467967](https://pubmed.ncbi.nlm.nih.gov/37467967/) | 2023 | Review | Biomedical Journal | Review of small cell neuroendocrine carcinoma of the cervix, covering molecular basis and emerging therapies. Notes that evidence is limited to case series and reports. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11911X | Imfinzi | Solution concentrate for I.V. infusion, 120 mg in 2.4 mL | Not listed in the data compiled |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-L1 monoclonal antibody) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the Product Information (PI) warnings and precautions |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

## Safety Considerations

Warnings and contraindications were not available in the data compiled. Please refer to the TGA-approved Product Information (PI) for safety information.

**Drug Interactions:** The interaction query found 81 interacting drugs. Examples from the first 20 returned are listed below.
- **Major:** adalimumab.
- **Moderate:** systemic corticosteroids (hydrocortisone, dexamethasone, prednisolone, prednisone, methylprednisolone, betamethasone, budesonide, triamcinolone, deflazacort), roflumilast, alefacept, alemtuzumab, anakinra, anthrax vaccine, and tetanus toxoid vaccine.
- **Minor:** zinc salts (acetate, gluconate, sulfate, chloride).

Immunosuppressive agents such as corticosteroids and biologics may reduce the effect of checkpoint inhibitors, so concurrent use should be reviewed against the PI.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
For prostatic urethra urothelial carcinoma there are no trials or publications, and the evidence level is L5 (model prediction only). The biological rationale is reasonable because the tissue lineage matches the approved indication. A high TxGNN score alone is not enough to support clinical use.

**To proceed, the following is needed:**
- Site-specific evidence (clinical trials, case series or retrospective data) for prostatic urethra urothelial carcinoma, including PD-L1 expression data
- Mechanism of action data, which are currently missing
- Safety information (warnings and contraindications) taken from the TGA PI
- Review of the early-phase urothelial trials (NCT02812420, NCT03912818) once results are available, and consideration of whether the sarcomatoid or variant-histology indications (ranks 2 and 3) are better-supported candidates for further research
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

