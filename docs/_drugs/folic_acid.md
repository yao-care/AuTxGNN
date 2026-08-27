---
layout: default
title: Folic Acid
parent: 僅模型預測 (L5)
nav_order: 292
evidence_level: L5
indication_count: 10
---

# Folic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Folic Acid: From [Original Indication Not Documented] to Biotin Metabolic Disease

## One-Sentence Summary

Folic acid (DrugBank DB00158) is a B-vitamin; this evidence pack does not contain any Taiwan/Australia regulatory record of its original approved indication. TxGNN predicts activity against **biotin metabolic disease** with a very high score (**99.49%**), backed by **13 clinical trials** and **20 publications** — however, none of this evidence directly tests folic acid in this indication, and the evidence pack's own mechanistic review flags this as a **likely false-positive** signal from knowledge-graph clustering of "vitamin-responsive metabolic disease" entities rather than a genuine folate–biotin mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack |
| Predicted New Indication | Biotin metabolic disease |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for folic acid is not available in this evidence pack (data gap DG002, severity High). Based on general pharmacology, folic acid (vitamin B9) functions as a cofactor in one-carbon unit metabolism (e.g., nucleotide synthesis, homocysteine remethylation), which is biochemically distinct from biotin (vitamin B7), a cofactor for carboxylase reactions.

The evidence pack's own repurposing rationale for this candidate explicitly flags the prediction as likely spurious: biotin metabolic disease and folate deficiency are different disorders governed by different coenzyme systems, and the high TxGNN score is more plausibly explained by the knowledge graph clustering "vitamin-responsive metabolic disease" entities together (folic acid, biotin, B12, B1, E disorders are frequently co-reviewed in the literature as a class) rather than by a shared, causally relevant mechanism.

Consistent with this, none of the retrieved clinical trials or literature test folic acid specifically for biotin metabolic disease — the supporting material consists of general reviews of vitamin-responsive inborn errors of metabolism and multi-micronutrient supplementation trials that happen to include folic acid as one of several ingredients.

---

## Clinical Trial Evidence

No identified trial tests folic acid specifically for biotin metabolic disease. The following are the most relevant multi-vitamin/micronutrient trials retrieved by the evidence search; folic acid is at most a co-administered ingredient, not the studied intervention.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04312152](https://clinicaltrials.gov/study/NCT04312152) | NA | Unknown | 200 | RCT of Q10 ubiquinol + multivitamin B/E complex in autism spectrum disorder / Phelan-McDermid syndrome; not folic acid-specific |
| [NCT01474486](https://clinicaltrials.gov/study/NCT01474486) | NA | Completed | 40 | Multi-micronutrient palliative intervention in congestive heart failure; not disease-specific |
| [NCT01643187](https://clinicaltrials.gov/study/NCT01643187) | Phase 2 | Unknown | 1000 | Fortified food vs milk on nutritional/micronutrient status, including serum/erythrocyte folic acid, in malnourished children |
| [NCT03444155](https://clinicaltrials.gov/study/NCT03444155) | NA | Completed | 30 | Pilot comparing natural vs synthetic vitamin B-complex bioavailability |
| [NCT05687474](https://clinicaltrials.gov/study/NCT05687474) | N/A | Completed | 6824 | Universal newborn genomic screening for 126 treatable genetic diseases; a screening study, not a treatment trial |
| [NCT02302729](https://clinicaltrials.gov/study/NCT02302729) | NA | Completed | 1730 | Micronutrient powder vs placebo for childhood stunting in Guatemala |
| [NCT04586348](https://clinicaltrials.gov/study/NCT04586348) | Phase 4 | Active, not recruiting | 794 | Prenatal iodine reduction and neurodevelopment; unrelated to folate/biotin metabolism |
| [NCT00572741](https://clinicaltrials.gov/study/NCT00572741) | NA | Completed | 39 | Targeted nutritional intervention for oxidative stress/methylation impairment in autism |
| [NCT04067921](https://clinicaltrials.gov/study/NCT04067921) | N/A | Unknown | 1963 | Platform infrastructure for nutrition/nutrigenomics trials; not an intervention trial |
| [NCT07350538](https://clinicaltrials.gov/study/NCT07350538) | NA | Active, not recruiting | 20 | Gut microbiome/prebiotic pilot for alcohol addiction recovery; unrelated to this indication |

---

## Literature Evidence

No publication directly studies folic acid for biotin metabolic disease. The most relevant results are general reviews of vitamin-responsive/cofactor-dependent inborn errors of metabolism, which discuss folate and biotin disorders as a class rather than establishing a direct treatment link.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Review | Handbook of Clinical Neurology | Reviews vitamin-responsive disorders — cobalamin, folate, biotin, B1, E — as distinct cofactor-dependent conditions |
| [779426](https://pubmed.ncbi.nlm.nih.gov/779426/) | 1976 | Review | Advances in Human Genetics | "Vitamin-responsive inherited metabolic disorders" — general review (abstract not available) |
| [11031989](https://pubmed.ncbi.nlm.nih.gov/11031989/) | 2000 | Review | Ryoikibetsu Shokogun Shirizu | "Vitamin dependency syndrome" — general review (abstract not available) |
| [958746](https://pubmed.ncbi.nlm.nih.gov/958746/) | 1976 | Review | Pediatric Clinics of North America | Reviews B-complex vitamins as coenzymes in vitamin-responsive aminoacidopathies; notes difficulty predicting individual cofactor response |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Review | Acta Vitaminologica et Enzymologica | Reviews mechanisms linking vitamins to metabolic disease: malabsorption, metabolic errors, vitamin-dependent syndromes |
| [30557456](https://pubmed.ncbi.nlm.nih.gov/30557456/) | 2019 | Review | Movement Disorders | Movement disorders in treatable inborn errors of metabolism, including vitamin-responsive conditions |
| [16343871](https://pubmed.ncbi.nlm.nih.gov/16343871/) | 2006 | Review | Archives de Pédiatrie | Neonatal epilepsy secondary to inborn metabolic disorders, including vitamin-responsive types |
| [4279121](https://pubmed.ncbi.nlm.nih.gov/4279121/) | 1974 | Review | Biomembranes | Absorption of water-soluble vitamins (abstract not available) |
| [6396715](https://pubmed.ncbi.nlm.nih.gov/6396715/) | 1984 | Other | Progress in Food & Nutrition Science | Deficiencies of protein, vitamin A, pyridoxine, biotin and zinc impair cell-mediated immunity |
| [14989256](https://pubmed.ncbi.nlm.nih.gov/14989256/) | 2004 | Other | Archives of Biochemistry and Biophysics | Deficiency of vitamins B12, folic acid, B6, C or E may mimic radiation-induced DNA damage ("metabolic tune-up" hypothesis) |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

*(Note: TFDA/TGA label warnings and contraindications are flagged as a Blocking data gap (DG001) in this evidence pack — this must be resolved before any safety assessment can proceed. No drug-drug interaction data was found for folic acid in this pack.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN score, no clinical trial or publication directly tests folic acid for biotin metabolic disease, and the evidence pack's own mechanistic analysis identifies this prediction as a probable false positive arising from embedding-based clustering of unrelated "vitamin-responsive metabolic disease" entities rather than a genuine folate–biotin pharmacological link. Combined with the missing MOA data and missing TGA safety/label data, there is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications) — currently a Blocking data gap (DG001)
- Verified mechanism-of-action data for folic acid (DG002)
- Independent confirmation of whether this signal reflects a true biological relationship or a knowledge-graph clustering artifact (e.g., via pathway/target-level analysis distinguishing folate vs. biotin coenzyme systems)
- Any primary studies that specifically dose folic acid (not multi-vitamin combinations) in patients with biotin-responsive metabolic disorders, should they exist
- Clarification of the "not marketed / 0 ARTG entries" status recorded here, given folic acid's typical wide availability as an OTC supplement — worth a data-source check before relying on this market-status field
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

