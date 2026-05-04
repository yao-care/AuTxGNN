---
layout: default
title: Docusate
parent: 僅模型預測 (L5)
nav_order: 161
evidence_level: L5
indication_count: 10
---

# Docusate
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

# Docusate: From Constipation Management to Plummer-Vinson Syndrome

## One-Sentence Summary

Docusate is an anionic surfactant widely used internationally as a faecal softener for constipation management, though it holds no current TGA registration in Australia.
The TxGNN model predicts it may have potential in **Plummer-Vinson Syndrome**, with **no clinical trials** and **no publications** directly supporting this indication.
The evidence base is entirely model-derived, and across all ten predicted indications the mechanistic rationale remains weak or absent.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No TGA-registered indication (not marketed in Australia) |
| Predicted New Indication | Plummer-Vinson Syndrome |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on established pharmacological knowledge, Docusate (available as docusate sodium or docusate calcium) is an anionic surfactant. It reduces the surface tension at the oil–water interface within the intestinal lumen, allowing water and lipids to penetrate the stool mass — producing a faecal softening effect without stimulating peristalsis. It is most commonly used as an adjunct to prevent straining in post-operative patients or those at cardiovascular risk.

Plummer-Vinson Syndrome (also known as Paterson-Brown-Kelly Syndrome) is a rare condition defined by the clinical triad of iron deficiency anaemia, dysphagia caused by oesophageal webs, and atrophic glossitis. It predominantly affects middle-aged women and is strongly associated with chronic nutritional deficiency, particularly iron.

There is no credible mechanistic bridge between Docusate's surfactant action and the pathophysiology of Plummer-Vinson Syndrome. Docusate has no documented role in iron metabolism, erythropoiesis, or oesophageal mucosal repair. The high TxGNN score (99.18%) most likely reflects indirect graph topology — the knowledge graph may connect Docusate through nutritional absorption nodes to iron deficiency clusters — rather than a genuine therapeutic signal. The repurposing rationale embedded in the Evidence Pack itself explicitly acknowledges the absence of mechanistic support, characterising this as an indirect graph inference rather than a biologically grounded prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Docusate currently holds no ARTG entries and is not registered with the TGA. It is not marketed in Australia as a standalone product.

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|-------------|--------------|-------------|---------------------|
| — | No entries found | — | — |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.18%), this result is assessed as a knowledge graph topology artefact rather than a biologically meaningful therapeutic signal. There is no mechanistic rationale, no supporting clinical trial data, no published literature, and no existing TGA registration for Docusate in any indication. This pattern is consistent across all ten predicted indications — nine of which are L5 (model prediction only), with the sole exception being a completed iron deficiency trial (NCT05423249) where Docusate most likely served as an ancillary stool softener rather than the primary intervention. Advancing any of these predictions without foundational mechanistic and safety data would not be appropriate.

**To proceed, the following is needed:**

- Establish a credible mechanistic hypothesis linking Docusate's surfactant properties to the target disease pathophysiology — this is a prerequisite before any indication can exit Hold status
- Obtain complete MOA data from DrugBank (DB11089) to fill the current data gap
- Source and review the TGA Product Information document (or equivalent global PI) to complete baseline safety assessment, including warnings and contraindications
- Conduct a targeted preclinical literature search (in vitro / animal model studies) for any of the predicted indications to determine whether evidence level can be elevated above L5
- Consider consolidating the three bile-related predictions (bile duct disease, bile duct neoplasm, obstructive jaundice) into a single mechanistic evaluation, as these share the most biologically plausible theoretical link to Docusate's known surfactant activity in bile salt emulsification — this cluster represents the most scientifically defensible avenue for hypothesis generation if further investigation is warranted

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

