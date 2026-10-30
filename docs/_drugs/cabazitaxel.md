---
layout: default
title: Cabazitaxel
parent: Model Prediction Only (L5)
nav_order: 119
evidence_level: L5
indication_count: 10
monitor_inn: "Cabazitaxel"
predicted_indications: ["female breast carcinoma", "sickle cell-beta-thalassemia disease syndrome", "sickle cell-hemoglobin c disease syndrome", "hereditary persistence of fetal hemoglobin-sickle cell disease syndrome", "sickle cell-hemoglobin d disease syndrome", "sickle cell-hemoglobin E disease syndrome", "HIV infectious disease", "hyperthyroidism", "neuroblastoma", "rheumatoid arthritis"]
last_modified_at: 2026-10-30
description: "Cabazitaxel: predicted new indication female breast carcinoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Cabazitaxel
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Cabazitaxel: taxane microtubule inhibitor → 女性乳癌 (female breast carcinoma)
{: .text-alpha }

Note: the page language is English, so the main prediction is written once as "female breast carcinoma".

## Cabazitaxel: taxane microtubule inhibitor → female breast carcinoma
{: .text-alpha }

## One-Sentence Summary

Cabazitaxel is a taxane-class cytotoxic drug that stabilises microtubules.
The TxGNN model predicts it may be effective for **female breast carcinoma**. No clinical trials are listed for this prediction, but **20 publications** were compiled, including one randomised phase II neoadjuvant study (GENEVIEVE) and its long-term follow-up. Most of the other publications are preclinical or review articles.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | female breast carcinoma |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on the published literature, cabazitaxel is a taxane that stabilises microtubules and blocks cell division, the same class as paclitaxel and docetaxel, which are established in breast cancer treatment.

Cabazitaxel has a low affinity for P-glycoprotein, and studies in resistant cell models show it is less cross-resistant than paclitaxel and docetaxel. This suggests possible activity in taxane-resistant breast tumours.

Human data in breast cancer come from the GENEVIEVE randomised phase II study, which compared neoadjuvant cabazitaxel with weekly paclitaxel in HER2-negative disease (triple-negative or luminal B), and from a phase I/II study of cabazitaxel plus capecitabine in metastatic breast cancer after anthracycline and taxane treatment. The remaining publications are mostly preclinical nanoformulation work.

## Clinical Trial Evidence

Currently no related clinical trials registered. The human studies identified are reported in the literature below.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28768217](https://pubmed.ncbi.nlm.nih.gov/28768217/) | 2017 | Randomised phase II | Eur J Cancer | GENEVIEVE: cabazitaxel vs weekly paclitaxel as neoadjuvant treatment in operable triple-negative or luminal B/HER2-negative breast cancer, with pathological complete response as the endpoint |
| [38663168](https://pubmed.ncbi.nlm.nih.gov/38663168/) | 2024 | Randomised phase II (long-term follow-up) | ESMO Open | Long-term outcomes of GENEVIEVE; the earlier report had shown differences in pCR rates |
| [21339064](https://pubmed.ncbi.nlm.nih.gov/21339064/) | 2011 | Phase I/II | Eur J Cancer | Cabazitaxel plus capecitabine in metastatic breast cancer after anthracycline and taxane treatment; assessed maximum tolerated dose, safety and activity |
| [25416788](https://pubmed.ncbi.nlm.nih.gov/25416788/) | 2015 | Preclinical/Review | Mol Cancer Ther | Resistance mechanisms; cabazitaxel was less cross-resistant than paclitaxel and docetaxel in resistant models, including MCF-7 breast cancer variants |
| [33753567](https://pubmed.ncbi.nlm.nih.gov/33753567/) | 2021 | Preclinical | J Immunother Cancer | Cabazitaxel's effect on macrophages improves CD47-targeted immunotherapy in triple-negative breast cancer |
| [30529259](https://pubmed.ncbi.nlm.nih.gov/30529259/) | 2019 | Preclinical | J Control Release | Cabazitaxel-loaded nanoparticles gave complete remission in 6 of 8 tumours in a patient-derived breast cancer xenograft |
| [38562610](https://pubmed.ncbi.nlm.nih.gov/38562610/) | 2024 | Preclinical | Int J Nanomedicine | Cabazitaxel-loaded poly(alkyl cyanoacrylate) nanoparticle variants, building on a triple-negative breast cancer xenograft model |
| [28504249](https://pubmed.ncbi.nlm.nih.gov/28504249/) | 2017 | Preclinical | Acta Pharmacol Sin | Cabazitaxel-loaded polymeric micelles against breast cancer metastasis |
| [30521787](https://pubmed.ncbi.nlm.nih.gov/30521787/) | 2019 | Preclinical | Chem Phys Lipids | Cabazitaxel and thymoquinone co-loaded lipospheres for breast cancer |
| [33360926](https://pubmed.ncbi.nlm.nih.gov/33360926/) | 2021 | Preclinical | Colloids Surf B | Cabazitaxel-loaded nanostructured lipid carriers tested in breast cancer cell lines |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 4376H | Cabazitaxel Juno | Concentrated injection 60 mg in 1.5 mL, with diluent | Not recorded in the local data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (taxane, microtubule inhibitor) |
| Myelosuppression Risk | High (neutropenia is a leading toxicity of taxanes) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Full blood count with differential, liver function, renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

Please also refer to the Product Information (PI) warnings and precautions.

## Safety Considerations

- **Drug Interactions**: The data compiled for this report list 100 interactions. Examples include:
  - Major: deferiprone, samarium (153Sm) lexidronam
  - Moderate: aprepitant, clarithromycin, clotrimazole, metronidazole, miconazole, rosuvastatin, simvastatin, ticagrelor, cobicistat, deferasirox

For other safety information, including warnings and contraindications, please refer to the TGA-approved Product Information (PI).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Cabazitaxel belongs to a drug class already established in breast cancer, and a randomised phase II study (GENEVIEVE) directly studied it in breast cancer. However, no registered trials were compiled, the evidence is limited to one phase II study with a phase I/II study, and cabazitaxel carries significant myelosuppression risk.

**To proceed, the following is needed:**
- Review of the full GENEVIEVE results (efficacy against the paclitaxel comparator) to judge clinical benefit
- Confirmation of the mechanism of action data
- Review of the TGA Product Information for warnings and contraindications
- A haematological and toxicity monitoring plan appropriate for breast cancer patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

