---
layout: default
title: Chlorpromazine
parent: Moderate Evidence (L3-L4)
nav_order: 156
evidence_level: L4
indication_count: 10
---

# Chlorpromazine
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

# Chlorpromazine: From Schizophrenia and Other Psychotic Disorders to Retinal Dystrophy

## One-Sentence Summary

Chlorpromazine is a long-established antipsychotic, originally used for schizophrenia and related psychotic and manic disorders.
The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**, but there are **0 clinical trials** and only **1 publication** (a 1967 report of phototoxic reactions, which is a safety signal rather than evidence of benefit).
The prediction is not supported by evidence and is best treated as a computational artefact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia and other psychotic disorders, manic bipolar affective disorder (the Australian licence text is blank, so these come from the knowledge graph) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Chlorpromazine is a phenothiazine antipsychotic that is generally known to act as a dopamine D2 and multi-receptor antagonist. Its efficacy in schizophrenia and other psychotic disorders is well established.

For retinal dystrophy, **no therapeutic mechanism is supported**. The only literature found describes phototoxic reactions to high-dose chlorpromazine and thioridazine. Chlorpromazine is known to cause pigmentary deposits in the retina and cornea at high doses, so it could worsen an existing retinal dystrophy. The high TxGNN score appears to reflect a graph association with the eye rather than a treatment rationale.

Other predictions in the model output were also reviewed. Most (congenital disorder of glycosylation, X-linked and syndromic myopia, hydranencephaly, polymicrogyria, Charcot-Marie-Tooth type 1G, atypical glycine encephalopathy) have no trials, no literature and no plausible mechanism. For myopia, dopamine antagonism is theoretically unfavourable.

The only prediction with strong biological plausibility is **early-onset schizophrenia** (score 99.47%, evidence level L4). It is essentially an extension of the existing schizophrenia indication rather than true repurposing. The retrieved literature is observational or pharmacogenetic, with no controlled efficacy data in children or adolescents, and newer antipsychotics are generally preferred in this population. It could be considered a research question separate from this report.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [5336672](https://pubmed.ncbi.nlm.nih.gov/5336672/) | 1967 | Review/case observation | JAMA | Phototoxic reactions induced by high doses of chlorpromazine and thioridazine. This is an adverse-effect report, not evidence of benefit. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1195X | Largactil | Injection containing chlorpromazine hydrochloride 50 mg in 2 mL | Not stated in the data compiled |

## Safety Considerations

**Contraindications (knowledge-graph associations, not label text):**
Associated conditions include:
- **Cardiac and haemodynamic:** long QT syndrome (including familial), torsades de pointes, orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy, myocardial infarction, coronary thrombosis, sudden cardiac arrest, heart conduction disease.
- **Haematological:** neutropenia, agranulocytosis, leukopenia, thrombocytopenia, anaemia (including macrocytic), haemoglobinopathy.
- **Neurological:** epilepsy, basal ganglia disease, focal hand dystonia, blepharospasm.
- **Other:** liver disease, gallbladder disease, hyperglycaemia, benign prostatic hyperplasia, substance abuse/dependence, female breast carcinoma, obesity disorders.

**Drug Interactions:** 100 interactions were recorded. Major-level interactions in the sample reviewed include **bupropion** and **morphine**. Moderate-level interactions include:
- antidiabetic agents (acarbose, metformin, pioglitazone, alogliptin, canagliflozin, chlorpropamide, albiglutide)
- anticholinergics (atropine, hyoscyamine, glycopyrronium)
- others (epinephrine, hydrocortisone, famotidine, amphotericin B, loperamide, lorcaserin, bisacodyl)

Retinal and corneal pigmentary deposits and phototoxicity at high doses are directly relevant to this predicted indication. For full warnings, please refer to the TGA-approved Product Information (PI).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials, the only literature describes harm to the eye and skin rather than benefit, and no therapeutic mechanism is supported. The high TxGNN score appears to reflect a graph association rather than a treatment rationale.

**To proceed, the following is needed:**
- Mechanism of action data (currently unavailable) and any preclinical evidence of benefit in retinal dystrophy
- Review of the PI warnings and contraindications, since this data is currently missing and blocks safety screening
- Assessment of ocular toxicity risk in patients with existing retinal disease
- Consideration of early-onset schizophrenia as a separate research question, with controlled paediatric and adolescent data and a safety review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

