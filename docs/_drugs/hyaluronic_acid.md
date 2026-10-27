---
layout: default
title: Hyaluronic Acid
parent: Model Prediction Only (L5)
nav_order: 351
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Hyaluronic Acid: predicted new indication Dry eye syndrome (evidence level L5). Approved use: Not stated in the data compiled for this report (the marketed product…"
monitor_inn: "Hyaluronic acid"
predicted_indications: ["dry eye syndrome", "Sjogren syndrome", "xerophthalmia", "psoriasis", "dermatitis, atopic", "prolapse of lacrimal gland", "parapsoriasis", "pityriasis lichenoides", "severe nonproliferative diabetic retinopathy", "exanthem (disease)"]
---

# Hyaluronic Acid
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

## Hyaluronic Acid: From Ocular Lubrication (Eye Drops) to Dry Eye Syndrome
{: .text-alpha }

## One-Sentence Summary

Hyaluronic acid (sodium hyaluronate) is a lubricating, water-binding glycosaminoglycan that is marketed in Australia as an eye drop.
The TxGNN model predicts it may be effective for **dry eye syndrome**, which is an established use rather than a new one,
with **9 clinical trials** (including one completed Phase 3 randomised trial) and **20 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the marketed product is an ophthalmic eye drop) |
| Predicted New Indication | Dry eye syndrome |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L1 per the scoring in the data; note that only one completed Phase 3 RCT (NCT00599716) is identified, so on the strict criteria (≥2 completed Phase 3 RCTs) this would be closer to L2, supported by meta-analyses |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known information, hyaluronic acid is a viscoelastic, hygroscopic glycosaminoglycan. It binds water, lubricates the ocular surface, prolongs tear film stability and supports corneal epithelial healing, partly through CD44 interaction.

These properties directly address the tear-film instability and ocular surface damage seen in dry eye. Because hyaluronic acid is already widely used as a marketed artificial tear (including in Australia), this is an established use rather than a speculative repurposing. The TxGNN score mainly confirms an existing therapeutic relationship.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00599716](https://clinicaltrials.gov/study/NCT00599716) | Phase 3 | Completed | 300 | Multicentre, double-masked RCT of Vismed (sodium hyaluronate) vs vehicle in dry eye syndrome; the most direct evidence |
| [NCT06478134](https://clinicaltrials.gov/study/NCT06478134) | Phase 2/3 | Completed | 124 | Multi-component tear substitute (TriMix) vs an HA-based control; HA contribution confounded |
| [NCT07722650](https://clinicaltrials.gov/study/NCT07722650) | N/A | Completed | 120 | Twice-daily Systane Complete vs four-times-daily Thealoz Duo (trehalose plus HA); non-inferiority design |
| [NCT05823961](https://clinicaltrials.gov/study/NCT05823961) | N/A | Completed | 80 | Single-arm post-market follow-up of cross-linked HA eye drops; performance and safety data |
| [NCT03074344](https://clinicaltrials.gov/study/NCT03074344) | N/A | Completed | 40 | Cross-linked HA plus coenzyme Q10 eye drops in mild to moderate dry eye; small, combination product |
| [NCT06122428](https://clinicaltrials.gov/study/NCT06122428) | N/A | Completed | 16 | Retrospective study of riboflavin-enhanced HA 0.1% eye drops in dry eye; very small |

Other registered trials identified (NCT04673643, NCT06544447, NCT07089511) test non-HA interventions in dry eye, with HA at most a comparator or background therapy, so they are not direct evidence. NCT01838252 (HA gel for lower lid retraction) was withdrawn with no enrolment.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33804439](https://pubmed.ncbi.nlm.nih.gov/33804439/) | 2021 | Meta-analysis | Int J Environ Res Public Health | Compared HA-based with non-HA eye drops (saline, conventional artificial tears) for dry eye |
| [38895674](https://pubmed.ncbi.nlm.nih.gov/38895674/) | 2024 | Systematic review/Meta-analysis | Int J Ophthalmol | Compared high vs low concentration HA eye drops for dry eye |
| [39260878](https://pubmed.ncbi.nlm.nih.gov/39260878/) | 2024 | RCT | BMJ | Non-inferiority trial of laughter exercise vs 0.1% sodium hyaluronate for ocular surface discomfort in dry eye |
| [37162564](https://pubmed.ncbi.nlm.nih.gov/37162564/) | 2023 | Meta-analysis | Graefes Arch Clin Exp Ophthalmol | Topical diquafosol vs HA in randomised trials for dry eye |
| [37682142](https://pubmed.ncbi.nlm.nih.gov/37682142/) | 2023 | RCT | Medicine | 0.15% HA vs 0.05% cyclosporine A vs 3% diquafosol in moderate to severe dry eye |
| [35514082](https://pubmed.ncbi.nlm.nih.gov/35514082/) | 2022 | Review | Acta Ophthalmol | Critical evaluation of the safety and efficacy of HA artificial tears in dry eye |
| [37042308](https://pubmed.ncbi.nlm.nih.gov/37042308/) | 2024 | Review | Acta Ophthalmol | Comparison of HA with other single-ingredient eye drops for dry eye |
| [31373862](https://pubmed.ncbi.nlm.nih.gov/31373862/) | 2019 | Review | J Ocul Pharmacol Ther | Role of cross-linked HA as a tear film substitute |
| [37117131](https://pubmed.ncbi.nlm.nih.gov/37117131/) | 2023 | Clinical study | Contact Lens & Anterior Eye | Trehalose plus HA artificial tears in women aged 42-54 vs ≥55 years with dry eye |
| [33923222](https://pubmed.ncbi.nlm.nih.gov/33923222/) | 2021 | Review | Molecules | Applications of HA in ophthalmology and contact lenses |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14354L | Hylo-Fresh | Eye drops containing sodium hyaluronate 1 mg per mL, 10 mL | Not available |

## Safety Considerations

- **Contraindications (knowledge-graph signal, not label text)**: The TxGNN knowledge graph links hyaluronic acid with glaucoma as a contraindication. This should be checked against the Product Information.
- **Drug Interactions**: Two moderate-level interactions were recorded, both with topical preservative agents: cetylpyridinium (topical) and benzalkonium (topical).

For full warnings and contraindications, please refer to the TGA-approved Product Information (PI).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Dry eye syndrome is an established use of hyaluronic acid. It is supported by a completed Phase 3 vehicle-controlled RCT, several meta-analyses and a marketed Australian eye drop product. Other predicted indications (Sjögren syndrome, xerophthalmia, psoriasis, atopic dermatitis) have indirect or weak evidence, and the remainder (prolapse of lacrimal gland, parapsoriasis, pityriasis lichenoides, severe nonproliferative diabetic retinopathy, exanthem) are prediction-only with no supporting evidence.

**To proceed, the following is needed:**
- Product Information warnings and contraindications for the Australian product, including clarification of the glaucoma signal
- The approved indication wording for ARTG 14354L
- Detailed mechanism of action data
- Review of the interaction with benzalkonium and cetylpyridinium in practice (for example, preservative-containing co-administered drops)
- If a second Phase 3 RCT is sought for a stricter evidence grade, a search for additional HA-specific placebo-controlled trials
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

