---
layout: default
title: Evolocumab
parent: 僅模型預測 (L5)
nav_order: 211
evidence_level: L5
indication_count: 10
---

# Evolocumab
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

# Evolocumab: From Hypercholesterolaemia to Symptomatic Form of Haemophilia in Female Carriers

## One-Sentence Summary

Evolocumab (DrugBank: DB09303) is a PCSK9 inhibitor, well established internationally for the treatment of hypercholesterolaemia and cardiovascular risk reduction, though no TGA-registered products were identified in the current dataset.
The TxGNN model predicts it may be effective for **Symptomatic Form of Haemophilia in Female Carriers** (Rank 1 prediction),
however there are currently **0 clinical trials** and **0 publications** directly supporting this repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current regulatory dataset (PCSK9 inhibitor; internationally indicated for hypercholesterolaemia and cardiovascular risk reduction) |
| Predicted New Indication | Symptomatic form of haemophilia in female carriers |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed (0 ARTG entries found) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on known pharmacological information, Evolocumab is a fully human monoclonal antibody (IgG2) that inhibits PCSK9 (proprotein convertase subtilisin/kexin type 9), a serine protease secreted by the liver. By binding and neutralising PCSK9, Evolocumab prevents the degradation of LDL receptors on hepatocytes, resulting in upregulation of LDL receptor expression and a substantial reduction in circulating LDL-cholesterol. This mechanism is entirely within the lipid metabolism pathway.

Symptomatic haemophilia in female carriers involves partial deficiency of coagulation Factor VIII (in X-linked carriers with skewed X-inactivation), leading to abnormal bleeding. This condition sits firmly within the coagulation cascade — a pathway biochemically independent from PCSK9-mediated LDL receptor cycling. The repurposing rationale in the Evidence Pack notes no known molecular intersection between PCSK9 inhibition and Factor VIII biology, and suggests the high TxGNN prediction score may arise from missing PCSK9 MOA node data in the knowledge graph, leading the model to assign similarity via non-specific topological proximity rather than true mechanistic overlap.

In summary, the biological plausibility for this specific repurposing prediction is **very low**. The prediction is not supported by any clinical trial data or published literature, and the mechanistic justification is absent. This is a case where a high model score does not translate into a clinically actionable hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Evolocumab in symptomatic haemophilia in female carriers.

---

## Literature Evidence

Currently no related literature available for Evolocumab in symptomatic haemophilia in female carriers.

---

## Australia Market Information

No ARTG entries were identified for Evolocumab in the current dataset. The regulatory query returned 0 results.

> **Note for clinicians:** Evolocumab (brand name Repatha®) is approved by multiple major regulatory agencies internationally (FDA, EMA) for hypercholesterolaemia and established cardiovascular disease. Clinicians should independently verify current TGA registration status at the ARTG public portal (https://www.tga.gov.au/resources/artg).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No safety data (key warnings, contraindications, or drug interaction data) was available in the current dataset for this evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigned a high prediction score (99.82%), but this appears to reflect a knowledge graph artefact rather than genuine mechanistic plausibility — PCSK9 inhibition (lipid metabolism) and haemophilia in female carriers (coagulation Factor VIII deficiency) operate through entirely separate biological pathways with no documented molecular intersection. There is no supporting clinical trial or published literature evidence whatsoever (Evidence Level L5).

**To consider progressing beyond Hold, the following would be required:**

- Identification of a credible mechanistic hypothesis linking PCSK9 biology to Factor VIII expression, function, or clearance (currently absent in the literature)
- At least one published preclinical study (in vitro or animal model) demonstrating relevant biological activity in haemophilia or coagulation physiology
- Review of whether the TxGNN knowledge graph has been updated with complete PCSK9 MOA nodes, as the rationale notes this gap may be artificially inflating the prediction score
- TGA/ARTG registration confirmation for Evolocumab to establish baseline regulatory standing in Australia
- Complete MOA documentation (DrugBank query recommended to close DG002)
- TGA Product Information retrieval to complete safety profiling (DG001)

---

> ⚠️ **Disclaimer:** This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require rigorous clinical validation before therapeutic application. All predictions should be interpreted in the context of their evidence level.
>
> *Report generated: 5 April 2026 | Candidate ID: TW-DB09303-multi | Version: v4*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

