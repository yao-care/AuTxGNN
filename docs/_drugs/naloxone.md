---
layout: default
title: Naloxone
parent: 僅模型預測 (L5)
nav_order: 459
evidence_level: L5
indication_count: 10
---

# Naloxone
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

# Naloxone: From Opioid Overdose Reversal to Continuous Spikes and Waves During Sleep

## One-Sentence Summary

Naloxone is a competitive opioid receptor antagonist most widely known for reversing opioid overdose and opioid-induced respiratory depression. The TxGNN model's top prediction for this drug is **continuous spikes and waves during sleep (CSWS)**, a rare paediatric epileptic encephalopathy, but this direction is currently supported by **0 clinical trials** and **0 publications**. This is a model-only signal with no corroborating clinical or mechanistic evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack's regulatory data (no ARTG licences found); naloxone is generally used to reverse opioid overdose/respiratory depression |
| Predicted New Indication | Continuous spikes and waves during sleep (CSWS) |
| TxGNN Prediction Score | 88.17% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this candidate was not available in the evidence pack (DrugBank MOA field flagged as a data gap). Based on general pharmacological knowledge, naloxone is a competitive antagonist at opioid receptors (predominantly mu-opioid), and its established clinical role is reversing the effects of opioid agonists in overdose or perioperative settings.

CSWS is a rare, structurally and electrophysiologically defined childhood epilepsy syndrome. There is no established pathophysiological link between opioid receptor blockade and the mechanisms thought to drive CSWS (abnormal cortico-thalamic synchronisation during sleep). No clinical trials or publications were retrieved connecting naloxone (or related opioid antagonists) to this condition, so the prediction currently rests entirely on TxGNN's embedding-based similarity score, with no independent evidence to support or refute a plausible mechanistic rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

No ARTG entries were identified for naloxone in this evidence pack, and market status is recorded as **not marketed**. This should be independently confirmed against the current TGA/ARTG database, as naloxone products are generally available in other markets for opioid overdose reversal — the absence of a record here may reflect a data-collection gap rather than true non-availability.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Key warnings, contraindications, and drug interaction data were not available in this evidence pack (DDI query returned no results).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (CSWS) has no supporting clinical trials or literature (L5 — model prediction only) and no plausible mechanistic link between opioid receptor antagonism and this rare paediatric epilepsy syndrome. In addition, a blocking data gap on TFDA/TGA warnings and contraindications currently prevents even an initial safety screen (S1) for naloxone in this evidence pack.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications, interactions) to clear the blocking safety gap
- Confirmed DrugBank/mechanism-of-action detail for naloxone
- Confirmation of current ARTG/marketing status in Australia
- Any emerging clinical or preclinical evidence directly linking opioid antagonism to CSWS before this candidate is reconsidered

*Note: Other TxGNN-ranked candidates for naloxone (e.g., psychotic disorder, schizophreniform disorder) have somewhat more evidence volume but suffer from drug-identity mismatch — most retrieved trials/literature involve naltrexone rather than naloxone itself — and were independently scored Hold. None currently clear the bar for further progression.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

