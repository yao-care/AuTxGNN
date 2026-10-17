---
layout: default
title: Amiodarone
parent: Model Prediction Only (L5)
nav_order: 43
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Amiodarone: predicted new indication Catecholaminergic polymorphic ventricular tachycardia (evidence level L5). Approved use: Ventricular fibrillation (the registered indication text for the Aust…"
monitor_inn: "Amiodarone"
predicted_indications: ["catecholaminergic polymorphic ventricular tachycardia", "incessant infant ventricular tachycardia", "ventricular tachycardia", "obsolete bundle branch block", "rheumatoid arthritis", "brachydactyly-syndactyly syndrome", "heparin cofactor 2 deficiency", "trichotillomania", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "gout"]
---

# Amiodarone
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

# Amiodarone: From Ventricular Fibrillation to Ventricular Tachycardia

## One-Sentence Summary

Amiodarone is an antiarrhythmic drug originally used to treat ventricular fibrillation.
The TxGNN model's top-ranked prediction is catecholaminergic polymorphic ventricular tachycardia (CPVT), but the evidence is weak there. The best-supported prediction is **Ventricular Tachycardia** (rank 3), with **18 clinical trials** and **20 publications**, including several Phase 3 trials. This is closer to an established use than to a novel repurposing.

## Quick Overview

The table below covers the top-ranked prediction (CPVT) as the report's primary indication. The best-supported candidate (ventricular tachycardia) is discussed in the evidence sections and the conclusion.

| Item | Content |
|------|------|
| Original Indication | Ventricular fibrillation (the registered indication text for the Australian entry is not available) |
| Predicted New Indication | Catecholaminergic polymorphic ventricular tachycardia (rank 1); best-supported candidate: Ventricular tachycardia (rank 3) |
| TxGNN Prediction Score | 99.78% (CPVT); 99.64% (ventricular tachycardia) |
| Evidence Level | L4 for CPVT; L1 for ventricular tachycardia |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold for CPVT; Proceed with Guardrails for ventricular tachycardia |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for this drug is not available in the data compiled for this report. Based on known pharmacology, amiodarone is a multi-channel blocker. It acts mainly as a class III agent (K+ channel blockade, prolonging repolarisation), with additional sodium channel, calcium channel and beta-adrenergic blocking effects. These actions suppress reentrant and triggered ventricular arrhythmias.

**Ventricular tachycardia** is closely related to the original indication of ventricular fibrillation. Both are life-threatening ventricular arrhythmias, so the mechanistic link is strong. Randomised trials against procainamide and lidocaine, and large Phase 3 trials, support its use. 

**CPVT** is caused by RYR2 or CASQ2 mutations that produce catecholamine-triggered calcium leak. Amiodarone's anti-adrenergic and calcium-channel effects are plausibly relevant. However, it is not first-line therapy (beta-blockers and flecainide are the standard options), and none of the retrieved literature shows amiodarone efficacy in CPVT.

## Clinical Trial Evidence

**CPVT (rank 1):** Currently no related clinical trials registered.

**Ventricular tachycardia (rank 3), most relevant trials:**

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01401647](https://clinicaltrials.gov/study/NCT01401647) | Phase 3 | Completed | 3024 | Amiodarone, lidocaine or placebo in out-of-hospital cardiac arrest from shock-refractory VF/pulseless VT |
| [NCT00000531](https://clinicaltrials.gov/study/NCT00000531) | Phase 3 | Completed | Not reported | AVID: antiarrhythmic drugs (mainly amiodarone) vs implantable defibrillators in patients resuscitated from sudden cardiac death |
| [NCT00257959](https://clinicaltrials.gov/study/NCT00257959) | Phase 4 | Completed | 400 | OPTIC: amiodarone plus beta-blocker vs beta-blocker alone vs sotalol for preventing ICD shocks |
| [NCT00383799](https://clinicaltrials.gov/study/NCT00383799) | Phase 4 | Terminated | 302 | PROCAMIO: IV amiodarone vs IV procainamide in well-tolerated wide QRS tachycardia |
| [NCT03299517](https://clinicaltrials.gov/study/NCT03299517) | Phase 4 | Unknown | 80 | Amiodarone vs lidocaine in stable VT in the emergency room |
| [NCT02830360](https://clinicaltrials.gov/study/NCT02830360) | Phase 4 | Completed | 416 | VANISH2: catheter ablation vs antiarrhythmic drug therapy after myocardial infarction |
| [NCT01722942](https://clinicaltrials.gov/study/NCT01722942) | Not applicable | Unknown | 1100 | CHAGASICS: amiodarone vs ICD for primary prevention in Chagas cardiomyopathy |
| [NCT01097330](https://clinicaltrials.gov/study/NCT01097330) | Phase 3 | Terminated | 12 | Catheter ablation vs amiodarone for shock prophylaxis in ICD patients; stopped early with very few participants |
| [NCT03855826](https://clinicaltrials.gov/study/NCT03855826) | Phase 4 | Unknown | 756 | Nifekalant injection vs amiodarone in VT/VF (indirect) |
| [NCT03734562](https://clinicaltrials.gov/study/NCT03734562) | Not applicable | Completed | 180 | Substrate ablation vs antiarrhythmic drugs in ischaemic VT |

No ANZCTR identifiers are available in the data compiled for this report.

## Literature Evidence

**CPVT (rank 1):** No literature shows amiodarone efficacy. The retrieved papers are a systematic review, cohort studies and case reports on CPVT in general.

**Ventricular tachycardia (rank 3), most relevant publications:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27354046](https://pubmed.ncbi.nlm.nih.gov/27354046/) | 2017 | RCT | Eur Heart J | PROCAMIO: randomised comparison of IV procainamide vs amiodarone for tolerated wide QRS tachycardia |
| [30084131](https://pubmed.ncbi.nlm.nih.gov/30084131/) | 2018 | Cohort | Emerg Med Australas | Safety and efficacy of paramedic-administered amiodarone for stable VT in the prehospital setting |
| [20730062](https://pubmed.ncbi.nlm.nih.gov/20730062/) | 2010 | Review | Vasc Health Risk Manag | Amiodarone is a leading therapy for termination and prevention of VF and VT |
| [36878200](https://pubmed.ncbi.nlm.nih.gov/36878200/) | 2023 | Review | Cardiology | Pharmacotherapy in ventricular arrhythmias |
| [28900864](https://pubmed.ncbi.nlm.nih.gov/28900864/) | 2017 | Review | Curr Cardiol Rep | When to medicate and when to ablate in VT with ICD shocks |
| [41217320](https://pubmed.ncbi.nlm.nih.gov/41217320/) | 2026 | Substudy of RCT | J Am Coll Cardiol | VANISH2 substudy: catheter ablation vs sotalol or amiodarone |
| [37380314](https://pubmed.ncbi.nlm.nih.gov/37380314/) | 2023 | Trial analysis | JACC Clin Electrophysiol | VT and ICD therapy burden with ablation vs escalated antiarrhythmic drugs |
| [9137212](https://pubmed.ncbi.nlm.nih.gov/9137212/) | 1997 | Review | J Am Coll Cardiol | Intravenous amiodarone for malignant and resistant ventricular arrhythmia |
| [8258259](https://pubmed.ncbi.nlm.nih.gov/8258259/) | 1993 | Case report | Clin Pharm | Amiodarone-induced thyroid dysfunction |

**Other predictions of note:**
- **Incessant infant ventricular tachycardia (rank 2, L2):** a randomised, double-blind trial of IV amiodarone for incessant tachyarrhythmias in children ([16316969](https://pubmed.ncbi.nlm.nih.gov/16316969/), Circulation, 2005) and an infant cohort ([14508682](https://pubmed.ncbi.nlm.nih.gov/14508682/), 2003). These populations mix supraventricular and ventricular tachycardia, so VT-specific effect is uncertain.
- **Ranks 4 to 10** (obsolete bundle branch block, rheumatoid arthritis, brachydactyly-syndactyly syndrome, heparin cofactor 2 deficiency, trichotillomania, colobomatous microphthalmia-rhizomelic dysplasia syndrome, gout): no trials, and no literature showing therapeutic benefit. These predictions have no biological rationale and appear to be knowledge-graph artefacts.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2343H | Amdarone | Tablet containing amiodarone hydrochloride 200 mg | Not available |

## Cytotoxicity

Not applicable: amiodarone is not an antineoplastic drug.

## Safety Considerations

Detailed label warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for full safety information.

**Contraindicated or high-risk conditions (from the knowledge graph, not label text):**
- Cardiac conduction and rhythm: long QT syndrome (including familial), torsades de pointes, atrioventricular block, sick sinus syndrome
- Thyroid: hypothyroidism, myxedema, congenital hypothyroidism, hyperthyroidism, Graves disease, thyrotoxicosis
- Lung: interstitial lung disease, eosinophilic pneumonia, pulmonary eosinophilia, hypersensitivity pneumonitis (extrinsic allergic alveolitis, farmer's lung)
- Liver: liver disease, drug-induced liver injury, gallbladder disease
- Eye and nerve: optic neuritis, optic nerve disease, corneal deposit, peripheral neuropathy
- Metabolic: potassium deficiency disease

**Drug interactions:** The query returned 100 interactions. Examples classed as Major include:
- Cisapride, clarithromycin, dolasetron and eliglustat (QT-prolongation or metabolic concerns)
- Amphotericin B (including liposomal, lipid complex and cholesteryl sulfate forms)
- Hydrocortisone and dexamethasone
- Clotrimazole and agalsidase beta

Moderate examples include famotidine, cimetidine, aprepitant, bisacodyl and budesonide. Fidaxomicin is Minor. The literature also reports a cyclosporine interaction. These interactions need review before any new use.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (ventricular tachycardia); Hold (CPVT and all other predictions)**

**Rationale:**
- Ventricular tachycardia is supported by multiple Phase 3 and 4 randomised trials, including large completed studies, and sits very close to the original indication. It is an established use rather than a new one.
- CPVT, the top-scoring prediction, has no trials and no evidence of amiodarone benefit, and better first-line options exist. The remaining high-scoring predictions have no supporting rationale.

**To proceed, the following is needed:**
- Mechanism of action data (currently unavailable)
- The approved indication text and Product Information for the Australian ARTG entry (currently missing), to confirm the registered scope against ventricular tachycardia
- A monitoring plan for thyroid, pulmonary, hepatic and QT toxicity, and a systematic review of major drug interactions
- For infant ventricular tachycardia: VT-specific paediatric efficacy and safety data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

