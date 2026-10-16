---
layout: default
title: Docusate
parent: Model Prediction Only (L5)
nav_order: 222
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Docusate: predicted new indication Plummer-Vinson syndrome (evidence level L5). Approved use: Constipation . The ARTG entry has no approved indication text recorded"
---

# Docusate
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

# Docusate: From Constipation and Deficiency Anaemias to Plummer-Vinson Syndrome

## One-Sentence Summary

Docusate is a surfactant stool softener, listed in the knowledge graph for constipation and several deficiency anaemias (the anaemia links come from the graph, not from its approved use).
The TxGNN model predicts it may be effective for **Plummer-Vinson syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction is most likely an artefact of the knowledge graph.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Constipation (the graph also lists folic acid deficiency, iron deficiency, hypochromic, microcytic and other deficiency anaemias). The ARTG entry has no approved indication text recorded. |
| Predicted New Indication | Plummer-Vinson syndrome |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Docusate is an anionic surfactant stool softener, and its efficacy in constipation is established. There is no known mechanism linking it to Plummer-Vinson syndrome.

Plummer-Vinson syndrome is characterised by iron deficiency anaemia together with oesophageal webs. The high score most likely reflects the closeness of this disease to the iron deficiency anaemia indications in the knowledge graph. Docusate has no known effect on iron absorption or on oesophageal webs, so the link appears to be a graph artefact rather than a pharmacological rationale.

Other top-ranked predictions show the same pattern. They include B12- and folate-independent megaloblastic anaemia, vitamin deficiency disorder and IRIDA syndrome, which sit close to the anaemia indications. Others, such as bile duct disease, acute urate nephropathy, nephrolithiasis, bile duct neoplasm and obstructive jaundice, have no supported mechanism. None has any trial or publication support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 4199B | Waxsol | Ear drops 5 mg per mL (0.5%), 10 mL | Not recorded in the data compiled for this report |

Note that the only ARTG entry is an ear-drop product (ceruminolytic use). It is not an oral laxative formulation, so no registered route matches the predicted systemic indications.

## Safety Considerations

- **Drug Interactions** (4 recorded):
  - Lactulose: Moderate
  - Mineral oil: Moderate
  - Phenolphthalein: Moderate
  - Linaclotide: Minor
- **Disease-level contraindication signals** (from the knowledge graph, not product label text): peptic ulcer disease, potassium deficiency, sickle cell anaemia, haemolytic anaemia, hereditary haemochromatosis, haemosiderosis, iron metabolism disease, Wilson disease, ulcerative colitis, inflammatory bowel disease, appendicitis, chronic atrophic gastritis, gastroenteritis, primary hyperoxaluria, hereditary persistence of fetal haemoglobin and Leber hereditary optic neuropathy.

Warnings and contraindications from the TGA-approved Product Information (PI) were not available. Please refer to the PI for confirmed safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials, no literature and no plausible mechanism. The high score appears to reflect proximity to the anaemia indications in the knowledge graph rather than a real pharmacological link.

**To proceed, the following is needed:**
- Mechanism of action data for docusate, and a testable hypothesis for Plummer-Vinson syndrome
- Product Information warnings and contraindications for a relevant formulation
- Any preclinical or clinical evidence supporting benefit in the predicted condition
- A route and formulation assessment, since the only ARTG entry is an ear-drop product
- Consideration of whether a more established treatment, such as iron replacement and oesophageal dilatation for Plummer-Vinson syndrome, already addresses the need
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

