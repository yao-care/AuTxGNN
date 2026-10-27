---
layout: default
title: Maraviroc
parent: Model Prediction Only (L5)
nav_order: 446
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Maraviroc: predicted new indication Multiple endocrine neoplasia (evidence level L5). Approved use: Not stated in the data compiled for this report (the registered entry…"
monitor_inn: "Maraviroc"
predicted_indications: ["multiple endocrine neoplasia", "acne (disease)", "primary cutaneous T-cell lymphoma", "pediatric systemic lupus erythematosus", "primary cutaneous T-cell non-Hodgkin lymphoma", "primary cutaneous B-cell lymphoma", "candidiasis", "complement component 4a deficiency", "cytomegalovirus infection", "HER2 positive breast carcinoma"]
---

# Maraviroc
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

## Maraviroc: From HIV-1 Infection (CCR5-Tropic) to Multiple Endocrine Neoplasia
{: .text-alpha }

## One-Sentence Summary

Maraviroc is an oral CCR5 antagonist marketed in Australia as a 150 mg tablet. The TxGNN model predicts it may be effective for **multiple endocrine neoplasia**, but **no clinical trials** and **no publications** currently support this prediction. It is a model-only prediction, and a different candidate (HER2-positive breast carcinoma) has far more biological support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the registered entry lists no indication text). Maraviroc is generally known as a CCR5 antagonist used in HIV-1 infection. |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, maraviroc is a CCR5 antagonist. It blocks a chemokine receptor involved in immune-cell trafficking and signalling.

For multiple endocrine neoplasia (MEN), no established link between CCR5 signalling and the disease was identified. MEN is driven by MEN1 or RET alterations, which are not obviously related to CCR5. The prediction therefore appears to be a statistical output of the model rather than a mechanistically supported hypothesis.

Other predictions for this drug are better grounded. The strongest is **HER2-positive breast carcinoma** (score 99.22%). A preclinical study (PMID 32404410) reported that autocrine CCL5 drives trastuzumab resistance through ERK pathway activation. CCL5 signals via CCR5, so CCR5 blockade is a coherent hypothesis. This is preclinical and indirect, and it warrants laboratory validation before any clinical consideration. Cutaneous T-cell lymphoma also has a plausible chemokine-trafficking rationale, but only an indirect review supports it.

## Clinical Trial Evidence

Currently no related clinical trials registered for multiple endocrine neoplasia. None were found for any of the other top-10 predicted indications either.

## Literature Evidence

Currently no related literature available for multiple endocrine neoplasia.

For context, the following publications relate to other predicted indications and are indirect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32404410](https://pubmed.ncbi.nlm.nih.gov/32404410/) | 2020 | Preclinical | Mol Cancer Ther | Autocrine CCL5 mediates trastuzumab resistance via ERK activation in HER2-positive breast cancer (CCR5 pathway relevance) |
| [37006247](https://pubmed.ncbi.nlm.nih.gov/37006247/) | 2023 | Review | Front Immunol | Review of targeting ACKR1 (an atypical chemokine receptor) in cancer and other diseases; indirect, relevant to cutaneous T-cell lymphoma predictions |
| [25397464](https://pubmed.ncbi.nlm.nih.gov/25397464/) | 2014 | Cohort | J Int AIDS Soc | Innate immunity and metabolic markers in HIV+ patients on ART; indirect, linked to the cytomegalovirus prediction |
| [21671545](https://pubmed.ncbi.nlm.nih.gov/21671545/) | 2011 | Review | Am Fam Physician | Adverse effects of antiretroviral therapy in HIV; candidiasis appears as HIV context, not a maraviroc effect |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10318C | Maraviroc Waymade | Tablet 150 mg | Not stated in the compiled data |

## Safety Considerations

- **Disease-level cautions from the knowledge graph** (these are model-derived contraindication links, not label text): multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, kidney disease (including chronic and end-stage), liver disease (including drug-induced liver injury, chronic hepatitis B and hepatitis C infection), gallbladder disease, coronary artery disease, myocardial infarction and ischaemia, coronary thrombosis, hemoglobinopathy, and pyoureter.
- **Drug Interactions**: 93 interactions were recorded. The one rated **Major** among those listed is **clarithromycin**. Many others are rated Moderate, including aprepitant, dexamethasone, cimetidine, cobicistat, clotrimazole, miconazole, eliglustat, naltrexone, rolapitant, deferasirox, promethazine and epoprostenol.

Product Information warnings and contraindications were not available in the compiled data. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for multiple endocrine neoplasia rests on a model score alone (L5), with no trials, no literature and no plausible mechanistic link to CCR5 antagonism. The data compiled also lacked label safety information and the original indication text.

**To proceed, the following is needed:**
- Mechanistic evidence linking CCR5 signalling to MEN pathogenesis, or preclinical studies testing maraviroc in MEN models
- Mechanism of action data and the registered indication for the Australian product
- Product Information warnings and contraindications, with review of the Major clarithromycin interaction and the liver, kidney and cardiovascular cautions
- Consideration of redirecting effort to HER2-positive breast carcinoma (CCL5/CCR5 and trastuzumab resistance), which is the most biologically grounded candidate and would first need preclinical validation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

