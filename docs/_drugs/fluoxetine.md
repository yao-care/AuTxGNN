---
layout: default
title: Fluoxetine
parent: 僅模型預測 (L5)
nav_order: 286
evidence_level: L5
indication_count: 10
---

# Fluoxetine
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

# Fluoxetine: From SSRI Antidepressant Use to Schizoid Personality Disorder (TxGNN Top-Ranked Prediction)

## One-Sentence Summary

> Fluoxetine is a well-established selective serotonin reuptake inhibitor (SSRI), broadly used for depression, panic disorder and related anxiety conditions, though this Evidence Pack has no registered original indication text on file. The TxGNN model's top-ranked prediction for this drug is **Schizoid Personality Disorder**, but this is currently supported only by **3 indirect publications** and **no clinical trials**, and the drug itself is not currently marketed in this jurisdiction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in this Evidence Pack (no ARTG-style licence record). Literature within this pack repeatedly characterises fluoxetine as an SSRI antidepressant used for major depressive disorder, panic disorder and related anxiety conditions. |
| Predicted New Indication | Schizoid Personality Disorder |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data could not be confirmed via DrugBank in this Evidence Pack (flagged as data gap DG002, High severity). That said, the literature captured within this pack consistently describes fluoxetine as an SSRI: it selectively blocks neuronal reuptake of serotonin (5-HT), increasing synaptic serotonin availability (e.g. PMID 2878798, PMID 7786880). This serotonergic mechanism underlies fluoxetine's established use across depression, panic disorder, OCD and bulimia nervosa.

Schizoid Personality Disorder, however, is not conventionally framed as a serotonergic-circuit-driven condition. Its core features — social detachment, restricted range of emotional expression, and indifference to relationships — sit outside the anxiety/mood pathology that SSRIs are pharmacologically designed to target. This is a meaningful mismatch between the drug's established mechanism and the predicted indication's clinical phenotype.

Consistent with this, the evidence base is weak: no clinical trials have tested fluoxetine specifically in schizoid PD, and the three retrieved publications are comorbidity descriptions or reviews of Cluster A personality disorders generally, not direct treatment evidence. This pattern suggests the TxGNN score likely reflects a knowledge-graph-level association (e.g., shared psychiatric disease neighbourhoods) rather than a pharmacologically validated signal.

---

## Clinical Trial Evidence

No related clinical trials are currently registered for fluoxetine in schizoid personality disorder.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29955451](https://pubmed.ncbi.nlm.nih.gov/29955451/) | 2016 | Review | The Mental Health Clinician | Reviews pharmacologic treatment of Cluster A personality disorders (paranoid, schizoid, schizotypal); notes reduced quality of life in these patients but does not establish a fluoxetine-specific protocol for schizoid PD. |
| [16390895](https://pubmed.ncbi.nlm.nih.gov/16390895/) | 2006 | Cohort | American Journal of Psychiatry | Six-month outcome study of depressed patients; personality-disorder comorbidity examined as a predictor of illness course — not a direct schizoid PD treatment trial. |
| [10929788](https://pubmed.ncbi.nlm.nih.gov/10929788/) | 2000 | Cohort (comorbidity description) | Comprehensive Psychiatry | Assessed personality traits/disorders (including schizoid traits) in 148 patients with body dysmorphic disorder; some received fluvoxamine (not fluoxetine) — indirect evidence only. |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. This Evidence Pack has no resolved data for key warnings, contraindications, or drug–drug interactions (DDI query returned "not found").

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between fluoxetine's serotonergic action and schizoid PD's core pathology (social/emotional detachment rather than anxiety- or mood-circuit dysfunction) is weak, and no direct treatment evidence — trial or otherwise — currently exists for this pairing. This corresponds to decision stage S0 in the scoring model.

**To proceed, the following is needed:**
- TFDA/TGA-approved Product Information (PI) with warnings and contraindications — currently blocking entry into the S1 safety review (data gap DG001)
- Confirmed mechanism-of-action data via DrugBank (data gap DG002)
- At minimum, a case series or open-label study directly treating schizoid personality disorder with fluoxetine, rather than comorbidity-level or indirect literature
- Note: several lower-ranked predictions in this same Evidence Pack (e.g., agoraphobia, phobic disorder, melancholia) carry substantially stronger evidence (L2, decision stage S3, "Proceed with Guardrails") and may warrant a separate, higher-priority report if the goal is near-term repurposing rather than following the single highest TxGNN score.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

