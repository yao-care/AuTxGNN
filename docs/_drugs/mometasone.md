---
layout: default
title: Mometasone
parent: Model Prediction Only (L5)
nav_order: 486
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Mometasone: predicted new indication Primary cutaneous T-cell lymphoma (evidence level L4). Approved use: Not available in the data compiled . Pharmacology data describe topic…"
monitor_inn: "Mometasone"
predicted_indications: ["primary cutaneous T-cell lymphoma"]
---

# Mometasone
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

## Mometasone: From Inflammatory Skin Conditions to Primary Cutaneous T-Cell Lymphoma
{: .text-alpha }

## One-Sentence Summary

Mometasone is a corticosteroid marketed in Australia as a topical ointment (Elocon), and the data compiled for this report do not include a formal approved indication text for it.
The TxGNN model predicts it may be effective for **primary cutaneous T-cell lymphoma**,
but there are currently **0 registered clinical trials** and only **2 case reports** that mention mometasone in this context, so this is a research question rather than an established direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled (the ARTG entry has no indication text). Pharmacology data describe topical use for allergic skin disorders, and intranasal use for asthma, allergic rhinitis and nasal polyposis. |
| Predicted New Indication | Primary cutaneous T-cell lymphoma |
| TxGNN Prediction Score | 0.9936 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the compiled data. Pharmacology records identify the glucocorticoid receptor (NR3C1) as mometasone's target. Mometasone is a medium-to-high potency topical corticosteroid with anti-inflammatory, immunosuppressive and anti-proliferative effects mediated through this receptor.

Topical corticosteroids are a recognised skin-directed therapy for early-stage mycosis fungoides (the patch and plaque stages of primary cutaneous T-cell lymphoma). This gives the prediction biological plausibility at the drug-class level. However, the literature supplied does not test mometasone as a treatment for this condition. The two publications are case reports, and in one of them mometasone was an unsuccessful treatment for a different condition (pseudolymphoma). The high TxGNN score is a model prediction only and should not be read as clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40821495](https://pubmed.ncbi.nlm.nih.gov/40821495/) | 2025 | Case report | Proceedings (Baylor University Medical Center) | Refractory cutaneous pseudolymphoma (a benign mimic of lymphoma) in a 62-year-old woman. Mometasone and tacrolimus were unsuccessful, and the patient was then treated with tapinarof. |
| [25442255](https://pubmed.ncbi.nlm.nih.gov/25442255/) | 2015 | Case report | Journal of Cutaneous Pathology | Childhood mycosis fungoides with a CD8+ CD56+ cytotoxic immunophenotype in an 11-year-old boy, highlighting delayed diagnosis in children. The abstract excerpt provided does not describe mometasone treatment. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10791Y | Elocon | Ointment containing mometasone furoate 1 mg per g, 15 g | Not available in the data compiled |

## Safety Considerations

- **Drug Interactions**: The interaction query completed with one record, which is a pharmacology target association (glucocorticoid receptor) and not a drug-drug interaction. No specific interacting drugs were identified.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is biologically plausible because topical corticosteroids are used in early-stage mycosis fungoides. However, there are no clinical trials, and the only literature is two case reports that do not test mometasone for this indication. Class-level use is not evidence for mometasone specifically.

**To proceed, the following is needed:**
- Approved indication text and the TGA-approved Product Information (warnings and contraindications) for Elocon, which are needed for safety screening
- Detailed mechanism of action data (e.g. from DrugBank)
- Mometasone-specific clinical evidence in primary cutaneous T-cell lymphoma, such as retrospective series or prospective studies of topical corticosteroids in early-stage mycosis fungoides
- Review of route compatibility, as the only Australian product is a topical ointment and the data do not define the route required for this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

