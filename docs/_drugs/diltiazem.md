---
layout: default
title: Diltiazem
parent: Moderate Evidence (L3-L4)
nav_order: 217
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Diltiazem: predicted new indication Cerebrovascular disorder (evidence level L4). Approved use: Hypertension, atrial fibrillation, Prinzmetal angina…"
---

# Diltiazem
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Diltiazem: From Hypertension and Arrhythmia to Cerebrovascular Disorder

## One-Sentence Summary

Diltiazem is a calcium channel blocker originally used for hypertension, atrial fibrillation, Prinzmetal angina and ventricular tachycardia.
The TxGNN model predicts it may be effective for **Cerebrovascular Disorder** (the highest-ranked prediction with any supporting data), but only **1 indirect clinical trial** and **20 largely non-specific publications** are available, so the evidence is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, atrial fibrillation, Prinzmetal angina, ventricular tachycardia (from the knowledge graph; no approved indication text is available for the Australian product) |
| Predicted New Indication | Cerebrovascular disorder (see note below) |
| TxGNN Prediction Score | 97.63% |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

**Note on candidate selection:** The top-ranked predictions are "obsolete susceptibility to ischemic stroke" (99.08%), "brain stem infarction" (98.23%) and "obsolete bundle branch block" (97.88%). None has any trial or literature support, and two use obsolete disease terms. Cerebrovascular disorder is the highest-ranked prediction with any supporting data, so it is the focus of this report. The other predictions, all with a TxGNN score of at least 96.7%, are summarised in the conclusion.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not currently available. Based on known information, diltiazem is a calcium channel blocker. It blocks L-type calcium channels in vascular smooth muscle and cardiac tissue, causing vasodilation, blood pressure reduction and slowed atrioventricular nodal conduction. Its efficacy in hypertension and rate control in atrial fibrillation is established, and mechanistically it may be applicable to cerebrovascular disease.

The link to cerebrovascular disease is plausible in two ways. First, blood pressure control is central to stroke prevention and post-stroke care. Second, atrial fibrillation, one of diltiazem's existing uses, is a major cause of stroke. Preclinical work also suggests calcium influx contributes to neuronal injury after ischaemia (PMID 7902749), and early animal studies tested diltiazem in acute stroke (PMID 4056906).

However, no data compiled for this report show that diltiazem itself improves cerebrovascular outcomes in people. The prediction is best viewed as a hypothesis, not a supported new use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03529149](https://clinicaltrials.gov/study/NCT03529149) | Phase 4 | Unknown | 90 | Transcranial Doppler (TCD)-guided blood pressure control after endovascular thrombectomy. Diltiazem is not confirmed as the studied intervention, so this is indirect evidence at best (relevance grade C). |

No ANZCTR trial identifiers were available.

---

## Literature Evidence

The 20 publications retrieved are mostly general reviews on atrial fibrillation, drug interactions and calcium channel blockers. None provides direct evidence for cerebrovascular disease. The most relevant are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4056906](https://pubmed.ncbi.nlm.nih.gov/4056906/) | 1985 | Preclinical (cats) | J Neurosurg | Verapamil and diltiazem infusions tested in acute middle cerebral artery occlusion. |
| [17309423](https://pubmed.ncbi.nlm.nih.gov/17309423/) | 2007 | Review | Med J Aust | Atrial fibrillation management. Beta-blockers, verapamil and diltiazem control heart rate better than digoxin during exercise. |
| [11975840](https://pubmed.ncbi.nlm.nih.gov/11975840/) | 2002 | Review | Heart Dis | Atrial fibrillation is associated with a higher incidence of stroke and mortality. |
| [41730211](https://pubmed.ncbi.nlm.nih.gov/41730211/) | 2026 | Cohort | Ann Intern Med | Bleeding risk in atrial fibrillation with apixaban or rivaroxaban plus diltiazem, compared with metoprolol. |
| [41152878](https://pubmed.ncbi.nlm.nih.gov/41152878/) | 2025 | Cohort | BMC Med | Stroke and bleeding with DOACs plus interacting antiarrhythmic drugs in non-valvular atrial fibrillation. |
| [35861836](https://pubmed.ncbi.nlm.nih.gov/35861836/) | 2022 | Observational | J Am Heart Assoc | Diltiazem, a moderate CYP3A4/P-glycoprotein inhibitor, may raise DOAC bleeding risk. |
| [36149579](https://pubmed.ncbi.nlm.nih.gov/36149579/) | 2023 | Observational | J Interv Card Electrophysiol | Major bleeding risk after co-prescription of diltiazem and DOACs in atrial fibrillation. |
| [40326046](https://pubmed.ncbi.nlm.nih.gov/40326046/) | 2026 | Meta-analysis | Ann Pharmacother | Diltiazem or verapamil with DOACs. Earlier real-world findings were contradictory. |
| [40670662](https://pubmed.ncbi.nlm.nih.gov/40670662/) | 2025 | Systematic review | Eur J Clin Pharmacol | Observational studies of DOACs combined with antiarrhythmic drugs. |
| [11002856](https://pubmed.ncbi.nlm.nih.gov/11002856/) | 2000 | Review | Drugs | Calcium antagonists lower blood pressure effectively. Morbidity and mortality trials are needed. |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1312C | Cardizem CD | Controlled-delivery capsule containing diltiazem hydrochloride 180 mg (oral) | Not available in the data compiled for this report |

---

## Safety Considerations

**Contraindication signals from the knowledge graph (not label text):** these come from drug-disease contraindication links in the TxGNN knowledge graph and should be verified against the Product Information. They include:
- **Cardiac conduction and rhythm:** atrioventricular block, sick sinus syndrome, Wolff-Parkinson-White syndrome, Lown-Ganong-Levine syndrome, ventricular tachycardia
- **Haemodynamic and structural:** hypotensive disorder, aortic stenosis, hypertrophic cardiomyopathy, renal artery obstruction
- **Organ disease:** kidney disease, liver disease, gallbladder disease
- **Haematological:** neutropenia, agranulocytosis
- **Angioedema** (several forms)

Several of these (atrioventricular block, sick sinus syndrome, hypotension) are especially relevant if diltiazem were used in stroke patients, who often have labile blood pressure and arrhythmias.

**Drug interactions:** 100 interactions were identified. Those listed in the data include:
- **Major:** loperamide
- **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), pioglitazone, bupropion, aprepitant, morphine, aspirin, canagliflozin, and calcium salts

The literature also highlights that diltiazem inhibits CYP3A4 and P-glycoprotein, which may raise DOAC levels and bleeding risk. Statin interactions (e.g. simvastatin) have also been reported. This matters because patients with cerebrovascular disease commonly take anticoagulants and statins.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications, as these were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score and a plausible vasodilatory mechanism. There is no direct clinical evidence, only one indirect Phase 4 trial and literature that is mostly about other topics. Safety is also a concern in this population, given the conduction-related contraindication signals and bleeding-related interactions with anticoagulants.

**Other predictions reviewed (all Hold, no supporting evidence):**
- Obsolete susceptibility to ischemic stroke, brain stem infarction, pulmonary hypertension (unclear multifactorial mechanism), malignant hypertensive renal disease and malignant renovascular hypertension: plausible only through vasodilation or blood pressure lowering, with no supporting trials.
- Obsolete bundle branch block: mechanistically questionable and carries a safety concern, since diltiazem slows AV conduction.
- Pulmonary hypertension owing to lung disease and/or hypoxia: only preclinical evidence, and calcium channel blockers are generally not recommended because they can worsen gas exchange.
- ABri amyloidosis and Braddock syndrome: no plausible mechanism, likely network artefacts.

**To proceed, the following is needed:**
- Product Information warnings and contraindications for the Australian product, and the approved indication text for ARTG 1312C
- Mechanism of action data (for example from DrugBank)
- A targeted literature review for diltiazem in secondary stroke prevention or post-stroke blood pressure management
- Confirmation of whether diltiazem is an intervention in NCT03529149
- A safety plan covering conduction disorders, hypotension, and interactions with anticoagulants and statins
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

