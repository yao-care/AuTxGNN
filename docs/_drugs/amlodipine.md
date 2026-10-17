---
layout: default
title: Amlodipine
parent: Model Prediction Only (L5)
nav_order: 46
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Amlodipine: predicted new indication Brain stem infarction . The best-supported prediction is intracerebra… (evidence level L5). Approved use: Hypertension, stroke and cerebrovascular disorders…"
monitor_inn: "Amlodipine"
predicted_indications: ["brain stem infarction", "malignant hypertensive renal disease", "MRI defined brain infarct", "ABri amyloidosis", "intracerebral hemorrhage"]
---

# Amlodipine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Amlodipine: From Hypertension to Intracerebral Haemorrhage (Secondary Prevention)

## One-Sentence Summary

Amlodipine is a calcium channel blocker originally used to treat hypertension, stroke-related disorders and Prinzmetal angina.
The TxGNN model predicts it may be effective for **intracerebral haemorrhage** (the best-supported of the top 10 predictions), with **1 completed Phase 3 trial (a triple-pill combination)** and **10 publications** currently supporting this direction.
The Phase 3 evidence tests a combination pill, so the effect cannot be attributed to amlodipine alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, stroke and cerebrovascular disorders, cerebral infarction, Prinzmetal angina (the ARTG entry carries no indication text; indications are from the knowledge graph) |
| Predicted New Indication | Brain stem infarction (rank 1 by TxGNN score, prediction only). The best-supported prediction is intracerebral haemorrhage (rank 10), which is the focus of this report |
| TxGNN Prediction Score | 99.94% for brain stem infarction; 99.79% for intracerebral haemorrhage |
| Evidence Level | L5 for brain stem infarction; L1 for intracerebral haemorrhage (combination therapy) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold for brain stem infarction; Proceed with Guardrails for intracerebral haemorrhage |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on known information, amlodipine is a dihydropyridine calcium channel blocker. It relaxes vascular smooth muscle and lowers blood pressure, and its efficacy in hypertension is established.

Blood pressure control is the main modifiable risk factor for recurrent intracerebral haemorrhage (ICH). Amlodipine is already indicated for stroke and cerebrovascular disorders, so extending its use to ICH secondary prevention is mechanistically plausible.

The TRIDENT programme tested a low-dose triple-pill strategy (typically amlodipine with an angiotensin receptor blocker and a diuretic) in people with prior ICH. Because the benefit comes from the combination, it cannot be attributed to amlodipine alone. The evidence covers secondary prevention through blood pressure lowering, not acute-phase treatment.

The top-ranked prediction, brain stem infarction, has no trials or literature. It is plausible only as an extension of the existing stroke indication.

---

## Clinical Trial Evidence

Trials for intracerebral haemorrhage (rank 10):

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Phase 3 | Completed | 1671 | TRIDENT: double-blind, placebo-controlled RCT of a low-dose triple BP-lowering pill on top of standard care to reduce recurrent stroke after ICH. The strongest direct evidence, but it tests a combination |
| [NCT07458880](https://clinicaltrials.gov/study/NCT07458880) | Not applicable | Recruiting | 140 | Triple antihypertensive therapy for BP control after ICH (TRICH score); no results yet |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | Not applicable | Terminated | 4 | TRIDENT MRI sub-study; terminated, no usable data |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Terminated | 1 | TRIDENT cognitive sub-study; terminated, no usable data |

Trials for cerebral artery occlusion (rank 6) are of low relevance:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00805311](https://clinicaltrials.gov/study/NCT00805311) | Phase 4 | Terminated | 400 | Carotid endarterectomy vs optimal medical treatment in asymptomatic stenosis; amlodipine is not the tested intervention |

No related clinical trials are registered for brain stem infarction, pulmonary hypertension, malignant renovascular hypertension, malignant hypertensive renal disease, Braddock syndrome, MRI-defined brain infarct or ABri amyloidosis. No ANZCTR identifiers were found in the data compiled for this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42019018](https://pubmed.ncbi.nlm.nih.gov/42019018/) | 2026 | RCT | N Engl J Med | Three low-dose antihypertensives in a single pill after ICH, assessed for BP reduction and recurrent stroke risk |
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | Trial protocol | Int J Stroke | TRIDENT rationale and design: single-pill combination for secondary prevention after ICH |
| [14717341](https://pubmed.ncbi.nlm.nih.gov/14717341/) | 2003 | RCT design (indirect) | Hypertens Res | CASE-J rationale and methods; candesartan-based trial in high-risk hypertension |
| [3154329](https://pubmed.ncbi.nlm.nih.gov/3154329/) | 1988 | Review | Cardiovasc Drugs Ther | Calcium antagonists in hypertension; lowering of systemic vascular resistance |
| [19299323](https://pubmed.ncbi.nlm.nih.gov/19299323/) | 2009 | Case report | Ann Pharmacother | Probable amlodipine-induced angioedema in a patient with haemorrhagic stroke |
| [21538457](https://pubmed.ncbi.nlm.nih.gov/21538457/) | 2011 | Preclinical (animal) | J Neurosci Res | Amlodipine plus atorvastatin gave additive neuroprotection after MCAO in rats |
| [17070425](https://pubmed.ncbi.nlm.nih.gov/17070425/) | 2006 | Preclinical (animal) | Am J Hypertens | Amlodipine reduced stroke size in ApoE-deficient mice (cerebral artery occlusion) |
| [11282121](https://pubmed.ncbi.nlm.nih.gov/11282121/) | 2001 | Preclinical (animal) | Eur J Pharmacol | Amlodipine attenuated pulmonary vascular remodelling in hypoxic rats; fully prevented with perindopril |
| [10759437](https://pubmed.ncbi.nlm.nih.gov/10759437/) | 2000 | Randomised crossover | Eur Respir J | Amlodipine vs placebo on pulmonary vascular responses to hypoxia in 14 mountaineers |
| [36856509](https://pubmed.ncbi.nlm.nih.gov/36856509/) | 2023 | Case report | Heart Surg Forum | Preoperative amlodipine was considered responsible for hypoxia during one-lung ventilation |

The remaining literature for the other predictions is largely indirect or tangential. Evidence for malignant renovascular hypertension is limited to two paediatric case reports (PMIDs 16467664, 15113447).

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 13532F | Norvasc | Tablet 5 mg (as besilate) | Not listed in the data compiled for this report |

Only an oral tablet is registered. The identifier shown is as recorded in the compiled data and should be checked against the ARTG.

---

## Safety Considerations

Warnings and contraindications from the Product Information were not available. Please refer to the TGA-approved Product Information (PI) for these.

**Conditions flagged in the knowledge graph** (drug-disease contraindication links, not label text):
- Hepatic and biliary: liver failure, liver disease, gallbladder disease, pancreatitis
- Renal: kidney disease, pyoureter
- Endocrine and metabolic: hypothyroidism (including myxedema and congenital forms), diabetes mellitus, diabetic ketoacidosis, hyperparathyroidism, hyperuricaemia, potassium deficiency
- Immune and haematological: angioedema (several forms, including hereditary), systemic lupus erythematosus, neutropenia, agranulocytosis
- Neuromuscular: myopathy, muscular disease, familial periodic paralysis
- Cardiovascular: hypotensive disorder

These links need clinical verification against the PI. Angioedema is consistent with a published case report of probable amlodipine-induced angioedema (PMID 19299323).

**Drug interactions:** 100 interactions were identified, and the 20 shown are all rated Moderate. They include corticosteroids (hydrocortisone, betamethasone, budesonide, dexamethasone), aspirin, aprepitant, bupropion, clarithromycin, clotrimazole, canagliflozin, dapagliflozin and multiple calcium salts.

**Additional concern for pulmonary hypertension:** vasodilators can worsen ventilation-perfusion matching in hypoxic lung disease.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (intracerebral haemorrhage secondary prevention); Hold for all other predicted indications**

**Rationale:**
- The completed Phase 3 TRIDENT trial (n=1671) and its 2026 NEJM publication support BP lowering with a triple pill after ICH, but the effect is for a combination and cannot be attributed to amlodipine alone.
- Brain stem infarction, the top-scoring prediction, is prediction only with no trials or literature, so it should be held. Cerebral artery occlusion has mostly preclinical evidence. The pulmonary hypertension predictions have only preclinical or case-level evidence and a safety concern.

**To proceed, the following is needed:**
- Review of the full TRIDENT results to determine the contribution of amlodipine and the applicability of the triple-pill formulation. The pill's availability in Australia needs confirming, since only amlodipine 5 mg tablets appear on the ARTG in the compiled data.
- Mechanism of action data and PI warnings and contraindications (flagged as blocking gaps in the compiled data)
- Verification of the knowledge-graph contraindications against the TGA-approved PI
- A BP-targeted safety monitoring plan for people with prior ICH, including hypotension and angioedema
- Confirmation of the approved indication text for the ARTG entry
- Registry search for Australian and New Zealand trials (ANZCTR)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

