---
layout: default
title: Fentanyl
parent: Model Prediction Only (L5)
nav_order: 291
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Fentanyl: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Not available in the data compiled for this report . Fentanyl is gene…"
monitor_inn: "Fentanyl"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "Tourette syndrome", "trichotillomania", "myofascial pain syndrome", "manic bipolar affective disorder", "migraine with brainstem aura", "methemoglobinemia", "myositis fibrosa", "idiopathic granulomatous myositis", "tendinitis"]
---

# Fentanyl
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

# Fentanyl: From Pain Management (Original Indication Not Recorded) to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Fentanyl is a potent mu-opioid analgesic, and the sublingual tablet is registered in Australia (ARTG entry for Abstral). The TxGNN model's top prediction is **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but there are **0 clinical trials** and **0 publications** supporting it. The evidence is model prediction only. The only prediction with a registered Phase 3 trial is **myofascial pain syndrome** (rank 4), and that link is unverified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the ARTG entry has no indication text). Fentanyl is generally used as an opioid analgesic, and the Abstral sublingual tablet is used for breakthrough pain. |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Fentanyl is known to be a mu-opioid receptor agonist used for analgesia.

For the top prediction, **the mechanistic link is weak**. NSIAD is caused by gain-of-function variants in the vasopressin V2 receptor (AVPR2) pathway. Fentanyl has no known direct action on this receptor. Opioids can modulate antidiuretic hormone release, but that would not correct a receptor-level defect. The high score (0.995) reflects a graph-based prediction only.

Other predictions fare similarly:

- **Tourette syndrome, trichotillomania, manic bipolar disorder, migraine with brainstem aura:** There is no supportive treatment evidence. Opioid-system involvement has been hypothesised for tic and compulsive disorders, but the agents studied there are antagonists such as naltrexone, not agonists. Opioids are generally discouraged in migraine because of medication-overuse headache.
- **Methemoglobinemia:** The literature describes it as an adverse event from other drugs (for example topical benzocaine) in settings where fentanyl was co-administered. This is co-occurrence, not treatment.
- **Myositis fibrosa, idiopathic granulomatous myositis:** There is no evidence. They share an identical score, which suggests a shared graph neighbourhood rather than independent evidence.
- **Tendinitis:** The literature concerns postoperative analgesia after shoulder surgery, not treatment of tendinitis itself.
- **Myofascial pain syndrome (rank 4):** This is the most biologically coherent candidate, since fentanyl is an analgesic used in chronic pain. However, long-term opioid use in musculoskeletal pain carries risks of tolerance, dependence and hyperalgesia.

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked indication (NSIAD). Currently no related clinical trials registered.

For reference, one trial was linked to the rank 4 prediction (myofascial pain syndrome):

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00343733](https://clinicaltrials.gov/study/NCT00343733) | Phase 3 | Completed | 120 | 12-week open-label study with three within-patient double-blind, placebo-controlled periods of OraVescent fentanyl citrate for breakthrough pain in opioid-tolerant patients with noncancer chronic pain. The population is chronic noncancer pain, not confirmed as myofascial pain, so relevance is unverified. |

No ANZCTR identifiers were available in the data compiled for this report.

## Literature Evidence

No literature is available for NSIAD. Currently no related literature available.

For reference, the most relevant publications linked to lower-ranked predictions are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23809446](https://pubmed.ncbi.nlm.nih.gov/23809446/) | 2013 | RCT | Arthroscopy | Postoperative fentanyl patch versus subacromial bupivacaine infusion after arthroscopic shoulder surgery (tendinitis prediction; addresses surgical pain, not tendinitis) |
| [21419546](https://pubmed.ncbi.nlm.nih.gov/21419546/) | 2011 | Review | J Oral Maxillofac Surg | Long-term opioid use in temporomandibular joint dysfunction can be neither supported nor refuted; evidence supports opioids in other chronic noncancer pain states (myofascial pain prediction) |
| [12369265](https://pubmed.ncbi.nlm.nih.gov/12369265/) | 2002 | Mechanistic pilot study | Prog Neuropsychopharmacol Biol Psychiatry | Fentanyl-induced prolactin response used as an opiate receptor sensitivity test in stereotypic movement disorder and trichotillomania; a diagnostic probe, not a treatment study |
| [15102255](https://pubmed.ncbi.nlm.nih.gov/15102255/) | 2001 | Case report | Pain Medicine | Limited absorption of transdermal fentanyl in two patients with systemic sclerosis, one treated for deltoid tendinitis pain |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10600X | Abstral | Tablet (sublingual) 200 micrograms (as citrate) | Not stated in the data compiled for this report |

## Safety Considerations

Safety information from the TGA-approved Product Information was not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI).

- **Drug Interactions:** 100 interactions were identified. Examples rated **Major**: alvimopan, aprepitant, bupropion, clarithromycin, clotrimazole, dexamethasone, dexfenfluramine, dolasetron, fenfluramine, granisetron and lorcaserin. Examples rated **Moderate**: atropine, cimetidine, clidinium, dicyclomine, dronabinol, eluxadoline, glycopyrronium and hyoscyamine.
- **Knowledge-graph contraindication signals** (from a knowledge graph, not label text): hypertension, orthostatic and other hypotensive disorders, long QT syndrome and torsades de pointes, liver failure and liver disease, kidney disease, chronic obstructive pulmonary disease, asthma, pancreatitis, gallbladder disease, inflammatory bowel disease, benign prostatic hyperplasia, anxiety and related disorders, and substance abuse/dependence.
- **General class concerns noted in the evidence:** abuse liability, respiratory depression, tolerance and dependence, and medication-overuse headache.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (NSIAD) has no clinical or published support and no plausible mechanistic link, because the disease is driven by a receptor-level defect that fentanyl does not address. Overall evidence is L5, and the safety profile of a potent opioid calls for caution.

**To proceed, the following is needed:**
- Mechanism of action data for fentanyl
- The approved indication text and Product Information (warnings and contraindications) for the Abstral ARTG entry
- For myofascial pain syndrome (the only candidate with a Phase 3 trial): verification that NCT00343733 tested fentanyl in the relevant population, followed by a risk-benefit review of long-term opioid use
- Route compatibility assessment (not yet completed)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

