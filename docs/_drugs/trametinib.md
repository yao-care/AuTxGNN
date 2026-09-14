---
layout: default
title: Trametinib
parent: 僅模型預測 (L5)
nav_order: 692
evidence_level: L5
indication_count: 10
---

# Trametinib
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

# Trametinib: From BRAF V600 Mutation-Positive Melanoma to Choroideremia

## One-Sentence Summary

> Trametinib is a MEK1/2 inhibitor originally developed (in combination with dabrafenib) for BRAF V600 mutation-positive melanoma.
> The TxGNN model predicts a possible link to **Choroideremia**, but this prediction is currently supported by **zero clinical trials** and **zero publications**, and the drug's own rationale flags it as a likely knowledge-graph false positive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | BRAF V600 mutation-positive melanoma (in combination with dabrafenib) — inferred from associated trial records in this evidence pack, not from an Australian regulatory listing |
| Predicted New Indication | Choroideremia |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for trametinib was not available as a structured field in this evidence pack. However, trial-level documentation within the pack (e.g. NCT01387204) describes trametinib (GSK1120212) as "a reversible and highly selective allosteric inhibitor of MEK1 and MEK2 activation and kinase activity," developed for malignant melanoma. Its established clinical role, evident throughout the associated trial records, is as a MAPK-pathway (BRAF/MEK) inhibitor used together with dabrafenib in BRAF V600E/K mutation-positive melanoma.

Choroideremia is a hereditary retinal degeneration caused by loss-of-function mutations in the *CHM* gene, which encodes Rab escort protein 1 (REP1) — a protein involved in intracellular vesicle trafficking, not in MAPK/MEK signalling. There is no established pathway overlap between MEK inhibition and REP1-dependent photoreceptor/retinal pigment epithelium degeneration.

The evidence pack's own repurposing rationale for this candidate states explicitly that the association shows "no known mechanistic link to the MAPK/MEK pathway" and should be judged "a knowledge-graph false positive, with no supporting evidence." This assessment is consistent with the complete absence of clinical trials or literature retrieved for this drug–disease pair, and the recommendation below reflects that.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Trametinib has no ARTG entries in the dataset used for this evidence pack (`total_licenses = 0`, market status "Not marketed"). No Australian product/indication information is available to summarise.

---

## Cytotoxicity

Trametinib is an antineoplastic agent (MEK1/2 inhibitor used in BRAF-mutant melanoma), so this section applies to the drug's established oncology use, independent of the (unsupported) choroideremia prediction above.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (MEK1/2 inhibitor) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the Product Information (PI) warnings and precautions |
| Handling Protection | Please refer to institutional cytotoxic/hazardous drug handling guidelines |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The choroideremia prediction has no clinical trial or literature support, and there is no plausible mechanistic link between MEK inhibition and *CHM*/REP1-driven retinal degeneration. The evidence pack itself flags this as a likely knowledge-graph artefact rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- Independent biological/mechanistic validation (e.g. preclinical or genetic evidence connecting MAPK/MEK signalling to *CHM*/REP1 pathology) before any further review
- TGA-approved Product Information for trametinib to fill the safety data gaps (key warnings, contraindications, drug interactions) noted in this evidence pack
- Verified mechanism-of-action documentation (DG002) to replace the current data gap

**Note for reviewers:** this evidence pack (`TW-DB08911-multi`) contains other predicted indications for trametinib with materially stronger evidence — notably *non-cutaneous melanoma* (L2, "Proceed with Guardrails," supported by multiple completed Phase 2/3 BRAF/MEK trials) — which may warrant a separate, dedicated evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

