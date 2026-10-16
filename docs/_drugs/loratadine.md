---
layout: default
title: Loratadine
parent: Moderate Evidence (L3-L4)
nav_order: 436
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-13
description: "Loratadine: predicted new indication Allergic urticaria (evidence level L3). Approved use: Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold…"
monitor_inn: "Loratadine"
predicted_indications: ["allergic urticaria", "nasal cavity disease", "acute laryngopharyngitis", "rosacea conjunctivitis", "cold urticaria", "viral conjunctivitis", "punctate epithelial keratoconjunctivitis", "trigeminal autonomic cephalalgia", "faucial diphtheria", "cervical disc degenerative disorder"]
---

# Loratadine
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

# Loratadine: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Loratadine is a second-generation antihistamine, originally used to treat allergic rhinitis and related allergic conditions.
The TxGNN model predicts it may be effective for **allergic urticaria**,
with **1 post-marketing clinical study** and **18 publications** (mostly narrative reviews) currently supporting this direction.
Because idiopathic urticaria is already an original indication, this is a close extension of an existing use rather than a true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, atopic/papillary/vernal conjunctivitis, nasopharyngitis, idiopathic urticaria (the Australian ARTG entry has no indication text recorded) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 98.98% |
| Evidence Level | L3 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the data compiled for this report. Based on known pharmacology, loratadine is a selective peripheral H1-receptor inverse agonist. Histamine released from mast cells drives the wheal-and-flare reaction in allergic urticaria, so H1 blockade directly targets this pathway.

Idiopathic urticaria is already among loratadine's original indications. The prediction is therefore a close extension of an existing indication, not a new therapeutic area. Second-generation H1 antihistamines are widely recognised as the first-line mainstay of urticaria treatment, which is consistent with the model's high score.

The supporting evidence consists of a large post-marketing drug use investigation and literature reviews. There is no randomised trial specifically in this population.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00762983](https://clinicaltrials.gov/study/NCT00762983) | N/A (post-marketing survey) | Completed | 1003 | Drug use investigation of Claritin tablet, RediTabs and dry syrup in children, collecting adverse reactions, symptom scores and symptom improvement. Gives real-world safety and effectiveness data, not controlled efficacy evidence. Relevance to urticaria is likely but not confirmed from the title alone. |

No ANZCTR trial identifiers were found in the data compiled for this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7528133](https://pubmed.ncbi.nlm.nih.gov/7528133/) | 1994 | Review | Drugs | Loratadine was superior to placebo and as effective as several comparator antihistamines in allergic rhinitis and urticaria in controlled studies |
| [11702618](https://pubmed.ncbi.nlm.nih.gov/11702618/) | 2001 | Systematic review | Am J Clin Dermatol | Evidence-based evaluation of antihistamines in urticaria; antihistamines remain the mainstay of treatment |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Review | Ann Pharmacother | Efficacy and safety of first- and newer-generation oral antihistamines in allergic rhinitis and chronic idiopathic urticaria |
| [35396016](https://pubmed.ncbi.nlm.nih.gov/35396016/) | 2022 | Review | Profiles Drug Subst Excip Relat Methodol | Profile of loratadine, widely used for allergic diseases including rhinitis, chronic urticaria and asthma |
| [7530629](https://pubmed.ncbi.nlm.nih.gov/7530629/) | 1994 | Review | Drugs | Non-sedating antihistamines are the mainstay of treatment for most chronic idiopathic urticaria |
| [9951950](https://pubmed.ncbi.nlm.nih.gov/9951950/) | 1999 | Review | Drugs | Comparative review of second-generation antihistamines, including loratadine |
| [20067329](https://pubmed.ncbi.nlm.nih.gov/20067329/) | 2010 | Post-marketing surveillance | Clin Drug Investig | Desloratadine (loratadine's active metabolite) in seasonal allergic rhinitis and chronic urticaria; second-generation antihistamines recommended first line |
| [19348661](https://pubmed.ncbi.nlm.nih.gov/19348661/) | 2009 | Case report | J Dermatol | Rare case of urticaria exacerbated by H1-antihistamines |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 4313B | Claratyne | Tablet 10 mg (oral) | Not recorded in the data compiled for this report |

---

## Safety Considerations

Product Information warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for safety information.

**Other relevant signals from the data compiled:**
- **Knowledge-graph contraindication associations** (these come from a knowledge graph, not label text, and need verification against the PI): hypertension, liver and kidney disease or impaired renal function, gallbladder disease, diabetes mellitus and diabetic ketoacidosis, benign prostatic hyperplasia, coronary artery disease and atherosclerosis, angle-closure glaucoma, and hyperthyroidism (including Graves disease).
- **Drug interactions:** 100 interactions were identified in total. The main graded ones are:
  - Moderate: glycerol phenylbutyrate, troglitazone
  - Minor: clarithromycin, miconazole
  - Many others are listed with an unknown severity level (for example metformin, omeprazole, morphine, doxycycline).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Loratadine already carries an idiopathic urticaria indication and H1 blockade is mechanistically well matched. Evidence is limited to a large post-marketing study and reviews, with no randomised trial in this exact population (L3).

**To proceed, the following is needed:**
- The TGA Product Information, to confirm approved indications, warnings and contraindications (the ARTG entry currently has no indication text)
- Mechanism of action data from DrugBank
- Verification of the knowledge-graph contraindication signals against the PI
- Review of the interaction list, particularly the moderate-level pairs

---

## Other Predicted Indications (Brief Notes)

| Rank | Predicted Indication | Score | Evidence Level | Decision | Comment |
|------|------|------|------|------|------|
| 2 | Nasal cavity disease | 98.98% | L2 | Proceed with Guardrails | Dominated by allergic rhinitis, which is already approved. The only RCT ([PMID 32312261](https://pubmed.ncbi.nlm.nih.gov/32312261/)) used loratadine as the comparator for ginger extract. |
| 3 | Acute laryngopharyngitis | 98.84% | L5 | Hold | Model prediction only; plausible link through the pharyngitis indication. |
| 4 | Rosacea conjunctivitis | 98.51% | L5 | Hold | Weak mechanistic fit; the condition is not mainly histamine-driven. |
| 5 | Cold urticaria | 96.19% | L3 | Research question | Mechanistically reasonable; evidence is a small 1992 comparative study ([PMID 1364168](https://pubmed.ncbi.nlm.nih.gov/1364168/)) plus reviews. |
| 6 | Viral conjunctivitis | 89.26% | L5 | Hold | At most itch relief; no antiviral activity. |
| 7 | Punctate epithelial keratoconjunctivitis | 84.15% | L5 | Hold | No clinical evidence. |
| 8 | Trigeminal autonomic cephalalgia | 80.36% | L4 | Hold | Single case report ([PMID 9195770](https://pubmed.ncbi.nlm.nih.gov/9195770/)); unclear whether loratadine was the agent. |
| 9 | Faucial diphtheria | 78.46% | L5 | Hold | No plausible mechanism; likely an artefact of similarity to pharyngitis. |
| 10 | Cervical disc degenerative disorder | 76.82% | L5 | Hold | No mechanistic rationale or evidence. |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

