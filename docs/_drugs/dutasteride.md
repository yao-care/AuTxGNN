---
layout: default
title: Dutasteride
parent: 僅模型預測 (L5)
nav_order: 176
evidence_level: L5
indication_count: 10
---

# Dutasteride
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

# Dutasteride: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Dutasteride is a dual 5α-reductase inhibitor approved internationally for benign prostatic hyperplasia (BPH) and androgenetic alopecia; it is not currently listed in the Australian Register of Therapeutic Goods (ARTG) based on the data retrieved for this report.
The TxGNN model's top prediction is **Ambras Type Hypertrichosis Universalis Congenita** (score 99.998%), however **no clinical trials or supporting publications** exist for this specific indication, and mechanistic analysis strongly suggests this is a knowledge graph propagation artefact rather than a clinically meaningful repurposing opportunity.
Across all 10 model predictions, **Diffuse Alopecia Areata** (Rank 8, L4) represents the only candidate with any indirect mechanistic plausibility and is recommended as a research question for further exploration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Benign Prostatic Hyperplasia (BPH); androgenetic alopecia — international approvals; no ARTG entries retrieved in this dataset |
| Predicted New Indication | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed (no ARTG entries retrieved) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data was not available in this Evidence Pack. Based on established pharmacological literature, Dutasteride inhibits both type 1 and type 2 isoforms of 5α-reductase — the enzyme that converts testosterone to dihydrotestosterone (DHT). By suppressing DHT levels by approximately 90%, it is effective in androgen-dependent conditions such as BPH and male-pattern hair loss. This DHT-dependent pathway is the core basis against which all predicted indications should be assessed.

Ambras type hypertrichosis universalis congenita is a rare genetic disorder caused by mutations in the *TRPS1* gene (and related loci), resulting in generalised excessive hair growth present from birth. Critically, this condition is **not driven by androgen excess or elevated DHT** — it is a structural developmental defect in hair follicle programming. There is therefore no established mechanistic pathway by which Dutasteride's DHT-suppressing action would be expected to benefit or modify this disorder.

The high TxGNN prediction score (0.9999) most likely reflects a **knowledge graph propagation artefact**: nodes representing "hair growth" and "hair follicle" disorders cluster in close graph proximity regardless of their underlying molecular aetiology. This is a recognised limitation of graph-based prediction models when applied to heterogeneous disease categories that share phenotypic surface similarity but differ fundamentally in their biology. The mechanistic rationale analysis embedded in the Evidence Pack independently reaches the same conclusion.

---

## Clinical Trial Evidence

Currently no clinical trials related to Dutasteride and Ambras Type Hypertrichosis Universalis Congenita are registered on ClinicalTrials.gov, ANZCTR, or ICTRP.

---

## Literature Evidence

Currently no related literature is available for Dutasteride in Ambras Type Hypertrichosis Universalis Congenita.

---

## Additional Predictions — Clinician Summary

The TxGNN model returned 10 predictions for Dutasteride. For completeness, the full prediction landscape is summarised below, as the top-ranked indication is assessed as a false positive and the most actionable signal sits at Rank 8.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision | Summary Assessment |
|------|---------------------|-------------|----------------|----------|--------------------|
| 1 | Ambras type hypertrichosis universalis congenita | 99.998% | L5 | **Hold** | TRPS1 gene defect; non-DHT-dependent; likely KG artefact |
| 2 | Hypertrichosis (disease) | 99.997% | L5 | **Hold** | Heterogeneous aetiology; no Dutasteride-specific evidence |
| 3 | Malformation syndrome with odontal/periodontal component | 99.997% | L5 | **Hold** | 20 literature hits all on general periodontitis; none on Dutasteride; KG artefact |
| 4 | Syndrome with Dandy-Walker malformation as major feature | 99.996% | L5 | **Hold** | Congenital posterior fossa brain defect; no DHT pathway link |
| 5 | Isolated genetic hair shaft abnormality | 99.996% | L5 | **Hold** | Keratin structural protein mutations; non-DHT-dependent |
| 6 | Hypotrichosis simplex of the scalp | 99.771% | L5 | **Hold** | Autosomal genetic hypotrichosis (CDSN/LPAR6); non-androgenic |
| 7 | Congenital hypotrichosis milia | 99.753% | L5 | **Hold** | Rare skin barrier protein defect; no DHT intersection |
| **8** | **Diffuse alopecia areata** | **99.675%** | **L4** | **Research Question** | **Indirect DHT–immune privilege link; 1 supporting review (2026)** |
| 9 | Migraine with brainstem aura | 99.667% | L5 | **Hold** | Neurosteroid hypothesis present but multi-step indirect; no clinical data |
| 10 | Familial isolated trichomegaly | 99.565% | L5 | **Hold** | Rare eyelash genetic disorder; no Dutasteride research proposed to date |

### Diffuse Alopecia Areata — Rank 8 Detail

Diffuse alopecia areata (DAA) is primarily an autoimmune condition mediated by CD8⁺ T-cell attack on hair follicles. However, three indirect connections support a research question:

1. DAA and androgenetic alopecia (AGA) frequently **co-exist** and can be clinically difficult to distinguish in practice.
2. DHT is known to modulate the **follicular immune privilege microenvironment** — the mechanism by which healthy follicles evade immune surveillance — providing a plausible indirect link.
3. A 2026 narrative review (PMID 41714473) documents expanding clinical applications of Dutasteride in follicular diseases in women, suggesting the field is actively exploring its scope.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [41714473](https://pubmed.ncbi.nlm.nih.gov/41714473/) | 2026 | Narrative Review | American Journal of Clinical Dermatology | Comprehensive review of AGA pathophysiology and treatments in women including Dutasteride; highlights hormonal, genetic, and environmental interactions in chronic hair loss |

---

## Australia Market Information

No ARTG entries were retrieved for Dutasteride in this data query.

> **Important notice for clinicians:** The absence of ARTG entries in this dataset does not confirm that Dutasteride is unavailable in Australia. Dutasteride is internationally marketed (e.g., as **Avodart**, GSK) for BPH, and registration status should be verified directly via the [TGA ARTG Public Summary Portal](https://www.tga.gov.au/resources/artg) before any clinical or regulatory decision is made. It is likely that the data retrieval step for this drug did not capture existing ARTG entries, which should be treated as a **data gap requiring remediation**.

---

## Safety Considerations

Safety data including key warnings, contraindications, and drug–drug interactions were not available in this Evidence Pack.

Please refer to the TGA-approved Product Information (PI) for complete safety information. Key areas to review include:

- **Teratogenicity**: Dutasteride is a Category X agent in pregnancy. As it is absorbed through the skin and excreted in semen, male patients with pregnant partners must use condoms. Female healthcare workers and caregivers must avoid contact with capsule contents.
- **PSA and prostate cancer screening**: Dutasteride suppresses PSA levels by approximately 50% after 6 months; clinicians should double the measured PSA value when assessing patients on Dutasteride using standard reference ranges.
- **CYP3A4 interactions**: Dutasteride is metabolised by CYP3A4 and CYP3A5; potent inhibitors (e.g., ketoconazole, ritonavir, verapamil) may increase plasma concentrations.
- **Donation restrictions**: Patients must not donate blood during treatment and for 6 months after cessation.

*(Above safety profile is based on established pharmacological references, pending retrieval of TGA-approved PI.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN prediction (Ambras type hypertrichosis universalis congenita) has no credible mechanistic basis, no clinical trials, and no supporting literature — consistent with a knowledge graph propagation artefact arising from shared "hair-related" node proximity in the knowledge graph. All 10 predictions are rated L5 (model prediction only) except Rank 8 (Diffuse Alopecia Areata, L4), which remains at the "Research Question" stage and is not ready for repurposing evaluation without further targeted work.

**To proceed, the following is needed:**

- **Verify ARTG status** — Conduct a direct TGA ARTG portal search to confirm current Australian registration for Dutasteride; the zero-result data retrieval is likely a data gap rather than true absence
- **Retrieve TGA Product Information (PI)** — Download and parse the PI to formally document approved indications, contraindications, warnings, and drug interactions
- **Retrieve MOA from DrugBank** — Query DrugBank API (DB01126) to populate the mechanistic data gap and enable structured mechanistic link analysis for all 10 predictions
- **For Diffuse Alopecia Areata (Rank 8)** — Define a specific clinical research question (e.g., "Does Dutasteride reduce hair loss severity in patients with DAA co-occurring with AGA?"), perform a structured literature search on Dutasteride + alopecia areata, and consult a dermatologist to assess feasibility of a pilot study or case series

---

*This report is generated for research reference only and does not constitute medical advice. Drug repurposing candidates require rigorous clinical validation before therapeutic application. Results should be interpreted by qualified healthcare professionals in the appropriate clinical context.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

