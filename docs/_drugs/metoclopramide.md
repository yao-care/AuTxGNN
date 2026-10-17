---
layout: default
title: Metoclopramide
parent: Model Prediction Only (L5)
nav_order: 471
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Metoclopramide: predicted new indication Gastric ulcer (evidence level L5). Approved use: Gastro-oesophageal reflux disease, oesophagitis, peptic oesophagitis"
monitor_inn: "Metoclopramide"
predicted_indications: ["gastric ulcer (disease)", "gastroduodenitis", "gastrojejunal ulcer", "peptic ulcer perforation", "duodenal obstruction", "achlorhydria", "hiatus hernia (disease)", "Dieulafoy lesion", "pylorospasm"]
---

# Metoclopramide
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

# Metoclopramide: From Gastro-oesophageal Reflux Disease to Gastric Ulcer

## One-Sentence Summary

Metoclopramide is a prokinetic and antiemetic medicine, originally used for gastro-oesophageal reflux disease (GORD) and oesophagitis.
The TxGNN model predicts it may be useful for **gastric ulcer**, but the supporting evidence is weak: **1 clinical trial** (a procedural use in upper GI bleeding, not ulcer treatment) and **about 20 publications**, mostly older reviews.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastro-oesophageal reflux disease, oesophagitis, peptic oesophagitis (from the TxGNN knowledge graph; the Australian licence entry has no indication text) |
| Predicted New Indication | Gastric ulcer |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L3 (reviews and physiology studies; no completed Phase 3 RCT for this indication) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, metoclopramide is a dopamine D2 antagonist and 5-HT4 agonist that speeds gastric emptying and upper GI motility, and it raises lower oesophageal sphincter tone.

This mechanism could plausibly reduce gastric stasis and bile (alkaline) reflux, which can aggravate mucosal injury. However, metoclopramide does not suppress acid, protect the mucosa or act against *H. pylori*, so it cannot treat the core pathology of an ulcer. The high TxGNN score most likely reflects overlap with the approved GORD and oesophagitis indications rather than ulcer-specific activity. At best it would be an adjunct for dyspeptic symptoms or delayed gastric emptying.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05746377](https://clinicaltrials.gov/study/NCT05746377) | Phase 4 | Unknown | 60 | Double-blind RCT of metoclopramide premedication in upper GI bleeding, aiming to improve endoscopic visualisation and reduce repeat endoscopy, radiological intervention or surgery. This is a procedural use, not ulcer therapy, and no results are available. |

No Australian (ANZCTR) trials were identified in the data compiled.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [786607](https://pubmed.ncbi.nlm.nih.gov/786607/) | 1976 | Review | Drugs | Pharmacology and clinical use of metoclopramide, including easing emergency endoscopy in upper GI haemorrhage |
| [12825960](https://pubmed.ncbi.nlm.nih.gov/12825960/) | 2003 | Review | Drugs | Diabetic gastroparesis, a condition where prokinetics are relevant |
| [19445547](https://pubmed.ncbi.nlm.nih.gov/19445547/) | 2009 | Systematic review | Paediatric Drugs | Pharmacological management of GORD in children |
| [8686797](https://pubmed.ncbi.nlm.nih.gov/8686797/) | 1996 | Review | Am J Surg | Delayed gastric emptying after gastric surgery, often performed for peptic ulcer disease |
| [579607](https://pubmed.ncbi.nlm.nih.gov/579607/) | 1978 | Review | Can J Surg | Medical treatment of peptic ulcer; metoclopramide discussed as hastening gastric emptying |
| [6782467](https://pubmed.ncbi.nlm.nih.gov/6782467/) | 1981 | Crossover study | MMW Munch Med Wochenschr | In 12 healthy men, metoclopramide did not significantly change serum gastrin or gastric acid secretion |
| [15259526](https://pubmed.ncbi.nlm.nih.gov/15259526/) | 2004 | Review | Am Fam Physician | Evaluation and management of nonulcer dyspepsia |
| [12684590](https://pubmed.ncbi.nlm.nih.gov/12684590/) | 2003 | Review | Rev Gastroenterol Disord | Drug therapy in non-ulcer dyspepsia |
| [8095331](https://pubmed.ncbi.nlm.nih.gov/8095331/) | 1993 | Review | Postgrad Med | Strategies for ulcers and reflux oesophagitis that resist standard regimens |
| [7017896](https://pubmed.ncbi.nlm.nih.gov/7017896/) | 1981 | Review | Scand J Gastroenterol Suppl | Therapeutic implications of duodeno-gastric reflux; some drugs act by enhancing gastric emptying |

Most of these are general reviews on dyspepsia, gastroparesis or reflux. None shows that metoclopramide heals gastric ulcers. Related literature for other predicted indications (for example, recent RCTs of metoclopramide for endoscopic visualisation in upper GI bleeding, PMID 38059896 and 42259699) concerns a procedural use only.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10762K | Metoclopramide Injection BP | Injection containing 10 mg metoclopramide hydrochloride (as monohydrate) in 2 mL | Not stated in the data compiled |

## Safety Considerations

Contraindications and warnings from the product label were not available in the data compiled. Please refer to the TGA-approved Product Information (PI) for full safety information.

**Contraindications and cautions flagged in the knowledge graph** (these are not label text and should be verified against the PI): phaeochromocytoma and other catecholamine-secreting tumours, epilepsy, hypertension, Parkinson disease and parkinsonian disorders, tardive dyskinesia, neuroleptic malignant syndrome, torsion dystonia, porphyria, impaired renal function, cirrhosis, active peptic ulcer disease, anxiety and related disorders, and methaemoglobinaemia due to methaemoglobin reductase deficiency.

**Drug interactions:** the interaction screen returned 100 entries; the first 20 reviewed included:
- **Major:** tramadol, amisulpride
- **Moderate:** opioids (fentanyl, alfentanil, codeine, dihydrocodeine), sedating antihistamines (chlorpheniramine, cetirizine), alprazolam, amitriptyline, amobarbital, ethanol, amantadine, abiraterone, amifampridine
- **Minor:** acetaminophen

Many of the moderate interactions involve additive central nervous system depression.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Metoclopramide has no acid-suppressive or cytoprotective action, the only registered trial tests a procedural use rather than ulcer healing, and the literature is largely generic and dated. The high TxGNN score appears to reflect overlap with the existing GORD indication. Several knowledge-graph contraindications, including active peptic ulcer disease, also conflict with the proposed use.

**To proceed, the following is needed:**
- Mechanism of action data and TGA Product Information warnings and contraindications (currently missing)
- Evidence from controlled trials showing a clinical benefit in gastric ulcer, such as healing rates or symptom relief as an adjunct to standard therapy
- Clarification of the knowledge-graph contraindication relating to active peptic ulcer disease
- Confirmation of the approved indication text for the Australian ARTG entry
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

