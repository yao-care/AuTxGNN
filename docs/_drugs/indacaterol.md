---
layout: default
title: Indacaterol
parent: High Evidence (L1-L2)
nav_order: 348
evidence_level: L1
indication_count: 10
---

# Indacaterol
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Indacaterol: From COPD/Asthma Maintenance Therapy to Bronchial Disease (Broad Indication Expansion)

## One-line Summary

Indacaterol is a long-acting beta-2 adrenergic receptor agonist (LABA) with known clinical use mechanisms for COPD/asthma maintenance therapy as a bronchodilator component; however, it is **not yet marketed in Taiwan** (no TFDA approval number). The TxGNN model identifies 10 predicted new indications for this drug, of which only **"bronchial disease"** has substantial support—**37 clinical trials** and **20 literature reports**, with multiple Phase 3 large-scale controlled trials; the remaining 9 predicted indications, while scoring high, lack clinical trial or literature evidence, and some mechanistic directions contradict known pharmacological action.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Data gap (Taiwan: Not marketed, no TFDA approval record; mechanistic description within evidence package indicates international approval for COPD/asthma maintenance therapy) |
| Predicted New Indication | Bronchial disease |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L1 |
| Taiwan Market Status | Not marketed |
| TFDA Approval Number | 0 |
| Recommended Decision | Proceed with Guardrails |

> Note: The first-ranked prediction by TxGNN score is "nephrogenic syndrome of inappropriate antidiuresis" (99.54% score), but that candidate has no clinical trials or literature support, and the model's own mechanistic reasoning explicitly indicates no relationship to β2 agonist mechanism (see "Other Predicted Indications" at end of report). This report uses **the highest evidence level indication with actual decision value—"bronchial disease"—as the primary assessment target**.

---

## Why Is This Prediction Reasonable?

Currently, there is no complete mechanism of action (MOA) structured data available (DrugBank query field represents a data gap). However, based on the mechanistic description in the evidence package, indacaterol is a **long-acting beta-2 adrenergic receptor agonist (LABA)**, which promotes bronchial dilation by activating β2 receptors on airway smooth muscle. This mechanism is already the clinical application foundation for its international approval for COPD and asthma maintenance therapy.

"Bronchial disease" is a broad respiratory indication classification that significantly overlaps with indacaterol's existing COPD/asthma indications in pathophysiology; therefore, the TxGNN prediction has direct, explicit pharmacological correspondence in mechanism, not a cross-system novel linkage. In other words, this prediction is more akin to a **classification expansion confirmation of existing approved use** rather than traditional "drug repurposing." Consequently, while evidence strength is high (L1), clinical novelty is limited, and actual benefit depends on whether this classification corresponds to specific indication subcategories not yet covered in Taiwan.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolled N | Key Findings |
|---------------|-------|--------|------------|--------------|
| [NCT02554786](https://clinicaltrials.gov/study/NCT02554786) | Phase 3 | Completed | 2216 | Comparison of two doses of QMF149 (indacaterol/mometasone) vs. mometasone monotherapy regarding efficacy and safety in patients with uncontrolled asthma |
| [NCT02571777](https://clinicaltrials.gov/study/NCT02571777) | Phase 3 | Completed | 3092 | Comparison of QVM149 (indacaterol/glycopyrronium/mometasone triple combination) vs. two doses of QMF149 regarding efficacy and safety |
| [NCT00529529](https://clinicaltrials.gov/study/NCT00529529) | Phase 3 | Completed | 805 | Salmeterol as active comparator; safety evaluation of indacaterol 300/600 µg over 26 weeks in patients with moderate-to-severe persistent asthma |
| [NCT03158311](https://clinicaltrials.gov/study/NCT03158311) | Phase 3 | Completed | 1426 | QVM149 vs. salmeterol/fluticasone + tiotropium free combination therapy; demonstrated non-inferiority |
| [NCT01079130](https://clinicaltrials.gov/study/NCT01079130) | Phase 3 | Completed | 511 | Randomized, double-blind trial with salmeterol as active comparator; evaluated bronchodilation efficacy of indacaterol at day 14 |
| [NCT00941798](https://clinicaltrials.gov/study/NCT00941798) | Phase 2 | Completed | 2283 | Safety comparison of QMF149 vs. mometasone monotherapy; event-driven trial assessing severe asthma exacerbation incidence |
| [NCT01609478](https://clinicaltrials.gov/study/NCT01609478) | Phase 2 | Completed | 335 | 12-week dose exploration trial supporting fixed-dose combination selection for QMF149 |
| [NCT05562466](https://clinicaltrials.gov/study/NCT05562466) | Phase 3 | Recruiting | 200 | QMF149 vs. budesonide regarding efficacy and safety in children aged 6–12 years with asthma |
| [NCT02892019](https://clinicaltrials.gov/study/NCT02892019) | Phase 2 | Completed | 79 | Evaluation of indacaterol acetate regarding lung function and systemic exposure in children aged 6–12 years with asthma |
| [NCT02059434](https://clinicaltrials.gov/study/NCT02059434) | Phase 1 | Completed | 55 | Preliminary safety, tolerability, and pharmacodynamic evaluation of inhaled bronchodilator in asthma and COPD patients |

---

## Literature Evidence

| PMID | Year | Study Type | Journal | Key Findings |
|------|------|-----------|---------|--------------|
| [32653074](https://pubmed.ncbi.nlm.nih.gov/32653074/) | 2020 | RCT (Phase 3) | Lancet Respir Med | IRIDIUM trial: once-daily mometasone-indacaterol-glycopyrronium triple combination vs. dual combination or twice-daily fluticasone-salmeterol in patients with uncontrolled asthma |
| [33711782](https://pubmed.ncbi.nlm.nih.gov/33711782/) | 2021 | Meta-analysis (Phase 3) | Respir Med | Meta-analysis of multiple Phase 3 trials assessing cardiovascular safety of mometasone/indacaterol and triple combination regimens |
| [28768531](https://pubmed.ncbi.nlm.nih.gov/28768531/) | 2017 | RCT (crossover) | Respir Res | Three-way crossover trial evaluating effects of glycopyrronium and indacaterol monotherapy and combination on methacholine dose-response curve in patients with mild asthma |
| [35348408](https://pubmed.ncbi.nlm.nih.gov/35348408/) | 2023 | Open-label long-term safety study | J Asthma | Two 52-week open-label studies assessing long-term safety of IND/GLY/MF high-dose in Japanese asthma patients |
| [34329722](https://pubmed.ncbi.nlm.nih.gov/34329722/) | 2021 | Pharmacokinetic bridge study | Pulm Pharmacol Ther | Bridging data for mometasone dose between MF/IND and MF/IND/GLY fixed-dose combinations |
| [33871819](https://pubmed.ncbi.nlm.nih.gov/33871819/) | 2021 | Review | Drugs | Comprehensive review of indacaterol/glycopyrronium/mometasone (Enerzair) in asthma treatment |
| [19609496](https://pubmed.ncbi.nlm.nih.gov/19609496/) | 2009 | Review | Adv Ther | Review of preclinical and clinical data on indacaterol as a novel once-daily LABA in obstructive airway disease treatment |
| [39905183](https://pubmed.ncbi.nlm.nih.gov/39905183/) | 2025 | Systematic review and meta-analysis | Sci Rep | Comparison of relative efficacy of different triple therapies in patients with uncontrolled asthma |
| [35072888](https://pubmed.ncbi.nlm.nih.gov/35072888/) | 2022 | Review | Adv Ther | Review of development strategy for IND/GLY/MF, the first-in-class once-daily triple fixed-dose combination |
| [31425937](https://pubmed.ncbi.nlm.nih.gov/31425937/) | 2019 | Review | Respir Med | Review of the role of ultra-LABA (including indacaterol) in asthma treatment |

---

## Taiwan Market Information

No TFDA-approved indacaterol marketing authorization has been identified (`total_licenses = 0`); Taiwan market status is **Not marketed**. This is a data gap that requires priority completion before proceeding to the next evaluation stage (see Conclusion).

---

## Safety Considerations

Please consult the TFDA-approved product package insert (PI) for safety information. Currently, data on package insert warnings, contraindications, and drug-drug interactions (DDI) are not available; this is a blocking-level data gap that must be completed at the next stage before preliminary safety assessment can be conducted.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The "bronchial disease" prediction has substantial support from multiple completed Phase 3 large-scale controlled trials and 20 literature reports (L1), with clear mechanistic reasonableness; however, this indication classification has high overlap with indacaterol's existing LABA-approved uses, with limited clinical novelty. Additionally, since it is currently not marketed in Taiwan with all safety package insert data missing, completion is necessary before formal safety preliminary assessment can proceed.

**Required completion before advancement:**
- TFDA package insert warnings and contraindications data (Blocking, DG001)
- Complete DrugBank mechanism of action (MOA) data (High, DG002)
- Tracking of Taiwan market application status (currently 0 approved numbers)
- Clarification of the actual added clinical value of "bronchial disease" as a broad classification relative to current COPD/asthma indications

---

### Note: Other TxGNN Predicted Indications (Insufficient Evidence, Hold)

The following 9 candidate indications, although scoring similarly or higher to "bronchial disease" by TxGNN, lack clinical trial or literature support, evidence level L5, and are recommended to be **held**:

| Rank | Predicted Indication | TxGNN Score | Mechanistic Reasonableness Summary |
|------|--------|----------|-----------|
| 1 | Nephrogenic syndrome of inappropriate antidiuresis | 99.54% | V2 receptor gene mutation disease; unrelated to β2 agonist mechanism |
| 2 | Headache disorder | 99.53% | Cited trials are actually COPD tolerability studies; headache only a monitored adverse event; β-blockers (not agonists) are the mechanism for migraine prevention, opposite direction |
| 3 | Trigeminal autonomic cephalalgia | 99.33% | No known mechanistic association |
| 4 | Paratenonitis | 99.26% | No known mechanistic association |
| 5 | Calcific tendinitis | 99.25% | No known mechanistic association |
| 6 | Hypertrichosis (disease) | 99.23% | Hypertrichosis mechanism is potassium channel opener, unrelated to β2 agonism |
| 8 | Myositis | 99.12% | No evidence-based support |
| 9 | Anaphylaxis | 99.07% | Anaphylaxis first-line is epinephrine; indacaterol onset and pharmacokinetic properties unsuitable for acute management |
| 10 | Ambras type hypertrichosis universalis congenita | 99.06% | Rare chromosomal rearrangement disease; unrelated to drug pathway |

*This report is for research reference only and does not constitute medical advice; drug repurposing candidates require clinical verification before application.*

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

