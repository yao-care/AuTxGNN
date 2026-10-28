---
layout: default
title: Fulvestrant
parent: Moderate Evidence (L3-L4)
nav_order: 322
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Fulvestrant: predicted new indication HIV infectious disease (evidence level L5). Approved use: Not stated in the Australian registration data (fulvestrant is genera…"
monitor_inn: "Fulvestrant"
predicted_indications: ["HIV infectious disease", "multiple endocrine neoplasia", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "rheumatoid arthritis", "acne (disease)", "brachydactyly-syndactyly syndrome", "hemoglobinopathy", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
---

# Fulvestrant
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

## Fulvestrant: From Breast Cancer to HIV Infectious Disease
{: .text-alpha }

## One-Sentence Summary

Fulvestrant is an estrogen receptor antagonist and degrader, marketed in Australia as an injectable. The original indication text was not available in the data compiled for this report. The TxGNN model predicts it may be effective for **HIV infectious disease**, but there are **no registered clinical trials** and only **2 publications** (one preclinical study and one unrelated to HIV), so the evidence is very weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Australian registration data (fulvestrant is generally used for hormone receptor-positive advanced breast cancer, as reflected in the trials below) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L4 (preclinical only) |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, fulvestrant is an estrogen receptor alpha (ERα) antagonist and degrader. Its efficacy in hormone receptor-positive breast cancer is well established, and mechanistically it may be applicable to HIV.

The link is indirect. ERα is expressed in CD4+ T cells and appears to influence HIV transcription and latency. A 2026 preclinical study tested fulvestrant, together with estrogen and HIV latency-reversing agents, in CD4+ T cells. This suggests ERα blockade could modulate latency reversal, but the work is in vitro only. No human data exist.

It should be noted that the TxGNN score is high, but the model also ranks several implausible indications (veterinary immunodeficiency diseases and rare congenital syndromes) at similar scores. The score alone should not be read as evidence of clinical benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered for HIV infectious disease.

(For context, the second-ranked prediction, multiple endocrine neoplasia, was linked to 13 fulvestrant breast cancer trials. These appear to be keyword-mapping artefacts and do not study HIV or multiple endocrine neoplasia, so they are not listed here.)

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42430506](https://pubmed.ncbi.nlm.nih.gov/42430506/) | 2026 | Preclinical in vitro study | JCI Insight | Evaluated how estrogen, fulvestrant and HIV latency-reversing agents affect ERα in CD4+ T cells; supports a role for ER signalling in HIV latency |
| [40343334](https://pubmed.ncbi.nlm.nih.gov/40343334/) | 2025 | Cross-omics cohort analysis | Research Square | Concerns HTLV-1-associated myelopathy, not HIV; limited direct relevance |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12300J | Fulvestrant Sandoz | Injection 250 mg in 5 mL pre-filled syringe | Not stated in the data compiled |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Endocrine therapy (hormone receptor antagonist and degrader), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the Product Information (PI) warnings and precautions |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease links in the TxGNN knowledge graph, not label text): liver disease, gallbladder disease, thrombocytopenia and blood coagulation disease. These should be checked against the PI.
- **Drug Interactions**: 92 potential interactions were identified, all with an unclassified severity level. Examples include warfarin, acetylsalicylic acid, prednisone, dexamethasone, simvastatin, metformin, bupropion, and several proton pump inhibitors and antiemetics (pantoprazole, omeprazole, ondansetron, palonosetron). The warfarin and aspirin entries are worth reviewing given the thrombocytopenia and coagulation signals.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting evidence for HIV is a single indirect preclinical study, with no clinical trials. The high TxGNN score is not backed by human data, and the mechanism is speculative.

**To proceed, the following is needed:**
- Mechanism of action data and the approved indication text from the PI
- Product Information warnings and contraindications (a blocking gap for safety screening)
- Further preclinical work on ERα blockade and HIV latency in relevant models
- A rationale for a long-acting injectable in this population, and a review of interactions with antiretroviral therapy
- Any clinical evidence before further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

