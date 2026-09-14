---
layout: default
title: Pseudoephedrine
parent: 僅模型預測 (L5)
nav_order: 569
evidence_level: L5
indication_count: 10
---

# Pseudoephedrine
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

# Pseudoephedrine: Nasal Cavity Disease Signal — Not a Novel Repurposing Candidate

## One-Sentence Summary

Pseudoephedrine is a sympathomimetic (α1-adrenergic agonist) medicine; this evidence pack does not contain a documented original indication (data gap), though the model's own supporting rationale identifies nasal decongestion as its established use. The TxGNN model's top-ranked association — **Nasal Cavity Disease** — scored **99.75%**, but the evidence pack's own analysis flags this as a rediscovery of pseudoephedrine's known clinical use rather than a genuine repurposing signal, with **19 clinical trials** and **7 publications** returned, none conclusively confirmatory. A more distinct candidate (**Bronchial Disease**, rank 10) carries the pipeline's only "Research Question" stage with real human RCT support, but is also accompanied by a serious cardiovascular safety signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in this evidence pack (`original_indications` empty — data gap). The model's rationale text independently states nasal congestion/decongestion is pseudoephedrine's established core use. |
| Predicted New Indication | Nasal Cavity Disease *(see caveat below — likely not a true new signal)* |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L1 as tagged by the pipeline; on manual re-check against the stated L1–L5 rule this does **not** hold — no completed Phase 3 RCT was found for this drug–disease pair. Realistic level: **L4** (mixed Phase 1/2 + preclinical/comparative literature). |
| Australia Market Status | Not marketed *(figure sourced from Taiwan TFDA regulatory data in this evidence pack — no direct TGA/ARTG lookup was performed; see Market Information section)* |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data is marked as a data gap in this evidence pack (DG002, High severity). However, the model's own rationale text describes pseudoephedrine as an **α1-adrenergic receptor agonist** that causes direct nasal mucosal vasoconstriction, reducing turbinate engorgement — a textbook decongestant mechanism. This is consistent across the literature returned (e.g. PMID 11345158, comparing the topical/oral decongestant effects of d-pseudoephedrine and phenylpropanolamine).

The critical issue is that "Nasal Cavity Disease" is not a *new* indication relative to that mechanism — it is the condition pseudoephedrine is already used to treat. The evidence pack's own repurposing rationale states this explicitly: nasal congestion/nasal cavity disease is pseudoephedrine's original core indication, so a high TxGNN score here reflects the model re-identifying a known drug–disease pair rather than surfacing a novel hypothesis. Treating this as a genuine repurposing candidate risks contaminating downstream prioritisation.

For context, a more mechanistically distinct signal in this evidence pack is **Bronchial Disease** (rank 10, evidence level L2, decision stage S1 — "Research Question"), supported by human RCTs combining pseudoephedrine with antihistamines in allergic rhinitis with concomitant asthma (PMID 17042147, PMID 9438487) and an older crossover study showing modest bronchodilator activity via β-adrenergic effects (PMID 7140799). This is pharmacologically distinct enough to be a more legitimate — though still early-stage — repurposing direction, and it carries an important safety flag (see below).

---

## Clinical Trial Evidence
*(for the top-ranked indication: Nasal Cavity Disease)*

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00804687](https://clinicaltrials.gov/study/NCT00804687) | Phase 2 | Completed | 53 | Randomised, single-dose, double-dummy, placebo-controlled 3-way crossover comparing JNJ-39220675, pseudoephedrine, and placebo in allergic rhinitis (environmental exposure chamber model) — the only trial in this set that explicitly names pseudoephedrine as a study arm. |
| [NCT00562120](https://clinicaltrials.gov/study/NCT00562120) | Phase 2 | Completed | 21 | Double-blind, double-dummy, placebo-controlled 4-way crossover testing an H3-receptor antagonist against nasal-allergen-induced congestion; design typical of decongestant comparator trials, but the study drug identity for the comparator arm is not confirmed from the truncated title. |
| [NCT00517946](https://clinicaltrials.gov/study/NCT00517946) | N/A | Completed | 21 | MRI-based methodology study assessing anti-allergy drug effects on nasal/sinus mucosal anatomy after intranasal allergen challenge; may involve a decongestant comparator but the agent is not confirmed. |

The remaining 16 registered trials returned for this indication (e.g. balloon sinuplasty, probiotic sinusitis therapy, nasal endoscopy anaesthesia technique, medical-device seawater sprays) were assessed as low relevance — they test surgical, device, or unrelated pharmacological interventions, not pseudoephedrine's adrenergic mechanism. Full list available in the underlying evidence pack.

---

## Literature Evidence
*(for the top-ranked indication: Nasal Cavity Disease)*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11345158](https://pubmed.ncbi.nlm.nih.gov/11345158/) | 2001 | Comparative Clinical Study | American Journal of Rhinology | Direct comparison of oral and topical decongestant effects of phenylpropanolamine and d-pseudoephedrine using acoustic rhinometry — establishes pseudoephedrine's decongestant activity, not a new indication. |
| [22794679](https://pubmed.ncbi.nlm.nih.gov/22794679/) | 2012 | Review | Allergy and Asthma Proceedings | Overview of non-allergic rhinitis subtypes and management, providing background context rather than direct pseudoephedrine efficacy data. |
| [19769798](https://pubmed.ncbi.nlm.nih.gov/19769798/) | 2009 | Preclinical (Animal Model) | American Journal of Rhinology & Allergy | Feline model of nasal congestion; evaluated D-pseudoephedrine decongestant action with/without desloratadine. |
| [12387934](https://pubmed.ncbi.nlm.nih.gov/12387934/) | 2002 | Preclinical (Animal Model) | Journal of Pharmacological and Toxicological Methods | Canine model developed to characterise nasal decongestant drug mechanisms generally; not pseudoephedrine-specific. |
| [12962193](https://pubmed.ncbi.nlm.nih.gov/12962193/) | 2003 | Preclinical (Animal Model) | American Journal of Rhinology | Ragweed-sensitised dog model of allergic nasal congestion using acoustic rhinometry methodology. |
| [24492651](https://pubmed.ncbi.nlm.nih.gov/24492651/) | 2014 | Preclinical (Animal Model) | Journal of Pharmacology and Experimental Therapeutics | Evaluates selective α2c-adrenergic agonists (not pseudoephedrine) in nasal congestion models — included as a mechanistic comparator only. |
| [11895194](https://pubmed.ncbi.nlm.nih.gov/11895194/) | 2002 | Preclinical (Animal Model) | American Journal of Rhinology | Establishes acoustic rhinometry as a large-animal model for nasal congestion research. |

None of these constitute a completed Phase 3 RCT or systematic review specifically testing pseudoephedrine for a genuinely new indication — the strongest item (PMID 11345158) confirms known decongestant pharmacology rather than a novel disease association.

---

## Australia Market Information

No product licence entries are present in this evidence pack (0 records). **Note:** the regulatory fields supplied (`taiwan_regulatory`) originate from Taiwan's TFDA licensing data, not a direct Australian TGA/ARTG search — the "not marketed" status above should be treated as unverified for Australia until an ARTG lookup is completed (see Data Gaps below).

---

## Safety Considerations

The structured safety block for this evidence pack is empty (`key_warnings`, `contraindications` both marked as data gaps; DDI query returned no results). Per the escalation rule for this drug, TFDA label warnings/contraindications are a **Blocking** data gap (DG001) — this prevents even an initial (S1) safety screen from being completed.

Please refer to the TGA-approved Product Information (PI) for authoritative safety information.

Separately, literature surfaced elsewhere in this evidence pack (attached to other ranked indications, not the structured safety fields) raises signals worth flagging to prescribers pending formal PI review:
- **Cardiovascular**: a case report of acute myocardial infarction from coronary vasospasm associated with pseudoephedrine combined with metoprolol (PMID 28347584).
- **Neurological**: a case report of posterior reversible encephalopathy syndrome (PRES) linked to a pseudoephedrine-containing cold medicine (PMID 20398975).
- **Reproductive/developmental**: an older report associating sympathomimetic drug use (including pseudoephedrine-containing combinations) in pregnancy with limb malformations (PMID 10839324).

These are individual case reports, not controlled evidence, but they reinforce why DG001 (missing TFDA warnings/contraindications) should be resolved before any repurposing pathway proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked TxGNN association (Nasal Cavity Disease, 99.75%) is not a genuine repurposing signal — the evidence pack's own analysis identifies it as a rediscovery of pseudoephedrine's known decongestant use, and no completed Phase 3 RCT evidence supports treating it otherwise.
- A Blocking data gap (DG001 — TFDA label warnings/contraindications) prevents even an initial safety screen (S1), and a High-severity gap (DG002 — formal MOA documentation) limits mechanistic-relevance analysis.

**To proceed, the following is needed:**
- Resolve DG001: obtain and parse the TFDA product label for warnings/contraindications (Blocking).
- Resolve DG002: confirm mechanism-of-action documentation via DrugBank API (High priority).
- Confirm actual Australian TGA/ARTG registration status directly, rather than relying on Taiwan TFDA data as a proxy.
- If a genuine repurposing direction is still of interest, prioritise re-review of rank 10 (Bronchial Disease, L2/S1, "Research Question") over rank 1 — but only alongside dedicated cardiovascular risk assessment, given the coronary vasospasm signal identified in its supporting literature.
- Remove or re-flag "Nasal Cavity Disease" in the candidate list as a known-indication match rather than a novel prediction, to avoid distorting downstream prioritisation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

