---
layout: default
title: Oxaliplatin
parent: 僅模型預測 (L5)
nav_order: 498
evidence_level: L5
indication_count: 10
---

# Oxaliplatin
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

# Oxaliplatin: From Colorectal Cancer to Malignant Pleural Mesothelioma

## One-Sentence Summary

Oxaliplatin is a platinum-based chemotherapy agent established for metastatic and adjuvant colorectal cancer (typically as part of the FOLFOX regimen). The TxGNN model predicts it may also be effective for **Malignant Pleural Mesothelioma (MPM)**, with **5 clinical trials** and **20 publications** currently identified in this evidence pack supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Colorectal cancer (metastatic/adjuvant chemotherapy) — not derived from Australian regulatory data (drug not currently marketed in Australia; see below) |
| Predicted New Indication | Malignant Pleural Mesothelioma |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data was not available in this evidence pack (data gap). Based on the repurposing analysis that is available, Oxaliplatin is a third-generation, DACH-platinum compound that forms DNA cross-links, blocking replication and transcription and inducing apoptosis — the same general platinum mechanism as cisplatin, which underpins the current standard first-line therapy for MPM (cisplatin/pemetrexed).

Oxaliplatin's established indication is colorectal cancer. Although colorectal cancer and MPM are anatomically distinct, both are platinum-responsive solid tumours where DNA-adduct formation drives cytotoxic effect, and MPM standard-of-care already depends on a platinum backbone combined with an antifolate agent (pemetrexed or raltitrexed).

This mechanistic overlap is directly supported in the evidence pack by multiple completed or near-complete Phase 2 trials that substitute oxaliplatin into MPM combination regimens (with gemcitabine or raltitrexed) instead of cisplatin, which is consistent with the high TxGNN prediction score (99.68%, model rank 4,323 of the disease vocabulary).

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00859469](https://clinicaltrials.gov/study/NCT00859469) | Phase 2 | Completed | 29 | Oxaliplatin (Eloxatin) + Gemcitabine as first- or second-line chemotherapy for pleural/peritoneal mesothelioma; direct oxaliplatin-in-MPM evidence |
| [NCT00996385](https://clinicaltrials.gov/study/NCT00996385) | Phase 2 | Unknown | 29 | Velcade (bortezomib) + Eloxatin (oxaliplatin) in previously treated pleural/peritoneal mesothelioma patients |
| [NCT03210298](https://clinicaltrials.gov/study/NCT03210298) | N/A | Unknown | 1000 | International PIPAC/PITAC registry for malignant pleural/peritoneal disease; multi-drug, not oxaliplatin-specific (Relevance grade B) |
| [NCT06310473](https://clinicaltrials.gov/study/NCT06310473) | Phase 2 | Not yet recruiting | 30 | Neoadjuvant cadonilimab + chemotherapy for gastroesophageal junction/gastric cancer; disease mismatch — not MPM (Relevance grade C) |
| [NCT05107674](https://clinicaltrials.gov/study/NCT05107674) | Phase 1 | Recruiting | 345 | CBL-B inhibitor NX-1607 in advanced malignancies; no direct oxaliplatin link (Relevance grade C) |

No ANZCTR-registered trials were identified for this indication in the evidence pack.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12525529](https://pubmed.ncbi.nlm.nih.gov/12525529/) | 2003 | Cohort (Phase 2) | J Clin Oncol | Raltitrexed + oxaliplatin active in diffuse MPM (n=70, chemo-naïve and pretreated) |
| [14609447](https://pubmed.ncbi.nlm.nih.gov/14609447/) | 2003 | Cohort (Phase 2) | Clin Lung Cancer | Multicenter Phase 2 of gemcitabine + oxaliplatin in MPM (n=25) |
| [11989592](https://pubmed.ncbi.nlm.nih.gov/11989592/) | 2001 | Cohort (Pilot) | Tumori | Oxaliplatin + raltitrexed pilot study in inoperable MPM |
| [19091133](https://pubmed.ncbi.nlm.nih.gov/19091133/) | 2008 | Cohort (Observational) | J Occup Med Toxicol | Gemcitabine + oxaliplatin in MPM patients pretreated with pemetrexed |
| [15639727](https://pubmed.ncbi.nlm.nih.gov/15639727/) | 2005 | Phase 2 trial | Lung Cancer | Vinorelbine + oxaliplatin as first-line therapy in untreated MPM |
| [15893013](https://pubmed.ncbi.nlm.nih.gov/15893013/) | 2005 | Phase 2 trial | Lung Cancer | Raltitrexed-oxaliplatin inactive as second-line MPM treatment (negative result) |
| [10930799](https://pubmed.ncbi.nlm.nih.gov/10930799/) | 2000 | Cohort | Eur J Cancer | Institut Gustave Roussy 9-year experience with chemo/chemo-immunotherapy in mesothelioma |
| [26526504](https://pubmed.ncbi.nlm.nih.gov/26526504/) | 2015 | Review | Cancer Treat Rev | Vinca alkaloids in the therapeutic management of MPM; platinum/pemetrexed noted as standard of care |
| [11836672](https://pubmed.ncbi.nlm.nih.gov/11836672/) | 2002 | Review | Semin Oncol | Antifolates in MPM treatment, including the raltitrexed/oxaliplatin combination |
| [12601280](https://pubmed.ncbi.nlm.nih.gov/12601280/) | 2003 | Review | Curr Opin Oncol | Overview of chemotherapy for MPM, including platinum-based combinations |

## Australia Market Information

Oxaliplatin is currently **not marketed in Australia** according to this evidence pack (0 ARTG entries recorded, market status "not marketed"). No product listing, dosage form, or approved indication text is available to summarise.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — platinum compound (third-generation, DACH-platinum) |
| Myelosuppression Risk | Moderate (neutropenia and thrombocytopenia reported for this drug class); the dose-limiting toxicity for oxaliplatin specifically is typically cumulative peripheral sensory neuropathy rather than myelosuppression — please refer to the Product Information (PI) for full details |
| Emetogenicity Classification | Moderate to high (typical of platinum-class agents) |
| Monitoring Items | FBC with differential, renal function (oxaliplatin clearance is renal-dependent), neurological assessment for peripheral neuropathy, LFTs |
| Handling Protection | Yes — must follow standard cytotoxic drug handling and PPE protocols |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. This evidence pack has a **blocking data gap** on TFDA/TGA-equivalent warnings and contraindications (DG001), and drug interaction data was not found — safety data must be sourced before proceeding to formal safety review.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed/near-complete Phase 2 trials and several supporting cohort studies directly test oxaliplatin-based combinations in MPM patients, giving Evidence Level L2. However, all studies are small (n=25–70), the drug is not currently marketed in Australia, and safety/PI data is missing — so this cannot yet advance without guardrails.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications) — currently a blocking data gap
- Detailed mechanism-of-action data from DrugBank
- Drug-drug interaction data (currently not found)
- Confirmation of ARTG registration pathway, given the drug is not presently marketed in Australia
- Larger confirmatory trials, given the small sample sizes of existing Phase 2 MPM studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

