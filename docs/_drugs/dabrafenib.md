---
layout: default
title: Dabrafenib
parent: Model Prediction Only (L5)
nav_order: 193
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Dabrafenib: predicted new indication Non-cutaneous melanoma (evidence level L5). Approved use: Metastatic melanoma"
---

# Dabrafenib
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

# Dabrafenib: From Metastatic Melanoma to Non-Cutaneous Melanoma

## One-Sentence Summary

Dabrafenib is an oral BRAF inhibitor, originally used to treat metastatic melanoma.
The TxGNN model predicts it may be effective for **non-cutaneous melanoma** (the highest-ranked prediction with clinical trial support), with **9 retrieved clinical trials** (mostly pan-melanoma or tumour-agnostic designs) and no publications specific to this subtype.
Evidence is partial and extrapolated from cutaneous melanoma.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic melanoma (the ARTG entry carries no indication text) |
| Predicted New Indication | Non-cutaneous melanoma (see note below) |
| TxGNN Prediction Score | 98.48% |
| Evidence Level | L2 (see note below) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

**Note on selection:** The top-ranked TxGNN prediction is choroideremia (98.63%), but it has no trials or literature and no plausible BRAF/MAPK rationale. It is most likely a knowledge-graph artefact, so this report focuses on non-cutaneous melanoma, the highest-ranked prediction with a credible mechanism and trial evidence. The L2 grade is the pipeline's assessment. No Phase 3 RCT is specific to this subtype, and no trial was confirmed as a completed Phase 2/3 RCT in non-cutaneous melanoma, so the grade should be read cautiously.

Other predictions reviewed:

| Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|------|------|------|
| Choroideremia | 98.63% | L5 | Hold |
| Epithelioid cell melanoma | 98.44% | L4 | Research question |
| Eyelid melanoma | 98.41% | L4 | Research question |
| Scrotum melanoma | 98.28% | L4 | Research question |
| Choroidal dystrophy, central areolar | 98.27% | L5 | Hold |
| Amyotrophic lateral sclerosis | 98.26% | L5 | Hold |
| Bilateral parasagittal parieto-occipital polymicrogyria | 98.21% | L5 | Hold |
| Amelanotic skin melanoma | 98.09% | L3 | Proceed with Guardrails |
| Nodular malignant melanoma | 98.09% | L3 | Proceed with Guardrails |

The non-melanoma predictions (choroideremia, central areolar choroidal dystrophy, ALS, polymicrogyria) are inherited or developmental disorders with no evident BRAF-pathway link. They should be treated as computational artefacts.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, dabrafenib inhibits mutant BRAF kinase (for example V600E/K) in the MAPK pathway. Its efficacy in BRAF V600-mutant metastatic melanoma is established, usually in combination with the MEK inhibitor trametinib.

Non-cutaneous melanomas (mucosal, conjunctival and similar) are also driven by MAPK signalling, but BRAF mutations occur less often than in cutaneous melanoma. Benefit is therefore expected mainly in BRAF V600-mutant tumours and would need biomarker selection.

The same logic applies to the melanoma subtypes with literature support (epithelioid cell, eyelid/conjunctival, scrotal, amelanotic and nodular melanoma). Evidence for these subtypes is mostly case reports and reviews. Amelanotic and nodular melanoma are cutaneous variants that fall largely within the existing approved indication.

## Clinical Trial Evidence

Trials retrieved for non-cutaneous melanoma. Many are pan-melanoma or tumour-agnostic studies, so direct evidence is partial.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04439292](https://clinicaltrials.gov/study/NCT04439292) | Phase 2 | Active, not recruiting | 44 | NCI-MATCH Subprotocol H: dabrafenib + trametinib in BRAF V600-mutant tumours (excluding melanoma, thyroid, colorectal and NSCLC); tumour-agnostic design. Results not provided |
| [NCT02872259](https://clinicaltrials.gov/study/NCT02872259) | Phase 1/2 | Completed | 74 | BGB324 combined with pembrolizumab or dabrafenib/trametinib versus standard treatment alone in advanced melanoma |
| [NCT07440290](https://clinicaltrials.gov/study/NCT07440290) | Phase 2/3 | Recruiting | 30 | DETERMINE platform, Arm 07: dabrafenib + trametinib in BRAF V600-mutant cancers (adult, paediatric and TYA); results not yet available |
| [NCT04418167](https://clinicaltrials.gov/study/NCT04418167) | Phase 1 | Suspended | 71 | ERK1/2 inhibitor JSI-1187 alone or with dabrafenib in MAPK-mutant solid tumours |
| [NCT02410863](https://clinicaltrials.gov/study/NCT02410863) | Phase 2 | Terminated | 10 | Biopsy-driven optimisation of targeted therapy in BRAF-mutant metastatic melanoma; limited information because of early termination |
| [NCT03340506](https://clinicaltrials.gov/study/NCT03340506) | Phase 4 | Recruiting | 100 | Roll-over study for long-term safety of dabrafenib and/or trametinib; useful for safety rather than efficacy |
| [NCT03944356](https://clinicaltrials.gov/study/NCT03944356) | N/A | Completed | 232 | Non-interventional study of adjuvant dabrafenib + trametinib in clinical practice; mostly a cutaneous population |
| [NCT05585320](https://clinicaltrials.gov/study/NCT05585320) | Phase 1/2 | Active, not recruiting | 209 | MEK inhibitor IMM-1-104 in RAS/MAPK-activated solid tumours; indirect relevance to dabrafenib |
| [NCT02416232](https://clinicaltrials.gov/study/NCT02416232) | N/A | No longer available | N/A | Trametinib access programme in BRAF-mutant cutaneous melanoma; no efficacy data |

No ANZCTR trial identifiers were included in the data compiled for this report.

## Literature Evidence

No publications were retrieved for non-cutaneous melanoma itself. The following support related subtypes and the BRAF/MEK inhibitor class.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30376465](https://pubmed.ncbi.nlm.nih.gov/30376465/) | 2019 | Real-world cohort | Melanoma Res | Multicentre retrospective study of combination BRAF/MEK inhibitors in 65 patients with melanoma and active brain metastases |
| [40853557](https://pubmed.ncbi.nlm.nih.gov/40853557/) | 2025 | Review | JAMA | Review of cutaneous melanoma (epidemiology and management) |
| [38590555](https://pubmed.ncbi.nlm.nih.gov/38590555/) | 2024 | Review | Adv Ophthalmol Pract Res | Personalised treatment concepts in periocular and extraocular cancers, including immunotherapy |
| [31361915](https://pubmed.ncbi.nlm.nih.gov/31361915/) | 2020 | Case report/Review | Clin Exp Dermatol | Two BRAF-mutated conjunctival melanomas (epithelioid type) treated with vemurafenib, with literature review |
| [33872566](https://pubmed.ncbi.nlm.nih.gov/33872566/) | 2021 | Case report | Can J Urol | BRAF V600E-positive metastatic scrotal melanoma treated with oncogene-targeted therapy |
| [31747798](https://pubmed.ncbi.nlm.nih.gov/31747798/) | 2019 | Case report/Review | J Investig Med High Impact Case Rep | Lacrimal sac melanoma in 15 Japanese patients, with literature review |
| [26710785](https://pubmed.ncbi.nlm.nih.gov/26710785/) | 2015 | Molecular profiling | Mol Biol (Mosk) | Spectrum of BRAF, NRAS and KIT driver mutations differs between melanoma subtypes |
| [24879511](https://pubmed.ncbi.nlm.nih.gov/24879511/) | 2014 | Case series | Am J Dermatopathol | Panniculitis in 9 patients on BRAF inhibitors (about 3% on dabrafenib, 10% on dabrafenib + trametinib) |
| [25788221](https://pubmed.ncbi.nlm.nih.gov/25788221/) | 2015 | Case report | Eur J Dermatol | Panniculitis in two patients on BRAF + MEK inhibitor combination |
| [32877390](https://pubmed.ncbi.nlm.nih.gov/32877390/) | 2020 | Case report | Medwave | Panniculitis during dabrafenib/trametinib in stage IV BRAF V600E melanoma |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10003L | Tafinlar | Capsule 75 mg (as mesilate) | Not stated in the data compiled for this report |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (BRAF kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI. Cutaneous toxicity, including panniculitis, is a documented concern in the literature above |
| Handling Protection | Please refer to the PI and local handling policies |

## Safety Considerations

- **Drug Interactions**: The interaction screen identified 100 potential interactions. The 20 shown in the data are all rated Moderate: acarbose, famotidine, ranitidine, cimetidine, hydrocortisone, triamcinolone, dexamethasone, betamethasone, alogliptin, metformin, pioglitazone, chlorpropamide, acetohexamide, bupropion, aprepitant, clarithromycin, magnesium oxide, aluminium hydroxide, calcium carbonate and cisapride. Acid-reducing agents and antacids, antidiabetic agents and corticosteroids are the main groups to review. CYP3A4 induction by dabrafenib is a likely contributor, but this is not confirmed in the data compiled.
- **Class-related cutaneous effects**: Panniculitis has been reported with BRAF inhibitors, alone or combined with MEK inhibitors (case series above), so skin monitoring is advisable.

Warnings and contraindications from the Australian product label were not available. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for non-cutaneous melanoma, restricted to BRAF V600-mutant disease)

**Rationale:**
- The MAPK mechanism is strong, and dabrafenib is established in BRAF-mutant cutaneous melanoma. Tumour-agnostic and platform trials (NCI-MATCH Subprotocol H, DETERMINE) are in progress, but no subtype-specific Phase 3 RCT or published efficacy result exists, so evidence is partial and extrapolated.
- The non-melanoma predictions (choroideremia, ALS, central areolar choroidal dystrophy, polymicrogyria) have no supporting data and should be placed on **Hold**.

**To proceed, the following is needed:**
- Confirmation of BRAF V600 mutation status (biomarker selection) before any use
- Results from NCI-MATCH Subprotocol H and the DETERMINE platform trial in non-cutaneous melanoma
- Mechanism of action data from DrugBank
- Australian product label warnings and contraindications (a blocking data gap for safety screening), plus the approved indication text for the ARTG entry
- A drug interaction management plan, covering CYP3A4-related interactions
- Skin toxicity monitoring (including panniculitis) in the safety plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

