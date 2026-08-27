---
layout: default
title: Iloprost
parent: 僅模型預測 (L5)
nav_order: 343
evidence_level: L5
indication_count: 10
---

# Iloprost
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

# Iloprost: From Established Pulmonary Arterial Hypertension Use to PAH Associated with Congenital Heart Disease

*Note on candidate selection: This evidence pack (`TW-DB01088-multi`) scored 10 candidate indications. The two highest-scoring predictions (hypotrichosis simplex of the scalp; congenital hypotrichosis milia) are explicitly flagged in the pack's own rationale as likely knowledge-graph noise (zero trials, zero literature, no mechanistic plausibility). This report instead focuses on the highest-scoring **clinically plausible** candidate — PAH associated with congenital heart disease — and summarises four related PAH-subtype predictions below it. Diseases judged as noise are listed at the end for completeness.*

---

## One-Sentence Summary

Iloprost is a prostacyclin (PGI2) analogue; a formal record of its original approved indication is not available in this evidence pack, but its established pharmacological role — described consistently throughout the evidence — is pulmonary vasodilation in pulmonary arterial hypertension (PAH). The TxGNN model predicts efficacy in **PAH associated with congenital heart disease**, a recognised PAH subtype, with **1 clinical trial** and **20 publications** currently identified. Four related PAH-subtype predictions (connective tissue disease, HIV infection, schistosomiasis, chronic haemolytic anaemia) carry similar or lower evidence support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in this evidence pack (data gap); established use elsewhere is pulmonary arterial hypertension, per rationale notes across multiple predicted indications |
| Predicted New Indication | Pulmonary arterial hypertension associated with congenital heart disease |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L2 |
| Australia Market Status | Not currently marketed (未上市) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is marked as a data gap in the structured drug record. However, the evidence pack's repurposing rationale consistently describes Iloprost as a **prostacyclin (PGI2) analogue** that activates the IP receptor, producing pulmonary vasodilation and inhibiting platelet aggregation — the standard mechanistic basis for PAH (WHO Group 1) therapy.

PAH associated with congenital heart disease (including Eisenmenger physiology) is classified as a clinical subtype within the same WHO Group 1 PAH family as idiopathic PAH. The rationale explicitly frames this as **an extension within an existing indication class rather than a novel mechanistic hypothesis** — the underlying pulmonary vascular pathology (vasoconstriction, remodelling, elevated pulmonary vascular resistance) is shared across subtypes, which is why prostacyclin analogues are used across the WHO Group 1 spectrum in practice.

This mechanistic continuity also explains why several other WHO Group 1 subtypes appear as related high-scoring predictions in this pack (connective tissue disease-associated, HIV-associated, schistosomiasis-associated, and chronic haemolytic anaemia-associated PAH) — they are pathophysiological variants of the same disease category rather than unrelated indications.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01383083](https://clinicaltrials.gov/study/NCT01383083) | N/A | Unknown | 42 | Assessed safety, tolerability, and haemodynamic effects of Iloprost in adults with PAH related to congenital heart disease (Eisenmenger physiology); addresses a rare, complex population with limited prior treatment evidence. |

No ANZCTR-registered trials were identified for this indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28608969](https://pubmed.ncbi.nlm.nih.gov/28608969/) | 2017 | Cohort/Biomarker study | Clin Exp Pharmacol Physiol | Investigated endothelial biomarkers (NO, ET-1, ADMA, Gal-3, BNP, UA) in CHD-PAH and the effect of Iloprost on their regulation. |
| [29426959](https://pubmed.ncbi.nlm.nih.gov/29426959/) | 2018 | Interventional acute-response study (paediatric) | Pediatr Cardiol | Evaluated safety and acute haemodynamic effects of inhaled Iloprost during cardiac catheterisation in children with PAH-CHD. |
| [27053694](https://pubmed.ncbi.nlm.nih.gov/27053694/) | 2016 | Cohort / expert consensus | Heart | European consensus on haemodynamic assessment and acute pulmonary vasoreactivity testing in paediatric pulmonary vascular disease, including CHD-associated PAH. |
| [19436672](https://pubmed.ncbi.nlm.nih.gov/19436672/) | 2009 | Review | Vasc Health Risk Manag | Reviews inhaled Iloprost use for pulmonary artery hypertension control in children, including CHD-associated cases. |
| [16919006](https://pubmed.ncbi.nlm.nih.gov/16919006/) | 2006 | Review | Eur J Clin Invest | Overview of treatment options in paediatric PAH, noting congenital heart disease as a leading cause. |
| [25316472](https://pubmed.ncbi.nlm.nih.gov/25316472/) | 2014 | Case report | Saudi Med J | Complete resolution of chronic pericardial effusion with intensive inhaled Iloprost in an adult with unrepaired VSD and severe PAH. |
| [15929625](https://pubmed.ncbi.nlm.nih.gov/15929625/) | 2005 | Review | Rev Port Cardiol | Discusses new PAH drug classes, including prostacyclin analogues, applied to Eisenmenger syndrome and other CHD-related PAH. |
| [30719004](https://pubmed.ncbi.nlm.nih.gov/30719004/) | 2018 | Prospective cohort (cardiac MRI) | Front Pharmacol | Acute inhaled Iloprost improved right ventricular function in PAH patients on cardiac magnetic resonance imaging. |
| [24729548](https://pubmed.ncbi.nlm.nih.gov/24729548/) | 2015 | Retrospective study | Pediatr Pulmonol | Long-term effects of inhaled Iloprost analysed in children with pulmonary hypertension, a population overlapping with CHD-PAH. |
| [21852894](https://pubmed.ncbi.nlm.nih.gov/21852894/) | 2009 | Review | Prog Pediatr Cardiol | Discusses paediatric PAH aetiologies beyond congenital heart disease, providing differential context for CHD-PAH management. |

---

## Australia Market Information

Iloprost has **no ARTG-registered products in Australia** (0 entries on record; market status: not currently marketed).

---

## Additional Related Predictions (Same PAH Family)

The following WHO Group 1 PAH subtypes were also predicted with similar TxGNN scores and share the same mechanistic rationale as the lead candidate above:

| Disease | TxGNN Score | Evidence Level | Recommendation | Evidence Summary |
|---|---|---|---|---|
| PAH associated with connective tissue disease | 99.21% | L3 | Proceed with Guardrails | 0 trials; 20 publications (mostly reviews/cohorts), including long-term IV Iloprost outcomes data |
| PAH associated with HIV infection | 99.21% | L2 | Proceed with Guardrails | 1 completed Phase 3 trial ([NCT00709956](https://clinicaltrials.gov/study/NCT00709956), PROWESS-15, n=64; HIV-PAH was a sub-population, not the sole enrolment criterion); 4 publications |
| Pulmonary arteriovenous malformation | 99.31% | L4 | Research Question | 0 trials; 1 publication; structural (not vasoconstrictive) pathology — mechanistic link is weak |
| PAH associated with schistosomiasis | 99.21% | L4 | Research Question | 0 trials; 1 publication (not schistosomiasis-specific) |

**Excluded as likely model noise (no supporting evidence, Hold recommendation):** hypotrichosis simplex of the scalp, congenital hypotrichosis milia, PAH associated with chronic haemolytic anaemia, diffuse alopecia areata, alopecia.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Iloprost's prostacyclin mechanism is well established for PAH broadly, and PAH-CHD is a recognised subtype rather than a novel indication hypothesis — but the sole disease-specific trial identified has unknown status and unspecified phase, and Iloprost is not currently registered in Australia, so clinical use here would be off-label/unregistered pending further evaluation.

**To proceed, the following is needed:**
- TGA/PI-equivalent safety, warnings, and contraindication data (currently a blocking data gap)
- Formal mechanism-of-action and original-indication documentation for the drug record
- Confirmation of trial phase/status for NCT01383083, or identification of more definitive PAH-CHD trials
- ARTG registration pathway assessment, given the drug is not currently marketed in Australia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

