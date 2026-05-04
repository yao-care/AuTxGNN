---
layout: default
title: Epoprostenol
parent: 僅模型預測 (L5)
nav_order: 197
evidence_level: L5
indication_count: 10
---

# Epoprostenol
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

# Epoprostenol: From Pulmonary Arterial Hypertension to Respiratory Failure

## One-Sentence Summary

Epoprostenol (prostacyclin, PGI₂) is an established prostanoid therapy internationally approved for pulmonary arterial hypertension (PAH), though it is not currently registered with the TGA and has no ARTG entries in Australia.

The TxGNN model generated 10 predicted new indications; notably, the highest-scoring predictions (Ranks 1–8) are headache-related conditions — however, existing clinical evidence strongly indicates that epoprostenol **triggers** rather than treats headache disorders, representing a clinically important reversal of the repurposing hypothesis that clinicians must be aware of.

The most actionable repurposing opportunity is **Respiratory Failure** (inhaled route, TxGNN Rank 9, score 77.74%), supported by **L1-level evidence** including multiple completed clinical trials and 20 publications, earning a **"Proceed with Guardrails"** recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pulmonary Arterial Hypertension (PAH) — not TGA-registered; 0 ARTG entries |
| Primary Actionable New Indication | Respiratory Failure (acute / ARDS context, inhaled administration) |
| TxGNN Score — Top Prediction | 98.41% (Trigeminal Autonomic Cephalalgia, Rank 1) ⚠️ Reverse evidence — epoprostenol triggers headache |
| TxGNN Score — Respiratory Failure | 77.74% (Rank 9) |
| Evidence Level | L1 (Respiratory Failure) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | **Proceed with Guardrails** (Respiratory Failure) · **Hold** (all headache-related predictions, Ranks 1–8) |

---

## ⚠️ Critical Clinical Alert: TxGNN Headache Predictions — Reverse Evidence

The TxGNN model's top 8 predictions are dominated by headache-related conditions (trigeminal autonomic cephalalgia, headache disorder, migraine with brainstem aura, migraine disorder). **The weight of clinical evidence directly contradicts a therapeutic role in these conditions:**

- **PMID 19614689** (RCT/Provocation Study, *Cephalalgia*, 2010): IV epoprostenol (10 ng/kg/min over 25 min) **triggered migraine-like attacks in 11 of 12 migraineurs** in a placebo-controlled crossover design — direct clinical proof that PGI₂ is a headache *precipitant*, not a treatment.
- **NCT00291395** (Phase 1, Terminated): Designed explicitly to study PGI₂-*induced* headache and cerebral haemodynamics.
- **NCT00510172** (Status Unknown): Studies the migraine-*inducing* effects and brain haemodynamic changes of PGI₂.

The high TxGNN scores for headache conditions reflect **pathophysiological network proximity** (PGI₂ is mechanistically involved in headache as a vascular trigger via IP receptor–mediated meningeal vasodilation) rather than therapeutic efficacy. **Do not pursue headache or migraine indications without compelling new mechanistic evidence that contradicts the current clinical data.**

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this Evidence Pack. Based on established pharmacological knowledge, epoprostenol is a synthetic analogue of naturally occurring prostacyclin (PGI₂), produced by vascular endothelium. It acts primarily on IP (prostacyclin) receptors, exerting **pulmonary vasodilation**, **platelet anti-aggregation**, and **endothelial cytoprotection**. When delivered via inhalation, epoprostenol achieves **selective pulmonary vasodilation** with minimal systemic haemodynamic effects — a critical advantage in critically ill patients.

In acute respiratory failure (including ARDS), the core pathophysiology involves ventilation-perfusion (V/Q) mismatch: pulmonary perfusion continues to poorly ventilated or collapsed lung units, causing profound hypoxaemia. Inhaled epoprostenol preferentially vasodilates pulmonary vessels in well-ventilated regions, redistributing blood flow away from shunt-prone areas and thereby improving V/Q matching and arterial oxygenation. This mechanism is already well-validated in PAH and translates directly to the ARDS and post-cardiac surgery right ventricular failure contexts.

Importantly, the repurposing from PAH to respiratory failure represents primarily a **route-of-administration shift** (inhaled versus intravenous) combined with a clinical context shift (chronic vs acute disease). Evidence from COVID-19 ARDS, post-transplant right heart failure, and general ARDS supports this translation across multiple Phase 2–4 clinical trials and observational studies. The TxGNN model's prediction, while lower-ranked by score, aligns well with established pharmacological rationale.

---

## Clinical Trial Evidence

*The following trials relate to Respiratory Failure (Rank 9 — the primary actionable indication).*

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT04452669](https://clinicaltrials.gov/study/NCT04452669) | Phase 2 | Completed | 11 | Double-blind, placebo-controlled RCT of VentaProst (inhaled epoprostenol via dedicated breath-actuated delivery system) in COVID-19 patients requiring mechanical ventilation — directly evaluates efficacy and safety in acute respiratory failure |
| [NCT01717209](https://clinicaltrials.gov/study/NCT01717209) | Phase 4 | Completed | 14 | RCT evaluating individual and combined effects of inhaled nitric oxide (iNO) and inhaled prostacyclin (iPGI₂) after cardiac transplantation or LVAD placement — assesses right ventricular function and pulmonary pressures in acute post-surgical respiratory failure |
| [NCT00159861](https://clinicaltrials.gov/study/NCT00159861) | Phase 3 | Completed | 267 | Multinational, multicentre, double-blind, placebo-controlled RCT of sildenafil + IV epoprostenol combination in PAH — highest-quality (L1) evidence directly supporting epoprostenol's pulmonary vasodilatory mechanism and tolerability |
| [NCT02170519](https://clinicaltrials.gov/study/NCT02170519) | Phase 4 | Terminated | 27 | Inhaled aerosolised prostacyclin as potential replacement for inhaled NO in acute secondary pulmonary hypertension — relevant design (n=27) but terminated before completion; data limited |
| [NCT03111212](https://clinicaltrials.gov/study/NCT03111212) | Phase 3 | Completed | 150 | ThIlo-Trial: nebulised iloprost (prostacyclin analogue) as inhalative therapy in ARDS — supports class-level evidence for inhaled prostanoids in acute respiratory failure |
| [NCT04420741](https://clinicaltrials.gov/study/NCT04420741) | Phase 2 | Completed | 80 | IV iloprost (prostacyclin analogue) vs placebo for 72 hours in COVID-19 respiratory failure — tests endothelial rescue treatment hypothesis; supports mechanistic rationale |

---

## Literature Evidence

*The following publications relate to Respiratory Failure (Rank 9 — the primary actionable indication).*

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [40513981](https://pubmed.ncbi.nlm.nih.gov/40513981/) | 2025 | Review | *Pulmonary Pharmacology & Therapeutics* | Comprehensive review of inhaled epoprostenol pharmacology and clinical application in acute respiratory failure and pulmonary vascular disease; synthesises current evidence for cardiopulmonary use |
| [37401479](https://pubmed.ncbi.nlm.nih.gov/37401479/) | 2023 | Comparative Study | *Circulation* | Head-to-head comparison of inhaled epoprostenol vs inhaled NO for right ventricular failure prevention and treatment after major cardiac surgery (heart transplantation and LVAD); supports epoprostenol as an effective alternative to iNO |
| [35952768](https://pubmed.ncbi.nlm.nih.gov/35952768/) | 2022 | Observational Target Trial | *Chest* | Target trial emulation comparing inhaled NO vs inhaled epoprostenol in mechanically ventilated patients with severe acute respiratory failure; provides comparative effectiveness data |
| [36158384](https://pubmed.ncbi.nlm.nih.gov/36158384/) | 2022 | Comparative Study | *Cureus* | Direct comparison of inhaled epoprostenol outcomes in traditional ARDS vs COVID-19-associated ARDS — explores disease-specific response differences |
| [35274053](https://pubmed.ncbi.nlm.nih.gov/35274053/) | 2022 | Review | *J Crit Care Med (Targu-Mures)* | Review and case series of inhaled epoprostenol for ARDS secondary to COVID-19 — documents clinical practice experience |
| [33234007](https://pubmed.ncbi.nlm.nih.gov/33234007/) | 2021 | Cohort/Case Series | *J Intensive Care Medicine* | Assessment of physiologic responsiveness to inhaled epoprostenol in COVID-19 respiratory failure — identifies characteristics of responders vs non-responders |
| [31729256](https://pubmed.ncbi.nlm.nih.gov/31729256/) | 2020 | Observational Cohort | *Annals of Pharmacotherapy* | Retrospective matched cohort comparing inhaled Flolan vs Veletri in ARDS — evaluates effectiveness, safety, and economic outcomes of formulation switch |
| [38854955](https://pubmed.ncbi.nlm.nih.gov/38854955/) | 2024 | Case Report/Safety | *Pulmonary Circulation* | First reported case of life-threatening bronchospasm and acute respiratory failure associated with inhaled prostacyclin administration — critical safety signal for pre-screening of reactive airway disease |
| [38516615](https://pubmed.ncbi.nlm.nih.gov/38516615/) | 2023 | Observational | *CHEST Critical Care* | Inhaled epoprostenol via humidified high-flow nasal cannula in non-intubated COVID-19 patients associated with progressive respiratory failure — important caution regarding non-invasive delivery route |
| [35787522](https://pubmed.ncbi.nlm.nih.gov/35787522/) | 2022 | RCT Protocol | *BMJ Open Respiratory Research* | TETON Phase 3 trial design for inhaled treprostinil in idiopathic pulmonary fibrosis — supports class-level evidence for inhaled prostanoid efficacy extending beyond PAH |

---

## Australia Market Information

Epoprostenol is **not currently registered with the TGA** and has no ARTG entries. It is not available through standard commercial channels in Australia.

Epoprostenol is available internationally under brand names including **Flolan®** (GlaxoSmithKline) and **Veletri®** (Actelion/Janssen), both approved by the US FDA and EMA for PAH. Australian clinicians requiring access should consider:

- **TGA Special Access Scheme (SAS Category B)** — for individual patients with serious or life-threatening conditions
- **Authorised Prescriber (AP) pathway** — for ongoing prescribing in a specific patient population
- **Compounding pharmacy** — IV epoprostenol has been prepared under specialist supervision in some Australian ICU settings

Note: The inhaled delivery formulation (e.g., VentaProst® dedicated nebuliser system) adds a device-level regulatory consideration beyond the drug product itself.

---

## Safety Considerations

Please refer to international Product Information (PI) documents for Flolan® and Veletri® for comprehensive safety information, as no TGA-approved PI exists for epoprostenol in Australia.

**The following safety signals are identified from available literature:**

- **Bronchospasm risk**: A case of life-threatening bronchospasm and acute respiratory failure has been reported with inhaled prostacyclin (PMID 38854955, 2024). Pre-treatment assessment for reactive airway disease is strongly recommended before initiating inhaled epoprostenol.
- **Non-invasive route caution**: Use via humidified high-flow nasal cannula in non-intubated COVID-19 patients was associated with progressive respiratory failure in one observational study (PMID 38516615). This route should be used with close monitoring and caution.
- **Known systemic effects (IV route)**: Flushing, hypotension, headache, jaw pain, nausea, and diarrhoea — generally attenuated with inhaled administration.
- **Drug interaction data**: No DDI data was retrievable for this report. Pharmacist consultation is recommended prior to initiation, particularly in patients receiving anticoagulants, antihypertensives, or other vasodilators.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(for Respiratory Failure — inhaled epoprostenol)*

**Rationale:**
Inhaled epoprostenol has a mechanistically coherent rationale, L1-level clinical evidence, and a well-established international clinical practice base for use in acute respiratory failure (ARDS, post-cardiac surgery right ventricular failure, COVID-19-associated hypoxaemia). The primary barriers to use in Australia are the absence of TGA registration and the need for appropriate inhaled delivery infrastructure, rather than a lack of clinical evidence.

**To proceed, the following is needed:**

- **TGA access**: Initiate SAS Category B application or Authorised Prescriber pathway for individual patient or institutional access
- **MOA documentation**: Obtain full DrugBank pharmacology profile for regulatory submission support
- **International PI review**: Obtain and review US FDA-approved PI for Flolan® and Veletri® to confirm contraindications, warnings, and dosing protocols
- **Delivery system confirmation**: Verify availability of appropriate nebuliser/inhalation delivery device (standard ICU jet nebuliser or dedicated VentaProst® system) at the clinical site
- **DDI assessment**: Full drug interaction profile not available — formal pharmacist or clinical pharmacologist review required before use in polypharmacy ICU patients
- **Clinical monitoring protocol**: Establish clear parameters including SpO₂, PaO₂/FiO₂ ratio, pulmonary artery pressures (where available), systemic blood pressure, and airway reactivity monitoring

---

**Note on rejected predictions (Ranks 1–8, headache-related):**
Despite high TxGNN prediction scores (82–98%), all headache-related indications carry a **Hold** recommendation. RCT-level and provocation study evidence confirms that epoprostenol triggers rather than treats migraine and related headache disorders through IP receptor–mediated meningeal vasodilation. These indications should not be pursued for repurposing unless compelling new mechanistic evidence — such as subtype-specific receptor profiling or dose-range findings — overturns the current body of evidence.

> **Disclaimer**: This report is intended for research purposes only and does not constitute medical advice. Drug repurposing candidates require formal clinical validation before therapeutic application. All prescribing decisions should comply with Australian regulatory requirements.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

