---
layout: default
title: Mebendazole
parent: Model Prediction Only (L5)
nav_order: 448
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-17
monitor_inn: "Mebendazole"
predicted_indications: ["acne (disease)"]
description: "Mebendazole: predicted new indication Acne (disease) (evidence level L5). In Australia: 2 PBS items (2 currently listed)"
---

# Mebendazole
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

## Mebendazole: Acne (disease)
{: .text-alpha }

## One-Sentence Summary

Mebendazole is an oral anthelmintic (worm treatment) used for intestinal worm infections such as pinworm (enterobiasis), roundworm (ascariasis) and whipworm (trichuriasis).
The TxGNN model predicts it may be effective for **acne**, but there are **no registered clinical trials** and **no relevant publications** supporting this prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 0.9920 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (2 of 2 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for mebendazole: "Mebendazole, a benzimidazole, is an anthelmintic. […] Mebendazole interferes with cellular tubulin formation in the helminth and causes ultrastructural degenerative changes in its intestine. As a result, its glucose uptake and the digestive and reproductive functions are disrupted, leading to immobilization, inhibition of egg production and death of the helminth." ([DailyMed: Vermox (mebendazole) prescribing information, Janssen Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a720c424-517a-461b-8e13-6c37caf8aa3f), label version 2021-10-05; accessed 2026-11-19.) Mebendazole is a benzimidazole anthelmintic. Benzimidazoles are generally understood to act by inhibiting parasite tubulin polymerisation. Its efficacy in intestinal nematode infections is established.

For acne, no credible mechanistic link has been identified. Acne is driven by sebum production, follicular blockage, *Cutibacterium acnes* and inflammation. Tubulin inhibition in helminths has no established role in these processes.

The only publication retrieved is a 1982 case report of proliferative sparganosis (a tapeworm larval infection) in Venezuela. The patient had acne-like skin lesions, but the paper does not address acne treatment. The high TxGNN score therefore appears to be a model artefact rather than a clinically meaningful signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7072899](https://pubmed.ncbi.nlm.nih.gov/7072899/) | 1982 | Case report | Am J Trop Med Hyg | Proliferative sparganosis with acne-like skin lesions; not relevant to acne treatment or to mebendazole efficacy |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form |
|---------|------|------|
| ARTG 12194T | Trust Deworm | Chewable tablet, 100 mg (oral) |

---

## Safety Considerations

- **Disease-related cautions (knowledge graph, not label text)**: liver disease and gallbladder disease are flagged as contraindication-related conditions.
- **Drug Interactions**: 10 interactions were identified.
  - **Moderate**: metronidazole, iodide I-131, iodide I-123, phenobarbital, carbamazepine, ritonavir, fosphenytoin, phenytoin, primidone.
  - **Minor**: cimetidine.
  - Anticonvulsants (phenobarbital, carbamazepine, phenytoin, fosphenytoin, primidone) are a notable cluster.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no trials, no relevant literature and no plausible mechanism linking mebendazole to acne. It should not progress to clinical consideration on current evidence.

**To proceed, the following is needed:**
- A plausible mechanistic hypothesis and supporting preclinical data for acne
- Any clinical or observational evidence of benefit in acne
- Review of the TGA Product Information for safety, including hepatic precautions and interactions

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Vermox (mebendazole) prescribing information, Janssen Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a720c424-517a-461b-8e13-6c37caf8aa3f) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

