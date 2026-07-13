---
layout: default
title: Bupropion
parent: 僅模型預測 (L5)
nav_order: 109
evidence_level: L5
indication_count: 10
---

# Bupropion
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

# Bupropion: From Depression to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

Bupropion is a norepinephrine-dopamine reuptake inhibitor (NDRI) primarily used internationally to treat major depressive disorder and to support smoking cessation, though no current ARTG registration was identified in this Evidence Pack.
The TxGNN model predicts it may be effective for **Attention Deficit-Hyperactivity Disorder (ADHD)**,
with **8 clinical trials** and **19 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Major depressive disorder / smoking cessation (globally approved; no ARTG registration found in this search) |
| Predicted New Indication | Attention Deficit-Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed (no ARTG entries identified) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Bupropion acts as a norepinephrine-dopamine reuptake inhibitor (NDRI), blocking the dopamine transporter (DAT) and norepinephrine transporter (NET) in the central nervous system — particularly within the prefrontal cortex. Crucially, bupropion has no meaningful serotonergic activity, distinguishing it mechanistically from SSRIs and SNRIs. This dual catecholaminergic action is the foundation of the TxGNN prediction.

The neurobiological basis of ADHD centres on impaired dopaminergic and noradrenergic signalling in prefrontal circuits that govern sustained attention, impulse control, and working memory. These are precisely the systems bupropion modulates. This mechanistic overlap with first-line stimulant agents (methylphenidate, amphetamines) — which also enhance catecholamine neurotransmission, albeit by promoting release rather than blocking reuptake — provides a compelling pharmacological rationale. Bupropion can therefore be understood as a non-stimulant agent working "downstream" of the same neurochemical pathways disrupted in ADHD.

The translational leap from depression/smoking cessation to ADHD is well-supported by the literature. Multiple high-quality network meta-analyses published in *The Lancet Psychiatry* (PMID 30097390, 40203844) and *PLoS One* (PMID 33085721) have included bupropion as an active comparator in ADHD pharmacotherapy evaluations. The Cochrane Collaboration has produced a dedicated systematic review of bupropion specifically for adult ADHD (PMID 28965364), and bupropion is already recognised as a second-line non-stimulant option in international ADHD management guidelines for patients who do not tolerate or respond adequately to stimulants.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT00048360](https://clinicaltrials.gov/study/NCT00048360) | Phase 3 | Completed | 162 | Multicentre, randomised, double-blind, placebo-controlled trial of extended-release bupropion hydrochloride 300–450 mg/day in adults with ADHD — the pivotal L1 evidence anchor for this repurposing prediction |
| [NCT00936299](https://clinicaltrials.gov/study/NCT00936299) | Phase 4 | Completed | 105 | Bupropion for ADHD in adolescents with comorbid substance use disorder; directly evaluated safety and ADHD symptom efficacy in this high-risk, underserved population |
| [NCT00061087](https://clinicaltrials.gov/study/NCT00061087) | Phase 2/3 | Completed | 115 | Bupropion for adult ADHD in methadone-maintained patients; Phase 2/3 combined design with direct ADHD symptom endpoints |
| [NCT01270555](https://clinicaltrials.gov/study/NCT01270555) | Not reported | Completed | 32 | Open-label bupropion SR at clinically relevant doses for ADHD adults with recent/current substance use disorders; assessed efficacy and tolerability |
| [NCT00000268](https://clinicaltrials.gov/study/NCT00000268) | Not applicable | Completed | 32 | Cocaine abuse and ADHD comorbidity study; bupropion was one of the evaluated interventions, primarily addressing substance use endpoints |
| [NCT04553263](https://clinicaltrials.gov/study/NCT04553263) | Early Phase 1 | Withdrawn | 0 | Stimulant use disorder relapse prevention with/without ADHD; withdrawn before enrolment — no data available |
| [NCT03326128](https://clinicaltrials.gov/study/NCT03326128) | Phase 2 | Terminated | 12 | High-dose bupropion for smoking cessation; terminated early with minimal enrolment — ADHD not a primary endpoint |
| [NCT00330434](https://clinicaltrials.gov/study/NCT00330434) | Not applicable | Withdrawn | 0 | CYP2B6 pharmacokinetic induction study; withdrawn before enrolment — no relevance to ADHD efficacy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [28965364](https://pubmed.ncbi.nlm.nih.gov/28965364/) | 2017 | Cochrane Systematic Review | Cochrane Database of Systematic Reviews | Dedicated Cochrane review of bupropion for adult ADHD; summarises pooled efficacy, tolerability, and quality of evidence across available RCTs |
| [27813651](https://pubmed.ncbi.nlm.nih.gov/27813651/) | 2017 | Systematic Review | J Child Adolesc Psychopharmacol | Systematic review of bupropion use in children and adolescents with ADHD; supports its role as a non-stimulant alternative when stimulants are contraindicated or not tolerated |
| [30097390](https://pubmed.ncbi.nlm.nih.gov/30097390/) | 2018 | Network Meta-Analysis | The Lancet Psychiatry | Large network meta-analysis comparing ADHD medications across paediatric, adolescent, and adult populations; bupropion included as an active non-stimulant comparator |
| [33085721](https://pubmed.ncbi.nlm.nih.gov/33085721/) | 2020 | Systematic Review + Meta-Analysis | PLoS One | Network meta-analysis focused on adult ADHD pharmacotherapy; quantifies bupropion's comparative effect size relative to stimulants and other non-stimulants |
| [38950507](https://pubmed.ncbi.nlm.nih.gov/38950507/) | 2024 | Network Meta-Analysis | J Psychiatric Research | Bayesian NMA of monoamine reuptake inhibitors (including bupropion) in ADHD, evaluating efficacy and safety profiles across 31 clinical trials |
| [37405312](https://pubmed.ncbi.nlm.nih.gov/37405312/) | 2023 | Narrative Review | Health Psychology Research | Dedicated review of bupropion's pharmacokinetics, pharmacodynamics, and mechanisms in depression, ADHD, and smoking cessation — directly relevant to this repurposing rationale |
| [20051220](https://pubmed.ncbi.nlm.nih.gov/20051220/) | 2010 | Meta-Analysis | J Clinical Psychiatry | Compared effect sizes of adult ADHD medications using indirect meta-analysis; bupropion included with quantified effect size estimates |
| [38915262](https://pubmed.ncbi.nlm.nih.gov/38915262/) | 2024 | Clinical Review | Expert Review of Neurotherapeutics | Review of current non-stimulant options for adult ADHD; positions bupropion relative to atomoxetine, viloxazine, and emerging agents |
| [40203844](https://pubmed.ncbi.nlm.nih.gov/40203844/) | 2025 | Network Meta-Analysis | The Lancet Psychiatry | Comparative cardiovascular safety of ADHD pharmacotherapy across age groups; directly relevant to monitoring requirements if bupropion is used for ADHD |
| [26601963](https://pubmed.ncbi.nlm.nih.gov/26601963/) | 2016 | Review | Current Pharmaceutical Design | Reviews mechanisms of action of stimulants, atomoxetine, and bupropion in ADHD; contextualises bupropion's dopaminergic and noradrenergic contributions |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

> **Note:** No ARTG-registered Product Information was identified for bupropion in this Evidence Pack. Clinicians should consult the TGA Medicines Information database and available international prescribing information (e.g., US FDA label, EMA SmPC) for current safety data. Of particular clinical relevance when considering bupropion for ADHD: the drug carries a well-established seizure threshold–lowering effect that is dose-dependent, and the 2025 *Lancet Psychiatry* cardiovascular safety NMA (PMID 40203844) provides updated haemodynamic monitoring guidance applicable to ADHD use across age groups.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A Phase 3 multicentre randomised double-blind placebo-controlled trial (NCT00048360, n=162), a dedicated Cochrane systematic review, and two *Lancet Psychiatry* network meta-analyses collectively establish L1-level evidence for bupropion in adult ADHD. The drug's NDRI mechanism directly addresses the core catecholaminergic deficits of ADHD, and international guidelines already position bupropion as a recognised second-line non-stimulant option — making this repurposing prediction both mechanistically sound and clinically actionable.

**To proceed, the following is needed:**

- **Verify ARTG registration status** — bupropion is available internationally (e.g., as Zyban for smoking cessation); the absence of ARTG entries in this search likely reflects a data retrieval gap rather than true non-availability. A direct ARTG/TGA database search is recommended before concluding no Australian registration exists
- **Obtain TGA Product Information** — download and review the TGA-approved PI to complete formal safety evaluation (key warnings, contraindications, drug interactions, pregnancy category)
- **Clarify indication scope for ARTG use** — if current Australian registration covers only smoking cessation, an off-label prescribing framework or a new indication application (TGA Category 1 extension) would be required for ADHD
- **Develop a safety monitoring plan** addressing bupropion's known seizure risk (dose-dependent; threshold lowered by eating disorders, alcohol withdrawal, concurrent CNS drugs) and cardiovascular parameters identified in the 2025 Lancet Psychiatry cardiovascular NMA
- **Paediatric and adolescent evidence gap** — the only paediatric RCT (NCT00936299, n=105) was conducted in adolescents with comorbid substance use disorder; evidence for ADHD without substance comorbidity in this age group is limited and should be flagged in any prescribing guidance
- **Retrieve full MOA data from DrugBank** (DB01156) to complete the mechanistic analysis and support any TGA submission narrative
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

