---
layout: default
title: Posaconazole
parent: Model Prediction Only (L5)
nav_order: 585
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
monitor_inn: "Posaconazole"
predicted_indications: ["pneumocystosis"]
description: "Posaconazole: predicted new indication Pneumocystosis (evidence level L5). Approved use: Not recorded in the local data"
---

# Posaconazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Posaconazole: Pneumocystosis
{: .text-alpha }

## One-Sentence Summary

Posaconazole is a triazole antifungal, originally used for fungal infections such as candidiasis, aspergillosis and histoplasmosis.
The TxGNN model predicts it may be effective for **pneumocystosis**, but the data compiled for this report show **no clinical trials directly testing posaconazole** for this condition and only **5 general publications**, none of which show benefit.
The prediction is best regarded as a model-generated hypothesis with weak mechanistic support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 0.9977 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Posaconazole is a triazole antifungal. Drugs in this class generally inhibit fungal lanosterol 14-alpha-demethylase (CYP51), which blocks ergosterol synthesis in the fungal cell membrane.

This is where the prediction becomes doubtful. *Pneumocystis jirovecii* does not rely on ergosterol and instead uses cholesterol-type sterols, so azole antifungals are not expected to work against it. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The prediction should therefore be treated with caution.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | Completed | 602 | ReSPECT study: IV rezafungin versus the standard antimicrobial regimen to prevent invasive fungal disease after allogeneic blood and marrow transplantation. Posaconazole is not the agent under study, so this trial provides no direct evidence for posaconazole in pneumocystosis. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Review | Swiss Med Wkly | Overview of invasive candidiasis, aspergillosis, cryptococcosis and *Pneumocystis* pneumonia. Notes that mould-active posaconazole prophylaxis reduced invasive fungal disease in high-risk haemato-oncology patients. |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review | Clin Pharmacokinet | Penetration of antifungal and other anti-infective agents into pulmonary epithelial lining fluid. Pharmacokinetic data only. |
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2026 | Guideline | Lancet Infect Dis | British Society for Medical Mycology recommendations for diagnosing serious fungal diseases (2025 update). Diagnostic focus. |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Guideline | Zhonghua Jie He He Hu Xi Za Zhi | Chinese guidelines for diagnosing and managing invasive pulmonary fungal disease (2025). |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Cohort | Transpl Infect Dis | Infectious complications of acute graft-versus-host disease after liver transplantation. Not specific to posaconazole for pneumocystosis. |

None of these publications demonstrates efficacy of posaconazole against pneumocystosis.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10460M | Posaconazole Juno | Tablet (modified release) 100 mg | Not recorded in the data compiled for this report |

---

## Safety Considerations

- **Drug Interactions:** The interaction screen returned 100 interacting drugs. Of the 20 shown, the **major** interactions were with loperamide, triamcinolone and budesonide. **Moderate** interactions included:
  - Acid suppressants: famotidine, ranitidine, cimetidine, omeprazole and rabeprazole
  - Corticosteroids: hydrocortisone, dexamethasone and betamethasone
  - Others: aprepitant, clarithromycin, saxagliptin, bisacodyl, picosulfuric acid and polyethylene glycol with electrolytes

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction rests on model output alone. No trial tests posaconazole for pneumocystosis, and the literature shows no benefit.
- *Pneumocystis* lacks the ergosterol target of azoles, which makes the prediction mechanistically implausible.

**To proceed, the following is needed:**
- Mechanism of action data confirming a plausible target in *Pneumocystis*
- In vitro or animal evidence of posaconazole activity against *Pneumocystis*
- TGA-approved Product Information (PI) warnings and contraindications
- A review of the drug interaction profile if any clinical use is contemplated

**Other predictions in the ranked list:**
- **Vulvovaginal candidiasis:** mechanistically plausible, because *Candida* is within posaconazole's established antifungal spectrum. However, the evidence is limited to in vitro susceptibility studies, isolate typing, guidelines and one mouse vaginal model, with no clinical trial. Effective, cheaper alternatives such as fluconazole and topical azoles exist. It is best treated as a research question rather than a candidate for adoption.
- These appear to be TxGNN model (deep learning) artefacts, and for developmental conditions a teratogenicity concern would outweigh any therapeutic promise.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

