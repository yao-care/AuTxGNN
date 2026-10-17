---
layout: default
title: Goserelin
parent: Model Prediction Only (L5)
nav_order: 344
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Goserelin: predicted new indication Amenorrhoea (evidence level L5). Approved use: Endometriosis"
monitor_inn: "Goserelin"
predicted_indications: ["amenorrhea (disease)", "renal hypoplasia (disease)", "renal hypoplasia, bilateral", "gelatinous drop-like corneal dystrophy", "duodenogastric reflux", "duodenal obstruction", "duodenal ulcer (disease)"]
---

# Goserelin
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

# Goserelin: From Endometriosis to Amenorrhoea

## One-Sentence Summary

Goserelin is a gonadotropin-releasing hormone (GnRH) agonist, originally used to treat endometriosis.
The TxGNN model predicts it may be effective for **Amenorrhoea** (as a deliberate, medically induced effect), with **1 clinical trial** (indirect evidence only) and **15 publications** currently supporting this direction.
Amenorrhoea is an expected pharmacodynamic effect of goserelin, so this is better treated as a research question than a new therapeutic mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Endometriosis (the ARTG entries in the data compiled for this report carry no approved indication text) |
| Predicted New Indication | Amenorrhoea |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 (as assigned in the data; the single Phase 3 trial is indirect and its status is unknown) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, goserelin is a GnRH agonist. Continuous administration desensitises pituitary GnRH receptors, suppressing LH and FSH release and lowering ovarian oestrogen production.

This produces a reversible, medically induced amenorrhoea (ovarian suppression). The same effect underlies its use in endometriosis, where lowering oestrogen reduces the activity of oestrogen-dependent ectopic tissue. It is also used in ovarian ablation for premenopausal breast cancer.

The prediction is therefore mechanistically coherent, but amenorrhoea here is a documented effect of treatment rather than a new disease target. Using it as a deliberate goal (for example, menstrual suppression, or ovarian protection during chemotherapy) is a separate clinical question that needs its own evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02132390](https://clinicaltrials.gov/study/NCT02132390) | Phase 3 | Unknown | 300 | Adjuvant toremifene with or without goserelin in premenopausal women with hormone receptor-positive breast cancer, with or without chemotherapy-induced amenorrhoea. The primary objective is oncologic outcome, so this is indirect evidence only. |

No ANZCTR identifiers were available in the data compiled for this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12488406](https://pubmed.ncbi.nlm.nih.gov/12488406/) | 2002 | RCT | J Clin Oncol | Goserelin versus CMF chemotherapy as adjuvant therapy in premenopausal node-positive breast cancer (ZEBRA study) |
| [14679153](https://pubmed.ncbi.nlm.nih.gov/14679153/) | 2003 | RCT | J Natl Cancer Inst | Chemotherapy followed by goserelin versus either alone in node-negative premenopausal breast cancer (IBCSG Trial VIII) |
| [17159194](https://pubmed.ncbi.nlm.nih.gov/17159194/) | 2007 | RCT (secondary analysis) | J Clin Oncol | Impact of chemotherapy, goserelin or both on amenorrhoea, hot flushes and quality of life |
| [8513962](https://pubmed.ncbi.nlm.nih.gov/8513962/) | 1993 | RCT | Fertil Steril | Goserelin versus low-dose oral contraceptive for pelvic pain in endometriosis |
| [28472240](https://pubmed.ncbi.nlm.nih.gov/28472240/) | 2017 | Meta-analysis/Review | Ann Oncol | OPTION trial: GnRH agonist for protection against chemotherapy-induced premature ovarian insufficiency |
| [25187267](https://pubmed.ncbi.nlm.nih.gov/25187267/) | 2015 | Cohort | Cancer Res Treat | Goserelin ovarian ablation improved survival in stage II/III hormone receptor-positive breast cancer without chemotherapy-induced amenorrhoea |
| [21325445](https://pubmed.ncbi.nlm.nih.gov/21325445/) | 2011 | Long-term follow-up | Ann Oncol | Long-term results of IBCSG Trial VIII (endocrine, chemotherapy and combined therapy) |
| [1533675](https://pubmed.ncbi.nlm.nih.gov/1533675/) | 1992 | Review | J R Army Med Corps | Therapeutic induction of amenorrhoea, including goserelin, in female military personnel |
| [12353820](https://pubmed.ncbi.nlm.nih.gov/12353820/) | 2002 | Review | Breast Cancer Res Treat | LHRH agonists in early breast cancer and the benefits of reversible ovarian ablation |
| [12734855](https://pubmed.ncbi.nlm.nih.gov/12734855/) | 2003 | Review | Br J Surg | Methods and relevance of ovarian ablation in adjuvant treatment of breast cancer |

Most of this literature concerns breast cancer, where amenorrhoea is a side effect or surrogate marker rather than the treatment target.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1454M | Zoladex Implant | Subcutaneous implant 3.6 mg (as acetate) in pre-filled injection syringe | Not stated in the compiled data |
| ARTG 9064C | ZolaCos CP 3.6/50 | Pack with 1 goserelin 3.6 mg subcutaneous implant and 28 bicalutamide 50 mg tablets | Not stated in the compiled data |

---

## Safety Considerations

- **Contraindication-related conditions (knowledge-graph associations, not label text):** hypertensive disorder, hypertension, hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease, obesity disorder, monogenic obesity, urinary tract obstruction.
- **Drug interactions:** 100 interactions were identified. Those listed here are examples from the 20 interactions shown.
  - **Major:** dolasetron.
  - **Moderate:** antidiabetic agents (acarbose, albiglutide, alogliptin, canagliflozin, chlorpropamide, dapagliflozin, dulaglutide, empagliflozin, glimepiride, linagliptin, metformin, saxagliptin), clarithromycin, famotidine, loperamide, palonosetron, and bowel preparations or laxatives (bisacodyl, picosulfuric acid, polyethylene glycol).
  - The prominence of antidiabetic agents is consistent with the glucose-tolerance concerns noted above.

Label warnings and contraindications were not available in the compiled data. Please refer to the TGA-approved Product Information (PI) for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Amenorrhoea is an expected pharmacological effect of goserelin, not a distinct disease indication. The only trial is an indirect, status-unknown breast cancer study, and the literature mostly addresses oncology contexts. The high TxGNN score reflects a graph-based association rather than direct evidence for a new therapeutic use.

**To proceed, the following is needed:**
- A clear definition of the intended use (for example, menstrual suppression or ovarian protection during chemotherapy) and the target population
- Direct clinical evidence for that use, such as randomised trials with amenorrhoea or ovarian function as the primary endpoint
- Approved indication text and PI safety information (warnings, contraindications) for the Australian products
- Mechanism of action data to complete the mechanistic analysis
- Review of the interaction profile, particularly with antidiabetic agents and QT-prolonging drugs, and of bone density and hypo-oestrogenic effects with longer-term use

---

### Other Predicted Indications (for reference)

- **Cervix endometriosis, endometriosis of the rectovaginal septum and vagina:** anatomical subtypes of the approved indication (L4). The mechanistic rationale is sound, but no site-specific trials or literature were retrieved. These are research questions.
- **Endometriosis in cutaneous scar:** a single case report (PMID 19753740) describes combined medical and surgical treatment (L4). Surgical excision remains the primary treatment.
- **Renal hypoplasia (including bilateral), gelatinous drop-like corneal dystrophy, duodenogastric reflux, duodenal obstruction and duodenal ulcer:** no plausible mechanistic link and no clinical evidence (L5). The recommendation for these is Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

