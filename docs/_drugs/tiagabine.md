---
layout: default
title: Tiagabine
parent: Moderate Evidence (L3-L4)
nav_order: 673
evidence_level: L4
indication_count: 10
---

# Tiagabine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

Using no additional skill — this is a direct document-generation task fully specified by the prompt template; proceeding directly.

# Tiagabine: From Partial Seizures to Visual Epilepsy

## One-Sentence Summary

> Tiagabine is a GABA reuptake inhibitor (GAT-1) that has been used as an add-on antiepileptic drug for partial (focal) seizures.
> The TxGNN model predicts it may be effective for **Visual Epilepsy**,
> with **1 clinical trial** and **20 publications** currently associated with this prediction — though several of these describe tiagabine-induced visual field defects rather than treatment efficacy, and the drug is not currently marketed in Australia.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Partial (focal) seizures — adjunctive antiepileptic therapy (derived from published literature; no Australian regulatory record exists) |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.25% |
| Evidence Level | L4 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data is not available in DrugBank for this evidence pack. Based on the supporting literature, tiagabine is a nipecotic-acid derivative that selectively inhibits the GAT-1 GABA transporter, blocking presynaptic and glial reuptake of GABA and thereby increasing extracellular GABA concentrations in the brain (PMID 9097364, 15094857, 8595791). This GABAergic-enhancing mechanism underlies its established efficacy as add-on therapy for partial/complex partial seizures (PMID 9443711).

Visual epilepsy is a form of reflex epilepsy in which seizures are triggered by visual stimuli. Mechanistically, broad-spectrum GABAergic potentiation could theoretically raise cortical seizure threshold in reflex epilepsy subtypes, which is the basis for the TxGNN association. However, a critical caveat must be flagged: the most directly "visual"-related citation in this evidence pack, PMID 12588906 ("Vigabatrin, tiagabine, and visual fields"), actually reports **visual field constriction as an adverse effect** of GABAergic antiepileptic drugs (a class effect well documented for vigabatrin, with tiagabine less clearly implicated) — it is *not* evidence that tiagabine treats visually-induced seizures. This represents a directionality mismatch that must be resolved before this indication is taken seriously as a treatment hypothesis, rather than a drug-induced visual toxicity signal being mistaken for therapeutic relevance.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Phase 4 | Completed | 111 | Observational study of tiagabine and other newer AEDs (gabapentin, lamotrigine, levetiracetam, oxcarbazepine, pregabalin, topiramate) as first-choice bitherapy for focal epilepsy in routine clinical practice; not designed to evaluate visually-triggered (reflex) epilepsy specifically — relevance graded C. |

No Australian (ANZCTR) trials were identified for this indication.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | Guideline | Neurology | AAN/AES practice guideline on efficacy/tolerability of newer AEDs (including tiagabine) for new-onset epilepsy; general, not reflex-epilepsy specific. |
| [22592677](https://pubmed.ncbi.nlm.nih.gov/22592677/) | 2012 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Assesses tiagabine as add-on therapy for drug-resistant partial epilepsy; supports general anticonvulsant efficacy, not visual-triggered seizures specifically. |
| [17560495](https://pubmed.ncbi.nlm.nih.gov/17560495/) | 2007 | Review | Pediatric Neurology | Reviews visual adverse effects of AEDs (visual field and colour vision deficits); relevant to safety of GABAergic drugs on vision, not to treating visual epilepsy. |
| [12588906](https://pubmed.ncbi.nlm.nih.gov/12588906/) | 2003 | Cohort/Safety | J Neurol Neurosurg Psychiatry | Reports vigabatrin/tiagabine-associated visual field defects — an **adverse effect**, directly contradicting a simple "treats visual epilepsy" interpretation. |
| [32120063](https://pubmed.ncbi.nlm.nih.gov/32120063/) | 2020 | Review | Neuropharmacology | Comprehensive review of mechanisms of currently used antiseizure drugs, including GABA transporter inhibition by tiagabine. |
| [11520315](https://pubmed.ncbi.nlm.nih.gov/11520315/) | 2001 | Review | Epilepsia | Reviews GABAergic mechanisms underlying seizure generation and control, supporting the theoretical basis for GABA-enhancing drugs in epilepsy broadly. |
| [9097364](https://pubmed.ncbi.nlm.nih.gov/9097364/) | 1997 | Review | Seminars Pediatr Neurol | Reviews tiagabine pharmacokinetics, efficacy (partial seizures) and safety in adults, adolescents and preliminary paediatric data. |
| [15094857](https://pubmed.ncbi.nlm.nih.gov/15094857/) | 1998 | Review | Drugs of Today | Reviews tiagabine's unique GABA-uptake-inhibition mechanism and efficacy in animal seizure models. |
| [19445769](https://pubmed.ncbi.nlm.nih.gov/19445769/) | 2009 | Clinical Evidence Review | BMJ Clin Evid | General epilepsy treatment evidence overview; not specific to reflex or visual epilepsy. |
| [25825412](https://pubmed.ncbi.nlm.nih.gov/25825412/) | 2016 | Retrospective/Toxicology Review | Hum Exp Toxicol | Reviews tiagabine toxicity/overdose trends reported to US poison centres 2000–2012, including FDA warnings on seizure risk in non-epileptic patients. |

## Australia Market Information

Tiagabine is **not currently marketed in Australia** and has **no ARTG entries** in this evidence pack (`market_status: Not marketed`, `total_licenses: 0`). No product listing table can be generated.

## Safety Considerations

No structured safety data (key warnings, contraindications, or drug interactions) is available in this evidence pack — this is flagged as a **blocking data gap (DG001)** that prevents progression to a formal S1 safety pre-assessment. Because tiagabine is not marketed in Australia, there is no TGA-approved Product Information to reference. Overseas approved labelling (e.g. US Gabitril PI) and the safety literature identified above — which documents a known risk of tiagabine-induced non-convulsive status epilepticus and visual field defects — should be used as interim safety references until local regulatory data can be obtained.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The lead prediction (visual epilepsy) rests on L4 (mechanistic/preclinical-level) evidence with no trial or literature directly evaluating tiagabine's efficacy in visually-triggered seizures, and the single most topically relevant citation (PMID 12588906) actually documents a tiagabine-related adverse visual effect rather than therapeutic benefit — a directionality conflict that must be resolved. Combined with the blocking absence of safety/warning data (DG001) and the drug's non-marketed status in Australia (0 ARTG entries), the evidence does not support proceeding at this time.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA/overseas approved Product Information (warnings, contraindications, DDI) to complete S1 safety pre-assessment
- Resolve DG002: confirm mechanism of action via DrugBank API query
- Clarify and correct the evidence-direction issue around PMID 12588906 (adverse effect vs. treatment) before this indication advances further
- Seek specialist neurology input on the feasibility and safety of trialling tiagabine in reflex (visual) epilepsy, given the documented risk of tiagabine-induced non-convulsive status epilepticus in related indications (see rank 9, status epilepticus, in the source evidence pack)
- Assess pathway/rationale for potential Australian market entry, given current absence of ARTG registration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

