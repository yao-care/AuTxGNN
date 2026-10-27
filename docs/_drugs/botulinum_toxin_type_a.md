---
layout: default
title: Botulinum Toxin Type A
parent: Model Prediction Only (L5)
nav_order: 104
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Botulinum Toxin Type A: predicted new indication Primary hereditary glaucoma . Best-supported: parkinsonian disorder (evidence level L5). Approved use: Not available in the data compiled for this rep…"
monitor_inn: "Botulinum toxin type A"
predicted_indications: ["primary hereditary glaucoma", "parkinsonian disorder", "open-angle glaucoma", "insomnia (disease)", "glaucoma 1, open angle", "restless legs syndrome", "Parkinson disease", "paralysis agitans, juvenile, of Hunt", "bronchitis", "autosomal recessive Parkinson disease"]
---

# Botulinum Toxin Type A
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Botulinum Toxin Type A: From an Unspecified Original Indication to Parkinsonian Disorder
{: .text-alpha }

## One-Sentence Summary

Botulinum toxin type A is a neuromuscular-blocking agent marketed in Australia as Botox, but the approved indication text was not available in the data compiled for this report.
The TxGNN model's top-ranked prediction is **primary hereditary glaucoma**, which has no supporting evidence. The best-supported prediction is **parkinsonian disorder** (rank 2), with **6 clinical trials** (one completed Phase 3) and **11 publications** retrieved.
For Parkinson's-related use, the evidence supports symptom-specific benefit (for example, sialorrhea), not disease modification.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Primary hereditary glaucoma (rank 1, no supporting evidence). Best-supported: parkinsonian disorder (rank 2) |
| TxGNN Prediction Score | 89.37% (primary hereditary glaucoma); 88.84% (parkinsonian disorder) |
| Evidence Level | L5 (primary hereditary glaucoma); L1 (parkinsonian disorder) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold for the top-ranked glaucoma prediction. Proceed with Guardrails for symptom-specific Parkinson's indications (see Conclusion) |

The top-ranked prediction has only a model score behind it. The remainder of this report therefore focuses on parkinsonian disorder (rank 2), the highest-ranked prediction with substantive evidence.

---

## Why is This Prediction Reasonable?

**Primary hereditary glaucoma (rank 1).** Botulinum toxin A blocks presynaptic acetylcholine release at neuromuscular and autonomic junctions. This has no established link to trabecular outflow resistance or intraocular pressure regulation. There are no trials or publications, so the prediction is a model output only. Open-angle glaucoma (ranks 3 and 5) is in the same position.

**Parkinsonian disorder (rank 2).** Currently, detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, botulinum toxin A causes localised chemodenervation, reducing cholinergic transmission in target tissues. It does not treat the underlying neurodegeneration. Its plausible benefit lies in specific symptoms:

- Sialorrhea (reduced salivary gland cholinergic drive)
- Dystonic muscles (foot dystonia, camptocormia)
- Tremor-generating muscles

The Phase 3 trial NCT02091739 is the most relevant study. Its title describes "chronic troublesome sialorrhea in various neurological conditions", so its direct applicability to Parkinson's disease should be confirmed. The sialorrhea literature (2001 to 2015) is consistent with this direction.

Other predictions are weak: bronchitis (rank 9) appears to be a spurious match, and insomnia (rank 4) rests on a comorbidity association in blepharospasm rather than treatment evidence. Restless legs syndrome (rank 6) has a plausible but speculative mechanism (reduced muscle afferent input) and limited, low-quality evidence.

---

## Clinical Trial Evidence

Trials for parkinsonian disorder:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02091739](https://clinicaltrials.gov/study/NCT02091739) | Phase 3 | Completed | 184 | Randomised, double-blind, placebo-controlled study of NT 201 (75 U or 100 U) for chronic troublesome sialorrhea in neurological conditions. Results not provided in the data compiled |
| [NCT04277247](https://clinicaltrials.gov/study/NCT04277247) | Phase 2/3 | Unknown | 40 | Randomised, double-blind, placebo-controlled study of foot dystonia-associated pain in Parkinson's disease |
| [NCT02668497](https://clinicaltrials.gov/study/NCT02668497) | Phase 2 | Unknown | 50 | Kinematic-guided injection for upper-limb Parkinson's tremor |
| [NCT06094309](https://clinicaltrials.gov/study/NCT06094309) | Not applicable | Unknown | 20 | Randomised pilot study for freezing of gait |
| [NCT00477802](https://clinicaltrials.gov/study/NCT00477802) | Phase 4 | Terminated | 8 | Cervical injections for levodopa-induced dyskinesia; underpowered |
| [NCT03069911](https://clinicaltrials.gov/study/NCT03069911) | Phase 1 | Terminated | 3 | Depression in Parkinson's disease; uninformative |

No ANZCTR identifiers were found in the data compiled. Trials for glaucoma, insomnia, restless legs syndrome and the other predictions: currently no related clinical trials registered (the one trial linked to bronchitis concerned back muscle function and is not relevant).

---

## Literature Evidence

Selected publications for Parkinson's disease and parkinsonian disorders:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16440332](https://pubmed.ncbi.nlm.nih.gov/16440332/) | 2006 | RCT | Movement Disorders | Double-blind, placebo-controlled study (32 patients, 50 U Botox per parotid gland); reduced drooling frequency and associated disability |
| [29334040](https://pubmed.ncbi.nlm.nih.gov/29334040/) | 2018 | RCT (crossover) | Can J Neurol Sci | Botulinum toxin A versus placebo for limb pain in advanced Parkinson's disease |
| [16995596](https://pubmed.ncbi.nlm.nih.gov/16995596/) | 2006 | Clinical study | Acta Neurol Taiwan | Botulinum toxin A to reduce saliva in parkinsonian patients with moderate to severe sialorrhea |
| [21791351](https://pubmed.ncbi.nlm.nih.gov/21791351/) | 2011 | Clinical study | J Urol | 100 U intradetrusor injection in Parkinson's disease with refractory detrusor overactivity; 6-month follow-up |
| [34017433](https://pubmed.ncbi.nlm.nih.gov/34017433/) | 2021 | Clinical study | Am J Transl Res | Effects on mood and cognition in Parkinson's disease with depression |
| [26566459](https://pubmed.ncbi.nlm.nih.gov/26566459/) | 2015 | Open-label study | Tremor Other Hyperkinet Mov | Sensor-guided incobotulinumtoxinA injections for upper-limb Parkinson's tremor over 38 weeks |
| [28837826](https://pubmed.ncbi.nlm.nih.gov/28837826/) | 2018 | Review | Toxicon | Review noting a high level of evidence for sialorrhea in parkinsonism |
| [41745739](https://pubmed.ncbi.nlm.nih.gov/41745739/) | 2026 | Cohort study | Toxins | Botulinum toxin injections for drooling also improved dysphagia in 20 Parkinson's patients |
| [34828584](https://pubmed.ncbi.nlm.nih.gov/34828584/) | 2021 | Systematic review and meta-analysis | Healthcare (Basel) | Botulinum toxin A in restless legs syndrome (a separate prediction); evidence limited and low quality |
| [39559314](https://pubmed.ncbi.nlm.nih.gov/39559314/) | 2024 | Observational | Int J Ophthalmol | Link between blepharospasm and anxiety, depression and sleep disorder; does not show treatment of insomnia |

Some retrieved Parkinson's-related results concern other conditions (cervical dystonia, head tremor, spasticity) and are indirect. Glaucoma predictions: currently no related literature available.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10993N | Botox | Lyophilised powder for injection, 100 units | Not available in the data compiled |

The product is registered as a valid single-ingredient injectable.

---

## Safety Considerations

**Drug Interactions** (41 interactions identified, mainly from DDInter):

- **Major:** aminoglycosides and related agents (kanamycin, neomycin, streptomycin) and polymyxin B. These may potentiate neuromuscular blockade.
- **Moderate:** anticholinergics (atropine, clidinium, dicyclomine, glycopyrronium, hyoscyamine, mepenzolate, methscopolamine, propantheline, scopolamine, trospium) and sedating antihistamines (promethazine, acrivastine, azatadine, brompheniramine, carbinoxamine, chlorcyclizine).

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications, which were not available in the data compiled.

---

## Conclusion and Next Steps

**Decision: Hold** for the top-ranked prediction (primary hereditary glaucoma) and the other L5 predictions. **Proceed with Guardrails** only for symptom-specific Parkinson's indications, framed as a research question.

**Rationale:**
- The top-ranked prediction has no mechanistic rationale and no trials or literature, so the score is a model output only.
- Parkinsonian disorder has L1-level evidence (a completed Phase 3 RCT), but benefit is symptomatic and localised, not disease-modifying. The Phase 3 trial's indication needs confirmation.
- The data gaps on package-insert warnings and mechanism of action limit safety screening.

**To proceed, the following is needed:**
- The TGA Product Information for Botox, to establish approved indications, warnings and contraindications
- Confirmation of the indication and results of NCT02091739
- Focus on specific symptom indications (sialorrhea, tremor, dystonic pain, overactive bladder) rather than Parkinson's disease broadly
- Detailed mechanism of action data
- Review of the restless legs syndrome meta-analysis conclusions if that indication is pursued
- Check of ANZCTR for Australian trials
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

