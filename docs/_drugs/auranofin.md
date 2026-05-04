---
layout: default
title: Auranofin
parent: 僅模型預測 (L5)
nav_order: 66
evidence_level: L5
indication_count: 10
---

# Auranofin
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

# Auranofin: From Rheumatoid Arthritis to Arthropathy

## One-Sentence Summary

Auranofin (Ridaura) is an oral gold(I) compound approved by the FDA in 1985 as a disease-modifying antirheumatic drug (DMARD) for rheumatoid arthritis (RA), with over 40 years of international clinical use. The TxGNN model predicts it may be effective for **Arthropathy** (inflammatory joint disease), consistent with its established pharmacological profile — currently supported by **20 publications including historical Phase 3 comparative trial data**, though no Auranofin-specific trials are registered in ClinicalTrials.gov or ICTRP at this time. Critically, Auranofin is **not currently registered in Australia**, representing a potential access gap for patients with inflammatory arthropathy who may benefit from this unique oral gold therapy.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Rheumatoid Arthritis (FDA-approved 1985; not TGA-registered) |
| Predicted New Indication | Arthropathy |
| TxGNN Prediction Score | 62.81% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Auranofin is the only FDA-approved oral gold compound and has been used in chrysotherapy for rheumatoid arthritis for more than four decades. Although the complete mechanism of action was not fully characterised at the time of its approval, substantial pharmacological research has since identified several key pathways. **(1) TXNRD1/TrxR1 inhibition:** Auranofin covalently inhibits thioredoxin reductase 1, disrupting cellular redox homeostasis and inducing apoptosis in activated T and B lymphocytes and macrophages — the central driver of its immunosuppressive effect. **(2) NF-κB pathway suppression:** Auranofin blocks NF-κB activation, reducing downstream production of pro-inflammatory mediators including TNF-α, IL-1β, IL-6, COX-2, and inducible nitric oxide synthase (iNOS). **(3) NLRP3 inflammasome inhibition:** 2025 research (PMID 41090769) demonstrates that Auranofin suppresses NLRP3 activation and neutrophil migration via the IL-33/ST2-CXCL1 axis, extending its anti-inflammatory activity to gout and other crystal-induced arthropathies.

Arthropathy broadly encompasses the spectrum of inflammatory and degenerative joint diseases, with RA as the paradigm condition. Multiple Phase 2/3 comparative trials from the 1980s–1990s established Auranofin's clinical efficacy in RA, favourably comparing it to parenteral gold sodium thiomalate across joint inflammation scoring (Ritchie index), swollen joint counts, ESR, grip strength, and morning stiffness. A 1990 double-blind RCT with 145 patients (PMID 2261735) demonstrated significant improvements in all these parameters during both the blinded and open-extension phases. More recent data (PMID 36243005, 2022) revealed that Auranofin also normalises obesity-associated inflammation and metabolic dysfunction in mouse models, illustrating the breadth of its systemic anti-inflammatory reach beyond the joint.

The TxGNN model's prediction is mechanistically well-grounded and supported by Level 1 historical evidence. However, current clinical trial registries contain no Auranofin-specific arthropathy trials; the trials identified in this evidence pack evaluate other agents (tofacitinib and rituximab) and were retrieved due to overlapping arthropathy classification tags. The primary evidentiary strength resides in the literature corpus spanning 1983–2025.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03975790](https://clinicaltrials.gov/study/NCT03975790) | N/A | Completed | 479 | Retrospective cohort study comparing tofacitinib (Xeljanz) + MTX vs. tofacitinib alone in RA patients using US healthcare claims data — **evaluates tofacitinib, not Auranofin**; retrieved due to arthropathy classification overlap |
| [NCT01557348](https://clinicaltrials.gov/study/NCT01557348) | N/A | Completed | 1,239 | Prospective observational study of rituximab vs. alternative TNF inhibitors in RA patients who failed a single TNF inhibitor — **evaluates biologics, not Auranofin**; provides background on refractory RA management context |

> **Note:** Neither trial above evaluates Auranofin directly. No Auranofin-specific arthropathy trials are currently registered in ClinicalTrials.gov or ICTRP. The L1 evidence designation is derived from historical Phase 3 RCT-era data documented in the literature set below.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34731781](https://pubmed.ncbi.nlm.nih.gov/34731781/) | 2021 | Comprehensive Review | Int Immunopharmacol | Synthesis of 40+ years of Auranofin in RA; confirms TXNRD1, NF-κB, COX-2, Prdx1/Nrf2 mechanisms; documents growing repurposing portfolio across oncology, infectious disease, and metabolic conditions |
| [6426044](https://pubmed.ncbi.nlm.nih.gov/6426044/) | 1983 | Phase 3 Era Review | Scand J Rheumatol Suppl | Comparative safety and efficacy of Auranofin vs. parenteral gold across 12 published studies; 8/12 showed equivalent efficacy, 2 favoured each agent; withdrawal rate substantially lower with Auranofin |
| [2261735](https://pubmed.ncbi.nlm.nih.gov/2261735/) | 1990 | RCT + Open Extension | Clin Rheumatol | 6-month double-blind RCT of OM-8980 vs. Auranofin (145 RA patients), followed by 6-month open phase; significant improvements in Ritchie index, swollen joints, pain scale, morning stiffness, grip strength, and ESR |
| [41090769](https://pubmed.ncbi.nlm.nih.gov/41090769/) | 2025 | Preclinical (In vitro + In vivo) | Cells | Auranofin suppresses NLRP3 inflammasome activation and neutrophil migration via IL-33/ST2-CXCL1 axis in MSU crystal gout models; extends anti-arthritic mechanism to crystal arthropathies |
| [6426923](https://pubmed.ncbi.nlm.nih.gov/6426923/) | 1984 | Drug Review | Drugs | Preliminary pharmacological review of Auranofin in RA; efficacy approaches sodium aurothiomalate; mechanism involves immunological modulation and lysosomal enzyme activity reduction |
| [6318557](https://pubmed.ncbi.nlm.nih.gov/6318557/) | 1983 | Pharmacology Study | Am J Med | Original preclinical pharmacokinetic and biological action profile; Auranofin superior to parenteral gold in suppressing inflammation and stimulating cell-mediated immunity; inhibited lysosomal enzyme release and ADCC |
| [6239742](https://pubmed.ncbi.nlm.nih.gov/6239742/) | 1984 | Drug Profile | Clin Rheum Dis | Original documentation of Auranofin's clinical profile in progressive RA; established favourable therapeutic-to-toxicity ratio compared with other chrysotherapeutic agents |
| [3110942](https://pubmed.ncbi.nlm.nih.gov/3110942/) | 1986 | Pharmacology Review | Scand J Rheumatol Suppl | Updated pharmacology overview; confirmed oral vs. injectable gold differ in side-effect profile; withdrawal rate for adverse reactions several-fold lower with Auranofin |
| [36243005](https://pubmed.ncbi.nlm.nih.gov/36243005/) | 2022 | Mechanistic Study | Cell Metabolism | Computational screen identified Auranofin as improving insulin sensitivity and normalising obesity-associated inflammation (hepatic steatosis, hyperinsulinemia) in mouse models; reduces leptin via adipose tissue pathway |
| [40089079](https://pubmed.ncbi.nlm.nih.gov/40089079/) | 2025 | Molecular Pharmacology | Free Radic Biol Med | Auranofin targets peroxiredoxin 1 and 2 → ROS-ER stress axis → apoptosis and cytoprotective autophagy; mechanistically links anti-inflammatory and cytotoxic activities via shared TXNRD1/Prdx pathway |

---

## Safety Considerations

As Auranofin is not registered with the TGA and no Australian Product Information exists, prescribers should consult the **FDA-approved US Prescribing Information (Ridaura®)** for comprehensive safety data. The following information is drawn from the published literature:

- **Gastrointestinal adverse effects:** Diarrhoea, loose stools, nausea, and abdominal discomfort are the most common adverse effects and the primary cause of discontinuation; incidence substantially higher than with injectable gold
- **Gold-induced colitis:** Rare but serious; documented cases include ulcerative-colitis-like presentations with mucosal erosions and gold deposits on rectal biopsy (PMID 3318725); gold-associated colitis with eosinophilia has also been reported (PMID 3807438)
- **Nephropathy / proteinuria:** Risk of gold nephropathy with cumulative dosing; however, Auranofin's renal safety profile appears more favourable than parenteral gold compounds — urinalysis monitoring is recommended
- **Haematological effects:** Thrombocytopenia and other blood dyscrasias reported with gold therapy; baseline and periodic full blood count (FBC) monitoring recommended

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Auranofin has robust L1-grade historical evidence supporting its efficacy in RA/arthropathy from multiple Phase 3-era comparative trials, and its multi-target anti-inflammatory mechanism (TXNRD1/TrxR1, NF-κB, NLRP3) is well-characterised. Its absence from the Australian market represents a regulatory gap rather than an evidence gap, and access via the TGA Special Access Scheme may be appropriate for suitable patients. The 2025 NLRP3 inflammasome data further extend its clinical applicability to gout and other crystal-induced arthropathies.

**To proceed, the following is needed:**
- **TGA regulatory pathway review:** Assess eligibility for TGA Special Access Scheme (SAS Category B/C) for RA patients who have failed conventional DMARDs and biologics; evaluate requirements for full ARTG registration
- **Current guideline positioning:** Review latest EULAR and ACR RA treatment guidelines to confirm Auranofin's contemporary place in the treatment algorithm relative to modern biologics and JAK inhibitors
- **Australian prescribing and safety protocol:** Establish local monitoring standards covering urinalysis (proteinuria), FBC (with differential), liver function, and GI symptom surveillance prior to initiation and at regular intervals
- **MOA and pharmacokinetics documentation:** Obtain complete DrugBank record and current US PI to supplement known mechanism data and inform dose selection for Australian clinical practice
- **OA extension consideration:** The TXNRD1/Nrf2 preclinical evidence in osteoarthritis (PMID 36308906) warrants a dedicated preclinical programme and potential Phase 2 pilot study in OA with prominent synovitis — this represents a secondary repurposing opportunity with emerging mechanistic rationale
- **DDI assessment:** No drug-drug interaction data were available in this evidence pack; a formal DDI review against common co-prescriptions in arthritic patients (NSAIDs, methotrexate, warfarin) is required before clinical use

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require prospective clinical validation before therapeutic application. Data cutoff: 5 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

