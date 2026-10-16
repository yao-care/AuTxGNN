---
layout: default
title: Probenecid
parent: Moderate Evidence (L3-L4)
nav_order: 604
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Probenecid: predicted new indication Renal hypouricaemia (evidence level L4). Approved use: Gout"
---

# Probenecid
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

# Probenecid: From Gout to Renal Hypouricaemia

## One-Sentence Summary

Probenecid is a uricosuric drug originally used to treat gout and hyperuricaemia.
The TxGNN model predicts it may be effective for **renal hypouricaemia**, but there are **no registered clinical trials** and **20 publications** that only describe the disease, with none reporting probenecid as a treatment.
The mechanistic review suggests the prediction is a pharmacological association and not a genuine therapeutic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout; hyperuricaemia (from the TxGNN knowledge graph, as no approved indication text is available for the Australian entry) |
| Predicted New Indication | Renal hypouricaemia |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, probenecid inhibits URAT1 (SLC22A12) and other renal organic anion transporters. This increases urinary uric acid excretion and lowers serum urate, which is the basis of its use in gout.

The predicted condition runs in the opposite direction. Hereditary renal hypouricaemia is caused mainly by loss-of-function mutations in URAT1 (or GLUT9), which already cause excessive urate excretion and low serum urate. Probenecid would be expected to further lower serum urate and worsen the underlying defect, not correct it.

The high TxGNN score most likely reflects a shared transporter target and disease neighbourhood in the knowledge graph. The retrieved literature describes the disease and its genetics, and does not report probenecid as a treatment. Probenecid is more plausibly useful as a **diagnostic or mechanistic probe** (for example, in probenecid and pyrazinamide tests that characterise urate transport defects) than as therapy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The publications below concern renal hypouricaemia. None is a randomised trial of probenecid as treatment. Several use probenecid only as a diagnostic challenge.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Cohort/Genetic analysis | J Am Soc Nephrol | SLC22A12 (URAT1) sequencing in 32 patients with idiopathic renal hypouricaemia, linking genotype to urate excretion |
| [16678460](https://pubmed.ncbi.nlm.nih.gov/16678460/) | 2006 | Review | Mol Genet Metab | Hereditary renal hypouricaemia is mostly caused by loss-of-function SLC22A12 mutations |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clin Rheumatol | Narrative review of the causes and clinical approach to hypouricaemia for rheumatologists |
| [7771493](https://pubmed.ncbi.nlm.nih.gov/7771493/) | 1995 | Review/Case report | Am J Kidney Dis | Prevention of exercise-induced acute renal failure in renal hypouricaemia, with literature review |
| [8976099](https://pubmed.ncbi.nlm.nih.gov/8976099/) | 1996 | Review | Nihon Rinsho | Concept and classification of urate metabolism abnormalities |
| [854144](https://pubmed.ncbi.nlm.nih.gov/854144/) | 1977 | Case report | Nephron | Familial hypouricaemia with an attenuated uric acid clearance response to probenecid and pyrazinamide (diagnostic use) |
| [2709741](https://pubmed.ncbi.nlm.nih.gov/2709741/) | 1989 | Case report | Klin Wochenschr | Acute renal failure from uric acid nephropathy in renal hypouricaemia; urate clearance enhanced by probenecid |
| [9583212](https://pubmed.ncbi.nlm.nih.gov/9583212/) | 1998 | Case report | Acta Paediatr Jpn | Exercise-induced acute renal failure in a girl with renal hypouricaemia |
| [8302413](https://pubmed.ncbi.nlm.nih.gov/8302413/) | 1993 | Case report | Nephron | Hypouricaemia with urolithiasis; probenecid markedly increased urate clearance |
| [14747372](https://pubmed.ncbi.nlm.nih.gov/14747372/) | 2004 | Preclinical | J Am Soc Nephrol | Function and localisation of URAT1 in mouse kidney |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13942T | Pro-Cid | Tablet 500 mg (oral) | Indication text not available in the data compiled for this report |

---

## Safety Considerations

Product Information warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for full safety information.

**Contraindication-related associations (from the TxGNN knowledge graph, not label text):**
- Liver failure, kidney disease and impaired renal function
- Blood disorders, including thrombocytopenia, leukopenia, agranulocytosis and neutropenia (including congenital forms)
- Peptic ulcer disease
- Muscle disorders, including myopathy and rhabdomyolysis
- Diarrhoeal disease, including *Clostridium difficile* colitis

**Drug Interactions** (71 interactions recorded; main examples):
- **Major:** phenylbutyric acid, glycerol phenylbutyrate
- **Moderate:** acetylsalicylic acid (aspirin), and sulfonylurea or glinide antidiabetic drugs (chlorpropamide, glimepiride, glipizide, glyburide, tolazamide, tolbutamide, acetohexamide, repaglinide, nateglinide)
- **Minor:** famotidine, amoxicillin, levofloxacin, eluxadoline

**Clinical relevance of the prediction:** in renal hypouricaemia, probenecid could worsen urinary urate loss. This raises concern about urolithiasis and exercise-induced acute renal failure, both described in these patients.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone. There are no clinical trials, and the literature does not support probenecid as a treatment. The mechanism points in the wrong direction, because probenecid increases urate excretion in a condition already defined by excessive urate excretion. The other predicted indications (Lesch-Nyhan syndrome, partial HPRT deficiency, cholelithiasis, liver-related conditions and phenylalanine metabolism disorders) are also at L4–L5 with no supportive clinical evidence, and are all on Hold.

**To proceed, the following is needed:**
- Review of the TGA-approved Product Information for warnings, contraindications and the approved indication
- Detailed mechanism of action data (MOA)
- Evidence of therapeutic benefit, or a clear rationale for a diagnostic-only role, which would need a different regulatory pathway
- A safety assessment covering the risk of worsened urate loss, urolithiasis and acute kidney injury
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

