---
layout: default
title: Atenolol
parent: 僅模型預測 (L5)
nav_order: 60
evidence_level: L5
indication_count: 10
---

# Atenolol
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

# Atenolol: From Hypertension to Posterolateral Myocardial Infarction

---

## One-Sentence Summary

Atenolol is a cardioselective β1-adrenergic receptor blocker established in the management of hypertension and angina pectoris. The TxGNN model predicts it may be effective for **Posterolateral Myocardial Infarction** — the highest-ranked prediction with a score of **99.87%** — though no dedicated clinical trials or publications yet exist for this specific anatomical MI subtype. Across all 10 predicted indications, **Chronic Pulmonary Heart Disease (rank 9)** carries the strongest clinical evidence (L3) and is the most immediately actionable direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension, angina pectoris |
| Predicted New Indication | Posterolateral Myocardial Infarction |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| Australia Market Status | No current ARTG entries found in dataset (see note) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

> **⚠️ Data Note:** The Evidence Pack returns 0 ARTG entries for Atenolol. This is inconsistent with its recognised availability as a generic cardiovascular agent and most likely reflects a data collection gap. Clinicians should independently verify current ARTG registration status at [www.tga.gov.au/resources/artg](https://www.tga.gov.au/resources/artg).

---

## Why Is This Prediction Reasonable?

Atenolol is a cardioselective β1-adrenergic receptor antagonist. While detailed mechanism of action data is not available in this Evidence Pack (DrugBank query gap), the pharmacology is well established. Atenolol competitively blocks β1-receptors in cardiac tissue, producing negative chronotropy (reduced heart rate), negative inotropy (reduced contractility), and blood pressure lowering via reduced cardiac output. The net effect is a significant reduction in myocardial oxygen demand — the central therapeutic goal in both ischaemic heart disease and hypertension.

Posterolateral myocardial infarction involves ischaemic necrosis of the posterior-lateral left ventricular wall, most commonly supplied by the left circumflex artery (LCx). Regardless of the specific infarct territory, β-blockers are a cornerstone of post-MI management: they limit infarct extension, attenuate adverse left ventricular remodelling, suppress ventricular arrhythmias, and reduce the risk of reinfarction. The mechanistic basis for Atenolol in this setting is therefore pharmacologically sound.

However, no randomised trials or published literature have addressed posterolateral MI as a distinct anatomical subtype. Large landmark trials — such as ISIS-1 and COMMIT/CCS-2 — validated beta-blocker therapy across general MI populations without stratifying by infarct territory. The TxGNN prediction most likely reflects this broader MI evidence base, meaning this represents a research question rather than a directly established indication at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for posterolateral myocardial infarction.

---

## Literature Evidence

Currently no related literature available for posterolateral myocardial infarction.

---

## Australia Market Information

The current dataset contains no ARTG entries for Atenolol. This is likely a data collection gap given Atenolol's longstanding use as a generic beta-blocker globally. Clinicians should verify current registration directly via the TGA ARTG database.

---

## All Predicted Indications — Summary Overview

The following table summarises all 10 TxGNN predictions, providing a complete picture for clinical decision-making:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Trials | Publications | Decision |
|------|---------------------|-------------|----------------|--------|-------------|----------|
| 1 | Posterolateral myocardial infarction | 99.87% | L4 | 0 | 0 | Hold |
| 2 | Posteroinferior myocardial infarction | 99.87% | L4 | 0 | 1 | Hold |
| 3 | Malignant hypertensive renal disease | 99.85% | L5 | 0 | 0 | Hold |
| 4 | Malignant renovascular hypertension | 99.85% | L4 | 0 | 1 | Hold |
| 5 | Pulmonary hypertension — multifactorial ⚠️ | 99.84% | L5 | 0 | 0 | Hold |
| 6 | Pulmonary hypertension — lung disease/hypoxia ⚠️ | 99.84% | L5 | 0 | 20* | Hold |
| 7 | Septal myocardial infarction | 99.84% | L4 | 0 | 1 | Hold |
| 8 | Braddock syndrome | 99.80% | L5 | 0 | 0 | Hold |
| **9** | **Chronic pulmonary heart disease** | **99.04%** | **L3** | **1** | **15** | **Proceed with Guardrails** |
| 10 | Primary hereditary glaucoma | 98.84% | L4 | 0 | 0 | Hold |

> *Publications for rank 6 are general hypoxia biology reviews with no specific relevance to Atenolol use.

> ⚠️ **Safety Alert — Pulmonary Hypertension (ranks 5 & 6):** β-blockers are generally considered relatively or absolutely contraindicated in pulmonary arterial hypertension. Atenolol may worsen right ventricular failure by reducing cardiac output, precipitate bronchospasm, and suppress the compensatory tachycardic response to low oxygen delivery. **These two indications should not be pursued.**

---

## Spotlight: Chronic Pulmonary Heart Disease (Rank 9) — Strongest Evidence Across All Predictions

Chronic pulmonary heart disease (cor pulmonale) frequently develops secondary to COPD and is often accompanied by systemic hypertension and ischaemic heart disease. Atenolol's β1-selectivity means it has comparatively less impact on β2-mediated bronchodilation than non-selective beta-blockers, making it relatively better tolerated in COPD patients who also carry a cardiac indication.

**Clinical Trial Evidence**

| Trial | Phase | Status | Enrolment | Key Findings |
|-------|-------|--------|-----------|--------------|
| [NCT03278509](https://clinicaltrials.gov/study/NCT03278509) | Phase 4 | Active, not recruiting | 5,000 | REDUCE-SWEDEHEART: registry-based RCT evaluating whether long-term beta-blocker therapy is necessary after MI in patients with preserved left ventricular ejection fraction; enrolls real-world populations including cardiopulmonary comorbidities. Results pending (completion December 2025). |

**Literature Evidence**

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [31524](https://pubmed.ncbi.nlm.nih.gov/31524/) | 1978 | Clinical Study | Lille médical | Direct study of atenolol in chronic pulmonary patients with airway obstruction |
| [15881093](https://pubmed.ncbi.nlm.nih.gov/15881093/) | 2005 | Clinical Study | Terapevticheskii arkhiv | Long-term atenolol in ischaemic heart disease with concomitant COPD — respiratory safety assessment |
| [14520850](https://pubmed.ncbi.nlm.nih.gov/14520850/) | 2003 | Clinical Study | Terapevticheskii arkhiv | Atenolol vs metoprolol vs bisoprolol in isolated systolic hypertension with COPD and/or diabetes — comparative safety |
| [6673339](https://pubmed.ncbi.nlm.nih.gov/6673339/) | 1983 | Clinical Study | Vutreshni bolesti | Beta-blockers in COPD with ischaemic heart disease — 14-day comparative trial |
| [11219471](https://pubmed.ncbi.nlm.nih.gov/11219471/) | 2001 | RCT | Clinical Therapeutics | Telmisartan vs atenolol in mild-to-moderate hypertension — 26-week efficacy and tolerability RCT |
| [28982831](https://pubmed.ncbi.nlm.nih.gov/28982831/) | 2017 | Cohort Study | BMJ Open | ACOS (asthma-COPD overlap) associated with coronary artery disease, dysrhythmia and heart failure — population retrospective cohort |
| [30191469](https://pubmed.ncbi.nlm.nih.gov/30191469/) | 2018 | Retrospective Cohort | Cardiology and Therapy | Cardiovascular hospitalisation risk: nebivolol vs atenolol vs metoprolol in hypertensive patients |
| [1686421](https://pubmed.ncbi.nlm.nih.gov/1686421/) | 1991 | Clinical Study | Cardiologia | Neurohumoral changes in chronic heart failure treated with long-term atenolol 50 mg/day — improved EF and exercise capacity at 1 year |
| [20354044](https://pubmed.ncbi.nlm.nih.gov/20354044/) | 2010 | Registry Survey | Postgraduate Medical Journal | Heart rate control in stable angina — European Heart Survey, includes cardiopulmonary comorbidities |
| [25350545](https://pubmed.ncbi.nlm.nih.gov/25350545/) | 2014 | Experimental Study | PLoS One | β2-adrenergic receptor-dependent attenuation of hypoxic pulmonary vasoconstriction in intermittent hypoxia model — mechanistic relevance to cardiopulmonary interface |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for complete safety information.

The following safety signals are highlighted within the Evidence Pack clinical rationale and warrant attention:

- **AV Conduction in Inferior/Posterior MI:** Posteroinferior MI (rank 2) frequently involves right coronary artery occlusion, which supplies both the SA and AV nodes. Beta-blockers may worsen sinus bradycardia or precipitate AV block in this setting — conduction status must be assessed before initiation.
- **Renal Accumulation:** Atenolol is primarily renally excreted. In conditions involving renal impairment (e.g., malignant hypertensive renal disease, rank 3), dose reduction and close monitoring are required due to accumulation risk.
- **Pulmonary Safety in COPD:** Although Atenolol is β1-selective, residual β2-blockade at higher doses may cause clinically meaningful bronchospasm in severe obstructive airway disease.
- **Pulmonary Hypertension — Contraindication Signal:** Beta-blockers including Atenolol are potentially harmful in pulmonary arterial hypertension; use in ranks 5 and 6 should be avoided.

---

## Conclusion and Next Steps

### Primary Indication (Rank 1 — Posterolateral MI)

**Decision: Hold**

**Rationale:**
No clinical trials or literature specifically address posterolateral MI as an independent anatomical entity. While beta-blocker therapy is standard of care in post-MI management generally, the L4 evidence level reflects mechanistic reasoning only and does not meet the threshold for active clinical application of this specific indication.

**To proceed, the following is needed:**
- Subgroup analysis from existing large MI beta-blocker trials (ISIS-1, COMMIT/CCS-2, REDUCE-SWEDEHEART) stratified by infarct territory
- Independent verification of current ARTG registration status via the TGA website
- TGA-approved Product Information (PI) review for complete contraindications and warnings
- DrugBank MOA data retrieval to complete the mechanistic profile

---

### Highest-Priority Actionable Indication (Rank 9 — Chronic Pulmonary Heart Disease)

**Decision: Proceed with Guardrails**

**Rationale:**
This indication carries L3 evidence, supported by one active large-scale Phase 4 trial (REDUCE-SWEDEHEART, n=5,000) and multiple observational and clinical studies directly investigating Atenolol in COPD-cardiac comorbidity populations. The β1-selectivity of Atenolol provides a relative safety advantage in this patient group.

**To proceed, the following is needed:**
- Await final results from NCT03278509 (REDUCE-SWEDEHEART, completion December 2025) for definitive guidance on long-term beta-blocker use in MI patients with preserved EF
- Establish a multidisciplinary cardiopulmonary monitoring plan: serial spirometry (FEV1/FVC), right heart function assessment (echocardiogram), and oxygen saturation monitoring
- Exclude patients with active bronchospasm, severe COPD (GOLD Stage III–IV), or significant pulmonary hypertension prior to initiation
- Confirm ARTG status and access to Atenolol in Australia, including dosing guidance for renal-impaired patients

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application. Refer to TGA-approved Product Information for prescribing decisions.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

