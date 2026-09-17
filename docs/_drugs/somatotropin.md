---
layout: default
title: Somatotropin
parent: Model Prediction Only (L5)
nav_order: 638
evidence_level: L5
indication_count: 10
---

# Somatotropin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Somatotropin: From Growth Hormone Deficiency to Middle Ear Neuroendocrine Tumor

## One-Sentence Summary

Somatotropin (recombinant human growth hormone) is established therapy for growth hormone deficiency and related growth failure conditions. The TxGNN model's top-ranked prediction for this drug is **Middle Ear Neuroendocrine Tumor**, but this association is supported only by **2 indirectly related publications** and **no clinical trials**, and the drug's own mechanism (GH/IGF-1 axis activation) is more plausibly a theoretical *risk* for this tumour type than a treatment rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Growth hormone deficiency / growth failure (general therapeutic use; specific ARTG-approved indication text is not available — see Australia Market Information) |
| Predicted New Indication | Middle Ear Neuroendocrine Tumor |
| TxGNN Prediction Score | 96.82% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for this Evidence Pack is not available (data gap, High severity). Based on general pharmacological knowledge, Somatotropin is recombinant human growth hormone, which acts on the GH receptor to stimulate hepatic IGF-1 production, driving linear growth and metabolic effects. Its established clinical use is treatment of growth hormone deficiency and growth failure syndromes.

The link between growth hormone and middle ear neuroendocrine tumour is not mechanistically supported by the evidence collected. The two available publications examine stress hormones (including GH) in Ménière's disease/acoustic neuroma patients, and histopathological growth factors in vestibular schwannomas — neither studies GH as a treatment for these tumours. If anything, the theoretical concern runs in the opposite direction: GH/IGF-1 axis activation could plausibly *promote* proliferation in a neuroendocrine tumour, making this a potential safety signal rather than a therapeutic hypothesis.

The TxGNN model score (96.82%) reflects a strong statistical association in the knowledge graph, but this is not corroborated by any direct clinical, preclinical, or mechanistic evidence of therapeutic benefit. This is a case where a high model score does not translate into a credible repurposing candidate without further validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15925138](https://pubmed.ncbi.nlm.nih.gov/15925138/) | 2005 | Observational | Brain Research Bulletin | Measured stress hormones (ACTH, cortisol, GH, prolactin) in Ménière's disease and acoustic neuroma patients vs. facial spasm controls; found a positive correlation between cortisol and ACTH in Ménière's patients. GH was one of several hormones assayed, not a treatment variable. |
| [11200590](https://pubmed.ncbi.nlm.nih.gov/11200590/) | 2000 | Immunohistochemical Study | Acta Oto-Laryngologica | Retrospective morphological/immunohistochemical study of 69 vestibular schwannomas examining vascularity and inflammation as growth predictors; does not evaluate GH or somatotropin therapy. |

---

## Australia Market Information

Somatotropin is currently not marketed in Australia under this Evidence Pack's regulatory data — 0 ARTG entries were found.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Note: TGA/TFDA-equivalent warnings and contraindications for this drug are a **Blocking** data gap in this Evidence Pack and must be resolved before any safety assessment (S1 stage) can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Middle Ear Neuroendocrine Tumor) has no clinical trial support and only indirect, non-therapeutic literature. The plausible mechanistic direction (GH/IGF-1 promoting tumour proliferation) argues against rather than for repurposing, so this candidate should not advance.

**To proceed, the following is needed:**
- TFDA/TGA-equivalent Product Information (warnings, contraindications) — currently a Blocking data gap
- Confirmed mechanism of action (MOA) data from DrugBank or primary literature
- Dedicated preclinical or case-level evidence specifically evaluating GH exposure in neuroendocrine tumour patients before any therapeutic hypothesis can be entertained

**Note:** This Evidence Pack contains 9 additional TxGNN-predicted indications for Somatotropin, several with materially stronger evidence (e.g., mosaic monosomy X and Turner syndrome variants reach Evidence Level L1–L2 with completed Phase 3 data). Those candidates warrant separate evaluation and are not covered by this report, which addresses only the highest-scoring prediction as specified.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

