---
layout: default
title: Dupilumab
parent: 僅模型預測 (L5)
nav_order: 174
evidence_level: L5
indication_count: 10
---

# Dupilumab
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

# Dupilumab: From Atopic Dermatitis/Asthma to Bronchitis

## One-Sentence Summary

Dupilumab (Dupixent®) is a human monoclonal antibody that blocks IL-4 and IL-13 signalling — cytokines central to Type 2 (Th2) inflammatory diseases — and is internationally approved for moderate-to-severe atopic dermatitis, uncontrolled asthma, chronic rhinosinusitis with nasal polyps, prurigo nodularis, and eosinophilic oesophagitis, though no ARTG entries were identified in the current Evidence Pack.

The TxGNN model predicts it may be effective for **bronchitis** (particularly eosinophilic and Type 2 airway subtypes), with **1 clinical trial** and **6 publications** providing indirect mechanistic support.

Given the well-characterised mechanism and strong international evidence base in overlapping airway conditions, this represents a scientifically plausible repurposing candidate warranting further evaluation in bronchitis-specific trials.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not currently TGA-registered (internationally: atopic dermatitis, uncontrolled asthma, CRSwNP) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 (observational studies and systematic reviews in overlapping airway conditions) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Dupilumab works by blocking the interleukin-4 receptor alpha subunit (IL-4Rα), which is the shared receptor component used by both IL-4 and IL-13. This dual blockade interrupts the core Type 2 (Th2) inflammatory cascade — the same mechanism underpinning its internationally approved indications for asthma and atopic dermatitis. Detailed mechanism of action data (MOA) was not available in the current Evidence Pack, but the drug's mode of action is well-characterised in the global literature.

The mechanistic case for bronchitis is strongest in eosinophilic and Type 2 inflammatory subtypes. IL-4 and IL-13 are the primary drivers of airway mucus hypersecretion, eosinophilic airway infiltration, subepithelial fibrosis, and bronchial epithelial remodelling — hallmark pathological features of Type 2 bronchitis. In eosinophilic bronchitis (characterised by airway eosinophilia without variable airflow obstruction), the IL-4/IL-13 axis is a recognised central driver. Dupilumab's existing international approvals in moderate-to-severe asthma — where airway eosinophilia and Type 2 inflammation are shared features — provide strong indirect mechanistic validation for this TxGNN prediction.

The upper and lower respiratory tract share convergent Type 2 inflammatory pathways (the "unified airway" concept). Dupilumab's efficacy in chronic rhinosinusitis with nasal polyps (an upper airway Type 2 disease) further reinforces the biological plausibility of its benefit extending to lower airway inflammatory conditions including eosinophilic bronchitis. It is important to note that the mechanistic rationale applies specifically to Type 2/eosinophilic bronchitis subtypes, and is unlikely to extend to non-eosinophilic or infectious bronchitis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT04362501](https://clinicaltrials.gov/study/NCT04362501) | Phase 2 | Completed | 33 | Dupilumab for chronic rhinosinusitis without nasal polyps (CRSsNP). Evaluates clinical effectiveness across Type 2 and non-Type 2 disease endotypes of CRS. Provides indirect support for bronchitis via shared upper/lower airway Th2 inflammation; the small sample size (n=33) limits direct extrapolation to bronchitis populations |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [34597534](https://pubmed.ncbi.nlm.nih.gov/34597534/) | 2022 | RCT Extension (2-year) | The Lancet. Respiratory Medicine | TRAVERSE: long-term safety and sustained efficacy of dupilumab in moderate-to-severe asthma over 2 years, demonstrating durable IL-4/IL-13 blockade in chronic airway disease |
| [30273510](https://pubmed.ncbi.nlm.nih.gov/30273510/) | 2019 | Systematic Review / Meta-analysis | Journal of Asthma | Meta-analysis of RCTs confirming dupilumab significantly reduces asthma exacerbations and improves FEV1; provides the strongest pooled evidence for IL-4Rα blockade in airway inflammation |
| [39904363](https://pubmed.ncbi.nlm.nih.gov/39904363/) | 2025 | Comprehensive Review | Tuberculosis and Respiratory Diseases | Review of pharmacological therapies for preventing COPD exacerbations; contextualises dupilumab among novel biologic agents targeting Type 2 inflammation in obstructive airways disease |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Narrative Review | Expert Opinion on Pharmacotherapy | Highlights challenges in managing asthma with smoking-induced airway diseases including chronic bronchitis and ACO (asthma-COPD overlap); underscores unmet clinical need in bronchitis-asthma overlap populations where IL-4/IL-13 inhibition is mechanistically plausible |
| [38488768](https://pubmed.ncbi.nlm.nih.gov/38488768/) | 2024 | Case Series / Review | Pediatric Pulmonology | Novel therapies for eosinophilic paediatric plastic bronchitis; dupilumab discussed as an emerging therapeutic option given IL-4/IL-13 involvement in mucus plug formation and airway cast development |
| [32428511](https://pubmed.ncbi.nlm.nih.gov/32428511/) | 2020 | Pilot RCT / Exploratory | Chest | Anti-T2 biologic therapy (dupilumab) measurably improved MRI-visualised lung ventilation defects in prednisone-dependent asthma with sputum eosinophilia, supporting mechanistic benefit in eosinophil-driven airway disease at a functional imaging level |

---

## Australia Market Information

No ARTG entries were identified for Dupilumab in the current Evidence Pack.

> **Important:** Clinicians should verify current ARTG registration status directly via the [TGA ARTG portal](https://www.tga.gov.au/resources/artg) before any prescribing decision, as registration data may be subject to lag in the Evidence Pack.

---

## Safety Considerations

> Please refer to the TGA-approved Product Information (PI) for full safety information.

No TGA-specific key warnings, contraindications, or drug interaction data were available in the current Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple high-quality systematic reviews and RCTs demonstrate dupilumab's sustained efficacy in asthma — an airway condition sharing the IL-4/IL-13-driven eosinophilic inflammation characteristic of Type 2 bronchitis — providing scientifically plausible indirect support for this repurposing prediction; however, no direct Phase 2/3 trials in bronchitis as a primary indication were identified, and patient subtype selection (eosinophilic vs. non-eosinophilic bronchitis) will be critical to any clinical programme.

**To proceed, the following is needed:**

- **ARTG verification:** Confirm current Australian registration status directly via the TGA portal, as the Evidence Pack shows 0 ARTG entries — a likely data gap given dupilumab's international regulatory history
- **TGA Product Information review:** Obtain full PI document for complete safety, contraindications, special population warnings, and drug interaction data prior to any clinical use
- **Patient subtype stratification protocol:** Restrict initial evaluation to eosinophilic/Type 2 bronchitis (blood eosinophils ≥300 cells/µL or FeNO ≥25 ppb); mechanistic rationale does not support use in non-eosinophilic, infectious, or smoking-related bronchitis subtypes
- **Direct clinical evidence:** Commission or identify a dedicated Phase 2 RCT in eosinophilic bronchitis; the current evidence base is entirely indirect (asthma and CRS trials)
- **Detailed MOA documentation:** Formal mechanism of action data from DrugBank should be obtained to strengthen the mechanistic rationale section for regulatory submissions
- **Pharmacoeconomic assessment:** Dupilumab carries a high acquisition cost; a cost-effectiveness analysis within the Australian healthcare context (PBS eligibility pathway) is required before any broader recommendation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

