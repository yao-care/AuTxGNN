---
layout: default
title: Icosapent Ethyl
parent: Model Prediction Only (L5)
nav_order: 364
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
monitor_inn: "Icosapent ethyl"
predicted_indications: ["hemoglobinopathy"]
description: "Icosapent Ethyl: predicted new indication Hemoglobinopathy (evidence level L5). Approved use: Not recorded in the local data"
---

# Icosapent Ethyl
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

## Icosapent Ethyl: Hemoglobinopathy
{: .text-alpha }

## One-Sentence Summary

Icosapent ethyl is a highly purified eicosapentaenoic acid (EPA) ethyl ester, originally used to treat hypertriglyceridemia.
The TxGNN model predicts it may be effective for **hemoglobinopathy**,
with **1 registered clinical trial (withdrawn, no participants)** and **19 publications** currently supporting this direction, including several analyses of the Phase 3 REDUCE-IT trial.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hemoglobinopathy |
| TxGNN Prediction Score | 0.9909 |
| Evidence Level | L5 (REDUCE-IT-derived evidence; see note below) |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

Note: the top-ranked prediction (hemoglobinopathy) has model prediction only (L5, Hold). The L1 grading rests on the REDUCE-IT trial as reported in the supplied literature. The trial registry record itself was not among the supplied data.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the supplied literature, icosapent ethyl is a purified EPA ethyl ester that lowers triglycerides and triglyceride-rich lipoproteins. It is also reported to have anti-inflammatory, plaque-stabilising and antithrombotic effects.

Elevated triglycerides are linked to residual cardiovascular risk even when LDL cholesterol is well controlled.

The literature includes multiple REDUCE-IT analyses, a large randomised trial in statin-treated patients with elevated triglycerides. The benefit is established for the REDUCE-IT population (statin-treated, elevated triglycerides, high cardiovascular risk). This indication is also close to existing cardiovascular risk-reduction use, so it may be label-adjacent rather than a truly novel repurposing.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT06280976](https://clinicaltrials.gov/study/NCT06280976) | Phase 4 | Withdrawn | 0 | ART-CAP: coronary CT angiography to guide plaque assessment and preventive drug therapy. Withdrawn with no enrolment, so no usable efficacy or safety data |

No ANZCTR trial identifiers were available in the data compiled for this report.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30415628](https://pubmed.ncbi.nlm.nih.gov/30415628/) | 2019 | RCT | N Engl J Med | REDUCE-IT: icosapent ethyl and cardiovascular risk reduction in patients with elevated triglycerides |
| [38873793](https://pubmed.ncbi.nlm.nih.gov/38873793/) | 2024 | RCT | Circulation | RESPECT-EPA: statin plus EPA for secondary prevention in coronary artery disease with a low EPA/AA ratio |
| [31567003](https://pubmed.ncbi.nlm.nih.gov/31567003/) | 2019 | Meta-analysis | J Am Heart Assoc | Marine omega-3 and cardiovascular disease across 13 RCTs (127,477 participants) |
| [35483753](https://pubmed.ncbi.nlm.nih.gov/35483753/) | 2022 | RCT post-hoc | J Am Coll Cardiol | REDUCE-IT: reduced cardiovascular events and mortality in patients with prior MI |
| [40982548](https://pubmed.ncbi.nlm.nih.gov/40982548/) | 2025 | RCT post-hoc | Eur J Prev Cardiol | REDUCE-IT: benefit across MI types and sizes |
| [38678009](https://pubmed.ncbi.nlm.nih.gov/38678009/) | 2024 | RCT post-hoc | Eur Heart J Cardiovasc Pharmacother | REDUCE-IT: effects by baseline residual risk in ASCVD |
| [34710343](https://pubmed.ncbi.nlm.nih.gov/34710343/) | 2021 | Subgroup analysis | Circulation | REDUCE-IT CABG: reduced ischaemic events in patients with prior bypass surgery |
| [36802845](https://pubmed.ncbi.nlm.nih.gov/36802845/) | 2023 | Post-hoc analysis | J Am Heart Assoc | Benefit with and without atrial fibrillation; AF/flutter hospitalisation was higher with icosapent ethyl (3.1% vs 2.1%) |
| [40752806](https://pubmed.ncbi.nlm.nih.gov/40752806/) | 2025 | Cohort | Int J Cardiol | CALLINICUS-Hellas registry: eligibility for icosapent ethyl after acute coronary syndrome and re-infarction risk |
| [42628912](https://pubmed.ncbi.nlm.nih.gov/42628912/) | 2026 | Preclinical (mouse) | J Mol Cell Cardiol | GPR120 activation improves post-MI cardiac remodelling |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14617H | Vazkepa | Capsule 998 mg (oral) | Not available in the data compiled for this report |

## Safety Considerations

- **Atrial fibrillation/flutter:** REDUCE-IT analyses reported higher AF/flutter hospitalisation with icosapent ethyl than placebo (3.1% vs 2.1%).
- **Evidence caveats:** the literature notes concerns about the mineral-oil placebo, bleeding risk, and neutral results for other omega-3 products (such as mixed EPA/DHA formulations).

No drug interactions were identified in the data compiled for this report. For contraindications and other warnings, please refer to the TGA-approved Product Information (PI).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The benefit should not be generalised beyond statin-treated, high-risk patients with elevated triglycerides. The other nine predictions have no direct evidence (hemoglobinopathy, thalassaemia, rheumatoid arthritis and others: Hold; MI subtypes: research question only).

**To proceed, the following is needed:**
- Confirm the ARTG-approved indication for Vazkepa and whether MI-related risk reduction is already covered (label-adjacent)
- Review the PI for warnings and contraindications, particularly AF and bleeding risk
- Retrieve the mechanism of action data from DrugBank
- Define the eligible population (statin-treated, elevated triglycerides, established cardiovascular disease or diabetes with risk factors)
- Verify REDUCE-IT trial registry details and any ANZCTR registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

