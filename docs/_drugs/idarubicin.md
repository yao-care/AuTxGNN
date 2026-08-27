---
layout: default
title: Idarubicin
parent: 僅模型預測 (L5)
nav_order: 340
evidence_level: L5
indication_count: 10
---

# Idarubicin
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

# Idarubicin: From Acute Myeloid Leukaemia to Bulbar Polio

## One-Sentence Summary

> Idarubicin is an anthracycline cytotoxic agent whose established use is in acute myeloid leukaemia (AML), though this cannot be confirmed against Australian licensing data as the drug is not currently marketed here. The TxGNN model's top-ranked prediction is **Bulbar Polio**, scoring **97.05%**, but this signal is supported by **zero clinical trials** and **zero publications**, and the model's own mechanistic rationale flags it as a likely false-positive rather than a credible repurposing lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Myeloid Leukaemia (AML) — inferred from evidence-pack rationale text; not confirmed by structured licence data, as idarubicin is not marketed in Australia |
| Predicted New Indication | Bulbar Polio |
| TxGNN Prediction Score | 97.05% |
| Evidence Level | L5 (model prediction only — no trials, no literature) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for idarubicin is not available in this evidence pack (flagged as a High-severity data gap). Based on the drug's known pharmacological class, idarubicin is an anthracycline that intercalates DNA and inhibits topoisomerase II, and is used as a cytotoxic chemotherapy agent — the evidence pack's own rationale text repeatedly references its approved use in AML.

For the top-ranked candidate, **bulbar polio**, the model's own repurposing rationale is explicit that there is **no plausible mechanistic link**: bulbar polio is a viral (poliovirus) infection of brainstem motor neurons, whereas idarubicin has no antiviral or neuroprotective activity. The rationale describes this as "a likely false-positive signal from knowledge-graph embedding similarity" rather than a genuine pharmacological hypothesis. The same pattern holds for most of the other nine candidates screened (5q35 microduplication syndrome, neuralgic amyotrophy, familial/reactive thrombocytosis, vertebral–endocrine–T-cell dysfunction syndrome, and obsolete Hodgkin's granuloma) — none have a coherent mechanistic rationale, clinical trials, or literature support.

The one partial exception is rank 8, **retroperitoneal neoplasm** (score 77.40%, L4/S1), where a single case-report/review (PMID 39588445) describes granulocytic (myeloid) sarcoma — an extramedullary manifestation of AML-spectrum disease that can occur retroperitoneally. This is mechanistically closer to idarubicin's established AML indication, but the cited literature is a descriptive case series, not evidence of idarubicin efficacy in this setting, and it did not rank as the model's top prediction. Because the report format is built around the single highest-ranked candidate, this signal is noted here for completeness but is not the primary subject of this evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Idarubicin holds no ARTG entries and is not currently marketed in Australia (0 licences on record).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Anthracycline class; DNA intercalator / topoisomerase II inhibitor) |
| Myelosuppression Risk | High — anthracyclines including idarubicin characteristically cause dose-limiting neutropenia and thrombocytopenia |
| Emetogenicity Classification | Moderate to high (typical of anthracycline-class agents) |
| Monitoring Items | FBC with differential, cardiac function (LVEF/echocardiogram, given class-related cardiotoxicity), liver and renal function, infusion site (vesicant potential) |
| Handling Protection | Yes — standard cytotoxic drug handling precautions required per anthracycline class |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. (TFDA warnings, contraindications and drug-interaction data are recorded as a Blocking data gap in this evidence pack — direct PI lookup is required before any clinical use is considered.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (bulbar polio) has a high raw score but no supporting clinical trials, no literature, and an explicit mechanistic disqualification in the model's own rationale — this is an L5, S0 signal with no basis for further action. None of the other nine screened candidates fare materially better; the closest to a credible lead (retroperitoneal neoplasm, via an AML-related extramedullary case report) is indirect, descriptive evidence only.

**To proceed, the following is needed:**
- TFDA/TGA Product Information PDF for idarubicin (Blocking gap — required before any safety assessment)
- Confirmed mechanism-of-action data from DrugBank (High-priority gap)
- If pursuing the retroperitoneal neoplasm / granulocytic sarcoma lead further: targeted literature search on idarubicin specifically (not just AML-class agents) in extramedullary/granulocytic sarcoma presentations
- No further action warranted on bulbar polio or the other L5/S0 candidates without new mechanistic or empirical evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

