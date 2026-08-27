---
layout: default
title: Montelukast
parent: 僅模型預測 (L5)
nav_order: 454
evidence_level: L5
indication_count: 10
---

# Montelukast
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

# Montelukast: From Established Airway Disease Use to Bronchitis

## One-Sentence Summary

Montelukast is a leukotriene receptor antagonist (LTRA) with well-documented use in asthma and allergic rhinitis, reflected throughout the supporting evidence in this pack. The TxGNN model's top-ranked new-indication signal is **Bronchitis**, supported by **23 clinical trials** and **20 publications**, though most of this evidence base actually concerns a related but distinct condition — bronchiolitis obliterans and eosinophilic bronchitis — rather than bronchitis in the general sense.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the Australian registration data reviewed (0 ARTG entries on file); evidence in this pack repeatedly refers to montelukast as an established asthma/allergic rhinitis therapy |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L2 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in this evidence pack. Based on the supporting trial and literature descriptions, montelukast is a selective cysteinyl leukotriene receptor 1 (CysLT1) antagonist — an established leukotriene receptor antagonist (LTRA) class drug. Its efficacy in asthma and allergic rhinitis is well documented across the evidence base collected here (multiple trials describe it as "an approved medication" for asthma), and mechanistically it may extend to other inflammatory airway conditions.

The predicted link to "bronchitis" is mechanistically plausible in principle, since leukotriene-mediated inflammation contributes to airway hyperresponsiveness in several respiratory conditions. However, the clinical trial and literature evidence actually retrieved for this candidate is concentrated in **bronchiolitis obliterans syndrome (BOS)** — a fibrotic, obstructive condition seen after lung or stem cell transplantation — and in **nonasthmatic eosinophilic bronchitis (NAEB)**, rather than bronchitis as commonly understood (acute or chronic bronchial inflammation, typically infective or smoking-related). This is flagged directly in the underlying evidence pack as a likely disease-ontology mapping discrepancy between the TxGNN "bronchitis" node and the studies retrieved.

Within the narrower NAEB subgroup, there is more direct mechanistic and trial support (e.g. add-on montelukast to inhaled corticosteroids reducing cough and airway eosinophilia). For classic bronchitis, the evidence is thin and largely indirect. This distinction matters for how the prediction should be interpreted and communicated to prescribers.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01211509](https://clinicaltrials.gov/study/NCT01211509) | Phase 4 | Completed | 30 | RCT testing montelukast to slow progression of bronchiolitis obliterans syndrome (chronic rejection) after lung transplantation |
| [NCT01307462](https://clinicaltrials.gov/study/NCT01307462) | Phase 2 | Completed | 36 | Montelukast combined with fluticasone and azithromycin (FAM) for bronchiolitis obliterans after stem cell transplant |
| [NCT00656058](https://clinicaltrials.gov/study/NCT00656058) | Phase 2 | Completed | 25 | Prospective study of montelukast for bronchiolitis obliterans following stem cell transplantation |
| [NCT01370187](https://clinicaltrials.gov/study/NCT01370187) | N/A | Completed | 146 | Montelukast for acute bronchiolitis and post-bronchiolitis wheezing in infants 3–12 months |
| [NCT04613180](https://clinicaltrials.gov/study/NCT04613180) | Phase 4 | Unknown | 100 | Evaluated montelukast for treatment and prevention of recurrent obstructive bronchitis in children aged 1–7 |
| [NCT01121016](https://clinicaltrials.gov/study/NCT01121016) | Phase 4 | Unknown | 63 | Add-on montelukast to inhaled budesonide for nonasthmatic eosinophilic bronchitis, cough outcome |
| [NCT00076973](https://clinicaltrials.gov/study/NCT00076973) | Phase 3 | Completed | 1,125 | Large RCT of montelukast for respiratory symptoms in RSV-induced bronchiolitis, children 3–24 months |
| [NCT02479074](https://clinicaltrials.gov/study/NCT02479074) | Phase 4 | Completed | 49 | Compared montelukast vs prednisolone response in chronic cough differential diagnosis (includes NAEB) |
| [NCT00524693](https://clinicaltrials.gov/study/NCT00524693) | N/A | Completed | 51 | Placebo-controlled trial of montelukast in acute RSV bronchiolitis, clinical and cytokine response |
| [NCT00863317](https://clinicaltrials.gov/study/NCT00863317) | N/A | Completed | 141 | RCT of daily montelukast on duration of acute illness in first-time viral bronchiolitis |

No ANZCTR-registered trials were identified in the evidence pack for this candidate.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38485149](https://pubmed.ncbi.nlm.nih.gov/38485149/) | 2024 | Clinical Practice Guideline | The European respiratory journal | ERS/EBMT joint guideline on treatment of pulmonary chronic GvHD, including BOS management |
| [25563311](https://pubmed.ncbi.nlm.nih.gov/25563311/) | 2015 | RCT | Chinese medical journal | Montelukast + budesonide improved airway inflammation, cough and quality of life vs budesonide alone in nonasthmatic eosinophilic bronchitis |
| [20976161](https://pubmed.ncbi.nlm.nih.gov/20976161/) | 2010 | RCT | PloS one | Compared fish oil and montelukast, alone and combined, on airway inflammation and exercise-induced bronchoconstriction |
| [26475726](https://pubmed.ncbi.nlm.nih.gov/26475726/) | 2016 | Cohort (Phase 2) | Biology of blood and marrow transplantation | Single-arm Phase II study of fluticasone/azithromycin/montelukast (FAM) for new-onset BOS after HCT |
| [27229850](https://pubmed.ncbi.nlm.nih.gov/27229850/) | 2016 | Cohort/Comparative | Respiratory research | Budesonide/formoterol + montelukast + N-acetylcysteine for BOS after stem cell transplant |
| [22819521](https://pubmed.ncbi.nlm.nih.gov/22819521/) | 2012 | Pilot Study | Respiratory medicine | Add-on montelukast vs double-dose budesonide in nonasthmatic eosinophilic bronchitis |
| [35114411](https://pubmed.ncbi.nlm.nih.gov/35114411/) | 2022 | Phase II Trial | Transplantation and cellular therapy | Prospective Phase II trial of montelukast for BOS after HCT, with pathogenesis investigation |
| [38504551](https://pubmed.ncbi.nlm.nih.gov/38504551/) | 2024 | Review | Therapeutic advances in respiratory disease | Reviews therapeutic potential and possible mechanisms of montelukast in BOS after transplantation |
| [21486501](https://pubmed.ncbi.nlm.nih.gov/21486501/) | 2011 | Review | BMJ clinical evidence | General review of bronchiolitis in infants, most common lower respiratory tract infection |
| [28545478](https://pubmed.ncbi.nlm.nih.gov/28545478/) | 2017 | Animal/Preclinical | Journal of cardiothoracic surgery | Rat model study of LTB4 and montelukast in transplantation-related bronchiolitis obliterans |

---

## Australia Market Information

No ARTG entries are recorded for montelukast in the data reviewed — the evidence pack lists 0 total licences and a market status of "Not Marketed." This should be verified directly against the TGA/ARTG database, as it conflicts with the drug's broader international regulatory history and may reflect a gap in the source dataset rather than the true market status.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No warnings, contraindications, or drug interaction data were available in this evidence pack — this is flagged internally as a **blocking data gap** (TGA/TFDA product-label data required before any safety assessment can proceed).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence pack itself stages this candidate at "Research Question" (L2 evidence), and the clinical trial/literature base largely addresses bronchiolitis obliterans syndrome and nonasthmatic eosinophilic bronchitis rather than bronchitis proper — a likely disease-ontology mismatch that needs resolving before the prediction can be acted on. Combined with the absence of any local safety/labelling data, this candidate is not ready to progress.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications, DDI) — currently a blocking gap
- Confirmed mechanism of action documentation from DrugBank or an equivalent source
- Clarification of whether "bronchitis" in the TxGNN prediction should instead be mapped to bronchiolitis obliterans syndrome or nonasthmatic eosinophilic bronchitis, and re-scoring accordingly
- Verification of montelukast's actual ARTG registration status in Australia, given the 0-entry result appears inconsistent with its known international availability
- If pursuing the NAEB sub-indication specifically, a focused evidence review of the Cochrane-type and RCT literature identified for that narrower population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

