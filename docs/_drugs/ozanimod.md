---
layout: default
title: Ozanimod
parent: 僅模型預測 (L5)
nav_order: 504
evidence_level: L5
indication_count: 10
---

# Ozanimod
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

# Ozanimod: From Relapsing Multiple Sclerosis to Progressive Relapsing Multiple Sclerosis

## One-Sentence Summary

Ozanimod is an oral sphingosine-1-phosphate (S1P) receptor modulator originally approved for **relapsing forms of multiple sclerosis** (clinically isolated syndrome, relapsing-remitting MS, and active secondary progressive MS). The TxGNN model predicts it may also be effective for **Progressive Relapsing Multiple Sclerosis (PRMS)**, with **8 clinical trials** and **18 publications** currently identified in the evidence pack — though none of these studies specifically enrolled or targeted the PRMS subtype.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relapsing forms of multiple sclerosis (per literature evidence; no ARTG record exists for this indication in Australia) |
| Predicted New Indication | Progressive Relapsing Multiple Sclerosis |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

A structured DrugBank mechanism-of-action record for Ozanimod was not available in this evidence pack (data gap DG002). However, the literature captured here consistently describes Ozanimod as a selective **S1P1 and S1P5 receptor modulator**. By binding these receptors, it prevents autoreactive lymphocytes from egressing lymph nodes, reducing peripheral lymphocyte counts and limiting inflammatory infiltration into the central nervous system — the core mechanism underlying its approved efficacy in relapsing MS.

Progressive Relapsing Multiple Sclerosis is a historical MS subtype (progressive disease course from onset, punctuated by relapses) that has largely been reclassified into the broader "progressive MS" category. Because it still involves a relapsing component, there is a superficial mechanistic rationale for extending an S1P modulator's anti-inflammatory effect to this population — the KG-level similarity likely reflects this shared "relapsing MS" feature space.

However, the evidence pack's own rationale flags an important caveat: PRMS-associated disability accumulation is thought to be driven predominantly by **neurodegeneration and chronic microglial activation**, not peripheral lymphocyte trafficking. Other S1P modulators in the same class (fingolimod, siponimod) have shown only limited benefit against the pure progressive/neurodegenerative component of MS. This is a recognised class-level limitation, and no trial identified here specifically isolated or studied the PRMS phenotype — all clinical evidence comes from broader relapsing-MS trial populations (including rank 6, "relapsing-remitting multiple sclerosis," which the evidence pack explicitly identifies as Ozanimod's **already-approved original indication**, not a repurposing candidate).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03535298](https://clinicaltrials.gov/study/NCT03535298) | Phase 4 | Active, not recruiting | 800 | DELIVER-MS: compares early intensive vs. escalation DMT strategies in relapsing MS; overlaps partially with progressive/active populations but is not PRMS-specific. |
| [NCT05828901](https://clinicaltrials.gov/study/NCT05828901) | N/A | Recruiting | 60 | Studies disease-activity and rebound-risk prediction in MS patients on S1P receptor modulators (class includes ozanimod). |
| [NCT02576717](https://clinicaltrials.gov/study/NCT02576717) | Phase 3 | Completed | 2494 | Pivotal RCT of RPC1063 (ozanimod) vs. interferon beta-1a in relapsing MS — the key registrational efficacy/safety trial, but enrolled relapsing (not progressive) MS patients. |
| [NCT04676204](https://clinicaltrials.gov/study/NCT04676204) | N/A | Enrolling by invitation | 323 | STATURE: observational study of oral DMT treatment burden and adherence (includes ozanimod); not an efficacy study. |
| [NCT05605782](https://clinicaltrials.gov/study/NCT05605782) | N/A | Active, not recruiting | 9000 | ORION: large real-world, post-authorisation safety registry in relapsing-remitting MS patients on ozanimod. |
| [NCT05688436](https://clinicaltrials.gov/study/NCT05688436) | N/A | Recruiting | 1178 | Pregnancy outcomes in women exposed to diroximel fumarate — a different DMT; low direct relevance, likely a knowledge-graph class-level link. |
| [NCT03500328](https://clinicaltrials.gov/study/NCT03500328) | N/A | Active, not recruiting | 900 | Pragmatic trial comparing early aggressive vs. escalation therapy across MS DMTs, including high-efficacy agents; not PRMS-specific. |
| [NCT06396039](https://clinicaltrials.gov/study/NCT06396039) | Phase 4 | Active, not recruiting | 84 | Open-label effectiveness/safety study of oral ozanimod in Chinese adults with relapsing MS. |

No trial identified here specifically enrolled or reported outcomes for the Progressive Relapsing MS subtype.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39254048](https://pubmed.ncbi.nlm.nih.gov/39254048/) | 2024 | Network meta-analysis | Cochrane Database Syst Rev | Immunomodulators/immunosuppressants for progressive MS — notes relative benefit and safety remain unclear due to lack of direct head-to-head comparisons. |
| [31598138](https://pubmed.ncbi.nlm.nih.gov/31598138/) | 2019 | Review | Ther Adv Neurol Disord | Reviews progressive MS pathophysiology and therapeutic developments; highlights that continued compartmentalised CNS inflammation, not peripheral trafficking, drives progression. |
| [33287177](https://pubmed.ncbi.nlm.nih.gov/33287177/) | 2020 | Comprehensive review | Neurology International | Reviews ozanimod's efficacy and safety in relapsing forms of MS. |
| [32385738](https://pubmed.ncbi.nlm.nih.gov/32385738/) | 2020 | Regulatory approval review | Drugs | Confirms ozanimod's first approval (US/EU) for relapsing MS, including clinically isolated syndrome, RRMS, and active secondary progressive disease. |
| [36946625](https://pubmed.ncbi.nlm.nih.gov/36946625/) | 2023 | Review | Expert Opin Pharmacother | Updates on S1P receptor modulators (fingolimod, siponimod, ozanimod, ponesimod) for relapsing MS. |
| [33797705](https://pubmed.ncbi.nlm.nih.gov/33797705/) | 2021 | Review | CNS Drugs | Reviews the S1P receptor modulator class across MS and other autoimmune indications. |
| [30410033](https://pubmed.ncbi.nlm.nih.gov/30410033/) | 2018 | General review | Nat Rev Dis Primers | Overview of MS pathogenesis, subtypes and heterogeneity. |
| [35805142](https://pubmed.ncbi.nlm.nih.gov/35805142/) | 2022 | Mechanistic review | Cells | Reviews S1P/S1PR signalling pathway modulators and their pharmacology. |
| [32059809](https://pubmed.ncbi.nlm.nih.gov/32059809/) | 2020 | Review | Lancet Neurol | Reviews oral immunomodulating therapies in relapsing MS. |
| [38162670](https://pubmed.ncbi.nlm.nih.gov/38162670/) | 2023 | Review | Front Immunol | Reviews CNS-bioavailable DMTs, noting limited efficacy of current DMTs (including S1P modulators) once the progressive phase has begun. |

No literature identified here directly studies ozanimod in a PRMS-specific population.

---

## Australia Market Information

Ozanimod has no current ARTG (Australian Register of Therapeutic Goods) entries (0 licences on record) and is not marketed in Australia. Prescribing and safety information will need to be sourced from overseas regulators (e.g. US FDA label, EMA SmPC) pending any future TGA registration.

---

## Safety Considerations

No structured Australian safety data (key warnings, contraindications, or drug-interaction records) is currently available for Ozanimod in this evidence pack, and this is compounded by the fact that the drug is not TGA-registered, so no Australian Product Information exists yet. Until local registration and a TGA-approved PI are available, prescribers should rely on overseas regulatory labelling (e.g. US FDA/EMA) for safety and interaction information, noting that the S1P-modulator class carries known risks including bradyarrhythmia at treatment initiation, macular oedema, liver enzyme elevation, and infection risk from lymphopenia.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for Ozanimod in Progressive Relapsing MS specifically is indirect — all identified trials and literature address relapsing MS broadly (which is Ozanimod's existing approved indication) or progressive MS as a general category, rather than the PRMS phenotype itself. Combined with a Blocking data gap on TFDA/TGA label and safety information (DG001), this candidate cannot yet proceed to an initial safety assessment (S1).

**To proceed, the following is needed:**
- TGA/overseas Product Information (warnings, contraindications, interactions) to complete an initial safety assessment
- Structured DrugBank mechanism-of-action data (DG002)
- Trials or registry data specifically enrolling patients with the progressive-relapsing MS phenotype, rather than relapsing MS generally
- Clarification of Australian registration pathway/status, given there are currently 0 ARTG entries

*Note: Several other TxGNN-predicted indications for Ozanimod in this evidence pack (e.g. transient neonatal thrombocytopenia, hereditary thrombocytopenia variants, dense granule disease) have no supporting clinical trials or literature and are assessed in the underlying evidence pack as likely knowledge-graph artefacts rather than genuine repurposing signals; they are not carried forward in this report.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

