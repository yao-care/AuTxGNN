---
layout: default
title: Ascorbic Acid
parent: Model Prediction Only (L5)
nav_order: 62
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ascorbic Acid: predicted new indication Non-syndromic esophageal malformation . Best-supported candidate: inj… (evidence level L5). Approved use: Ascorbic acid deficiency"
monitor_inn: "Ascorbic acid"
predicted_indications: ["non-syndromic esophageal malformation", "esophageal disease", "congenital prothrombin deficiency", "injury", "biotin metabolic disease", "segmental odontomaxillary dysplasia", "perinatal disease", "florid cemento-osseous dysplasia", "disease by subcellular system affected", "vitamin deficiency disorder"]
---

# Ascorbic Acid
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

# Ascorbic Acid: From Ascorbic Acid Deficiency (Scurvy) to Injury

## One-Sentence Summary

Ascorbic acid (vitamin C) is an essential nutrient, originally used to treat and prevent ascorbic acid deficiency and scurvy.
The TxGNN model's top-ranked prediction is **non-syndromic esophageal malformation**, but this has no supporting evidence. The best-supported repurposing direction in the data compiled for this report is **injury** (oxidative and ischaemia-reperfusion injury), with **16 clinical trials** and **20 publications**. These are mostly small, early-phase or heterogeneous studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ascorbic acid deficiency; scurvy (the ARTG entry has no indication text recorded) |
| Predicted New Indication | Non-syndromic esophageal malformation (rank 1, no evidence). Best-supported candidate: injury (rank 4) |
| TxGNN Prediction Score | 99.96% (rank 1 indication); 99.60% (injury) |
| Evidence Level | L5 for the rank 1 indication; L2 for injury |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold (rank 1 indication). Injury: Research Question. |

The rank 1 prediction has no mechanistic link, trials or literature, so the sections below focus mainly on the best-supported candidate (injury). The other candidates are summarised in a short table afterwards.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, ascorbic acid is an antioxidant and a cofactor for collagen synthesis. Its efficacy in correcting deficiency is well established.

**Rank 1 (non-syndromic esophageal malformation):** No plausible link. This is a congenital structural anomaly, and ascorbic acid has no known role in oesophageal embryogenesis. The very high score is a graph-based prediction only.

**Injury (rank 4):** Antioxidant and collagen-supporting actions plausibly support roles in wound and tendon healing, attenuation of oxidative injury (sepsis-induced lung injury, ischaemia-reperfusion, cardiac surgery) and burn resuscitation. "Injury" is a heterogeneous category, so the evidence is scattered across distinct conditions. One in vitro study (PMID 39769123) suggests high-dose vitamin C may harm tendon cells, so dose and context matter.

**Other candidates**

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Vitamin deficiency disorder | 99.47% | L3 | Closest to the original indication, so largely on-label rather than true repurposing. Supported by a Phase 1 bioavailability study, an observational latent-scurvy study, case reports and reviews. Extension to alcohol use disorder, spondylodiscitis and care home residents is reasonable if guided by measured vitamin C status. Proceed with Guardrails. |
| Perinatal disease | 99.47% | L3 | One small completed RCT (n=60) of ascorbic acid plus ibuprofen in neonatal hypoxic ischaemic encephalopathy. The combination limits attribution and neonatal dosing and safety need evaluation. |
| Oesophageal disease | 99.90% | L4 | Mixed preclinical and review literature, with no clinical trials. One rat study (PMID 17953708) reports **enhanced** oesophageal carcinogenesis with ascorbic acid in an acid reflux model, which is a safety signal. |
| Congenital prothrombin deficiency, biotin metabolic disease, segmental odontomaxillary dysplasia, florid cemento-osseous dysplasia, disease by subcellular system affected | 99.4–99.7% | L5 | No plausible mechanism or clinical evidence. Prediction only. |

---

## Clinical Trial Evidence

Trials for **injury** (up to 10 most relevant shown; 16 retrieved):

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02106975](https://clinicaltrials.gov/study/NCT02106975) | Phase 2 | Completed | 170 | IV vitamin C in sepsis-induced acute lung injury; endpoints include SOFA score, oxygenation and inflammatory and vascular injury biomarkers |
| [NCT03509662](https://clinicaltrials.gov/study/NCT03509662) | Phase 2 | Completed | 270 | Early high-dose vitamin C in post-cardiac arrest syndrome (reperfusion injury) |
| [NCT01167569](https://clinicaltrials.gov/study/NCT01167569) | Phase 4 | Completed | 57 | Double-blind RCT of high-dose IV vitamin C on outcomes after cardiac surgery |
| [NCT04344184](https://clinicaltrials.gov/study/NCT04344184) | Phase 2 | Completed | 47 | Safety of 96-hour IV vitamin C infusion in COVID-19 acute lung injury |
| [NCT04153487](https://clinicaltrials.gov/study/NCT04153487) | Phase 2 | Completed | 40 | Ascorbic acid infusion in transfusion-related acute lung injury |
| [NCT05327348](https://clinicaltrials.gov/study/NCT05327348) | Phase 3 | Unknown | 34 | Perioperative parenteral ascorbic acid for oxidative stress in free flap surgery; biomarker endpoint |
| [NCT03965637](https://clinicaltrials.gov/study/NCT03965637) | Phase 3 | Completed | 80 | Ascorbic acid on intraoperative blood loss and wound healing in hysterectomy |
| [NCT02455180](https://clinicaltrials.gov/study/NCT02455180) | Phase 4 | Completed | 20 | Pharmacokinetics of two high-dose IV regimens in critically ill patients; informs dosing, not efficacy |
| [NCT06384833](https://clinicaltrials.gov/study/NCT06384833) | Phase 4 | Unknown | 110 | Vitamin C plus N-acetylcysteine after rotator cuff repair; combination confounds attribution |
| [NCT01897792](https://clinicaltrials.gov/study/NCT01897792) | Phase 2 | Terminated | 11 | Antioxidant vitamins (C and E) after severe trauma; underpowered |

Other trials of note:
- Perinatal disease: [NCT00624871](https://clinicaltrials.gov/study/NCT00624871) (completed, n=60) tested ascorbic acid plus ibuprofen in neonatal hypoxic ischaemic encephalopathy.
- Vitamin deficiency disorder: [NCT03467022](https://clinicaltrials.gov/study/NCT03467022) (completed, n=47, observational) examined latent scurvy risk in alcohol withdrawal. [NCT02606773](https://clinicaltrials.gov/study/NCT02606773) (Phase 1, n=32) compared the bioavailability of a liposomal vitamin C product.

No ANZCTR identifiers appear in the data compiled for this report. No Phase 3 trial in the injury group provides confirmatory efficacy evidence. The only Phase 3 trials are small or of unknown status.

---

## Literature Evidence

Publications for **injury** (up to 10 shown, prioritising higher-tier types):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38051821](https://pubmed.ncbi.nlm.nih.gov/38051821/) | 2024 | Guideline | J Burn Care Res | American Burn Association guideline on burn shock resuscitation |
| [31440996](https://pubmed.ncbi.nlm.nih.gov/31440996/) | 2020 | Review | Neurocrit Care | High-dose IV ascorbic acid in traumatic brain injury: rationale based on oxidative stress and secondary injury |
| [23994411](https://pubmed.ncbi.nlm.nih.gov/23994411/) | 2013 | Review | J Am Coll Cardiol | Ascorbic acid for prevention of contrast-induced acute kidney injury |
| [27600125](https://pubmed.ncbi.nlm.nih.gov/27600125/) | 2016 | Review | Crit Care Clin | Vitamin C in burn resuscitation: antioxidant effects on capillary permeability |
| [30802561](https://pubmed.ncbi.nlm.nih.gov/30802561/) | 2019 | Review | J Am Acad Dermatol | Management of acute radiation dermatitis, including topical agents |
| [32768934](https://pubmed.ncbi.nlm.nih.gov/32768934/) | 2020 | Review | Biomed Pharmacother | Post-concussion protocols, including nutraceuticals |
| [37199082](https://pubmed.ncbi.nlm.nih.gov/37199082/) | 2023 | Animal study | Clin Exp Pharmacol Physiol | Melatonin plus ascorbic acid protects against sepsis-induced lung injury in rats |
| [21953354](https://pubmed.ncbi.nlm.nih.gov/21953354/) | 2011 | Animal study | Intensive Care Med | Ascorbic acid mitigates myocardial injury after cardiac arrest in rats |
| [39769123](https://pubmed.ncbi.nlm.nih.gov/39769123/) | 2024 | In vitro | Int J Mol Sci | High-dose vitamin C and tendon cell degeneration; dose-dependent effects |
| [26084697](https://pubmed.ncbi.nlm.nih.gov/26084697/) | 2015 | Crossover study | Am J Physiol Regul Integr Comp Physiol | Ascorbic acid (2 g daily) diminished microparticle elevations after SCUBA diving (n=14) |

Related literature for **vitamin deficiency disorder** includes the cohort study [38291316](https://pubmed.ncbi.nlm.nih.gov/38291316/) (2024, ANZ J Surg) on ascorbic acid deficiency in spondylodiscitis patients, and several scurvy case reports and reviews.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Licence 674L | Not recorded | Not recorded | Not recorded |

One valid single-ingredient registration is recorded, with no cancelled entries. Product name, dosage form, manufacturer and indication text are not available in the data compiled for this report, and the licence number should be verified against the ARTG.

---

## Safety Considerations

**Contraindication-related disease associations (knowledge graph, not label text):** The TxGNN knowledge graph links ascorbic acid to caution or contraindication in several conditions, including:
- Kidney disease, anuria, nephrocalcinosis and primary hyperoxaluria
- Hypercalcaemia, hyperparathyroidism and phosphorus metabolism disease
- Hereditary haemochromatosis, sickle cell anaemia and blood coagulation disease
- Diabetes mellitus and diabetic ketoacidosis
- Hypertension, epilepsy, liver disease, gallbladder disease and peptic ulcer disease
- Rheumatoid arthritis, systemic lupus erythematosus, multiple sclerosis and sarcoidosis
- Allergic and vasomotor rhinitis, sunburn and potassium deficiency disease

These are graph-derived associations and should be confirmed against the TGA-approved Product Information (PI).

**Drug Interactions** (25 recorded; 20 listed in the data):
- **Moderate:** amphetamine, dextroamphetamine, lisdexamfetamine, metamfetamine, benzphetamine, aluminium hydroxide, bortezomib, deferoxamine
- **Minor:** paclitaxel, cisplatin, doxorubicin (including liposomal), pseudoephedrine, ephedrine, ethinylestradiol, flecainide, fluphenazine, indinavir, mexiletine

**Study-specific signals:**
- One rat study reported enhanced oesophageal carcinogenesis with ascorbic acid in an acid reflux model (PMID 17953708).
- High-dose vitamin C may be detrimental to tendon cells in vitro.
- Neonatal use would need careful dose and safety evaluation.

Please refer to the TGA-approved Product Information (PI) for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold** for the top-ranked prediction (non-syndromic esophageal malformation). **Proceed with Guardrails** for vitamin deficiency disorder, which is largely on-label. **Research Question** for injury and perinatal disease.

**Rationale:**
- The rank 1 prediction has no mechanistic rationale, trials or literature, so its high TxGNN score is not clinically actionable.
- Injury has the broadest trial activity (L2), but the trials are small, early-phase or terminated, and the category mixes unrelated conditions. No confirmatory Phase 3 result is available.
- Vitamin deficiency disorder is the most defensible direction, as it extends the established original indication.

**To proceed, the following is needed:**
- Mechanism of action data (currently unavailable)
- TGA Product Information with warnings and contraindications for the registered product (a blocking data gap for safety screening)
- Product name, dosage form and indication details for ARTG licence 674L
- For injury: a specific, well-defined condition (for example sepsis-induced lung injury or burns), with adequately powered Phase 3 RCTs and defined dose and route
- For vitamin deficiency disorder: studies targeting at-risk Australian populations, guided by measured vitamin C status
- Dose-response and safety evaluation, including renal risk, interactions and neonatal use where relevant
- Route compatibility assessment (IV and oral formulations) for the candidate indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

