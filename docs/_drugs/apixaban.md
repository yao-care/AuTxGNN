---
layout: default
title: Apixaban
parent: 僅模型預測 (L5)
nav_order: 51
evidence_level: L5
indication_count: 10
---

# Apixaban
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

# Apixaban: From Venous Thromboembolism to Migraine Disorder

> **Disclaimer:** This report is intended for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before clinical application. All clinical decisions should reference TGA-approved Product Information and current clinical guidelines.

---

## One-Sentence Summary

Apixaban (Eliquis®) is a direct oral Factor Xa inhibitor established for preventing and treating venous thromboembolism (DVT/PE) and stroke in non-valvular atrial fibrillation.
The TxGNN model predicts it may have activity in **Migraine Disorder**, supported by **1 Phase 3 clinical trial** providing indirect evidence and **4 publications** spanning case reports to a prospective pilot trial.
Critically, the existing literature presents a mixed safety picture — while anticoagulation broadly may benefit certain migraine subtypes, case evidence specifically suggests apixaban may *worsen* migraine in some patients, distinguishing it from warfarin.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Venous thromboembolism prevention and treatment; stroke prevention in non-valvular atrial fibrillation *(inferred from drug class — no ARTG entries identified in dataset; see note below)* |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.02% |
| Evidence Level | L3 |
| Australia Market Status | Not Marketed *(per dataset — verification against ARTG strongly recommended)* |
| Number of ARTG Entries | 0 *(per dataset — verification against ARTG strongly recommended)* |
| Recommended Decision | Proceed with Guardrails |

> ⚠️ **Data Verification Required:** The dataset records Apixaban as unregistered in Australia with zero ARTG entries. Apixaban is internationally marketed as Eliquis® (Bristol-Myers Squibb/Pfizer). Australian clinicians should verify current registration status directly via the [TGA ARTG Search](https://www.tga.gov.au/resources/resource/artg). This discrepancy likely reflects a dataset limitation and does not reflect the actual TGA registration position.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this dataset. Based on established pharmacology, Apixaban is a highly selective, direct inhibitor of activated Factor Xa (FXa) — the key prothrombinase enzyme that converts prothrombin to thrombin in the coagulation cascade. By inhibiting FXa, Apixaban reduces thrombin generation, fibrin clot formation, and platelet aggregation. This mechanism is well validated in the prevention and treatment of thromboembolic disease.

The proposed link to migraine disorder centres on FXa's role beyond haemostasis. FXa can activate protease-activated receptors PAR-1 and PAR-2 on platelets and neuroinflammatory cells, which may contribute to cortical spreading depression (CSD) — the neurophysiological event underlying migraine aura. In specific migraine subtypes, particularly those associated with patent foramen ovale (PFO) or antiphospholipid antibody syndrome (APS), paradoxical microembolism may trigger or perpetuate migraine attacks. In this mechanistic context, reducing thrombin generation through FXa inhibition could theoretically decrease the frequency of embolic migraine triggers.

However, the evidence presents a significant and clinically important complication: case reports document that warfarin — a vitamin K antagonist (VKA) with broad pleiotropic coagulation effects — effectively suppressed migraine with aura in patients, whereas switching to apixaban resulted in migraine recurrence within weeks, resolving again upon warfarin resumption. This suggests the anti-migraine mechanism may involve Factor Xa-independent pathways uniquely conferred by VKAs — such as Protein C/S modulation, PAR-4 effects, or other pleiotropic actions — that are absent with selective FXa inhibition. This class-specific difference is a key uncertainty that must be resolved before apixaban repurposing in migraine can be responsibly advanced.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | CLOSE-type trial comparing PFO transcatheter closure, oral anticoagulation, and antiplatelet therapy for secondary stroke prevention. The primary endpoint is stroke recurrence; migraine is a secondary/exploratory endpoint. Provides indirect evidence of anticoagulant effects in PFO patients — a population with substantially elevated migraine comorbidity — but does not directly test apixaban for migraine treatment. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33402037](https://pubmed.ncbi.nlm.nih.gov/33402037/) | 2021 | Prospective Pilot Trial | *Lupus* | Retrospective study of 75 patients with refractory migraine and antiphospholipid antibodies: antithrombotic therapy (anticoagulants and/or antiplatelet agents) produced clinically meaningful symptomatic improvement in migraine frequency. Supports APS-related migraine as a potentially responsive subtype — the strongest evidence of biological plausibility in this dataset. |
| [37582651](https://pubmed.ncbi.nlm.nih.gov/37582651/) | 2023 | Case Report + Literature Review | *The Neurologist* | Migraine with aura **worsened** after initiating apixaban; accompanying literature review concludes the impact of DOACs on migraine is unclear and contradictory. Represents a key safety signal specific to apixaban. |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Case Report | *Headache* | 55-year-old female with 12-year complete remission of migraine with aura while on warfarin; symptoms returned within 3 weeks of switching to apixaban; resolved again within days of warfarin resumption. Strongly suggests a class-specific effect (VKA superior to FXa inhibitor) rather than a general anticoagulant effect. |
| [29611190](https://pubmed.ncbi.nlm.nih.gov/29611190/) | 2018 | Case Report | *Headache* | Vestibular migraine resolved with warfarin combined with topiramate — further supports a role for VKA-class anticoagulation in vestibular/brainstem migraine subtypes, though not specific to apixaban. |

---

## Australia Market Information

No ARTG entries for Apixaban were identified in this dataset. As noted in the Quick Overview, this is inconsistent with the drug's known international market status and should be verified against the TGA ARTG database before any regulatory or formulary decisions are made.

> Healthcare professionals can search the ARTG at: [https://www.tga.gov.au/resources/resource/artg](https://www.tga.gov.au/resources/resource/artg)

---

## Safety Considerations

No safety data (key warnings, contraindications, or drug-drug interactions) were available in this dataset.

Please refer to the TGA-approved Product Information (PI) for Apixaban for complete safety information, which is expected to cover:

- **Bleeding risk:** Major bleeding, clinically relevant non-major bleeding, and fatal haemorrhage
- **Contraindications:** Active clinically significant bleeding; severe hepatic impairment; concomitant use with other anticoagulants in most circumstances
- **Drug interactions:** Strong dual inhibitors/inducers of CYP3A4 and P-glycoprotein (e.g., ketoconazole, rifampicin, carbamazepine)
- **Renal dose adjustment:** Required in specific populations (refer to current PI)

**Specific to this repurposing context:** Case report evidence raises an additional safety signal — Apixaban may **worsen migraine frequency or severity** in some patients. Any prospective study design must include prospective headache diary monitoring and a pre-specified stopping rule for migraine worsening.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A biologically plausible mechanistic framework exists for anticoagulation in PFO-related and APS-related migraine subtypes, and preliminary pilot data in APS-positive refractory migraine supports proof-of-concept. However, apixaban-specific case evidence directly challenges whether FXa inhibition — as distinct from broader VKA-class anticoagulation — can deliver a migraine benefit; in some patients it appears to do the opposite. Advancement is warranted only within a tightly defined research framework targeting the most biologically credible subpopulations.

**To proceed, the following is needed:**

- **Subtype stratification:** Define the target population precisely — restrict to PFO-confirmed or APS-confirmed migraine patients rather than general migraine; avoid enrolment of patients with episodic migraine without a clear thrombotic/embolic mechanism
- **Comparative mechanistic analysis:** Commission pre-clinical or translational work to clarify whether VKA-specific pleiotropic effects (Protein C/S, PAR-4, or Factor IIa activity) are responsible for the anti-migraine effect seen with warfarin but not apixaban — this is the critical scientific question before investing in a Phase 2 RCT
- **Prospective Phase 2 RCT design:** If mechanistic work supports FXa inhibition, design a controlled, crossover or parallel-arm Phase 2 RCT (apixaban vs. warfarin vs. placebo) in a biologically stratified migraine population, with headache frequency as the primary endpoint and bleeding as the primary safety endpoint
- **ARTG verification:** Confirm current TGA registration and approved indications for apixaban in Australia via the ARTG database before any regulatory submission or off-label use discussion
- **Safety monitoring plan:** Mandate prospective headache diary completion in all enrolled patients; include pre-specified criteria for study withdrawal if migraine worsens by ≥50% from baseline
- **MOA data acquisition:** Obtain complete mechanism of action documentation from DrugBank API to support a mechanistic dossier for any future regulatory or ethics submission

> **Note for clinical prioritisation:** Among all 10 predicted indications in this Evidence Pack, **pulmonary hypertension** (rank 8; particularly CTEPH/Group 4 and systemic sclerosis-related PAH/Group 1) carries stronger overall evidence (L3, Stage S2), with a dedicated RCT protocol (SPHInX study, PMID 27932335) already published and a well-defined mechanistic rationale. This indication may represent a higher-priority and more feasible near-term repurposing target than migraine disorder.

---

*Report generated: 5 April 2026 | Evidence cutoff: 5 April 2026 | Candidate ID: TW-DB06605-multi v4*
*This report is for research purposes only and does not constitute medical advice or a recommendation for clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

