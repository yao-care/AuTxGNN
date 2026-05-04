---
layout: default
title: Baclofen
parent: 僅模型預測 (L5)
nav_order: 74
evidence_level: L5
indication_count: 10
---

# Baclofen
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

# Baclofen: From Spasticity to Attention Deficit-Hyperactivity Disorder

> **Multi-Indication Assessment** | Candidate ID: TW-DB00181-multi | Data Cutoff: 5 April 2026

---

## One-Sentence Summary

Baclofen is a GABA-B receptor agonist used internationally as a centrally-acting muscle relaxant and antispasticity agent; it is not currently registered on the Australian Register of Therapeutic Goods (ARTG) based on available data. The TxGNN model predicts potential utility across 10 indications, with **Attention Deficit-Hyperactivity Disorder (ADHD)** ranking highest (99.32%), supported by **10 publications but no registered clinical trials**. Notably, the second-ranked prediction — **Nicotine Dependence** — carries substantially stronger clinical evidence (one completed Phase 2 RCT and 20 publications) and represents the most actionable candidate from this assessment.

---

## Quick Overview

*Based on Rank 1 prediction: Attention Deficit-Hyperactivity Disorder*

| Item | Content |
|------|---------|
| Original Indication | Spasticity and muscle spasms associated with neurological conditions (e.g., multiple sclerosis, spinal cord injury, stroke) |
| Predicted New Indication (Rank 1) | Attention Deficit-Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L4 — Preclinical studies and indirect literature only |
| Australia Market Status | Not registered (0 ARTG entries — independent TGA verification strongly recommended) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Summary of All Predicted Indications

| Rank | Indication | TxGNN Score | Evidence Level | Trials | Publications | Recommendation |
|------|-----------|------------|---------------|--------|-------------|---------------|
| 1 | Attention Deficit-Hyperactivity Disorder | 99.32% | L4 | 0 | 10 | Hold |
| 2 | **Nicotine Dependence** | 99.19% | **L2** | **3** | **20** | **Proceed with Guardrails** |
| 3 | ADHD — Inattentive Type | 98.89% | L5 | 0 | 0 | Hold |
| 4 | Myofascial Pain Syndrome | 98.87% | L3 | 1* | 4 | Research Question |
| 5 | Faciodigitogenital Syndrome (Aarskog-Scott) | 98.78% | L5 | 0 | 0 | Hold |
| 6 | Trigeminal Nerve Neoplasm | 98.70% | L5 | 0 | 2† | Hold |
| 7 | Methemoglobinemia | 98.33% | L5 | 0 | 1† | Hold |
| 8 | Chondromyxoid Fibroma | 98.15% | L5 | 0 | 0 | Hold |
| 9 | Methemoglobinemia — Alpha Type | 97.97% | L5 | 0 | 0 | Hold |
| 10 | Specific Developmental Disorder | 97.95% | L4 | 2† | 2 | Research Question |

> \* Trial status unverified (UNKNOWN). † Retrieved literature has limited or no direct relevance to the mapped indication — likely reflects knowledge graph retrieval artefacts.
>
> ⚠️ **Clinical Note:** Ranks 5–9 (faciodigitogenital syndrome, trigeminal nerve neoplasm, both methemoglobinemia variants, chondromyxoid fibroma) have no clinically plausible mechanistic connection to Baclofen's GABA-B pharmacology. These predictions are not recommended for further investigation.

---

## Why is This Prediction Reasonable?

### Baclofen's Mechanism of Action

Baclofen acts as a selective GABA-B receptor agonist at both pre- and post-synaptic sites throughout the central nervous system. By activating these receptors — particularly in the spinal cord, limbic system, and prefrontal cortex — it inhibits neuronal excitability, reduces spastic muscle tone, and modulates the release of monoamine neurotransmitters including dopamine and noradrenaline. It is this indirect monoaminergic influence that underpins several of the higher-ranked predictions.

### Rank 1: ADHD — Why the Prediction Is Plausible but Weak

GABA-B receptor activation in the prefrontal cortex (PFC) theoretically modulates attention and impulse control circuits. The most directly relevant preclinical evidence (PMID 21300040) examined EEG responses to GABA agonists in the spontaneously hypertensive rat (SHR) — a well-validated ADHD animal model — demonstrating that baclofen alters cortical and hippocampal electrophysiological patterns in ADHD-relevant circuits.

However, the mechanistic pathway is largely **orthogonal to first-line ADHD pharmacotherapy**. Methylphenidate and amphetamines act via dopamine transporter (DAT) inhibition; atomoxetine via noradrenaline reuptake blockade; guanfacine via postsynaptic α2A-adrenergic stimulation. Baclofen's GABA-B mechanism does not directly address the dopamine/noradrenaline dysregulation central to ADHD pathophysiology. The bulk of supporting literature relates to Tourette syndrome — a frequently comorbid condition — where baclofen has been explored for tic suppression, not ADHD itself. The high TxGNN score most likely reflects knowledge graph proximity through shared comorbidity nodes (Tourette syndrome, ASD) rather than a direct pharmacological relationship.

### Rank 2: Nicotine Dependence — Why the Prediction Is Strong

The mechanistic case here is well-defined. Baclofen activates GABA-B receptors in the mesolimbic reward pathway — specifically inhibiting the ventral tegmental area (VTA) → nucleus accumbens (NAc) dopamine projection that mediates nicotine's rewarding and reinforcing effects. This directly attenuates cue-induced craving, nicotine-seeking behaviour, and withdrawal manifestations. Multiple animal studies confirm baclofen suppresses nicotine-induced conditioned place preference and prevents reinstatement of extinguished nicotine-seeking. The GABAergic hypothesis has been formally tested in a completed Phase 2 clinical trial. Regulatory precedent from baclofen's approved use in alcohol use disorder (France) further strengthens biological plausibility across addiction indications.

### Rank 4: Myofascial Pain Syndrome — Why the Prediction Is Intuitive

This is perhaps the most pharmacologically natural extension for baclofen. Spinal GABA-B receptor agonism directly inhibits both monosynaptic and polysynaptic reflexes, interrupting the "pain → muscle spasm → pain" cycle that drives myofascial pain syndrome. A Russian clinical observational study (PMID 18577932) directly documents baclofen (sold as "baclosan") in the complex therapy of muscle-tonic and myofascial pain syndromes, providing real-world clinical data supporting this prediction.

---

## Clinical Trial Evidence

### Rank 1 — ADHD

No clinical trials for Baclofen in ADHD are currently registered in ClinicalTrials.gov or ICTRP.

---

### Rank 2 — Nicotine Dependence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01821560](https://clinicaltrials.gov/study/NCT01821560) | Phase 2 | Completed | 44 | Perfusion fMRI study evaluating baclofen's effects on brain activity and behavioural responses to smoking cues in cigarette smokers; directly assessed dopaminergic pathway modulation — primary clinical evidence for this indication |
| [NCT00257894](https://clinicaltrials.gov/study/NCT00257894) | Phase 2 | Terminated | 41 | Assessed baclofen's effects on smoking urge, withdrawal symptoms, and reinforcement in moderate-to-heavy smokers; terminated but 41 participants enrolled prior to closure |
| [NCT01228994](https://clinicaltrials.gov/study/NCT01228994) | Phase 2 | Terminated | 6 | Randomised double-blind placebo-controlled trial formally testing the GABAergic hypothesis in nicotine-dependent smokers; terminated due to severe enrolment shortfall (n=6 of target); design sound but feasibility barriers identified |

---

### Rank 4 — Myofascial Pain Syndrome

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05617118](https://clinicaltrials.gov/study/NCT05617118) | N/A | Unknown | 52 | Prospective multicentre cohort study comparing oral baclofen (60 days) versus botulinum toxin A injections in myofascial pelvic pain syndrome — direct comparative design; trial status requires independent verification |

---

## Literature Evidence

### Rank 1 — ADHD

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21300040](https://pubmed.ncbi.nlm.nih.gov/21300040/) | 2011 | Animal Study | Brain Research | EEG responses to GABA and DA agonists in spontaneously hypertensive (SHR/ADHD model) vs. kainate-treated rats — most direct baclofen-ADHD preclinical link |
| [35345730](https://pubmed.ncbi.nlm.nih.gov/35345730/) | 2022 | Systematic Review | Cureus | Efficacy of behavioural, antipsychotic, and alpha-agonist treatments for Tourette syndrome tics; ADHD comorbidity discussed as clinical context |
| [26366961](https://pubmed.ncbi.nlm.nih.gov/26366961/) | 2015 | Review | Clinical Neuropharmacology | Mood stabilisers in children/adolescents with ASD; attention-deficit symptoms in neurodevelopmental context relevant to ADHD comorbidity |
| [11393328](https://pubmed.ncbi.nlm.nih.gov/11393328/) | 2001 | Review | Paediatric Drugs | Tourette syndrome management — baclofen mentioned as adjunct option for tic suppression alongside clonidine |
| [24295630](https://pubmed.ncbi.nlm.nih.gov/24295630/) | 2013 | Review | Int Review of Neurobiology | Emerging Tourette syndrome treatments; ADHD as major comorbidity; emerging pharmacological options |
| [10342599](https://pubmed.ncbi.nlm.nih.gov/10342599/) | 1999 | Review | J Child Neurology | 450-patient clinical series using baclofen and botulinum toxin A for tic/Tourette syndrome; most direct baclofen clinical use data in this population |
| [24062084](https://pubmed.ncbi.nlm.nih.gov/24062084/) | 2014 | Animal Study | Psychopharmacology | Guanfacine (α2A agonist) reduces impulsive decision-making via ventral hippocampus — comparator context demonstrating alternative ADHD pharmacological pathways |
| [30122296](https://pubmed.ncbi.nlm.nih.gov/30122296/) | 2019 | Clinical Review | L'Encephale | Supervised off-label methylphenidate prescribing in adult ADHD — regulatory and prescribing context relevant to off-label use considerations |

---

### Rank 2 — Nicotine Dependence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24553576](https://pubmed.ncbi.nlm.nih.gov/24553576/) | 2014 | Animal Study | Psychopharmacology | Baclofen attenuates nicotine rewarding properties and withdrawal manifestations in rodents — core behavioural pharmacology evidence |
| [19250803](https://pubmed.ncbi.nlm.nih.gov/19250803/) | 2009 | Animal Study | Eur Neuropsychopharmacology | Baclofen prevents drug-induced reinstatement of nicotine-seeking and conditioned place preference in rats — relapse prevention mechanism established |
| [18682277](https://pubmed.ncbi.nlm.nih.gov/18682277/) | 2008 | Animal Study | Neuroscience Letters | Baclofen selectively reduces nicotine conditioned place preference and discriminative stimulus effects; high-dose (3 mg/kg) effect confirmed |
| [23500668](https://pubmed.ncbi.nlm.nih.gov/23500668/) | 2013 | Animal Study | Prog Neuropsychopharmacol Biol Psychiatry | Baclofen prevents mecamylamine-precipitated nicotine withdrawal syndrome; α4β2 nAChR receptor density changes characterised |
| [25868070](https://pubmed.ncbi.nlm.nih.gov/25868070/) | 2015 | Conference Abstract | Neuropsychopharmacology | Double-blind placebo-controlled RCT of baclofen for concurrent alcohol and nicotine dependence — dual addiction application |
| [38555115](https://pubmed.ncbi.nlm.nih.gov/38555115/) | 2024 | Narrative Review | Int Review of Neurobiology | Drug repurposing for alcohol use disorder; baclofen listed as approved AUD medication with broader substance dependence applicability |
| [29250815](https://pubmed.ncbi.nlm.nih.gov/29250815/) | 2018 | Review | Pharmacotherapy | Current and emerging pharmacotherapies for smoking cessation; baclofen reviewed as an investigational GABA-B agent |
| [24971600](https://pubmed.ncbi.nlm.nih.gov/24971600/) | 2015 | Review | Neuropharmacology | GABA-B receptors as therapeutic targets in substance use disorders; positive allosteric modulator potential summarised |

---

### Rank 4 — Myofascial Pain Syndrome

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18577932](https://pubmed.ncbi.nlm.nih.gov/18577932/) | 2008 | Clinical Observational | Zh Nevrol Psikhiatr | Baclofen (baclosan) in complex therapy for muscle-tonic and myofascial pain syndromes in dorsopathy patients (n=20); pain reduction demonstrated versus control group — most directly relevant publication |
| [32342054](https://pubmed.ncbi.nlm.nih.gov/32342054/) | 2019 | RCT | Frontiers in Dentistry | LLLT and TENS as adjuncts to pharmaceutical therapy for myofascial pain dysfunction syndrome — trial context and comparator pharmacotherapy landscape |

---

## Australia Market Information

Based on the data available for this report, Baclofen does not have any current entries in the Australian Register of Therapeutic Goods (ARTG): **0 licences returned**.

> ⚠️ **Data Quality Alert:** This result is unexpected given Baclofen's widespread international availability as a prescription muscle relaxant. Healthcare professionals should independently verify current TGA registration status at **[www.tga.gov.au](https://www.tga.gov.au)** before making any access or prescribing decisions. The zero-entry result may reflect a data retrieval limitation rather than the true ARTG status.

---

## Safety Considerations

No product-specific safety data (TGA-approved warnings, contraindications, or drug interaction data) were available in this Evidence Pack. Please refer to the **TGA-approved Product Information (PI)** for Baclofen for complete and current safety information.

**Class-level safety considerations for GABA-B agonists (for general guidance):**

- **CNS Depression:** Sedation, dizziness, and muscle weakness are commonly reported — exercise caution in patients who drive or operate machinery
- **Withdrawal Seizures:** Abrupt discontinuation can precipitate seizures and hallucinations — dose tapering is essential
- **Renal Impairment:** Baclofen is primarily renally excreted; dose reduction is required in renal insufficiency
- **Falls Risk in Older Patients:** Combined muscle relaxation and sedation substantially increases falls risk — prescribe with caution in elderly populations
- **Respiratory Depression Risk:** Particularly relevant in nicotine or polysubstance-dependent populations where concurrent CNS depressant use may be present
- **Intrathecal vs. Oral Dosing:** Intrathecal baclofen carries specific risks distinct from oral formulations — ensure formulation and route are appropriate for any proposed use

---

## Conclusion and Next Steps

### Overall Recommendation: Prioritise Nicotine Dependence for Further Investigation

While ADHD ranks first in TxGNN scoring, **Nicotine Dependence (Rank 2) is the most clinically actionable prediction** in this multi-indication assessment, with meaningful clinical trial data and a well-characterised mechanistic basis.

---

**Decision for ADHD (Rank 1): Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.32%), evidence for baclofen in ADHD is limited to animal studies and reviews in overlapping conditions — predominantly Tourette syndrome. The GABA-B pathway does not align with established ADHD pharmacological targets, and no clinical trials have been registered in this indication.

**To proceed, the following would be needed:**
- At minimum one exploratory clinical trial (Phase 1/2) specifically in ADHD-diagnosed populations
- Mechanistic studies demonstrating GABA-B modulation of prefrontal dopamine/noradrenaline circuits in humans with ADHD
- Clear definition of the target population and ADHD subtype (given Rank 3, the inattentive subtype, carries even less supporting evidence)
- Consultation with a psychiatrist specialising in ADHD before any clinical study design

---

**Decision for Nicotine Dependence (Rank 2): Proceed with Guardrails**

**Rationale:**
One completed Phase 2 RCT (NCT01821560, n=44) provides direct human clinical evidence. The mechanistic basis — mesolimbic GABA-B modulation attenuating nicotine reward — is well-characterised and biologically coherent. International regulatory precedent exists (baclofen approved for alcohol use disorder in France). Two terminated trials signal feasibility challenges that must be prospectively addressed.

**To proceed, the following is needed:**
- Obtain and review published results from NCT01821560
- Formal analysis of termination reasons for NCT00257894 and NCT01228994 to inform future trial design
- A well-powered, pragmatic Phase 2/3 RCT incorporating lessons from prior feasibility barriers
- Assessment of combinatorial use with existing cessation pharmacotherapy (e.g., varenicline, NRT)
- Independent TGA ARTG verification and regulatory pathway consultation for Australian use
- Full drug interaction profile relevant to smoking cessation populations (including nicotine replacement and psychotropic co-medications)

---

**Decision for Myofascial Pain Syndrome (Rank 4): Research Question**

**Rationale:**
The mechanistic case is straightforward and pharmacologically intuitive (central muscle relaxation). Direct clinical observational evidence exists (PMID 18577932) and a prospective comparative trial (NCT05617118) has been registered. However, trial status is unverified, and evidence quality remains insufficient for clinical use without further validation.

**To proceed, the following is needed:**
- Verify the current status of NCT05617118 and access interim or final results
- Conduct a systematic review of baclofen specifically in myofascial/muscle-tonic pain conditions
- Consider liaison with pain medicine specialists given overlapping use of baclofen in established musculoskeletal practice

---

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application in patient care. Results from TxGNN represent computational predictions and must be interpreted alongside clinical expertise and regulatory guidance. Australian healthcare professionals should consult current TGA Product Information and relevant clinical guidelines for all prescribing decisions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

