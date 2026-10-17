---
layout: default
title: Posaconazole
parent: Moderate Evidence (L3-L4)
nav_order: 585
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Posaconazole: predicted new indication Pneumocystosis (evidence level L4). Approved use: Fungal infections, including candidiasis, aspergillosis…"
monitor_inn: "Posaconazole"
predicted_indications: ["pneumocystosis", "leprosy", "multibacillary leprosy", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "isolated genetic hair shaft abnormality", "syndrome with a Dandy-Walker malformation as major feature", "hypertrichosis (disease)", "paucibacillary leprosy"]
---

# Posaconazole
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Posaconazole: From Invasive Fungal Infections to Pneumocystosis

## One-Sentence Summary

Posaconazole is a triazole antifungal, originally used for fungal infections such as candidiasis, aspergillosis and histoplasmosis.
The TxGNN model predicts it may be effective for **pneumocystosis**, but the data compiled for this report show **no clinical trials directly testing posaconazole** for this condition and only **5 general publications**, none of which show benefit.
The prediction is best regarded as a model-generated hypothesis with weak mechanistic support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Fungal infections, including candidiasis, aspergillosis, histoplasmosis and sporotrichosis (the ARTG entry has no indication text recorded) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Posaconazole is a triazole antifungal. Drugs in this class generally inhibit fungal lanosterol 14-alpha-demethylase (CYP51), which blocks ergosterol synthesis in the fungal cell membrane.

This is where the prediction becomes doubtful. *Pneumocystis jirovecii* does not rely on ergosterol and instead uses cholesterol-type sterols, so azole antifungals are not expected to work against it. The high TxGNN score most likely reflects the drug's general association with antifungal indications in the knowledge graph rather than a true mechanistic fit. The prediction should therefore be treated with caution.

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
- **Vulvovaginal candidiasis (score 98.9%):** mechanistically plausible, because *Candida* is within posaconazole's established antifungal spectrum. However, the evidence is limited to in vitro susceptibility studies, isolate typing, guidelines and one mouse vaginal model, with no clinical trial. Effective, cheaper alternatives such as fluconazole and topical azoles exist. It is best treated as a research question rather than a candidate for adoption.
- **Leprosy, multibacillary leprosy and paucibacillary leprosy (scores 97.98–98.84%):** *Mycobacterium leprae* is a bacterium with no ergosterol target. The retrieved literature concerns fungal infections and appears to be keyword matches. No supporting evidence was found.
- **Hair, developmental and malformation conditions** (Ambras type hypertrichosis universalis congenita, hypertrichosis, isolated genetic hair shaft abnormality, malformation syndromes with a dental or periodontal component, and Dandy-Walker malformation syndromes): no credible mechanism and no clinical or literature evidence. These appear to be knowledge-graph artefacts, and for developmental conditions a teratogenicity concern would outweigh any therapeutic promise.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

