---
layout: default
title: Atropine
parent: Model Prediction Only (L5)
nav_order: 70
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Atropine: predicted new indication Migraine disorder (evidence level L5). Approved use: Not available in the data compiled for this report"
---

# Atropine
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

# Atropine: From Unspecified Original Indication to Migraine Disorder

## One-Sentence Summary

Atropine is a long-established muscarinic (anticholinergic) drug marketed in Australia as an injection, but the data compiled for this report do not record an approved indication text.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are **0 clinical trials** and only preclinical or indirect literature supporting this direction.
The evidence is essentially a model prediction, so the recommendation is to hold.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the ARTG entry has no indication text) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L4 (preclinical and mechanistic studies only) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Atropine is a well-known non-selective muscarinic receptor antagonist, and this class effect is the basis for the mechanistic reasoning below.

Preclinical work suggests a cholinergic contribution to migraine biology. Studies in rodents describe parasympathetic-driven neurogenic inflammation in the meninges (involving meningeal mast cells and the trigeminal ganglia) and plasma protein extravasation in the dura mater after parasympathetic stimulation. A mouse study also found that cholinergic modulation affects cortical spreading depression, the process underlying migraine aura. Blocking muscarinic receptors could therefore plausibly modulate these pathways.

The link is indirect. The retrieved literature is mostly animal, pharmacology or adverse-event reports. The direction of effect for an antagonist is unclear, and no human efficacy data were identified. The very high TxGNN score is a prediction only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for migraine disorder.

For context, two completed trials exist in a related condition, post-dural puncture headache (a secondary headache, not migraine). Both use a neostigmine/atropine mixture as the comparator, so atropine's own effect cannot be isolated:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03997006](https://clinicaltrials.gov/study/NCT03997006) | Phase 4 | Completed | 60 | IV aminophylline vs IV neostigmine/atropine for post-dural puncture headache |
| [NCT04910477](https://clinicaltrials.gov/study/NCT04910477) | Phase 3 | Completed | 90 | Nebulised dexmedetomidine vs neostigmine/atropine vs saline placebo for post-dural puncture headache after caesarean section |

---

## Literature Evidence

No human efficacy studies of atropine in migraine were identified. The most relevant items are mechanistic or indirect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17186568](https://pubmed.ncbi.nlm.nih.gov/17186568/) | 2007 | Review | J Appl Toxicol | Pharmacology of anisodamine, an atropine derivative and non-specific cholinergic antagonist |
| [36485173](https://pubmed.ncbi.nlm.nih.gov/36485173/) | 2024 | Preclinical | Eur J Neurosci | Meningeal mast cell and cholinergic mechanisms in neurogenic inflammation in a rat migraine model |
| [9344563](https://pubmed.ncbi.nlm.nih.gov/9344563/) | 1997 | Preclinical | Exp Neurol | Parasympathetic ganglion stimulation induces dural plasma extravasation in rats |
| [8930196](https://pubmed.ncbi.nlm.nih.gov/8930196/) | 1996 | Preclinical | J Pharmacol Exp Ther | Central cholinergic system involved in sumatriptan-induced antinociception in rodents |
| [2943405](https://pubmed.ncbi.nlm.nih.gov/2943405/) | 1986 | Case series | Cephalalgia | Systemic atropine reduced attack-related sweating, tearing and nasal secretion in chronic paroxysmal hemicrania |
| [40590589](https://pubmed.ncbi.nlm.nih.gov/40590589/) | 2024 | Case report | Pain Med Case Rep | Botulinum treatment-induced dropped head syndrome in chronic migraine (not about atropine) |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1089H | Atropine Injection (Bridgewest) | Injection containing atropine sulfate monohydrate 600 micrograms in 1 mL | Not recorded in the data compiled |

---

## Safety Considerations

- **Drug Interactions**: An interaction screen returned 100 interacting drugs. Most of those listed are rated Moderate, with a few Minor. Examples include:
  - Other anticholinergics and antimuscarinics (aclidinium, hyoscyamine, amitriptyline, chlorpheniramine, acrivastine, phenyltoloxamine, amantadine): additive anticholinergic effects
  - Opioids (fentanyl, alfentanil, codeine, dihydrocodeine, tramadol), ethanol and botulinum toxin type A
  - Acetylcholine and galantamine (opposing cholinergic action), loperamide, acebutolol
  - Minor: acetaminophen, hydrochlorothiazide
- **Other signals from the literature**: Atropine can raise intraocular pressure or precipitate angle closure, so caution is needed in glaucoma. One case report describes reversible cerebral vasoconstriction syndrome after neostigmine plus atropine given for post-dural puncture headache.

Warnings and contraindications from the Product Information were not available. Please refer to the TGA-approved Product Information (PI) for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The migraine prediction rests on indirect preclinical and mechanistic evidence. There are no clinical trials and no human efficacy data, and the high TxGNN score is a prediction only. The direction of effect for a muscarinic antagonist in migraine is also unclear.

**Other predicted indications reviewed:**
- **Headache disorder (L2, research question)**: the only clinical trials involve neostigmine/atropine as a comparator in post-dural puncture headache, so atropine's own effect is not isolated. There is also a safety signal (reversible cerebral vasoconstriction syndrome).
- **Trigeminal autonomic cephalalgia**: only a 1984 case series and preclinical work.
- **Open-angle glaucoma and primary hereditary glaucoma**: no evidence of benefit, and atropine is potentially harmful because of the risk of raised intraocular pressure.
- **Migraine with brainstem aura**: a single mouse study.
- **Migraine with or without aura, susceptibility to**: a genetic susceptibility entity rather than a treatable indication.
- **Atrophoderma vermiculata, ulerythema ophryogenesis and nephrogenic syndrome of inappropriate antidiuresis**: no supporting literature or trials.

**To proceed, the following is needed:**
- The TGA Product Information (approved indications, warnings and contraindications), which was a blocking data gap
- Mechanism of action data (for example from DrugBank)
- Human proof-of-concept data, such as a small controlled study of an atropine-containing regimen in migraine, with a clear rationale for the direction of effect
- A route and formulation assessment, as only an injectable form is registered in Australia
- A safety plan for anticholinergic interactions and for patients with glaucoma risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

