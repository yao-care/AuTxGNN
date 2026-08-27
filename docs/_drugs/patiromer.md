---
layout: default
title: Patiromer
parent: 僅模型預測 (L5)
nav_order: 512
evidence_level: L5
indication_count: 10
---

# Patiromer
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

# Patiromer: From Hyperkalaemia to Mitochondrial Oxidative Phosphorylation Disorder

## One-Sentence Summary

Patiromer is a potassium-binding polymer whose only established clinical use, as reflected in this evidence pack, is managing RAAS inhibitor-associated hyperkalaemia. The TxGNN model's top prediction for this drug is **mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies**, but this is supported by **zero clinical trials and zero publications**, and the evidence pack's own mechanistic review flags the prediction as a likely knowledge-graph artefact rather than a genuine signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperkalaemia associated with RAAS inhibitor therapy (noted in evidence pack rationale; not a TGA-approved indication, as the product is unregistered in Australia) |
| Predicted New Indication | Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies |
| TxGNN Prediction Score | 98.72% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Patiromer is not available in structured form (marked as a data gap in this evidence pack). However, the evidence pack's own rationale text describes Patiromer as an orally administered, gut-restricted calcium-based cation exchange polymer: it binds potassium in the intestinal lumen and is eliminated in faeces without entering systemic circulation.

This is important context for interpreting the top prediction. Mitochondrial oxidative phosphorylation disorders are systemic, cellular-energy-metabolism conditions with no known relationship to luminal cation exchange. The evidence pack's mechanistic assessment for this specific candidate states plainly that there is no recognisable pharmacological basis for the link, and attributes the prediction to knowledge-graph node proximity noise rather than a real signal.

The other nine ranked candidates in this pack follow a similar pattern: several (colonic neoplasm, cecum villous adenoma, cecal disease, lipoma of colon, colonic lymphangioma, etc.) cluster around gastrointestinal/colonic anatomy — likely reflecting Patiromer's physical transit through the colon rather than any pharmacological effect on those tissues. None of the ten candidates have any clinical trial or literature support, and all are scored L5/Hold. This pattern suggests the current prediction set for Patiromer is dominated by graph-topology artefacts rather than biologically plausible repurposing leads.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Patiromer has no ARTG entries and is not marketed in Australia (0 licences recorded in this evidence pack).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No warnings, contraindications, or drug interaction data for Patiromer are currently available in this evidence pack — this is itself a **Blocking**-severity data gap (DG001) that prevents any preliminary safety assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical, literature, or mechanistic support for this prediction beyond the raw TxGNN score, and the evidence pack's own analysis concludes the top-ranked candidate is most likely a knowledge-graph artefact rather than a genuine repurposing signal. Combined with the missing TGA safety data, this candidate does not meet the bar to advance.

**To proceed, the following is needed:**
- TFDA/TGA-equivalent product information (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action data from DrugBank or another authoritative source (DG002)
- Independent mechanistic or preclinical rationale connecting Patiromer's cation-exchange activity to mitochondrial oxidative phosphorylation disorders, before any further evidence-gathering is warranted
- If pursuing repurposing signals for Patiromer at all, re-screening against candidates with plausible mechanistic links (e.g., conditions related to potassium/electrolyte handling) rather than the current top-ranked, graph-noise-flagged candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

