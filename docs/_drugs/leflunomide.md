---
layout: default
title: Leflunomide
parent: 僅模型預測 (L5)
nav_order: 388
evidence_level: L5
indication_count: 10
---

# Leflunomide
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

# Leflunomide: From Rheumatoid Arthritis to Plasma Cell Myeloma (Multiple Myeloma)

## One-Sentence Summary

Leflunomide is a DMARD (disease-modifying antirheumatic drug) originally used for rheumatoid arthritis. The TxGNN model's raw top-ranked prediction (brachydactyly-syndactyly syndrome) has no clinical or mechanistic support and is flagged in the evidence pack itself as likely embedding noise; the strongest evidence-backed repurposing candidate is instead **Plasma Cell Myeloma (Multiple Myeloma)**, supported by **8 clinical trials** (including a completed and published Phase 1/2 study and an actively recruiting Phase 2 combination trial) and **8 publications**, with a related "indolent/smoldering myeloma" sub-entry corroborating the same trial evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis (per internationally established product information; no Australian ARTG record exists as this product is not currently marketed locally) |
| Predicted New Indication | Plasma Cell Myeloma (Multiple Myeloma) |
| TxGNN Prediction Score | 95.16% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

*Note: leflunomide's own literature/rationale data flag the model's #1-ranked disease and several other high-scoring candidates (colobomatous microphthalmia-rhizomelic dysplasia syndrome, Meester-Loeys syndrome, ganglioneuroblastoma, WHIM syndrome, vertebral anomalies/T-cell dysfunction syndrome) as having zero supporting trials or literature — these are excluded from clinical consideration and not detailed further below.*

---

## Why is This Prediction Reasonable?

Official mechanism-of-action data for leflunomide was not available in this evidence pack (data gap). However, the evidence pack's own repurposing rationale and supporting literature converge on a well-characterised mechanism: leflunomide's active metabolite, A771726 (teriflunomide), inhibits dihydroorotate dehydrogenase (DHODH), blocking de novo pyrimidine synthesis. In rheumatoid arthritis this slows proliferation of autoreactive lymphocytes; in plasma cell myeloma, the same antiproliferative pressure is directed at malignant plasma cells, which have a high demand for pyrimidine nucleotides to sustain rapid proliferation.

Preclinical literature supports this link directly: DHODH inhibition by A771726 induces apoptosis and reduces proliferation across multiple myeloma cell lines (PMID 19174558), produces mitochondria-linked cytotoxicity in the RPMI-8226 myeloma cell line (PMID 34577124), and downregulates c-Myc via PIM kinase inhibition, extending survival in an in vivo myeloma model when combined with lenalidomide (PMID 30940637). This mechanistic case has already progressed into human trials: a completed Phase 1/2 dose-escalation study in relapsed/refractory myeloma (NCT02509052, published as PMID 32268821) and an actively recruiting Phase 2 combination trial with pomalidomide and dexamethasone (NCT04508790).

The same DHODH-targeting rationale also underlies a related, lower-evidence signal in myeloid leukaemia (an actively recruiting Phase 1/2 leflunomide + decitabine trial, NCT06923488, plus 2026 preclinical data on BCOR-mutant AML sensitivity to DHODH inhibition) — worth monitoring but not yet at the same evidence maturity as the myeloma signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02509052](https://clinicaltrials.gov/study/NCT02509052) | Phase 1/2 | Completed | 12 | Dose-escalation of single-agent leflunomide in relapsed/refractory myeloma (≥3 prior therapies); no dose-limiting toxicities at 20–40 mg; published as PMID 32268821. |
| [NCT04508790](https://clinicaltrials.gov/study/NCT04508790) | Phase 2 | Recruiting | 29 | Leflunomide + pomalidomide + dexamethasone in relapsed/refractory myeloma; efficacy evaluation ongoing. |
| [NCT03952832](https://clinicaltrials.gov/study/NCT03952832) | Phase 2 | Withdrawn | 0 | Planned trial in high-risk smoldering myeloma; withdrawn before enrolment, no data generated. |
| [NCT04370483](https://clinicaltrials.gov/study/NCT04370483) | Early Phase 1 | Active, not recruiting | 1 | Pilot study in high-risk smoldering myeloma assessing anti-myeloma activity; single-patient enrolment limits interpretability. |
| [NCT05014646](https://clinicaltrials.gov/study/NCT05014646) | Phase 2 | Active, not recruiting | 27 | Leflunomide in African-American and European-American patients with high-risk smoldering myeloma; results not yet reported. |
| [NCT01646385](https://clinicaltrials.gov/study/NCT01646385) | N/A | Completed | 6393 | UK rheumatoid arthritis registry study of etanercept safety — different drug; likely a database cross-linkage artefact rather than direct evidence. |
| [NCT00720798](https://clinicaltrials.gov/study/NCT00720798) | Phase 3 | Completed | 2067 | Tocilizumab long-term safety extension in RA — different drug; not directly relevant to leflunomide or myeloma. |
| [NCT05605587](https://clinicaltrials.gov/study/NCT05605587) | N/A | Terminated | 3 | LUMEN1 trial of leflunomide in MEN1 (endocrine neoplasia) patients, not myeloma; terminated early with minimal enrolment. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32268821](https://pubmed.ncbi.nlm.nih.gov/32268821/) | 2020 | Phase 1 trial | Leukemia & Lymphoma | Single-agent leflunomide in relapsed/refractory myeloma (≥3 prior therapies); tolerable at 20–40 mg (NCT02509052). |
| [30940637](https://pubmed.ncbi.nlm.nih.gov/30940637/) | 2019 | Cohort/mechanistic | Blood Advances | Teriflunomide downregulates c-Myc via PIM kinase inhibition; combined with lenalidomide extended survival in an in vivo myeloma model. |
| [36349910](https://pubmed.ncbi.nlm.nih.gov/36349910/) | 2022 | Review/citation | Blood Advances | Secondary citation of the same PIM/c-Myc mechanistic study above. |
| [34577124](https://pubmed.ncbi.nlm.nih.gov/34577124/) | 2021 | Preclinical | Molecules | Mitochondria-independent cytotoxicity of leflunomide/teriflunomide in the RPMI-8226 myeloma cell line. |
| [19174558](https://pubmed.ncbi.nlm.nih.gov/19174558/) | 2009 | Preclinical | Molecular Cancer Therapeutics | DHODH inhibitor A771726 induces apoptosis and reduces proliferation across myeloma cell lines. |
| [40814067](https://pubmed.ncbi.nlm.nih.gov/40814067/) | 2025 | Preclinical | Journal of Translational Medicine | MARCH5-MFN2/mitochondrial fusion axis in myeloma cells sensitising to venetoclax; mechanistic context, not leflunomide-specific. |
| [16155443](https://pubmed.ncbi.nlm.nih.gov/16155443/) | 2005 | Review | Current Opinion in Neurology | General review of drug-induced peripheral neuropathy; safety-context reference only, not myeloma-specific. |
| [36996290](https://pubmed.ncbi.nlm.nih.gov/36996290/) | 2023 | Cohort | Journal of Immunological Sciences | Leflunomide used off-label in two immunocompromised cancer patients with severe COVID-19; safety/tolerability context, unrelated to myeloma. |

---

## Safety Considerations

This medicine has 0 ARTG entries and is not currently marketed in Australia, so no local Product Information could be retrieved. Key warnings, contraindications, and drug-interaction data are all unavailable from the sources queried for this evaluation (DDI lookup: not found). Overseas prescribing information (e.g., FDA/EMA leflunomide PI) should be consulted before any off-label use is considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale (DHODH inhibition) and early clinical signal (a completed, published Phase 1/2 trial plus an actively recruiting Phase 2 combination trial) are genuinely promising for plasma cell myeloma. However, this drug is not registered in Australia (0 ARTG entries) and no safety/contraindication/interaction data could be sourced — this is flagged as a **Blocking** data gap in the evidence pack, meaning the candidate cannot yet proceed to a formal safety review.

**To proceed, the following is needed:**
- Local (or overseas reference) Product Information: warnings, contraindications, and drug interactions
- Confirmation of Australian regulatory pathway, since the drug currently has no ARTG presence
- Monitoring of the ongoing Phase 2 trials (NCT04508790, NCT05014646) for efficacy read-outs
- Optional: track the parallel myeloid leukaemia signal (NCT06923488) as a lower-priority secondary candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

