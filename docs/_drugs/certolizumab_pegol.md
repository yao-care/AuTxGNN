---
layout: default
title: Certolizumab Pegol
parent: 僅模型預測 (L5)
nav_order: 138
evidence_level: L5
indication_count: 10
---

# Certolizumab Pegol
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

Using the Evidence Pack provided, I've synthesized a report. Note: unlike a typical single-indication candidate, this Evidence Pack (`TW-DB08904-multi`) contains **10 TxGNN-predicted indications** for certolizumab pegol with very different evidence quality — including one (highest model score) that is actually a **safety signal against** use, and several that are model noise. I've adapted the template's tables to reflect this honestly rather than force-fitting a single "top" prediction, per the "no guessing / explain every change" rule.

# Certolizumab Pegol: From Established Anti-TNF Indications to Inflammatory Spondylopathy (Multi-Indication TxGNN Assessment)

## One-Sentence Summary

Certolizumab pegol is a PEGylated anti-TNF-α biologic already established internationally for rheumatoid arthritis, psoriatic arthritis, axial spondyloarthritis and Crohn's disease, but it is **not currently marketed in Australia** (0 ARTG entries). TxGNN generated 10 candidate indications for this drug; the **best-supported new-market opportunity is inflammatory spondylopathy / axial spondyloarthritis**, backed by **6+ completed Phase 3 trials** and multiple systematic reviews, while the model's *highest-scoring* prediction (rheumatoid vasculitis) is actually contradicted by safety literature showing the drug can **induce** vasculitis rather than treat it. Several other candidates (e.g. congenital/structural syndromes) have no supporting evidence at all and are best treated as prediction noise.

## Quick Overview

| Item | Content |
|------|------|
| Original (global) indications | Rheumatoid arthritis, psoriatic arthritis, axial spondyloarthritis, Crohn's disease (anti-TNF biologic; per literature evidence, e.g. PMID 27704400, 24919863) |
| Highest TxGNN-Scored Indication | Rheumatoid vasculitis (99.78%) — **flagged Hold**, safety signal contradicts efficacy hypothesis |
| Best-Evidenced New Indication | Inflammatory spondylopathy / axial spondyloarthritis (99.73%) |
| Evidence Level (best candidate) | L1 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | **Proceed with Guardrails** (inflammatory spondylopathy, vertebral disease); **Research Question** (polyarticular JIA, tenosynovitis); **Hold** (rheumatoid vasculitis and all congenital/structural predictions) |

### Predicted Indications — Full Ranking

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|---|---|---|---|---|
| 1 | Rheumatoid vasculitis | 99.78% | L4 | Hold (safety contradiction) |
| 2 | Hypermobility of coccyx | 99.75% | L5 | Hold (no biological plausibility) |
| 3 | Inflammatory spondylopathy | 99.73% | L1 | Proceed with Guardrails |
| 4 | Kummell disease | 99.70% | L5 | Hold (no biological plausibility) |
| 5 | Polyarticular juvenile rheumatoid arthritis | 99.69% | L2 | Research Question |
| 6 | Vertebral disease | 99.26% | L1 | Proceed with Guardrails |
| 7 | Mendelian susceptibility to mycobacterial disease (IL12B deficiency) | 96.85% | L5 | Hold (mechanistic contraindication) |
| 8 | Brachydactyly-syndactyly syndrome | 96.01% | L5 | Hold (no biological plausibility) |
| 9 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 95.72% | L5 | Hold (no biological plausibility) |
| 10 | Tenosynovitis | 95.69% | L5 | Research Question |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not returned for this drug in the Evidence Pack (data gap, DG002). Based on the literature evidence collected, certolizumab pegol is a Fc-free, PEGylated Fab' fragment that selectively neutralises TNF-α; it lacks the antibody Fc region, so it does not fix complement or trigger antibody-dependent cytotoxicity, distinguishing it pharmacologically from other anti-TNF agents (PMID 27704400, 24919863).

For **inflammatory spondylopathy / vertebral disease**, this is not a novel repurposing hypothesis but a **known, established anti-TNF class indication** (axial spondyloarthritis and ankylosing spondylitis) that the drug simply has not yet been registered for in Australia. TNF-α is central to synovial and enthesial inflammation in spondyloarthropathies, and certolizumab pegol has multiple dedicated Phase 3 RCTs (RAPID-axSpA, C-OPTIMISE, C-axSpAnd) directly demonstrating efficacy in this population. The prediction therefore represents **market expansion of a proven mechanism**, not a mechanistic leap.

For **polyarticular juvenile rheumatoid arthritis**, the mechanistic link is a reasonable extension (shared TNF-α-driven synovitis with adult RA) and is supported by a dedicated Phase 3 PK/safety/efficacy trial (NCT01550003), but no published results were found in this pack, so evidence remains incomplete.

For **rheumatoid vasculitis**, the mechanistic story is inverted: the literature returned by this search consists overwhelmingly of **case reports of certolizumab-induced vasculitis and related autoimmune adverse reactions** (leukocytoclastic vasculitis, hypocomplementemic urticarial vasculitis, medium-vessel vasculitis, rapidly progressive glomerulonephritis), with only a single case report supporting therapeutic benefit (leg ulcers in rheumatoid vasculitis, PMID 34786446). The model's high similarity score here appears to reflect shared disease/drug co-occurrence in the literature rather than a genuine treatment signal.

The remaining low-ranked predictions (hypermobility of coccyx, Kummell disease, brachydactyly-syndactyly syndrome, colobomatous microphthalmia-rhizomelic dysplasia syndrome) are structural, congenital, or degenerative conditions with no inflammatory/immune component and no supporting trials or literature — these are assessed as model noise. Mendelian susceptibility to mycobacterial disease due to IL12B deficiency is a distinct case: anti-TNF agents are well known to increase mycobacterial reactivation risk, so this prediction runs **counter** to the drug's known risk profile and should be treated as a potential contraindication signal, not an opportunity.

## Clinical Trial Evidence

*(Trials shown relate primarily to the inflammatory spondylopathy / vertebral disease group, plus the dedicated polyarticular JIA trial; rows 1–7 are shared across both indications given their overlapping trial evidence.)*

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01087762](https://clinicaltrials.gov/study/NCT01087762) | Phase 3 | Completed | 325 | Randomised, double-blind, placebo-controlled trial of two CZP dose regimens in active axial spondyloarthritis |
| [NCT02505542](https://clinicaltrials.gov/study/NCT02505542) | Phase 3 | Completed | 736 | C-OPTIMISE: maintenance of remission with CZP 200mg Q2W/Q4W vs placebo in axSpA |
| [NCT02552212](https://clinicaltrials.gov/study/NCT02552212) | Phase 3 | Completed | 317 | C-axSpAnd: CZP efficacy/safety in non-radiographic axSpA with objective inflammation signs |
| [NCT01087788](https://clinicaltrials.gov/study/NCT01087788) | Phase 3 | Completed | 409 | CZP efficacy/safety in adult-onset active and progressive psoriatic arthritis |
| [NCT03215277](https://clinicaltrials.gov/study/NCT03215277) | Phase 2A | Completed | 76 | Head-to-head bimekizumab vs certolizumab pegol in active ankylosing spondylitis |
| [NCT02354105](https://clinicaltrials.gov/study/NCT02354105) | N/A (real-world) | Completed | 680 | Non-interventional real-world effectiveness of CZP in axSpA daily practice |
| [NCT03020992](https://clinicaltrials.gov/study/NCT03020992) | Phase 4 | Completed | 89 | C-VIEW: CZP reduces anterior uveitis flares in axSpA patients with uveitis history |
| [NCT01550003](https://clinicaltrials.gov/study/NCT01550003) | Phase 3 | Completed | 193 | Pharmacokinetics, safety and efficacy of CZP in children/adolescents with polyarticular JIA |

No dedicated clinical trials support rheumatoid vasculitis, hypermobility of coccyx, Kummell disease, mendelian susceptibility to mycobacterial disease, brachydactyly-syndactyly syndrome, colobomatous microphthalmia-rhizomelic dysplasia syndrome, or tenosynovitis as treatment indications.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36270657](https://pubmed.ncbi.nlm.nih.gov/36270657/) | 2023 | Systematic Review | Ann Rheum Dis | Efficacy/safety of biological DMARDs informing 2022 ASAS-EULAR axSpA management recommendations |
| [27366922](https://pubmed.ncbi.nlm.nih.gov/27366922/) | 2016 | Systematic Review | Expert Opin Biol Ther | Review of certolizumab pegol for treating axial spondyloarthritis |
| [38503473](https://pubmed.ncbi.nlm.nih.gov/38503473/) | 2024 | Systematic Review | Ann Rheum Dis | Efficacy/safety review informing 2023 EULAR psoriatic arthritis recommendations |
| [31969328](https://pubmed.ncbi.nlm.nih.gov/31969328/) | 2020 | Guideline (EULAR) | Ann Rheum Dis | 2019 update of EULAR RA management recommendations with synthetic/biologic DMARDs |
| [37423647](https://pubmed.ncbi.nlm.nih.gov/37423647/) | 2023 | RCT | Ann Rheum Dis | NORD-STAR trial: certolizumab pegol vs abatacept, tocilizumab or active conventional therapy in early RA |
| [33268527](https://pubmed.ncbi.nlm.nih.gov/33268527/) | 2020 | RCT | BMJ | Phase IV comparison of active conventional treatment vs three biologics in early RA |
| [35296532](https://pubmed.ncbi.nlm.nih.gov/35296532/) | 2022 | Long-term follow-up (Phase 3 extension) | RMD Open | 3-year safety/outcomes of CZP in non-radiographic axSpA (C-axSpAnd) |
| [24919863](https://pubmed.ncbi.nlm.nih.gov/24919863/) | 2014 | Review | Drugs | Established EU/US indications for CZP: axSpA (AS and nr-axSpA) and psoriatic arthritis |
| [34786446](https://pubmed.ncbi.nlm.nih.gov/34786446/) | 2021 | Case Report | JAAD Case Reports | Sole positive efficacy signal: CZP for leg ulcers due to rheumatoid vasculitis |
| [31990069](https://pubmed.ncbi.nlm.nih.gov/31990069/) | 2020 | Case Report (adverse reaction) | J Clin Pharm Ther | Hypocomplementemic urticarial vasculitis **induced** during CZP treatment — contradicts vasculitis-indication hypothesis |

## Australia Market Information

Certolizumab pegol currently has **no ARTG entries** and is **not marketed in Australia**. All 10 predicted indications above would therefore require a new market-entry registration pathway rather than an indication-extension of an existing local product.

## Safety Considerations

No TFDA/TGA Product Information data (key warnings, contraindications, or drug interactions) was returned for this drug in the Evidence Pack — this is logged as a **Blocking** data gap (DG001) that prevents formal S1 safety screening. Please refer to the TGA-approved Product Information (PI), once registration is pursued, for authoritative safety information.

In the interim, literature captured in this Evidence Pack surfaces class-level safety signals worth flagging for any repurposing decision:

- **Paradoxical vasculitis induction**: multiple case reports describe certolizumab pegol *causing* leukocytoclastic vasculitis, hypocomplementemic urticarial vasculitis, medium-vessel vasculitis, and rapidly progressive glomerulonephritis (PMID 31990069, 28405087, 41158918, 32687015) — directly relevant to, and contradicting, the rheumatoid vasculitis prediction.
- **Infection risk**: a comparative review of immune-modulatory drug SmPC data highlights serious infection as a recurring concern across this drug class (PMID 36418084).
- **Mechanistic contraindication signal**: anti-TNF agents are known to increase risk of mycobacterial reactivation, which is directly counter-indicated in patients with IL-12/23 pathway defects (e.g. mendelian susceptibility to mycobacterial disease, rank 7) — this should be treated as a safety exclusion, not a treatment opportunity.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for inflammatory spondylopathy / vertebral disease only) — **Research Question** (polyarticular JIA, tenosynovitis) — **Hold** (rheumatoid vasculitis, mendelian susceptibility to mycobacterial disease, and all structural/congenital predictions)

**Rationale:**
- Inflammatory spondylopathy and vertebral disease are backed by ≥2 completed Phase 3 RCTs plus systematic reviews (L1), and represent an established anti-TNF class indication simply awaiting Australian market registration — the clearest actionable opportunity in this pack.
- Polyarticular JIA and tenosynovitis have plausible mechanisms but insufficient published evidence (single unpublished-result trial, or no trials at all) to move past a research question.
- Rheumatoid vasculitis has a strong TxGNN score but is contradicted by the balance of safety literature, which shows the drug can induce rather than treat vasculitic disease; and mendelian susceptibility to mycobacterial disease represents a probable contraindication rather than an indication. The remaining structural/congenital predictions have zero supporting evidence and are best explained as knowledge-graph noise.

**To proceed, the following is needed:**
- TGA-approved Product Information (PI) — warnings, contraindications, and drug interaction data (currently a Blocking data gap, DG001)
- Detailed mechanism-of-action documentation from DrugBank (DG002)
- Published results for the polyarticular JIA Phase 3 trial (NCT01550003) before advancing that indication
- A formal causality review reconciling the vasculitis-induction case reports against the single positive case report before any further work on the rheumatoid vasculitis hypothesis
- Confirmation that IL-12/23 pathway deficiency is listed as a contraindication/precaution in any future PI, given the mechanistic conflict identified above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

