---
layout: default
title: Trihexyphenidyl
parent: 僅模型預測 (L5)
nav_order: 703
evidence_level: L5
indication_count: 10
---

# Trihexyphenidyl
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

# Trihexyphenidyl: From Parkinsonism to Attention-Deficit/Hyperactivity Disorder

## One-Sentence Summary

Trihexyphenidyl is a classic anticholinergic (antimuscarinic) agent, traditionally used for Parkinson's disease and drug-induced extrapyramidal symptoms/dystonia. TxGNN's highest-ranked prediction proposes efficacy in **Attention-Deficit/Hyperactivity Disorder (ADHD)** with a **99.92%** model score, but it is supported by **no clinical trials** and only **one tangentially related case series**, and the evidence pack's own mechanistic review concludes there is no plausible pharmacological link — this appears to be a pure model-derived statistical signal rather than genuine repurposing evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented as structured data (drug is unregistered in Australia); per evidence-pack annotations, classified as an anticholinergic agent with conventional use in Parkinsonism / dystonia |
| Predicted New Indication | Attention-Deficit/Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on the evidence pack's own mechanistic annotations (drawn from the repurposing rationale for other ranked candidates), Trihexyphenidyl is understood to be a central anticholinergic/antimuscarinic agent, conventionally used for Parkinsonism and dystonia, acting by blocking cholinergic signalling to help rebalance the dopamine–acetylcholine ratio in the basal ganglia.

ADHD, by contrast, is conventionally managed by *enhancing* prefrontal dopaminergic and noradrenergic signalling (stimulants, atomoxetine). The evidence pack's own repurposing rationale for this candidate states explicitly that anticholinergic agents have no such action and could theoretically *impair* cognition, and that the single supporting literature record concerns tic disorder with persistent dystonia — not ADHD — most likely reflecting a keyword/entity-matching artefact rather than a genuine biological signal.

On this basis, we do not consider the ADHD prediction mechanistically reasonable. It should be treated as a knowledge-graph statistical association only, not as pharmacological evidence for repurposing.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21506147](https://pubmed.ncbi.nlm.nih.gov/21506147/) | 2011 | Case Series | Movement Disorders | Describes tic disorder with persistent dystonia; does not address ADHD — likely an off-topic literature match rather than direct supporting evidence |

## Australia Market Information

No ARTG entries were found in the evidence pack. Trihexyphenidyl currently has 0 registered licences and is not marketed in Australia.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Note: TFDA/product-level warnings, contraindications, and interaction data were not available in this evidence pack (Blocking gap, DG001) and must be obtained before any safety assessment can proceed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (ADHD) has no clinical trial support, only one topically unrelated case series, and the evidence pack's own mechanistic assessment concludes there is no plausible pharmacological link between an anticholinergic agent and a disorder requiring enhanced dopaminergic/noradrenergic signalling. Across all ten TxGNN predictions for this drug, nine are rated Hold/L5; only rank 5 (PLA2G6-associated neurodegeneration, L4, "Research Question") shows a mechanistically coherent overlap (parkinsonian/dystonic phenotype), though it too lacks any direct interventional evidence.

**To proceed, the following is needed:**
- TGA-approved Product Information / label warnings and contraindications (currently Blocking gap, DG001)
- Confirmed mechanism-of-action data from DrugBank or primary pharmacology sources (High-severity gap, DG002)
- If pursuing further research, prioritise rank 5 (PLA2G6-associated neurodegeneration) over the top-ranked ADHD signal, given its stronger mechanistic rationale
- An independent, targeted literature/trial search specific to Trihexyphenidyl and ADHD, to confirm whether the top TxGNN score reflects a genuine signal or a data/keyword artefact
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

