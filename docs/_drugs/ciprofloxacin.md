---
layout: default
title: Ciprofloxacin
parent: Model Prediction Only (L5)
nav_order: 162
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ciprofloxacin: predicted new indication Diffuse scleroderma (evidence level L4). Approved use: Bacterial infections (e.g. typhoid fever, salmonellosis…"
monitor_inn: "Ciprofloxacin"
predicted_indications: ["diffuse scleroderma", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "punctate epithelial keratoconjunctivitis", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
---

# Ciprofloxacin
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

## Ciprofloxacin: From Bacterial Infections to Diffuse Scleroderma
{: .text-alpha }

## One-Sentence Summary

Ciprofloxacin is a fluoroquinolone antibiotic, originally used for infections such as typhoid fever, bacterial pneumonia, anthrax and shigellosis.
The TxGNN model predicts it may be effective for **diffuse scleroderma**, but there are **no registered clinical trials** and only **2 publications**, so the evidence is weak.
One 2010 paper suggests a possible skin antifibrotic effect, but its design and results could not be confirmed from the data compiled for this report.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (e.g. typhoid fever, salmonellosis, bacterial pneumonia, Pseudomonas aeruginosa infection, anthrax, shigellosis) |
| Predicted New Indication | Diffuse scleroderma |
| TxGNN Prediction Score | 0.9987 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Ciprofloxacin is a fluoroquinolone that inhibits bacterial DNA gyrase and topoisomerase IV. Its efficacy in bacterial infections is well established. Nothing in that mechanism directly explains an effect on scleroderma.

Any link to scleroderma is indirect and has two possible routes:

1. **Treating small bowel bacterial overgrowth.** This is common in systemic sclerosis and causes diarrhoea, weight loss and malabsorption. A 1995 study examined this complication. Treating it would relieve a complication, not modify the underlying disease.
2. **A proposed antifibrotic effect in the skin.** A 2010 paper investigated oral ciprofloxacin as an antifibrotic in scleroderma skin. No direct disease-modifying mechanism has been established.

The very high TxGNN score is not backed by clinical data. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20507401](https://pubmed.ncbi.nlm.nih.gov/20507401/) | 2010 | Exploratory (antifibrotic effect in scleroderma skin) | The Journal of Dermatology | Examines whether oral ciprofloxacin reduces scleroderma severity. The abstract describes a controlled, double-blind randomised trial, but the available text is truncated and the results could not be confirmed. |
| [7728404](https://pubmed.ncbi.nlm.nih.gov/7728404/) | 1995 | Cohort/Diagnostic | British Journal of Rheumatology | 24 systemic sclerosis patients with diarrhoea and weight loss were assessed for small bowel bacterial overgrowth and treatment outcome. This concerns a complication, not the underlying disease. |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1208N | C-Flox 250 | Tablet 250 mg (as hydrochloride) | Not stated in the data compiled for this report |

Only an oral tablet formulation is listed.

---

## Safety Considerations

Label-based warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for these.

- **Contraindication-related conditions (from a knowledge graph, not label text):** long QT syndrome, torsades de pointes, epilepsy, kidney disease, potassium deficiency, tendinitis and other tendon disorders, peripheral neuropathy, myasthenia gravis, and *Clostridium difficile* colitis.
- **Drug interactions:** 100 interactions were recorded. Those rated **Major** include the corticosteroids hydrocortisone, triamcinolone, dexamethasone and betamethasone, and bupropion. Interactions rated **Moderate** include metformin, pioglitazone, alogliptin, albiglutide, acarbose, famotidine, loperamide, alosetron, aprepitant, aspirin, balsalazide, bisacodyl, budesonide and calcium phosphate. Corticosteroid co-use is relevant because tendon disorders appear among the flagged conditions, and corticosteroids are commonly used in scleroderma care.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a very high model score, but there are no registered trials. The two publications are exploratory or concern a complication of the disease. No direct disease-modifying mechanism is established. The knowledge-graph safety signals (tendon, neuropathy, QT) also argue for caution in a chronic condition like scleroderma.

**To proceed, the following is needed:**
- Full text of the 2010 study (design, sample size, outcomes) to judge whether the antifibrotic signal is credible
- Mechanistic data supporting an antifibrotic effect
- A well-designed controlled trial in diffuse scleroderma, ideally registered (ClinicalTrials.gov or ANZCTR)
- Label safety information from the TGA PI, including tendon, neuropathy and QT warnings
- A risk-benefit assessment for long-term use, including antimicrobial resistance and corticosteroid co-prescribing

**Note on other predictions:** The strongest-supported prediction for this drug in the data compiled is **septicaemic plague** (TxGNN score 0.9964, Evidence Level L1, Proceed with Guardrails). It is supported by randomised trial publications, mainly in bubonic plague. It is an extension of ciprofloxacin's existing antibacterial spectrum, not a new mechanism, and it merits separate evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

