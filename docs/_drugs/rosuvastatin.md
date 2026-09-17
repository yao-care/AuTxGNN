---
layout: default
title: Rosuvastatin
parent: High Evidence (L1-L2)
nav_order: 607
evidence_level: L1
indication_count: 10
---

# Rosuvastatin
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

# Rosuvastatin: From Dyslipidaemia to Familial Hypercholesterolaemia (Ten TxGNN-Predicted Indications Assessed)

## One-Sentence Summary

Rosuvastatin is a well-established HMG-CoA reductase inhibitor (statin) used for dyslipidaemia/hypercholesterolaemia; this evidence pack is a **multi-indication** TxGNN screen returning 10 ranked candidates for the drug. The most credible new-use signal is **Familial Hypercholesterolaemia**, backed by **23 clinical trials** and **13 publications** (Evidence Level L1), while the top-ranked candidate by raw model score (cholesterol-ester transfer protein deficiency) is flagged in the evidence itself as a likely disease-entity matching error. Several other candidates (HIV, hyperlipidaemia) carry moderate-to-strong evidence; the remainder have weak or no supporting data.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dyslipidaemia / hypercholesterolaemia (per literature review, PMID 12269853); no formal Australian regulatory indication text is available — see Data Gaps |
| Predicted New Indication | Familial Hypercholesterolaemia |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data is not available in this evidence pack (flagged as Data Gap DG002). Based on the literature that is available, rosuvastatin is an HMG-CoA reductase inhibitor (statin class) — a well-established mechanism for lowering LDL cholesterol by inhibiting hepatic cholesterol synthesis (PMID 12269853).

In familial hypercholesterolaemia (FH), a defect in LDL-receptor function reduces LDL clearance. Statins upregulate residual LDL-receptor activity and inhibit endogenous cholesterol synthesis, which is precisely the mechanism needed to counteract FH pathophysiology. This is already standard of care in international treatment guidelines, and the mechanistic link is direct and clinically proven, including in children and adolescents — this is arguably a well-validated *extension* of statin pharmacology rather than a novel repurposing hypothesis.

By contrast, the model's single highest-scoring candidate — cholesterol-ester transfer protein (CETP) deficiency — does not hold up on inspection: CETP deficiency is characterised by markedly *elevated* HDL rather than elevated LDL, which runs counter to a statin's primary LDL-lowering direction of effect. The two supporting papers are actually case reports on Apo A-I deficiency and hepatic lipase deficiency, not CETP deficiency itself, indicating this is most likely a TxGNN disease-entity matching artefact rather than a genuine signal.

## Clinical Trial Evidence (Familial Hypercholesterolaemia)

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01078675](https://clinicaltrials.gov/study/NCT01078675) | Phase 3 | Completed | 315 | Efficacy and 2-year safety of open-label rosuvastatin in children/adolescents (6–<18y) with FH, including PK analysis |
| [NCT00355615](https://clinicaltrials.gov/study/NCT00355615) | Phase 3 | Completed | 173 | 12-week double-blind RCT + 40-week open-label follow-up of once-daily rosuvastatin in children 10–17y with HeFH; LDL-C reduction from baseline |
| [NCT02434497](https://clinicaltrials.gov/study/NCT02434497) | Phase 3 | Completed | 9 | Open-label long-term extension evaluating rosuvastatin safety in children/adolescents with homozygous FH (HoFH) |
| [NCT02226198](https://clinicaltrials.gov/study/NCT02226198) | Phase 3 | Completed | 20 | Randomised, double-blind, placebo-controlled crossover study establishing efficacy, safety and tolerability of rosuvastatin in HoFH children/adolescents |
| [NCT00654602](https://clinicaltrials.gov/study/NCT00654602) | Phase 3 | Completed | 1500 | 48-week open-label study of rosuvastatin in Fredrickson Type IIa/IIb dyslipidaemia, including heterozygous FH; assessed LDL-C goal achievement |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3 | Completed | 442 | 6-week open-label RCT comparing renal effects of rosuvastatin vs simvastatin in Type IIa/IIb dyslipidaemia including HeFH |
| [NCT06910098](https://clinicaltrials.gov/study/NCT06910098) | N/A | Completed | 195 | RCT assessing impact of rosuvastatin dose on LDL, CPK and AST levels |
| [NCT02107898](https://clinicaltrials.gov/study/NCT02107898) | Phase 3 | Completed | 216 | RCT of alirocumab added to background statin (rosuvastatin) therapy in HeFH/high-CV-risk patients uncontrolled on lipid-modifying therapy |
| [NCT01730040](https://clinicaltrials.gov/study/NCT01730040) | Phase 3 | Completed | 355 | RCT comparing alirocumab, ezetimibe, atorvastatin dose increase, or switch to rosuvastatin in patients (including HeFH) uncontrolled on atorvastatin |
| [NCT06686615](https://clinicaltrials.gov/study/NCT06686615) | N/A | Recruiting | 2000 | Observational study of bempedoic acid + ezetimibe + rosuvastatin/atorvastatin in primary hypercholesterolaemia or mixed dyslipidaemia |

No ANZCTR identifiers were present in the source data for these trials.

## Literature Evidence (Familial Hypercholesterolaemia)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | AACE/ACE dyslipidaemia management and CVD prevention guideline, positioning statins as first-line therapy |
| [28592434](https://pubmed.ncbi.nlm.nih.gov/28592434/) | 2017 | RCT | Circulation | CHARON study: 2-year rosuvastatin treatment slowed carotid intima-media thickness progression in children with HeFH |
| [28838366](https://pubmed.ncbi.nlm.nih.gov/28838366/) | 2017 | Cohort | J Am Coll Cardiol | Rosuvastatin efficacy in HoFH children varies with the underlying LDLR mutation |
| [20223367](https://pubmed.ncbi.nlm.nih.gov/20223367/) | 2010 | Cohort | J Am Coll Cardiol | Efficacy and safety of rosuvastatin therapy in children with FH |
| [26687694](https://pubmed.ncbi.nlm.nih.gov/26687694/) | 2015 | Clinical study | J Clin Lipidol | CHARON study results: efficacy and safety of rosuvastatin in children/adolescents with FH |
| [26387811](https://pubmed.ncbi.nlm.nih.gov/26387811/) | 2016 | PK study | Eur J Clin Pharmacol | Population pharmacokinetics of rosuvastatin in paediatric patients with HeFH |
| [26988948](https://pubmed.ncbi.nlm.nih.gov/26988948/) | 2016 | Review | J Am Coll Cardiol | Improving monitoring and care of patients with FH |
| [12269853](https://pubmed.ncbi.nlm.nih.gov/12269853/) | 2002 | Review | Drugs | Overview of rosuvastatin pharmacology and comparative lipid-lowering efficacy |
| [40254247](https://pubmed.ncbi.nlm.nih.gov/40254247/) | 2025 | Preclinical/mechanistic | Toxicology | iPSC-derived skeletal muscle model of statin-induced myotoxicity in FH patients |
| [30270066](https://pubmed.ncbi.nlm.nih.gov/30270066/) | 2018 | Observational | Atherosclerosis | FH treatment patterns and LDL-C goal attainment in a real-world Slovak cohort |

## Australia Market Information

No ARTG entries were found for rosuvastatin in this evidence pack; the drug is currently recorded as **not marketed** in Australia. This should be independently verified against the TGA/ARTG database before any regulatory decision, since a "not marketed" status combined with zero licences is unusual for a globally established generic statin and may reflect a data-collection gap rather than true market absence.

## Safety Considerations

No safety data (key warnings, contraindications, or drug-drug interactions) was returned for this drug in the current pack — this is recorded as a **Blocking** data gap (DG001: TFDA/PI warnings and contraindications not retrieved). Please refer to the TGA-approved Product Information (PI) for safety information before any clinical or regulatory use.

One interaction risk is worth flagging qualitatively from the repurposing rationale for the HIV candidate below: co-administration with protease-inhibitor-boosted antiretroviral regimens carries a known drug-drug interaction risk with statins generally — this should be confirmed against the PI once available.

## Portfolio Overview: All 10 TxGNN-Predicted Indications

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation | Note |
|------|---------|------|------|------|------|------|
| 1 | Cholesterol-ester transfer protein deficiency | 99.54% | L4 | S0 | Hold | Likely TxGNN entity-matching error — cited literature concerns unrelated disorders (Apo A-I, hepatic lipase deficiency) |
| 2 | **Familial hypercholesterolaemia** | 99.54% | **L1** | S3 | **Proceed with Guardrails** | Strongest candidate — direct mechanism, extensive paediatric/adult trial base |
| 3 | Hypercholesterolaemia due to CYP7A1 deficiency | 99.51% | L4 | S1 | Hold | Mechanistic rationale only; no trials in this rare disorder |
| 4 | Brain stem infarction | 99.44% | L4 | S1 | Hold | Only animal/mechanistic and biomarker literature; no trials in this population |
| 5 | HIV infectious disease | 99.37% | L2 | S2 | Research Question | Adjunct anti-inflammatory/cardiovascular use, not antiviral; watch for antiretroviral DDI |
| 6 | Hypoalphalipoproteinemia (low HDL) | 99.25% | L3 | S1 | Research Question | Weak mechanistic fit; evidence mostly indirect |
| 7 | Neurodevelopmental disorder (ataxic gait/absent speech) | 99.22% | L5 | S0 | Hold | No mechanism, trials, or literature — score only |
| 8 | Hyperlipidaemia due to hepatic triglyceride lipase deficiency | 99.20% | L5 | S0 | Hold | No supporting evidence beyond model score |
| 9 | ABri amyloidosis | 99.18% | L5 | S0 | Hold | No known mechanistic link; no evidence |
| 10 | Hyperlipidaemia | 99.09% | L1 | S3 | Proceed with Guardrails | Mechanistically sound but overlaps with already-approved statin use — not true repurposing |

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for Familial Hypercholesterolaemia specifically; all other candidates should Hold or remain Research Questions pending further evidence)

**Rationale:**
- Familial hypercholesterolaemia has L1 evidence (23 trials, 13 publications, including paediatric Phase 3 RCTs) and a direct, guideline-endorsed mechanistic link, making it the only candidate in this pack ready for guarded progression.
- The top-scoring candidate by TxGNN alone (CETP deficiency) should not be advanced — it appears to be a model matching artefact rather than a real signal.

**To proceed, the following is needed:**
- Resolve Data Gap DG001 (TFDA/PI warnings and contraindications) — currently a **Blocking** gap that prevents formal safety review (S1) for any candidate
- Resolve Data Gap DG002 (formal DrugBank MOA record), even though literature-derived MOA is reasonably clear
- Independently verify Australian ARTG/market status, since "0 licences / not marketed" is atypical for this drug and may reflect incomplete data collection rather than fact
- For the HIV candidate: characterise drug-drug interaction risk with protease-inhibitor-based antiretroviral regimens before any further evaluation
- Re-run TxGNN disease-entity mapping QA on the CETP deficiency candidate to confirm or rule out the suspected matching error
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

