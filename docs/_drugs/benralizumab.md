---
layout: default
title: Benralizumab
parent: Model Prediction Only (L5)
nav_order: 83
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Benralizumab: predicted new indication Dermatitis (evidence level L5). Approved use: Eosinophilic pneumonia"
monitor_inn: "Benralizumab"
predicted_indications: ["thrombocytopenia due to immune destruction", "dermatitis", "acne keloid", "neonatal dermatomyositis", "amyopathic dermatomyositis", "acrodermatitis chronica atrophicans", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "hydroa vacciniforme, familial", "autoimmune thrombocytopenic", "Evans syndrome"]
---

# Benralizumab
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

# Benralizumab: From Eosinophilic Pneumonia to Dermatitis

## One-Sentence Summary

Benralizumab is an anti-IL-5 receptor alpha (IL-5Rα) monoclonal antibody, originally used for eosinophilic lung conditions (eosinophilic pneumonia and pulmonary eosinophilia) and, per the data compiled for this report, for severe eosinophilic asthma.
The TxGNN model predicts it may be effective for **dermatitis**, with **3 Phase 2 clinical trials** and **20 publications** (mostly reviews) identified.
Direct efficacy evidence is weak: the largest placebo-controlled trial was terminated, and a published report describes a lack of effect in atopic dermatitis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Eosinophilic pneumonia; pulmonary eosinophilia (from the knowledge graph; the ARTG entry lists no indication text) |
| Predicted New Indication | Dermatitis |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L2 (as scored; see note below) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

*Note on evidence level:* The data compiled for this report assigns L2, but there is no completed Phase 2/3 randomised trial with a positive result. The only completed trial is a small mechanistic study (n=20), and the randomised trial was terminated. In practice the evidence is weaker than L2 suggests.

*Note on ranking:* The top-ranked TxGNN prediction (immune thrombocytopenia, score 99.34%) has no trials or literature (L5). Dermatitis is the highest-ranked prediction with any supporting evidence, so this report focuses on it.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known information, benralizumab depletes eosinophils and basophils through antibody-dependent cellular cytotoxicity directed at IL-5Rα.

Eosinophils, basophils and innate lymphoid type 2 cells contribute to type 2 inflammation in atopic dermatitis and related eosinophilic skin disease. This gives a plausible link to the original eosinophil-driven lung indications, where the same cells are the therapeutic target.

However, plausibility has not translated into clinical benefit. A published report of the Phase 2 HILLIER trial describes a **lack of effect** on signs and symptoms of moderate-to-severe atopic dermatitis. The mechanistic rationale should therefore be treated as unproven.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04605094](https://clinicaltrials.gov/study/NCT04605094) | Phase 2 | Terminated | 194 | HILLIER: randomised, double-blind, 16-week placebo-controlled study in moderate-to-severe atopic dermatitis despite topical treatment, with a 36-week extension. Terminated early; the published report describes no effect on disease signs and symptoms. |
| [NCT03563066](https://clinicaltrials.gov/study/NCT03563066) | Phase 2 | Completed | 20 | Mechanistic study of benralizumab effects on eosinophils, basophils and innate lymphoid type 2 cells in atopic dermatitis. Supports biological plausibility only; too small to show efficacy. |
| [NCT06734884](https://clinicaltrials.gov/study/NCT06734884) | Phase 2 | Not yet recruiting | 96 | Anti-IL-5R therapy in drug reaction with eosinophilia and systemic symptoms (DRESS). No results yet; relevant to eosinophilic skin disease, not atopic dermatitis specifically. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37178404](https://pubmed.ncbi.nlm.nih.gov/37178404/) | 2023 | Phase 2 RCT report (HILLIER) | J Eur Acad Dermatol Venereol | Lack of effect of benralizumab on signs and symptoms of moderate-to-severe atopic dermatitis versus placebo. |
| [35987486](https://pubmed.ncbi.nlm.nih.gov/35987486/) | 2022 | Review | J Allergy Clin Immunol Pract | Safety of biologics, including benralizumab, for atopic diseases during pregnancy. |
| [36411004](https://pubmed.ncbi.nlm.nih.gov/36411004/) | 2023 | Review | Immunol Allergy Clin North Am | Monoclonal antibodies for allergic rhinitis, asthma and atopic dermatitis during pregnancy and lactation. |
| [39600395](https://pubmed.ncbi.nlm.nih.gov/39600395/) | 2024 | Review | Allergologie Select | Update on biologics for atopic diseases, urticaria and angioedema, with a focus on hypersensitivity reactions. |
| [42383238](https://pubmed.ncbi.nlm.nih.gov/42383238/) | 2026 | Review | Curr Ther Res | Efficacy and safety of monoclonal antibodies in paediatric atopic dermatitis. |
| [36534318](https://pubmed.ncbi.nlm.nih.gov/36534318/) | 2023 | Review | Dermatol Ther | Updated pharmacologic approach to paediatric atopic dermatitis. |
| [34642091](https://pubmed.ncbi.nlm.nih.gov/34642091/) | 2021 | Review | Ann Allergy Asthma Immunol | Guidance on choosing among biologics for allergy and asthma, including atopic dermatitis. |
| [31690400](https://pubmed.ncbi.nlm.nih.gov/31690400/) | 2019 | Review | Allergy Asthma Proc | Immunobiologics, including anti-IL-5 agents, for severe asthma, atopic dermatitis and chronic urticaria. |
| [33236428](https://pubmed.ncbi.nlm.nih.gov/33236428/) | 2020 | Review | Pediatr Allergy Immunol | Anti-IL-5 therapy in paediatric allergic diseases, including atopic dermatitis. |
| [37170653](https://pubmed.ncbi.nlm.nih.gov/37170653/) | 2023 | Review | Clin Transl Sci | Evolving immunotherapy landscape for allergic conditions including atopic dermatitis. |

The remaining publications retrieved are general reviews of biologics in asthma and allergic disease and do not provide direct evidence for benralizumab in dermatitis.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11994G | Fasenra Pen | Injection 30 mg in 1 mL single dose pre-filled pen | Not listed in the compiled data |

---

## Safety Considerations

No warnings or contraindications were available in the compiled data. Please refer to the TGA-approved Product Information (PI) for safety information.

The only interaction record identified is a pharmacology entry for the drug's target (IL-5Rα), not a drug-drug interaction. Reviews retrieved discuss use of benralizumab and other biologics in pregnancy and lactation, where safety data remain limited.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale is plausible, but the only randomised placebo-controlled trial in atopic dermatitis was terminated and has been reported as showing no effect. The remaining evidence is a small mechanistic study, a trial in a different eosinophilic condition with no results, and review articles. The high TxGNN score is a computational prediction and does not offset the negative clinical signal.

**To proceed, the following is needed:**
- Review of the HILLIER termination reason and full results (efficacy futility versus safety)
- Reassessment of whether any dermatitis subtype, such as eosinophil-driven DRESS, merits focused investigation once NCT06734884 reports
- Mechanism of action data and TGA PI warnings and contraindications
- Confirmation of the approved indications for ARTG 11994G

**Other predictions:** The other top-10 predictions (including immune thrombocytopenia, Evans syndrome and dermatomyositis variants) have no clinical trials or literature and weak mechanistic support. All remain at **Hold**.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

