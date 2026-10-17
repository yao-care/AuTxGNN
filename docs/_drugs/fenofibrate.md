---
layout: default
title: Fenofibrate
parent: Moderate Evidence (L3-L4)
nav_order: 290
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Fenofibrate: predicted new indication Homozygous familial hypercholesterolaemia (evidence level L4). Approved use: Hypertriglyceridaemia, hyperlipidaemia, familial hyperlipidaemia…"
monitor_inn: "Fenofibrate"
predicted_indications: ["homozygous familial hypercholesterolemia", "cholesterol-ester transfer protein deficiency", "hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency", "hypercholesterolemia, autosomal dominant", "hypolipoproteinemia (disease)", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Fenofibrate
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Fenofibrate: From Hypertriglyceridaemia and Hyperlipidaemia to Homozygous Familial Hypercholesterolaemia

## One-Sentence Summary

Fenofibrate is a lipid-lowering drug originally used for hypertriglyceridaemia and other hyperlipidaemias.
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolaemia (HoFH)**, but the data compiled for this report contain **no clinical trial of fenofibrate in HoFH**, only one small historical case within a 1984 cohort study.
The prediction is supported by model score alone, and the mechanism makes a meaningful LDL-C effect unlikely.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertriglyceridaemia, hyperlipidaemia, familial hyperlipidaemia, hypoalphalipoproteinaemia (from the knowledge graph; the ARTG entry has no indication text) |
| Predicted New Indication | Homozygous familial hypercholesterolaemia |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

**Note on other predictions:** The top-ranked prediction (HoFH) has the weakest direct support. The rank 2 prediction, **hyperlipoproteinaemia**, is essentially an on-label use (mixed dyslipidaemia and hypertriglyceridaemia). It has L1 evidence, with multiple Phase 3 randomised trials and a "Proceed with Guardrails" recommendation, but it is not true repurposing. The remaining predictions are covered briefly in the conclusion.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, fenofibrate is a PPAR-alpha agonist. It increases lipoprotein lipase activity, reduces ApoC-III and promotes fatty acid oxidation. This lowers triglycerides, raises HDL-C and modestly lowers LDL-C, mainly by shifting LDL particle size and composition.

HoFH is caused by LDL receptor dysfunction. PPAR-alpha activation does not correct this defect, so a clinically meaningful LDL-C reduction is unlikely. The link to the original indications is therefore indirect, through general lipid modulation. The only direct human signal is a 1984 cohort of 22 patients with type II hyperlipoproteinaemia. In that study, one patient with HoFH showed the greatest fall in total and LDL cholesterol on fenofibrate 300 mg/day, but this is a single anecdotal observation.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Alirocumab (PCSK9 inhibitor) in children and adolescents with HoFH, with LDL-C reduction at Week 12 as the primary endpoint. Does not involve fenofibrate, so it is not direct evidence. |

No registered trial testing fenofibrate in HoFH was found. No ANZCTR identifiers were available in the data compiled for this report.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6593751](https://pubmed.ncbi.nlm.nih.gov/6593751/) | 1984 | Cohort | Pharmacol Res Commun | 22 patients with type II hyperlipoproteinaemia given fenofibrate 300 mg/day for 4-12 months: total cholesterol fell about 22% and LDL-C about 24%. One HoFH patient showed the greatest fall. |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart J | Non-statin lipid-lowering drugs. The most definite indication for fenofibrate monotherapy is fasting triglycerides >500 mg/dL, to reduce acute pancreatitis risk. |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Review (guideline) | Endocr Pract | AACE/ACE guidelines for dyslipidaemia management and cardiovascular prevention. |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Review | Ann N Y Acad Sci | Drug and surgical treatment of dyslipidaemic children. Fenofibrate is among agents reported to reduce lipids in familial hypercholesterolaemia. |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | Pharmacokinetic study | Pharmacotherapy | Lomitapide (approved for HoFH) pharmacokinetic interactions with several lipid-lowering drugs, including fenofibrate. |
| [35499807](https://pubmed.ncbi.nlm.nih.gov/35499807/) | 2022 | Review | Curr Atheroscler Rep | Dyslipidaemia management in pregnancy. Not specific to fenofibrate. |

The remaining retrieved publications are reviews of other agents (ezetimibe, atorvastatin, PCSK9 inhibitors) and add no fenofibrate-specific evidence.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13469X | FENOFIBRATE RBX | Tablet 48 mg (oral) | Not stated in the data compiled for this report |

## Safety Considerations

The data compiled for this report contain no label-derived warnings or contraindications. The following come from knowledge-graph contraindication associations, not product label text, and should be verified against the TGA-approved Product Information (PI):

- **Hepatic and biliary:** liver failure, liver disease, gallbladder disease, cholelithiasis and cholecystolithiasis
- **Pancreatic:** pancreatitis
- **Muscle:** myopathy, muscular and skeletal muscle disease, rhabdomyolysis, familial periodic paralysis
- **Haematological:** thrombocytopenia, anaemia, leukopenia, agranulocytosis, neutropenia (including several congenital forms)
- **Renal:** impaired renal function

**Drug interactions:** The interaction screen returned 100 interactions, all in the sample shown rated Moderate. These include:
- Sulfonylureas (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide)
- Many insulin formulations
- Chenodeoxycholic acid
- Esomeprazole

Glucose-lowering therapy may need monitoring when fenofibrate is co-prescribed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
HoFH is caused by LDL receptor dysfunction, and fenofibrate does not address this defect. There is no fenofibrate trial in HoFH, and the evidence is limited to one patient in a 1984 cohort. Established HoFH therapies (statins, ezetimibe, PCSK9 inhibitors, lomitapide) have far stronger support. A high model score alone is not enough to advance this indication.

**Other predictions:**
- **Hyperlipoproteinaemia (rank 2):** On-label use with L1 evidence, so Proceed with Guardrails. This is not repurposing.
- **Familial hypercholesterolaemia and autosomal dominant hypercholesterolaemia (ranks 3 and 7):** Research question (L3). Older small studies show modest LDL-C lowering, and fenofibrate is at best an adjunct.
- **Hyperlipidaemia due to hepatic triglyceride lipase deficiency (rank 6):** Research question (L3), with a very small kinetic study in two patients.
- **CETP deficiency, hypolipoproteinaemia, hyperalphalipoproteinaemia, 7-alpha-hydroxylase deficiency and the neurodevelopmental disorder (ranks 4, 5, 8, 9, 10):** Hold, with preclinical or no evidence. Several of these have no plausible therapeutic rationale.

**To proceed, the following is needed:**
- Mechanism of action data confirmed from DrugBank
- Product Information review for warnings and contraindications (a blocking gap for safety screening)
- Prospective controlled data on fenofibrate in HoFH, if pursued at all, and a clear comparison against current standard therapy
- Confirmation of the approved indication text for the ARTG entry
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

