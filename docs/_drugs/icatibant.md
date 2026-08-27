---
layout: default
title: Icatibant
parent: 僅模型預測 (L5)
nav_order: 338
evidence_level: L5
indication_count: 10
---

# Icatibant
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

# Icatibant: From Hereditary Angioedema to C1 Inhibitor Deficiency

## One-Sentence Summary

Icatibant is a bradykinin B2 receptor antagonist established internationally for acute attacks of hereditary angioedema (HAE) — the evidence pack does not carry a structured "original indication" field, but this use is directly documented throughout the supplied trial and literature evidence.
The TxGNN model's top prediction, **C1 inhibitor deficiency**, is in fact the same underlying disease entity as HAE (HAE is caused by C1 inhibitor deficiency/dysfunction), so this is best read as the model correctly recovering icatibant's known indication rather than identifying a genuinely novel use.
This is backed by **23 clinical trials** (including 3 completed Phase 3 RCTs) and **20 publications**, but icatibant is **not currently marketed or registered in Australia**, and no TGA Product Information is available.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in structured licence data (drug not registered in Australia). Trial/literature evidence indicates the established international use is Hereditary Angioedema (HAE) due to C1-inhibitor deficiency. |
| Predicted New Indication | C1 inhibitor deficiency |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Icatibant is described in the supplied literature as a selective, decapeptide **bradykinin B2 receptor antagonist** (e.g. Prescrire Int. 2010, PMID 21284353; Zanichelli et al. 2012, PMID 22686628). By blocking B2 receptor activation, it counteracts the excess bradykinin that drives vascular permeability and tissue swelling.

C1 inhibitor deficiency (hereditary or acquired) leads to unchecked activation of the kallikrein-kinin system and consequent bradykinin accumulation — this is the direct pathophysiological cause of hereditary angioedema. The predicted indication and icatibant's real-world established use therefore describe the same causal pathway, not two distinct conditions connected only by mechanistic inference.

**Important caveat for decision-making**: because the drug's structured `original_indications` and `original_moa` fields are data gaps, and no Australian licence record exists, this evidence pack cannot formally confirm icatibant already holds this indication elsewhere. The strength of the supporting evidence (multiple completed Phase 3 RCTs, large international registries, and a Taiwan-specific reimbursement study) suggests this is a market-access/registration question for Australia rather than a scientific repurposing question — this should be verified against overseas regulatory labels (e.g. EMA/FDA Firazyr PI) before proceeding.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00097695](https://clinicaltrials.gov/study/NCT00097695) | Phase 3 | Completed | 84 | Randomised, double-blind, placebo-controlled study of subcutaneous icatibant in acute HAE attacks |
| [NCT00912093](https://clinicaltrials.gov/study/NCT00912093) | Phase 3 | Completed | 98 | Randomised, double-blind, placebo-controlled multicentre study confirming efficacy/safety vs placebo |
| [NCT00500656](https://clinicaltrials.gov/study/NCT00500656) | Phase 3 | Completed | 85 | Randomised, controlled comparison of subcutaneous icatibant vs oral tranexamic acid for HAE attacks |
| [NCT00997204](https://clinicaltrials.gov/study/NCT00997204) | Phase 3 | Completed | 151 | Open-label study of self-administered subcutaneous icatibant: safety, tolerability, convenience |
| [NCT01034969](https://clinicaltrials.gov/study/NCT01034969) | N/A | Completed | 1761 | Icatibant Outcome Survey (IOS) — large international post-marketing registry for HAE/C1-INH deficiency |
| [NCT01457430](https://clinicaltrials.gov/study/NCT01457430) | Phase 4 | Completed | 19 | Open-label study of self-administered icatibant for acute HAE attacks |
| [NCT04654351](https://clinicaltrials.gov/study/NCT04654351) | Phase 3 | Completed | 2 | Safety, efficacy and PK of subcutaneous icatibant in Japanese children/adolescents with HAE |
| [NCT03888755](https://clinicaltrials.gov/study/NCT03888755) | Phase 3 | Completed | 8 | Open-label study of icatibant efficacy, PK and safety in Japanese HAE patients |
| [NCT01386658](https://clinicaltrials.gov/study/NCT01386658) | Phase 3 | Completed | 32 | PK, tolerability and safety of single-dose icatibant in children/adolescents with HAE |
| [NCT07290855](https://clinicaltrials.gov/study/NCT07290855) | Phase 4 | Completed | 5 | Taiwan (NHI-reimbursed) real-world safety/efficacy study of icatibant for bradykinin-induced angioedema |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22686628](https://pubmed.ncbi.nlm.nih.gov/22686628/) | 2012 | Observational | Allergy | Real-world use of icatibant in 8 patients with acquired C1-inhibitor deficiency |
| [34965883](https://pubmed.ncbi.nlm.nih.gov/34965883/) | 2021 | Registry/Observational | Allergy, Asthma & Clinical Immunology | Icatibant Outcome Survey (IOS) real-world experience in Spain |
| [35662289](https://pubmed.ncbi.nlm.nih.gov/35662289/) | 2022 | Registry | Clinical & Experimental Allergy | Registry-based analysis of icatibant and C1-inhibitor use for laryngeal HAE attacks |
| [23420425](https://pubmed.ncbi.nlm.nih.gov/23420425/) | 2013 | Systematic Review | Pneumonologia i Alergologia Polska | Comparative effectiveness of conestat alfa, C1-INH and icatibant for acute HAE attacks |
| [29757016](https://pubmed.ncbi.nlm.nih.gov/29757016/) | 2018 | Review | Expert Review of Clinical Immunology | Icatibant use in adolescents and children with C1-INH-HAE |
| [37898409](https://pubmed.ncbi.nlm.nih.gov/37898409/) | 2024 | Review | Journal of Allergy and Clinical Immunology | Burden of HAE due to C1-inhibitor deficiency in the Asia-Pacific region |
| [21284353](https://pubmed.ncbi.nlm.nih.gov/21284353/) | 2010 | Review/Commentary | Prescrire International | Icatibant positioning relative to C1 esterase inhibitor for HAE attacks |
| [24925394](https://pubmed.ncbi.nlm.nih.gov/24925394/) | 2014 | Review | Chemical Immunology and Allergy | Mechanistic overview of bradykinin-mediated angioedema diseases |
| [28687105](https://pubmed.ncbi.nlm.nih.gov/28687105/) | 2017 | Review | Immunology and Allergy Clinics of North America | Acquired C1 inhibitor deficiency overview |
| [26106828](https://pubmed.ncbi.nlm.nih.gov/26106828/) | 2015 | Review | Current Opinion in Allergy and Clinical Immunology | Diagnostic and therapeutic management of C1-INH-HAE (Italian experience) |

---

## Australia Market Information

Icatibant is not currently marketed or registered in Australia — there are no ARTG entries in the evidence pack (0 licences on file).

---

## Safety Considerations

Icatibant is not currently registered in Australia, and no TGA-approved Product Information is available in the evidence pack. Please refer to overseas regulatory documentation (e.g. EMA/FDA labelling for Firazyr) as an interim reference pending local registration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Efficacy evidence is strong (L1 — three completed Phase 3 RCTs plus large international registries), but a Blocking data gap on TGA/Australian safety information (warnings, contraindications, PI) means this candidate cannot proceed to the S1 safety pre-assessment stage. Icatibant is also not currently marketed in Australia.

**To proceed, the following is needed:**
- TGA-approved Product Information or equivalent overseas label (warnings, contraindications, DDI) to complete S1 safety assessment
- Confirmation from an authoritative source (e.g. EMA/FDA/sponsor) of icatibant's already-approved indication, to clarify whether this is a repurposing case or a new-market registration case
- A drug interaction (DDI) profile, currently unavailable ("not_found")
- Assessment of the TGA registration pathway, given the indication appears well-established overseas
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

