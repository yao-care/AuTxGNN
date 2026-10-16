---
layout: default
title: Lanthanum Carbonate
parent: Model Prediction Only (L5)
nav_order: 413
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Lanthanum Carbonate: predicted new indication Dyspepsia (evidence level L5). Approved use: Not stated in the data compiled for this report . Published literatur…"
monitor_inn: "Lanthanum carbonate"
predicted_indications: ["dyspepsia", "infectious otitis media", "otosalpingitis", "middle ear cholesterol granuloma", "allergic otitis media", "chronic otitis media", "middle ear disease", "non-suppurative otitis media", "suppurative otitis media", "pharyngitis"]
---

# Lanthanum Carbonate
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

# Lanthanum Carbonate: From Hyperphosphataemia (Presumed) to Dyspepsia

## One-Sentence Summary

Lanthanum carbonate is an oral, non-calcium phosphate binder (marketed in Australia as Fosrenol), used in chronic kidney disease to control phosphate levels. The TxGNN model predicts it may be effective for **dyspepsia**, but there are **no registered clinical trials** and **no publications that test it as a treatment for dyspepsia**. The prediction therefore rests on computation alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the ARTG entry has no indication text). Published literature describes use for hyperphosphataemia in chronic kidney disease. |
| Predicted New Indication | Dyspepsia |
| TxGNN Prediction Score | 95.11% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, lanthanum carbonate is a non-calcium phosphate binder that works locally in the gastrointestinal tract with minimal systemic absorption. Its efficacy is established in hyperphosphataemia in chronic kidney disease, but a mechanistic basis for treating dyspepsia has not been shown.

The only link between the drug and dyspepsia in the retrieved literature is a case report in which a patient with chronic kidney disease who had taken lanthanum carbonate for three years was biopsied for dyspepsia and had lanthanum deposits in the gastric mucosa. This suggests local gastrointestinal exposure and possible mucosal effects. It points toward caution, not therapeutic benefit. Dyspepsia is more plausibly a tolerability signal than a treatment target.

The high TxGNN score is a knowledge-graph prediction. It is not supported by clinical data. Other top-ranked predictions (middle ear and pharyngeal conditions) also have no identifiable mechanism, which suggests the scores reflect graph proximity rather than biology.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the publications below evaluates dyspepsia as a treatment target.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34602015](https://pubmed.ncbi.nlm.nih.gov/34602015/) | 2021 | Meta-analysis | Renal Failure | Efficacy and safety of lanthanum carbonate versus calcium salts, other binders, sevelamer or placebo for hyperphosphataemia in CKD |
| [21069570](https://pubmed.ncbi.nlm.nih.gov/21069570/) | 2012 | Clinical study | Int Urol Nephrol | Usefulness of lanthanum carbonate for serum phosphate control in difficult-to-control dialysis patients |
| [30902374](https://pubmed.ncbi.nlm.nih.gov/30902374/) | 2019 | Case report | Rev Esp Patol | Lanthanum deposits in the gastric mucosa of a CKD patient biopsied for dyspepsia; clinical significance uncertain |
| [20613851](https://pubmed.ncbi.nlm.nih.gov/20613851/) | 2010 | Cross-sectional study | Nefrologia | Haemodialysis patients' preferences for phosphate binders and their impact on adherence and phosphorus control |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13874F | Fosrenol | Tablet, chewable, 1000 mg (as carbonate hydrate) | Not stated in the data compiled for this report |

## Safety Considerations

- **Gut-related contraindication signals (knowledge graph, not label text):** ileus, intestinal obstruction, constipation disorder and intestinal impaction.
- **Drug Interactions:** 76 interactions were identified. The 20 listed in the data compiled for this report are all rated Moderate. They include:
  - Tetracycline-class antibiotics: doxycycline, minocycline, tetracycline.
  - Fluoroquinolones: levofloxacin, ciprofloxacin, delafloxacin.
  - Bisphosphonates: alendronic acid, risedronic acid.
  - Beta-blockers: acebutolol, atenolol, betaxolol, bisoprolol, carvedilol.
  - ACE inhibitors: benazepril, captopril, enalapril.
  - Others: iron, chloroquine, digoxin, valproic acid.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for dyspepsia has no clinical trials and no supporting studies, and the one related publication is a case report suggesting a possible gastrointestinal adverse effect rather than a benefit. The evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Mechanism of action data to assess any biological link to dyspepsia
- The TGA-approved Product Information (approved indication, warnings and contraindications), as the safety screening cannot proceed without it
- Preclinical or clinical evidence that lanthanum carbonate relieves dyspepsia symptoms
- An assessment of whether gastrointestinal effects of lanthanum, including mucosal deposition, argue against use in dyspepsia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

