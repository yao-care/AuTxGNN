---
layout: default
title: Orlistat
parent: Model Prediction Only (L5)
nav_order: 531
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "Orlistat"
predicted_indications: ["hypervitaminosis"]
description: "Orlistat: predicted new indication Hypervitaminosis (evidence level L5). In Australia: 1 PBS item (1 currently listed)"
---

# Orlistat
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Orlistat: Hypervitaminosis
{: .text-alpha }

## One-Sentence Summary

Orlistat is a gastrointestinal lipase inhibitor, originally used to treat obesity.

*Note: The model's top-ranked prediction is hypervitaminosis (score 0.9942), but it has no supporting evidence and is likely a TxGNN model (deep learning) artefact.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 0.9942 |
| Evidence Level | L5 (no completed Phase 2/3 RCT in the registered trials, but supported by a published RCT and a meta-analysis; provisional) |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails (research question) |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for orlistat: "Orlistat is a reversible inhibitor of gastrointestinal lipases. It exerts its therapeutic activity in the lumen of the stomach and small intestine by forming a covalent bond with the active serine residue site of gastric and pancreatic lipases." ([DailyMed: Xenical (orlistat) prescribing information, H2-Pharma LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6240792b-9224-2d10-e053-2a91aa0a2c3e), label version 2026-09-30; accessed 2026-11-19.) Based on known pharmacology, orlistat inhibits gastrointestinal lipases, which reduces absorption of dietary fat and promotes weight loss.

Weight loss can reduce hepatic steatosis and improve liver enzymes in obesity-associated NAFLD/NASH/MAFLD. Part of the benefit may also be independent of weight loss. The indication is therefore closely related to orlistat's original use in obesity.

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

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 4570M | Xenical | Orlistat | Capsule 120 mg | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

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
However, the trials are small and no Phase 3 confirmation of histological benefit exists. The other nine predictions (including hypervitaminosis) have little or no evidence and should stay on Hold. Amenorrhoea has only a single small 2006 study.

**To proceed, the following is needed:**
- Review of the full results of NCT00160407, NCT00207311 and the 2023 RCT, particularly histological and liver enzyme outcomes
- Appraisal of the 2024 meta-analysis for quality and heterogeneity
- Mechanism of action data to be confirmed (for example, from DrugBank)
- The TGA Product Information (warnings, contraindications and approved indication) to complete safety screening
- A monitoring plan for fat-soluble vitamins and liver function in patients with liver disease
- Confirmation of the ARTG entry details (licence number, sponsor and approved indication)

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Xenical (orlistat) prescribing information, H2-Pharma LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6240792b-9224-2d10-e053-2a91aa0a2c3e) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

