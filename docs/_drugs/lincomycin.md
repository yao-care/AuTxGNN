---
layout: default
title: Lincomycin
parent: 僅模型預測 (L5)
nav_order: 398
evidence_level: L5
indication_count: 10
---

# Lincomycin
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

# Lincomycin: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Lincomycin is a lincosamide-class antibiotic, referenced throughout the evidence pack as an antibacterial agent for susceptible Gram-positive and anaerobic infections; no TFDA/ARTG-approved indication text or mechanism-of-action data is on file. The TxGNN model's top-ranked prediction for this drug is **Hyperamylasemia**, with a prediction score of **99.14%**, but this candidate currently has **zero clinical trials** and **zero publications** supporting it. This is a model-only signal (Evidence Level L5) with no mechanistic or clinical rationale identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No TFDA/ARTG-approved indication text on file (drug not marketed in Australia); generically known as a lincosamide antibiotic |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Lincomycin is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on information embedded elsewhere in this evidence pack, Lincomycin is described as an antibacterial agent that inhibits bacterial protein synthesis via the 50S ribosomal subunit — consistent with its known class, the lincosamides.

For the top-ranked candidate, **hyperamylasemia** (elevated blood amylase, typically associated with pancreatic or salivary gland pathology), the evidence pack's own rationale is explicit: there is **no known mechanistic link** between an antibacterial agent acting on bacterial ribosomes and this metabolic/enzymatic condition. The prediction rests entirely on the TxGNN model's statistical score (rank 8,929 of the model's output), with no supporting clinical trial or literature evidence identified in any of the three source databases queried (ClinicalTrials.gov, ICTRP, PubMed).

This is a case where the model signal and the biological plausibility diverge — the score is high, but nothing in the supporting evidence (mechanistic, clinical, or published) corroborates it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

Lincomycin is not currently marketed in Australia — 0 ARTG entries were found, and no product license records are available for this drug.

## Safety Considerations

Lincomycin is not currently marketed in Australia, so no ARTG-registered Product Information is available to reference. Key warnings, contraindications, and drug interaction data are all currently unrecorded in this evidence pack (DDI query returned "not found"). This is flagged as a **Blocking** data gap (DG001) — safety review (S1) cannot proceed until TFDA/international product labelling is obtained and parsed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (hyperamylasemia) has no clinical trial or literature support and no identified mechanistic link — it is a model-only signal (L5) with no basis for further evaluation at this time. Separately, the drug's regulatory and safety data are incomplete, which independently blocks any safety pre-assessment.

**To proceed, the following is needed:**
- Mechanism-of-action data for Lincomycin (DrugBank API query, DG002)
- TFDA/TGA product information (label, warnings, contraindications) — currently a blocking gap (DG001)
- Any preclinical or mechanistic rationale connecting Lincomycin to hyperamylasemia, if this candidate is to be pursued further
- Drug interaction (DDI) data, currently unresolved ("not found")

**Note on this batch:** This evidence pack scored 10 candidate indications for Lincomycin; per report convention, only the top-ranked candidate (by TxGNN score) is profiled above. Two lower-ranked candidates in the same batch — *septicemic plague* (rank 8) and *urinary tract infection* (rank 10) — reached decision stage S1 ("Research Question") on the strength of older in-vitro susceptibility literature and loosely related trial registrations, but neither reached a stronger recommendation than Hold/Research Question. None of the 10 candidates in this batch currently support a Go or Proceed-with-Guardrails decision.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

