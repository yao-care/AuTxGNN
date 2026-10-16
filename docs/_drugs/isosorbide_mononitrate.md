---
layout: default
title: Isosorbide Mononitrate
parent: Model Prediction Only (L5)
nav_order: 395
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Isosorbide Mononitrate: predicted new indication Hypertrichosis (disease) (evidence level L5). Approved use: Not available in the data compiled for this report"
---

# Isosorbide Mononitrate
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

# Isosorbide Mononitrate: From an Unspecified Original Indication to Hypertrichosis

## One-Sentence Summary

Isosorbide mononitrate is a nitric oxide (NO) donor and vasodilator. The data compiled for this report do not state its approved indication in Australia.
The TxGNN model predicts it may be effective for **hypertrichosis (disease)**, with a very high score, but **no clinical trials and no publications** currently support this prediction.
The only candidate with any related literature is pulmonary arterial hypertension (rank 10), and that evidence is indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the approved indication text on the ARTG entry is blank) |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.995% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, isosorbide mononitrate is an NO donor. It raises cyclic GMP (cGMP) in vascular smooth muscle and causes vasodilation.

For hypertrichosis, no plausible mechanistic link has been identified. NO-mediated vasodilation has been loosely discussed in hair follicle biology, as with minoxidil, but this is speculative. The high TxGNN score is a graph-based prediction and is not backed by clinical or literature data.

The other top-ranked predictions (Ambras-type hypertrichosis, hair shaft abnormalities, hypotrichosis, alopecia and alopecia areata, and several malformation syndromes) show the same pattern. They appear to cluster around shared hair and ectodermal phenotypes in the knowledge graph. Most are genetic or structural conditions that a vasodilator would not be expected to correct. The only biologically plausible candidate is **pulmonary arterial hypertension (PAH)**, ranked 10th (score 99.94%). The NO-sGC-cGMP pathway is a validated PAH target (PDE5 inhibitors, riociguat). However, organic nitrates are not established in PAH, and concerns include tolerance, systemic hypotension and possible ventilation-perfusion mismatch.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (for hypertrichosis or for the other predicted indications).

---

## Literature Evidence

Currently no related literature available for hypertrichosis.

For reference, the two indirect publications found for the PAH prediction (rank 10) are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16422873](https://pubmed.ncbi.nlm.nih.gov/16422873/) | 2005 | Clinical hemodynamic study | J Sex Med | Haemodynamic effects of sildenafil combined with isosorbide mononitrate in men with coronary artery disease and erectile dysfunction (not a PAH population) |
| [29705351](https://pubmed.ncbi.nlm.nih.gov/29705351/) | 2018 | Preclinical (rat) | Life Sci | Stimulation of NO-sensitive soluble guanylate cyclase in monocrotaline-induced pulmonary hypertensive rats (did not test isosorbide mononitrate) |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13461L | Imdur Durule | Tablet 60 mg (sustained release), oral | Not stated in the data compiled |

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** hypotensive disorder, hypertrophic cardiomyopathy, myocardial infarction, coronary thrombosis, haemoglobinopathy, anaemia (including macrocytic), hyperthyroidism, Graves disease, thyrotoxicosis and intracerebral haemorrhage. These come from graph contraindication edges and need confirmation against the Product Information.
- **Drug interactions:** 100 interactions were identified. Examples rated Moderate include bupropion, morphine, opium, dronabinol, nabilone, sapropterin, rosiglitazone and the SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin). Omeprazole is rated Minor. Several others (e.g. calcitriol, pantoprazole, glimepiride, metformin) have an unknown severity rating.
- **General concern for any non-cardiac use:** systemic nitrate dosing carries risks of hypotension and headache. These would be hard to justify for a cosmetic or dermatological indication.

Please refer to the TGA-approved Product Information (PI) for the full warnings and contraindications, which were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a graph-based score alone (Evidence Level L5), with no registered trials, no relevant publications and no credible mechanism for hypertrichosis. The only plausible candidate, PAH, has just indirect, low-tier evidence and is better treated as a research question than as a repurposing recommendation.

**To proceed, the following is needed:**
- The approved indication text from the TGA PI/ARTG entry, to confirm the original indication
- Mechanism of action data (e.g. from DrugBank)
- The PI warnings and contraindications, to complete safety screening
- For PAH, a focused literature review and, if justified, preclinical or early-phase haemodynamic studies addressing tolerance, hypotension and gas exchange
- No further work on hypertrichosis or the other hair/malformation predictions unless a credible mechanism emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

