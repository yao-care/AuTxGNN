---
layout: default
title: Rosuvastatin
parent: Model Prediction Only (L5)
nav_order: 649
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Rosuvastatin: predicted new indication Cholesterol-ester transfer protein deficiency (evidence level L5). Approved use: Lipid disorders (hypertriglyceridaemia…"
monitor_inn: "Rosuvastatin"
predicted_indications: ["cholesterol-ester transfer protein deficiency", "brain stem infarction", "HIV infectious disease", "hypoalphalipoproteinemia", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "hyperlipidemia due to hepatic triglyceride lipase deficiency", "ABri amyloidosis"]
---

# Rosuvastatin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Rosuvastatin: From Hyperlipidaemia and Atherosclerotic Disease to Cholesterol-Ester Transfer Protein Deficiency

## One-Sentence Summary

Rosuvastatin is a statin (HMG-CoA reductase inhibitor) originally used for lipid disorders such as hypertriglyceridaemia, homozygous familial hypercholesterolaemia and atherosclerosis, and for stroke-related conditions.
The TxGNN model's top-ranked prediction is **cholesterol-ester transfer protein (CETP) deficiency** (score 99.54%), but **no clinical trials or publications** were found for it.
The best-supported prediction in the data is **familial hypercholesterolaemia** (99.54%), which is largely an on-label or closely related use, with **10 Phase 3 trials** and **12 publications** compiled for it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Lipid disorders (hypertriglyceridaemia, homozygous familial hypercholesterolaemia, hyperlipoproteinaemia), atherosclerosis and cerebrovascular disease (from knowledge-graph indication data; no approved indication text available from the ARTG entry) |
| Predicted New Indication | Cholesterol-ester transfer protein deficiency (rank 1); familial hypercholesterolaemia is the best-supported candidate (rank 2) |
| TxGNN Prediction Score | 99.54% (rank 1); 99.54% (rank 2, familial hypercholesterolaemia) |
| Evidence Level | L5 for rank 1 (model prediction only); L1 for familial hypercholesterolaemia |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold for rank 1; Proceed with Guardrails for familial hypercholesterolaemia |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, rosuvastatin inhibits HMG-CoA reductase, which reduces hepatic cholesterol synthesis, upregulates hepatic LDL receptors and lowers LDL cholesterol.

**CETP deficiency (rank 1).** CETP deficiency raises HDL cholesterol and lowers LDL cholesterol. A lipid-lowering rationale is plausible, but the high score is a model prediction only. No trials or literature were retrieved, so there is no clinical support. Cardiovascular benefit in this rare condition is unestablished, and the value of lowering LDL cholesterol further in a population that already has low LDL cholesterol is unclear.

**Familial hypercholesterolaemia (rank 2).** Lowering LDL cholesterol through LDL receptor upregulation is the core mechanism in this condition. Homozygous familial hypercholesterolaemia is already among the listed original indications, so this is closer to on-label use than true repurposing. Heterozygous disease and paediatric populations are supported by multiple completed Phase 3 trials.

---

## Clinical Trial Evidence

Trials below relate to the best-evidenced prediction, familial hypercholesterolaemia (rank 2). The top-ranked prediction, CETP deficiency, has currently no related clinical trials registered.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00654602](https://clinicaltrials.gov/study/NCT00654602) | Phase 3 | Completed | 1500 | 48-week open-label study of rosuvastatin in Fredrickson type IIa/IIb dyslipidaemia, including heterozygous FH |
| [NCT01078675](https://clinicaltrials.gov/study/NCT01078675) | Phase 3 | Completed | 315 | 2-year open-label efficacy and safety study in children and adolescents (6 to <18 years) with FH |
| [NCT00355615](https://clinicaltrials.gov/study/NCT00355615) | Phase 3 | Completed | 173 | 12-week double-blind placebo-controlled study, then 40-week open-label follow-up, in children aged 10-17 years with heterozygous FH |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3 | Completed | 442 | Renal effects of rosuvastatin versus simvastatin in type IIa/IIb dyslipidaemia, including heterozygous FH |
| [NCT02226198](https://clinicaltrials.gov/study/NCT02226198) | Phase 3 | Completed | 20 | Double-blind placebo-controlled crossover study in children and adolescents with homozygous FH |
| [NCT02434497](https://clinicaltrials.gov/study/NCT02434497) | Phase 3 | Completed | 9 | Open-label long-term extension of the paediatric homozygous FH study (safety) |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Phase 3 | Completed | 249 | Alirocumab versus placebo in heterozygous FH on background lipid-modifying therapy (rosuvastatin contribution not isolated) |
| [NCT03510884](https://clinicaltrials.gov/study/NCT03510884) | Phase 3 | Completed | 153 | Alirocumab in children with heterozygous FH on stable statin therapy (not a rosuvastatin efficacy trial) |
| [NCT02748057](https://clinicaltrials.gov/study/NCT02748057) | Phase 3 | Completed | 135 | Long-term safety of ezetimibe plus rosuvastatin in Japanese patients with hypercholesterolaemia |
| [NCT06910098](https://clinicaltrials.gov/study/NCT06910098) | N/A | Completed | 195 | Effect of rosuvastatin doses on LDL cholesterol, creatine phosphokinase and AST (supportive dose-response data) |

No trial registered in the Australian New Zealand Clinical Trials Registry (ANZCTR) appeared in the data compiled for this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20223367](https://pubmed.ncbi.nlm.nih.gov/20223367/) | 2010 | RCT | J Am Coll Cardiol | Efficacy and safety of rosuvastatin in children with familial hypercholesterolaemia |
| [28838366](https://pubmed.ncbi.nlm.nih.gov/28838366/) | 2017 | Cohort | J Am Coll Cardiol | Efficacy of rosuvastatin in children with homozygous FH, and association with underlying genetic mutations |
| [26387811](https://pubmed.ncbi.nlm.nih.gov/26387811/) | 2016 | Cohort | Eur J Clin Pharmacol | Population pharmacokinetics of rosuvastatin in children with heterozygous FH |
| [12269853](https://pubmed.ncbi.nlm.nih.gov/12269853/) | 2002 | Review | Drugs | Rosuvastatin superior to atorvastatin, simvastatin and pravastatin for lipid improvement; low propensity for drug interactions |
| [15531000](https://pubmed.ncbi.nlm.nih.gov/15531000/) | 2004 | Review | Clin Ther | Rosuvastatin in primary hypercholesterolaemia, mixed dyslipidaemia and homozygous FH |
| [40254247](https://pubmed.ncbi.nlm.nih.gov/40254247/) | 2025 | Preclinical | Toxicology | Differences in myotoxicity between lipophilic and hydrophilic statins in iPSC-derived muscle cells from FH patients |
| [20531065](https://pubmed.ncbi.nlm.nih.gov/20531065/) | 2010 | Case report | South Med J | Rosuvastatin-induced severe thrombocytopenia (rare adverse event) |
| [24849689](https://pubmed.ncbi.nlm.nih.gov/24849689/) | 2014 | Review | Consult Pharm | Statin-associated incident diabetes |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | AACE/ACE guidelines for management of dyslipidaemia and prevention of cardiovascular disease |
| [36928267](https://pubmed.ncbi.nlm.nih.gov/36928267/) | 2023 | Cohort | J Atheroscler Thromb | Real-world LDL-C goal achievement in high-risk patients in Japan |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13406N | Rosuvastatin Sandoz | Tablet 5 mg (as calcium), oral | Not available in the data compiled for this report |

---

## Safety Considerations

- **Contraindication-related conditions (knowledge graph, not label text):** liver disease, gallbladder disease, hypothyroidism, myxedema, congenital hypothyroidism, myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, substance abuse/dependence, rhabdomyolysis, nodular fasciitis, injury, proteinuria.
- **Drug Interactions** (100 interactions identified; selected examples):
  - **Major:** fenofibrate, atazanavir
  - **Moderate:** atorvastatin, ezetimibe, bempedoic acid, amiodarone, paclitaxel, alpelisib, apalutamide, zidovudine, adalimumab, ethanol, others
  - **Minor:** levonorgestrel, norethisterone, desogestrel
- **Literature signals:** rare thrombocytopenia (case report), possible increased incident diabetes (review), and myotoxicity concerns.

Please also refer to the TGA-approved Product Information (PI) for full warnings and contraindications, as label text was not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold for CETP deficiency (rank 1); Proceed with Guardrails for familial hypercholesterolaemia (rank 2)**

**Rationale:**
- CETP deficiency has a high TxGNN score but no trials, no literature and no established mechanistic benefit, so it remains a model prediction (L5).
- Familial hypercholesterolaemia is supported by multiple completed Phase 3 trials, including paediatric studies, and a randomised controlled trial publication (L1). It overlaps with existing indications, so it is not a true new use.

**To proceed, the following is needed:**
- Review of the TGA-approved PI, since the data compiled for this report contain no approved indication text, warnings or contraindications for the ARTG entry
- Detailed mechanism of action data
- For CETP deficiency: mechanistic and clinical studies establishing whether lipid lowering gives any cardiovascular benefit
- Guardrails for familial hypercholesterolaemia use: monitoring for myopathy and rhabdomyolysis, liver enzymes and thyroid function, plus a plan to manage interactions (especially fenofibrate and protease inhibitors) and dose adjustment in renal impairment and in Asian patients
- Confirmation that the Australian product's approved age groups cover paediatric FH use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

