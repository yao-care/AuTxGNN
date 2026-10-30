---
layout: default
title: Sacubitril
parent: Model Prediction Only (L5)
nav_order: 654
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-30
monitor_inn: "sacubitril"
predicted_indications: ["brain small vessel disease 1 with or without ocular anomalies", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "diabetic nephropathy", "rheumatoid arthritis", "hemoglobinopathy"]
description: "Sacubitril: predicted new indication Brain small vessel disease 1 with or without ocular anomalies (evidence level L5). Approved use: Not recorded in the local data"
---

# Sacubitril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Sacubitril: Brain small vessel disease 1 with or without ocular anomalies
{: .text-alpha }

## One-Sentence Summary

Sacubitril is a neprilysin inhibitor supplied in Australia as a fixed-dose tablet with valsartan (Entresto). The licence record compiled for this report does not state an approved indication.
The TxGNN model predicts it may be effective for **diabetic nephropathy**, the most credible of its top five predictions, with **1 clinical trial** (Phase 4, status unknown) and **15 publications**, most of them preclinical or reviews.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Brain small vessel disease 1 with or without ocular anomalies |
| TxGNN Prediction Score | 0.9958 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold (research question; see conclusion) |

The top-ranked prediction by score was brain small vessel disease 1 with or without ocular anomalies (0.9958). It has no supporting mechanism or evidence (L5, Hold). Diabetic nephropathy is the only prediction with a clinical trial and a plausible mechanism, so this report focuses on it. Rankings 1, 2, 4 and 5 have little or no evidence:

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 1 | Brain small vessel disease 1 (COL4A1-related) | 0.9958 | L5 | The only paper retrieved concerns systemic right ventricular failure, which is unrelated. No mechanistic link is evident. |
| 2 | Autosomal dominant familial haematuria-retinal arteriolar tortuosity-contractures syndrome | 0.9957 | L5 | No trials or literature. Computational prediction only. |
| 4 | Rheumatoid arthritis | 0.9935 | L5 | The only paper is a case report of golimumab-associated myocarditis. It is not evidence of efficacy. |
| 5 | Haemoglobinopathy | 0.9918 | L5 | No trials or literature. Any hypothesis is speculative. |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, sacubitril is a prodrug whose active metabolite inhibits neprilysin, an enzyme that degrades natriuretic peptides. Inhibition raises natriuretic peptide levels, which promotes vasodilation and natriuresis and has anti-fibrotic effects. In the marketed tablet it is combined with valsartan, an angiotensin II receptor blocker.

Blocking the renin-angiotensin system is a cornerstone of diabetic kidney disease management. The neprilysin inhibitor adds a complementary pathway. Preclinical studies in rats and db/db mice report reduced oxidative stress, NF-κB-mediated inflammation, glomerular and tubular injury, and gut microbiota changes. A secondary analysis of the PARADIGM-HF trial (Lancet Diabetes Endocrinol, 2018) examined renal function in patients with type 2 diabetes and heart failure.

An important caveat is that the benefit of sacubitril beyond valsartan alone on renal outcomes has not been established. The prediction is plausible but unconfirmed.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT06501651](https://clinicaltrials.gov/study/NCT06501651) | Phase 4 | Unknown | 297 | Hyper-Save: randomised, controlled, multicentre comparison of sacubitril/valsartan with valsartan over 12 weeks (2:1 allocation) in essential hypertension with type 2 diabetic nephropathy. No results available. Planned dates were August 2024 to April 2025. |

No ANZCTR trials were identified in the data compiled for this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37549515](https://pubmed.ncbi.nlm.nih.gov/37549515/) | 2023 | Clinical study (randomised groups, n=112) | Int Immunopharmacol | Nifedipine controlled-release plus sacubitril/valsartan versus plus valsartan in diabetic nephropathy with hypertension. |
| [29661699](https://pubmed.ncbi.nlm.nih.gov/29661699/) | 2018 | Secondary analysis of RCT | Lancet Diabetes Endocrinol | PARADIGM-HF secondary analysis of neprilysin inhibition and renal function in type 2 diabetes with heart failure. |
| [40416927](https://pubmed.ncbi.nlm.nih.gov/40416927/) | 2025 | Clinical imaging study | Diabetes Metab Syndr Obes | BOLD-MRI evaluation of renal effects of sacubitril/valsartan in diabetic nephropathy. |
| [37625003](https://pubmed.ncbi.nlm.nih.gov/37625003/) | 2023 | Review | Diabetes Care | Update on the pillars of therapy slowing diabetic nephropathy progression. |
| [35165832](https://pubmed.ncbi.nlm.nih.gov/35165832/) | 2022 | Review | Curr Hypertens Rep | Newer drugs for blood pressure lowering and hypertensive organ damage. |
| [35992034](https://pubmed.ncbi.nlm.nih.gov/35992034/) | 2022 | Preclinical (rat) | Diabetes Metab Syndr Obes | Sacubitril/valsartan slowed early diabetic nephropathy via NLRP3 inflammasome inhibition. |
| [36589853](https://pubmed.ncbi.nlm.nih.gov/36589853/) | 2022 | Preclinical (mouse) | Front Endocrinol | Improved diabetic kidney disease and modulated gut microbiota. |
| [32596035](https://pubmed.ncbi.nlm.nih.gov/32596035/) | 2020 | Preclinical (rat) | PeerJ | LCZ696 reduced oxidative stress, inflammation and glomerulosclerosis. |
| [33870733](https://pubmed.ncbi.nlm.nih.gov/33870733/) | 2021 | Preclinical (mouse) | Am J Physiol Renal Physiol | Differential effects versus valsartan in db/db and KKAy mice. |
| [30909895](https://pubmed.ncbi.nlm.nih.gov/30909895/) | 2019 | Preclinical (rat) | Cardiovasc Diabetol | Attenuated glomerular and tubular injury in Zucker obese rats. |

Five further publications (reviews, a podocyte cell study and a mouse study) were retrieved but are not listed here.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11122J | Entresto | Tablet containing sacubitril 97.2 mg with valsartan 102.8 mg | Not stated in the data compiled |

---

## Safety Considerations

**Drug Interactions** (6 moderate-level interactions recorded):
- Nitisinone
- Rosuvastatin
- Simvastatin
- Cobicistat
- Revefenacin
- Alpelisib

For other warnings and contraindications, please refer to the TGA-approved Product Information (PI). The label-based safety data was not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but the evidence is early. There is one Phase 4 trial of unknown status, preclinical data, and no completed Phase 3 renal outcome trial. The other four predictions have no meaningful support. Blocked safety screening (no label data) is also a reason to wait. Diabetic nephropathy remains a reasonable research question, and could move to Proceed with Guardrails if the evidence below is obtained.

**To proceed, the following is needed:**
- Results and current status of NCT06501651, including eGFR and albuminuria endpoints
- Evidence that sacubitril adds renal benefit beyond valsartan alone
- The TGA Product Information, including approved indications, warnings and contraindications
- Mechanism of action data confirmed from DrugBank
- A safety plan for patients with diabetic kidney disease, covering renal function, potassium and blood pressure monitoring
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

