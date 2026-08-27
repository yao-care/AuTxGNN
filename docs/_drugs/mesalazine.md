---
layout: default
title: Mesalazine
parent: 僅模型預測 (L5)
nav_order: 428
evidence_level: L5
indication_count: 10
---

# Mesalazine
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

# Mesalazine: From Ulcerative Colitis to Rheumatoid Arthritis

## One-Sentence Summary

> Mesalazine (5-aminosalicylic acid, 5-ASA) is an aminosalicylate anti-inflammatory long established in the treatment of **ulcerative colitis**, as reflected throughout the literature evidence in this pack.
> The TxGNN model flagged 10 potential new indications; of these, only two carry any supporting trial or literature evidence — **Rheumatoid Arthritis** (L2, 6 trials, 20 publications) and **Osteoarthritis** (L4, 3 preclinical publications, no trials) — while the remaining eight are unsupported knowledge-graph signals recommended for **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ulcerative colitis (inferred from literature evidence in this pack — no TGA licence data available) |
| Predicted New Indication (Primary) | Rheumatoid Arthritis |
| TxGNN Prediction Score (Primary) | 99.57% |
| Secondary Candidate | Osteoarthritis (score 99.63%, evidence level L4, no trials) |
| Evidence Level (Primary) | L2 |
| Australia Market Status | Not marketed (0 ARTG entries in this data pack) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap — DrugBank API query pending). Based on known information, mesalazine is the active 5-ASA component released from sulfasalazine after colonic bacterial cleavage into sulfapyridine + 5-ASA. Sulfasalazine has been an established disease-modifying antirheumatic drug (DMARD) since the 1940s, which is the biological basis for the TxGNN rheumatoid arthritis signal — however, this evidence pack contains a critical caveat that must be weighed carefully.

Three separate historical studies in this pack (PMID 2860942, 2877851, 8535642) directly tested which component of sulfasalazine drives its antirheumatic effect, and all consistently found that **sulfapyridine**, not 5-ASA/mesalazine, is the more active moiety, with mesalazine alone showing only a weak effect. This means most of the RA clinical evidence attributed to "sulfasalazine" cannot be safely extrapolated to mesalazine as a standalone agent — a significant mechanistic attribution risk.

For osteoarthritis, the picture is more mechanistically direct but much earlier stage: a 2024 Nature Communications paper (PMID 38310093) describes 5-ASA specifically (not sulfasalazine) suppressing osteoarthritis via the OSCAR-PPARγ axis — a novel, drug-specific mechanistic finding. However, this remains preclinical/mechanistic only, with no clinical trials yet registered.

---

## Clinical Trial Evidence

**Rheumatoid Arthritis**

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02930343](https://clinicaltrials.gov/study/NCT02930343) | Phase 3 | Terminated | 136 | Sulfasalazine vs leflunomide combination DMARD in RA after methotrexate failure — the only trial directly designed for RA efficacy, but terminated and tests sulfasalazine (not isolated mesalazine) |
| [NCT00637780](https://clinicaltrials.gov/study/NCT00637780) | Phase 4 | Terminated | 2 | Pharmacokinetic study of sulfasalazine in juvenile idiopathic arthritis; not a efficacy trial, enrolment too small to be informative |
| [NCT05580861](https://clinicaltrials.gov/study/NCT05580861) | Phase 1/2 | Recruiting | 64 | Sulfasalazine combined with induction therapy in acute myeloid leukaemia; RA relevance unclear from available summary |
| [NCT00514982](https://clinicaltrials.gov/study/NCT00514982) | Phase 2 | Withdrawn | 0 | Observational study of IBD-type therapy in Hermansky-Pudlak syndrome colitis; not an RA population |
| [NCT06201793](https://clinicaltrials.gov/study/NCT06201793) | Phase 2 | Completed | 46 | Minocycline add-on to mesalamine in ulcerative colitis; different investigational drug, not RA |
| [NCT03591770](https://clinicaltrials.gov/study/NCT03591770) | Phase 4 | Terminated | 15 | Shingrix vaccine immunogenicity in ulcerative colitis patients on tofacitinib; safety background only, not RA efficacy |

**Osteoarthritis**

Currently no related clinical trials registered.

---

## Literature Evidence

**Rheumatoid Arthritis** (10 most relevant of 20 total)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2860942](https://pubmed.ncbi.nlm.nih.gov/2860942/) | 1985 | Cohort/Mechanistic | BMJ | Sulphapyridine, not 5-ASA, showed pronounced second-line effect in RA over 24 weeks; 5-ASA alone only weakly active |
| [2877851](https://pubmed.ncbi.nlm.nih.gov/2877851/) | 1986 | Clinical study | Drugs | 6-month comparison of 5-ASA vs sulphapyridine in RA; sulphasalazine group improved, 5-ASA group did not |
| [8535642](https://pubmed.ncbi.nlm.nih.gov/8535642/) | 1995 | Review | British Journal of Rheumatology | Weight of evidence favours sulphapyridine, not 5-ASA, as the active moiety and main source of side-effects in RA |
| [7588084](https://pubmed.ncbi.nlm.nih.gov/7588084/) | 1995 | Review | Drugs | Comprehensive review of sulfasalazine pharmacology/efficacy in RA; notes uncertainty over whether sulfapyridine, mesalazine, or both drive the antirheumatic effect |
| [2899645](https://pubmed.ncbi.nlm.nih.gov/2899645/) | 1988 | Cohort | Journal of Rheumatology | Sulfasalazine treatment normalised abnormal lymphocyte function in RA patients over 12 weeks |
| [10743803](https://pubmed.ncbi.nlm.nih.gov/10743803/) | 2000 | Mechanistic | Journal of Rheumatology | Sulfasalazine and metabolites (including 5-ASA) modulate cytokine and MMP mRNA in rheumatoid synovial fibroblasts |
| [12235076](https://pubmed.ncbi.nlm.nih.gov/12235076/) | 2002 | Pharmacovigilance | Gut | Re-evaluation of serious adverse reactions to sulphasalazine and mesalazine reported to the UK Committee on Safety of Medicines |
| [41443863](https://pubmed.ncbi.nlm.nih.gov/41443863/) | 2025 | Case report | Internal Medicine (Tokyo) | Mesalazine-induced colitis in an RA patient without underlying IBD, confirmed by drug-induced lymphocyte stimulation test — relevant safety signal |
| [17708602](https://pubmed.ncbi.nlm.nih.gov/17708602/) | 2007 | Review | World Journal of Gastroenterology | Historical review noting 5-ASA therapy was originally designed to treat RA before its repurposing to ulcerative colitis |
| [7904547](https://pubmed.ncbi.nlm.nih.gov/7904547/) | 1993 | Review | Clinical Pharmacokinetics | Pharmacokinetics of slow-acting antirheumatic drugs including sulphasalazine |

**Osteoarthritis** (3 of 3 available)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38310093](https://pubmed.ncbi.nlm.nih.gov/38310093/) | 2024 | Preclinical/Mechanistic | Nature Communications | 5-ASA suppresses osteoarthritis via the OSCAR-PPARγ axis, competing with extracellular matrix components — direct mesalazine-specific mechanism |
| [38491514](https://pubmed.ncbi.nlm.nih.gov/38491514/) | 2024 | Bioinformatics/Target discovery | Journal of Translational Medicine | Identifies therapeutic targets in OA by combining transcriptional datasets and drug-target interaction data; indirect supporting evidence |
| [1673814](https://pubmed.ncbi.nlm.nih.gov/1673814/) | 1991 | In vitro/Mechanistic | Wiener Klinische Wochenschrift | Sulfasalazine and metabolites (including 5-ASA) inhibit leukotriene/prostaglandin release from synovial tissue in OA, chondrocalcinosis, and RA patients |

---

## Australia Market Information

No ARTG entries are recorded in this data pack (`market_status: 未上市`, `total_licenses: 0`). Mesalazine's Australian market/registration status could not be confirmed from the data provided.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Key warnings, contraindications, and drug-drug interaction data were not available in this evidence pack (DG001, Blocking).

---

## Low-Confidence Candidates (Not Recommended)

The remaining 8 predicted indications — congenital hypotrichosis with juvenile macular dystrophy, seborrheic keratosis, osteoarthritis susceptibility, vulvar inverted follicular keratosis, pseudoachondroplasia, acromesomelic dysplasia (Hunter-Thompson type), colobomatous microphthalmia-rhizomelic dysplasia syndrome, and brachydactyly-syndactyly syndrome — have zero clinical trials and zero literature support. These are largely rare monogenic/developmental disorders with no plausible mechanistic link to mesalazine's anti-inflammatory action, and are assessed as knowledge-graph node-sharing artefacts (Evidence Level L5, **Hold**).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The strongest candidate (rheumatoid arthritis, L2) is undermined by three independent studies indicating sulfapyridine — not mesalazine — is the active antirheumatic component of sulfasalazine; no completed trial has tested mesalazine alone in RA.
- The osteoarthritis signal (L4) is a genuine, recent, drug-specific mechanistic finding but is preclinical only, with no clinical trials registered.
- The drug has no recorded Australian market registration (0 ARTG entries), and a Blocking data gap (DG001, TGA PI/warnings) prevents any safety pre-assessment.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications, DDI) to resolve DG001
- Confirmed mechanism of action data via DrugBank API to resolve DG002
- A clinical trial testing mesalazine specifically (not sulfasalazine) in RA, to resolve the active-moiety attribution question
- Early-phase/translational studies confirming the OSCAR-PPARγ osteoarthritis mechanism in vivo or in humans
- Confirmation of current Australian registration/ARTG status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

