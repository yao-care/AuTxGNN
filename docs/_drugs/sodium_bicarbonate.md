---
layout: default
title: Sodium Bicarbonate
parent: Moderate Evidence (L3-L4)
nav_order: 635
evidence_level: L3
indication_count: 10
---

# Sodium Bicarbonate
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

Using superpowers:using-superpowers checked — no listed skill matches "write a drug-repurposing evaluation report from a supplied Evidence Pack" (txgnn-pipeline covers model/pipeline ops, not report authoring), so proceeding directly per the detailed format already specified in the prompt.

A few notes before the report: `original_moa` and `original_indications` are both empty/Data Gap in this pack, and `taiwan_regulatory.licenses` is empty (0 ARTG entries, market status "Not marketed"/Not Marketed) — so I'm not fabricating Australian regulatory specifics for those fields, only using well-established general pharmacology of sodium bicarbonate as a systemic alkalinising agent, flagged as such.

---

# Sodium Bicarbonate: From Metabolic Acidosis Correction to Bronchitis

## One-Sentence Summary

Sodium bicarbonate is a systemic alkalinising agent whose original approved indications are not recorded in this evidence pack (and it is not currently marketed in Australia).
The TxGNN model predicts it may be effective for **bronchitis**, with **4 clinical trials** and **5 publications** currently associated with this prediction — though most of the trial evidence is of low direct relevance.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (`original_indications` and `original_moa` are data gaps); sodium bicarbonate is generally known as a systemic alkalinising agent (e.g., metabolic acidosis correction) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 97.91% |
| Evidence Level | L3 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (`original_moa` = data gap). Based on general pharmacological knowledge, sodium bicarbonate acts systemically as an alkalinising agent; in the airway, alkalinisation of mucus is understood to reduce viscosity and promote mucociliary clearance. The repurposing rationale notes that CFTR-mediated epithelial bicarbonate secretion abnormalities are implicated in COPD/chronic bronchitis pathology (PMID 23934925), providing a plausible — but indirect — mechanistic bridge.

Two Soviet-era case series (PMID 2838916, PMID 2846955) specifically describe endobronchial administration of expectorant therapy (consistent with bicarbonate-type alkalinising agents) in chronic bronchitis patients, which is the most directly relevant evidence for this pairing. However, this is a supportive/adjunctive mucolytic role rather than treatment of the underlying infective or inflammatory process, and none of the identified clinical trials directly test sodium bicarbonate in a bronchitis population.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02981602](https://clinicaltrials.gov/study/NCT02981602) | Phase 2 | Completed | 31 | Dose-escalation safety/tolerability study of IONIS-HBVRx in chronic HBV — drug identity does not match sodium bicarbonate; low relevance (Grade C) |
| [NCT01163253](https://clinicaltrials.gov/study/NCT01163253) | Phase 3 | Terminated | 2,867 | Long-term safety of CP-690,550 (tofacitinib) in chronic plaque psoriasis — unrelated to sodium bicarbonate/bronchitis; low relevance (Grade C) |
| [NCT02469298](https://clinicaltrials.gov/study/NCT02469298) | Phase 2 | Completed | 45 | Safety/tolerability of danirixin ± oseltamivir in acute influenza — unrelated drug; low relevance (Grade C) |
| [NCT01421160](https://clinicaltrials.gov/study/NCT01421160) | Phase 1 | Withdrawn | 0 | Pilot study on urine pH regulation for chronic joint pain — withdrawn, no enrolment, unrelated to bronchitis (Grade C) |

**None of the identified trials directly evaluate sodium bicarbonate for bronchitis** — all are graded C (low relevance) in the evidence pack, likely reflecting disease-label co-occurrence rather than a true drug-disease match.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2838916](https://pubmed.ncbi.nlm.nih.gov/2838916/) | 1988 | Case series | Sovetskaia meditsina | Endobronchial expectorant therapy in chronic bronchitis patients |
| [2846955](https://pubmed.ncbi.nlm.nih.gov/2846955/) | 1988 | Case series | Klinicheskaia meditsina | Endobronchial therapy in patients with chronic bronchitis |
| [23934925](https://pubmed.ncbi.nlm.nih.gov/23934925/) | 2013 | Review | Am J Physiol Lung Cell Mol Physiol | CFTR-mediated bicarbonate secretion abnormalities implicated in COPD/chronic bronchitis pathogenesis |
| [16424422](https://pubmed.ncbi.nlm.nih.gov/16424422/) | 2006 | Clinical study (comparator) | Chest | Compares albuterol enantiomer formulations on airway secretions in intubated patients; not a sodium bicarbonate study |
| [778960](https://pubmed.ncbi.nlm.nih.gov/778960/) | 1976 | Physiology study | Respiration | Effect of ventilation hypercapnia on pulmonary vascular response; general respiratory physiology, not a treatment study |

## Australia Market Information

Sodium bicarbonate currently has **no ARTG entries** on record in this evidence pack — the drug is marked as **not marketed** in Australia (`total_licenses = 0`).

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. This evidence pack contains a **blocking data gap (DG001)**: TFDA/TGA label warnings and contraindications could not be retrieved, and drug interaction lookup returned no results (`query_status: not_found`), so no drug-specific safety detail can be reported here.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only directly relevant clinical evidence for sodium bicarbonate in bronchitis consists of two small, decades-old (1988) case series from non-indexed abstracts, with no modern controlled trials specifically testing this pairing; the four identified clinical trials are unrelated drugs/populations (Grade C relevance). Combined with a **Blocking**-severity safety data gap (no TFDA/TGA label data available) and the drug not currently being marketed in Australia, the evidence does not yet support proceeding.

**To proceed, the following is needed:**
- TGA-approved Product Information (label warnings/contraindications) — currently a blocking data gap (DG001)
- Mechanism of action data from DrugBank or equivalent — currently a data gap (DG002)
- Confirmation of ARTG registration pathway, since the drug is not currently marketed in Australia
- Contemporary controlled studies (ideally RCTs) directly testing sodium bicarbonate (oral or nebulised) in chronic bronchitis, to replace the existing 1980s case-series evidence
- Drug-drug interaction data (current query status: not found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

