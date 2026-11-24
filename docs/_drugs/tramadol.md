---
layout: default
title: Tramadol
parent: Model Prediction Only (L5)
nav_order: 743
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "Tramadol"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "juvenile idiopathic arthritis", "juvenile arthritis due to defect in LACC1", "rheumatoid nodulosis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis"]
description: "Tramadol: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). In Australia: 13 PBS items (13 currently listed)"
---

# Tramadol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Tramadol: Acromesomelic dysplasia, Hunter-Thompson type
{: .text-alpha }

## One-Sentence Summary

Tramadol is an opioid/SNRI-type analgesic, originally associated with osteoarthritis and arthropathy pain.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare genetic skeletal disorder,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction. It is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (13 of 13 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 13 (valid: 13) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for tramadol: "Tramadol Hydrochloride Extended-Release Capsules contain tramadol, an opioid agonist, and an inhibitor of reuptake of norepinephrine and serotonin. Although its mode of action is not completely understood, from animal tests, at least two complementary mechanisms appear applicable: binding of parent and M1 metabolite to mu-opioid receptors and weak inhibition of reuptake of norepinephrine and serotonin." ([DailyMed: Tramadol Hydrochloride Extended-Release (tramadol hydrochloride) prescribing information, Trigen Laboratories, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c0bc7218-3fd0-4646-96f4-25355fc84aa9), label version 2026-01-23; accessed 2026-11-19.) Based on known information, tramadol is a centrally acting analgesic with mu-opioid agonist and monoamine reuptake inhibition activity, and it is used for pain in joint conditions such as osteoarthritis.

Acromesomelic dysplasia, Hunter-Thompson type, is a rare genetic skeletal dysplasia caused by loss-of-function variants in the CDMP1/GDF5 gene, affecting limb growth. Tramadol does not act on the GDF5/BMP pathway, so there is no credible mechanistic link. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. At most, tramadol could offer symptomatic analgesia, which is not a disease-modifying indication.

Other top-ranked predictions show the same pattern. They include brachyolmia, myosclerosis, pseudoachondroplasia, spondyloarthropathy and several forms of juvenile arthritis. Only pseudoachondroplasia, which is associated with early-onset osteoarthritis, and the arthritis-related conditions have a weak, indirect symptomatic connection through joint pain management.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked prediction.

For context, the only publication identified in the wider prediction set is for juvenile idiopathic arthritis (rank 7):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20799760](https://pubmed.ncbi.nlm.nih.gov/20799760/) | 2010 | Review | Paediatric Drugs | Review of ketoprofen (an NSAID) pharmacokinetics, efficacy and tolerability in children. It concerns ketoprofen, not tramadol, so it gives no direct evidence for this drug. |

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 2527B | Tramal SR 50 | Tramadol | Tablet (sustained release) containing tramadol hydrochloride 50 mg | Valid |
| 3484J | Tramal 100 | Tramadol | Injection containing tramadol hydrochloride 100 mg in 2 mL | Valid |
| 5150C | Tramal | Tramadol | Oral drops containing tramadol hydrochloride 100 mg per mL, 10 mL | Valid |
| 5231H | Tramal 100 | Tramadol | Injection containing tramadol hydrochloride 100 mg in 2 mL | Valid |
| 5232J | Tramal | Tramadol | Capsule containing tramadol hydrochloride 50 mg | Valid |
| 8455B | Tramal | Tramadol | Capsule containing tramadol hydrochloride 50 mg | Valid |
| 8523N | Tramal SR 100 | Tramadol | Tablet (sustained release) containing tramadol hydrochloride 100 mg | Valid |
| 8524P | Tramal SR 150 | Tramadol | Tablet (sustained release) containing tramadol hydrochloride 150 mg | Valid |
| 8525Q | Tramal SR 200 | Tramadol | Tablet (sustained release) containing tramadol hydrochloride 200 mg | Valid |
| 8582Q | Tramal 100 | Tramadol | Injection containing tramadol hydrochloride 100 mg in 2 mL | Valid |
| 8843K | Tramal | Tramadol | Oral drops containing tramadol hydrochloride 100 mg per mL, 10 mL | Valid |
| 12008B | Tramal | Tramadol | Capsule containing tramadol hydrochloride 50 mg | Valid |
| 12024W | Tramal | Tramadol | Capsule containing tramadol hydrochloride 50 mg | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

## Safety Considerations

- **Contraindications and conditions of concern (from knowledge graph drug-disease links, not label text):** hypertension, liver failure, liver disease, cirrhosis, gallbladder disease, epilepsy, anxiety disorder, neurotic disorder, dysthymic disorder, diabetes mellitus, diabetic ketoacidosis, substance abuse/dependence, substance-related disorder, hyperlipidaemia, familial hyperlipidaemia, respiratory failure, paracetamol poisoning, serotonin syndrome, pseudotumor cerebri, intracranial hypertension, alcohol withdrawal, Wernicke-Korsakoff syndrome, substance withdrawal syndrome, and central nervous system infectious disorders.
- **Drug Interactions:** 100 interactions were recorded. The first 20 listed include the following.
  - **Major:** alvimopan, bupropion, cisapride, dexfenfluramine, diethylpropion, dolasetron, dronabinol, ephedrine, fenfluramine.
  - **Moderate:** atropine, bisacodyl, castor oil, cimetidine, clarithromycin, clidinium, dicyclomine, eliglustat, eluxadoline, famotidine, glycerin.
- **Paediatric use:** Several top predictions involve juvenile arthritis. Tramadol carries paediatric safety restrictions, including respiratory depression risk and CYP2D6 ultra-rapid metabolism, which would need careful review.

Please also refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is a computational signal only (L5). There are no registered trials or supporting publications, and no plausible mechanistic link between tramadol and GDF5-related skeletal dysplasia. Any benefit would be limited to symptomatic pain relief, which is already within tramadol's existing analgesic use.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) to enable a proper mechanistic-link analysis
- TGA Product Information for the ARTG entry, including approved indications, warnings and contraindications
- Preclinical or clinical evidence showing a disease-relevant effect in the predicted condition
- A decision on whether symptomatic analgesia in rare skeletal or arthritic conditions is a useful question, since a disease-modifying claim is not supported
- A dedicated paediatric safety review before any use in juvenile arthritis

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Tramadol Hydrochloride Extended-Release (tramadol hydrochloride) prescribing information, Trigen Laboratories, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c0bc7218-3fd0-4646-96f4-25355fc84aa9) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

