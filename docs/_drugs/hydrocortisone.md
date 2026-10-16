---
layout: default
title: Hydrocortisone
parent: Model Prediction Only (L5)
nav_order: 353
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Hydrocortisone: predicted new indication Alopecia areata (evidence level L5). Approved use: Adrenocortical insufficiency, autoimmune disease, Crohn disease…"
monitor_inn: "Hydrocortisone"
predicted_indications: ["alopecia areata", "alopecia mucinosa", "telogen effluvium", "Quinquaud's folliculitis decalvans", "alopecia antibody deficiency", "hereditary hypotrichosis with recurrent skin vesicles", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "atrichia with papular lesions", "alopecia universalis onychodystrophy vitiligo", "idiopathic steroid-sensitive nephrotic syndrome"]
---

# Hydrocortisone
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

# Hydrocortisone: From Autoimmune and Endocrine Conditions to Alopecia Areata

## One-Sentence Summary

Hydrocortisone is a glucocorticoid originally used for conditions such as adrenocortical insufficiency, autoimmune disease, Crohn disease and acute lymphoblastic leukaemia.
The TxGNN model predicts it may be effective for **alopecia areata**,
with **1 clinical trial** (a Phase 3 RCT in which hydrocortisone was the low-potency comparator) and **a small number of relevant publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Adrenocortical insufficiency, autoimmune disease, Crohn disease, acute lymphoblastic leukaemia and others (the ARTG entry has no indication text on file, so these come from the TxGNN knowledge graph) |
| Predicted New Indication | Alopecia areata |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 (see note below) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

*Note on evidence level:* The pipeline assigned L1, but the single Phase 3 trial used hydrocortisone as the comparator rather than the test drug, and it favoured clobetasol. Strictly, this is closer to L2–L3 for hydrocortisone's own efficacy, and the decision below reflects that.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, hydrocortisone is a glucocorticoid with anti-inflammatory and immunosuppressive effects, and its efficacy in autoimmune and inflammatory conditions is well established.

Alopecia areata is a T-cell-mediated autoimmune disease in which the immune system attacks hair follicles. Corticosteroids are therefore mechanistically plausible. Topical and intralesional steroids are already used in practice.

However, hydrocortisone is a low-potency steroid. In the available RCT it was the comparator against clobetasol propionate (a super-potent steroid), and the published result favoured clobetasol. The evidence mainly supports a steroid class effect, not hydrocortisone's own efficacy. Other predicted indications (for example alopecia mucinosa, telogen effluvium and folliculitis decalvans) have no hydrocortisone-specific clinical evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | Completed | 41 | Clobetasol propionate 0.05% cream vs hydrocortisone 1% cream in children with alopecia areata (2002–2003). Small trial; the published result favoured clobetasol, so it does not clearly show hydrocortisone benefit. |

No ANZCTR trial identifiers were available.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24226568](https://pubmed.ncbi.nlm.nih.gov/24226568/) | 2014 | RCT | JAMA Dermatology | Clobetasol 0.05% vs hydrocortisone 1% for alopecia areata in children; the randomised comparison of the two topical steroids. |
| [15692503](https://pubmed.ncbi.nlm.nih.gov/15692503/) | 2005 | Case report | J Am Acad Dermatol | Four cases of congenital alopecia areata, treated with minoxidil and a range of topical agents; not hydrocortisone-specific. |
| [19289325](https://pubmed.ncbi.nlm.nih.gov/19289325/) | 2009 | Case report | Endocr Pract | Autoimmune polyglandular syndrome type 3 with alopecia universalis and isolated corticotropin deficiency; indirect. |
| [13368875](https://pubmed.ncbi.nlm.nih.gov/13368875/) | 1956 | Case series | Medical Times | Historical report on cortisone, hydrocortisone and analogues in alopecia areata. |
| [13610145](https://pubmed.ncbi.nlm.nih.gov/13610145/) | 1958 | Historical report | Der Hautarzt | Hair regrowth in alopecia areata after intracutaneous hydrocortisone injection (no abstract available). |
| [13525930](https://pubmed.ncbi.nlm.nih.gov/13525930/) | 1958 | Review | J Med Soc N J | Overview of alopecia areata and common scalp problems. |

Several further historical (1955–1973) reports describe intralesional hydrocortisone for alopecia areata, but they have no abstracts and no formal classification. The remaining retrieved publications were off-target (animal models, veterinary, trichotillomania or adverse events with other steroids) and are not listed.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13863P | Hydrocortisone Viatris 4 | Tablet 4 mg (oral) | Not available in the data compiled for this report |

The only registered product is an oral tablet. The supporting trial used a topical 1% cream, so route compatibility has not been established.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

- **Knowledge-graph contraindications** (not label text): hypertension, epilepsy, gastric ulcer, kidney disease, liver disease, gallbladder disease, hyperglycaemia, herpes simplex keratitis, measles, common wart, anogenital HPV infection, and various pituitary/growth hormone deficiency disorders.
- **Drug interactions** (100 recorded; examples from the retrieved subset):
  - **Major:** adalimumab.
  - **Moderate:** zidovudine, isotretinoin, acarbose, acebutolol, acetazolamide, ketorolac, ibuprofen, nifedipine, ethinylestradiol, albiglutide, aldesleukin, alemtuzumab, and certain live or inactivated vaccines (e.g. tetanus toxoid, adenovirus type 4).
  - **Minor:** formoterol, salbutamol.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only trial places hydrocortisone as the weaker comparator, and its published result favoured clobetasol. The supporting evidence is a class-level steroid rationale. Safety screening also cannot proceed without label data, and the only ARTG product is an oral tablet that does not match the topical use studied.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) for hydrocortisone
- Product Information warnings and contraindications for the registered product
- Evidence that hydrocortisone itself, not a more potent steroid, is effective in alopecia areata (for example a placebo-controlled trial)
- Assessment of route and formulation (topical or intralesional) and whether an Australian product is available
- Safety monitoring plan, including interactions and the knowledge-graph contraindications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

