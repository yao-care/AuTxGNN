---
layout: default
title: Digoxin
parent: Model Prediction Only (L5)
nav_order: 216
evidence_level: L5
indication_count: 5
monitor_inn: "Digoxin"
predicted_indications: ["Prinzmetal angina", "duodenal obstruction", "duodenal ulcer (disease)", "duodenogastric reflux", "hypoalphalipoproteinemia"]
last_modified_at: 2026-11-17
description: "Digoxin: predicted new indication Prinzmetal angina (evidence level L5). In Australia: 3 PBS items (3 currently listed)"
---

# Digoxin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Digoxin: Cardiac glycoside (Na+/K+-ATPase inhibitor) → Prinzmetal angina (Prinzmetal angina)
{: .text-alpha }

## One-Sentence Summary

Digoxin is a cardiac glycoside available in Australia as an oral tablet. The TxGNN model predicts it may be relevant to **Prinzmetal angina**, but **no clinical trials** and only **1 loosely related publication** were found, so the prediction is not supported by direct evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 0.9981 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (3 of 3 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 3 (valid: 3) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for digoxin: "All of digoxin’s actions are mediated through its effects on Na-K ATPase. This enzyme, the “sodium pump,” is responsible for maintaining the intracellular milieu throughout the body by moving sodium ions out of and potassium ions into cells." ([DailyMed: Lanoxin (digoxin) prescribing information, Covis Pharma US, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9ec84cac-6ecc-43dc-8006-6ccc029e2707), label version 2025-10-17; accessed 2026-11-19.) Digoxin is generally understood to inhibit the Na+/K+-ATPase pump, which raises intracellular calcium in cardiac muscle.

For Prinzmetal angina, which is caused by coronary vasospasm, this mechanism does not offer a clear link. In theory, increased intracellular calcium could raise vascular tone, and cardiac glycosides are generally not favoured in vasospastic angina. The high TxGNN score is a model-based prediction only and is not backed by mechanistic or clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Review | Acta Physiol Pharmacol Bulg | General review of chronopharmacology and antihypertensive treatment; it does not address digoxin in Prinzmetal angina |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1322N | Lanoxin | Tablet 250 micrograms | Not recorded in the local data |

---

## Safety Considerations

Warning and contraindication text is not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for safety information.

**Drug Interactions:** An interaction screen returned 100 interacting drugs. Examples flagged as moderate include:
- Acarbose, rabeprazole, doxycycline, tetracycline, metformin
- Epinephrine, bupropion, acetylsalicylic acid, cholecalciferol, calcium phosphate
- Amphotericin B (including lipid complex)
- Corticosteroids: hydrocortisone, triamcinolone, dexamethasone, betamethasone

Minor interactions include albiglutide, hyoscyamine, atropine and glycopyrronium.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or publication directly studies digoxin in Prinzmetal angina, so the evidence level is L5. The high model score is not supported by a plausible mechanism, and cardiac glycosides are generally not favoured in vasospastic angina.

**To proceed, the following is needed:**
- Mechanistic evidence supporting a role in coronary vasospasm
- Direct clinical or preclinical studies in Prinzmetal angina
- Review of TGA Product Information warnings and contraindications
- A safety assessment covering digoxin's narrow therapeutic window and the interactions listed above

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Lanoxin (digoxin) prescribing information, Covis Pharma US, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9ec84cac-6ecc-43dc-8006-6ccc029e2707) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

