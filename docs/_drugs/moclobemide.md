---
layout: default
title: Moclobemide
parent: 僅模型預測 (L5)
nav_order: 451
evidence_level: L5
indication_count: 10
---

# Moclobemide
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

# Moclobemide: From Depression to Agoraphobia

## One-Sentence Summary

Moclobemide is a reversible monoamine oxidase-A inhibitor (RIMA), originally developed and established for the treatment of depression.
The TxGNN model predicts it may also be effective for **Agoraphobia**,
with **no dedicated clinical trials** but **12 supporting publications** currently identified — most of which studied moclobemide in the closely related diagnosis of panic disorder (of which agoraphobia is frequently a comorbid subtype), rather than agoraphobia as an independent primary endpoint.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in this evidence pack (no ARTG entries); literature context indicates moclobemide's original approved indication is depression |
| Predicted New Indication | Agoraphobia |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L2 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data for moclobemide is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on the information available in the supporting literature, moclobemide is a **reversible, selective inhibitor of monoamine oxidase-A (RIMA)**. It raises synaptic concentrations of serotonin, noradrenaline and dopamine — the mechanism underlying its established antidepressant effect.

Panic disorder and agoraphobia sit on the same anxiety-disorder spectrum and are frequently comorbid, sharing serotonergic/noradrenergic dysregulation as a proposed common pathway. Several older RCTs tested moclobemide specifically in "panic disorder with agoraphobia" cohorts, which is why the TxGNN model links moclobemide to agoraphobia with a high prediction score.

Importantly, none of the identified trials used agoraphobia itself as the primary diagnostic endpoint — agoraphobia was consistently a comorbid subgroup within panic disorder trials. This is a **neighbouring-indication extrapolation** rather than direct disease-specific evidence, which is why the evidence level is capped at L2 despite the high TxGNN score. (For reference, two other TxGNN-predicted indications for this drug — neurotic depression and melancholia — carry stronger direct evidence, L1/Proceed with Guardrails, since they map onto moclobemide's original depression mechanism more directly.)

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10448444](https://pubmed.ncbi.nlm.nih.gov/10448444/) | 1999 | RCT (placebo-controlled) | The British Journal of Psychiatry | Randomised trial of moclobemide, CBT, and their combination in panic disorder with agoraphobia |
| [10361962](https://pubmed.ncbi.nlm.nih.gov/10361962/) | 1999 | RCT (vs clomipramine) | European Archives of Psychiatry and Clinical Neuroscience | Multicentre double-blind trial: moclobemide 450mg/day vs clomipramine 150mg/day in panic disorder with/without agoraphobia (n=135) |
| [16850261](https://pubmed.ncbi.nlm.nih.gov/16850261/) | 2006 | Comparative small trial | Metabolic Brain Disease | SPECT study comparing citalopram and moclobemide effects on resting brain perfusion in social anxiety disorder |
| [28867934](https://pubmed.ncbi.nlm.nih.gov/28867934/) | 2017 | Review | Dialogues in Clinical Neuroscience | Guideline-based review of anxiety disorder treatment, including panic disorder/agoraphobia |
| [32002937](https://pubmed.ncbi.nlm.nih.gov/32002937/) | 2020 | Review | Advances in Experimental Medicine and Biology | Review of current and novel psychopharmacological drugs for anxiety disorders including panic disorder/agoraphobia |
| [7717094](https://pubmed.ncbi.nlm.nih.gov/7717094/) | 1995 | Review | Acta Psychiatrica Scandinavica Supplementum | Review of reversible MAO-A inhibitors (RIMAs) including moclobemide in mental and other disorders |
| [2248064](https://pubmed.ncbi.nlm.nih.gov/2248064/) | 1990 | Review | Acta Psychiatrica Scandinavica Supplementum | Review of MAOI efficacy in panic disorder with agoraphobia, social phobia and other psychiatric disorders |
| [8313401](https://pubmed.ncbi.nlm.nih.gov/8313401/) | 1993 | Review | Clinical Neuropharmacology | Review of reversible MAO-A inhibitors in panic disorder |
| [1498904](https://pubmed.ncbi.nlm.nih.gov/1498904/) | 1992 | Review | Clinical Neuropharmacology | Review of reversible MAO-A inhibitors in panic disorder |
| [7892341](https://pubmed.ncbi.nlm.nih.gov/7892341/) | 1995 | Case report | Psychiatrische Praxis | Case report: treatment-refractory panic disorder with agoraphobia responding to combined imipramine, moclobemide and behaviour therapy |

---

## Australia Market Information

Moclobemide currently has **no ARTG entries** and is **not marketed** in Australia (0 licences recorded).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
Supporting evidence consists of one placebo-controlled RCT and one active-comparator RCT, but both used panic disorder (with agoraphobia as a comorbid subgroup) as the primary endpoint rather than agoraphobia itself — a neighbouring-indication extrapolation, not direct disease-specific evidence. This is sufficient to justify a formal research question, but not yet sufficient to progress to a guardrailed proceed decision.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA) — currently a data gap (DG002)
- TGA-approved Product Information / warnings and contraindications — currently a data gap (DG001); note moclobemide is not currently registered on the ARTG
- An agoraphobia-specific trial or subgroup analysis with agoraphobia as the primary (not comorbid) endpoint
- Clarification of a viable Australian regulatory pathway, given the drug is not currently marketed here
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

