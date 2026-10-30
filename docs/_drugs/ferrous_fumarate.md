---
layout: default
title: Ferrous Fumarate
parent: Model Prediction Only (L5)
nav_order: 294
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
monitor_inn: "Ferrous fumarate"
predicted_indications: ["non-syndromic esophageal malformation"]
description: "Ferrous Fumarate: predicted new indication Non-syndromic esophageal malformation (evidence level L5). Approved use: Not recorded in the local data"
---

# Ferrous Fumarate
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

## Ferrous Fumarate: Non-syndromic esophageal malformation
{: .text-alpha }

## One-Sentence Summary

Ferrous fumarate is an oral iron salt, originally used to treat iron deficiency anaemia and related anaemias.
The TxGNN model predicts it may be effective for **non-syndromic esophageal malformation** (top-ranked), but there are **no registered clinical trials** and **no supporting publications** for that prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Non-syndromic esophageal malformation |
| TxGNN Prediction Score | 0.9949 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

*Note: The approved indication text for the Australian product was not available in the data compiled for this report.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, ferrous fumarate is an oral iron salt whose efficacy in iron deficiency anaemia is well established. It replenishes iron stores so that haemoglobin can be made.

For the top-ranked prediction, **non-syndromic esophageal malformation**, no plausible mechanism is evident. Esophageal malformations are structural developmental defects, and iron supplementation would not be expected to correct them.

Other predictions fall into three groups:

- Vitamin B12- and folate-independent megaloblastic anaemia is not an iron-responsive condition.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction or for any of the other top 10 predicted indications.

## Literature Evidence

No literature was found for the top-ranked prediction (non-syndromic esophageal malformation). The table below shows the most relevant publications retrieved for the other predicted indications, with their relevance noted.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1944691](https://pubmed.ncbi.nlm.nih.gov/1944691/) | 1991 | Review / case-based | Ned Tijdschr Geneeskd | A 73-year-old woman with Plummer-Vinson syndrome (dysphagia, esophageal web, iron deficiency, anaemia). After ferrous fumarate treatment the dysphagia, web and anaemia resolved. |
| [25318791](https://pubmed.ncbi.nlm.nih.gov/25318791/) | 2014 | Case report | Internal Medicine | Iron-deficiency anaemia developed in a man taking rabeprazole (a proton pump inhibitor) for reflux disease. It did not improve with ferrous fumarate and resolved after switching to famotidine. This shows iron deficiency as a consequence of acid suppression, not a new use. |
| [31235618](https://pubmed.ncbi.nlm.nih.gov/31235618/) | 2023 | Interventional study | BMJ Military Health | Iron supplementation study in female combatants, looking at haemoglobin, ferritin and injuries. Poor compliance compromised the study. |
| [17209540](https://pubmed.ncbi.nlm.nih.gov/17209540/) | 2006 | Case report | Dental Update | Severe oral mucosal ulceration from ferrous sulphate tablets, which resolved on switching to ferrous fumarate syrup. Relevant to safety. |
| [18976122](https://pubmed.ncbi.nlm.nih.gov/18976122/) | 2009 | Case report | J Laparoendosc Adv Surg Tech A | Laparoscopic-assisted gastrotomy for an iron bezoar after iron ingestion. Relevant to safety. |
| [3371313](https://pubmed.ncbi.nlm.nih.gov/3371313/) | 1988 | Case report | Equine Vet J | Fatal hepatic failure in newborn foals after oral ferrous fumarate (veterinary; not applicable to humans). |

One further retrieved paper (PMID 28716993, on soluble Fms-like tyrosine kinase-1, endoglin and endothelin-1 in women using proton pump inhibitors) appears unrelated to ferrous fumarate and is not included.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10594N | Ferro-tab | Tablet 200 mg (equivalent to 65.7 mg iron), oral | Not available in the data compiled for this report |

## Safety Considerations

- **Contraindications (knowledge graph, not label text):** The TxGNN knowledge graph links ferrous fumarate to contraindication edges with a range of conditions. Notable groups include:
  - iron overload and metabolism disorders (hereditary hemochromatosis, hemosiderosis, iron metabolism disease);
  - haemoglobin disorders (sickle cell anaemia, hereditary persistence of fetal haemoglobin);
  - porphyrias;
  - gastrointestinal, liver, gallbladder and kidney disease (including peptic ulcer disease);
  - diabetes-related conditions, hypertension and anxiety disorders;
  - Wilson disease and calcium or phosphorus disorders.
  
  These come from a knowledge graph, and the TGA-approved Product Information (PI) should be consulted for official contraindications.
- **Drug Interactions:** The interaction query returned 80 interactions. Examples from the 20 retrieved:
  - *Moderate:* proton pump inhibitors (rabeprazole, omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole), tetracyclines (doxycycline, tetracycline, minocycline), levofloxacin, antacids (calcium carbonate, magnesium oxide, aluminium hydroxide, magaldrate), pancrelipase, sodium sulfate and triethylenetetramine.
  - *Minor:* cimetidine, zinc sulfate and zinc acetate.
  
  In practice, acid suppression and antacids can reduce iron absorption, and iron can reduce absorption of tetracyclines and quinolones.
- **Literature-derived safety signals:** Oral iron can cause mucosal ulceration, and iron overdose can cause bezoar formation and serious systemic toxicity.

Please refer to the TGA-approved Product Information (PI) for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (non-syndromic esophageal malformation) has no mechanistic rationale, no trials and no literature, and the high TxGNN score is not supported by any clinical data. It may be worth pursuing as a research question.

**To proceed, the following is needed:**
- The TGA-approved Product Information (warnings, contraindications and approved indications) for Ferro-tab, since this is currently missing and blocks safety screening
- Mechanism of action data
- Confirmation that the predicted indications are clinically distinct from the existing anaemia indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

