---
layout: default
title: Zoledronic Acid
parent: 僅模型預測 (L5)
nav_order: 736
evidence_level: L5
indication_count: 10
---

# Zoledronic Acid
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

Using no additional skill — this is a direct report-generation task fully specified by the provided template; proceeding straight to the deliverable.

# Zoledronic Acid: From Bone Metabolic Disease to HIV Infectious Disease

## One-Sentence Summary

> Zoledronic acid is a nitrogen-containing bisphosphonate with an established literature-documented role in bone metabolic disease (osteoporosis, hypercalcaemia of malignancy, bone metastases), though specific Australian regulatory indication data is not available in this Evidence Pack.
> The TxGNN model predicts it may be effective for **HIV Infectious Disease**,
> supported by **0 dedicated clinical trials** and **20 publications**, most of which address a related but distinct endpoint (bone loss in HIV patients on antiretroviral therapy) rather than direct antiviral efficacy.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not specified in Australian regulatory data (drug not marketed, no ARTG licences); literature evidence in this pack references established use in bone metabolic disease (osteoporosis, hypercalcaemia of malignancy, bone metastases) |
| Predicted New Indication | HIV Infectious Disease |
| TxGNN Prediction Score | 93.95% |
| Evidence Level | L4 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data for zoledronic acid is flagged as a data gap in this Evidence Pack (DG002, High severity). However, the literature evidence collected for this specific prediction provides a clear mechanistic rationale: zoledronic acid inhibits farnesyl pyrophosphate synthase (FPPS) in the mevalonate pathway. In bone, this suppresses osteoclast activity — the basis of its established role in bone metabolic disease. Separately, FPPS inhibition causes intracellular accumulation of isopentenyl pyrophosphate (IPP), a phosphoantigen that potently activates and expands Vγ9Vδ2 γδT cells, a lymphocyte subset with documented antiviral effector functions, including direct cytotoxicity against HIV-infected cells and enhancement of dendritic cell antigen presentation.

The link between the original and predicted indication is not purely theoretical: zoledronic acid is already used clinically in HIV-positive patients, but for a different purpose — preventing and treating antiretroviral therapy (ART)-induced bone loss, a well-documented complication of HIV treatment. This existing clinical familiarity in the HIV population is what generates most of the randomised controlled trial (RCT) evidence in this pack.

Importantly, this creates an evidence-endpoint mismatch that should be flagged to reviewers: the majority of RCTs identified test bone mineral density (BMD) outcomes in HIV-infected adults on ART, not viral suppression, immune reconstitution, or clinical HIV outcomes. Only a smaller set of mechanistic/cohort studies (γδT cell expansion, immunocompetence activation) speak directly to the predicted antiviral hypothesis. This is why the evidence level has been scored L4 (preclinical/mechanistic) despite the presence of multiple Phase 2/3-equivalent RCTs in the broader literature set — those RCTs do not test the indication being predicted here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered specifically testing zoledronic acid for HIV infectious disease as an endpoint.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29927785](https://pubmed.ncbi.nlm.nih.gov/29927785/) | 2018 | RCT | AIDS | Zoledronic acid superior to tenofovir-switching for improving low bone mineral density in HIV-positive adults |
| [27193748](https://pubmed.ncbi.nlm.nih.gov/27193748/) | 2016 | RCT (Phase IIb) | Clin Infect Dis | Single-dose zoledronic acid infusion prevents ART-induced bone loss in treatment-naïve HIV patients |
| [31361922](https://pubmed.ncbi.nlm.nih.gov/31361922/) | 2019 | RCT (long-term follow-up) | J Bone Miner Res | Prolonged (36-month) BMD benefit from zoledronic acid persists in HIV-infected adults on tenofovir |
| [19050386](https://pubmed.ncbi.nlm.nih.gov/19050386/) | 2009 | RCT | AIDS | Double-blinded RCT confirming efficacy of single-dose IV zoledronate for HIV-associated osteopenia/osteoporosis |
| [17227801](https://pubmed.ncbi.nlm.nih.gov/17227801/) | 2007 | RCT | J Clin Endocrinol Metab | Annual zoledronate increases bone density in HAART-treated HIV-infected men |
| [31621838](https://pubmed.ncbi.nlm.nih.gov/31621838/) | 2020 | RCT (Phase IIB) | Clin Infect Dis | Single-dose zoledronic acid durably suppresses ART-induced bone loss in treatment-naïve persons with HIV |
| [25300622](https://pubmed.ncbi.nlm.nih.gov/25300622/) | 2014 | Systematic Review/Meta-analysis | AIDS Reviews | Meta-analysis of 8 RCTs on bisphosphonate effects on BMD in HIV-infected adults |
| [19238075](https://pubmed.ncbi.nlm.nih.gov/19238075/) | 2009 | Cohort/Clinical Study | AIDS | Zoledronic acid + IL-2 improves immunocompetence in HIV-infected persons by activating Vγ9Vδ2 γδT cells — mechanistic basis for the antiviral prediction |
| [33637048](https://pubmed.ncbi.nlm.nih.gov/33637048/) | 2021 | Cohort/Mechanistic | Molecular Medicine | Zoledronic acid alleviates osteoporosis in HIV patients by suppressing osteoclastogenesis via RANKL regulation |
| [22029653](https://pubmed.ncbi.nlm.nih.gov/22029653/) | 2012 | Cohort/Mechanistic | Cytotherapy | γδT cells from HIV+ donors expanded in vitro by zoledronate/IL-2 become cytotoxic ADCC effectors |

---

## Australia Market Information

No ARTG entries recorded in this Evidence Pack. Zoledronic acid is listed as **Not Marketed** with 0 total licences, so no approved indication text or product listing is available for Australia in this dataset.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No key warnings, contraindications, or drug–drug interaction data were returned in this Evidence Pack (DG001, Blocking severity — TGA PI warnings/contraindications not yet retrieved).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale (FPPS inhibition → γδT cell phosphoantigen activation) is biologically plausible and supported by mechanistic/cohort studies, but no clinical trial has directly tested zoledronic acid against an HIV clinical or virological endpoint — existing RCTs test a different endpoint (ART-induced bone loss). This is a research hypothesis, not an established treatment effect, and the Blocking-severity safety data gap (DG001) independently precludes progression past initial safety screening.

**To proceed, the following is needed:**
- TGA Product Information (PI) warnings, precautions, and contraindications (resolves DG001, Blocking)
- Confirmed mechanism-of-action and DrugBank category data (resolves DG002)
- A dedicated clinical trial or prospective cohort testing zoledronic acid against HIV-specific endpoints (viral load, immune reconstitution, γδT cell response) rather than bone density
- Clarification of Australian market/registration status, given the current dataset shows zero ARTG entries
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

