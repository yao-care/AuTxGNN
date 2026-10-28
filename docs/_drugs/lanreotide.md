---
layout: default
title: Lanreotide
parent: Model Prediction Only (L5)
nav_order: 411
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
monitor_inn: "Lanreotide"
predicted_indications: ["hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "Ambras type hypertrichosis universalis congenita"]
description: "Lanreotide: predicted new indication Hypertrichosis (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Lanreotide
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

## Lanreotide: Hypertrichosis (disease)
{: .text-alpha }

## One-Sentence Summary

Lanreotide is a long-acting somatostatin analogue, originally used to treat **acromegaly** and related pituitary growth hormone excess conditions.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Lanreotide is a somatostatin analogue that acts mainly through somatostatin receptors SSTR2 and SSTR5. This suppresses growth hormone (GH), IGF-1 and other hormones, which is the basis of its use in acromegaly. Detailed mechanism of action data were not available in the data compiled for this report, so this description reflects general knowledge of the drug class.

For hypertrichosis, **no plausible mechanistic link has been identified**. Nothing suggests that somatostatin receptor agonism influences hair growth disorders, and hypertrichosis is not a recognised treatment target for lanreotide. The other top-five predictions show the same pattern: hair shaft abnormalities, Ambras-type hypertrichosis universalis congenita, a dental/periodontal malformation syndrome and a Dandy-Walker malformation syndrome. None has any trial or publication support.

Cholangiocytes and renal cyst epithelium express somatostatin receptors. Lanreotide lowers cAMP through this signalling, which reduces fluid secretion and cell proliferation and slows cyst and liver volume growth. This is the more credible repurposing direction for lanreotide.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for hypertrichosis, and none for the other predictions in the data compiled for this report.

---

## Literature Evidence

No literature is available for hypertrichosis.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19646443](https://pubmed.ncbi.nlm.nih.gov/19646443/) | 2009 | RCT (double-blind, placebo-controlled) | Gastroenterology | Lanreotide reduced polycystic liver volume in ADPKD or isolated polycystic liver disease |
| [31022403](https://pubmed.ncbi.nlm.nih.gov/31022403/) | 2019 | RCT (open-label randomised data) | Gastroenterology | Lanreotide reduced liver growth in ADPKD, assessed by height-adjusted liver and kidney volume |
| [25369108](https://pubmed.ncbi.nlm.nih.gov/25369108/) | 2015 | RCT (RESOLVE trial) | Liver Int | 6 months of lanreotide 120 mg every 4 weeks in ADPKD with polycystic liver |
| [23799922](https://pubmed.ncbi.nlm.nih.gov/23799922/) | 2013 | Pooled analysis of RCTs | Aliment Pharmacol Ther | Safety and efficacy of different lanreotide doses in polycystic liver disease |
| [42476150](https://pubmed.ncbi.nlm.nih.gov/42476150/) | 2026 | Network meta-analysis | Clin Transl Gastroenterol | Compared octreotide, lanreotide and pasireotide in ADPKD and polycystic liver disease, with adverse event data |
| [26688394](https://pubmed.ncbi.nlm.nih.gov/26688394/) | 2016 | Review | Ann R Coll Surg Engl | Systematic review of somatostatin analogues and mTOR inhibitors for polycystic liver disease |
| [26126910](https://pubmed.ncbi.nlm.nih.gov/26126910/) | 2015 | Review | Curr Top Med Chem | SSTR/cAMP rationale for lanreotide in polycystic kidney and liver diseases |
| [22111942](https://pubmed.ncbi.nlm.nih.gov/22111942/) | 2012 | Cohort (long-term follow-up) | Aliment Pharmacol Ther | Long-term outcomes of lanreotide in polycystic liver disease |
| [38071418](https://pubmed.ncbi.nlm.nih.gov/38071418/) | 2024 | Post hoc cohort analysis | Eur J Clin Invest | Serum bile acids track liver volume and fall with lanreotide |
| [33779943](https://pubmed.ncbi.nlm.nih.gov/33779943/) | 2021 | Safety study | Drugs R D | Gallstones during somatostatin analogue treatment are linked to acute biliary complications, especially after discontinuation |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form |
|---------|------|------|
| ARTG 11289E | Mytolac | Injection 120 mg (as acetate) in single dose pre-filled syringe |

---

## Safety Considerations

- **Disease-related cautions (knowledge graph, not label text):** The knowledge graph links lanreotide with caution in the following conditions: hypertension, liver disease, gallbladder disease and gallstones (cholelithiasis, choledocholithiasis), hyperglycaemia, hypoglycaemia, hypothyroidism (including myxedema and congenital hypothyroidism), and impaired renal function.
- **Drug Interactions:** The interaction screen returned 100 interactions, of which the 20 reviewed were all rated Moderate. They are mainly with glucose-lowering agents, because somatostatin analogues can alter glucose control. Examples include:
  - metformin, pioglitazone, acarbose and glimepiride
  - SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin)
  - DPP-4 inhibitors (alogliptin, linagliptin)
  - GLP-1 agonists (semaglutide, dulaglutide, albiglutide)
  - several insulins
- **Literature signals:** Gallstones are a known adverse effect, with a risk of acute biliary complications, especially after discontinuation (PMID 33779943).

Please refer to the TGA-approved Product Information (PI) for the official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold** (for the rank 1 prediction, hypertrichosis)

**Rationale:**
- Hypertrichosis has a very high model score but no trials, no literature and no plausible mechanism (Evidence Level L5). It should not be pursued.
- It is graded L1 and would warrant **Proceed with Guardrails** if assessed as its own candidate. Liver volume reductions are consistent but modest, kidney benefit is weaker, and effects may wane after stopping treatment.

**To proceed, the following is needed:**
- Re-rank the candidates so that the evidence-supported indication (polycystic liver or kidney disease) is assessed as the primary one.
- Confirm study designs and outcomes from the full texts. The L1 grade currently rests on titles and abstracts, and no registered trials were found in the data compiled for this report.
- Obtain detailed mechanism of action data and the TGA Product Information warnings and contraindications.
- Define guardrails for a polycystic liver disease use: restrict to symptomatic or severe disease, monitor for gallstones, gastrointestinal adverse effects and glucose disturbance, and weigh cost and the need for long-term therapy.
- Check the approved indication text for the ARTG entry, which was not available in the data compiled for this report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

