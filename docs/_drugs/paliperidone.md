---
layout: default
title: Paliperidone
parent: 僅模型預測 (L5)
nav_order: 507
evidence_level: L5
indication_count: 10
---

# Paliperidone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Using the report template to generate this evaluation. One methodological note before the report: this Evidence Pack is a **multi-candidate** screen (`candidate_id: TW-DB01267-multi`) — TxGNN returned 10 ranked candidates for Paliperidone. Nine of the ten (including the #1-ranked candidate by raw score, "retinal dystrophy with or without extraocular anomalies") have **zero clinical trial or literature evidence**, and the evidence pack's own `repurposing_rationale` explicitly flags them as embedding-level noise with no plausible mechanistic link. Only rank #10, **treatment-refractory schizophrenia**, has real supporting evidence (4 trials, 2 publications, L2/Proceed with Guardrails). Reporting the raw #1-by-score candidate as the headline finding would be clinically misleading, so this report leads with the only substantiated signal and documents the other nine as screened-and-rejected. This deviation is disclosed here rather than silently applied.

---

# Paliperidone: From Schizophrenia to Treatment-Refractory Schizophrenia

## One-Sentence Summary

Paliperidone is a dopamine D2/serotonin 5-HT2A receptor antagonist established as an antipsychotic for schizophrenia. Of 10 candidate indications returned by the TxGNN screen for this drug, only one — **Treatment-Refractory Schizophrenia** — is supported by actual evidence, with **4 clinical trials** and **2 publications**; the remaining nine top-scoring candidates (including unrelated congenital eye and metabolic disorders) have no supporting evidence and are assessed as algorithmic noise. This is not a novel mechanistic repurposing but a within-class extension to a treatment-resistant subpopulation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed via Australian regulatory records (Paliperidone is not currently ARTG-listed); internationally established use is Schizophrenia / schizoaffective disorder, corroborated by trial NCT01860781 in this pack |
| Predicted New Indication | Treatment-Refractory Schizophrenia |
| TxGNN Prediction Score | 99.80% (rank 3,125 in the full model output) |
| Evidence Level | L2 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails (this candidate only — see note below) |

**Note on the other 9 candidates:** TxGNN's top-ranked candidate by raw score (retinal dystrophy with or without extraocular anomalies, 99.92%) and eight others (X-linked myopia, syndromic myopia, hydranencephaly, a congenital glycosylation disorder, MYP26 myopia, a polymicrogyria syndrome, CMT1G, atypical glycine encephalopathy) all returned **zero** matching clinical trials and little to no relevant literature. All are scored **L5 / Hold** and are not recommended for further evaluation — see "Other Candidates Screened" below.

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data was not returned for the drug-level record in this pack (`original_moa: [Data Gap]`). However, the evidence pack's own trial-level rationale confirms Paliperidone is a **dopamine D2 and serotonin 5-HT2A receptor antagonist**, i.e. a standard atypical antipsychotic already used to treat the positive and negative symptoms of schizophrenia (supported directly by NCT01860781, a completed Phase 4 study of paliperidone palmitate "within three different group[s] of schizophrenia patients").

Treatment-refractory schizophrenia is not a distinct disease with a different biology — it is a clinical subpopulation defined by inadequate response to prior antipsychotic therapy. The TxGNN signal here therefore reflects a **within-class, within-indication extension** rather than a genuine mechanistic leap: the same D2/5-HT2A antagonism already approved for schizophrenia is being evaluated in patients who have failed other agents, including via the long-acting palmitate formulation and in head-to-head comparisons against aripiprazole. This is mechanistically coherent and is why this candidate, alone among the ten, carries real trial and literature support.

By contrast, the other nine candidates (congenital retinal/ocular dystrophies, X-linked and syndromic myopia, hydranencephaly, congenital glycosylation disorders, a cortical malformation syndrome, a demyelinating neuropathy, and glycine encephalopathy) are structural, developmental, or inborn metabolic disorders with no established relationship to monoamine receptor antagonism. None returned supporting trials, and the associated "literature" (e.g. for retinal dystrophy) consists of general ophthalmology reviews and case reports that do not mention Paliperidone or any antipsychotic — consistent with TxGNN surfacing gene/phenotype co-occurrence patterns rather than genuine drug-disease evidence.

## Clinical Trial Evidence

*(For Treatment-Refractory Schizophrenia — the only candidate with registered trials)*

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01860781](https://clinicaltrials.gov/study/NCT01860781) | Phase 4 | Completed | 30 | Prospective naturalistic case series evaluating paliperidone palmitate effectiveness across three schizophrenia patient groups; direct, concluded real-world evidence (Grade A) |
| [NCT06060886](https://clinicaltrials.gov/study/NCT06060886) | Phase 4 | Unknown | 244 | Open-label multicentre RCT comparing aripiprazole vs paliperidone/risperidone using multi-omics data in first-episode psychosis; larger sample but status unconfirmed (Grade B) |
| [NCT07047651](https://clinicaltrials.gov/study/NCT07047651) | Phase 4 | Recruiting | 40 | Evaluating pharmacotherapy combined with recovery-oriented programs (RECOVERYTRSGR) in treatment-resistant schizophrenia; still enrolling, no results yet (Grade B) |
| [NCT05741502](https://clinicaltrials.gov/study/NCT05741502) | Phase 4 | Terminated | 5 | Exploratory comparison of clozapine vs non-clozapine antipsychotics on inflammatory markers in treatment-resistant schizophrenia; terminated with minimal enrolment, hypothesis-generating only (Grade C) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31648341](https://pubmed.ncbi.nlm.nih.gov/31648341/) | 2019 | Review | Actas Españolas de Psiquiatría | Reviews psychopharmacology evidence for schizoaffective disorder; notes lack of disorder-specific treatment guidelines |
| [23364281](https://pubmed.ncbi.nlm.nih.gov/23364281/) | 2013 | Review | Current Opinion in Psychiatry | Reviews pharmacological and psychosocial treatment approaches in early-onset schizophrenia spectrum disorders |

## Australia Market Information

Paliperidone has **no ARTG entries** in this evidence pack (`total_licenses: 0`, `market_status: Not Marketed`). No product listings, dosage forms, or approved indication text are currently available for the Australian market.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No key warnings, contraindications, or drug-drug interaction data were returned in this evidence pack (DDI query status: not found).

**Important:** the evidence pack's data-gap log flags the absence of TFDA/label warning and contraindication data as a **Blocking** severity item (DG001) — this specifically prevents the candidate from entering the safety initial-assessment stage (S1) until sourced. Mechanism-of-action detail is also flagged as a **High** severity gap (DG002).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(applies only to Treatment-Refractory Schizophrenia; the other 9 TxGNN-ranked candidates are Hold)*

**Rationale:**
Treatment-refractory schizophrenia is mechanistically coherent with Paliperidone's established antipsychotic action and is supported by one completed Phase 4 real-world evidence study plus three additional registered trials, meeting L2 evidence criteria. However, a **Blocking** data gap on PI-level warnings/contraindications means this cannot yet clear a formal safety review, and Paliperidone is not currently marketed in Australia (0 ARTG entries).

**To proceed, the following is needed:**
- TGA-approved Product Information (PI) — warnings, precautions, and contraindications (currently a Blocking gap)
- Confirmed drug-drug interaction data (current DDI query returned "not found")
- Formal mechanism-of-action documentation (currently a data gap)
- Regulatory pathway assessment given the drug has no existing ARTG listing
- Awaited outcomes from ongoing trials NCT06060886 and NCT07047651 before any efficacy conclusion in the refractory subpopulation

**Other candidates screened:** the remaining nine TxGNN-ranked candidates (retinal dystrophy, X-linked myopia, syndromic myopia, hydranencephaly, congenital disorder of glycosylation, MYP26 myopia, a perisylvian polymicrogyria syndrome, CMT1G, and atypical glycine encephalopathy) returned no supporting clinical trials and, where literature exists, it does not reference Paliperidone or antipsychotics. These are assessed as **Hold / L5** and are not recommended for further evaluation without a specific new mechanistic hypothesis and supporting data.

---

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require full clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

