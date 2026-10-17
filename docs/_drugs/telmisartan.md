---
layout: default
title: Telmisartan
parent: Model Prediction Only (L5)
nav_order: 703
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Telmisartan: predicted new indication Intracerebral haemorrhage (evidence level L5). Approved use: Hypertension, stroke and cerebrovascular disorders…"
monitor_inn: "Telmisartan"
predicted_indications: ["Prinzmetal angina", "brain stem infarction", "ABri amyloidosis", "malignant hypertensive renal disease", "intracerebral hemorrhage"]
---

# Telmisartan
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

# Telmisartan: From Hypertension and Stroke Prevention to Intracerebral Haemorrhage

## One-Sentence Summary

Telmisartan is an angiotensin receptor blocker, originally used to treat hypertension and to reduce the risk of stroke and cerebrovascular disease.
The data compiled for this report cover 10 predicted new indications. The best-supported is **Intracerebral Haemorrhage** (secondary prevention), with **3 clinical trials** and **11 publications**, though the key trial tests a triple-pill combination and the effect cannot be attributed to telmisartan alone.
The top-ranked prediction by TxGNN score, **Prinzmetal angina**, has no supporting trials or literature.

> **Note on indication selection:** The top-ranked prediction (Prinzmetal angina) is model-only (L5, Hold). This report therefore centres on the best-evidenced candidate, intracerebral haemorrhage, and summarises the others in a short table.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, stroke and cerebrovascular disorders, cerebral infarction (from the knowledge graph; no approved indication text is available for the Australian entry) |
| Predicted New Indication | Intracerebral haemorrhage (best-evidenced); top-scored prediction is Prinzmetal angina |
| TxGNN Prediction Score | 99.93% (intracerebral haemorrhage); 99.98% (Prinzmetal angina) |
| Evidence Level | L2 (intracerebral haemorrhage) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails (intracerebral haemorrhage); Hold for the other predictions without evidence |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Telmisartan is known as an angiotensin II type 1 (AT1) receptor blocker, and preclinical papers also describe partial PPAR-gamma agonist activity. These are the mechanisms discussed in the retrieved literature.

Blood pressure lowering is the main proven way to prevent recurrent stroke. Telmisartan is already used for hypertension and stroke-related conditions, so extending it to prevent recurrent intracerebral haemorrhage is a logical step. The TRIDENT trial tested a single-pill combination of three low-dose antihypertensives, which includes telmisartan, in patients with previous intracerebral haemorrhage. Animal studies also report anti-inflammatory and antioxidant effects in intracerebral and subarachnoid haemorrhage models.

An important caveat is that TRIDENT used a combination pill. Any benefit seen cannot be assigned to telmisartan on its own.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Phase 3 | Completed | 1671 | TRIDENT: double-blind, placebo-controlled trial of a low-dose triple-pill BP-lowering strategy on top of standard care to prevent recurrent stroke after intracerebral haemorrhage. Telmisartan is one component. |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | NA | Terminated | 4 | TRIDENT MRI sub-study. Too small to give usable evidence. |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Terminated | 1 | TRIDENT cognitive sub-study (memory decline). No analysable data. |

For cerebral artery occlusion, NCT01075698 (Phase 4, completed, 1228 participants) examined telmisartan versus ordinary therapy in high-risk hypertensive patients for cardiovascular prevention. It is only indirectly relevant.

No Australian New Zealand Clinical Trials Registry (ANZCTR) identifiers were included in the data compiled for this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42019018](https://pubmed.ncbi.nlm.nih.gov/42019018/) | 2026 | RCT | N Engl J Med | TRIDENT main publication: three low-dose antihypertensives in a single pill after intracerebral haemorrhage. Only the background statement was available in the compiled data, so results should be read directly. |
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | Trial protocol | Int J Stroke | TRIDENT rationale and design: single-pill combination for secondary prevention in high-risk patients. |
| [24636673](https://pubmed.ncbi.nlm.nih.gov/24636673/) | 2014 | Post-hoc RCT analysis | Int J Stroke | PRoFESS: ischaemic and haemorrhagic stroke recurrence rates across race-ethnic groups. |
| [17538008](https://pubmed.ncbi.nlm.nih.gov/17538008/) | 2007 | Preclinical | J Pharmacol Exp Ther | Telmisartan reduced apoptosis, inflammation and oxidative stress in rats with intracerebral haemorrhage. |
| [27078703](https://pubmed.ncbi.nlm.nih.gov/27078703/) | 2016 | Preclinical | Neurol Res | Telmisartan reduced oxidative stress and vasospasm after subarachnoid haemorrhage in animals. |
| [15834293](https://pubmed.ncbi.nlm.nih.gov/15834293/) | 2005 | Preclinical | J Hypertens | Telmisartan versus ramipril on cerebrovascular structure in hypertensive rats. |
| [22957022](https://pubmed.ncbi.nlm.nih.gov/22957022/) | 2012 | Preclinical | PLoS One | Short-term candesartan versus telmisartan effects on pial arteriole diameter in hypertensive rats. |

Several other retrieved papers were case reports or not specific to telmisartan and are not listed.

For cerebral artery occlusion (L3), the literature is preclinical only, mainly rodent stroke models showing reduced infarct volume, oxidative stress and inflammation, with synergy reported alongside nimodipine.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13437F | Micardis | Tablet 40 mg (oral) | Not available in the compiled data |

---

## Other Predicted Indications

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Comment |
|---|---|---|---|---|
| 1 | Prinzmetal angina | 99.98% | L5 | Prediction only; no trials or literature |
| 2 | Brain stem infarction | 99.98% | L5 | Within the original stroke scope, but no direct evidence |
| 3 | ABri amyloidosis | 99.97% | L5 | Prediction only |
| 4 | Cerebral artery occlusion | 99.95% | L3 | Preclinical data and one indirect Phase 4 trial |
| 5 | Pulmonary hypertension, unclear multifactorial mechanism | 99.93% | L5 | Prediction only |
| 6 | Pulmonary hypertension due to lung disease/hypoxia | 99.93% | L4 | Indirect animal, in vitro and altitude studies only |
| 7 | Malignant renovascular hypertension | 99.93% | L5 | Prediction only; ARB safety concerns in renal artery stenosis |
| 8 | Malignant hypertensive renal disease | 99.93% | L5 | Prediction only |
| 9 | Intracerebral haemorrhage | 99.93% | L2 | Phase 3 TRIDENT (combination therapy) |
| 10 | Braddock syndrome | 99.92% | L5 | Prediction only; no identifiable mechanistic basis |

---

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text):** liver failure, hepatic coma/encephalopathy, cholestasis (including benign recurrent and familial intrahepatic forms), liver and gallbladder disease, kidney disease, anuria, renal artery obstruction, pancreatitis, diabetes mellitus and diabetic ketoacidosis, gout, hyperuricaemia, hypotensive disorders, systemic lupus erythematosus (including paediatric), potassium deficiency, hypercalcaemia, hyperparathyroidism, osteitis fibrosa, nephrocalcinosis, phosphorus metabolism disease, pyoureter and neonatal jaundice. These come from a model knowledge graph and should be verified against the TGA-approved Product Information.
- **Drug Interactions:** 100 interactions were identified; 20 were reviewed here. Two are classed as **Major**: potassium citrate and potassium bicarbonate (consistent with a risk of raised potassium). Moderate interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), aspirin, morphine, bupropion, SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), insulin and exenatide, dronabinol, and bowel-preparation agents (picosulfuric acid, sodium sulfate, polyethylene glycol with electrolytes).

Label warnings and contraindications from the Product Information were not available. Please refer to the TGA-approved Product Information (PI) for full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (intracerebral haemorrhage only). Hold for all other predictions without evidence.**

**Rationale:**
- A completed Phase 3 trial (TRIDENT, 1671 participants) tested a telmisartan-containing triple pill after intracerebral haemorrhage, and the NEJM publication has appeared. However, the combination design means telmisartan's individual contribution is unknown, and only one Phase 3 trial supports it (L2).
- The remaining predictions rest on the model alone or on preclinical data, and do not currently justify progression.

**To proceed, the following is needed:**
- Review of the full TRIDENT results (primary outcome, blood pressure effect, safety), which were not available in the compiled data
- Assessment of whether the effect can be attributed to telmisartan or only to the combination
- Mechanism of action data and TGA Product Information warnings and contraindications (both currently missing; label safety data is a blocking gap for safety screening)
- Approved indication text for the Australian ARTG entry
- Confirmation of the knowledge-graph contraindications (renal, hepatic, potassium-related) against the Product Information
- A safety review before any consideration of renovascular or renal indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

