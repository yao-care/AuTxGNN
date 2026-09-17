---
layout: default
title: Sotalol
parent: High Evidence (L1-L2)
nav_order: 641
evidence_level: L2
indication_count: 10
---

# Sotalol
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

# Sotalol: From Cardiac Arrhythmias to Stroke Disorder (Atrial Fibrillation-Related)

## One-Sentence Summary

Sotalol is a Class III antiarrhythmic with additional non-selective β-blocking activity, established for managing atrial and ventricular arrhythmias (notably atrial fibrillation). The TxGNN model's highest-ranked candidate for this drug (sick sinus syndrome) is flagged internally as a **reverse-mechanism, likely contraindicated** prediction with no supporting evidence, so this report instead evaluates the highest-evidence candidate in the pack — **Stroke Disorder** — which is backed by **22 clinical trials** and **20 publications**, most relating to sotalol's established role in atrial fibrillation (AF) rhythm control.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cardiac arrhythmias (Class III antiarrhythmic; structured indication text not available in this pack — see MOA note below) |
| Predicted New Indication | Stroke Disorder (evidence base is predominantly atrial-fibrillation-related) |
| TxGNN Prediction Score | 99.44% (rank 6455 of candidate pool) |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

**A caution on TxGNN ranking first:** the single highest-scoring candidate for sotalol in this pack (sick sinus syndrome, 99.76%) is explicitly annotated as pharmacologically *opposite* to sotalol's known effect — sotalol's β-blockade and Class III action suppress sinoatrial node automaticity, and sick sinus syndrome is a relative/absolute contraindication for sotalol. This is a useful reminder that a high TxGNN score alone does not indicate a viable repurposing candidate. "Stroke Disorder" (rank 4, 99.44%) is chosen as the focus of this report because it is the only candidate in the pack with substantive clinical trial and literature support.

Detailed mechanism-of-action data is not available in this evidence pack (Data Gap DG002). Based on well-established pharmacology, Sotalol is a Class III antiarrhythmic agent (potassium-channel blockade prolonging repolarization) combined with non-selective β-blocking activity. Its efficacy in maintaining sinus rhythm in atrial fibrillation is well documented — most directly in the VA Cooperative Study CSP #399 (SAFE-T trial, NCT00007605), a completed Phase 3 RCT comparing sotalol, amiodarone, and placebo for sinus rhythm maintenance in AF.

Atrial fibrillation is a leading cause of ischaemic stroke through atrial thrombus formation and embolisation. Sotalol's rhythm-control effect in AF is the plausible mechanistic bridge to the "stroke disorder" prediction — i.e., reducing AF burden may indirectly lower thromboembolic stroke risk — rather than any direct neuroprotective or antithrombotic action. Reviewers should note that the disease label "stroke disorder" may reflect an ontology-mapping artefact in the knowledge graph, and the underlying evidence base is really about **atrial fibrillation management**, not stroke treatment per se; this should be clarified before further progression.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00007605](https://clinicaltrials.gov/study/NCT00007605) | Phase 3 | Completed | 706 | CSP #399 (SAFE-T): sotalol, amiodarone, and placebo compared for maintaining sinus rhythm in AF — the most direct high-quality sotalol evidence in this pack |
| [NCT05279833](https://clinicaltrials.gov/study/NCT05279833) | N/A (SLR/NMA) | Completed | 87,810 | Systematic literature review/network meta-analysis comparing safety of dronedarone vs sotalol in AF patients |
| [NCT02145546](https://clinicaltrials.gov/study/NCT02145546) | Phase 4 | Unknown | 600 | Compares amiodarone, sotalol, and propafenone for long-term AF management, including in sick sinus syndrome patients |
| [NCT07405671](https://clinicaltrials.gov/study/NCT07405671) | Phase 4 | Not yet recruiting | 988 | Tests whether flecainide is as safe as standard rhythm-control drugs (sotalol or amiodarone) in AF with stable coronary artery disease |
| [NCT00523978](https://clinicaltrials.gov/study/NCT00523978) | Phase 3 | Completed | 245 | STOP AF: cryoablation vs AF drugs (flecainide, propafenone, or sotalol) in paroxysmal AF after drug failure |
| [NCT00911508](https://clinicaltrials.gov/study/NCT00911508) | N/A | Completed | 2,204 | CABANA: catheter ablation vs anti-arrhythmic drug therapy (sotalol among options) for AF |
| [NCT01856075](https://clinicaltrials.gov/study/NCT01856075) | N/A | Completed | 1,015 | Real-world observational study of dronedarone vs other anti-arrhythmics (incl. sotalol) in AF |
| [NCT02459574](https://clinicaltrials.gov/study/NCT02459574) | N/A | Completed | 321 | Ablation vs anti-arrhythmic drug therapy for reducing AF-related hospitalisation |
| [NCT02294955](https://clinicaltrials.gov/study/NCT02294955) | N/A | Unknown | 152 | Catheter ablation vs optimised pharmacological therapy in symptomatic AF |
| [NCT06096337](https://clinicaltrials.gov/study/NCT06096337) | N/A | Active, not recruiting | 484 | Pulsed field ablation vs anti-arrhythmic drug therapy as first-line treatment for persistent AF |

No ANZCTR (Australian and New Zealand) trial identifiers were found for sotalol in this evidence pull.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29954667](https://pubmed.ncbi.nlm.nih.gov/29954667/) | 2019 | Cohort | International Journal of Cardiology | Efficacy and safety of sotalol in adults with congenital heart disease |
| [37485722](https://pubmed.ncbi.nlm.nih.gov/37485722/) | 2023 | Cohort | Circulation: Arrhythmia and Electrophysiology | Retrospective comparison of dronedarone vs sotalol effectiveness/safety in anti-arrhythmic-drug-naive veterans with AF |
| [1281807](https://pubmed.ncbi.nlm.nih.gov/1281807/) | 1992 | Cohort | International Journal of Cardiology | Sotalol's efficacy and safety in complex ventricular arrhythmias (626 patients) |
| [8346725](https://pubmed.ncbi.nlm.nih.gov/8346725/) | 1993 | Cohort | American Journal of Cardiology | Effect of oral sotalol on systemic haemodynamics and programmed electrical stimulation in structural heart disease |
| [7509121](https://pubmed.ncbi.nlm.nih.gov/7509121/) | 1994 | Cohort | American Journal of Cardiology | Response to sotalol predicts response to amiodarone in sustained ventricular tachycardia with CAD |
| [28496906](https://pubmed.ncbi.nlm.nih.gov/28496906/) | 2013 | Cohort | Journal of Atrial Fibrillation | Real-world risk of CV events, stroke, CHF, and other outcomes: dronedarone vs amiodarone and other anti-arrhythmics (incl. sotalol) |
| [25428811](https://pubmed.ncbi.nlm.nih.gov/25428811/) | 2015 | Health Economics | Kardiologia Polska | Cost-effectiveness of dronedarone vs amiodarone, propafenone, and sotalol in AF |
| [37777295](https://pubmed.ncbi.nlm.nih.gov/37777295/) | 2023 | Guideline Review | American Journal of Cardiology | ACC/AHA/HRS and ESC guideline recommendations for anti-arrhythmic drug selection in AF |
| [38011245](https://pubmed.ncbi.nlm.nih.gov/38011245/) | 2023 | Review | Circulation | Contemporary management of AF in hypertrophic cardiomyopathy, incl. stroke risk stratification |
| [39077579](https://pubmed.ncbi.nlm.nih.gov/39077579/) | 2023 | Review | Reviews in Cardiovascular Medicine | Managing AF during pregnancy, including anti-arrhythmic and anticoagulant risk-benefit |

---

## Australia Market Information

No ARTG entries were found for Sotalol in the current data pull — the drug is recorded as **not marketed** in Australia (0 licences).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for formal safety information — the structured safety dataset for this candidate (key warnings, contraindications, DDI) returned no data (Data Gap DG001, flagged as **Blocking** for progression to safety pre-screening).

**Signals surfaced during the repurposing screen** (from mechanistic analysis, not structured PI data, but relevant for pharmacist awareness):
- Sotalol is mechanistically contraindicated in sick sinus syndrome — its β-blocking and Class III effects can provoke significant bradycardia or sinus arrest. This was the model's *highest-scoring* candidate for sotalol, illustrating that score alone should not guide clinical judgement.
- QT-prolongation interaction risk: literature identified in this pack notes that β-blockade can augment the torsadogenic potential of QT-prolonging antipsychotics (e.g. risperidone) when co-administered with sotalol, relevant to any consideration of psychiatric comorbidity populations.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A completed Phase 3 RCT (SAFE-T) and supporting cohort literature give genuine L2-level evidence for sotalol's role in AF rhythm control, which plausibly underlies the "stroke disorder" prediction — but the disease-ontology mapping needs verification, TGA Product Information data required for a basic safety pre-screen (S1) is currently missing (Blocking gap), and the drug has no current ARTG registration in Australia.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications, DDI) to clear the Blocking safety data gap (DG001)
- Confirmation of DrugBank mechanism-of-action data (DG002)
- Clarification of whether the TxGNN "stroke disorder" node should instead be mapped to "atrial fibrillation" given the evidence composition
- Confirmation of an Australian import/registration pathway if this candidate is pursued further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

