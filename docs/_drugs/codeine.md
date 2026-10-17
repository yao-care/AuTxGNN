---
layout: default
title: Codeine
parent: Model Prediction Only (L5)
nav_order: 182
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Codeine: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold…"
monitor_inn: "Codeine"
predicted_indications: ["trigeminal autonomic cephalalgia", "allergic urticaria", "faucial diphtheria", "cervical disc degenerative disorder", "papillary conjunctivitis", "tracheal disease", "cold urticaria", "bronchial disease"]
---

# Codeine
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

# Codeine: From Allergic Rhinitis and Related Upper Respiratory Conditions to Nasal Cavity Disease

## One-Sentence Summary

Codeine is an opioid medicine originally used for symptomatic relief in conditions such as allergic rhinitis, pharyngitis, the common cold and headache disorders.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but there are **no registered clinical trials** and only **1 publication** (a case report describing a complication, not a treatment effect).
This prediction should be treated as weak and not clinically actionable.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, rhinitis, nasopharyngitis, headache disorder (from the TxGNN knowledge graph; no approved indication text was available for the Australian entries) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 (model prediction with only a case report; no supporting clinical study) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Codeine is a well-known opioid with centrally acting antitussive and analgesic properties, and it is established in symptomatic management of cough and pain. This general pharmacology is background knowledge, not something drawn from the data compiled for this report.

The predicted indication, nasal cavity disease, is closely related to the original rhinitis and nasopharyngitis indications in the knowledge graph. The high score most likely reflects network proximity to those existing indications rather than a new therapeutic mechanism. The only literature found is a case report of rhinolithiasis formed around an impacted foreign body, which turned out to be a hardened mixture of codeine and opium (an "opioma"). That describes a drug-related complication, not a benefit.

Overall, the prediction is an extension of existing symptomatic uses rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17315836](https://pubmed.ncbi.nlm.nih.gov/17315836/) | 2007 | Case report | Ear, Nose & Throat Journal | Unusual unilateral rhinolith in a 21-year-old man, formed around a foreign body that was a hardened codeine and opium mixture. Describes a complication, not therapeutic benefit. |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12054K | Aspen Pharmacare Australia Pty Ltd (sponsor name listed as product) | Tablet containing codeine phosphate hemihydrate 30 mg (oral) | Not available in the data compiled |
| ARTG 191C | Not available | Not available | Not available in the data compiled |

---

## Safety Considerations

No label-based warnings or contraindications were available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for authoritative safety information.

The following items come from other sources and are supplementary only:

- **Knowledge-graph contraindication signals (not label text)**: hypertension, liver failure and liver disease, kidney disease, epilepsy, insomnia, chronic obstructive pulmonary disease, anxiety and other mental disorders (including psychotic disorders), porphyria, pancreatitis, gallbladder disease, thrombocytopenia, hypothyroidism, peptic ulcer disease, inflammatory bowel disease, gastritis and dermatitis herpetiformis.
- **Drug interactions**: 100 interactions were identified in the interaction database, and 20 are listed in the data compiled. Major-level interactions include **alvimopan** and **bupropion**. Moderate-level interactions include anticholinergics (atropine, clidinium, dicyclomine, glycopyrronium, hyoscyamine), antidiarrhoeals (loperamide, kaolin, attapulgite), cimetidine, dexamethasone, 5-HT3 antagonists (dolasetron, granisetron), dronabinol, eliglustat, eluxadoline, fenfluramine and dexfenfluramine, and glycerol phenylbutyrate.
- **Literature safety signals**: codeine is a non-immunologic mast cell histamine releaser that can provoke urticaria, it can cause bronchoconstriction in asthmatic subjects, and ultrarapid CYP2D6 metabolism has been linked to postoperative death. Misuse of paracetamol-codeine combination products has been associated with unintentional deaths in Australia.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a case report of a codeine-related complication, with no clinical trials and no evidence of therapeutic benefit. The high TxGNN score appears to reflect proximity to existing rhinitis indications, and opioid safety concerns are well documented.

**To proceed, the following is needed:**
- Mechanism of action data (currently unavailable)
- Product Information warnings and contraindications from the Australian regulatory source, so that safety screening can be completed
- Approved indication text for the two ARTG entries
- A clear clinical rationale and hypothesis for benefit in nasal cavity disease beyond existing symptomatic uses
- Any controlled clinical evidence, which would be required before reconsidering

---

### Other Predicted Indications (Brief Note)

None of the other predictions in the data compiled justify advancing either:

- **Acute laryngopharyngitis, faucial diphtheria, cervical disc degenerative disorder, papillary conjunctivitis:** model prediction only, with no trials or literature (L5, Hold).
- **Trigeminal autonomic cephalalgia:** the literature has no evidence of codeine efficacy, and opioids are generally not recommended for cluster headache (L4, Hold).
- **Allergic urticaria and cold urticaria:** the literature describes codeine causing, or being used to test for, mast cell histamine release, which is a safety or diagnostic signal rather than a therapeutic one (L4, Hold).
- **Tracheal disease:** antitussive plausibility exists, but the evidence is mostly preclinical or concerns other agents (L4, Hold).
- **Bronchial disease:** this is the most developed signal (L3, flagged as a research question). It includes antitussive efficacy and kinetics studies and chronic cough guidelines, but there are opposing safety signals, including bronchoconstriction in asthmatic subjects, and no registered trials. It overlaps with existing cough-related uses and would need a careful risk-benefit evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

