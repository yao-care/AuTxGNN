---
layout: default
title: Ibandronate
parent: Moderate Evidence (L3-L4)
nav_order: 360
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Ibandronate: predicted new indication Duodenal ulcer (evidence level L4). Approved use: Postmenopausal osteoporosis, osteoporosis, hypercalcaemia"
monitor_inn: "Ibandronate"
predicted_indications: ["duodenal ulcer (disease)", "duodenogastric reflux", "duodenal obstruction", "Worth syndrome", "autosomal dominant neovascular inflammatory vitreoretinopathy", "digitalis poisoning", "succinyl-CoA:3-ketoacid CoA transferase deficiency", "multiple endocrine neoplasia", "calcium-alkali syndrome"]
---

# Ibandronate
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

# Ibandronate: From Osteoporosis to Duodenal Ulcer (Computational Prediction)

## One-Sentence Summary

Ibandronate is a nitrogen-containing bisphosphonate originally used for postmenopausal osteoporosis, osteoporosis and hypercalcaemia-related conditions.
The TxGNN model predicts it may be effective for **duodenal ulcer**, but there are **no registered clinical trials** and only **2 publications**, both retrospective claims analyses of gastrointestinal events. These suggest the prediction reflects a safety association rather than a therapeutic one.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Postmenopausal osteoporosis, osteoporosis, hypercalcaemia (knowledge graph indications; no approved indication text is available for the ARTG entry) |
| Predicted New Indication | Duodenal ulcer |
| TxGNN Prediction Score | 97.79% |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Ibandronate is a nitrogen-containing bisphosphonate, a class that inhibits osteoclast-mediated bone resorption. Its efficacy in osteoporosis is established, but this mechanism has no recognised connection to healing duodenal ulcers.

The prediction is most likely a knowledge-graph artefact. Oral nitrogen-containing bisphosphonates are known to cause upper gastrointestinal irritation and mucosal injury. The model's high score probably reflects this adverse-event association rather than a therapeutic one. The two retrieved studies describe GI events in patients starting osteoporosis therapy and the link between those events and compliance. Neither shows benefit in duodenal ulcer.

The same pattern appears in the other top-ranked predictions. Duodenogastric reflux (rank 2) and duodenal obstruction (rank 3) have no clinical or literature support. Of the 10 predictions, the only one with a plausible mechanistic link is **pregnancy-associated osteoporosis** (rank 7). It is a bone-loss disease, consistent with ibandronate's mechanism, and is supported by case reports. It is discussed in the conclusion as a better-grounded research question.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25866298](https://pubmed.ncbi.nlm.nih.gov/25866298/) | 2015 | Retrospective cohort (claims database) | Clinical Therapeutics | Characterised gastrointestinal events among women on oral bisphosphonate therapy. Describes adverse events, not benefit. |
| [27112533](https://pubmed.ncbi.nlm.nih.gov/27112533/) | 2016 | Retrospective cohort (claims database) | Clinical Therapeutics | Estimated GI event rates in women taking oral bisphosphonates and examined the association between GI events and compliance. Describes adverse events, not benefit. |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 9357L | Bondronat | Tablet 50 mg (as ibandronate sodium monohydrate) | Not available in the data compiled for this report |

---

## Safety Considerations

- **Related conditions flagged in the knowledge graph (not label text):** upper GI conditions (gastritis, duodenitis, oesophagitis, oesophageal ulcer, gastro-oesophageal reflux disease, achalasia and other oesophageal motility disorders), osteonecrosis of the jaw, and disorders of calcium and vitamin D metabolism (osteomalacia, rickets). These need confirmation against the Product Information.
- **Drug Interactions (100 interactions identified, all listed here moderate):**
  - Polyvalent cation products that may reduce oral absorption: calcium salts (carbonate, acetate, citrate, gluconate, lactate and others), aluminium hydroxide, iron, kaolin and attapulgite.
  - Amphotericin B formulations.
  - Aspirin and the mesalazine class (mesalazine, balsalazide), which may add to GI irritation.
  - Exenatide and kanamycin.
- **Clinical note:** ibandronate can cause hypocalcaemia, which is relevant in patients with arrhythmia risk.

Please also refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The duodenal ulcer prediction has no therapeutic mechanism and no supporting trials. The only literature describes GI adverse events with oral bisphosphonates, so using ibandronate for this condition would be biologically implausible and potentially harmful.
- Among the other predictions, pregnancy-associated osteoporosis (L4, case reports only) is the only one mechanistically coherent. It could be taken forward as a separate research question, not as a recommendation.

**To proceed, the following is needed:**
- Mechanism of action data for ibandronate
- Approved indication text and Product Information (warnings and contraindications) for the Australian product
- Re-evaluation of the prediction as a safety signal rather than a repurposing opportunity
- For pregnancy-associated osteoporosis: prospective or controlled evidence, with attention to skeletal retention and fetal risk in women of childbearing potential
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

