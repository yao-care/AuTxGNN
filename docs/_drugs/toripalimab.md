---
layout: default
title: Toripalimab
parent: 僅模型預測 (L5)
nav_order: 689
evidence_level: L5
indication_count: 10
---

# Toripalimab
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

# Toripalimab: From Cancer Immunotherapy to Mixed-Type Autoimmune Hemolytic Anemia

## One-Sentence Summary

Toripalimab is an anti-PD-1 monoclonal antibody used in oncology (evidence in this pack references esophageal, nasopharyngeal, hepatocellular, renal cell, and other cancers). The TxGNN model's top prediction is **Mixed-Type Autoimmune Hemolytic Anemia**, but this prediction — and 8 of the other 9 top-ranked candidates in this pack — is **mechanistically contradictory**: PD-1 blockade removes immune tolerance and would be expected to *trigger or worsen* autoimmune/haemolytic conditions, not treat them. There are **no supporting clinical trials or literature** for this specific indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded (drug not registered in Australia). Based on trial/literature context in this pack, toripalimab is an anti-PD-1 checkpoint inhibitor used in oncology (e.g. esophageal, nasopharyngeal, hepatocellular, renal cell carcinoma) |
| Predicted New Indication | Mixed-Type Autoimmune Hemolytic Anemia |
| TxGNN Prediction Score | 93.76% |
| Evidence Level | L5 (model prediction only — no clinical trials, no literature, and flagged as mechanistically contradictory) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

**It is not.** The evidence pack's own mechanistic analysis flags this prediction as directionally contradictory. PD-1 blockade works by releasing an immune "brake," restoring T-cell activity against tumour cells. This same mechanism is a well-documented cause of immune-related adverse events (irAEs), including autoimmune haemolytic anaemia, rather than a treatment for it. Using an immune-activating agent to treat an autoimmune haemolytic disorder runs counter to its established pharmacology.

This is not a theoretical concern — it is corroborated elsewhere in this same evidence pack. Literature retrieved under rank 3 ("dermatitis") describes toripalimab as the *causative* agent of severe skin immune reactions (Steven-Johnson syndrome/toxic epidermal necrolysis, lichenoid drug eruption), and literature under rank 6 ("proteinuria") describes renal irAEs during toripalimab-based cancer combination therapy. In both cases, the condition TxGNN proposes as a "new indication" is actually a known **adverse effect** of the drug, not a treatment target.

A formal mechanism-of-action (MOA) record is listed as a data gap (DG002) in this pack, so a full biological-plausibility assessment cannot be completed. However, the mechanistic reasoning already provided (immune checkpoint blockade → enhanced T-cell/immune activity) is sufficient to conclude that this direction of repurposing is not currently supportable.

---

## Other Predicted Indications (Ranks 2–10)

All ten top-ranked TxGNN predictions for toripalimab in this evidence pack follow the same pattern — high model scores, but either no supporting evidence or evidence that actually documents the disease as an adverse effect rather than a treatment target.

| Rank | Disease | Score | Evidence Level | Recommendation | Note |
|------|---------|-------|-----------------|-----------------|------|
| 1 | Mixed-type autoimmune hemolytic anemia | 93.76% | L5 | Hold | No evidence; mechanism contradicts |
| 2 | Idiopathic aplastic anemia | 93.76% | L5 | Hold | No evidence; immune-mediated marrow suppression risk |
| 3 | Dermatitis | 93.69% | L4 | Hold | Trials/literature describe drug as **cause** of severe skin irAEs (SJS/TEN), not treatment |
| 4 | Paroxysmal nocturnal hemoglobinuria | 93.67% | L5 | Hold | Mechanism unrelated (complement-mediated, not T-cell) |
| 5 | Drug-induced autoimmune hemolytic anemia | 93.67% | L5 | Hold | Logically inconsistent — checkpoint inhibitors are a known *cause* of this condition |
| 6 | Proteinuria | 93.07% | L4 | Hold | Literature describes proteinuria as a renal irAE during toripalimab combination therapy |
| 7 | Acne keloid | 93.05% | L5 | Hold | No evidence, no mechanistic rationale |
| 8 | Neonatal autoimmune hemolytic anemia | 93.03% | L5 | Hold | Population mismatch; mechanism contradicts |
| 9 | Primary CD59 deficiency | 92.84% | L5 | Hold | No known mechanistic link (genetic complement disorder) |
| 10 | Amyopathic dermatomyositis | 92.79% | L5 | Hold | PD-1 inhibitors are a known trigger of myositis/dermatomyositis-like irAEs |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Mixed-Type Autoimmune Hemolytic Anemia.

---

## Literature Evidence

Currently no related literature available for Mixed-Type Autoimmune Hemolytic Anemia.

---

## Australia Market Information

Toripalimab is not currently registered on the ARTG (Australian Register of Therapeutic Goods) and has no market presence in Australia. No approved Australian product information exists.

---

## Cytotoxicity

Based on trial/literature context in this pack, toripalimab is an anti-PD-1 checkpoint inhibitor (immunotherapy class), used in combination regimens across multiple solid tumours.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-1 checkpoint inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Low from direct cytotoxicity; however, immune-related haematological adverse events (e.g. autoimmune haemolytic anaemia, aplastic anaemia) are a recognised risk class |
| Emetogenicity Classification | Low (checkpoint inhibitors have minimal intrinsic emetogenic potential) |
| Monitoring Items | FBC and haemolysis markers, skin examination (irAE reports include SJS/TEN — [PMID 39347662](https://pubmed.ncbi.nlm.nih.gov/39347662/), [PMID 34632814](https://pubmed.ncbi.nlm.nih.gov/34632814/), [PMID 41656837](https://pubmed.ncbi.nlm.nih.gov/41656837/)), renal function/urinalysis (proteinuria reported as renal irAE — [PMID 38687583](https://pubmed.ncbi.nlm.nih.gov/38687583/)), thyroid/endocrine panel |
| Handling Protection | Standard monoclonal antibody IV handling; conventional cytotoxic drug handling regulations do not apply |

---

## Safety Considerations

No structured safety data (key warnings, contraindications, DDI) has been collected for this drug in this evidence pack (DG001 — blocking gap: TFDA/product-label warnings not yet obtained), and no TGA-approved Product Information exists as toripalimab is not registered in Australia.

That said, literature retrieved elsewhere in this pack for related predicted indications documents known immune-related adverse events associated with toripalimab, including toxic epidermal necrolysis/Steven-Johnson syndrome, lichenoid drug eruption, and renal proteinuria — these should be treated as safety signals rather than repurposing rationale.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate should not proceed. The top-ranked prediction has no clinical or literature support and is mechanistically implausible — PD-1 blockade would be expected to worsen, not treat, autoimmune haemolytic anaemia. Across all ten top-ranked predictions in this pack, the pattern repeats: either no evidence, or evidence that documents the "predicted indication" as a known adverse effect of the drug rather than a treatment target.

**To proceed, the following is needed:**
- Formal MOA data from DrugBank (DG002) to complete a rigorous mechanistic-plausibility check
- TFDA/TGA product information and warnings (DG001, blocking) before any safety-stage evaluation
- Given the systematic contradiction across all 10 ranked candidates for this drug, flag this candidate to the data science team for model/output review before further evidence collection is invested
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

