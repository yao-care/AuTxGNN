---
layout: default
title: Propantheline
parent: Moderate Evidence (L3-L4)
nav_order: 607
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Propantheline: predicted new indication Gastroduodenitis (evidence level L4). Approved use: Peptic ulcer disease"
monitor_inn: "Propantheline"
predicted_indications: ["gastroduodenitis", "irritable bowel syndrome", "acute laryngopharyngitis", "nasal cavity disease", "pharyngitis", "bronchitis", "overactive bladder (disease)", "gastroenteritis", "cauda equina syndrome", "large intestine disease"]
---

# Propantheline
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Propantheline: From Peptic Ulcer Disease to Gastroduodenitis

## One-Sentence Summary

Propantheline is an antimuscarinic (anticholinergic) drug, originally used to treat peptic ulcer disease.
The TxGNN model predicts it may be effective for **gastroduodenitis**, but there are **no registered clinical trials** and only **3 publications** (1956-1983), all indirect.
The strongest repurposing signal in the data is actually for **overactive bladder**, which has **1 clinical trial** and several class-level systematic reviews (see the note below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease (the Australian ARTG entry has no approved indication text, so this comes from the knowledge graph) |
| Predicted New Indication | Gastroduodenitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

**Other predicted indications (for context):**

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|------|------|------|------|
| 2 | Irritable bowel syndrome | 99.16% | L4 | Research Question |
| 3 | Acute laryngopharyngitis | 98.58% | L5 | Hold |
| 4 | Nasal cavity disease | 98.55% | L5 | Hold |
| 5 | Pharyngitis | 97.98% | L5 | Hold |
| 6 | Bronchitis | 93.15% | L5 | Hold |
| 7 | Overactive bladder | 89.20% | L3 | Research Question |
| 8 | Gastroenteritis | 88.28% | L4 | Hold |
| 9 | Cauda equina syndrome | 86.87% | L5 | Hold |
| 10 | Large intestine disease | 76.86% | L5 | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, propantheline is a muscarinic receptor antagonist. It reduces gastric acid secretion and gastrointestinal motility, which is consistent with its original use in peptic ulcer disease.

Gastroduodenitis shares much of the same pathophysiology as gastroduodenal ulcer (acid-related mucosal injury and increased motility), so the prediction is biologically plausible. However, the available literature concerns gastroduodenal ulcer rather than gastroduodenitis itself. It is also largely historical, and the one controlled trial found no added benefit from propantheline when combined with cimetidine. The evidence is therefore indirect.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for gastroduodenitis.

For reference, one trial is registered for the rank 7 prediction, overactive bladder:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01640002](https://clinicaltrials.gov/study/NCT01640002) | Phase 1 | Unknown | 42 | Double-blind, placebo-controlled study of propantheline for overactive bladder in HTLV-1 infected patients. The aim was a 60% reduction in nocturia and frequency. No results are available. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6342335](https://pubmed.ncbi.nlm.nih.gov/6342335/) | 1983 | Double-blind clinical trial | Acta Med Scand | In 58 outpatients with gastroduodenal ulcer, cimetidine plus low-dose propantheline (45 mg/day) did not differ significantly from cimetidine plus placebo in ulcer healing or symptom relief at 3 or 6 weeks. |
| [761954](https://pubmed.ncbi.nlm.nih.gov/761954/) | 1979 | Pharmacokinetic/secretion study | Int J Clin Pharmacol Biopharm | Trithiozine was compared with propantheline for suppression of gastric secretion. Propantheline reduced gastric juice volume and acid output after histamine stimulation more effectively than trithiozine. |
| [13392433](https://pubmed.ncbi.nlm.nih.gov/13392433/) | 1956 | Clinical report | Vie Med | Report on anticholinergic treatment of gastroduodenal ulcer using propantheline (no abstract available). |

**Supporting literature for the other predictions (class-level or indirect):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17054185](https://pubmed.ncbi.nlm.nih.gov/17054185/) | 2006 | Cochrane systematic review | Cochrane Database Syst Rev | Anticholinergics versus placebo for overactive bladder in adults (class-level, not specific to propantheline). |
| [19160231](https://pubmed.ncbi.nlm.nih.gov/19160231/) | 2009 | Cochrane systematic review | Cochrane Database Syst Rev | Anticholinergics for urinary symptoms in multiple sclerosis (class-level). |
| [2697886](https://pubmed.ncbi.nlm.nih.gov/2697886/) | 1989 | RCT | Q J Med | Long-term irritable bowel syndrome treatment after initial therapy with ispaghula husk and propantheline (28 patients). The contribution of propantheline alone is unclear. |
| [2888056](https://pubmed.ncbi.nlm.nih.gov/2888056/) | 1987 | Multicentre clinical study | Minerva Dietol Gastroenterol | Bromazepam plus propantheline combination in irritable bowel syndrome (the combination confounds the effect of propantheline). |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13927B | Pro-Banthine | Tablet containing propantheline bromide 15 mg (oral) | Not specified in the data compiled for this report |

---

## Safety Considerations

Product Information warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for safety information.

**Contraindication signals from the knowledge graph (not label text):** the knowledge graph links propantheline with contraindications in the following conditions, which are consistent with the known effects of anticholinergics:
- **Gastrointestinal:** intestinal obstruction, paralytic ileus, toxic megacolon, ulcerative colitis and inflammatory bowel disease, achalasia and megaesophagus, pyloric stenosis, hiatus hernia, familial visceral myopathy
- **Genitourinary:** benign prostatic hyperplasia, bladder neck obstruction
- **Eye:** angle-closure glaucoma
- **Neuromuscular:** myasthenia gravis and neuromuscular junction disease
- **Cardiovascular and endocrine:** hypertension, coronary artery disease, hyperthyroidism (including Graves disease)
- **Organ impairment:** kidney disease, liver disease, gallbladder disease

**Drug interactions:** 100 interactions were identified, mostly of moderate severity. Examples include:
- **Other anticholinergic or antimuscarinic agents (additive effects):** aclidinium, hyoscyamine, homatropine, amitriptyline, amantadine
- **Sedating antihistamines:** chlorpheniramine, acrivastine, phenyltoloxamine
- **Opioids and CNS depressants:** fentanyl, alfentanil, codeine, dihydrocodeine, tramadol, ethanol
- **Others:** botulinum toxin type A, acetylcholine, loperamide, acebutolol
- **Minor interactions:** acetaminophen, hydrochlorothiazide

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The gastroduodenitis prediction scores highly (99.90%), but there are no registered trials. The few publications are old, indirect, and concern gastroduodenal ulcer. The one controlled trial showed no added benefit when propantheline was added to cimetidine. Modern acid suppression with proton pump inhibitors also makes an anticholinergic add-on of limited interest.

**To proceed, the following is needed:**
- Direct clinical evidence of propantheline in gastroduodenitis (for example, a well-designed controlled trial)
- Mechanism of action data (for example, from DrugBank)
- The TGA-approved Product Information, including approved indications, warnings and contraindications (the ARTG entry has no indication text in the compiled data)
- A safety review of anticholinergic burden, particularly in older patients and those with the contraindicated conditions above
- If the programme is redirected, overactive bladder (rank 7, L3) is the most advanced alternative. Next steps there would be the results and status of NCT01640002 and propantheline-specific efficacy data.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

