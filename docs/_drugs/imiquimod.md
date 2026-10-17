---
layout: default
title: Imiquimod
parent: Model Prediction Only (L5)
nav_order: 371
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Imiquimod: predicted new indication Pre-malignant neoplasm (evidence level L5). Approved use: Common wart, anogenital HPV infection…"
monitor_inn: "Imiquimod"
predicted_indications: ["benign neoplasm of buccal mucosa", "cervical neuroblastoma", "odontogenic cyst", "benign neoplasm of tongue", "nasopharyngeal teratoma", "cystic neoplasm", "inner ear neoplasm", "neoplasm of major salivary gland", "schwannoma of jugular foramen"]
---

# Imiquimod
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

# Imiquimod: From Actinic Keratosis and HPV-Related Skin Lesions to Pre-malignant Neoplasm

## One-Sentence Summary

Imiquimod is a topical immune response modifier, originally used for skin conditions such as actinic keratosis, anogenital warts and superficial basal cell carcinoma.
The TxGNN model predicts it may be effective for **pre-malignant neoplasm**, with **2 clinical trials** and **9 publications** currently supporting this direction.
Most of this evidence comes from labelled skin uses or small, underpowered studies, so the extension to other pre-malignant sites (cervical, vulval, anal) is only partly supported.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Common wart, anogenital HPV infection, superficial multifocal basal cell carcinoma, actinic keratosis and related skin conditions (from the knowledge graph; the ARTG entry has no indication text) |
| Predicted New Indication | Pre-malignant neoplasm |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 (see note below) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

*Evidence level note:* Two Phase 3 trials are registered, but one is a small single-arm study in actinic keratosis (already a labelled use) and the other was terminated after 9 participants. Neither is a completed, adequately powered Phase 3 RCT. A strict reading of the rules therefore gives L2 or lower, rather than the L1 listed in the source scoring. The recommendation is kept at Proceed with Guardrails.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Imiquimod is, however, a well-known Toll-like receptor 7 (TLR7) agonist. It triggers local release of type I interferon and pro-inflammatory cytokines and activates cell-mediated immunity. This is a plausible way to clear dysplastic and pre-malignant lesions.

Many of the original indications are HPV-driven or sun-induced skin lesions. These include warts, anogenital HPV infection and actinic keratosis. Pre-malignant lesions at other sites, such as cervical, vulval and anal intraepithelial neoplasia, share the same HPV-related biology. Actinic keratosis, itself a pre-malignant lesion, is already an established use. The prediction is therefore best read as an extension of a known mechanism to related lesions.

The other nine predicted indications are much weaker. Most have no trials and little or no relevant literature, and several rest on computational prediction alone (see the Conclusion).

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Phase 3 | Completed | 20 | Open-label, single-arm study of imiquimod 5% cream, 3 days per week for 1 or 2 cycles, in actinic keratoses on the head. It assessed how long the effect lasts. Small and supportive only. |
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Phase 3 | Terminated | 9 | Randomised trial of topical imiquimod versus standard excision (LLETZ) for high-grade cervical intraepithelial neoplasia. Terminated with only 9 participants, so no efficacy conclusion can be drawn. |

No ANZCTR identifiers were found in the data compiled for this report.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Cochrane systematic review | Cochrane Database Syst Rev | Interventions for anal canal intraepithelial neoplasia, a pre-malignant HPV-associated condition. |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Cochrane systematic review | Cochrane Database Syst Rev | Medical interventions for high-grade vulval intraepithelial neoplasia, which may progress to invasive disease. |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Review | Int J Mol Sci | Combined treatments with photodynamic therapy for non-melanoma skin cancer. |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Review | Semin Cutan Med Surg | Topical treatments for non-melanoma skin cancer and precursor lesions, including imiquimod. |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Review | Skin Therapy Lett | Current management of actinic keratoses, a pre-malignant lesion that can progress to squamous cell carcinoma. |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Case report | Int J STD AIDS | Successful imiquimod 5% treatment of high-grade vulval intra-epithelial neoplasia in a renal transplant recipient. |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Case report | Int J STD AIDS | Clearance of bowenoid papulosis of the penis with imiquimod 5% cream. |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Preclinical (rat) | Urol Oncol | Pharmacokinetics of investigational TLR7 agonists for bladder cancer. Not direct evidence for imiquimod. |
| [18931984](https://pubmed.ncbi.nlm.nih.gov/18931984/) | 2008 | Imaging case study | Hautarzt | Optical coherence tomography imaging of actinic porokeratosis. Not drug-efficacy evidence. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10106X | Aldara Pump | Cream, 50 mg per g, 2 g, 2 | Indication text not available in the data compiled for this report |

## Cytotoxicity

Imiquimod is a topical immune response modifier, not a conventional cytotoxic agent. Please refer to the Product Information (PI) warnings and precautions for any handling and monitoring requirements.

## Safety Considerations

- **Contraindication-related conditions (from knowledge graph, not label text):** photosensitivity disease, photoparoxysmal response, sunburn, autoimmune disease and graft versus host disease. These should be checked against the PI before any use.
- **Drug Interactions:** 59 potential interactions were identified, but none has an assigned severity level. Examples include pantoprazole, warfarin, clopidogrel, prednisone, prednisolone, budesonide, hydroxychloroquine and simvastatin. These are unverified and need clinical review.
- **Literature safety signals:** Case reports describe malignant conversion of oral papillomatosis during imiquimod treatment, erythema multiforme in a patient with Gorlin syndrome, and lichen planopilaris after imiquimod use. These relate to other predicted indications but are relevant to off-label use generally.

Warnings and contraindications from the TGA-approved Product Information (PI) were not available. Please refer to the PI for full safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is plausible and imiquimod is already marketed in Australia, with actinic keratosis as an established use. However, the trial evidence for new pre-malignant sites is thin: one small single-arm study and one terminated trial with 9 participants. Support for cervical, vulval and anal lesions rests mainly on reviews and case reports.

**To proceed, the following is needed:**
- Review of the TGA Product Information for warnings, contraindications and approved indications. The ARTG entry in the data compiled for this report has no indication text.
- Mechanism of action data from DrugBank.
- Adequately powered randomised trials in specific sites such as high-grade vulval or anal intraepithelial neoplasia.
- Clinical review of the 59 unclassified drug interactions.
- A monitoring plan for patients with autoimmune disease, transplant recipients and those with photosensitivity.

**Other predicted indications (not recommended at this time):**
- **Benign neoplasm of buccal mucosa (L4, Research Question):** no registered trials. Support comes from reviews, animal models and case reports, with safety concerns about off-label oral use.
- **Odontogenic cyst, cystic neoplasm, benign neoplasm of tongue, inner ear neoplasm, cervical neuroblastoma, nasopharyngeal teratoma, major salivary gland neoplasm and jugular foramen schwannoma (Hold):** no clinical evidence, or only indirect or irrelevant publications. Several of these sites are also not accessible to a topical cream.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

