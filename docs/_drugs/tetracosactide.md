---
layout: default
title: Tetracosactide
parent: Model Prediction Only (L5)
nav_order: 715
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Tetracosactide: predicted new indication Top-ranked: familial adrenal hypoplasia with absent pituitary luteini… (evidence level L5). Approved use: Adrenocortical insufficiency"
monitor_inn: "Tetracosactide"
predicted_indications: ["familial adrenal hypoplasia with absent pituitary luteinizing hormone", "adrenomyodystrophy", "Congenital adrenal insuffiency with 46, XY sex reversal OR 46,XY disorder of sex development-adrenal insufficiency due to CYP11A1 deficiency", "46,XY disorder of sex development", "PAGOD syndrome", "inherited isolated adrenal insufficiency due to partial CYP11A1 deficiency", "IMAGe syndrome", "adrenal cortex disease", "familial glucocorticoid deficiency", "glucocorticoid deficiency"]
---

# Tetracosactide
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

## Tetracosactide: From Adrenocortical Insufficiency to Adrenal Cortex Disease
{: .text-alpha }

## One-Sentence Summary

Tetracosactide is a synthetic ACTH (1-24) analogue, originally used for adrenocortical insufficiency and Addison disease.
The TxGNN model's top-ranked prediction is **familial adrenal hypoplasia with absent pituitary luteinizing hormone**, but it has **no clinical trials and no publications**, and the mechanism argues against benefit. The best-supported candidate is **adrenal cortex disease**, with **0 clinical trials** and **10 publications**, only one of which suggests a possible therapeutic signal. This report therefore covers both.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Adrenocortical insufficiency; Addison disease (from the knowledge graph; no approved indication text is available for the ARTG entry) |
| Predicted New Indication | Top-ranked: familial adrenal hypoplasia with absent pituitary luteinizing hormone. Best-supported: adrenal cortex disease (rank 8) |
| TxGNN Prediction Score | 98.25% (rank 1); 92.85% (adrenal cortex disease) |
| Evidence Level | L5 for the rank 1 prediction; L4 for adrenal cortex disease |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold (rank 1 prediction); adrenal cortex disease is a research question only |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Tetracosactide is known to be an ACTH 1-24 analogue that stimulates the melanocortin 2 receptor (MC2R) on adrenocortical cells, driving cortisol and other adrenal steroid production.

**Rank 1 prediction (familial adrenal hypoplasia).** The model score is high, but the biology does not support it. In this type of adrenal hypoplasia (for example, NR0B1/DAX-1 related), adrenal cortical tissue is lost, so there is little tissue for ACTH stimulation to act on. At most, tetracosactide has diagnostic value here, not therapeutic value.

**Adrenal cortex disease (rank 8).** This is the most plausible link to the original indication. One 2014 study (PMID 24170102) reported improved residual adrenal function in autoimmune Addison disease after tetracosactide treatment. That is a possible therapeutic signal where some adrenal function remains. However, most of the other papers concern diagnostic testing (the Synacthen test), so much of this overlaps with the existing diagnostic use rather than representing new repurposing.

**Other predictions** (adrenomyodystrophy, CYP11A1 deficiency, 46,XY disorder of sex development, PAGOD syndrome, IMAGe syndrome, familial glucocorticoid deficiency, glucocorticoid deficiency) are model predictions only. In most of them ACTH is already elevated, there is a downstream enzymatic block, or the receptor system itself is defective (for example, MC2R or MRAP mutations), so an ACTH analogue is unlikely to help.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Publications for **adrenal cortex disease** (the only prediction with substantial literature):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24170102](https://pubmed.ncbi.nlm.nih.gov/24170102/) | 2014 | Clinical study (design not confirmed) | J Clin Endocrinol Metab | Residual adrenal function in autoimmune Addison disease improved after tetracosactide treatment; the only possible therapeutic signal |
| [35699085](https://pubmed.ncbi.nlm.nih.gov/35699085/) | 2022 | Cohort | Clin Exp Rheumatol | Impaired adrenal reserve in rheumatic patients who relapse on glucocorticoid tapering |
| [19404783](https://pubmed.ncbi.nlm.nih.gov/19404783/) | 2009 | Cohort | Neurocrit Care | Low-dose vs high-dose Synacthen testing in traumatic brain injury (diagnostic) |
| [28132968](https://pubmed.ncbi.nlm.nih.gov/28132968/) | 2017 | Clinical study | Endocr J | Tetracosactide-stimulated adrenal vein sampling in primary aldosteronism (diagnostic) |
| [22677116](https://pubmed.ncbi.nlm.nih.gov/22677116/) | 2013 | Case report | J Crohns Colitis | Autoimmune polyglandular syndrome type 2 with alopecia universalis and Crohn's disease |
| [6294170](https://pubmed.ncbi.nlm.nih.gov/6294170/) | 1982 | Case report | J Endocrinol Invest | Primary hypothyroidism with secondary adrenocortical insufficiency; tetracosactide used diagnostically |
| [9686000](https://pubmed.ncbi.nlm.nih.gov/9686000/) | 1997 | Case report | Ann Endocrinol | Pre-Cushing syndrome: 17-hydroxyprogesterone response to ACTH analogue stimulation |

The remaining three papers (an in vitro l-lysine/serotonin aldosterone study, a neonatal Netherton syndrome case, and canine and mouse cell-line studies) are not relevant to a therapeutic use in humans.

For **glucocorticoid deficiency** (rank 10), the only paper is a 2011 review on late-onset congenital adrenal hyperplasia due to 21-hydroxylase deficiency ([PMID 21672447](https://pubmed.ncbi.nlm.nih.gov/21672447/)). It describes ACTH stimulation as diagnostic and does not show therapeutic benefit.

For the rank 1 prediction and the other predictions, currently no related literature is available.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 2832C | Synacthen Depot 1 mg/1 mL | Compound depot injection 1 mg in 1 mL | Not available in the data compiled |

The product is a single-ingredient injectable. No cancelled entries were found.

---

## Safety Considerations

**Drug Interactions** (100 interactions were identified; 20 are shown in the data compiled, mostly Moderate):
- **Major:** Bupropion
- **Moderate (glucose-lowering agents):** acarbose, albiglutide, alogliptin, metformin, canagliflozin, chlorpropamide, acetohexamide, dapagliflozin, dulaglutide, empagliflozin, ertugliflozin, exenatide
- **Moderate (other):** amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms), bisacodyl, picosulfuric acid, castor oil

Corticosteroid stimulation can raise blood glucose, which may account for the antidiabetic interactions. This is an inference, not stated in the data compiled.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications, which were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (familial adrenal hypoplasia) is supported by model score alone, with no trials or literature. Its mechanism argues against benefit because the adrenal tissue is lacking.
- Adrenal cortex disease has some literature, including one possible therapeutic signal in autoimmune Addison disease (PMID 24170102). It is best treated as a research question, since most of the evidence reflects the existing diagnostic use.

**To proceed, the following is needed:**
- Full review of PMID 24170102 to confirm its design, sample size and outcomes
- A prospective, registered trial in autoimmune Addison disease with residual adrenal function, if the signal holds up
- Mechanism of action data for tetracosactide
- TGA Product Information warnings and contraindications for Synacthen Depot, plus the approved indication text for ARTG 2832C
- Review of the glucose-lowering and bupropion interactions before any new use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

