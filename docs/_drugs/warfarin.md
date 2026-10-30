---
layout: default
title: Warfarin
parent: Model Prediction Only (L5)
nav_order: 787
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-30
description: "Warfarin: predicted new indication Heparin cofactor 2 deficiency (evidence level L4). Approved use: Pulmonary embolism, thrombotic disease, intracranial embolism"
monitor_inn: "Warfarin"
predicted_indications: ["heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "thrombophilia", "rheumatoid arthritis", "breast fibrocystic disease", "benign mammary dysplasia"]
---

# Warfarin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Warfarin: From Thrombotic Disease to heparin cofactor 2 deficiency
{: .text-alpha }

## One-Sentence Summary

Warfarin is an oral vitamin K antagonist anticoagulant, originally used for pulmonary embolism, thrombotic disease and intracranial embolism.
The TxGNN model predicts it may be useful for **heparin cofactor II deficiency**, an inherited thrombophilia.
Support is limited to **3 case reports** and **no registered clinical trials**, and the prediction is largely an extension of its existing thrombotic indication rather than true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary embolism, thrombotic disease, intracranial embolism (the ARTG entry in the data compiled for this report has no approved indication text) |
| Predicted New Indication | Heparin cofactor 2 deficiency |
| TxGNN Prediction Score | 0.9987 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, warfarin is a vitamin K antagonist that reduces synthesis of clotting factors II, VII, IX and X. Its efficacy in venous thromboembolism is well established.

Heparin cofactor II deficiency is an inherited thrombophilia, so patients are prone to venous thrombosis. Long-term oral anticoagulation is a plausible management option, and the case reports describe patients with thrombosis treated with warfarin. This is essentially an extension of the existing thrombotic-disease indication to a specific at-risk population, not a new mechanism of action.

Other high-scoring predictions have weaker support. Antithrombin deficiency type 2 (rank 3) and thrombophilia (rank 4) are also close to the original use. Rheumatoid arthritis, the breast conditions and migraine are explained mainly by drug-interaction studies or anecdotal reports, not by a therapeutic mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered for heparin cofactor II deficiency.

For context, the broader thrombophilia prediction (rank 4) has one trial:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00895505](https://clinicaltrials.gov/study/NCT00895505) | Phase 3 | Unknown | 300 | D-dimer-guided duration of oral anticoagulant secondary prophylaxis after unprovoked DVT. It tests a duration strategy, not warfarin efficacy itself. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2214444](https://pubmed.ncbi.nlm.nih.gov/2214444/) | 1990 | Case report | Kyobu Geka | Adolescent with familial heparin cofactor II deficiency and a right ventricular thrombus mimicking a myxoma; the thrombus was surgically removed. |
| [2033902](https://pubmed.ncbi.nlm.nih.gov/2033902/) | 1991 | Case report | Nihon Kyobu Shikkan Gakkai Zasshi | Woman with congenital antithrombin deficiency and repeated thrombosis, treated with warfarin for 7 years. This is a related antithrombin deficiency report, not heparin cofactor II deficiency. |
| [11570053](https://pubmed.ncbi.nlm.nih.gov/11570053/) | 2001 | Case report (family) | J UOEH | Family with multiple thromboses, including infant onset; one child developed recurrent DVT despite warfarin. Known hereditary thrombophilias were excluded. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 2209G | Coumadin | Tablet containing warfarin sodium 2 mg | Not stated in the data compiled for this report |

## Cytotoxicity

Not applicable. Warfarin is an anticoagulant, not an antineoplastic drug.

## Safety Considerations

- **Contraindications flagged by the knowledge graph (not label text):** Warfarin has drug-disease contraindication links to conditions including liver failure and liver disease, impaired renal function, blood coagulation disease, hypertension, congestive heart failure, anaemia, cholestasis, hypothyroidism, nephrotic syndrome, psychotic and mental disorders, substance abuse/dependence, and chronic diarrhoeal disease. These must be checked against the TGA-approved Product Information (PI).
- **Drug interactions:** The compiled data shows 100 interactions, of which the first 20 were retrieved. Major interactions include **acetylsalicylic acid** and **metronidazole**. Moderate interactions include ranitidine, rabeprazole, doxycycline, amoxicillin, metformin, bupropion, aprepitant, mesalazine and several corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide). Minor interactions include acarbose, albiglutide and ascorbic acid.
- **Reported safety issue:** Warfarin-induced skin necrosis is a rare complication (0.01–0.1%), noted in the thrombophilia literature.

Please also refer to the TGA-approved Product Information (PI) for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Support for heparin cofactor II deficiency is limited to a few case reports, with no trials. The predicted use largely overlaps with warfarin's existing thrombotic-disease indication, so this is a population refinement rather than a new repurposing opportunity. Warfarin's bleeding risk and heavy interaction burden also call for caution.

**To proceed, the following is needed:**
- The TGA Product Information (warnings, contraindications and approved indications), since the label data is missing from the compiled data
- Mechanism of action data (for example, from DrugBank)
- Controlled or cohort data on warfarin in inherited thrombophilias, including heparin cofactor II deficiency
- Comparison with direct oral anticoagulants (DOACs), which are now first-line for secondary VTE prevention, although evidence in severe thrombophilia is limited (ISTH 2024 communication)
- A pharmacovigilance and INR monitoring plan, including interaction management
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

