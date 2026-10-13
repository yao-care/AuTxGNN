---
layout: default
title: Modafinil
parent: High Evidence (L1-L2)
nav_order: 485
evidence_level: L1
indication_count: 10
---

# Modafinil
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Modafinil: From Narcolepsy to Hypersomnia (Idiopathic and Related Central Disorders)

## One-Sentence Summary

Modafinil is a wake-promoting agent originally used to treat narcolepsy and excessive daytime sleepiness.
The TxGNN model predicts it may be effective for **hypersomnia (disease)**, the highest-ranked prediction with meaningful clinical support (the top-scoring prediction, insomnia, is not mechanistically plausible; see below),
with **14 clinical trials** and **20 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Narcolepsy (the approved indication text was not available in the Australian ARTG data compiled for this report) |
| Predicted New Indication | Hypersomnia (disease). Note: the rank 1 TxGNN prediction is insomnia, which is not supported (see below) |
| TxGNN Prediction Score | 96.53% (hypersomnia); insomnia ranked first at 99.85% |
| Evidence Level | L1 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on the literature reviewed, modafinil promotes wakefulness through dopamine transporter inhibition and effects on histaminergic, orexinergic and glutamatergic circuits. It is already established for excessive sleepiness in narcolepsy.

Hypersomnia (the central disorders of hypersomnolence, including idiopathic hypersomnia and narcolepsy type 2) shares excessive daytime sleepiness as its core symptom with narcolepsy. Guideline-level sources (AASM 2021 and the European narcolepsy guideline) support modafinil use in this group. Evidence is strongest for narcolepsy and weaker for idiopathic hypersomnia, where it relies on a comparative trial against amphetamine and expert opinion. Extension beyond narcolepsy should be treated as off-label use with monitoring.

**Other predictions in context:**
- **Insomnia (rank 1, 99.85%)**: Not plausible. Modafinil is a wake-promoting agent, so its action runs opposite to insomnia treatment. The high score is likely a network artefact of the sleep-disorder neighbourhood. The two registered trials are uninformative (one terminated with 2 participants, one without insomnia as its target).
- **ADHD (rank 3, 98.27%)**: Phase 2 and 3 randomised trials and a meta-analysis (PMID 27810669) suggest some efficacy, and the mechanism overlaps with ADHD stimulants. However, it was not approved for ADHD, and reviews place it behind first-line agents. Cardiovascular and dermatological safety in children needs clarification.
- **Circadian rhythm sleep disorder (rank 9)**: Supported mainly by reviews for symptomatic management of shift work sleepiness. Modafinil does not correct circadian misalignment.
- **Trichotillomania (rank 4)**: Only a small acute-dose cognition study (L3).
- **Narcolepsy, susceptibility to (rank 7)**: Largely duplicates the existing indication.
- **Faciodigitogenital syndrome, peroxisomal oxidation disorder, ACBD5 deficiency, Tourette syndrome**: No evidence (L5). Hold. For Tourette syndrome, dopamine reuptake inhibition could plausibly worsen tics.

## Clinical Trial Evidence

Trials for hypersomnia (up to 10 most relevant shown):

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00107796](https://clinicaltrials.gov/study/NCT00107796) | Phase 3 | Completed | 140 | Randomised, double-blind, placebo-controlled study of modafinil (100, 200, 400 mg/day) in children and adolescents with narcolepsy-related sleepiness |
| [NCT00107809](https://clinicaltrials.gov/study/NCT00107809) | Phase 3 | Completed | 140 | Placebo-controlled study of modafinil in children and adolescents with sleepiness from obstructive sleep apnoea/hypopnoea syndrome |
| [NCT00107848](https://clinicaltrials.gov/study/NCT00107848) | Phase 3 | Completed | 280 | 1-year open-label extension assessing long-term safety and effectiveness in children and adolescents |
| [NCT00214968](https://clinicaltrials.gov/study/NCT00214968) | Phase 3 | Completed | 92 | 6-month open-label safety and effectiveness study in children and adolescents |
| [NCT03772314](https://clinicaltrials.gov/study/NCT03772314) | Phase 2 | Completed | 44 | Pragmatic trial of modafinil versus amphetamines in central disorders of hypersomnolence |
| [NCT00174174](https://clinicaltrials.gov/study/NCT00174174) | Not specified | Completed | 30 | Placebo-controlled, double-blind crossover study in narcolepsy |
| [NCT00916253](https://clinicaltrials.gov/study/NCT00916253) | Not applicable | Completed | 27 | Driving ability assessment in patients with wakefulness disorders on modafinil |
| [NCT01080807](https://clinicaltrials.gov/study/NCT01080807) | Phase 4 | Completed | 385 | Armodafinil (R-enantiomer) versus placebo in shift work disorder sleepiness; supportive only |
| [NCT01766323](https://clinicaltrials.gov/study/NCT01766323) | Phase 3 | Unknown | 200 | Modafinil for sleepiness in patients on oral morphine for pain palliation; indirectly related |
| [NCT00393562](https://clinicaltrials.gov/study/NCT00393562) | Not specified | Withdrawn | 0 | Modafinil versus methylphenidate for sleepiness in Parkinson's disease; no participants enrolled |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34743789](https://pubmed.ncbi.nlm.nih.gov/34743789/) | 2021 | Guideline | J Clin Sleep Med | AASM clinical practice guideline on treatment of central disorders of hypersomnolence |
| [34743790](https://pubmed.ncbi.nlm.nih.gov/34743790/) | 2021 | Systematic review | J Clin Sleep Med | AASM systematic review, meta-analysis and GRADE assessment supporting the guideline |
| [34173695](https://pubmed.ncbi.nlm.nih.gov/34173695/) | 2021 | Guideline | Eur J Neurol | European guideline on management of narcolepsy in adults and children |
| [39306601](https://pubmed.ncbi.nlm.nih.gov/39306601/) | 2024 | Randomised trial | CNS Drugs | Blinded non-inferiority trial of modafinil versus amphetamine-dextroamphetamine in idiopathic hypersomnia and narcolepsy type 2 |
| [36921459](https://pubmed.ncbi.nlm.nih.gov/36921459/) | 2023 | Review | Sleep Med Rev | Update on idiopathic hypersomnia treatment; management largely expert-consensus based |
| [32901432](https://pubmed.ncbi.nlm.nih.gov/32901432/) | 2021 | Review | Neurotherapeutics | Treatment of idiopathic hypersomnia and other hypersomnia syndromes |
| [26599679](https://pubmed.ncbi.nlm.nih.gov/26599679/) | 2016 | Review | Sleep Med Rev | Overview of idiopathic hypersomnia |
| [27549768](https://pubmed.ncbi.nlm.nih.gov/27549768/) | 2016 | Review | Curr Treat Options Neurol | Management of narcolepsy types 1 and 2 |
| [32386693](https://pubmed.ncbi.nlm.nih.gov/32386693/) | 2020 | Review | Sleep Med Clin | Pharmacologic management of excessive daytime sleepiness, including modafinil and armodafinil |
| [10481909](https://pubmed.ncbi.nlm.nih.gov/10481909/) | 1999 | Preclinical | Cell | Orexin knockout mice show a narcolepsy-like phenotype |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 8816B | Modafin | Tablet 100 mg (oral) | Not available in the data compiled |

## Safety Considerations

No label-derived warnings or contraindications were available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for safety information.

**Contraindication signals from the knowledge graph (not label text):** hypertension, liver failure, anxiety disorders, psychotic and other mental disorders, substance abuse/dependence, acute coronary syndrome, myocardial infarction, myocardial ischaemia, coronary artery disease, mitral valve prolapse and postural orthostatic tachycardia syndrome. These should be verified against the PI.

**Drug interactions:** The interaction query returned 100 records. Those shown include:
- **Moderate**: omeprazole, esomeprazole, rabeprazole, dexamethasone, eliglustat, linagliptin, cisapride
- **Minor**: hydrocortisone, pioglitazone, aprepitant, triamcinolone, betamethasone, cimetidine, clarithromycin, saxagliptin, dronabinol, clotrimazole, granisetron, miconazole, naldemedine

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
For hypersomnia, multiple Phase 3 trials, a randomised comparative trial and guideline-level sources (AASM 2021, European guideline) support modafinil for excessive sleepiness. Evidence is strongest for narcolepsy and weaker for idiopathic hypersomnia, so any extension should be off-label with monitoring. The top-ranked insomnia prediction should be rejected (Hold), as should the unsupported predictions with no evidence. ADHD and circadian rhythm sleep disorder remain research questions or symptomatic-use options only.

**To proceed, the following is needed:**
- Product Information (PI) warnings and contraindications for the Australian product (the safety screen cannot be completed without them)
- The approved indication text for ARTG 8816B
- Detailed mechanism of action data
- Cardiovascular and psychiatric risk assessment, given the contraindication signals above
- Clarification of the interaction profile (CYP-related interactions) before use in patients on multiple medicines
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

