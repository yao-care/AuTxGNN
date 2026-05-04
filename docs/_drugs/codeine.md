---
layout: default
title: Codeine
parent: 僅模型預測 (L5)
nav_order: 127
evidence_level: L5
indication_count: 10
---

# Codeine
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

# Codeine: From Analgesic/Antitussive to Bronchial Disease

## One-Sentence Summary

Codeine is a well-established opioid alkaloid, widely recognised for mild-to-moderate pain relief and cough suppression (antitussive use), though no original indications were recorded in this evidence pack and the drug is not currently registered on the ARTG as a standalone product.
The TxGNN model generated 10 predicted indications; **ranks 1–9 were assessed as false positives or mechanistically unsupported**, while **bronchial disease** (rank 10) represents the only candidate with genuine mechanistic plausibility, supported by **5 clinical trials** and **20 publications**.
Overall evidence strength is **L3**, and a dedicated codeine-specific trial for this indication has not yet been conducted.

---

## ⚠️ Prediction Quality Alert: Top-Ranked Predictions Require Caution

Before the primary analysis, this evidence pack contains an important finding: the highest-scoring TxGNN predictions are **not valid repurposing signals**. The table below summarises the quality assessment across all 10 ranked candidates.

| Rank | Disease | TxGNN Score | Issue | Decision |
|------|---------|------------|-------|---------|
| 1 | Nasal cavity disease | 99.93% | **False positive** — literature describes opioid-induced nasal tissue *damage*, not treatment | Hold |
| 2 | Acute laryngopharyngitis | 99.92% | Infectious aetiology; codeine has no anti-infective mechanism; no evidence | Hold |
| 3 | Trigeminal autonomic cephalalgia | 99.43% | Opioids generally contraindicated in cluster headache; literature reports describe drug misuse, not efficacy | Hold |
| 4 | Allergic urticaria | 99.37% | **Reverse mechanism** — codeine is a known urticaria *trigger* via non-immunological mast cell degranulation | Hold |
| 5 | Faucial diphtheria | 97.63% | Bacterial toxin disease; codeine has no antibacterial or anti-toxin mechanism; zero evidence | Hold |
| 6 | Cervical disc degenerative disorder | 97.40% | Extension of existing analgesic use, not novel repurposing; chronic opioid use in musculoskeletal pain is actively discouraged | Hold |
| 7 | Papillary conjunctivitis | 97.17% | No mechanistic rationale; opioid-induced histamine release could theoretically worsen allergic ocular symptoms | Hold |
| 8 | Tracheal disease | 95.70% | Antitussive rationale is plausible for cough symptom only; no disease-modifying evidence; structural tracheal pathology unaddressed | Hold |
| 9 | Cold urticaria | 94.63% | **Methodological false positive** — codeine used as a positive control stimulus in lab skin tests, not as a therapy | Hold |
| **10** | **Bronchial disease** | **93.66%** | **Best available candidate** — antitussive mechanism is supported; L3 evidence; targeted research warranted | **Research Question** |

> **Root cause**: Ranks 1–9 most likely reflect literature co-occurrence bias. Codeine appears frequently in allergy, ENT, and dermatology literature as a pharmacological tool (mast cell degranulator, diagnostic skin-test agent) rather than as a therapeutic. TxGNN cannot distinguish "drug causes disease" from "drug treats disease" in these contexts.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Analgesic and antitussive *(original_indications field empty in evidence pack; based on established pharmacological profile)* |
| Predicted New Indication | Bronchial Disease |
| TxGNN Prediction Score | 93.66% |
| Evidence Level | L3 — Observational studies and systematic reviews |
| Australia Market Status | Not marketed (未上市) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Research Question (Hold for all other ranks) |

---

## Why is This Prediction Reasonable?

Codeine is a naturally occurring opium alkaloid and prodrug that is hepatically O-demethylated by CYP2D6 to morphine, its active form. As a central μ-opioid receptor agonist acting on the medullary cough centre (nucleus tractus solitarius), codeine suppresses the cough reflex by raising the threshold for cough stimulation. This mechanism is directly relevant to bronchial disease presentations where pathological, non-productive cough is a dominant and disabling symptom — particularly in chronic bronchitis, chronic obstructive pulmonary disease (COPD), and post-infectious cough.

The relationship between codeine and bronchial disease is not a speculative leap. ACCP evidence-based guidelines explicitly reference opioids, including codeine, as antitussive agents for chronic cough due to chronic bronchitis when first-line therapies are insufficient (PMID:16428699). A 2024 nationwide Korean population-based cohort study (PMID:39632868) directly evaluated chronic codeine use across cough-related bronchial conditions including COPD and asthma, demonstrating real-world utilisation at scale. Head-to-head comparative studies against dextromethorphan in patients with pathological cough have established codeine's pharmacokinetic and antitussive profile (PMID:6539224).

However, a critical safety boundary must be drawn: codeine can **induce bronchoconstriction** in asthmatic patients via bronchial opioid receptors and secondary histamine release (PMID:7626920). This finding fundamentally limits the viable repurposing target to **non-asthmatic** bronchial disease, and any clinical application must explicitly exclude patients with asthma, atopic airways disease, or hyperreactive airways. The mechanistic plausibility is real but narrow.

---

## Clinical Trial Evidence (Bronchial Disease)

> **Important caveat**: No clinical trials were identified that directly study **codeine** as the named intervention for **bronchial disease**. The trials below are the most contextually relevant based on antitussive/opioid mechanisms in airway disease. Direct evidence is therefore indirect.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|------------|------|------|----------|-------------|
| [NCT03738917](https://clinicaltrials.gov/study/NCT03738917) | Phase 4 | Completed | 668 | Multicentre RCT comparing antitussive agents (dextromethorphan), anticholinergics (ipratropium), and honey vs usual care in adults with uncomplicated acute bronchitis; directly relevant to antitussive class evidence in bronchial disease |
| [NCT02321397](https://clinicaltrials.gov/study/NCT02321397) | Phase 2/3 | Completed | 155 | Randomised double-blind equivalence study of oxycodone/naloxone tablet strengths in chronic non-malignant and malignant pain; opioid class safety data relevant to codeine |
| [NCT01438567](https://clinicaltrials.gov/study/NCT01438567) | Phase 3 | Completed | 270 | Parallel-group RCT of oxycodone/naloxone vs oxycodone alone in cancer and non-cancer pain; bowel function and analgesic efficacy endpoints; opioid class reference |
| [NCT00513656](https://clinicaltrials.gov/study/NCT00513656) | Phase 2 | Completed | 230 | Active-controlled RCT of oxycodone/naloxone in chronic cancer pain; safety and efficacy of opioid class |
| [NCT02982876](https://clinicaltrials.gov/study/NCT02982876) | N/A | Completed | 50 | RCT of airway stents for excessive dynamic airway collapse (EDAC) — device intervention; low relevance to codeine pharmacotherapy |

---

## Literature Evidence (Bronchial Disease)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|-----|-------|------------|
| [39632868](https://pubmed.ncbi.nlm.nih.gov/39632868/) | 2024 | Population-based Cohort | *Scientific Reports* | Nationwide Korean cohort study of chronic codeine use across cough-related diseases; evaluated utilisation patterns in COPD, asthma, and allergic rhinitis — the highest-quality study in this pack |
| [20385478](https://pubmed.ncbi.nlm.nih.gov/20385478/) | 2010 | Systematic Review | *Respiratory Medicine* | Systematic review of pharmacological and non-pharmacological interventions for cough in adults with respiratory diseases; 75 trials included; codeine addressed as antitussive reference agent |
| [16428699](https://pubmed.ncbi.nlm.nih.gov/16428699/) | 2006 | ACCP Clinical Guidelines | *Chest* | Evidence-based guidelines for chronic cough due to chronic bronchitis; opioids including codeine identified as antitussive option when standard therapies fail |
| [7626920](https://pubmed.ncbi.nlm.nih.gov/7626920/) | 1994 | Controlled Clinical Study | *Pulmonary Pharmacology* | **Critical safety finding**: Codeine induces bronchoconstriction in asthmatic subjects; naloxone partially blocks this effect; establishes absolute contraindication in asthma subtype |
| [6539224](https://pubmed.ncbi.nlm.nih.gov/6539224/) | 1984 | Comparative Clinical Study | *Eur J Respir Dis* | Plasma kinetics and antitussive dose-response of dextromethorphan vs codeine phosphate (60 mg) in patients with pathological cough; pharmacokinetic basis for antitussive dosing |
| [15827540](https://pubmed.ncbi.nlm.nih.gov/15827540/) | 2005 | Review | *Minerva Medica* | Pathophysiology and therapy of chronic cough; codeine discussed as established antitussive with central mechanism of action |
| [29182956](https://pubmed.ncbi.nlm.nih.gov/29182956/) | 2018 | Epidemiological Study | *Forensic Science International* | Australian-specific study of unintentional mortality associated with paracetamol/codeine/doxylamine combination products; key Australian safety and regulatory context |
| [19692698](https://pubmed.ncbi.nlm.nih.gov/19692698/) | 2009 | Pharmacogenomics Case Study | *NEJM* | CYP2D6 ultra-rapid metabolism genotype and postoperative death following codeine — foundational pharmacogenomic safety signal for all codeine prescribing |
| [952583](https://pubmed.ncbi.nlm.nih.gov/952583/) | 1976 | Comparative Preclinical/Clinical | *Arch Int Pharmacodyn* | Antitussive properties of butorphanol vs codeine and morphine; establishes codeine as the historical antitussive reference standard |
| [36088097](https://pubmed.ncbi.nlm.nih.gov/36088097/) | 2022 | Case Report | *Chest* | 65-year-old with intractable cough; management discussion referencing antitussive options including opioids |

---

## Australia Market Information

Codeine has **no current standalone registrations** on the Australian Register of Therapeutic Goods (ARTG). The TGA search returned zero entries for codeine as an active ingredient.

> **Regulatory context**: From **1 February 2018**, the TGA up-scheduled all over-the-counter codeine-containing products to **Schedule 4 (prescription-only)** in Australia, citing risks of dependence, misuse, and accidental overdose. Prior to this date, low-dose combination products (e.g., paracetamol/codeine) were available as Schedule 3 pharmacy medicines. Any new repurposing application in Australia must be developed within this prescription-only regulatory framework.

---

## Safety Considerations

Full TGA-approved Product Information was not available in this evidence pack. Please refer to the TGA-approved Product Information (PI) for complete safety information.

Based on the clinical literature reviewed in this pack, the following safety signals are specifically relevant to any bronchial disease repurposing pathway:

- **Bronchoconstriction in asthma**: Codeine-induced bronchoconstriction has been documented in asthmatic subjects (PMID:7626920). This is a **hard exclusion criterion** for any bronchial disease indication that includes asthmatic or hyperreactive airway patients.
- **CYP2D6 pharmacogenomics**: Ultra-rapid CYP2D6 metabolisers convert codeine to morphine at an accelerated rate, causing potentially fatal opioid toxicity; poor metabolisers receive inadequate antitussive effect. The NEJM case (PMID:19692698) led to significant international regulatory action. CYP2D6 genotyping is a key safety requirement.
- **Australian mortality signal**: Unintentional deaths from codeine-containing combination products have been documented in Australia (PMID:29182956), supporting the TGA's 2018 scheduling decision and signalling real-world risk in Australian patients.
- **Mast cell degranulation**: Codeine directly triggers non-immunological histamine release — relevant to patients with concurrent allergic conditions or atopic disease who may also present with cough-predominant bronchial symptoms.
- **Dependence and opioid misuse**: As a Schedule 4 controlled medicine in Australia, codeine carries a recognised dependence risk that is especially pertinent if long-term antitussive use is contemplated in chronic bronchial disease.

---

## Conclusion and Next Steps

**Decision: Research Question** *(for bronchial disease only — Hold for all other ranked predictions)*

**Rationale:**
Ranks 1–9 of the TxGNN predictions are false positives driven by literature co-occurrence bias and should not be pursued as repurposing candidates. Bronchial disease (rank 10) is the sole candidate with a coherent mechanistic basis — codeine's well-established central antitussive action — supported by L3 real-world and observational evidence. However, no codeine-specific RCT for bronchial disease exists, codeine is not currently registered on the ARTG as a standalone product, and its 2018 TGA up-scheduling creates a significant regulatory and safety hurdle.

**To proceed, the following is needed:**

- **TGA PI acquisition**: Obtain and review the full TGA Product Information for codeine phosphate to document approved Australian warnings, contraindications, and precautions
- **Population definition**: Precisely define the target population as **non-asthmatic, non-atopic** chronic bronchial disease with pathological cough, with formal exclusion criteria for asthma and hyperreactive airways
- **CYP2D6 genotyping protocol**: Develop a pharmacogenomic testing strategy to screen out ultra-rapid metabolisers (safety) and poor metabolisers (efficacy) prior to any prospective study or compassionate use
- **Dedicated clinical trial**: Commission a prospective, codeine-specific RCT in non-asthmatic chronic bronchial disease; the existing literature treats codeine as a comparator rather than the study drug, which constitutes a significant evidence gap
- **Comparative effectiveness framing**: Consider a head-to-head design against dextromethorphan and/or gefapixant (P2X3 antagonist) to identify any clinically meaningful advantage for codeine in this narrow indication
- **TGA regulatory consultation**: Engage TGA early to assess the feasibility of a new indication pathway under the prescription-only framework; determine whether a data package for a Section 19A exemption or a formal NDA supplement is appropriate given the scheduling status

---

> *This report is intended for Australian healthcare professionals for research evaluation purposes only. It does not constitute medical advice or clinical guidance. All repurposing candidates require clinical validation before therapeutic application. Results from the TxGNN predictive model are exploratory and do not represent established medical evidence.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

