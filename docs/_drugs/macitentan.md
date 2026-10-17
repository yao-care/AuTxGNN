---
layout: default
title: Macitentan
parent: Model Prediction Only (L5)
nav_order: 441
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Macitentan: predicted new indication Pulmonary arterial hypertension associated with congenital heart dise… (evidence level L5). Approved use: Pulmonary arterial hypertension"
monitor_inn: "Macitentan"
predicted_indications: ["pulmonary arteriovenous malformation (disease)", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia"]
---

# Macitentan
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

# Macitentan: From Pulmonary Arterial Hypertension to PAH Associated with Congenital Heart Disease

## One-Sentence Summary

Macitentan is an oral endothelin receptor antagonist originally used to treat pulmonary arterial hypertension (PAH).
The TxGNN model predicts it may be effective for **pulmonary arterial hypertension associated with congenital heart disease (CHD-PAH)**,
with **no registered clinical trials** but **18 publications** (including two randomised controlled trials in related populations) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary arterial hypertension (the TGA approved-indication text is not available in the data compiled for this report) |
| Predicted New Indication | Pulmonary arterial hypertension associated with congenital heart disease |
| TxGNN Prediction Score | 98.75% |
| Evidence Level | L1 (based on the data's classification; see the caveat below) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, macitentan is a dual endothelin receptor antagonist (ETA/ETB). Endothelin-1 drives vasoconstriction and vascular remodelling in the pulmonary circulation.

CHD-PAH, including Eisenmenger syndrome, is a subgroup of Group 1 PAH and shares the same endothelin-driven pathology as the approved indication. This is therefore better described as a PAH subgroup extension than a true repurposing. The prediction is mechanistically coherent, and the literature includes a dedicated Phase 3 trial (MAESTRO) in Eisenmenger syndrome.

**Caveat on evidence level:** The L1 grading relies on MAESTRO (a Phase 3 trial that was neutral on its primary exercise-capacity endpoint, with an acceptable safety profile), the paediatric TOMORROW trial, and subgroup analyses of the SERAPHIN trial. Study designs were inferred from partly truncated titles and abstracts, so they should be verified before the grading is relied on.

## Clinical Trial Evidence

Currently no related clinical trials registered for this indication in the data compiled for this report.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30586694](https://pubmed.ncbi.nlm.nih.gov/30586694/) | 2019 | RCT (Phase 3, MAESTRO) | Circulation | 16-week double-blind placebo-controlled trial of macitentan in Eisenmenger syndrome; evaluated efficacy and safety |
| [41796854](https://pubmed.ncbi.nlm.nih.gov/41796854/) | 2026 | RCT (TOMORROW) | J Pediatr | Macitentan vs standard of care in paediatric PAH; pharmacokinetics, efficacy and safety |
| [28867027](https://pubmed.ncbi.nlm.nih.gov/28867027/) | 2017 | RCT (post-hoc subgroup) | Heart Lung Circ | Macitentan in PAH associated with congenital heart defects |
| [31096477](https://pubmed.ncbi.nlm.nih.gov/31096477/) | 2019 | Systematic review and meta-analysis | Medicine | Safety and efficacy of PAH-specific therapy in Eisenmenger syndrome |
| [38276220](https://pubmed.ncbi.nlm.nih.gov/38276220/) | 2023 | Review | J Pers Med | Current management and future directions for CHD-PAH |
| [39585521](https://pubmed.ncbi.nlm.nih.gov/39585521/) | 2024 | Real-world cohort | Cardiol Ther | OPUS/OrPHeUS real-world data on macitentan in CHD-PAH |
| [36196862](https://pubmed.ncbi.nlm.nih.gov/36196862/) | 2022 | Cohort | Anatol J Cardiol | Consistent effectiveness and safety of macitentan in idiopathic and CHD-associated PAH (single centre) |
| [40616677](https://pubmed.ncbi.nlm.nih.gov/40616677/) | 2026 | Multicentre cohort | Pediatr Cardiol | Observational safety and efficacy of macitentan in children with PAH |
| [36329372](https://pubmed.ncbi.nlm.nih.gov/36329372/) | 2023 | Real-world cohort | Drugs Real World Outcomes | Post-marketing safety and outcomes in Asian PAH patients |
| [28532389](https://pubmed.ncbi.nlm.nih.gov/28532389/) | 2017 | Case report | BMC Cardiovasc Disord | First reported use of macitentan in a Fontan circulation |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10134J | Opsumit | Tablet 10 mg (oral) | Not available in the data compiled for this report |

## Safety Considerations

Specific warnings and contraindications from the product label are not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for full safety information.

**Drug Interactions:** 58 interactions are listed. Major interactions include:
- Clarithromycin
- Erythromycin
- Ketoconazole
- Cobicistat
- Lumacaftor

Moderate interactions include aprepitant, dexamethasone, cimetidine, fluconazole, ticagrelor and others. Many of these involve CYP3A4 inhibitors or inducers.

**Class-related considerations to review against the PI:** embryo-fetal toxicity (contraception and pregnancy testing), hepatotoxicity and anaemia monitoring, and caution in Eisenmenger patients with right-to-left shunts.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
CHD-PAH is a recognised PAH subgroup with the same endothelin-driven mechanism as the approved indication. Supporting data include a Phase 3 trial in Eisenmenger syndrome (neutral on its primary endpoint), a paediatric RCT and real-world cohorts, though the Eisenmenger trial did not meet its primary endpoint.

**To proceed, the following is needed:**
- Review of the TGA Product Information for current approved indications, warnings and contraindications
- Verification of the study designs and results of the key trials, including the SERAPHIN subgroup data
- A monitoring plan covering liver function, haemoglobin and pregnancy prevention
- A review of interacting medicines, especially strong CYP3A4 inhibitors and inducers
- Mechanism of action data to be confirmed from DrugBank

---

### Other Predictions (Not Recommended for Progression)

| Predicted Indication | TxGNN Score | Evidence Level | Decision |
|------|------|------|------|
| PAH associated with connective tissue disease | 98.59% | L1 (relies on SERAPHIN subgroup data not listed in the input; verify) | Proceed with Guardrails. The only listed trial (NCT03726398) was withdrawn with 0 participants. Real-world studies and a meta-analysis support use. |
| PAH associated with HIV infection | 98.59% | L4 | Research question. Only indirect registry data; significant antiretroviral interaction concern. |
| Pulmonary arteriovenous malformation | 98.89% | L5 | Hold. Structural malformation, and a vasodilator could worsen shunting. |
| PAH associated with chronic haemolytic anaemia | 98.59% | L5 | Hold. No evidence, and macitentan can cause anaemia. |
| PAH associated with schistosomiasis | 98.59% | L5 | Hold. Plausible mechanism but no evidence. |
| Hypotrichosis simplex of the scalp, congenital hypotrichosis milia, diffuse alopecia areata, alopecia | 93.73% to 98.24% | L5 | Hold. No plausible mechanism or evidence, and the teratogenic risk is unattractive for non-life-threatening conditions. |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

