---
layout: default
title: Desmopressin
parent: 僅模型預測 (L5)
nav_order: 147
evidence_level: L5
indication_count: 10
---

# Desmopressin
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

# Desmopressin: From Mild Haemophilia A / Von Willebrand Disease to Congenital Prothrombin Deficiency

---

## One-Sentence Summary

Desmopressin (DDAVP) is a synthetic vasopressin analogue with established haemostatic use in mild haemophilia A and von Willebrand disease, where it triggers endothelial release of von Willebrand factor (vWF) and Factor VIII to enhance primary haemostasis.
The TxGNN model predicts it may be effective for **Congenital Prothrombin Deficiency** (highest-ranked of 10 predicted indications, score 99.70%); however, supporting evidence comprises only **1 clinical trial** (Grade C relevance — different drug, different disease) and **4 publications** with no direct studies.
Critically, across all 10 TxGNN predictions, the most clinically actionable finding is **Primary Release Disorder of Platelets** (Rank 4, "Proceed with Guardrails"), while three other predictions — inherited thrombophilia, pseudo-von Willebrand disease, and thrombocytopenic purpura — carry documented or mechanistically predicted **harm signals** with Desmopressin.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available — no ARTG registration data captured in current dataset (see note below) |
| Predicted New Indication (Rank 1) | Congenital Prothrombin Deficiency |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L4 (mechanistic studies only; no direct clinical evidence) |
| Australia Market Status | Not found in current dataset (0 ARTG entries) |
| Number of ARTG Entries | 0 |
| Recommended Decision (Rank 1) | Hold |
| Most Actionable Prediction Overall | Primary Release Disorder of Platelets — **Proceed with Guardrails** |

> **Data Integrity Note:** The absence of ARTG entries almost certainly reflects a dataset retrieval gap rather than true non-registration. Desmopressin is commercially available in Australia under products such as Minirin®, DDAVP®, and Nocdurna® for indications including central diabetes insipidus, nocturnal enuresis, and haemostatic support. Clinicians should verify current registration status at [www.tga.gov.au/artg](https://www.tga.gov.au/artg).

---

## Why is This Prediction Reasonable?

Desmopressin acts as a selective V2 receptor (V2R) agonist on vascular endothelial cells. Activation of V2R triggers exocytosis of Weibel-Palade bodies, releasing pre-formed stores of von Willebrand factor (including high-molecular-weight multimers) and Factor VIII into the circulation. This surge in plasma vWF strengthens the GPIb–vWF–collagen primary adhesion axis, shortening bleeding time and providing transient haemostatic benefit. This mechanism is clinically well-validated in von Willebrand disease (Type 1 and selected Type 2 subtypes) and mild haemophilia A.

Congenital prothrombin deficiency (Factor II deficiency) is a rare autosomal recessive coagulopathy caused by reduced synthesis or impaired function of prothrombin, the central zymogen of the coagulation cascade. Prothrombin deficiency leads to inadequate thrombin generation, impairing fibrin clot formation. The TxGNN model's prediction likely reflects general proximity within the haemostasis disease domain of the knowledge graph. However, **Desmopressin has no direct pharmacological effect on prothrombin synthesis, secretion, or function** — its mechanism operates entirely through primary haemostasis (platelet adhesion enhancement) and FVIII release, upstream of and unrelated to Factor II.

The sole mechanistically plausible scenario would be in rare combined coagulation factor deficiency syndromes (e.g., combined Factor V and VIII deficiency, as described in PMID 2607619), where DDAVP's ability to raise FVIII levels could provide partial haemostatic bridging. This does not, however, constitute evidence for isolated prothrombin deficiency. The mechanistic disconnect significantly weakens this prediction, and the recommendation is **Hold** pending further mechanistic validation.

---

## All Predicted Indications — Summary

The TxGNN model predicted 10 new indications for Desmopressin. The following table provides a full overview, including critical safety flags:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Key Safety Flag |
|------|---------|-------------|----------------|----------------|-----------------|
| 1 | Congenital prothrombin deficiency | 99.70% | L4 | Hold | Weak mechanistic link (DDAVP does not affect Factor II) |
| 2 | Inherited thrombophilia | 99.44% | L4 | Hold | ⚠️ Potential contraindication — DDAVP promotes platelet aggregation in already hypercoagulable states |
| 3 | Glanzmann thrombasthenia | 99.30% | L4 | Research Question | Partial benefit plausible via GPIb-vWF alternative pathway; GPIIb/IIIa remains non-functional |
| 4 | **Primary release disorder of platelets** | **99.26%** | **L3** | **Proceed with Guardrails** | **Best mechanistic-evidence match; prospective clinical data available** |
| 5 | Pseudo-von Willebrand disease | 99.16% | L4 | Hold | ⚠️ Known contraindication — GPIbα gain-of-function mutation; DDAVP worsens thrombocytopenia |
| 6 | Scott syndrome | 99.16% | L5 | Hold | No mechanistic relevance — DDAVP cannot correct phosphatidylserine externalisation defect |
| 7 | Flood factor deficiency | 99.15% | L5 | Hold | ⚠️ Uncertain disease definition; term not standard — requires clarification before evaluation |
| 8 | Thrombocytopenic purpura (TTP) | 98.95% | L3 | Hold | ⚠️ Documented harm — DDAVP worsens TTP by releasing additional vWF multimers (PMID 15499705, PMID 21921792) |
| 9 | Bleeding diathesis due to collagen receptor defect | 98.95% | L4 | Research Question | Indirect mechanistic rationale — DDAVP-vWF may bridge collagen via GPIb-vWF-A3 domain pathway |
| 10 | Hereditary thrombocytosis with transverse limb defect | 98.95% | L5 | Hold | No evidence; DDAVP rationale absent in thrombocytosis setting |

### ⚠️ Safety Alert — Documented Harmful Predictions (Do Not Proceed)

Three of the 10 TxGNN predictions are **contraindicated or carry documented harm**:

- **Inherited Thrombophilia (Rank 2):** Conditions such as Factor V Leiden, Prothrombin G20210A mutation, Protein C/S deficiency, and antiphospholipid antibody syndrome are characterised by a hypercoagulable state. DDAVP-induced release of large vWF multimers further enhances platelet adhesion and aggregation, with a plausible risk of precipitating arterial or venous thrombosis. Literature (PMID 16460464) already documents DDAVP's association with inherited thrombotic thrombocytopenic purpura — a related thrombophilic condition.

- **Pseudo-von Willebrand Disease / Platelet-Type vWD (Rank 5):** This condition involves a gain-of-function GPIbα mutation (e.g., Met239Val) causing enhanced GPIb affinity for vWF. DDAVP release of high-molecular-weight vWF multimers would be avidly captured by the hypersensitive GPIbα, triggering spontaneous platelet aggregation, vWF-platelet complex formation, and consumption thrombocytopenia. PMID 27819553 explicitly documents the diagnostic and therapeutic hazards in this condition.

- **Thrombocytopenic Purpura / TTP (Rank 8):** TTP is driven by ADAMTS13 deficiency, leading to accumulation of ultra-large vWF multimers that promote microvascular platelet thrombi. DDAVP directly worsens this pathological mechanism by releasing additional large vWF multimers. **PMID 15499705 directly documents TTP symptom worsening after Desmopressin administration.** PMID 21921792 describes a Moschcowitz-like syndrome (TTP-equivalent) induced by DDAVP. The Phase 2 clinical trial NCT00632242 evaluated ARC1779 — an anti-vWF aptamer that *blocks* vWF — for TTP, confirming from the opposite direction that vWF is pathogenic in this condition.

---

## Clinical Trial Evidence (Rank 1: Congenital Prothrombin Deficiency)

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT04567511](https://clinicaltrials.gov/study/NCT04567511) | Phase 4 | Recruiting | 20 | Single-arm study of **Emicizumab** (not Desmopressin) in mild haemophilia A (FVIII 5–30%). Evaluates haemostatic laboratory parameters, joint health, and quality of life. **Relevance Grade C** — different drug (bispecific antibody bridging FIXa-FX), different disease (FVIII deficiency, not prothrombin deficiency). Provides contextual evidence that haemostatic interventions in mild coagulation factor deficiencies are an active research area, but offers no direct evidence for this repurposing hypothesis. |

No clinical trials directly investigating Desmopressin for congenital prothrombin deficiency are currently registered.

---

## Literature Evidence (Rank 1: Congenital Prothrombin Deficiency)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [7684674](https://pubmed.ncbi.nlm.nih.gov/7684674/) | 1993 | Narrative Review | *Drugs* | Rational treatment of inherited bleeding disorders; confirms DDAVP utility in mild haemophilia A and vWD. No specific evidence for prothrombin deficiency. Provides disease-class context only. |
| [21115138](https://pubmed.ncbi.nlm.nih.gov/21115138/) | 2011 | Narrative Review | *Autoimmunity Reviews* | Acquired haemophilia A — autoantibodies against FVIII. Disease context for coagulopathy management; no direct data linking DDAVP to prothrombin deficiency. |
| [2607619](https://pubmed.ncbi.nlm.nih.gov/2607619/) | 1989 | Case Report | *Japanese J Clinical Haematology* | DDAVP administered in combined Factor V + VIII deficiency in a 43-year-old male. Showed partial haemostatic benefit attributable to FVIII release. **Most mechanistically relevant result** — shows DDAVP may assist in combined factor deficiencies where FVIII component is involved, but does not address isolated prothrombin deficiency. |
| [1942544](https://pubmed.ncbi.nlm.nih.gov/1942544/) | 1991 | Case Report | *Japanese J Clinical Haematology* | Combined Factor V + VIII deficiency in a 25-year-old pregnant woman managed with FVIII concentrates for caesarean section. DDAVP mentioned peripherally. Disease context only — no prothrombin deficiency data. |

---

## Supporting Literature Evidence (Rank 4: Primary Release Disorder of Platelets — Most Actionable)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [36656570](https://pubmed.ncbi.nlm.nih.gov/36656570/) | 2023 | Systematic Review | *European Journal of Haematology* | Comprehensive review confirming DDAVP efficacy in mild haemophilia A, selected vWD subtypes, uraemia, liver disease, and platelet dysfunction. Identifies hyponatraemia and rare arterial thrombosis as principal safety concerns. |
| [21509710](https://pubmed.ncbi.nlm.nih.gov/21509710/) | 2011 | Prospective Clinical Study | *Klinische Pädiatrie* | **Direct prospective evidence:** DDAVP shortens bleeding time in paediatric patients with aspirin-like defect (hereditary thrombocytopathy — a primary release disorder). Demonstrates clinical haemostatic benefit beyond vWF/FVIII elevation. |
| [23051555](https://pubmed.ncbi.nlm.nih.gov/23051555/) | 2013 | Clinical Mechanistic Study | *Haemophilia* | Post-DDAVP, significantly increased vWF is bound to microparticles. Supports a mechanism whereby DDAVP enhances haemostasis in platelet disorders via microparticle-associated vWF, not solely through free plasma vWF or FVIII elevation. |
| [1613990](https://pubmed.ncbi.nlm.nih.gov/1613990/) | 1992 | Clinical Study | *Nihon Rinsho* | DDAVP shortened bleeding time in 11 of 17 patients with platelet dysfunction (including aspirin-like defects and ITP). Suggests DDAVP can bypass the granule release defect via an independent mechanism. |
| [10509036](https://pubmed.ncbi.nlm.nih.gov/10509036/) | 1999 | Clinical Mechanistic Study | *Haematologica* | In vitro and ex vivo characterisation of DDAVP–platelet interactions. Investigates direct vs. indirect platelet activation by DDAVP — relevant to understanding haemostatic mechanism in platelet release disorders. |

---

## Australia Market Information

No ARTG entries for Desmopressin were identified in the current dataset.

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|-------------|-------------|-------------|---------------------|
| — | No entries retrieved | — | — |

As noted above, this almost certainly represents a data retrieval limitation. Australian healthcare professionals should search the ARTG directly at [tga.gov.au](https://www.tga.gov.au) using the search term "Desmopressin" to retrieve current approved products, dosage forms, and indications.

---

## Safety Considerations

TGA-approved Product Information (PI) data for Desmopressin was not available in the current dataset. Please refer to the **TGA-approved Product Information (PI)** for complete warnings, contraindications, and precautions.

The following safety signals were identified through the evidence review and should be considered in any clinical decision:

**Contraindications Identified from Evidence Review:**

- **Platelet-type (pseudo-) von Willebrand disease** — DDAVP precipitates platelet consumption and worsening thrombocytopenia via hypersensitive GPIbα (PMID 27819553)
- **Thrombotic thrombocytopenic purpura (TTP)** — Documented disease worsening; DDAVP releases vWF multimers that exacerbate microvascular thrombosis (PMID 15499705, PMID 21921792)
- **Inherited thrombophilia** — Risk of promoting thrombotic events in hypercoagulable states (PMID 16460464)
- **vWD Type 2B** — DDAVP induces release of abnormal vWF that causes platelet clumping and paradoxical thrombocytopenia (PMID 12109311)

**Key Safety Considerations from Known Pharmacology:**

- **Hyponatraemia:** Most clinically significant adverse effect of DDAVP — risk increases with fluid overload, paediatric use, and repeated dosing. Serum sodium monitoring is essential.
- **Tachyphylaxis:** Repeated DDAVP dosing within 24–48 hours depletes Weibel-Palade body stores, substantially reducing haemostatic response. Spacing of doses is critical.
- **Cardiovascular risk:** Rare arterial thrombotic events reported (PMID 36656570). Use with caution in patients with established cardiovascular disease.
- **Drug interactions:** No DDI data was available in the current dataset. Clinicians should review interactions with diuretics (hyponatraemia risk), NSAIDs (fluid retention and sodium dilution), and antidepressants.

---

## Conclusion and Next Steps

### Decision for Top Prediction — Congenital Prothrombin Deficiency (Rank 1): Hold

**Rationale:**
The mechanistic link between Desmopressin (which releases vWF and FVIII) and congenital prothrombin deficiency (Factor II deficiency) is pharmacologically weak. DDAVP has no known influence on prothrombin synthesis, secretion, or activity. The single retrieved clinical trial tests a different drug for a different disease (Grade C relevance), and the four retrieved publications provide only peripheral disease-class context. The TxGNN high score (99.70%) most likely reflects general haemostasis-domain knowledge graph connectivity rather than a targeted mechanistic relationship. Proceeding to clinical evaluation of this indication is not justified on current evidence.

---

### Decision for Most Actionable Prediction — Primary Release Disorder of Platelets (Rank 4): **Proceed with Guardrails**

**Rationale:**
This is the strongest repurposing candidate across all 10 TxGNN predictions. Desmopressin's mechanism of releasing high-molecular-weight vWF multimers directly compensates for the GPIb-vWF adhesion step that is impaired when platelet granule release is defective. Prospective clinical evidence (PMID 21509710) demonstrates bleeding time shortening in paediatric hereditary thrombocytopathy, and mechanistic studies (PMID 23051555) confirm additional haemostatic pathways involving microparticle-bound vWF.

**To proceed, the following steps are needed:**

1. **Confirm ARTG registration:** Verify current TGA approval status and approved indications for available Desmopressin products in Australia — suspected data gap in this evidence pack
2. **Obtain TGA Product Information:** Complete the S1 safety screening gate (currently blocked by missing PI data on warnings and contraindications)
3. **Subtype-specific patient selection:** Define the specific platelet release disorder (delta-granule storage pool deficiency, alpha-granule deficiency, or arachidonic acid pathway defect) — DDAVP response varies by subtype
4. **DDAVP trial infusion:** Perform a pre-treatment DDAVP challenge with standardised bleeding time measurement to confirm individual haemostatic response before committing to therapeutic use
5. **Establish safety monitoring protocol:** Serum sodium (pre- and 4 hours post-dose), fluid restriction during dosing period, minimum 48-hour interval between doses to prevent tachyphylaxis
6. **Specialist consultation:** Engage a haematologist with expertise in inherited platelet disorders for case-by-case clinical decision-making

---

> **Disclaimer:** This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates identified by TxGNN require prospective clinical validation before therapeutic application. All clinical decisions should be made in consultation with relevant medical specialists. Patients and clinicians should refer to TGA-approved Product Information for regulatory-approved safety and efficacy information.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

