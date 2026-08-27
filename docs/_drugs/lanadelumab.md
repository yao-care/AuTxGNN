---
layout: default
title: Lanadelumab
parent: 僅模型預測 (L5)
nav_order: 381
evidence_level: L5
indication_count: 10
---

# Lanadelumab
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

# Lanadelumab: From Hereditary Angioedema Prophylaxis to C1 Inhibitor Deficiency

## One-Sentence Summary

Lanadelumab is a fully human monoclonal antibody that inhibits plasma kallikrein, globally established for long-term prophylaxis of hereditary angioedema (HAE) attacks, but it is **not currently registered on Australia's ARTG**. The TxGNN model's top-ranked prediction for this drug is **C1 inhibitor deficiency** — essentially its already-recognised primary indication overseas — supported by **22 clinical trials** (including a pivotal placebo-controlled Phase 3 RCT) and **20 publications** identified in this evidence pack. Because this candidate largely confirms an existing indication rather than revealing a novel mechanistic link, the key open question for Australia is market registration and safety documentation, not efficacy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hereditary Angioedema (HAE) prophylaxis — not ARTG-registered; established from literature evidence in this pack (see below), as structured original-indication and MOA fields were not available |
| Predicted New Indication | C1 inhibitor deficiency |
| TxGNN Prediction Score | 99.9955% (internal rank 142) |
| Evidence Level | L2 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the structured `original_moa` field (data gap). However, the literature evidence attached to this candidate consistently describes lanadelumab as a fully human monoclonal antibody that inhibits plasma kallikrein, thereby blocking excessive bradykinin production within the kallikrein-kinin pathway (PMID 30267321). This pathway is directly dysregulated in hereditary angioedema caused by C1-inhibitor (C1-INH) deficiency or dysfunction, where insufficient C1-INH activity leads to uncontrolled kallikrein activity and bradykinin-mediated swelling.

Importantly, "C1 inhibitor deficiency" is not a mechanistically distant new indication — it corresponds closely to the disease population (HAE Type I/II, due to C1-INH deficiency) for which lanadelumab (Takhzyro®) already holds approvals in multiple jurisdictions, including the US, EU, Japan, China and South Korea, as reflected in the trial evidence below. TxGNN's high-confidence score here should therefore be read as the model correctly recovering a well-established drug-disease relationship, rather than surfacing a genuinely novel repurposing hypothesis. The practical value of this candidate for Australia is that the drug is absent from the ARTG (0 entries, "Not Marketed"), meaning the open question is one of local registration and safety documentation, not of biological plausibility.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02586805](https://clinicaltrials.gov/study/NCT02586805) | Phase 3 | Completed | 125 | Pivotal placebo-controlled RCT (HELP Study): lanadelumab significantly reduced HAE attack rate vs placebo in Type I/II HAE |
| [NCT02741596](https://clinicaltrials.gov/study/NCT02741596) | Phase 3 | Completed | 212 | HELP Study Extension: long-term open-label data confirming sustained safety and efficacy of prophylaxis |
| [NCT04070326](https://clinicaltrials.gov/study/NCT04070326) | Phase 3 | Completed | 21 | SPRING study: PK/PD, safety and attack-reduction efficacy in paediatric patients aged 2 to <12 years |
| [NCT04180163](https://clinicaltrials.gov/study/NCT04180163) | Phase 3 | Completed | 12 | Confirmed efficacy and safety of lanadelumab in Japanese HAE Type I/II patients |
| [NCT05460325](https://clinicaltrials.gov/study/NCT05460325) | Phase 3 | Completed | 20 | Evaluated safety, PK and efficacy of lanadelumab in Chinese HAE patients over 26 weeks |
| [NCT04687137](https://clinicaltrials.gov/study/NCT04687137) | Phase 3 | Completed | 12 | Japan expanded access program providing compassionate pre-licensure access for HAE patients |
| [NCT04444895](https://clinicaltrials.gov/study/NCT04444895) | Phase 3 | Completed | 73 | Long-term safety/efficacy in non-histaminergic angioedema with normal C1-INH — a related but distinct HAE subtype |
| [NCT03845400](https://clinicaltrials.gov/study/NCT03845400) | N/A (Observational) | Completed | 168 | EMPOWER study: real-world US/Canada cohort comparing HAE attack rates before and after initiation |
| [NCT04130191](https://clinicaltrials.gov/study/NCT04130191) | N/A (Observational) | Completed | 140 | ENABLE study: three-year real-world data confirming sustained reduction in HAE attacks |
| [NCT02093923](https://clinicaltrials.gov/study/NCT02093923) | Phase 1b | Completed | 38 | Multiple ascending dose study establishing early safety, tolerability and PK in HAE subjects |

*No ANZCTR (Australian New Zealand Clinical Trials Registry) entries were identified in this evidence pack.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30480729](https://pubmed.ncbi.nlm.nih.gov/30480729/) | 2018 | RCT | JAMA | Pivotal HELP Study: lanadelumab significantly reduced HAE attack frequency vs placebo |
| [30267321](https://pubmed.ncbi.nlm.nih.gov/30267321/) | 2018 | Review | Drugs | First global approval review: lanadelumab as a plasma kallikrein inhibitor for HAE prevention |
| [32187470](https://pubmed.ncbi.nlm.nih.gov/32187470/) | 2020 | Review | New England Journal of Medicine | Comprehensive review of HAE pathophysiology, diagnosis and treatment, including lanadelumab |
| [39508959](https://pubmed.ncbi.nlm.nih.gov/39508959/) | 2024 | Systematic Review | Clinical Reviews in Allergy & Immunology | Review of breakthrough HAE attacks occurring in patients on long-term prophylaxis, incl. lanadelumab |
| [40434599](https://pubmed.ncbi.nlm.nih.gov/40434599/) | 2025 | Review (Network Meta-Analysis) | Drugs in R&D | Network meta-analysis comparing efficacy/safety of HAE prophylactic therapies incl. lanadelumab |
| [34287942](https://pubmed.ncbi.nlm.nih.gov/34287942/) | 2022 | Open-label Extension Study | Allergy | HELP OLE study: long-term effectiveness and safety of lanadelumab in HAE Type I/II |
| [39701274](https://pubmed.ncbi.nlm.nih.gov/39701274/) | 2025 | Observational Study | J Allergy Clin Immunol Pract | Multicountry INTEGRATED study confirming real-world effectiveness of lanadelumab in HAE |
| [37328263](https://pubmed.ncbi.nlm.nih.gov/37328263/) | 2023 | Observational Study | Allergy and Asthma Proceedings | Compared healthcare resource utilisation between lanadelumab and SC C1-INH concentrate users |
| [30539362](https://pubmed.ncbi.nlm.nih.gov/30539362/) | 2019 | Review | BioDrugs | Review of preclinical and Phase I data supporting lanadelumab's kallikrein-inhibition mechanism |
| [39836016](https://pubmed.ncbi.nlm.nih.gov/39836016/) | 2025 | Review (Indirect Treatment Comparison) | Journal of Comparative Effectiveness Research | Indirect comparison of lanadelumab vs C1-INH concentrate in paediatric HAE patients |

---

## Australia Market Information

Lanadelumab is currently **not registered on the ARTG (Australian Register of Therapeutic Goods)** — 0 entries were found in this evidence pack.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No key warnings, contraindications, or drug-drug interaction data were available in this evidence pack — this is flagged as a **Blocking data gap (DG001)** that must be resolved before any safety-stage assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Efficacy evidence for the predicted indication is strong — it corresponds to lanadelumab's well-established global approval for HAE due to C1-INH deficiency, supported by a pivotal Phase 3 RCT and extensive real-world data. However, this candidate cannot progress to safety assessment because product information (warnings/contraindications) is a confirmed Blocking data gap, and the drug has zero ARTG registrations in Australia.

**To proceed, the following is needed:**
- TGA-approved Product Information — key warnings and contraindications (DG001, Blocking)
- Mechanism-of-action detail from DrugBank to complete the mechanistic-relevance analysis (DG002, High)
- Drug-drug interaction data (current query status: not found)
- Confirmation of ARTG registration pathway/status, since this candidate is effectively a market-access question rather than a novel repurposing hypothesis
- Clarification of whether "C1 inhibitor deficiency" should be tracked as a distinct repurposing candidate or reclassified as a primary-indication registration gap
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

