---
layout: default
title: Bisoprolol
parent: 僅模型預測 (L5)
nav_order: 91
evidence_level: L5
indication_count: 10
---

# Bisoprolol
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

# Bisoprolol: From Heart Failure to Chronic Pulmonary Heart Disease

---

## One-Sentence Summary

Bisoprolol is a highly selective β1-adrenergic receptor blocker used internationally for chronic heart failure, hypertension, and stable coronary artery disease — though it currently holds no TGA registration in Australia.
The TxGNN model's highest-ranked prediction is **malignant renovascular hypertension** (score 99.94%), however no supporting clinical evidence currently exists for that indication; the most actionable predicted indication — and the focus of this report — is **Chronic Pulmonary Heart Disease** (score 98.63%), backed by **a completed Phase 3 RCT**, **multiple additional clinical trials**, and **20 publications**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic heart failure, hypertension, angina pectoris (internationally approved; no current Australian TGA registration) |
| Predicted New Indication | Chronic Pulmonary Heart Disease (cor pulmonale / heart failure with coexistent COPD) |
| TxGNN Prediction Score | 98.63% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on well-established pharmacological knowledge, Bisoprolol is widely regarded as the most highly selective β1-adrenergic receptor blocker available, with approximately 75-fold selectivity for β1- over β2-adrenoceptors at therapeutic doses. This extreme selectivity is the central feature underpinning its potential role in chronic pulmonary heart disease.

Chronic pulmonary heart disease — encompassing right heart failure and cardiac dysfunction arising from or coexisting with chronic obstructive pulmonary disease (COPD) — has historically created a prescribing dilemma: beta-blockers substantially reduce mortality in heart failure (CIBIS-II demonstrated a ~34% reduction in all-cause mortality with Bisoprolol), yet clinicians have long withheld them from COPD patients fearing β2-mediated bronchoconstriction and worsening of airflow obstruction. Bisoprolol's exceptional β1-selectivity theoretically addresses this concern — providing cardiac benefits (reduced heart rate, lowered myocardial oxygen demand, attenuation of sympathetic overactivation, inhibition of ventricular remodelling, and suppression of renin secretion) whilst exerting minimal clinically meaningful effect on β2-adrenoceptors in the airways at standard doses.

The TxGNN knowledge graph model almost certainly captures this mechanistic overlap through shared "hypertension," "heart failure," and "adrenergic" pathway nodes. Beyond the model prediction, a substantial and growing body of observational cohort data consistently associates β-blocker use — particularly cardioselective agents — with reduced COPD exacerbation rates and improved survival in patients with coexistent cardiac disease. The 2024 BICS Phase 3 RCT (NCT03917914) was the first dedicated randomised trial to directly address this question, and its results, published in JAMA, provide the strongest direct clinical evidence to date. This convergence of mechanistic rationale and clinical trial data supports the TxGNN prediction being well-grounded rather than a statistical artefact.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03917914](https://clinicaltrials.gov/study/NCT03917914) | Phase 3 | Completed | 280 | **BICS trial** — double-blind, randomised, placebo-controlled trial evaluating Bisoprolol for prevention of adverse cardiac events in COPD patients at high exacerbation risk. Results published in JAMA 2024 (PMID 38762800). Represents the strongest and most direct clinical evidence for this indication. |
| [NCT00702156](https://clinicaltrials.gov/study/NCT00702156) | Phase 2 | Terminated | 27 | Cardioselective beta-blockade with Bisoprolol in patients with CHF and moderate–severe COPD (with or without significant reversibility). Assessed pulmonary function and quality of life; terminated early, but directly tested the mechanistic hypothesis. |
| [NCT02380053](https://clinicaltrials.gov/study/NCT02380053) | Phase 4 | Completed | 10 | Head-to-head comparison of Bisoprolol versus Celiprolol in COPD: differential effects on cardiopulmonary outcomes at rest and during exercise. Small sample limits generalisability, but directly compares Bisoprolol in a COPD population. |
| [NCT01656005](https://clinicaltrials.gov/study/NCT01656005) | Phase 4 | Completed | 18 | Evaluated cardioselective (including Bisoprolol) versus non-cardioselective beta-blockers on cardiopulmonary function in moderate–severe COPD. Provides direct safety data relevant to airway effects. |
| [NCT00517725](https://clinicaltrials.gov/study/NCT00517725) | Phase 4 | Completed | 60 | Nebivolol vs Bisoprolol vs Carvedilol in heart failure: effects on exercise capacity, chemoreceptor response, hypoxia, and lung diffusion capacity. Partly overlaps with chronic pulmonary heart disease through hypoxia and pulmonary function assessments. |
| [NCT00292162](https://clinicaltrials.gov/study/NCT00292162) | N/A | Completed | 41 | Radiofrequency ablation for atrial fibrillation in advanced CHF; Bisoprolol used as background therapy. Atrial fibrillation is a common complication of cor pulmonale — indirect clinical relevance. |
| [NCT00878384](https://clinicaltrials.gov/study/NCT00878384) | N/A | Completed | 52 | Catheter ablation vs rate-control strategy (Bisoprolol as rate-control agent) for persistent AF in CHF. Indirect relevance via AF management in the cor pulmonale patient population. |
| [NCT03778554](https://clinicaltrials.gov/study/NCT03778554) | Phase 4 | Active (not recruiting) | 2,760 | **DANBLOCK** — long-term oral beta-blocker after myocardial infarction without reduced ejection fraction. Large contemporary trial; cardiovascular outcome data may inform broader beta-blocker use in cardiopulmonary overlap patients. |
| [NCT03646357](https://clinicaltrials.gov/study/NCT03646357) | Phase 4 | Active (not recruiting) | 2,895 | **BETAMI** — beta-blocker therapy after acute MI without reduced LVEF. Large ongoing Scandinavian trial; indirect relevance via cardiovascular mortality and heart failure outcomes. |
| [NCT01829880](https://clinicaltrials.gov/study/NCT01829880) | N/A | Unknown | 60 | Pharmacokinetic study of Bisoprolol and Ramipril in CHF patients with cachexia and altered body composition. No efficacy data, but informs dosing considerations in clinically complex cor pulmonale patients. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [38762800](https://pubmed.ncbi.nlm.nih.gov/38762800/) | 2024 | RCT (Phase 3) | JAMA | **BICS trial**: Bisoprolol in COPD patients at high risk of exacerbation. The landmark dedicated RCT for this indication. Metoprolol had previously been shown to increase COPD hospitalisations; this trial specifically examined Bisoprolol's superior β1-selectivity profile. |
| [40386836](https://pubmed.ncbi.nlm.nih.gov/40386836/) | 2025 | RCT / Full Report | Health Technology Assessment | Full HTA report of the BICS RCT, including health economic analysis, secondary endpoints, and comprehensive safety reporting. Confirmatory and complementary to the JAMA publication. |
| [38587241](https://pubmed.ncbi.nlm.nih.gov/38587241/) | 2024 | RCT / Meta-analysis | New England Journal of Medicine | Beta-blockers after MI with preserved ejection fraction in the modern treatment era. Contextualises the evolving evidence base for beta-blocker use in cardiovascular patients, many of whom have concurrent COPD. |
| [38152590](https://pubmed.ncbi.nlm.nih.gov/38152590/) | 2023 | Systematic Review & Meta-analysis | International Journal of Chronic Obstructive Pulmonary Disease | Comprehensive pooled analysis of Bisoprolol efficacy and safety specifically in COPD patients across all available published studies. Tier 1 evidence synthesis. |
| [29159953](https://pubmed.ncbi.nlm.nih.gov/29159953/) | 2018 | Observational Cohort | European Journal of Heart Failure | Danish nationwide cohort comparing Carvedilol vs Bisoprolol/Metoprolol/Nebivolol in patients with HF and concurrent COPD; assessed all-cause, HF, and COPD-related hospitalisation rates. |
| [31391573](https://pubmed.ncbi.nlm.nih.gov/31391573/) | 2019 | Register-based Comparative Study | Scientific Reports | Italian register cohort identifying predictors of beta-blocker choice in HF + COPD; supports current guideline preference for Bisoprolol/metoprolol/nebivolol over carvedilol in this population. |
| [27792991](https://pubmed.ncbi.nlm.nih.gov/27792991/) | 2017 | Clinical Study | International Journal of Cardiology | Bisoprolol versus Carvedilol in CHF: differences in myocardial injury protection and pulmonary function. Bisoprolol demonstrated superior preservation of pulmonary outcomes. |
| [26844454](https://pubmed.ncbi.nlm.nih.gov/26844454/) | 2016 | Population-based Cohort | Medicine | Taiwanese nationwide NHIRD study evaluating survival effects of Carvedilol, Bisoprolol, and Metoprolol in patients with coexistent HF and COPD. |
| [22157723](https://pubmed.ncbi.nlm.nih.gov/22157723/) | 2012 | Preclinical Study | Circulation: Heart Failure | Bisoprolol delays progression to right heart failure in an experimental pulmonary hypertension animal model, with sympathoadrenergic overactivity as the target pathway. Provides mechanistic support for cardiac benefit in cor pulmonale. |
| [19460848](https://pubmed.ncbi.nlm.nih.gov/19460848/) | 2009 | RCT | European Journal of Heart Failure | One of the first prospective randomised trials examining Bisoprolol in patients with both heart failure and moderate–severe COPD. Foundational evidence establishing the mechanistic and clinical feasibility of this approach. |

---

## Australia Market Information

Bisoprolol is **not currently listed on the Australian Register of Therapeutic Goods (ARTG)**. There are no TGA-approved products for this drug in Australia as of April 2026. Australian clinicians wishing to access Bisoprolol for any indication would need to explore one of the following regulatory pathways:

- **Special Access Scheme (SAS) Category B or C** — for individual patients with unmet clinical need
- **Authorised Prescriber (AP) pathway** — for clinicians with ongoing need to prescribe in a defined patient population
- **Clinical trial authorisation** — if investigating within a formal research framework

Note that Bisoprolol is widely registered and commercially available in comparable markets including the United Kingdom (MHRA), European Union (EMA), Japan (PMDA), and the United States (FDA), where it is approved for heart failure with reduced ejection fraction and hypertension. These international approvals and product information documents may be referenced for safety and dosing guidance pending local registration.

---

## Safety Considerations

No Australian-specific safety data (TGA-approved PI, ARTG warnings, or DDI data) is currently available in this evidence pack.

Please refer to international Product Information documents (e.g., EMA Summary of Product Characteristics or FDA Prescribing Information) for full safety information. Key safety areas that Australian clinicians should review prior to use include:

- **Airway disease**: Bisoprolol's high β1-selectivity substantially reduces — but does not eliminate — the risk of bronchoconstriction. It should be used with caution in reactive airway disease and is contraindicated in severe asthma.
- **Cardiac conduction**: Risk of bradycardia, AV block, and heart block; contraindicated in sick sinus syndrome and second/third degree AV block without a pacemaker.
- **Heart failure initiation**: Must be started at very low doses with slow up-titration in decompensated or unstable heart failure.
- **Abrupt withdrawal**: Should not be stopped suddenly; may precipitate rebound tachycardia, angina, or myocardial ischaemia.
- **Metabolic effects**: May mask hypoglycaemia symptoms in insulin-dependent diabetics.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The 2024 BICS Phase 3 RCT (NCT03917914, published in JAMA) directly evaluated Bisoprolol in COPD patients at high cardiac risk, supported by a 2023 systematic review and meta-analysis, multiple observational cohort studies across three continents, and a strong mechanistic rationale grounded in Bisoprolol's exceptional β1-selectivity. The evidence level meets L2 criteria, and international clinical guidelines already favour cardioselective beta-blockers (including Bisoprolol) for heart failure patients with concurrent COPD. Proceeding with structured evaluation in the Australian context is warranted.

**To proceed, the following is needed:**

- **TGA registration pathway**: Determine whether access via the Special Access Scheme, Authorised Prescriber pathway, or a formal registration application is most appropriate, given the absence of any current ARTG listing
- **Full safety data review**: Obtain and review the complete international Product Information to document contraindications, precautions, and drug interactions for the Australian clinical setting
- **MOA documentation**: Retrieve formal mechanism of action data from DrugBank (DB00612) to complete the mechanistic analysis for regulatory submissions
- **BICS trial primary results in full**: Review complete published outcomes (including the JAMA paper PMID 38762800 and HTA report PMID 40386836) before clinical adoption — noting that the BICS trial enrolled COPD patients at high exacerbation risk, which defines the target population
- **Patient population definition**: Clearly delineate the intended indication (CHF with concurrent COPD vs. COPD-associated cor pulmonale) and ensure patients with severe asthma are excluded
- **Pharmacovigilance plan**: Develop a monitoring plan aligned with TGA post-market requirements, including respiratory and cardiac safety surveillance, prior to any broader prescribing

---

*This report is generated from TxGNN model predictions and available literature as of 5 April 2026. Results are for research purposes only and do not constitute medical advice. Predicted drug repurposing candidates require clinical validation before application in patient care. All website content should include appropriate YMYL disclaimers.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

