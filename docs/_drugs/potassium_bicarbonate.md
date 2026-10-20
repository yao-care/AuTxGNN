---
layout: default
title: Potassium Bicarbonate
parent: Model Prediction Only (L5)
nav_order: 587
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Potassium Bicarbonate: predicted new indication Gastroduodenitis (evidence level L5). Approved use: Peptic ulcer disease, potassium deficiency…"
monitor_inn: "Potassium bicarbonate"
predicted_indications: ["gastroduodenitis", "stomach disease", "gastroparesis (disease)", "postgastrectomy syndrome", "acute urate nephropathy", "duodenal obstruction"]
---

# Potassium Bicarbonate
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

# Potassium Bicarbonate: From Peptic Ulcer Disease and Potassium Deficiency to Gastroduodenitis

## One-Sentence Summary

Potassium bicarbonate is an alkalinising agent and potassium supplement, originally used for acid-related upper gastrointestinal conditions (such as peptic ulcer disease, reflux and dyspepsia) and for potassium deficiency.
The TxGNN model predicts it may be effective for **gastroduodenitis**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease, potassium deficiency, gastroesophageal reflux disease, oesophagitis, dyspepsia (the ARTG entry lists no approved indication text) |
| Predicted New Indication | Gastroduodenitis |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, potassium bicarbonate is an alkalinising agent that can neutralise gastric acid. It also supplies potassium, which is relevant to its use in potassium deficiency.

Gastroduodenitis is an acid-related inflammatory condition of the stomach and duodenum, and it overlaps closely with the drug's existing indications (peptic ulcer disease, reflux, dyspepsia). The prediction is therefore mechanistically plausible, but it is better described as an extension of existing use than as true repurposing. The high score reflects model prediction only and is not supported by any trial or publication.

The other predicted indications show the same pattern. Most are gastric or peptic conditions that overlap with the original indications (active peptic ulcer disease, stomach disease, gastric ulcer). Others have a weak or speculative rationale (peptic ulcer perforation, gastroparesis, postgastrectomy syndrome, duodenal obstruction). Acute urate nephropathy has a plausible mechanism through urinary alkalinisation, but the potassium load is a significant safety concern in acute kidney injury.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no literature directly evaluates potassium bicarbonate for gastroduodenitis.

For the related prediction of active peptic ulcer disease, one publication was retrieved. It does not evaluate potassium bicarbonate as a therapy.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [883470](https://pubmed.ncbi.nlm.nih.gov/883470/) | 1977 | Diagnostic/clinical study | Acta Hepato-Gastroenterologica | Acetazolamide was used to help distinguish benign from malignant gastric ulcer niches. Potassium bicarbonate was only a minor co-administered component, so this is not a therapeutic evaluation of the drug. |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13933H | Sodibic | Capsule 840 mg (oral) | Not listed in the data compiled for this report |

---

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: congestive heart failure, anuria, atrioventricular block, hyperkalaemic periodic paralysis, periodic paralysis, hypoaldosteronism, myotonia congenita. These reflect the potassium load and should be confirmed against the Product Information.
- **Drug Interactions**: 59 interactions were identified. Of those listed, the main ones are:
  - **Major**: ACE inhibitors (fosinopril, benazepril, captopril, enalapril), angiotensin receptor blockers (olmesartan, valsartan, azilsartan medoxomil, eprosartan), and potassium-sparing agents (amiloride, spironolactone, eplerenone). The concern is additive hyperkalaemia.
  - **Moderate**: aliskiren, drospirenone, and NSAIDs (ketorolac, ibuprofen, diclofenac, oxaprozin, bromfenac, diflunisal, etodolac).

Please refer to the TGA-approved Product Information (PI) for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the TxGNN score alone (evidence level L5), with no clinical trials and no relevant literature. The predicted indication also overlaps heavily with existing uses. The potassium load and the many major interactions with agents that raise potassium call for caution if the drug is used outside current indications.

**To proceed, the following is needed:**
- The TGA-approved Product Information, to confirm approved indications, warnings and contraindications
- Mechanism of action data
- A targeted literature search and, if warranted, controlled clinical evidence for gastroduodenitis
- A clear assessment of whether the prediction is a genuinely new use or falls within existing use
- A safety plan covering potassium monitoring, renal function, and co-prescription with ACE inhibitors, ARBs and potassium-sparing diuretics
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

