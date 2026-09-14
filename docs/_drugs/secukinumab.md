---
layout: default
title: Secukinumab
parent: 僅模型預測 (L5)
nav_order: 618
evidence_level: L5
indication_count: 10
---

# Secukinumab
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

# Secukinumab: From Psoriasis/Psoriatic Arthritis to Primary Release Disorder of Platelets

## One-Sentence Summary

Secukinumab is an anti-IL-17A monoclonal antibody used for inflammatory conditions such as psoriasis, psoriatic arthritis and ankylosing spondylitis. The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the accompanying mechanistic review flags it as a likely false-positive knowledge-graph association rather than a biologically plausible lead.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Psoriasis / Psoriatic Arthritis / Ankylosing Spondylitis (as referenced in the evidence pack; not confirmed via a structured original-indication field) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 98.16% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form (flagged as a High-severity data gap). Based on the information available, Secukinumab neutralises IL-17A to suppress Th17-driven inflammatory signalling, and this mechanism underlies its established use in psoriasis, psoriatic arthritis and ankylosing spondylitis.

Primary release disorder of platelets, however, is a platelet granule secretion defect, predominantly inherited as a storage-pool disease. It has no known relationship to IL-17A signalling — the pathology is structural/secretory, not inflammatory. The evidence pack's own mechanistic review explicitly concludes that this prediction is most likely a false positive arising from node proximity or comorbidity patterns in the knowledge graph, rather than a genuine pharmacological link.

No clinical trials, ICTRP registrations, or PubMed literature were found connecting Secukinumab to this indication, which is consistent with the absence of a plausible biological rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Australia Market Information

Secukinumab has no ARTG listings (0 entries; market status: Not Marketed). No Australian product information is currently available for reference.

## Safety Considerations

- **Key Warnings**: Not available — TGA-approved Product Information does not exist for this product in Australia (drug not marketed; 0 ARTG entries). This is recorded as a Blocking data gap that prevents any formal safety pre-assessment (S1 stage).
- **Drug Interaction Data**: No interaction data found in the queried source.

Until local registration status changes, any safety assessment should rely on the manufacturer's overseas product information (e.g., FDA/EMA label) rather than a TGA PI.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical or literature evidence for Secukinumab in primary release disorder of platelets, and the proposed mechanism (IL-17A neutralisation) has no established connection to this platelet secretory defect — the evidence pack itself assesses this as a likely knowledge-graph false positive. A Blocking data gap on TFDA/TGA-equivalent safety labelling also prevents this candidate from advancing to formal safety review regardless of indication-level evidence.

**To proceed, the following is needed:**
- Formal mechanism of action documentation (currently a data gap)
- TGA-equivalent Product Information / safety labelling (Blocking gap — required before any S1 safety assessment)
- If this indication is pursued further, dedicated preclinical/mechanistic studies on IL-17A's role in platelet granule secretion, since none currently exist

**Note:** Among the other candidates reviewed for this drug, **drug-induced osteoporosis** (rank 5, score 95.27%) has comparatively stronger mechanistic grounding — IL-17 is known to promote RANKL expression and osteoclast differentiation — and was flagged as a "Research Question" rather than a straight Hold. This may be a more productive direction for future literature review than the top-ranked candidate above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

