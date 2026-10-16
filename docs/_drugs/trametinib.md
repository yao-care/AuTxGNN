---
layout: default
title: Trametinib
parent: Model Prediction Only (L5)
nav_order: 744
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Trametinib: predicted new indication Non-cutaneous melanoma (evidence level L5). Approved use: Metastatic melanoma"
---

# Trametinib
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

# Trametinib: From Metastatic Melanoma to Non-Cutaneous Melanoma

## One-Sentence Summary

Trametinib is an oral MEK inhibitor originally used to treat BRAF V600-mutant metastatic melanoma.
The TxGNN model predicts it may be effective for **non-cutaneous melanoma**, the highest-ranked prediction with any clinical trial support in the data compiled for this report. The top-ranked prediction, choroideremia, has no supporting evidence and no apparent mechanistic rationale.
Support for non-cutaneous melanoma is currently **10 registered trials** (mostly early-phase, combination or non-specific studies) and **no publications** for this specific indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic melanoma (TGA licence text for the Australian entry is not available) |
| Predicted New Indication | Non-cutaneous melanoma (see note below) |
| TxGNN Prediction Score | 99.30% (non-cutaneous melanoma) |
| Evidence Level | L2 (by the supplied scoring), though the trials are not specific to this subtype; a conservative reading is closer to L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold (research question only) |

**Note on indication choice:** The highest-scoring prediction, choroideremia (99.31%), has no clinical trials or literature, and choroideremia is an inherited retinal degeneration rather than a MAPK-driven disease. This report therefore focuses on non-cutaneous melanoma (rank 2), the first prediction with trial data. Other melanoma subtype predictions are summarised briefly below.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, trametinib is a reversible inhibitor of MEK1 and MEK2 (MAP2K1 and MAP2K2), kinases in the MAPK signalling pathway. This is consistent with the target records in the interaction data. Its established use is in BRAF V600-mutant melanoma, often combined with dabrafenib.

Non-cutaneous melanoma (mucosal, ocular and other non-skin sites) shares the melanocytic origin of cutaneous melanoma, and some cases carry MAPK-activating mutations. The case reports compiled describe BRAF-mutated conjunctival and other mucosal or ocular melanomas treated with BRAF-pathway inhibitors, which gives a plausible but anecdotal rationale.

There is an important caveat. Uveal melanoma is generally driven by GNAQ/GNA11 rather than BRAF, so benefit is likely to depend on molecular selection (for example, confirmed BRAF V600 mutation). The trials listed do not establish efficacy in non-cutaneous subtypes specifically.

---

## Clinical Trial Evidence

None of these trials is specific to non-cutaneous melanoma. They cover melanoma or BRAF-mutant tumours generally. Relevance grades below are from the supplied assessment.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02296112](https://clinicaltrials.gov/study/NCT02296112) | Phase 2 | Completed | 9 | Trametinib in melanoma with BRAF non-V600 mutations; very small sample (relevance B) |
| [NCT04439292](https://clinicaltrials.gov/study/NCT04439292) | Phase 2 | Active, not recruiting | 44 | NCI-MATCH Subprotocol H: dabrafenib + trametinib in BRAF V600E/K tumours, excluding melanoma, thyroid, colorectal and lung cancers; tumour-agnostic basket (relevance B) |
| [NCT03944356](https://clinicaltrials.gov/study/NCT03944356) | N/A (non-interventional) | Completed | 232 | Real-world use of adjuvant dabrafenib + trametinib in melanoma; likely cutaneous (relevance B) |
| [NCT07440290](https://clinicaltrials.gov/study/NCT07440290) | Phase 2/3 | Recruiting | 30 | DETERMINE platform trial: dabrafenib + trametinib in BRAF V600-positive cancers (relevance not yet graded) |
| [NCT02872259](https://clinicaltrials.gov/study/NCT02872259) | Phase 1/2 | Completed | 74 | BGB324 with pembrolizumab or dabrafenib/trametinib in advanced melanoma; trametinib contribution cannot be isolated |
| [NCT02974725](https://clinicaltrials.gov/study/NCT02974725) | Phase 1 | Terminated | 241 | LXH254-based combinations including trametinib in KRAS/BRAF-mutant NSCLC or NRAS-mutant melanoma |
| [NCT05907304](https://clinicaltrials.gov/study/NCT05907304) | Phase 1 | Active, not recruiting | 86 | Naporafenib + trametinib in RAS Q61X solid tumours; no results available |
| [NCT02410863](https://clinicaltrials.gov/study/NCT02410863) | Phase 2 | Terminated | 10 | Biomarker-driven targeted therapy in BRAF-mutant metastatic melanoma; terminated early |
| [NCT03340506](https://clinicaltrials.gov/study/NCT03340506) | Phase 4 | Recruiting | 100 | Roll-over study for long-term safety of dabrafenib and/or trametinib; no efficacy data |
| [NCT05275374](https://clinicaltrials.gov/study/NCT05275374) | Phase 1/2 | Not yet recruiting | 221 | XP-102 alone and with trametinib in BRAF V600 solid tumours; no data yet |

An additional access programme (NCT02416232, no longer available) provides no efficacy data.

---

## Literature Evidence

No publications were found for non-cutaneous melanoma itself. Literature for closely related predicted subtypes:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30376465](https://pubmed.ncbi.nlm.nih.gov/30376465/) | 2019 | Real-world cohort | Melanoma Res | Multicentre retrospective study of combination BRAF/MEK inhibitors in 65 patients with melanoma and active brain metastases (nodular melanoma prediction) |
| [40853557](https://pubmed.ncbi.nlm.nih.gov/40853557/) | 2025 | Review | JAMA | General review of cutaneous melanoma (supports amelanotic, nodular and acral predictions only indirectly) |
| [31361915](https://pubmed.ncbi.nlm.nih.gov/31361915/) | 2020 | Case report/Review | Clin Exp Dermatol | Two BRAF-mutated bulbar conjunctival melanomas (epithelioid cell type); one patient treated with vemurafenib (epithelioid cell and eyelid melanoma predictions) |
| [31747798](https://pubmed.ncbi.nlm.nih.gov/31747798/) | 2019 | Case report/Review | J Investig Med High Impact Case Rep | Lacrimal sac melanoma: one case and 14 Japanese cases reviewed |
| [42583475](https://pubmed.ncbi.nlm.nih.gov/42583475/) | 2026 | Case report | Ann Med Surg | Early metastatic BRAF V600E melanoma without a known primary lesion |
| [24879511](https://pubmed.ncbi.nlm.nih.gov/24879511/) | 2014 | Case series | Am J Dermatopathol | Panniculitis in 9 patients on BRAF inhibitors, including dabrafenib + trametinib (safety signal) |
| [25788221](https://pubmed.ncbi.nlm.nih.gov/25788221/) | 2015 | Case report | Eur J Dermatol | Panniculitis in two patients on BRAF + MEK inhibitor combination |
| [32877390](https://pubmed.ncbi.nlm.nih.gov/32877390/) | 2020 | Case report/Review | Medwave | Panniculitis in a patient with BRAF V600E melanoma on dabrafenib/trametinib |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10382K | Mekinist | Tablet 2 mg (oral) | Not available in the data compiled for this report |

Note: the licence number is reproduced as supplied and should be verified against the ARTG.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (MEK1/2 kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI; standard practice includes monitoring blood counts, liver function and skin reactions |
| Handling Protection | Please refer to the PI and local institutional policy for oral anticancer agents |

---

## Safety Considerations

- **Drug Interactions:** 15 interactions rated Moderate were identified (17 records in total, including 2 target-pharmacology records). The Moderate interactions involve: fostamatinib, elagolix, apalutamide, brigatinib, dabrafenib, encorafenib, isavuconazonium, lasmiditan, midostaurin, sarecycline, enzalutamide, erdafitinib, gilteritinib, idelalisib and tucatinib.
- **Adverse effects reported in the literature:** panniculitis has been described in patients on BRAF inhibitors, including combinations with trametinib.

Warnings and contraindications for Australia were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for non-cutaneous melanoma is high (99.30%), and trametinib is established in BRAF-mutant cutaneous melanoma. However, the supporting trials are small, early-phase, combination or tumour-agnostic studies, and no study specifically addresses non-cutaneous subtypes, where BRAF mutations are less common. The evidence supports framing this as a research question, not a treatment recommendation. Other predictions (choroideremia, scrotum, balloon cell and CDK4-linked melanoma) have no supporting evidence, and the cutaneous subtype predictions largely overlap with the existing approved indication.

**To proceed, the following is needed:**
- Mechanism of action data and Australian PI warnings and contraindications (flagged as blocking for safety screening)
- Subtype-specific evidence in mucosal, conjunctival or other non-cutaneous melanoma, ideally stratified by BRAF/NRAS/GNAQ status
- Review of results from NCT02296112, NCT04439292 and NCT07440290 for relevant melanoma subgroups
- Confirmation of the ARTG approved indication text and any PBS restrictions
- A molecular selection strategy (for example, BRAF V600 testing) and a safety monitoring plan, including attention to the moderate drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

