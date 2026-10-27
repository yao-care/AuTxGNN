---
layout: default
title: Apremilast
parent: Model Prediction Only (L5)
nav_order: 56
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Apremilast: predicted new indication Migraine disorder (evidence level L5). Approved use: Psoriatic arthritis"
monitor_inn: "Apremilast"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "pulmonary hypertension", "migraine with or without aura, susceptibility to", "kyphoscoliotic heart disease", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "atrophoderma vermiculata", "ulerythema ophryogenesis"]
---

# Apremilast
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Apremilast: From Psoriatic Arthritis to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Apremilast is an oral PDE4 inhibitor, originally used to treat psoriatic arthritis.
The TxGNN model predicts it may be effective for **migraine disorder**, but this is a model prediction only, with **no clinical trials** and **no publications** supporting this specific indication.
The best-supported alternative prediction is **rheumatoid arthritis** (3 clinical trials, 1 Phase 2 RCT), covered in a supplementary section below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Psoriatic arthritis |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 98.66% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Apremilast is known as a PDE4 inhibitor, which raises intracellular cAMP and dampens pro-inflammatory signalling. It is an established treatment for psoriatic arthritis.

PDE4 is highly expressed in the brain, and the neurological literature discusses it as a possible therapeutic target. However, no migraine-specific preclinical or clinical data were found for apremilast. Headache is also a known adverse effect of apremilast, which argues against a benefit. The prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered for migraine disorder.

## Literature Evidence

Currently no related literature available for migraine disorder.

## Supplementary: Best-Supported Alternative Prediction (Rheumatoid Arthritis)

Rheumatoid arthritis ranks third (TxGNN score 98.09%) and has the strongest evidence among the predictions (Evidence Level L2). The mechanism (PDE4 inhibition reducing TNF-alpha and related cytokines) is the same one underlying the approved psoriatic arthritis use.

### Clinical Trials

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01285310](https://clinicaltrials.gov/study/NCT01285310) | Phase 2 | Terminated | 237 | Randomised, double-blind, placebo-controlled comparison of two apremilast doses in RA with inadequate response to methotrexate |
| [NCT01250548](https://clinicaltrials.gov/study/NCT01250548) | Phase 2 | Completed | 34 | Controlled trial of apremilast vs placebo in active RA, assessing safety and time to response |
| [NCT01204138](https://clinicaltrials.gov/study/NCT01204138) | Phase 2 | Withdrawn | 0 | Apremilast added to TNF inhibition in active RA; no participants enrolled, so no evidence |

### Literature

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25779750](https://pubmed.ncbi.nlm.nih.gov/25779750/) | 2015 | RCT | Arthritis & Rheumatology | Phase 2 RCT of apremilast vs placebo in active RA with inadequate response to methotrexate |
| [20525198](https://pubmed.ncbi.nlm.nih.gov/20525198/) | 2010 | Preclinical | Arthritis Research & Therapy | Apremilast inhibited TNF-alpha production from human RA synovial cells and ameliorated experimental arthritis |
| [30072998](https://pubmed.ncbi.nlm.nih.gov/30072998/) | 2018 | Preclinical | Frontiers in Immunology | Apremilast reduced Th1/Th17 cells and increased regulatory T cells in a mouse arthritis model |
| [26097790](https://pubmed.ncbi.nlm.nih.gov/26097790/) | 2014 | Pharmacokinetic study | Clin Pharmacol Drug Dev | Pharmacokinetics of apremilast co-administered with methotrexate in RA and PsA |
| [24797159](https://pubmed.ncbi.nlm.nih.gov/24797159/) | 2014 | Review | Drugs | Overview of apremilast's first global approval and development programme |

No Phase 3 programme is evident, and efficacy appears modest relative to established RA therapies.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12218C | Otezla | Pack containing 4 tablets 10 mg, 4 tablets 20 mg and 19 tablets 30 mg | Not available in the data compiled for this report |

## Safety Considerations

- **Drug Interactions**: 75 interactions were identified in the interaction database, with the following examples:
  - **Major**: lumacaftor, fosphenytoin, apalutamide. These are likely strong enzyme inducers that may reduce apremilast exposure.
  - **Moderate**: dexamethasone, griseofulvin, bosentan, bexarotene, deferasirox, among others.
  - **Minor**: armodafinil.
- **Headache** is a known adverse effect of apremilast (noted in the pharmacovigilance literature), which is relevant to any migraine application.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The migraine prediction rests on model score alone (Evidence Level L5), with no trials or literature, and the known headache adverse effect argues against benefit. The other high-ranked predictions are also L5, except rheumatoid arthritis. For rheumatoid arthritis there is only Phase 2 evidence (L2), with a terminated and a withdrawn study and no Phase 3 programme.

**To proceed, the following is needed:**
- Mechanism of action data for apremilast
- Preclinical evidence for PDE4 inhibition in migraine models, and a review of headache incidence in existing apremilast trials
- Safety information from the TGA Product Information (warnings, contraindications), which was not available
- Australian approved indication text for the ARTG entry
- For rheumatoid arthritis, a clear rationale for why a Phase 3 programme was not pursued, and a comparison with established RA therapies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

