---
layout: default
title: Orlistat
parent: Model Prediction Only (L5)
nav_order: 531
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Orlistat: predicted new indication Fatty liver disease (NAFLD/NASH/MAFLD) (evidence level L5). Approved use: Obesity (including monogenic obesity)"
---

# Orlistat
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Orlistat: From Obesity to Fatty Liver Disease

## One-Sentence Summary

Orlistat is a gastrointestinal lipase inhibitor, originally used to treat obesity.
The TxGNN model predicts it may be effective for **fatty liver disease**, the highest-evidence candidate among its top 10 predictions. It is supported by **3 registered clinical trials (2 directly relevant, both small)** and **20 publications**, including one 2023 RCT and a 2024 meta-analysis.

*Note: The model's top-ranked prediction is hypervitaminosis (score 99.4%), but it has no supporting evidence and is likely a knowledge-graph artefact. This report therefore focuses on fatty liver disease, the best-supported candidate.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Obesity (including monogenic obesity); the Australian licence text does not state an indication |
| Predicted New Indication | Fatty liver disease (NAFLD/NASH/MAFLD) |
| TxGNN Prediction Score | 85.3% (the top-ranked prediction, hypervitaminosis, scores 99.4% but has no evidence) |
| Evidence Level | L2 (no completed Phase 2/3 RCT in the registered trials, but supported by a published RCT and a meta-analysis; provisional) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails (research question) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, orlistat inhibits gastrointestinal lipases, which reduces absorption of dietary fat and promotes weight loss.

Obesity is a major driver of fatty liver disease. Weight loss can reduce hepatic steatosis and improve liver enzymes in obesity-associated NAFLD/NASH/MAFLD. Part of the benefit may also be independent of weight loss. The indication is therefore closely related to orlistat's original use in obesity.

Lifestyle weight loss is first-line treatment, but compliance is often poor. A drug that supports weight reduction is therefore a reasonable option to investigate. However, histological benefit has not been confirmed in a Phase 3 trial.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00160407](https://clinicaltrials.gov/study/NCT00160407) | Phase 4 | Completed | 50 | Orlistat in overweight patients with NASH; tests whether enhanced weight loss improves necroinflammatory and fibrotic changes |
| [NCT00207311](https://clinicaltrials.gov/study/NCT00207311) | Phase 4 | Completed | 30 | Randomised, placebo-controlled trial of Xenical in steatosis/NASH with chronic hepatitis C, followed by PEG-interferon/ribavirin treatment |
| [NCT06501326](https://clinicaltrials.gov/study/NCT06501326) | Phase 4 | Unknown | 102 | Liraglutide (not orlistat) in obesity with MAFLD; only indirectly relevant |

No ANZCTR identifiers were available in the data compiled for this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36781126](https://pubmed.ncbi.nlm.nih.gov/36781126/) | 2023 | RCT | Am J Clin Nutr | Diet versus orlistat in obesity with MAFLD |
| [38910819](https://pubmed.ncbi.nlm.nih.gov/38910819/) | 2024 | Systematic review and meta-analysis | Proc (Bayl Univ Med Cent) | Efficacy of orlistat in obese patients with NAFLD across RCTs; orlistat reduces intestinal fat absorption and liver fat |
| [41069538](https://pubmed.ncbi.nlm.nih.gov/41069538/) | 2024 | Clinical study | Acta Endocrinol (Buchar) | Early effect of orlistat on NASH-related and atherogenicity indices in obese patients with NAFLD |
| [27646933](https://pubmed.ncbi.nlm.nih.gov/27646933/) | 2017 | Review | Gut | Current and upcoming NAFLD pharmacotherapy, including repurposing of existing agents |
| [35501557](https://pubmed.ncbi.nlm.nih.gov/35501557/) | 2022 | Review | Curr Obes Rep | Anti-obesity medications in NAFLD, focusing on hepatic histology |
| [18095746](https://pubmed.ncbi.nlm.nih.gov/18095746/) | 2008 | Review | Drug Saf | Orlistat adverse effects and drug interactions |
| [30502373](https://pubmed.ncbi.nlm.nih.gov/30502373/) | 2019 | Review | Metabolism | Obesity and NAFLD from pathophysiology to therapeutics |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 4570M (as listed in the data compiled for this report) | Xenical | Capsule 120 mg (oral) | Not stated in the available data |

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (not label text): liver failure, primary hyperoxaluria, anorexia nervosa, bulimia nervosa, vitamin deficiency disorders, cholestasis (including benign recurrent and familial intrahepatic cholestasis), and drug-induced liver injury. Liver-related flags deserve particular attention in a fatty liver population.
- **Fat-soluble vitamin absorption**: orlistat reduces absorption of vitamins A, D, E and K, so deficiency is a recognised concern.
- **Drug interactions** (100 recorded; examples from the interaction database):
  - Moderate: abacavir, lamivudine, emtricitabine, atazanavir, acarbose, metformin, alogliptin, canagliflozin, albiglutide, chlorpropamide, amiodarone, cannabidiol, asparaginase products, brentuximab vedotin, calaspargase pegol, clofarabine
  - Minor: cholecalciferol, calcifediol, calcitriol

Product Information warnings and contraindications were not available in the compiled data. Please refer to the TGA-approved Product Information (PI) for full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Fatty liver disease has the strongest support among orlistat's predicted indications: two small completed Phase 4 trials, a 2023 RCT and a 2024 meta-analysis. However, the trials are small and no Phase 3 confirmation of histological benefit exists. The other nine predictions (including hypervitaminosis) have little or no evidence and should stay on Hold. Amenorrhoea has only a single small 2006 study.

**To proceed, the following is needed:**
- Review of the full results of NCT00160407, NCT00207311 and the 2023 RCT, particularly histological and liver enzyme outcomes
- Appraisal of the 2024 meta-analysis for quality and heterogeneity
- Mechanism of action data to be confirmed (for example, from DrugBank)
- The TGA Product Information (warnings, contraindications and approved indication) to complete safety screening
- A monitoring plan for fat-soluble vitamins and liver function in patients with liver disease
- Confirmation of the ARTG entry details (licence number, sponsor and approved indication)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

