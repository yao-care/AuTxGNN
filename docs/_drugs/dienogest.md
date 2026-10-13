---
layout: default
title: Dienogest
parent: Moderate Evidence (L3-L4)
nav_order: 215
evidence_level: L4
indication_count: 10
---

# Dienogest
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Dienogest: From Endometriosis (Presumed) to Amenorrhoea

## One-Sentence Summary

Dienogest is an oral progestin marketed in Australia as a 2 mg tablet (Visanne). The data compiled for this report did not include approved indication text, and the literature points to endometriosis as its established use. The TxGNN model predicts it may be effective for **amenorrhoea**, but there are **0 registered clinical trials** and only **7 publications**, none of which directly tests dienogest as a treatment for amenorrhoea.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (literature describes endometriosis as the approved use) |
| Predicted New Indication | Amenorrhoea |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the literature, dienogest is a fourth-generation progestin with antiproliferative, anti-ovulatory and endometrial-decidualising activity. It suppresses ovarian oestradiol production.

Amenorrhoea is a commonly reported effect of dienogest therapy in endometriosis. That means the link to this prediction is largely an **effect or bleeding-pattern observation**, not a therapeutic target. Dienogest tends to *cause* amenorrhoea rather than treat it. The existing literature concerns endometriosis, adverse-effect profiling and case reports, so the high model score is not backed by direct clinical evidence. The prediction should be treated as a research question, not a treatment opportunity.

Other predicted indications (primary ovarian failure, hypogonadotropic hypogonadism, isolated growth hormone deficiency, chromosomal disorders and others) have no clinical or literature support. They appear to reflect network proximity in the knowledge graph. Mechanistically, suppressing the ovarian and gonadotropin axis would be unlikely to help in several of them.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39090694](https://pubmed.ncbi.nlm.nih.gov/39090694/) | 2024 | Systematic review / Bayesian meta-analysis | BMC Pharmacol Toxicol | Summarises adverse events and their prevalence with dienogest in endometriosis and adenomyosis |
| [29161960](https://pubmed.ncbi.nlm.nih.gov/29161960/) | 2018 | Retrospective cohort (n=514) | Reprod Sci | Long-term (>12 months) dienogest 2 mg daily in ovarian endometrioma: efficacy, safety and recurrence |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Review | Rev Endocr Metab Disord | Endocrine background of hormonal treatments for endometriosis |
| [41329046](https://pubmed.ncbi.nlm.nih.gov/41329046/) | 2026 | Clinical/pharmacodynamic study | Eur J Contracept Reprod Health Care | Further evidence for 2 mg dienogest in endometriosis; amenorrhoea noted as a treatment objective |
| [42438810](https://pubmed.ncbi.nlm.nih.gov/42438810/) | 2026 | Case report | JCEM Case Reports | Primary hyperparathyroidism unmasked after starting dienogest for menorrhagia |
| [34918698](https://pubmed.ncbi.nlm.nih.gov/34918698/) | 2021 | Case report | Medicine | Ovarian granulosa cell tumour in a patient with PCOS (indirect relevance) |
| [40543564](https://pubmed.ncbi.nlm.nih.gov/40543564/) | 2025 | Review / imaging | J Pediatr Adolesc Gynecol | Advanced visualisation of Müllerian anomalies (indirect relevance) |

No publication evaluates dienogest as a treatment for amenorrhoea.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14667Y | Visanne | Tablet 2 mg (oral) | Not available in the data compiled for this report |

## Safety Considerations

- **Drug Interactions**: 37 interactions were identified in total. Major-level interactions in the data include sugammadex, griseofulvin, bexarotene, brigatinib, dabrafenib and encorafenib. Moderate-level interactions include linaclotide, metreleptin, prucalopride, miltefosine, adalimumab, anakinra, certolizumab pegol and cladribine, among others. Ethanol is listed as minor.
- **Knowledge-graph contraindication signals** (from a drug-disease network, not label text): hypertension, epilepsy, liver disease, gallbladder disease, kidney disease, porphyria, diabetes mellitus, diabetic ketoacidosis, hypertriglyceridaemia, hypothyroidism, systemic lupus erythematosus, asthma, hypercalcaemia, female breast carcinoma and thrombophlebitis. These need verification against the Product Information.
- **Case-level signal**: one 2026 case report describes primary hyperparathyroidism emerging after dienogest, raising a possible calcium-homeostasis question.

Please refer to the TGA-approved Product Information (PI) for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high model score (99.71%) is not supported by direct evidence. Amenorrhoea is a recognised effect of dienogest rather than a condition it treats, and there are no registered trials. Evidence is at L4 (mechanistic and indirect literature only).

**To proceed, the following is needed:**
- The TGA-approved Product Information, including the approved indication, warnings and contraindications
- Detailed mechanism of action data
- A clear clinical rationale for whether a drug that induces amenorrhoea could treat any amenorrhoea subtype
- Reframing the question, for example towards specific bleeding disorders, before any trial design
- Review of the knowledge-graph contraindication signals and the major drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

