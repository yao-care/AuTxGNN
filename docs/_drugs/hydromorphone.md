---
layout: default
title: Hydromorphone
parent: Model Prediction Only (L5)
nav_order: 355
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Hydromorphone: predicted new indication Pharyngitis (evidence level L5). Approved use: Common cold, nasopharyngitis"
---

# Hydromorphone
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

# Hydromorphone: From Common Cold / Nasopharyngitis to Pharyngitis

## One-Sentence Summary

Hydromorphone is a mu-opioid analgesic. In the knowledge graph used by the TxGNN model, its recorded original indications are the **common cold** and **nasopharyngitis**.
TxGNN predicts it may be useful for **pharyngitis**, but the **3 clinical trials** found are all about post-tonsillectomy pain rather than pharyngitis, and **no publications** were found for this indication.
This prediction is best read as a symptom-relief (pain) association, not as evidence of disease-modifying benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Common cold, nasopharyngitis (from the TxGNN knowledge graph; no approved indication text is available for the Australian product) |
| Predicted New Indication | Pharyngitis |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L4 (indirect evidence only; see note below) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

*Note: The evidence level of L4 reflects the assessment compiled for this indication. The trials found do not test hydromorphone for pharyngitis, so in practice the evidence is close to prediction-only.*

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Hydromorphone is, however, a well-known mu-opioid receptor agonist used for moderate to severe pain.

The link to pharyngitis is most plausibly symptomatic. An opioid could reduce the pain of a sore throat, and opioids can suppress cough. Hydromorphone has no antimicrobial, antiviral or anti-inflammatory action against the cause of pharyngitis. The very high TxGNN score (99.81%) probably reflects network proximity to the original indications (common cold, nasopharyngitis) through shared pain and symptom links, and should not be taken as evidence of efficacy.

Other predictions for this drug are weaker still. Allergic urticaria, cold urticaria and papillary conjunctivitis are mechanistically implausible, since opioids can trigger histamine release. Faucial diphtheria, nasal cavity disease, acute laryngopharyngitis, trigeminal autonomic cephalalgia and cervical disc degenerative disorder have no supporting trials or literature. The one exception is headache disorder, which has direct emergency department migraine studies, but these show hydromorphone as a comparator rather than a preferred therapy.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04230681](https://clinicaltrials.gov/study/NCT04230681) | Early Phase 1 | Completed | 189 | Hydromorphone vs fentanyl for pain control in children after tonsillectomy or adenotonsillectomy. Indirect, surgical pain setting. |
| [NCT05244226](https://clinicaltrials.gov/study/NCT05244226) | Phase 2 | Completed | 66 | Short-acting opioids (fentanyl/hydromorphone) vs methadone for pain after paediatric tonsillectomy. Study drug is methadone. |
| [NCT06576830](https://clinicaltrials.gov/study/NCT06576830) | Phase 4 | Recruiting | 440 | Intraoperative methadone vs short-acting opioids (fentanyl/hydromorphone) in paediatric tonsillectomy. Study drug is methadone. |

None of these trials studied pharyngitis. All three are in post-tonsillectomy analgesia, and no ANZCTR identifiers were found in the data compiled for this report.

## Literature Evidence

Currently no related literature available for pharyngitis.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 12010D | Dilaudid | Tablet containing hydromorphone hydrochloride 8 mg | Not available in the data compiled |

This is the only registered entry, and it is an oral single-ingredient product. The listed number is as recorded in the data and should be checked against the ARTG.

## Safety Considerations

- **Contraindications and warnings (knowledge-graph associations, not label text):** The TxGNN knowledge graph links hydromorphone with contraindication or caution for several conditions, including:
  - Respiratory failure
  - Liver failure and liver disease
  - Kidney disease
  - Epilepsy
  - Adrenal insufficiency (including Addison disease and congenital adrenal hyperplasia)
  - Hypothyroidism and myxedema
  - Inflammatory bowel disease and ulcerative colitis
  - Constipation
  - Benign prostatic hyperplasia
  - Hypotension
  - Sudden cardiac arrest and heart conduction disease
  - Gallbladder disease
  - Substance-related disorders and drug dependence
- **Drug Interactions:** The interaction database returned 100 records. The Major-level interactions in the listed entries are:
  - Alvimopan
  - Bupropion
  - Morphine
  - Naltrexone

  Moderate-level interactions include:
  - Anticholinergics (atropine, hyoscyamine, glycopyrronium, dicyclomine, trospium)
  - Loperamide
  - Naloxone
  - Cimetidine
  - Antiemetics (dolasetron, palonosetron)
  - Cannabinoids (dronabinol, nabilone)
  - Eluxadoline
  - Bowel preparations

Product-specific warnings and contraindications from the TGA-approved Product Information (PI) were not available. Please refer to the PI for authoritative safety information. As an opioid, hydromorphone carries recognised risks of respiratory depression, dependence and misuse, which weigh heavily against use for a self-limiting condition such as pharyngitis.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pharyngitis prediction rests on a high model score but no direct evidence. The only trials are post-tonsillectomy pain studies, there is no literature, and the mechanism is symptomatic at best. Opioid risks outweigh any plausible benefit in a usually self-limiting condition.

**To proceed, the following is needed:**
- Product Information (warnings, contraindications and approved indications) for the Australian product
- Mechanism of action data
- Direct clinical evidence in pharyngitis, or a clear justification for symptomatic opioid use compared with standard analgesics
- If any indication is pursued, headache disorder is the only prediction with direct trial and guideline evidence, and it should be framed as a research question given that opioids are not recommended as first-line therapy for migraine
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

