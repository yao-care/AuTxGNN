---
layout: default
title: Carvedilol
parent: 僅模型預測 (L5)
nav_order: 129
evidence_level: L5
indication_count: 10
---

# Carvedilol
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

# Carvedilol: From Hypertension and Heart Failure to Malignant Renovascular Hypertension

## One-Sentence Summary

Carvedilol is a third-generation, non-selective β- and α1-adrenergic blocker established internationally for hypertension, chronic heart failure, and left ventricular dysfunction following myocardial infarction — though it is not currently registered with the TGA in Australia.

The TxGNN model ranks **Malignant Renovascular Hypertension** as its top predicted new indication, with a prediction confidence of **99.55%**, representing a mechanistically plausible extension of its established antihypertensive properties.

No clinical trials or publications directly address this specific indication; however, among the full set of ten TxGNN predictions, **Chronic Pulmonary Heart Disease** (rank 6) carries the strongest supporting evidence (Level L2) and a recommendation of **Proceed with Guardrails** — this is the most actionable finding in this Evidence Pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered with TGA; used internationally for hypertension and chronic heart failure |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## All Predicted Indications at a Glance

| Rank | Indication | TxGNN Score | Evidence Level | Decision |
|------|-----------|-------------|----------------|----------|
| 1 | Malignant Renovascular Hypertension | 99.55% | L4 | Hold |
| 2 | Malignant Hypertensive Renal Disease | 99.55% | L4 | Hold |
| 3 | Pulmonary Hypertension (Lung Disease / Hypoxia) | 99.54% | L5 | Hold |
| 4 | Pulmonary Hypertension (Unclear Multifactorial) | 99.54% | L5 | Hold |
| 5 | Braddock Syndrome | 99.37% | L5 | Hold |
| **6** | **Chronic Pulmonary Heart Disease** | **94.55%** | **L2** | **Proceed with Guardrails** |
| 7 | Susceptibility to Ischaemic Stroke *(obsolete ontology term)* | 68.65% | L5 | Hold |
| 8 | Cerebrovascular Disorder | 68.08% | L4 | Research Question |
| 9 | Ocular Tuberculosis | 61.20% | L5 | Hold |
| 10 | Brain Stem Infarction | 59.72% | L5 | Hold |

> **Note:** Rank 7 uses an obsolete disease ontology classification and should not be pursued as defined. Re-evaluation under current cerebrovascular disease terminology (rank 8) is appropriate. Rank 6 (Chronic Pulmonary Heart Disease) is the primary actionable finding and is discussed in detail below.

---

## Why Is This Prediction Reasonable?

Carvedilol belongs to the third-generation beta-blocker class and is pharmacologically distinctive from cardioselective agents. It simultaneously blocks β1, β2, and α1-adrenergic receptors: β1-blockade reduces heart rate, cardiac output, and renin release from the juxtaglomerular apparatus; α1-blockade causes peripheral arterial vasodilation, lowering systemic vascular resistance. This dual mechanism produces a broader antihypertensive effect than selective beta-blockers and is particularly relevant in conditions involving heightened adrenergic tone.

Malignant renovascular hypertension is a hypertensive crisis subtype driven by renal artery pathology — stenosis, thrombosis, or dysplasia — which massively activates the renin–angiotensin–sympathetic axis. Blood pressure elevation is both severe and rapidly progressive, causing end-organ damage including hypertensive nephropathy, retinopathy, and encephalopathy. Carvedilol's ability to suppress the sympathetic amplification loop via β-blockade (reducing cardiac output and renin) and to reduce peripheral vasoconstriction via α1-blockade is mechanistically well-matched to this pathophysiology.

Currently, detailed DrugBank mechanism of action data is not available in this Evidence Pack. While Carvedilol's antihypertensive role is globally established for broader hypertension populations, no clinical trials or publications specifically investigate its use in the malignant renovascular hypertension subtype. The high TxGNN prediction score likely reflects strong topological proximity within the cardiovascular disease knowledge graph rather than direct empirical clinical evidence for this specific condition.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Malignant Renovascular Hypertension.

---

## Literature Evidence

Currently no related literature available for Malignant Renovascular Hypertension.

---

## Key Secondary Finding: Chronic Pulmonary Heart Disease (L2 — Proceed with Guardrails)

Among all ten TxGNN predictions, Chronic Pulmonary Heart Disease (rank 6, TxGNN score 94.55%) carries the highest quality supporting evidence and the most actionable recommendation. Multiple completed Phase 4 trials and several prospective/cohort studies directly address Carvedilol's safety and efficacy in patients with comorbid heart failure and obstructive lung disease.

### Clinical Trials — Chronic Pulmonary Heart Disease

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02120339](https://clinicaltrials.gov/study/NCT02120339) | Phase 1 | Terminated | 5 | Beta-blockers (including Carvedilol) in Pulmonary Arterial Hypertension: efficacy and safety assessment — terminated early, safety signal identified; most directly relevant trial for this indication |
| [NCT00924833](https://clinicaltrials.gov/study/NCT00924833) | Phase 4 | Completed | 27 | Carvedilol vs Nebivolol at high altitude in heart failure patients: cardiovascular, metabolic, and respiratory effects under simulated hypoxia — directly compares non-selective beta-blockade respiratory safety |
| [NCT00517725](https://clinicaltrials.gov/study/NCT00517725) | Phase 4 | Completed | 60 | Three-way comparison (Nebivolol vs Bisoprolol vs Carvedilol) in heart failure: exercise capacity and chemoreceptor/hypoxic response, including lung diffusion capacity |
| [NCT01656005](https://clinicaltrials.gov/study/NCT01656005) | Phase 4 | Completed | 18 | Cardioselective vs non-cardioselective (Carvedilol-type) beta-blockers in moderate-to-severe COPD: chronic cardiopulmonary function effects evaluated over time |
| [NCT03370835](https://clinicaltrials.gov/study/NCT03370835) | Phase 4 | Completed | 21 | Randomised crossover: Metoprolol-ER vs Carvedilol tolerability in COPD — direct safety head-to-head at guideline-recommended doses |
| [NCT00384566](https://clinicaltrials.gov/study/NCT00384566) | Phase 4 | Withdrawn | 0 | CAMERA Study (Carvedilol vs Metoprolol respiratory assessment in heart failure) — withdrawn before enrolment, no data available; historically significant study design |

### Literature Evidence — Chronic Pulmonary Heart Disease

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32000982](https://pubmed.ncbi.nlm.nih.gov/32000982/) | 2020 | RCT (propensity-matched) | Am J Cardiology | Metoprolol vs Carvedilol in elderly patients with heart failure, COPD, and diabetes: 1:1 propensity score-matched survival analysis; quantifies the comparative risk of COPD hospitalisation under non-selective blockade |
| [29159953](https://pubmed.ncbi.nlm.nih.gov/29159953/) | 2018 | Cohort | Eur J Heart Failure | Carvedilol vs cardioselective beta-blockers in Danish HF+COPD cohort: all-cause, COPD-related, and HF hospitalisation hazards compared; informs real-world comparative safety |
| [26844454](https://pubmed.ncbi.nlm.nih.gov/26844454/) | 2016 | Retrospective Cohort | Medicine | Carvedilol, Bisoprolol, and Metoprolol in coexistent HF+COPD: nationwide Taiwan NHIRD survival analysis — Carvedilol use associated with comparable outcomes to cardioselective agents in this population |
| [20413026](https://pubmed.ncbi.nlm.nih.gov/20413026/) | 2010 | Comparative (Crossover) | JACC | Randomised crossover switching between β1-selective and non-selective beta-blockers in CHF+COPD: respiratory, haemodynamic, and clinical endpoints — directly quantifies respiratory impact of switching to Carvedilol |
| [22015086](https://pubmed.ncbi.nlm.nih.gov/22015086/) | 2011 | Prospective Cohort | Respiratory Medicine | Bisoprolol vs Carvedilol in CHF+COPD: FEV1, FVC, and cardiac function compared; Carvedilol showed greater FEV1 reduction |
| [12490274](https://pubmed.ncbi.nlm.nih.gov/12490274/) | 2002 | Prospective | J Heart Lung Transplant | Carvedilol tolerability in CHF with COPD or asthma: prospective assessment of withdrawal rate and pulmonary adverse events in real clinical setting |
| [31391573](https://pubmed.ncbi.nlm.nih.gov/31391573/) | 2019 | Observational | Scientific Reports | Italian register-based cohort: predictors of Carvedilol selection over cardioselective agents in HF+COPD — identifies patient factors driving clinical decision-making |
| [31521680](https://pubmed.ncbi.nlm.nih.gov/31521680/) | 2019 | Review | JACC Heart Failure | State-of-the-art review of diagnostic and therapeutic gaps in HF+COPD, including beta-blocker underprescription; contextualises Carvedilol's role in guideline-based care |
| [15358010](https://pubmed.ncbi.nlm.nih.gov/15358010/) | 2004 | Review | JACC | Non-selective β/α-blockade (Carvedilol) in CHF+COPD: theoretical and clinical considerations regarding ventilatory mechanics and exercise limitation |
| [17561440](https://pubmed.ncbi.nlm.nih.gov/17561440/) | 2007 | — | Eur J Heart Failure | Lung function with Carvedilol vs Bisoprolol in CHF: relevance of β-selectivity for airway and alveolar function — directly compares respiratory impact of non-selective vs selective beta-blockade |

### Mechanistic Rationale — Chronic Pulmonary Heart Disease

Carvedilol's multi-receptor profile provides several mechanistic advantages in chronic pulmonary heart disease (cor pulmonale with left ventricular dysfunction): **(1)** β1-blockade improves ventricular remodelling and reduces neurohormonal activation in both the right and left ventricle; **(2)** α1-blockade reduces right ventricular afterload by lowering systemic vascular resistance; **(3)** the carbazole moiety of Carvedilol confers antioxidant properties that may reduce oxidative stress-mediated vascular and myocardial damage.

The primary safety concern is **non-selective β2-blockade**, which may aggravate bronchospasm and worsen airway resistance in underlying COPD. Randomised crossover data (PMID 20413026) shows switching from cardioselective to Carvedilol is associated with measurable FEV1 reduction. Clinical guidelines generally recommend cardioselective agents (metoprolol, bisoprolol) when significant airflow limitation exists.

**Safety Guardrails for Chronic Pulmonary Heart Disease:**
- Baseline spirometry (FEV1/FVC) before initiation and at 4–6 weeks
- Start at lowest available dose; titrate slowly over 2–4 weeks
- Contraindicated in acute bronchospasm or severely decompensated obstructive airways disease
- Monitor dyspnoea and wheeze at each visit during titration
- Prefer cardioselective beta-blockers if FEV1 < 50% predicted or significant reversibility on spirometry
- Have bronchodilator (salbutamol) available for acute bronchospasm management

---

## Australia Market Information

Carvedilol is not currently registered with the TGA and has no ARTG entries. Australian prescribers seeking access would need to apply through one of the following pathways:

- **Special Access Scheme (SAS) Category B**: For individual patients with a serious or life-threatening condition where no suitable TGA-approved alternative is available
- **Authorised Prescriber (AP) Scheme**: For ongoing access by a specialist clinician for a defined class of patients
- **Clinical Trial / CTN**: If evaluating Carvedilol prospectively within an Australian research context

International product information — such as the US FDA-approved PI for Coreg® (carvedilol, GlaxoSmithKline) — should be consulted for full dosing, contraindications, and monitoring requirements.

---

## Safety Considerations

Please refer to international prescribing information for complete safety data, as no TGA-approved Australian PI is available. Key class-specific safety considerations include:

- **Bronchospasm risk**: Non-selective β2-blockade may precipitate bronchospasm; exercise caution or avoid in asthma or significant COPD
- **Haemodynamic effects**: Hypotension, dizziness, and bradycardia — titrate carefully in elderly patients or those with haemodynamic vulnerability
- **Hypoglycaemia masking**: May blunt tachycardia as a warning sign of hypoglycaemia in insulin-treated diabetes
- **Rebound hypertension/angina**: Abrupt withdrawal may precipitate rebound angina or hypertensive crisis — taper gradually

Drug interaction data is not currently available for this review.

---

## Conclusion and Next Steps

**Decision: Hold** *(Primary Indication — Malignant Renovascular Hypertension)*

**Rationale:**
Despite a high TxGNN prediction score (99.55%), no clinical trials or published literature directly support Carvedilol use in malignant renovascular hypertension. The evidence is at mechanistic plausibility level only (L4), Carvedilol is not registered in Australia, and a full pharmacological and safety profile review is still required before any clinical pathway can be recommended.

---

**Decision: Proceed with Guardrails** *(Secondary Finding — Chronic Pulmonary Heart Disease, L2)*

**Rationale:**
Multiple completed Phase 4 trials and prospective cohort studies support the tolerability and efficacy of Carvedilol in patients with comorbid heart failure and chronic obstructive pulmonary disease. The evidence is sufficient to consider carefully selected patients under close clinical supervision.

---

**To proceed for Malignant Renovascular Hypertension, the following is needed:**
- Systematic literature search targeting Carvedilol (or non-selective beta-blockers) specifically in malignant hypertensive crisis and renovascular hypertension subtypes
- Review of international hypertensive emergency guidelines (ESH/ESC, AHA/ACC) for beta-blocker positioning
- Retrieval of full DrugBank pharmacological profile for DB01136 (MOA, interactions, toxicity)
- TGA market access pathway evaluation (SAS, AP, or clinical trial pathway)

**To proceed for Chronic Pulmonary Heart Disease, the following is needed:**
- Australian cardio-pulmonary specialist panel review for patient selection criteria
- Proposed monitoring protocol: spirometry schedule, dose titration plan, adverse event thresholds
- Joint cardiologist–respiratory physician review framework for individual patient assessment
- SAS Category B application preparation if prescribing off-label prior to registration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

