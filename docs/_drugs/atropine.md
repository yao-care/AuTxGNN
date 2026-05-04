---
layout: default
title: Atropine
parent: 僅模型預測 (L5)
nav_order: 65
evidence_level: L5
indication_count: 10
---

# Atropine
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

# Atropine: From Anticholinergic Agent to Migraine Disorder

## One-Sentence Summary

Atropine is a classical antimuscarinic agent widely used in clinical medicine for bradycardia management, organophosphate poisoning, and as a preanesthetic agent — though it holds no current TGA registration in Australia.
The TxGNN model assigns it a 99.56% prediction confidence for **Migraine Disorder**, supported by **0 clinical trials** and **13 publications** that are predominantly animal studies and mechanistic research exploring the parasympathetic pathway in migraine pathophysiology.
No human clinical trials have been conducted on atropine specifically for migraine to date, and all supporting evidence currently remains at the preclinical level.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Australia (no ARTG approval) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L4 — Preclinical / Mechanistic Studies |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Although DrugBank MOA data was not retrieved for this report (data gap DG002), atropine's mechanism of action is extensively characterised in the biomedical literature. It is a competitive, non-selective antagonist of muscarinic acetylcholine receptors (M1–M5), acting principally on M2 and M3 subtypes to suppress parasympathetic effector responses — reducing glandular secretion, relaxing smooth muscle, and modulating vascular tone. These properties form the pharmacological basis of the migraine prediction.

Migraine pathophysiology centres on activation of the trigeminoparasympathetic reflex arc via the sphenopalatine ganglion (SPG), which drives dural vasodilation, plasma protein extravasation, and CGRP release — collectively producing the neurogenic inflammation associated with migraine pain. PMID 9344563 (1997) directly demonstrated that parasympathetic SPG stimulation in rats induces dural plasma protein extravasation, the hallmark of neurogenic inflammation. More recently, PMID 36485173 (2024, *European Journal of Neuroscience*) investigated muscarinic antagonism — atropine's core mechanism — in a nitroglycerin-induced rat migraine model, specifically examining the meningeal mast cell–cholinergic axis as a driver of neurogenic inflammation. PMID 8930196 showed that central cholinergic transmission is required for sumatriptan's antinociceptive effects in rodents, directly linking the cholinergic system to migraine pain modulation. PMID 15882801 further demonstrated that CGRP–nicotinic receptor interactions regulate centrally evoked facial blood flow, relevant to migraine triggers.

The most clinically notable observation comes from PMID 2943405 (1986, *Cephalalgia*): systemic atropine administration markedly reduced autonomic symptoms — sweating, lacrimation, and nasal secretion — during attacks of chronic paroxysmal hemicrania (a trigeminal autonomic cephalalgia closely related to cluster headache). This represents the only human-level observation in this evidence set directly associating atropine with relief of headache-associated autonomic features. While biologically plausible, the overall evidence base for migraine has not progressed beyond preclinical and mechanistic research, and the TxGNN model's high-confidence prediction likely reflects the strength of the underlying biological network connectivity between muscarinic blockade and migraine pathology rather than established clinical utility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for migraine disorder.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [36485173](https://pubmed.ncbi.nlm.nih.gov/36485173/) | 2024 | Mechanistic Study | European Journal of Neuroscience | Muscarinic antagonism in nitroglycerin-induced rat migraine model; meningeal mast cell–cholinergic axis shown to modulate neurogenic inflammation — most direct mechanistic support for atropine's predicted role |
| [9344563](https://pubmed.ncbi.nlm.nih.gov/9344563/) | 1997 | Animal Study | Experimental Neurology | Parasympathetic SPG stimulation directly induces dural plasma protein extravasation in rats; establishes parasympathetic neurogenic inflammation as a therapeutically targetable mechanism |
| [8930196](https://pubmed.ncbi.nlm.nih.gov/8930196/) | 1996 | Animal Study | J Pharmacol Exp Ther | Central cholinergic system (ACh pathway) shown to mediate sumatriptan antinociception in rodents; atropine used to confirm muscarinic pathway dependency |
| [2943405](https://pubmed.ncbi.nlm.nih.gov/2943405/) | 1986 | Clinical Observation | Cephalalgia | Systemic atropine markedly reduced sweating, lacrimation, and nasal secretion during chronic paroxysmal hemicrania attacks — the only human-level evidence of atropine relieving headache-associated autonomic features |
| [15882801](https://pubmed.ncbi.nlm.nih.gov/15882801/) | 2005 | Animal Study | Neuroscience Letters | CGRP and nicotinic receptors shown to regulate centrally evoked facial blood flow; mechanistic relevance to CGRP-mediated vascular changes in migraine |
| [10193781](https://pubmed.ncbi.nlm.nih.gov/10193781/) | 1999 | Animal Study | British J Pharmacology | Atropine used as pharmacological tool in guinea-pig basilar artery model; characterises nicotinic-mediated vascular relaxation in a migraine-relevant intracranial vessel |
| [17186568](https://pubmed.ncbi.nlm.nih.gov/17186568/) | 2007 | Pharmacology Review | J Applied Toxicology | Review of anisodamine, a naturally occurring atropine derivative; characterises class-level pharmacological properties and differential CNS toxicity profile compared with atropine and scopolamine |
| [1786517](https://pubmed.ncbi.nlm.nih.gov/1786517/) | 1991 | Animal Study | British J Pharmacology | Ergotamine and DHE characterised as 5-HT1C agonists in piglet choroid plexus; mechanistic context for receptor-level pharmacology in established antimigraine agents |
| [21252](https://pubmed.ncbi.nlm.nih.gov/21252/) | 1977 | Mechanistic Study | J Pharmacy and Pharmacology | Early investigation of beta-phenethylamine as a migraine trigger; establishes historical mechanistic framework for autonomic contributions to migraine |
| [40590589](https://pubmed.ncbi.nlm.nih.gov/40590589/) | 2024 | Case Report | Pain Medicine Case Reports | Botulinum toxin (anticholinergic mechanism class) used for chronic migraine; provides treatment context for autonomic-targeting pharmacotherapy in migraine management |

---

## Australia Market Information

Atropine (DrugBank ID: DB00572) is **not currently registered on the Australian Register of Therapeutic Goods (ARTG)** and has no approved product listings in Australia.

While atropine is used clinically in Australian healthcare — including in hospital formularies for acute bradycardia, organophosphate poisoning (typically alongside pralidoxime), ophthalmic mydriasis/cycloplegia, and as a preanesthetic agent — these clinical uses typically operate via hospital formulary pathways, TGA Special Access Scheme (SAS) provisions, or supply as an unlisted hospital medicine rather than through formal ARTG product registration with approved indications.

Any proposed off-label or repurposing use would require engagement with the TGA Special Access Scheme Category B or C, or relevant hospital pharmacy governance and ethics review processes, before clinical administration.

---

## Safety Considerations

Detailed safety information including TGA-approved contraindications, key prescribing warnings, and drug interaction data was not available in this Evidence Pack. Please refer to the relevant Product Information (PI), the **Australian Medicines Handbook (AMH)**, or **eTG Complete** for comprehensive safety guidance.

The following signals are noted from available literature and this Evidence Pack's predicted indications:

- **Glaucoma contraindication**: Atropine causes mydriasis and cycloplegia, increasing the risk of acute angle-closure glaucoma. It is contraindicated in narrow-angle glaucoma. Two predicted indications from this Evidence Pack — open-angle glaucoma (rank 5) and primary hereditary glaucoma (rank 6) — carry explicit safety flags and are **not recommended for further development**.
- **Reversible Cerebral Vasoconstriction Syndrome (RCVS)**: PMID 37802666 (2023, *British J Anaesthesia*) documents a case of RCVS following neostigmine/atropine administration for post-dural puncture headache — a directly relevant safety signal for any neurological indication.
- **Cardiovascular effects**: Tachycardia and arrhythmia risk are expected class effects; relevant at all doses and particularly important in perioperative or neurological applications.
- **CNS anticholinergic effects**: Confusion, agitation, and hallucinations — greater risk in elderly patients and at supratherapeutic doses; relevant to central nervous system indications including migraine.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's 99.56% prediction confidence for migraine disorder is mechanistically coherent — the role of the cranial parasympathetic system (SPG activation, CGRP release, dural neurogenic inflammation) provides clear biological plausibility for muscarinic blockade as a therapeutic strategy. However, all current supporting evidence remains preclinical or mechanistic (Evidence Level L4), with zero human clinical trials of atropine in migraine. Combined with the absence of Australian market registration, a Hold decision is appropriate for this indication until translational evidence is generated.

---

**High-Priority Secondary Signal — Headache Disorder / Post-Dural Puncture Headache (PDPH):**

A more immediately actionable signal was identified for the related indication of **headache disorder** (TxGNN rank 8, score 97.24%, Evidence Level L2). Neostigmine combined with Atropine has been studied in Phase 3 RCTs for post-dural puncture headache (PDPH) — a specific and clinically significant headache subtype. Key trials include:

| Trial | Phase | Status | n | Key Findings |
|-------|-------|--------|---|--------------|
| [NCT04910477](https://clinicaltrials.gov/study/NCT04910477) | Phase 3 | Completed | 90 | Nebulised Dexmedetomidine vs Neostigmine/Atropine for PDPH post-caesarean section — completed head-to-head comparison |
| [NCT03997006](https://clinicaltrials.gov/study/NCT03997006) | Phase 4 | Completed | 60 | IV Aminophylline vs IV Neostigmine/Atropine for PDPH treatment |
| [NCT06729047](https://clinicaltrials.gov/study/NCT06729047) | Phase 1/2 | Not yet recruiting | 330 | Prophylactic IV Neostigmine+Atropine vs Ketorolac for PDPH prevention — large planned sample |
| [NCT06824025](https://clinicaltrials.gov/study/NCT06824025) | Early Phase 1 | Not yet recruiting | 111 | Nebulised Neostigmine/Atropine vs Lignocaine for acute PDPH |

This signal is further supported by published RCTs: PMID [30169405](https://pubmed.ncbi.nlm.nih.gov/30169405/) (*Anesthesia & Analgesia*, 2018) and PMID [36651373](https://pubmed.ncbi.nlm.nih.gov/36651373/) (*Minerva Anestesiologica*, 2023). A dedicated report on **Headache Disorder / PDPH** is recommended and would likely result in a **Proceed with Guardrails** recommendation.

---

**To proceed on migraine disorder, the following is needed:**

- Formal MOA data retrieval from DrugBank API (resolving data gap DG002)
- A systematic review or scoping review of muscarinic antagonism in migraine and trigeminal autonomic cephalalgias
- A dedicated preclinical study testing atropine as a therapeutic candidate (not merely as a pharmacological tool) in a validated migraine animal model, with translatable endpoints
- Safety and tolerability profiling at neurologically relevant dosing ranges, with attention to the RCVS signal
- TGA Special Access Scheme or hospital pharmacy governance consultation before any clinical administration is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

