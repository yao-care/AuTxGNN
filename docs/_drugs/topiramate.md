---
layout: default
title: Topiramate
parent: High Evidence (L1-L2)
nav_order: 686
evidence_level: L2
indication_count: 10
---

# Topiramate
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Topiramate: From Epilepsy to Trigeminal Neuralgia

## One-Sentence Summary

> Topiramate is an established broad-spectrum antiseizure medication (ASM), with mechanistic and clinical literature in this Evidence Pack confirming efficacy across multiple seizure types (SANAD trial, multiple Cochrane reviews).
> Among ten TxGNN-predicted indications for this drug, the model's **highest-scoring** prediction ("trigeminal nerve neoplasm") is explicitly flagged by the underlying rationale as a likely knowledge-graph entity-confusion artefact with **no supporting evidence** and no antineoplastic mechanism — it should not be acted on.
> The best evidence-supported candidate is **Trigeminal Neuralgia**, supported by **1 completed Phase 2 RCT-context trial**, **1 dedicated placebo-controlled crossover RCT**, and **2 systematic reviews/meta-analyses** comparing topiramate to first-line carbamazepine.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the Evidence Pack (Taiwan/Australia regulatory license data absent). Literature in this pack confirms topiramate's established role in epilepsy (generalised and focal-onset seizures) and migraine prophylaxis |
| Predicted New Indication | Trigeminal Neuralgia |
| TxGNN Prediction Score | 98.92% (rank 10,866 of all drug-disease pairs) |
| Evidence Level | L2 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

**Note on candidate selection:** The Evidence Pack's #1-ranked prediction by raw TxGNN score ("trigeminal nerve neoplasm", 99.70%) is explicitly annotated in its own rationale as a probable knowledge-graph confusion between "trigeminal neoplasm" and "trigeminal neuralgia," with zero supporting trials or literature and no known antineoplastic mechanism for topiramate. It is scored **L5 / Hold** and is not carried forward in this report. Ranks 3–9 (various reflex/situational epilepsy subtypes — startle, orgasm-induced, eating, audiogenic, thinking, micturition-induced, and reading seizures) similarly lack subtype-specific human evidence (L3–L5, mostly "Hold") and are not detailed here; they may warrant future targeted literature review but are not decision-ready. Trigeminal Neuralgia (rank 10 by score, but the **strongest by evidence quality**) is used as the focus of this report.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (flagged as a Blocking/High-severity data gap). Based on the literature captured here, topiramate is a sulphamate-substituted antiseizure medication with multiple established mechanisms — voltage-gated Na⁺ channel blockade, GABA-A receptor potentiation, and AMPA/kainate glutamate receptor antagonism — consistent with its broad-spectrum efficacy across seizure types (confirmed in this pack via the SANAD RCT, PMID 17382828, and multiple Cochrane reviews on drug-resistant partial epilepsy).

Trigeminal neuralgia is a neuropathic pain syndrome driven by ephaptic (cross-talk) hyperexcitability and abnormal electrical discharge within the trigeminal nerve root — pathophysiologically analogous to epileptic hyperexcitability. Carbamazepine, the current first-line and only FDA-approved treatment for trigeminal neuralgia, acts primarily through the same voltage-gated Na⁺ channel blockade mechanism. This shared mechanistic basis is the core rationale for topiramate's plausibility as add-on or alternative therapy, particularly for patients who are carbamazepine-intolerant or refractory.

This mechanistic plausibility is corroborated by real clinical evidence: a dedicated placebo-controlled crossover pilot RCT (PMID 11307048) showed topiramate reduced pain by 31–64% in trigeminal neuralgia patients, and case series in both idiopathic and MS-associated symptomatic trigeminal neuralgia (PMID 11398791, 11094125, 17952282) report meaningful symptom remission. Two independent meta-analyses (PMID 21936587, 19471799) place topiramate alongside carbamazepine and oxcarbazepine as a recognised second-line pharmacological option.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00001725](https://clinicaltrials.gov/study/NCT00001725) | Phase 2 | Completed | 100 | Evaluated dextromethorphan and topiramate for orofacial pain, including trigeminal neuralgia, in adults with daily pain ≥3 months (Relevance grade A — direct match to indication) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11307048](https://pubmed.ncbi.nlm.nih.gov/11307048/) | 2001 | RCT | Clinical Neuropharmacology | Randomised, double-blind, placebo-controlled multi-crossover pilot study; topiramate reduced trigeminal neuralgia pain by 31–64% in 3 patients (p=0.04) |
| [21936587](https://pubmed.ncbi.nlm.nih.gov/21936587/) | 2011 | Review (meta-analysis) | CNS Drugs | Meta-analysis comparing topiramate vs carbamazepine for classical trigeminal neuralgia |
| [19471799](https://pubmed.ncbi.nlm.nih.gov/19471799/) | 2004 | Review (systematic review/meta-analysis) | Revista Brasileira de Anestesiologia | Systematic review/meta-analysis of pharmacological treatments for trigeminal neuralgia |
| [41718164](https://pubmed.ncbi.nlm.nih.gov/41718164/) | 2026 | Review (systematic review) | Medicines (Basel) | Class-oriented systematic review of anticonvulsant efficacy/safety in trigeminal neuralgia |
| [29114270](https://pubmed.ncbi.nlm.nih.gov/29114270/) | 2017 | Review | Asian Journal of Neurosurgery | Overview of trigeminal neuralgia pathophysiology and treatment |
| [19445753](https://pubmed.ncbi.nlm.nih.gov/19445753/) | 2009 | Review | BMJ Clinical Evidence | Clinical evidence summary on trigeminal neuralgia management |
| [25864062](https://pubmed.ncbi.nlm.nih.gov/25864062/) | 2015 | Review | Neurosciences (Riyadh) | Update on pharmacological and surgical options for trigeminal neuralgia |
| [17952282](https://pubmed.ncbi.nlm.nih.gov/17952282/) | 2007 | Case Series | Arquivos de Neuro-Psiquiatria | Low-dose topiramate (50–100mg/day) in 8 classical trigeminal neuralgia patients; 3 complete remission, 3 moderate improvement |
| [11398791](https://pubmed.ncbi.nlm.nih.gov/11398791/) | 2001 | Case Series | Journal of Pain and Symptom Management | Topiramate relieves idiopathic and symptomatic trigeminal neuralgia |
| [11094125](https://pubmed.ncbi.nlm.nih.gov/11094125/) | 2000 | Case Series | Neurology | Topiramate relieves refractory trigeminal neuralgia in MS patients |

---

## Australia Market Information

Topiramate is currently **not marketed** in Australia under this Evidence Pack's regulatory data (0 ARTG entries recorded). No product listings, dosage forms, or approved-indication text are available to summarise.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. This Evidence Pack's TFDA/local safety data (warnings, contraindications, drug-drug interactions) is recorded as a **Blocking data gap (DG001)** — it must be resolved before any Stage 1 (S1) safety pre-assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Trigeminal neuralgia is supported by a placebo-controlled RCT, two independent meta-analyses, and consistent case-series findings, with a mechanistically coherent rationale (shared Na⁺-channel blockade with first-line carbamazepine) — sufficient to justify further evaluation, but not yet sufficient for unguarded clinical adoption given the small RCT sample size (n=3) and topiramate's absence from current Australian market authorisation.

**To proceed, the following is needed:**
- TFDA/TGA Product Information (warnings, contraindications, DDI) to close Blocking data gap DG001 before any safety pre-assessment
- Confirmed mechanism of action documentation (currently a High-severity data gap, DG002)
- An Australian regulatory pathway assessment, since topiramate currently has 0 ARTG entries (not marketed)
- A larger, adequately powered RCT to confirm the effect size suggested by the 2001 pilot crossover study
- If pursued further, a separate targeted evidence review for the lower-confidence reflex/situational epilepsy candidates (ranks 2–9) before any action is taken on them
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

