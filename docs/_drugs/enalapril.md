---
layout: default
title: Enalapril
parent: 僅模型預測 (L5)
nav_order: 185
evidence_level: L5
indication_count: 10
---

# Enalapril
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

# Enalapril: From Hypertension / Heart Failure to Chronic Pulmonary Heart Disease

## One-Sentence Summary

Enalapril is an ACE (angiotensin-converting enzyme) inhibitor with established cardiovascular use, primarily for hypertension and heart failure.
The TxGNN model predicts it may be effective for **Chronic Pulmonary Heart Disease (Cor Pulmonale)**,
with **4 clinical trials** and **20 publications** currently available to support this direction — though direct, high-quality evidence remains limited.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No ARTG registration recorded; Enalapril is internationally established for hypertension and heart failure |
| Predicted New Indication | Chronic Pulmonary Heart Disease |
| TxGNN Prediction Score | 98.91% |
| Evidence Level | L3 |
| Australia Market Status | Not listed in ARTG (0 entries recorded) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current dataset. Based on well-established pharmacology, Enalapril is an ACE inhibitor that blocks the conversion of Angiotensin I to Angiotensin II, thereby reducing systemic and pulmonary vasoconstriction, lowering aldosterone-mediated fluid retention, and decreasing ventricular afterload. Its efficacy in hypertension and systolic heart failure has been confirmed across decades of clinical research, including the landmark SOLVD trial.

In chronic pulmonary heart disease (cor pulmonale), the right ventricle is subjected to sustained pressure overload driven by pulmonary hypertension — most commonly secondary to COPD. By suppressing Angiotensin II, Enalapril can theoretically reduce pulmonary vascular resistance and right ventricular afterload, while also alleviating fluid overload through aldosterone suppression. Both mechanisms address core pathophysiological drivers of cor pulmonale.

A small but direct clinical study (PMID 1405196, 1992) demonstrated that 30 days of Enalapril therapy in 11 patients with COPD-related cor pulmonale produced a moderate yet statistically significant reduction in mean pulmonary artery pressure, alongside improved haemodynamics and exercise tolerance. Preclinical work (PMID 9140694) further confirmed that ACE inhibition can reverse chronic hypoxia-induced pulmonary hypertension and right ventricular hypertrophy and fibrosis in animal models. The TxGNN score of 0.989 reflects a strong knowledge-graph association between the RAAS pathway and cor pulmonale nodes; however, current human evidence is limited to small observational studies, warranting prospective investigation before clinical application.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT02768298](https://clinicaltrials.gov/study/NCT02768298) | Phase 4 | Completed | 201 | Double-blind RCT comparing LCZ696 (sacubitril/valsartan) versus Enalapril in HFrEF patients to assess exercise capacity improvement. Enalapril served as the active control group, providing an efficacy benchmark for ACE inhibition in heart failure — offers indirect support for Enalapril's role in pulmonary heart disease management |
| [NCT00292162](https://clinicaltrials.gov/study/NCT00292162) | N/A | Completed | 41 | Radiofrequency ablation for atrial fibrillation in advanced chronic heart failure; no direct relevance to Enalapril in cor pulmonale, but highlights the complexity of managing combined HF and cardiopulmonary disease |
| [NCT00151619](https://clinicaltrials.gov/study/NCT00151619) | Phase 2 | Terminated | 7 | Evaluated regional haemodynamic effects of adding amlodipine to a background regimen of Enalapril, furosemide, and digoxin in CHF; terminated early due to insufficient enrolment — results inconclusive |
| [NCT06697353](https://clinicaltrials.gov/study/NCT06697353) | N/A | Completed | 4,936 | Japanese real-world retrospective cohort of chronic HFrEF patients treated with Vericiguat; no direct relevance to Enalapril or chronic pulmonary heart disease |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [1405196](https://pubmed.ncbi.nlm.nih.gov/1405196/) | 1992 | Clinical Study | Kardiologia polska | **Direct evidence**: Enalapril (10–20 mg/day, 30 days) in 11 cor pulmonale patients secondary to COPD produced a moderate but significant reduction in mean pulmonary artery pressure and improved haemodynamics, spirometry, and treadmill exercise tolerance |
| [9140694](https://pubmed.ncbi.nlm.nih.gov/9140694/) | 1997 | Preclinical Study | Cardiovascular Drugs and Therapy | Enalapril treatment in rats recovering from chronic hypoxia reduced ventricular collagen content and partially reversed hypoxia-induced pulmonary hypertension and right ventricular hypertrophy |
| [6313787](https://pubmed.ncbi.nlm.nih.gov/6313787/) | 1983 | Early Clinical Trial | JACC | Enalapril acutely and chronically increased cardiac index and reduced pulmonary capillary wedge pressure, right atrial pressure, and systemic vascular resistance in 15 chronic heart failure patients |
| [2210899](https://pubmed.ncbi.nlm.nih.gov/2210899/) | 1990 | Clinical Study | Int J Cardiology | Enalapril as initial monotherapy in severe CHF with sodium retention significantly reduced right atrial pressure (13 → ~9 mmHg) and pulmonary wedge pressure (29 → ~20 mmHg) |
| [33522249](https://pubmed.ncbi.nlm.nih.gov/33522249/) | 2021 | Cohort Study | J Am Heart Association | PARADIGM-HF subgroup (n=8,399): HFrEF patients with comorbid COPD were undertreated and had worse outcomes, highlighting the clinical importance of optimising RAAS-targeting therapies in this overlap population |
| [30738210](https://pubmed.ncbi.nlm.nih.gov/30738210/) | 2019 | Animal Study | J Pharmacol Toxicol Methods | BALB/c mouse HF model with pulmonary oedema and pleural effusion was validated using standard HF pharmacotherapies including Enalapril — supports translational relevance |
| [20592661](https://pubmed.ncbi.nlm.nih.gov/20592661/) | 2011 | Review | Am J Therapeutics | ACE inhibitors in heart failure exert immunomodulatory and anti-cytokine effects (reducing TNF-α, IL-6) that may contribute to therapeutic benefits beyond haemodynamic improvement |
| [39210725](https://pubmed.ncbi.nlm.nih.gov/39210725/) | 2024 | Post-hoc Analysis | JAMA Cardiology | PARADIGM-HF/PARAGON-HF pooled analysis: sacubitril/valsartan reduced all-cause hospitalisation versus Enalapril — reaffirms Enalapril as the established ACE inhibitor comparator in heart failure trials |
| [40329926](https://pubmed.ncbi.nlm.nih.gov/40329926/) | 2025 | Review | High Alt Med Biol | Comprehensive review of chronic mountain sickness management, including RAAS-related pulmonary hypertension complications — relevant background for hypoxic cor pulmonale pathophysiology |
| [9673832](https://pubmed.ncbi.nlm.nih.gov/9673832/) | 1998 | Pharmacokinetics Review | Clin Pharmacokinetics | Vasodilator pharmacokinetics review including ACE inhibitors in cardiopulmonary disease; useful reference for dosing considerations in COPD/cor pulmonale patients |

---

## Australia Market Information

Enalapril currently has **no recorded ARTG registrations** in this dataset (0 entries). Clinicians in Australia seeking to use Enalapril should note:

- Access may be possible via the **TGA Special Access Scheme (SAS)** or **Authorised Prescriber** pathway
- Closely related ACE inhibitors registered in Australia (e.g., **ramipril**, **perindopril**, **lisinopril**) are pharmacologically similar and may be considered as class-representative alternatives
- Prescribers should verify current ARTG status directly via the [TGA ARTG Public Summary](https://www.tga.gov.au/resources/artg)

*Note: This dataset reflects a query date of 4 April 2026. Market status may have changed.*

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. As Enalapril has no current ARTG registration, clinicians should consult internationally approved product labelling (e.g., EMA, FDA, or WHO prescribing information) until local documentation becomes available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic basis for Enalapril in chronic pulmonary heart disease is pharmacologically plausible, and one small direct clinical study (n=11) provides early positive haemodynamic evidence. However, no completed Phase 2/3 RCTs specifically targeting cor pulmonale exist, and Enalapril currently has no ARTG registration in Australia — both factors prevent a "Proceed" recommendation at this time.

**To proceed, the following is needed:**

- A prospective clinical trial evaluating Enalapril (or a class-representative ACE inhibitor) specifically in COPD-related cor pulmonale with adequate sample size (minimum n ≥ 100)
- Confirmation of drug access pathway in Australia via TGA SAS, Authorised Prescriber, or substitution with a registered ACE inhibitor
- Retrieval of DrugBank MOA data to formally document the mechanistic rationale in the evidence dossier
- Review of safety profile specific to pulmonary heart disease patients, particularly regarding right heart haemodynamic monitoring and renal function during therapy initiation
- TFDA/TGA Product Information review for drug-specific warnings and contraindications, including bilateral renal artery stenosis (known ACE inhibitor class contraindication) and pregnancy

---

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All treatment decisions should be made in accordance with TGA-approved indications and current clinical guidelines.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

