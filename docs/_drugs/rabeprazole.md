---
layout: default
title: Rabeprazole
parent: Model Prediction Only (L5)
nav_order: 618
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Rabeprazole: predicted new indication Smouldering systemic mastocytosis (evidence level L5). Approved use: Peptic ulcer disease, gastro-oesophageal reflux disease…"
monitor_inn: "Rabeprazole"
predicted_indications: ["Smouldering systemic mastocytosis", "lymphoadenopathic mastocytosis with eosinophilia", "active peptic ulcer disease", "duodenogastric reflux", "gastroduodenitis", "duodenal obstruction", "gastrojejunal ulcer", "peptic ulcer perforation", "gastric ulcer (disease)", "abnormality of glucagon secretion"]
---

# Rabeprazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Rabeprazole: From Peptic Ulcer Disease to Smouldering Systemic Mastocytosis

## One-Sentence Summary

Rabeprazole is a proton pump inhibitor (PPI) originally used for acid-related conditions such as peptic ulcer disease, gastro-oesophageal reflux disease and Zollinger-Ellison syndrome.
The TxGNN model predicts it may be useful for **smouldering systemic mastocytosis**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease, gastro-oesophageal reflux disease, Zollinger-Ellison syndrome and related acid-hypersecretion conditions (systemic mastocytosis is already among the listed indications) |
| Predicted New Indication | Smouldering systemic mastocytosis |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Rabeprazole belongs to the PPI class, which inhibits the gastric H+/K+-ATPase (proton pump) and suppresses acid secretion. Its efficacy in acid-related disease is well established.

Systemic mastocytosis is already listed among rabeprazole's original indications. In that setting, PPIs control gastric hyperacidity caused by histamine release from mast cells. This is symptom control through acid suppression. It is not disease-modifying activity against the mast cell disorder itself.

The high TxGNN score therefore likely reflects this existing link rather than a new therapeutic effect in the smouldering subtype. No trials or literature were found for this subtype, so a benefit beyond acid-related symptoms cannot be supported.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11670F | Rabeprazole Sandoz | Enteric-coated tablet containing rabeprazole sodium 20 mg (oral) | Not provided in the data compiled; refer to the TGA Product Information |

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not label text): liver disease, gallbladder disease, osteoporosis, postmenopausal osteoporosis and bone fracture. These should be checked against the TGA-approved Product Information.
- **Drug Interactions**: 100 interactions were identified, and the first 20 are summarised here.
  - Major: acalabrutinib, atazanavir.
  - Moderate: amikacin, amphetamine, amphotericin B (several formulations), apalutamide, aprepitant, armodafinil, bosutinib, bendroflumethiazide and others.
  - Minor: acetylsalicylic acid, axitinib.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

---

## Other Predictions Worth Noting

The data compiled for this report also include other predictions with stronger evidence.

| Predicted Indication | Evidence Level | Comment |
|------|------|------|
| Gastric ulcer | L2 | Falls under the already-approved peptic ulcer indication, so it is label-consistent rather than true repurposing. 17 trials are linked, including a Phase 2/3 H. pylori study and several Phase 4 studies. Guardrails are CYP2C19 genotype-dependent response and PPI drug interactions. |
| Duodenogastric reflux | L3 | Small, mostly single-centre studies, including a randomised trial in post-cholecystectomy alkaline gastritis. Some benefit may come from combination agents. |
| Gastroduodenitis | L3 | Includes randomised trials of rabeprazole for preventing aspirin-associated ulcer recurrence. Evidence for gastroduodenitis itself is indirect. |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The smouldering systemic mastocytosis prediction has no supporting trials or literature (L5). Any plausible benefit is limited to acid suppression, which is already an approved use in mastocytosis-related hypersecretion, not a disease-modifying effect.

**To proceed, the following is needed:**
- Mechanistic or clinical evidence that rabeprazole affects the smouldering disease course beyond acid control
- Detailed mechanism of action data
- Review of the TGA Product Information for warnings and contraindications
- Consideration of the better-supported acid-related candidates (for example gastric ulcer) as label-consistent uses rather than new repurposing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

