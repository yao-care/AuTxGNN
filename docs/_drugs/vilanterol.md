---
layout: default
title: Vilanterol
parent: Model Prediction Only (L5)
nav_order: 778
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-30
monitor_inn: "vilanterol"
predicted_indications: ["hyperlucent lung", "tracheal stenosis", "bronchial neoplasm (disease)", "respiratory malformation", "tracheal calcification", "laryngotracheitis"]
description: "Vilanterol: predicted new indication Hyperlucent lung (evidence level L5). Approved use: Not recorded in the local data"
---

# Vilanterol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Vilanterol: Hyperlucent lung
{: .text-alpha }

## One-Sentence Summary

Vilanterol is a long-acting beta2-agonist (LABA) used in fixed-dose inhaled combinations for chronic obstructive pulmonary disease (COPD) and asthma.
The TxGNN model predicts it may be effective for **Hyperlucent Lung**.
The data compiled for this report include **28 clinical trials** and **20 publications**, all of which test vilanterol as part of a combination product.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hyperlucent lung |
| TxGNN Prediction Score | 0.9972 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (3 of 3 items) – TGA (ARTG) registration status is not included in this data |
| Number of ARTG Entries | 3 (valid: 3) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. From general pharmacology, vilanterol is a long-acting beta2-adrenoceptor agonist. It relaxes bronchial smooth muscle and produces bronchodilation, which directly addresses airflow obstruction.


One caveat applies. The evidence comes from fixed-dose combinations (vilanterol with fluticasone furoate, umeclidinium, or both), so the contribution of vilanterol alone cannot be separated out.

---

## Clinical Trial Evidence

The data include 28 registered trials. The table below lists the 10 most relevant, prioritising completed Phase 3 studies with direct efficacy data. No ANZCTR identifiers were available.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03162055](https://clinicaltrials.gov/study/NCT03162055) | Phase 3 | Completed | 1119 | Glycopyrronium/formoterol vs umeclidinium/vilanterol over 24 weeks in moderate to very severe COPD (AERISTO) |
| [NCT05062304](https://clinicaltrials.gov/study/NCT05062304) | N/A | Completed | 17281 | Once-daily single-inhaler triple vs dual therapy in COPD, listed as the IMPACT trial (the registry record has no phase assigned) |
| [NCT01706198](https://clinicaltrials.gov/study/NCT01706198) | Phase 3 | Completed | 4233 | Open-label 12-month effectiveness study of fluticasone furoate/vilanterol vs usual maintenance therapy in asthma |
| [NCT02301975](https://clinicaltrials.gov/study/NCT02301975) | Phase 3 | Completed | 1526 | Non-inferiority study of fluticasone furoate/vilanterol vs fluticasone propionate/salmeterol in controlled asthma |
| [NCT01686633](https://clinicaltrials.gov/study/NCT01686633) | Phase 3 | Completed | 1040 | Fluticasone furoate/vilanterol 200/25 and 100/25 vs fluticasone furoate alone in persistent asthma over 12 weeks |
| [NCT01777334](https://clinicaltrials.gov/study/NCT01777334) | Phase 3 | Completed | 905 | Umeclidinium/vilanterol vs tiotropium on trough FEV1 over 24 weeks in COPD |
| [NCT01134042](https://clinicaltrials.gov/study/NCT01134042) | Phase 3 | Completed | 587 | Fluticasone furoate/vilanterol vs fluticasone furoate alone vs fluticasone propionate in persistent asthma over 24 weeks |
| [NCT01342913](https://clinicaltrials.gov/study/NCT01342913) | Phase 3 | Completed | 528 | 24-hour lung function with fluticasone furoate/vilanterol once daily vs salmeterol/fluticasone propionate twice daily in COPD |
| [NCT01323621](https://clinicaltrials.gov/study/NCT01323621) | Phase 3 | Completed | 512 | 24-hour lung function with fluticasone furoate/vilanterol 100/25 vs fluticasone propionate/salmeterol in COPD |
| [NCT02094937](https://clinicaltrials.gov/study/NCT02094937) | Phase 3 | Completed | 430 | Step-down from fluticasone furoate/vilanterol to fluticasone furoate or fluticasone propionate in well-controlled Japanese asthma patients |

Other trials in the data are small Phase 1/2 pharmacokinetic and pharmacodynamic studies, three withdrawn studies with zero enrolment, and trials focused on safety endpoints such as bone density and arterial stiffness.

---

## Literature Evidence

The data include 20 publications for this indication. The table below lists the 10 most relevant, prioritising RCTs, then systematic reviews and meta-analyses, then real-world cohort studies.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29668352](https://pubmed.ncbi.nlm.nih.gov/29668352/) | 2018 | RCT | N Engl J Med | IMPACT: once-daily single-inhaler triple therapy vs dual therapy in COPD |
| [28375647](https://pubmed.ncbi.nlm.nih.gov/28375647/) | 2017 | RCT | Am J Respir Crit Care Med | FULFIL: once-daily triple therapy vs dual ICS/LABA therapy in COPD |
| [32918892](https://pubmed.ncbi.nlm.nih.gov/32918892/) | 2021 | RCT | Lancet Respir Med | CAPTAIN: triple therapy (fluticasone furoate/umeclidinium/vilanterol) vs fluticasone furoate/vilanterol in inadequately controlled asthma |
| [32162970](https://pubmed.ncbi.nlm.nih.gov/32162970/) | 2020 | RCT (post hoc) | Am J Respir Crit Care Med | Reduced all-cause mortality with fluticasone furoate/umeclidinium/vilanterol vs umeclidinium/vilanterol in COPD |
| [35849317](https://pubmed.ncbi.nlm.nih.gov/35849317/) | 2022 | Network meta-analysis | Adv Ther | Comparative efficacy of fluticasone furoate/umeclidinium/vilanterol against other triple and dual therapies |
| [39696097](https://pubmed.ncbi.nlm.nih.gov/39696097/) | 2024 | Systematic review and meta-analysis | BMC Pulm Med | Umeclidinium/vilanterol compared with other bronchodilators in COPD |
| [31389190](https://pubmed.ncbi.nlm.nih.gov/31389190/) | 2019 | Systematic review | Clin Respir J | Fixed-dose umeclidinium/vilanterol for COPD |
| [39797646](https://pubmed.ncbi.nlm.nih.gov/39797646/) | 2024 | Cohort | BMJ | Comparative effectiveness and safety of single-inhaler triple therapies in routine practice |
| [40619503](https://pubmed.ncbi.nlm.nih.gov/40619503/) | 2025 | Cohort | Adv Ther | Real-world comparison of two single-inhaler triple therapies in patients stepping up from dual therapy |
| [28956463](https://pubmed.ncbi.nlm.nih.gov/28956463/) | 2017 | Review | Expert Rev Respir Med | Role of once-daily fluticasone furoate/vilanterol in stable COPD |

---

## Australia Market Information

All three ARTG entries are fixed-dose combination inhalers containing vilanterol 25 micrograms per dose. The approved indication text is not recorded in the data compiled for this report.

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10188F | Anoro Ellipta 62.5/25 | Inhalation powder (umeclidinium 62.5 mcg with vilanterol 25 mcg per dose, 30 doses) | Not recorded; refer to the Product Information |
| ARTG 11124L | Breo Ellipta 100/25 | Inhalation powder (fluticasone furoate 100 mcg with vilanterol 25 mcg per dose, 30 doses) | Not recorded; refer to the Product Information |
| ARTG 11379X | Trelegy Ellipta 100/62.5/25 | Inhalation powder (fluticasone furoate 100 mcg, umeclidinium 62.5 mcg and vilanterol 25 mcg per dose, 30 doses) | Not recorded; refer to the Product Information |

---

## Safety Considerations

- **Drug Interactions**: The data list 388 recorded interactions. The entries shown include:
  - **Moderate**: antidiabetic agents (acarbose, albiglutide, alogliptin, canagliflozin, chlorpropamide, dapagliflozin, dulaglutide, empagliflozin), QT-prolonging drugs (cisapride, clarithromycin, dolasetron), and sympathomimetics (diethylpropion, ephedrine, epinephrine).
  - **Minor**: corticosteroids (beclomethasone, betamethasone, budesonide, dexamethasone).

Product-specific warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for these. The cardiac safety studies in the literature (thorough QT studies of vilanterol combinations in healthy subjects) may also be useful background.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Obstructive lung disease covers the conditions vilanterol-containing inhalers are already used for. Multiple completed Phase 3 trials and large RCTs (IMPACT, FULFIL, CAPTAIN) provide direct evidence, and three products are marketed in Australia. The guardrails reflect that all evidence is for fixed-dose combinations, and that the Australian indication text and safety data were not available for this report.

**To proceed, the following is needed:**
- Approved indication wording, warnings and contraindications from the current TGA Product Information for each ARTG entry
- Mechanism of action data (for example from DrugBank)
- A clear statement that the evidence applies to the specific combination products, not to vilanterol alone
- Review of the interaction profile, particularly for QT-prolonging drugs, sympathomimetics and antidiabetic agents

**Other predicted indications (not recommended for progression):**
- Hyperlucent lung, tracheal stenosis, respiratory malformation, tracheal calcification and laryngotracheitis: **Hold**. These have no supporting trials or relevant literature, and the high scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. For respiratory malformation, the retrieved publications do not address the condition.
- Bronchial neoplasm: **Research Question**. The only related trial (NCT04536675, Phase 3, n=204) tests dual bronchodilators for COPD comorbidity in lung cancer surgery patients, so it does not support an effect on the tumour itself.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

