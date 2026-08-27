---
layout: default
title: Paroxetine
parent: 僅模型預測 (L5)
nav_order: 511
evidence_level: L5
indication_count: 10
---

# Paroxetine
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

# Paroxetine: From Major Depressive Disorder to Melancholia

## One-Sentence Summary

> Paroxetine is an established selective serotonin reuptake inhibitor (SSRI) used for depressive and anxiety-spectrum disorders.
> The TxGNN model's top-ranked signal (Ohdo syndrome, a rare genetic disorder) is very likely a knowledge-graph artefact with no plausible mechanistic basis.
> The most clinically credible signal in this evidence pack is **Melancholia**, supported by **1 completed clinical trial** and **20 publications** (including multiple RCTs), though this largely reflects recognition of paroxetine's known antidepressant activity rather than a genuinely novel indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally on record — no ARTG licence text available (drug not marketed in Australia). Established use is Major Depressive Disorder / depressive-spectrum disorders, per the drug's known SSRI classification cited throughout the literature evidence. |
| Predicted New Indication | Melancholia |
| TxGNN Prediction Score | 98.74% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

**Note on the top-ranked TxGNN signal:** The model's #1-scoring prediction (Ohdo syndrome and variants, 99.11%) — along with two related entries (blepharophimosis–intellectual disability syndrome, Ohdo type; benign paroxysmal torticollis of infancy) — has zero supporting trials or literature and no plausible mechanistic link (these are rare paediatric genetic/developmental disorders). The evidence pack itself flags these as probable embedding artefacts, possibly driven by lexical similarity between "paroxetine" and "paroxysmal," or proximity to intellectual-disability/psychiatric nodes in the knowledge graph. This report focuses on Melancholia (rank 2), the highest-ranked prediction with real supporting evidence.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (marked as a data gap). Based on known information from the supporting literature, paroxetine is a selective serotonin reuptake inhibitor (SSRI) — a phenylpiperidine compound that potently and selectively inhibits presynaptic serotonin reuptake with minimal affinity for adrenergic, dopaminergic, histaminergic, or cholinergic receptors.

Melancholia is a historically recognised subtype of severe major depressive disorder (DSM-III melancholic features). The repurposing rationale in this evidence pack states plainly that the SSRI mechanism is "the standard pharmacological basis for major depressive disorder including the melancholic subtype... an extension of an existing approved indication, not a novel repurposing hypothesis." In other words, this prediction is best understood as TxGNN correctly recognising paroxetine's core antidepressant activity rather than surfacing an unexpected new use. The clinical value of this evidence pack lies less in "discovering" melancholia as a target and more in confirming that the TxGNN signal, when it aligns with well-characterised pharmacology, tracks real evidence — which is useful context for judging the plausibility of the other, evidence-free predictions in the same output (e.g., Ohdo syndrome).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01916824](https://clinicaltrials.gov/study/NCT01916824) | Phase 4 | Completed | 53 | Compared decision-making styles and computerised task performance between unmedicated major depressive disorder patients and healthy controls; relevant to melancholic depression populations but not a direct paroxetine efficacy trial (relevance grade B). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1487627](https://pubmed.ncbi.nlm.nih.gov/1487627/) | 1992 | RCT | International Clinical Psychopharmacology | Meta-analysis of 178 paroxetine- vs 66 placebo-treated patients with DSM-III melancholia; paroxetine significantly superior to placebo with a clear dose–response relationship. |
| [8517168](https://pubmed.ncbi.nlm.nih.gov/8517168/) | 1993 | RCT | Acta Psychiatrica Scandinavica | Pooled double-blind, parallel-group trial (paroxetine n=167 vs placebo n=169); paroxetine significantly superior on major efficacy variables from week 2, well tolerated. |
| [10836286](https://pubmed.ncbi.nlm.nih.gov/10836286/) | 2000 | RCT | International Clinical Psychopharmacology | 24-week double-blind RCT comparing venlafaxine and paroxetine in major depression/dysthymia outpatients. |
| [11354239](https://pubmed.ncbi.nlm.nih.gov/11354239/) | 2001 | Meta-analysis | International Clinical Psychopharmacology | Meta-analysis of 39 RCTs (paroxetine n=1924 vs TCAs n=1834); comparable efficacy to TCAs including clomipramine, with better tolerability. |
| [8106649](https://pubmed.ncbi.nlm.nih.gov/8106649/) | 1993 | Review | Journal of Clinical Psychopharmacology | Overview of efficacy and safety of paroxetine as a novel SSRI for depression; favourable pharmacokinetic profile (once-daily dosing, no active metabolites). |
| [1464219](https://pubmed.ncbi.nlm.nih.gov/1464219/) | 1992 | Review | Clinical Pharmacy | Comparative review of paroxetine, sertraline, and fluvoxamine covering pharmacology, adverse effects, DDIs, and dosing. |
| [15089103](https://pubmed.ncbi.nlm.nih.gov/15089103/) | 2004 | Review | CNS Drugs | Review of controlled-release paroxetine formulation; consistently superior to placebo across major depressive disorder, social anxiety disorder, and PMDD trials. |
| [1431015](https://pubmed.ncbi.nlm.nih.gov/1431015/) | 1992 | Review | International Clinical Psychopharmacology | Dosage, tolerability, and safety overview; 20 mg/day identified as optimal dose, fewer anticholinergic effects than TCAs. |
| [1531828](https://pubmed.ncbi.nlm.nih.gov/1531828/) | 1992 | Review | The Journal of Clinical Psychiatry | Safety review of 6,705 paroxetine-treated patients; no significant cardiovascular effects, few significant drug interactions. |
| [8784663](https://pubmed.ncbi.nlm.nih.gov/8784663/) | 1996 | Case Report | Journal of Clinical Psychopharmacology | Case report of tardive dyskinesia associated with paroxetine use. |

---

## Australia Market Information

Paroxetine has **no ARTG entries** on record in this evidence pack — the drug is currently listed as not marketed in Australia (0 licences). No product name, dosage form, or approved-indication text is available to tabulate.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. This evidence pack contains no populated warnings, contraindications, or drug interaction data (DDI query returned no results).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Melancholia is supported by L1-level evidence (multiple RCTs plus a completed Phase 4 trial) and a coherent, well-established SSRI mechanism — but it substantially overlaps with paroxetine's already-known use in major depressive disorder rather than representing a novel repurposing target. Combined with the absence of any Australian market presence or local safety data, guardrails are warranted before any clinical application.

**To proceed, the following is needed:**
- Formal mechanism of action (MOA) documentation from DrugBank or TGA PI
- TGA-approved Product Information for warnings, contraindications, and drug interactions
- Confirmation of ARTG registration status or an import/access pathway, since the drug is not currently marketed in Australia
- Contemporary (post-2010) clinical evidence specific to the melancholic subtype, since most supporting trials/literature date from the 1990s–2000s
- A clarified evidence framing distinguishing "existing indication confirmation" (melancholia) from "novel repurposing hypothesis," since this candidate does not meet the latter bar
- Disregard rank 1, 3, and 5 predictions (Ohdo syndrome and variants, blepharophimosis-ID syndrome Ohdo type, benign paroxysmal torticollis of infancy) as likely model artefacts unless independent mechanistic or clinical evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

