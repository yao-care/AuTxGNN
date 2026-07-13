---
layout: default
title: Ipratropium
parent: 僅模型預測 (L5)
nav_order: 272
evidence_level: L5
indication_count: 10
---

# Ipratropium
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

# Ipratropium: From Bronchospasm to Obstructive Lung Disease

## One-Sentence Summary

Ipratropium bromide is an anticholinergic bronchodilator globally recognised as a cornerstone treatment for bronchospasm and chronic obstructive pulmonary disease (COPD).
The TxGNN model predicts — with very high confidence (99.97%) — its effectiveness for **Obstructive Lung Disease**, supported by **50 clinical trials** and **20 publications** in the current Evidence Pack, validating this established clinical application.
This finding represents confirmation of an existing therapeutic role rather than a novel drug repurposing.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not formally recorded in current dataset (globally established for COPD / bronchospasm) |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed (see data note below) |
| Number of ARTG Entries | 0 (probable data collection gap — verify via TGA ARTG) |
| Recommended Decision | Proceed with Guardrails |

> **Data Note:** Ipratropium bromide (Atrovent®) is an internationally available registered bronchodilator. The "0 ARTG entries" result almost certainly reflects an incomplete regulatory data collection pipeline rather than actual non-registration in Australia. Independent verification via the [TGA ARTG public search](https://www.tga.gov.au/resources/artg) is strongly recommended before clinical use.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not retrieved from DrugBank in this Evidence Pack. Based on extensive published literature, however, ipratropium bromide is a synthetic quaternary isopropyl derivative of atropine that acts as a competitive antagonist at muscarinic acetylcholine receptors — primarily M1 and M3 subtypes — on bronchial smooth muscle and submucosal glands. It interrupts vagally mediated bronchoconstriction by blocking the cyclic guanosine 3',5'-monophosphate (cGMP) system at parasympathetic nerve endings, and reduces pathological mucus hypersecretion — both of which are hallmarks of obstructive lung disease.

The link between ipratropium and obstructive lung disease is the most direct pharmacological relationship in this Evidence Pack. In COPD, increased cholinergic tone is a key reversible driver of airflow obstruction. Ipratropium produces dose-dependent bronchodilation as measured by improvements in FEV₁ and FVC, with a slower onset but more sustained effect than many short-acting beta-2 agonists. The drug is typically administered as a metered-dose inhaler (MDI) or nebuliser solution and has been used globally since the 1980s, both as monotherapy and in fixed-dose combination with salbutamol (Combivent®).

The TxGNN score of 99.97% correctly identifies this established application. The evidence base is exceptional in both depth and quality: Cochrane systematic reviews comparing ipratropium against placebo and active comparators, the landmark multi-year Lung Health Study Phase 3 RCT, multiple large-enrolment Phase 3 head-to-head trials (against tiotropium and indacaterol), and post-marketing surveillance programmes enrolling over 4,000 patients collectively confirm L1-level evidence. This report provides a structured summary of that evidence base for Australian healthcare decision-making.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT00000568](https://clinicaltrials.gov/study/NCT00000568) | Phase 3 | Completed | N/A | **Lung Health Study I & III**: Landmark long-term Phase 3 RCT assessing ipratropium's effect on rate of FEV₁ decline, smoking cessation, and cardiopulmonary morbidity/mortality in early COPD — highest-grade direct evidence for the drug |
| [NCT00846586](https://clinicaltrials.gov/study/NCT00846586) | Phase 3 | Completed | 1,134 | Double-blind 12-week RCT: indacaterol 150 µg od + tiotropium vs tiotropium alone in moderate-to-severe COPD; contextualises the role of anticholinergic agents in combination bronchodilator strategies |
| [NCT00400153](https://clinicaltrials.gov/study/NCT00400153) | Phase 3 | Completed | 1,480 | Combivent Respimat® (ipratropium 20 µg / salbutamol 100 µg) non-inferiority vs Combivent® CFC-MDI over 12 weeks in COPD; primary endpoint FEV₁ AUC 0–6 hours |
| [NCT02233881](https://clinicaltrials.gov/study/NCT02233881) | N/A | Completed | 4,222 | German post-marketing surveillance of Atrovent® Inhalets in COPD: large real-world tolerability and efficacy dataset under daily practice conditions |
| [NCT02172469](https://clinicaltrials.gov/study/NCT02172469) | Phase 3 | Completed | 215 | Double-blind double-dummy RCT: tiotropium 18 µg od vs Atrovent® MDI 20 µg qid in Filipino COPD patients; direct ipratropium bronchodilator efficacy and safety data as active comparator |
| [NCT00274040](https://clinicaltrials.gov/study/NCT00274040) | Phase 3 | Completed | 141 | Double-blind double-dummy RCT: tiotropium 18 µg od vs ipratropium MDI 20 µg qid in COPD; confirms ipratropium's bronchodilator efficacy with direct head-to-head data |
| [NCT01019694](https://clinicaltrials.gov/study/NCT01019694) | Phase 3 | Completed | 470 | Long-term safety and patient acceptability study: Combivent Respimat® vs Combivent® CFC-MDI vs free combination Atrovent® HFA + albuterol HFA; supports device transition for COPD patients |
| [NCT02182713](https://clinicaltrials.gov/study/NCT02182713) | Phase 4 | Completed | 30 | Phase 4 RCT: Combivent® (ipratropium 20 µg + salbutamol 100 µg) vs salbutamol alone in methacholine-induced bronchospasm in atopic asthma; demonstrates additive anticholinergic bronchodilator protection |
| [NCT00117182](https://clinicaltrials.gov/study/NCT00117182) | Phase 2 | Completed | 140 | Phase 2 mechanistic study: mannitol (Aridol™) challenge test to predict inhaled corticosteroid response in COPD, with ipratropium as a treatment component; validates airway hyperresponsiveness assessment tools |
| [NCT02182700](https://clinicaltrials.gov/study/NCT02182700) | Phase 3 | Terminated | 47 | Phase 3 study: Combivent® Aerosol (salbutamol 120 µg + ipratropium 20 µg) via spacer in adults with moderate-to-severe asthma crisis in the emergency department; provides direct bronchodilator efficacy data despite early termination |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38457591](https://pubmed.ncbi.nlm.nih.gov/38457591/) | 2024 | RCT | Medicine | 118 COPD patients: probiotics + budesonide + ipratropium improved FEV₁, FVC, and gut microbiota diversity compared with budesonide + ipratropium alone; supports multi-modal COPD management |
| [8181328](https://pubmed.ncbi.nlm.nih.gov/8181328/) | 1994 | RCT | Chest | **COMBIVENT Study** (85 days, multicentre, double-blind, parallel-group): ipratropium + albuterol combination superior to either agent alone in COPD — landmark fixed-dose combination efficacy trial |
| [7813271](https://pubmed.ncbi.nlm.nih.gov/7813271/) | 1995 | RCT | Chest | Double-blind crossover RCT: pirbuterol vs ipratropium in COPD; compared non-bronchodilator effects on gas exchange and ventilation distribution — demonstrates ipratropium's distinctive ventilation-perfusion profile |
| [20163324](https://pubmed.ncbi.nlm.nih.gov/20163324/) | 2010 | Systematic Review | Expert Opin Drug Metab Toxicol | Comprehensive review of inhaled albuterol, ipratropium, and their combination in COPD: mechanism of action, clinical efficacy, and safety; combination approved >15 years before publication |
| [16856113](https://pubmed.ncbi.nlm.nih.gov/16856113/) | 2006 | Cochrane SR | Cochrane Database Syst Rev | Ipratropium bromide vs long-acting beta-2 agonists (LABAs) in stable COPD: systematic review of RCTs assessing lung function, symptoms, exercise capacity, and quality of life outcomes |
| [26391969](https://pubmed.ncbi.nlm.nih.gov/26391969/) | 2015 | Cochrane SR | Cochrane Database Syst Rev | Tiotropium vs ipratropium bromide in stable COPD (updated Cochrane review): tiotropium superior in exacerbation prevention and lung function; ipratropium confirmed as a clinically meaningful active comparator |
| [24043433](https://pubmed.ncbi.nlm.nih.gov/24043433/) | 2013 | Cochrane SR | Cochrane Database Syst Rev | Tiotropium vs ipratropium bromide in COPD (earlier update): confirms both agents' efficacy and safety profiles across multiple RCTs; supports ipratropium as an evidence-based option in anticholinergic therapy |
| [35616126](https://pubmed.ncbi.nlm.nih.gov/35616126/) | 2022 | Cochrane SR | Cochrane Database Syst Rev | Magnesium sulfate for acute COPD exacerbations: ipratropium included as part of standard care arm across included studies; contextualises anticholinergic therapy within acute COPD management protocols |
| [28461224](https://pubmed.ncbi.nlm.nih.gov/28461224/) | 2017 | Clinical Study | EBioMedicine | Sex-based differences in FEV₁ response to ipratropium using Lung Health Study data in mild-to-moderate COPD: no significant sex differences identified, supporting broad applicability across patient populations |
| [23170031](https://pubmed.ncbi.nlm.nih.gov/23170031/) | 2012 | Clinical Study | Ann Pharmacother | Concomitant ipratropium + tiotropium in COPD: review of available efficacy and safety data for dual anticholinergic regimens — relevant to combination prescribing decisions in refractory cases |

---

## Australia Market Information

No ARTG entries were identified for Ipratropium in the current regulatory dataset.

> **Important:** This finding almost certainly reflects an incomplete data collection pipeline rather than actual non-registration. Ipratropium bromide (Atrovent®) is a long-established bronchodilator with a global registration history. Clinicians should verify current TGA registration, available formulations (MDI, nebuliser solution, nasal spray), and approved indications directly via the [TGA ARTG public search](https://www.tga.gov.au/resources/artg) before prescribing.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for complete safety information, including contraindications, warnings, precautions, and drug interactions.

Two safety issues of particular clinical importance are identified from the literature:

- **Ocular risk**: Ipratropium aerosol and nebuliser therapy may cause acute angle-closure glaucoma if the drug contacts the eyes. Patients should receive education on correct inhaler technique, and nebuliser masks should fit appropriately to prevent ocular exposure — especially important in patients with pre-existing narrow-angle glaucoma or raised intraocular pressure.
- **Rare anaphylaxis**: Severe anaphylactic reactions following ipratropium bromide inhalation have been documented in rare cases (PMID [8449120](https://pubmed.ncbi.nlm.nih.gov/8449120/)). Clinicians should be alert to this possibility and ensure emergency management resources are accessible, particularly in acute settings.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction score of 99.97% for obstructive lung disease validates ipratropium's established role as a first-line anticholinergic bronchodilator in COPD — this is not a novel repurposing finding but a high-confidence confirmation of existing clinical use. Multiple Cochrane systematic reviews, Phase 3 RCTs including the landmark Lung Health Study, large-enrolment head-to-head trials, and post-marketing surveillance data collectively provide L1-level evidence. The primary barriers to clinical deployment in Australia relate to regulatory data gaps in the pipeline, not to evidence quality.

**To proceed, the following is needed:**

- **Verify ARTG registration**: Search the TGA ARTG database to confirm current registration status and available ipratropium formulations in Australia — the "0 entries" in this dataset almost certainly reflects a data collection gap, not actual non-registration
- **Obtain TGA-approved Product Information (PI)**: Review the approved PI for complete contraindications, warnings (including angle-closure glaucoma and rare anaphylaxis risk), dosage forms, and approved indications
- **Confirm DrugBank MOA entry**: The DrugBank API query did not return MOA data for DB00332 in this Evidence Pack — verify M3 muscarinic antagonist classification via a direct DrugBank query to complete the pharmacological profile
- **Check PBS listing**: Determine current Pharmaceutical Benefits Scheme (PBS) status for ipratropium products to assess patient access, out-of-pocket cost, and prescribing restrictions in the Australian community setting
- **Assess combination regimen options**: Review evidence for ipratropium + salbutamol fixed-dose combination (Combivent®), which demonstrates superior bronchodilator efficacy over monotherapy in moderate-to-severe COPD and may be the preferred formulation in practice
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

