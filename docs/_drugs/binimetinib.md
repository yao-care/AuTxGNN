---
layout: default
title: Binimetinib
parent: Model Prediction Only (L5)
nav_order: 96
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Binimetinib: predicted new indication Non-cutaneous melanoma (evidence level L5). Approved use: Metastatic melanoma"
---

# Binimetinib
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

# Binimetinib: From Metastatic Melanoma to Non-Cutaneous Melanoma

## One-Sentence Summary

Binimetinib is a MEK inhibitor, originally used to treat BRAF V600-mutant metastatic melanoma.
The TxGNN model predicts it may be effective for **non-cutaneous melanoma** (a subtype group that includes mucosal, uveal and acral disease),
with **5 clinical trials** and **1 publication** currently linked to this direction. None of these trials has reported results, and the publication is a single case report on cutaneous melanoma.

*Note on indication selection:* The top-ranked TxGNN prediction is choroideremia (score 98.63%), but it has no supporting evidence and no plausible biological link to MEK inhibition. This report therefore focuses on the highest-ranked prediction with trial evidence, non-cutaneous melanoma (rank 2). Mucosal melanoma (rank 7) has the strongest single trial and is discussed where relevant.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic melanoma (approved indication text not available in the ARTG data compiled) |
| Predicted New Indication | Non-cutaneous melanoma |
| TxGNN Prediction Score | 98.60% |
| Evidence Level | L3 (as assigned in the compiled data; see the note under Clinical Trial Evidence) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Binimetinib is known to be a MEK1/2 inhibitor acting downstream of BRAF and RAS in the MAPK pathway. Its efficacy in BRAF V600-mutant cutaneous melanoma is established, and it is used in combination with encorafenib.

Non-cutaneous melanomas (mucosal, uveal, acral) often show MAPK pathway activation, so MEK inhibition is mechanistically reasonable. However, dependence on this pathway varies by subtype:

- **Mucosal melanoma** is less often BRAF-mutant than cutaneous melanoma (KIT, NRAS and NF1 alterations are more common), but MEK inhibition is plausible, especially in BRAF-mutant cases.
- **Uveal melanoma** is driven mainly by GNAQ/GNA11 mutations, so the rationale is weaker.
- **Acral melanoma** has a published case report of a durable response to encorafenib plus binimetinib (see Literature Evidence), but this is anecdotal.

The high TxGNN score reflects a computational prediction based on proximity to the original melanoma indication. It does not by itself demonstrate efficacy in these subtypes.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04511013](https://clinicaltrials.gov/study/NCT04511013) | Phase 2 | Recruiting | 112 | Randomised trial of encorafenib + binimetinib + nivolumab vs ipilimumab + nivolumab in BRAF V600-mutant melanoma with brain metastases. Listed under mucosal melanoma (rank 7); mucosal-specific enrolment is not confirmed. No results yet. |
| [NCT03235245](https://clinicaltrials.gov/study/NCT03235245) | Phase 2 | Active, not recruiting | 271 | EORTC randomised study (EBIN): encorafenib + binimetinib induction followed by ipilimumab + nivolumab vs immunotherapy alone in BRAF V600-mutant unresectable or metastatic melanoma. Likely cutaneous population. |
| [NCT04045691](https://clinicaltrials.gov/study/NCT04045691) | N/A (non-interventional) | Recruiting | 750 | BERING-MELANOMA: real-world effectiveness, quality of life and safety of encorafenib + binimetinib in BRAF V600-mutant melanoma (Germany, Austria, Switzerland). |
| [NCT04543188](https://clinicaltrials.gov/study/NCT04543188) | Phase 1a/b | Terminated | 65 | First-in-human study of PF-07284890 alone and with binimetinib in BRAF V600-mutant solid tumours, with and without brain involvement. Reason for termination not provided. |
| [NCT05355701](https://clinicaltrials.gov/study/NCT05355701) | Phase 1 | Active, not recruiting | 103 | Safety, tolerability and PK of PF-07799933 alone and in combination in advanced BRAF-altered solid tumours. Whether binimetinib is part of the regimen cannot be confirmed. |
| [NCT04913285](https://clinicaltrials.gov/study/NCT04913285) | Phase 1/1b | Recruiting | 400 | Safety, PK and preliminary efficacy of KIN-2787 in BRAF/NRAS-mutated solid tumours. Combination partners not verifiable. |

**Interpretation:** No completed Phase 3 trials are identified. Most trials are early phase, ongoing, or concentrated on BRAF-mutant cutaneous melanoma (the original indication), and none confirms a non-cutaneous melanoma population or reports results. The L3 grade assigned in the compiled data is therefore generous. A conservative reading is closer to L4/L5 for the non-cutaneous subtype specifically.

No ANZCTR trial identifiers were found in the data compiled.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33877099](https://pubmed.ncbi.nlm.nih.gov/33877099/) | 2021 | Case report | Recenti Prog Med | Amelanotic acral melanoma of the foot treated first-line with encorafenib + binimetinib: complete response lasting 37 months, then a partial response on second-line anti-PD-1 therapy. (Listed under amelanotic skin melanoma, rank 9.) |
| [41774417](https://pubmed.ncbi.nlm.nih.gov/41774417/) | 2025 | Case report | Pigment Cell Melanoma Res | Epidermotropic metastatic melanoma presenting as eruptive primary melanomas, diagnosed by molecular profiling. Cutaneous melanoma; no binimetinib efficacy data. |

Both items are single-patient case reports. They do not provide efficacy evidence for binimetinib in non-cutaneous melanoma.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11948W | Mektovi | Tablet 15 mg (oral) | Not available in the data compiled |

One valid single-ingredient licence is listed, with no cancelled entries.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (MEK inhibitor); not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI (liver function, creatine phosphokinase and cardiac function monitoring are generally considered for MEK inhibitors) |
| Handling Protection | Please refer to the PI and local institutional policy |

## Safety Considerations

Warnings and contraindications from the product label are not available in the data compiled. Please refer to the TGA-approved Product Information (PI) for safety information.

**Drug Interactions:** The interaction screen returned 100 potential interactions. The main examples are:

- **Major:** deferasirox, ibritumomab tiuxetan, tositumomab (including I-131 tositumomab), drotrecogin alfa
- **Moderate (selected):** omeprazole, dexamethasone, clarithromycin, simvastatin, ticagrelor, eltrombopag, naloxone, naltrexone, cobicistat, rolapitant, tolbutamide, fostamatinib, albendazole, eliglustat, fidaxomicin

These come from the DDInter database. Only a subset of the 100 interactions is shown, and the clinical significance of each should be checked against the PI and an interaction reference.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The MEK-inhibition rationale is plausible for non-cutaneous melanoma, but the evidence consists of early-phase or ongoing trials without results, most in BRAF-mutant cutaneous melanoma, plus single case reports. The 98.60% TxGNN score is a computational prediction only. Other top-ranked predictions (for example choroideremia, rank 1) have no supporting evidence.

**To proceed, the following is needed:**
- Results or subgroup data from NCT04511013 and other trials, confirming mucosal, acral or uveal enrolment and the contribution of binimetinib within combinations
- Molecular stratification (BRAF, NRAS, KIT, NF1, GNAQ/GNA11) to define which non-cutaneous subtypes could benefit
- Mechanism of action data for binimetinib (currently a data gap)
- Product Information warnings, contraindications and approved indication text (safety screening cannot be completed without them)
- Review of the clinical significance of the major interactions
- Confirmation of ANZCTR-registered Australian trials, if any
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

