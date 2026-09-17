---
layout: default
title: Vinorelbine
parent: High Evidence (L1-L2)
nav_order: 725
evidence_level: L2
indication_count: 10
---

# Vinorelbine
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Vinorelbine: From Established Chemotherapy Use to Ewing Sarcoma

## One-Sentence Summary

> Vinorelbine is a vinca alkaloid chemotherapy agent with an extensive evidence base in non-small cell lung cancer (NSCLC), though it is not currently marketed in Australia (no ARTG entries).
> The TxGNN model predicts it may also be effective for **Ewing Sarcoma**,
> with **4 clinical trials** and **5 publications** currently supporting this direction — largely reflecting existing paediatric oncology practice rather than a purely novel prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not TGA-registered (drug not marketed in Australia); literature evidence in this pack establishes NSCLC as its principal, well-documented indication |
| Predicted New Indication | Ewing Sarcoma |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L2 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal DrugBank mechanism-of-action text is a recorded data gap (DG002) in this evidence pack. However, the model's own repurposing rationale describes vinorelbine as a **microtubule-destabilising vinca alkaloid**: it inhibits mitotic spindle formation, arresting cells in mitosis and inducing apoptosis. This mechanism is preferentially cytotoxic to rapidly dividing cell populations — a category that includes Ewing sarcoma, a high-grade small round blue cell tumour with a very high proliferation index.

Vinorelbine's original and best-established use is in NSCLC, where its cytotoxic, anti-mitotic mechanism has been validated across numerous Phase III trials (e.g. the ANITA adjuvant trial, PMID 16945766). Ewing sarcoma and NSCLC are pharmacologically linked not through anatomical or histological similarity, but through shared vulnerability to microtubule-targeting agents in high-proliferation malignancies.

Importantly, this is not a purely computational extrapolation. Vinorelbine already has real-world use as a second-/later-line agent in relapsed or refractory paediatric solid tumours, including Ewing sarcoma family tumours, rhabdomyosarcoma, osteosarcoma and neuroblastoma (NCT00180947). Completed Phase II studies in this population (e.g. PMID 22633624, PMID 12115359) support feasibility and activity, making this prediction largely a formalisation of existing off-label/guideline-supported clinical practice rather than a novel hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00003234](https://clinicaltrials.gov/study/NCT00003234) | Phase 2 | Completed | 50 | Vinorelbine efficacy in children with recurrent or refractory malignancies (broad paediatric population, includes sarcomas) |
| [NCT00180947](https://clinicaltrials.gov/study/NCT00180947) | Phase 2 | Unknown | 210 | Vinorelbine + cyclophosphamide antitumour activity in refractory/relapsed rhabdomyosarcoma, Ewing tumours, osteosarcoma, neuroblastoma and medulloblastoma |
| [NCT06451302](https://clinicaltrials.gov/study/NCT06451302) | N/A (observational) | Active, not recruiting | 100 | Prospective multicentre cohort evaluating outcome and safety of risk-stratified treatment in paediatric Ewing sarcoma (China) |
| [NCT05999994](https://clinicaltrials.gov/study/NCT05999994) | Phase 2 | Recruiting | 105 | CAMPFIRE master protocol for paediatric/young-adult cancers; may include an Ewing sarcoma treatment arm |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22633624](https://pubmed.ncbi.nlm.nih.gov/22633624/) | 2012 | Prospective Phase II | European Journal of Cancer | Vinorelbine + continuous low-dose oral cyclophosphamide in relapsed/refractory paediatric solid tumours — good tolerance, efficacy signal particularly in rhabdomyosarcoma |
| [12115359](https://pubmed.ncbi.nlm.nih.gov/12115359/) | 2002 | Clinical study | Cancer | Vinorelbine in previously treated advanced childhood sarcomas — evidence of activity in rhabdomyosarcoma |
| [37637411](https://pubmed.ncbi.nlm.nih.gov/37637411/) | 2023 | Review | Frontiers in Pharmacology | Comprehensive review of chemotherapy options for soft tissue sarcomas, including vinca alkaloids |
| [26260582](https://pubmed.ncbi.nlm.nih.gov/26260582/) | 2016 | Preclinical (synergy study) | International Journal of Cancer | Vinorelbine synergises with PLK1 inhibitor BI 6727 to induce apoptosis in Ewing sarcoma cell lines |
| [36451163](https://pubmed.ncbi.nlm.nih.gov/36451163/) | 2022 | Case report | BMC Urology | Case report and literature review of extraosseous Ewing's sarcoma/pPNET of the kidney |

---

## Australia Market Information

Vinorelbine currently has **no ARTG entries** and is **not marketed in Australia**. No TGA-approved Product Information exists for this product in the Australian market at this time.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Vinca alkaloid class — microtubule/mitotic spindle inhibitor) |
| Myelosuppression Risk | High — literature in this pack consistently identifies neutropenia as the dose-limiting toxicity of vinorelbine (e.g. PMID 10585010, PMID 9535205) |
| Emetogenicity Classification | Low to moderate (typical for vinca alkaloids as a class) |
| Monitoring Items | FBC with differential (neutrophil count), liver function (hepatic impairment increases toxicity risk), assessment for peripheral neuropathy and extravasation site |
| Handling Protection | Must follow cytotoxic drug handling regulations; vinorelbine is a vesicant — extravasation precautions required during administration |

---

## Safety Considerations

Detailed TGA/TFDA product-label warnings, contraindications and drug interaction data are recorded as a **Blocking data gap (DG001)** in this evidence pack — no formal safety pre-assessment (S1) has been completed. Because vinorelbine is not currently marketed in Australia, there is also no Australian-approved Product Information to reference directly; safety information would need to be sourced from an equivalent overseas-approved label (e.g. US FDA or EMA Navelbine PI) as an interim measure.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed and ongoing Phase II trials, plus mechanistic and preclinical evidence, support vinorelbine's use in relapsed/refractory paediatric Ewing sarcoma — this largely reflects existing clinical practice rather than a novel signal. However, the drug is not TGA-registered and a Blocking safety data gap (DG001) means it has not yet cleared formal safety pre-assessment.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA/overseas Product Information (warnings, contraindications, DDI) to complete S1 safety pre-assessment
- Resolve DG002: obtain formal DrugBank/regulatory mechanism-of-action documentation
- Clarify Australian access pathway, since there are no ARTG entries (e.g. Special Access Scheme or Authorised Prescriber pathway for unregistered medicine)
- Confirm paediatric oncology dosing/monitoring protocols specific to Ewing sarcoma before clinical use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

