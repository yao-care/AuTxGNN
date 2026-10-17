---
layout: default
title: Celecoxib
parent: Model Prediction Only (L5)
nav_order: 144
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Celecoxib: predicted new indication Acromesomelic dysplasia… (evidence level L5). Approved use: Rheumatoid arthritis, ankylosing spondylitis, osteoarthritis…"
monitor_inn: "Celecoxib"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "rheumatoid nodulosis", "inflammatory spondylopathy", "WHIM syndrome"]
---

# Celecoxib
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

# Celecoxib: From Rheumatoid Arthritis and Ankylosing Spondylitis to Inflammatory Spondylopathy

## One-Sentence Summary

Celecoxib is a COX-2 selective NSAID, originally used for symptomatic treatment of rheumatoid arthritis, osteoarthritis, ankylosing spondylitis and juvenile idiopathic arthritis.
The TxGNN model's top-ranked predictions are mostly rare diseases with no supporting studies. The best-supported prediction is **inflammatory spondylopathy**, with **11 clinical trials** and **20 publications**. However, this largely overlaps with the existing ankylosing spondylitis indication, so it is closer to an on-label use than a true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, ankylosing spondylitis, osteoarthritis, juvenile idiopathic arthritis (from the knowledge graph; no approved indication text is available for the Australian listing) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type (rank 1 by TxGNN score; no supporting evidence). The best-supported prediction, inflammatory spondylopathy (rank 9), is covered below. |
| TxGNN Prediction Score | 99.88% (rank 1 prediction); 99.80% (inflammatory spondylopathy) |
| Evidence Level | L5 for the rank 1 prediction; L1 for inflammatory spondylopathy |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold for the rank 1 prediction; Proceed with Guardrails for inflammatory spondylopathy |

**Other top-ten predictions:**
- Eight have no or minimal supporting evidence and are rated Hold: brachyolmia-amelogenesis imperfecta syndrome, rheumatoid vasculitis, myosclerosis, hypermobility of coccyx, brachyolmia, rheumatoid nodulosis, WHIM syndrome, and the rank 1 prediction itself.
- Rheumatoid factor-positive polyarticular juvenile idiopathic arthritis (rank 8) has one safety registry publication and is rated L3, as a research question. It falls largely within the existing JIA indication.

The rest of this report focuses on inflammatory spondylopathy, the only prediction with substantial evidence.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, celecoxib is a COX-2 selective NSAID. COX-2 inhibition reduces prostaglandin-mediated inflammation and pain, and its efficacy in inflammatory arthritis is well established.

Inflammatory spondylopathy maps to axial spondyloarthritis and ankylosing spondylitis, which are already established celecoxib uses. The prediction is therefore mechanistically sound but not novel. Recent literature suggests that celecoxib may inhibit radiographic bone progression in spondyloarthritis more than other NSAIDs, and may affect sacroiliac joint inflammation through bone metabolism and angiogenesis. These findings are early and not yet confirmed.

For the other nine predictions, the data compiled for this report show no meaningful mechanistic link or clinical evidence. They rest on graph-based prediction alone and should not be pursued without new supporting data.

## Clinical Trial Evidence

Trials registered for inflammatory spondylopathy (11 in total; 10 most relevant shown):

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00648141](https://clinicaltrials.gov/study/NCT00648141) | Phase 3 | Completed | 458 | 12-week comparison of celecoxib 200 mg once daily, 200 mg twice daily and diclofenac in ankylosing spondylitis |
| [NCT00762463](https://clinicaltrials.gov/study/NCT00762463) | Phase 3 | Completed | 240 | Celecoxib 200 mg vs diclofenac SR in Chinese patients with ankylosing spondylitis, with a 6-week extension |
| [NCT02528201](https://clinicaltrials.gov/study/NCT02528201) | Phase 4 | Completed | 330 | Randomised, double-blind comparison of two celecoxib doses vs diclofenac over 12 weeks in ankylosing spondylitis |
| [NCT02758782](https://clinicaltrials.gov/study/NCT02758782) | Phase 4 | Completed | 156 | CONSUL trial: celecoxib added to golimumab vs golimumab alone, looking at spinal structural damage over 2 years |
| [NCT01934933](https://clinicaltrials.gov/study/NCT01934933) | Phase 4 | Completed | 150 | Etanercept and celecoxib alone or combined in active ankylosing spondylitis over 54 weeks |
| [NCT04115098](https://clinicaltrials.gov/study/NCT04115098) | Phase 2 | Terminated | 42 | N-of-1 trials comparing selective COX-2 and non-selective NSAIDs in axial spondyloarthritis; terminated early |
| [NCT03473665](https://clinicaltrials.gov/study/NCT03473665) | Phase 4 | Terminated | 9 | Pilot comparison of four NSAIDs in axial spondyloarthritis; too small to draw conclusions |
| [NCT03190603](https://clinicaltrials.gov/study/NCT03190603) | Phase 4 | Completed | 12 | NSAID effects on inflammatory lesions on MRI in axial spondyloarthritis |
| [NCT02638896](https://clinicaltrials.gov/study/NCT02638896) | Phase 4 | Unknown | 100 | Etanercept dose reduction with sulfasalazine; celecoxib is not the focus |
| [NCT01709656](https://clinicaltrials.gov/study/NCT01709656) | N/A | Completed | 120 | Molecular study of ankylosing spondylitis pathogenesis with stem cell treatment and an NSAID comparator; not a celecoxib treatment trial |

No ANZCTR trial identifiers were available in the data compiled for this report.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38228361](https://pubmed.ncbi.nlm.nih.gov/38228361/) | 2024 | RCT | Ann Rheum Dis | CONSUL trial: effect of adding celecoxib to golimumab on 2-year radiographic spinal progression in r-axSpA |
| [40911151](https://pubmed.ncbi.nlm.nih.gov/40911151/) | 2025 | Umbrella review | Drugs | Synthesis of systematic reviews on celecoxib safety in chronic musculoskeletal conditions |
| [39757202](https://pubmed.ncbi.nlm.nih.gov/39757202/) | 2025 | Comparative study | BMB Rep | Celecoxib was the only NSAID to inhibit bone progression in spondyloarthritis |
| [40676732](https://pubmed.ncbi.nlm.nih.gov/40676732/) | 2025 | N-of-1 trials | Rheumatology (Oxford) | Bayesian N-of-1 trials of celecoxib, meloxicam and naproxen in axial spondyloarthritis |
| [36800138](https://pubmed.ncbi.nlm.nih.gov/36800138/) | 2023 | Clinical study | Clin Rheumatol | Imrecoxib and celecoxib affect sacroiliac joint inflammation via bone metabolism and angiogenesis |
| [40028763](https://pubmed.ncbi.nlm.nih.gov/40028763/) | 2025 | Retrospective cohort | Scand J Rheumatol | Cardiovascular and gastrointestinal bleeding risk comparable between celecoxib and non-selective NSAIDs in ankylosing spondylitis |
| [16960941](https://pubmed.ncbi.nlm.nih.gov/16960941/) | 2006 | Clinical trial | J Rheumatol | Celecoxib efficacious and well tolerated for signs and symptoms of ankylosing spondylitis |
| [17196469](https://pubmed.ncbi.nlm.nih.gov/17196469/) | 2007 | Meta-analysis | Am J Cardiol | Cardiovascular event risk in patients receiving celecoxib across randomised trials |
| [22141388](https://pubmed.ncbi.nlm.nih.gov/22141388/) | 2011 | Review | Drugs | Celecoxib for symptomatic relief in osteoarthritis, rheumatoid arthritis and ankylosing spondylitis |
| [18613804](https://pubmed.ncbi.nlm.nih.gov/18613804/) | 2008 | Review | Expert Opin Drug Saf | Safety of celecoxib in ankylosing spondylitis treatment |

The evidence for the other predictions is minimal. Rheumatoid vasculitis has only a case report of spinal subarachnoid haemorrhage ([34847873](https://pubmed.ncbi.nlm.nih.gov/34847873/)), which does not show celecoxib efficacy. RF-positive polyarticular JIA has one safety registry ([25057265](https://pubmed.ncbi.nlm.nih.gov/25057265/)) comparing celecoxib with non-selective NSAIDs; it supports safety but not subtype-specific efficacy.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 8439E | Celebrex | Capsule 100 mg (oral) | Not available in the data compiled for this report |

## Safety Considerations

**Contraindication signals from the knowledge graph** (these come from graph relationships, not product label text) cover the following conditions:
- Cardiovascular: hypertension, congestive heart failure, myocardial infarction, coronary thrombosis, stroke and cerebrovascular disorders, and other heart disease
- Gastrointestinal: peptic ulcer disease, including active peptic ulcer disease
- Renal, hepatic and biliary: kidney disease, liver disease, gallbladder disease
- Respiratory: asthma (intrinsic and allergic)
- Haematological: anaemia and haemoglobinopathy
- Other: substance abuse/dependence

**Drug interactions:** 100 interactions are recorded. The sample of 20 reviewed includes one Major interaction, with eliglustat. The rest are Moderate and include:
- Antidiabetic agents: metformin, glimepiride, glipizide, glyburide, chlorpropamide, acetohexamide, nateglinide, exenatide
- Aminosalicylates: mesalazine, balsalazide, olsalazine
- Other: hydrocortisone, cimetidine, levofloxacin, metronidazole, kanamycin, naltrexone, fenfluramine, dexfenfluramine

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications, as product-level warning text was not available.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (inflammatory spondylopathy). Hold for the other nine predictions.**

**Rationale:**
- Inflammatory spondylopathy is supported by multiple completed Phase 3 and Phase 4 randomised trials and a recent RCT publication, giving L1 evidence. It is largely an existing indication, so this is not a true new repurposing.
- The other nine predictions, including the top-ranked rare skeletal dysplasias, have no or negligible supporting evidence and lack a plausible mechanistic rationale. They should remain on Hold.

**To proceed, the following is needed:**
- The TGA-approved Product Information, to confirm the registered indications and safety text, as the approved indication text for ARTG 8439E was not available
- Detailed mechanism of action data
- A cardiovascular, gastrointestinal and renal risk assessment for long-term use, with a review of the interaction profile
- Confirmation that the radiographic progression findings are reproducible, since celecoxib's advantage over other NSAIDs is not yet established
- For the rank 1 prediction and the other Hold items, preclinical or mechanistic evidence before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

