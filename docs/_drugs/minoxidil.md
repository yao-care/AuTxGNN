---
layout: default
title: Minoxidil
parent: 僅模型預測 (L5)
nav_order: 449
evidence_level: L5
indication_count: 3
---

# Minoxidil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Minoxidil: From Hypertension to Diffuse Alopecia Areata

## One-Sentence Summary

Minoxidil was originally developed as an oral vasodilator for severe hypertension, and its follicle-stimulating side effect later led to its well-known use in androgenetic alopecia. The TxGNN model additionally predicts efficacy for **diffuse alopecia areata** — an autoimmune, non-scarring form of hair loss — with **3 clinical trials** and **20 publications** currently available, making it the strongest-evidenced of three hair-loss-related predictions generated for this drug. Two further, much weaker-evidenced predictions (hypotrichosis simplex of the scalp; congenital hypotrichosis with milia) are also flagged and summarised below.

---

## Quick Overview

*(Based on the strongest-evidenced prediction: diffuse alopecia areata. See "Other Predicted Indications" below for the two remaining candidates.)*

| Item | Content |
|------|------|
| Original Indication | Hypertension (severe, oral vasodilator) — no TGA-specific Product Information is available in this evidence pack, as the drug is not currently marketed in Australia |
| Predicted New Indication | Diffuse Alopecia Areata |
| TxGNN Prediction Score | 99.9998% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (data gap DG002). Based on well-established public pharmacology, minoxidil is a potassium-channel opener that causes vasodilation; independent of that effect, it also prolongs the hair follicle anagen (growth) phase and promotes local angiogenesis around the follicle. This growth-promoting action is not restricted to a specific hair-loss aetiology, which is why it is already used empirically well beyond its original vasodilator indication.

Diffuse alopecia areata (AA) is an autoimmune condition, distinct in cause from androgenetic alopecia, but the shared endpoint — a follicle held out of active growth — means minoxidil's anagen-promoting mechanism can plausibly support regrowth as an adjunct even though it does not correct the underlying autoimmune attack. This is reflected in current practice: oral and topical minoxidil are already used as adjunctive therapy in AA and are referenced in the 2024 European expert consensus statement on systemic AA treatment, giving this prediction real-world clinical grounding.

By contrast, the other two predicted indications are genetic/structural hair disorders (hereditary follicle malformation) rather than growth-cycle disorders, so the same mechanistic logic applies far more weakly — see below.

---

## Other Predicted Indications (Lower Evidence)

| Disease | TxGNN Score | Evidence Level | Trials / Literature | Recommendation | Note |
|---|---|---|---|---|---|
| Hypotrichosis simplex of the scalp | 99.9999% | L4 | 0 trials / 3 case reports | Research Question | Monogenic (CDSN) follicle-structure disorder; minoxidil may slow progressive thinning but cannot correct the underlying structural defect |
| Congenital hypotrichosis with milia | 99.9999% | L5 | 0 trials / 0 literature | Hold | Prediction-only, no supporting evidence; mechanistic applicability to this congenital ectodermal syndrome is unclear |

---

## Clinical Trial Evidence

### Diffuse Alopecia Areata

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01900041](https://clinicaltrials.gov/study/NCT01900041) | Phase 2 | Completed | 74 | Multicentre comparative study of Pantovigar plus 2% minoxidil vs. 2% minoxidil alone for female pattern/diffuse hair loss; minoxidil used as active comparator/combination arm (Relevance grade B) |
| [NCT04011748](https://clinicaltrials.gov/study/NCT04011748) | Phase 2 | Unknown | 20 | Stem Cell Educator therapy for alopecia areata; does not involve minoxidil — background context only (Relevance grade C) |
| [NCT06527729](https://clinicaltrials.gov/study/NCT06527729) | Early Phase 1 | Completed | 28 | Sildenafil lipid-nanocarrier for AA; does not involve minoxidil, small early-phase study — background context only (Relevance grade C) |

### Hypotrichosis Simplex of the Scalp / Congenital Hypotrichosis with Milia

Currently no related clinical trials registered.

---

## Literature Evidence

### Diffuse Alopecia Areata

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35796224](https://pubmed.ncbi.nlm.nih.gov/35796224/) | 2022 | RCT (Comparative) | Dermatologic Therapy | Topical minoxidil 5% gel vs. methotrexate 1% gel in localized AA (n=50), compared clinically and dermoscopically |
| [36257912](https://pubmed.ncbi.nlm.nih.gov/36257912/) | 2022 | RCT (Comparative) | Dermatologic Therapy | Blinded multi-group RCT comparing latanoprost, minoxidil 5%, betamethasone and combinations in AA |
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | Network Meta-analysis | Cochrane Database Syst Rev | Network meta-analysis of AA treatments including hair-growth stimulants such as minoxidil |
| [36800063](https://pubmed.ncbi.nlm.nih.gov/36800063/) | 2023 | Systematic Review / Meta-analysis | Lasers in Medical Science | Laser/light therapy combined with topical minoxidil in AA — efficacy and safety across pooled RCTs |
| [38169088](https://pubmed.ncbi.nlm.nih.gov/38169088/) | 2024 | Guideline/Consensus | J Eur Acad Dermatol Venereol | European expert consensus on systemic AA treatment |
| [33940103](https://pubmed.ncbi.nlm.nih.gov/33940103/) | 2022 | Systematic Review | J Am Acad Dermatol | Systematic review of pediatric AA treatment options |
| [31499158](https://pubmed.ncbi.nlm.nih.gov/31499158/) | 2021 | Case Series | J Am Acad Dermatol | Combination tofacitinib and oral minoxidil in severe AA |
| [38634160](https://pubmed.ncbi.nlm.nih.gov/38634160/) | 2024 | Retrospective Case Series | Skin Res Technol | Microneedle-delivered minoxidil combined with triamcinolone acetonide in AA |
| [35244759](https://pubmed.ncbi.nlm.nih.gov/35244759/) | 2023 | Review | Arch Dermatol Res | Multi-centre retrospective analysis of oral minoxidil in androgenetic alopecia and telogen effluvium (adjacent, not AA-specific) |
| [38164355](https://pubmed.ncbi.nlm.nih.gov/38164355/) | 2024 | Review (Mechanistic) | Int J Med Sci | Overview of hair follicle regeneration research, referencing minoxidil among standard therapies |

### Hypotrichosis Simplex of the Scalp

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35761391](https://pubmed.ncbi.nlm.nih.gov/35761391/) | 2022 | Case Report | Dermatologic Therapy | Hereditary hypotrichosis simplex treated with oral minoxidil plus growth factors |
| [39902296](https://pubmed.ncbi.nlm.nih.gov/39902296/) | 2024 | Case Report | Frontiers in Genetics | Familial CDSN-mutation HSS in an 8-year-old treated with botanic extracts plus minoxidil |
| [36651821](https://pubmed.ncbi.nlm.nih.gov/36651821/) | 2023 | Case Report | J Dermatolog Treat | Hereditary hypotrichosis simplex treated with platelet-rich plasma plus topical minoxidil 2% |

### Congenital Hypotrichosis with Milia

Currently no related literature available.

---

## Australia Market Information

Minoxidil has no current ARTG entries and is **not marketed** in Australia under this evidence pack's data. No Australia-specific product, dosage form, or approved-indication text is available to tabulate.

---

## Safety Considerations

No TFDA/TGA-sourced warnings, contraindications, or drug interaction data were available in this evidence pack (blocking data gap DG001), and no drug interaction record was found (query status: not found). Please refer to an overseas TGA-equivalent Product Information (e.g. FDA/EMA-approved PI) for minoxidil safety information, since no Australian ARTG-registered PI currently exists for this product.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for diffuse alopecia areata; the other two predicted indications remain at **Research Question** and **Hold** respectively)

**Rationale:**
Diffuse alopecia areata is supported by completed comparative trials, RCTs, and systematic reviews/consensus guidelines that already position minoxidil as an adjunctive AA therapy, giving it evidence level L2 — well ahead of the other two candidates, which rest on case reports only or no evidence at all. However, no dedicated Phase 3 RCT of minoxidil monotherapy in AA exists, and the drug currently has no Australian regulatory footprint.

**To proceed, the following is needed:**
- TFDA/TGA-equivalent Product Information covering warnings, contraindications and interactions (blocking gap DG001)
- Confirmed mechanism-of-action data from DrugBank (gap DG002)
- A defined Australian regulatory pathway, since minoxidil currently has zero ARTG entries
- A dedicated Phase 2/3 RCT of minoxidil (monotherapy or as a defined adjunct) specifically in diffuse alopecia areata
- Continued literature/trial monitoring only (no active development) for hypotrichosis simplex of the scalp and congenital hypotrichosis with milia until stronger evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

