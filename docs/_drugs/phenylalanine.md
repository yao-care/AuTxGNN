---
layout: default
title: Phenylalanine
parent: Model Prediction Only (L5)
nav_order: 570
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Phenylalanine: predicted new indication Sclerosing cholangitis (evidence level L5). Approved use: Not recorded in the data compiled for this report"
---

# Phenylalanine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Phenylalanine: From Unspecified Original Indication to Sclerosing Cholangitis

## One-Sentence Summary

Phenylalanine is an essential aromatic amino acid, supplied in Australia as oral powder sachets, and no approved indication text is recorded for it in the data compiled for this report.
The TxGNN model predicts it may be effective for **sclerosing cholangitis**, but this rests on a network-based score alone, with **0 clinical trials** and **3 publications** that do not show a therapeutic effect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the data compiled for this report |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Phenylalanine is a dietary amino acid and a precursor of tyrosine. The data compiled for this report do not record an approved indication, so the link between an original use and the predicted one cannot be assessed.

The three publications retrieved do not support a therapeutic role:

- One cohort study examined plasma tyrosine, a downstream amino acid, and fatigue in primary biliary cirrhosis and primary sclerosing cholangitis. This is an association, not a treatment effect.
- One study profiled the serum metabolic signature of cholangiocarcinoma. This is a biomarker study in a different disease.
- One paper described a radioimmunoassay for a formylated bacterial peptide (fMLP), which is a different compound from L-phenylalanine used as a drug.

Aromatic amino acid metabolism may be altered in cholestatic liver disease, but that is a disease-state observation and not a rationale for supplementation. The high score most likely reflects network proximity rather than a biological mechanism.

A second prediction, congenital prothrombin deficiency (score 99.26%), has no clinical trials or literature. It is a monogenic coagulation factor II disorder treated with replacement therapy, and there is no known mechanism by which phenylalanine would correct it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15790420](https://pubmed.ncbi.nlm.nih.gov/15790420/) | 2005 | Cohort | BMC Gastroenterology | Examined the relation between plasma tyrosine and fatigue in primary biliary cirrhosis and primary sclerosing cholangitis; an association with a downstream amino acid, not a treatment effect |
| [32025163](https://pubmed.ncbi.nlm.nih.gov/32025163/) | 2020 | Cohort | Journal of Clinical and Experimental Hepatology | Serum metabolic signature of cholangiocarcinoma in a UK cohort; biomarker study in a different disease |
| [2103382](https://pubmed.ncbi.nlm.nih.gov/2103382/) | 1990 | Assay development | Journal of Gastroenterology and Hepatology | Radioimmunoassay for a formylated bacterial peptide (fMLP) and its enterohepatic circulation; not about L-phenylalanine as a drug |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 9384X | Phenylalanine 50 | Oral powder sachets, 4 g containing 50 mg phenylalanine, 30 | Not recorded |
| ARTG 11832R | TYR Sphere20 | Oral powder sachets, 35 g, 30 | Not recorded |

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (drug-disease links from the TxGNN knowledge graph, not product label text):
  - Phenylketonuria and other disorders of phenylalanine metabolism
  - Kidney disease, including chronic kidney disease, chronic renal failure, end stage renal failure, nephrolithiasis and nephrocalcinosis
  - Heart and cardiovascular disease, ventricular fibrillation and digitalis poisoning
  - Hypercalcaemia-related conditions, including sarcoidosis and humoral hypercalcaemia of malignancy
  - Phosphorus metabolism disease, acute urate nephropathy and pyoureter

Please refer to the TGA-approved Product Information (PI) for label warnings, contraindications and drug interactions, as none were available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but it is a network-based prediction only, with no clinical trials and no literature showing that phenylalanine treats sclerosing cholangitis. No plausible therapeutic mechanism is established, and the knowledge graph flags several relevant contraindications, including kidney and cardiovascular disease.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) and a plausible rationale linking phenylalanine to sclerosing cholangitis
- Approved indication and label information for both ARTG entries, including PI warnings and contraindications
- Preclinical or clinical evidence of a therapeutic effect, beyond metabolic marker studies
- A safety assessment for patients with liver disease, who may also have renal or cardiovascular comorbidities
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

