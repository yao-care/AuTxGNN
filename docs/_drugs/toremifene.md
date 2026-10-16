---
layout: default
title: Toremifene
parent: Model Prediction Only (L5)
nav_order: 740
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Toremifene: predicted new indication HIV infectious disease (evidence level L5). Approved use: Hormone-dependent breast cancer"
---

# Toremifene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Toremifene: From Breast Cancer to HIV Infectious Disease

## One-Sentence Summary

Toremifene is a selective estrogen receptor modulator (SERM) used for hormone-dependent breast cancer.
The TxGNN model predicts it may be effective for **HIV infectious disease**, but **no clinical trials** and only **1 preclinical publication** (on a related opportunistic fungal infection, not HIV itself) support this. The prediction is model-based only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hormone-dependent breast cancer (the ARTG entry in the data compiled for this report has no indication text; this is taken from the literature) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Toremifene is a SERM, a chlorinated tamoxifen analogue that blocks estrogen receptor signalling in breast tissue. Its efficacy in breast cancer is well established, but there is no direct mechanistic link to HIV.

The only linked paper (PMID 24520056) is a preclinical study. It reports that estrogen receptor antagonists related to tamoxifen and toremifene have antifungal activity against *Cryptococcus* and work synergistically with fluconazole. Cryptococcosis is a common opportunistic infection in people with advanced HIV/AIDS, but this does not show any effect on HIV itself.

The high TxGNN score (99.41%) is therefore best read as a knowledge-graph association, not as evidence of antiviral activity.

Related predictions in the same output show a similar pattern:
- **AIDS:** Two in vitro studies exist, one on AIDS-related Kaposi's sarcoma cells and one on cryptococcal infection. Neither shows an effect on HIV disease.
- **Simian immunodeficiency virus infection and feline AIDS:** Prediction only, with no studies.
- **Female breast carcinoma:** This is the best-supported prediction (multiple Phase 3 trials). However, it confirms existing use and is not true repurposing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for HIV infectious disease.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24520056](https://pubmed.ncbi.nlm.nih.gov/24520056/) | 2014 | Preclinical / in vitro | mBio | Tamoxifen and toremifene are fungicidal against *Cryptococcus* and synergise with fluconazole and amphotericin B. They act by binding EF-hand proteins. No HIV data. |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13859K | Fareston | Tablet 60 mg (as citrate), oral | Not listed in the data compiled for this report |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal (endocrine) therapy, a SERM. Not a conventional cytotoxic agent. |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions. Leukopenia and thrombocytopenia appear among the knowledge-graph contraindication links (see below). |
| Emetogenicity Classification | Please refer to the PI |
| Monitoring Items | Please refer to the PI. Consider baseline and periodic FBC, electrolytes (potassium, calcium) and ECG given the QT-related signals below. |
| Handling Protection | Please refer to the PI and local handling policies |

---

## Safety Considerations

Label-based warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for these.

- **Knowledge-graph contraindication links** (from the TxGNN knowledge graph, not label text): long QT syndrome, familial long QT syndrome, torsades de pointes, thrombocytopenia, potassium deficiency, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease, leukopenia and endometrial hyperplasia. QT prolongation is a recognised concern for this drug class.
- **Drug Interactions:** 100 interactions were identified, and 20 are listed in the data reviewed. The **Major** interactions among them are:
  - Dexamethasone
  - Clarithromycin
  - Levofloxacin
  - Dolasetron
  - Palonosetron
  - Picosulfuric acid
  - Polyethylene glycol (3350 with electrolytes)
  - Sodium sulfate

  Several of these are QT-prolonging agents or bowel preparations that can cause electrolyte disturbance. Moderate interactions include famotidine, cimetidine, pioglitazone, loperamide, aprepitant, bisacodyl, metreleptin, miconazole, nateglinide, lactitol and lactulose. The minor interaction listed is metronidazole.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The HIV prediction rests on a model score alone. The only linked evidence is a preclinical study on cryptococcal infection, and there are no clinical trials and no direct anti-HIV data. The QT and drug interaction profile would need careful management in people with HIV, who often take interacting antiretroviral and anti-infective agents.

**To proceed, the following is needed:**
- In vitro or in vivo evidence of anti-HIV activity (or of benefit for a defined HIV-associated condition)
- Mechanism of action data linking toremifene to HIV biology
- The approved indication text and PI safety information (warnings, contraindications) for the Australian product
- A drug interaction and QT risk assessment against common antiretroviral regimens
- If a repurposing programme is still wanted, consider the AIDS-associated conditions with preclinical signals (cryptococcosis and Kaposi's sarcoma). These are more plausible than HIV itself.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

