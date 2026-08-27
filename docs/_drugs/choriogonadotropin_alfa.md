---
layout: default
title: Choriogonadotropin Alfa
parent: 僅模型預測 (L5)
nav_order: 147
evidence_level: L5
indication_count: 10
---

# Choriogonadotropin Alfa
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

Using the report format directly since this task is a self-contained content-generation job (no code/DB work applies here). I reviewed the Evidence Pack carefully before drafting — note that `original_indications` and `licenses` are both empty and `original_moa` is a declared Data Gap, so I did not fabricate values for those fields; I only used mechanistic detail that is explicitly present in the pack's own `repurposing_rationale` text.

---

# Choriogonadotropin Alfa: Original Indication Not on File → Predicted Signal for Peptic Esophagitis

## One-Sentence Summary

Choriogonadotropin alfa (recombinant hCG, DrugBank DB00097) has no approved-indication or ARTG licence data in the current evidence pack, and its mechanism-of-action record is a declared data gap. The TxGNN model's top prediction for this drug is **Peptic Esophagitis**, but the evidence pack itself states there is **no known mechanistic link** between hCG and oesophageal disease, and **zero clinical trials and zero publications** currently support this — or any of the drug's other nine top-ranked — predictions.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no ARTG/TFDA licence data on file) |
| Predicted New Indication | Peptic Esophagitis |
| TxGNN Prediction Score | 98.44% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed (0 registered licences) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data and original-indication information are not available in the evidence pack for choriogonadotropin alfa. The only pharmacological detail on record comes from the prediction's own rationale text, which notes that hCG acts as an agonist at the LHCGR (luteinising hormone/choriogonadotropin receptor), primarily driving gonadal steroidogenesis.

The evidence pack is explicit that this receptor pathway has **no known intersection** with the pathophysiology of peptic esophagitis (oesophageal mucosal barrier integrity, acid reflux). The rationale describes the candidate as arising purely from TxGNN graph connectivity, with no biological plausibility evidence behind it.

This pattern is not isolated to the top candidate. Across all ten of the model's highest-ranked predictions for this drug — spanning oesophageal disorders, cardiac conduction disorders (His bundle tachycardia, sinoatrial block, sinoatrial node disease, progressive familial heart block), Raynaud disease and POTS — the accompanying rationale consistently states there is no known mechanistic link, and several cardiac-rhythm predictions are explicitly flagged as likely **clustering artefacts** rather than genuine signals. Taken together, this indicates the current TxGNN output for choriogonadotropin alfa reflects a model-evidence gap rather than a credible repurposing hypothesis.

## Clinical Trial Evidence

No clinical trials currently registered for peptic esophagitis with this drug (ClinicalTrials.gov and ICTRP queries both returned zero results).

## Literature Evidence

No related literature currently available (PubMed query returned zero results).

## Australia Market Information

No ARTG entries were identified for choriogonadotropin alfa in this evidence pack — 0 licences on file, and market status is recorded as not marketed. No product/dosage-form/indication information is available to summarise.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Key warnings, contraindications and drug–drug interaction data are all currently unrecorded in this evidence pack (DDI query status: not found).

## Other Candidate Indications (Ranks 2–10)

Because this evidence pack covers multiple TxGNN candidates for the same drug (`TW-DB00097-multi`), it's worth noting the same pattern holds across the board — every one of the top 10 predictions is Evidence Level **L5**, decision stage **S0**, recommendation **Hold**, with zero trials and zero literature:

| Rank | Predicted Indication | TxGNN Score | Notes from rationale |
|------|----------------------|-------------|-----------------------|
| 2 | Postural orthostatic tachycardia syndrome | 98.33% | No known link to autonomic/vascular regulation |
| 3 | Esophageal disease | 97.61% | Overly broad disease category; no specific pathology to map |
| 4 | Raynaud disease | 97.43% | Purely speculative; no published hCG–vasospasm link |
| 5 | Non-syndromic esophageal malformation | 96.89% | Congenital structural defect; low biological plausibility for any drug therapy |
| 6 | Esophageal ulcer | 96.84% | Same oesophageal cluster as rank 1 and 3; no mechanistic evidence |
| 7 | His bundle tachycardia | 95.95% | No known hCG action on cardiac conduction tissue |
| 8 | Sinoatrial block | 95.88% | Likely clustering artefact with other cardiac-rhythm predictions |
| 9 | Progressive familial heart block | 95.66% | Genetic ion-channel disorder; no hormonal mechanism pathway |
| 10 | Sinoatrial node disease | 95.47% | Same cardiac-rhythm cluster; flagged as prediction noise |

This spread — clustering around oesophageal and cardiac-conduction diseases with no shared pharmacological rationale — is itself a signal that the current TxGNN scores for this drug should not be acted on without independent mechanistic review.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten of the model's top predicted indications for choriogonadotropin alfa sit at Evidence Level L5 (model prediction only), with zero supporting clinical trials or publications, and the evidence pack's own rationale text explicitly denies biological plausibility for the top candidate and most of the others. In addition, two foundational data gaps — TFDA/PI warnings and contraindications (Blocking, DG001) and mechanism of action (High, DG002) — mean this candidate cannot yet even enter the S1 safety screening stage.

**To proceed, the following is needed:**
- TFDA/TGA-approved Product Information — warnings and contraindications (resolves blocking gap DG001)
- Verified original indication(s) and detailed mechanism of action from DrugBank/PI (resolves high-priority gap DG002)
- Independent mechanistic or preclinical evidence for peptic esophagitis (or any other top candidate) beyond the raw TxGNN connectivity score
- A re-query of clinical trial registries and PubMed at a later data cutoff, since all current searches across all 10 candidates returned zero results
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

