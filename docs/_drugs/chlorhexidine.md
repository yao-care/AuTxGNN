---
layout: default
title: Chlorhexidine
parent: Model Prediction Only (L5)
nav_order: 153
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Chlorhexidine: predicted new indication Chronic ethmoidal sinusitis (evidence level L5). Approved use: Gingivitis"
---

# Chlorhexidine
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

# Chlorhexidine: From Gingivitis to Chronic Ethmoidal Sinusitis

## One-Sentence Summary

Chlorhexidine is a broad-spectrum antiseptic, originally used to treat **gingivitis**.
The TxGNN model predicts it may be effective for **Chronic Ethmoidal Sinusitis**,
but **no clinical trials and no publications** currently support this specific prediction. This is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gingivitis |
| Predicted New Indication | Chronic ethmoidal sinusitis |
| TxGNN Prediction Score | 95.46% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, chlorhexidine is a broad-spectrum antiseptic with antibacterial and antifungal activity. Its efficacy in gingivitis (reducing oral bacterial load and plaque) is established, and mechanistically it may be applicable to infections of the sinonasal mucosa.

Gingivitis and chronic ethmoidal sinusitis are both mucosal conditions of the upper aerodigestive tract in which bacterial burden and biofilm may play a role. A topical antimicrobial could plausibly reduce this burden. However, no data were found for this specific indication, and this link remains a hypothesis.

Several other predictions from the same model help show how far the evidence extends. These are summarised below because the top-ranked prediction has no supporting literature:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Sinusitis | 95.30% | L4 | Only indirect literature (surgical prophylaxis, case reports) |
| 3 | Chronic rhinosinusitis | 95.22% | L4 | In vitro data on chlorhexidine-coated sinonasal stents; no clinical trials |
| 5 | Tinea corporis | 93.37% | L4 | Mostly veterinary and in vitro data |
| 9 | Cutaneous candidiasis | 88.01% | L4 | Indirect evidence only |

Chronic rhinosinusitis (rank 3) currently has the most relevant mechanistic support: a 2021 in vitro study (PMID 34834197) found that a sinonasal stent coated with slow-release chlorhexidine varnish gave sustained protection against bacterial biofilm. This is preclinical and not a treatment trial.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked prediction (chronic ethmoidal sinusitis).

For reference, the most relevant items retrieved for closely related sinus predictions are listed below. They are indirect evidence only:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41140432](https://pubmed.ncbi.nlm.nih.gov/41140432/) | 2025 | RCT | J Neurol Surg B Skull Base | Three-arm randomised trial of preoperative antiseptic preparation in transnasal skull base surgery. It addresses surgical-site infection prophylaxis, not treatment of sinusitis. |
| [34834197](https://pubmed.ncbi.nlm.nih.gov/34834197/) | 2021 | In vitro study | Pharmaceutics | Sinonasal stent coated with slow-release chlorhexidine varnish gave sustained protection against *S. aureus* and *P. aeruginosa* biofilm. |
| [38592477](https://pubmed.ncbi.nlm.nih.gov/38592477/) | 2024 | Review | HNO | Overview of antiseptics in otorhinolaryngology. Chlorhexidine is advised only as a mouth and body wash for MRSA decolonisation; clinical efficacy evidence for many other throat antiseptics is lacking. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 4161B | Plaqacide | Mouth wash 2 mg per mL (0.2%), 250 mL | Not stated in the data compiled |
| ARTG 183P | Not stated | Not stated | Not stated in the data compiled |

Both entries are valid single-ingredient products. Neither is a sinonasal formulation, so route compatibility with the predicted indication has not been established.

## Safety Considerations

- **Contraindications (knowledge-graph association):** The knowledge graph lists periodontitis as a disease with a drug-disease contraindication edge. This comes from the knowledge graph, not from product label text, and should be verified against the Product Information.
- **Drug Interactions:** The interaction screen returned 100 potential interacting drugs, but none has a severity level assigned. Examples include acetaminophen, atenolol, amlodipine, alprazolam, chloramphenicol, levothyroxine, celecoxib and cephalexin. These should be interpreted cautiously.

Please refer to the TGA-approved Product Information (PI) for warnings, precautions and full contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (chronic ethmoidal sinusitis) rests on a model score alone (L5), with no trials or literature. Related sinonasal evidence is indirect or preclinical, and the Australian products are oral mouthwashes rather than sinonasal formulations.

**To proceed, the following is needed:**
- Mechanism of action data for chlorhexidine
- Warnings and contraindications from the TGA-approved Product Information
- Direct clinical evidence in sinonasal disease, for example a pilot trial in chronic rhinosinusitis (rank 3), which has the strongest mechanistic support
- Assessment of a suitable sinonasal formulation and route, including mucosal tolerability, since current ARTG products are mouthwashes
- Clarification of interaction severity for the listed co-medications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

