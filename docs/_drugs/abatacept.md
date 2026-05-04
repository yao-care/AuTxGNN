---
layout: default
title: Abatacept
parent: 僅模型預測 (L5)
nav_order: 12
evidence_level: L5
indication_count: 10
---

# Abatacept
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

# AuTxGNN Drug Repurposing Evidence Report

## Abatacept (DB01281) — Multi-Indication Analysis

**Report ID**: AU-DB01281-multi  
**Version**: v4  
**Date Generated**: 3 April 2026  
**Data Cutoff**: 3 April 2026  
**Evidence Sources Queried**: DrugBank, ClinicalTrials.gov, PubMed, ICTRP

---

## 1. Executive Summary

This report presents the TxGNN knowledge-graph-based drug repurposing predictions for **abatacept** across ten candidate disease indications. Abatacept is a selective T-cell co-stimulation modulator (CTLA-4-Ig fusion protein) primarily approved internationally for rheumatoid arthritis (RA), psoriatic arthritis (PsA), and polyarticular juvenile idiopathic arthritis (pJIA).

### Key Findings at a Glance

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|:----:|----------------------|:-----------:|:--------------:|:--------------:|----------------|
| 1 | Rheumatoid vasculitis | 0.9991 | L4 | S1 | Research Question |
| 2 | Ankylosing spondylitis | 0.9991 | L3 | S1 | **Hold** |
| 3 | Hypermobility of coccyx | 0.9987 | L5 | S0 | Hold |
| 4 | Inflammatory spondylopathy | 0.9984 | L2 | S2 | **Proceed with Guardrails** |
| 5 | Kümmell disease | 0.9984 | L5 | S0 | Hold |
| 6 | Polyarticular juvenile rheumatoid arthritis | 0.9983 | **L1** | **S3** | **Proceed with Guardrails** |
| 7 | Vertebral disease | 0.9968 | L5 | S0 | Hold |
| 8 | Spondyloarthropathy, susceptibility to | 0.9965 | L4 | S0 | Hold |
| 9 | Brachydactyly-syndactyly syndrome | 0.9950 | L5 | S0 | Hold |
| 10 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 0.9948 | L5 | S0 | Hold |

**Summary**: Of ten predicted indications, **two** warrant active pursuit. Polyarticular JIA (Rank 6) is already a globally approved indication with Level 1 evidence, validating the TxGNN model. Inflammatory spondylopathy (Rank 4) has Level 2 evidence and Phase 3 trial data, primarily through the psoriatic arthritis sub-type, for which abatacept is already approved. One indication (rheumatoid vasculitis) merits formulation as a research question. The remaining seven predictions lack mechanistic plausibility or supporting clinical evidence and are placed on hold.

### TGA Registration Status

Abatacept is registered on the Australian Register of Therapeutic Goods (ARTG) and marketed in Australia under the brand name **Orencia®** (Bristol-Myers Squibb). TGA-approved indications include rheumatoid arthritis and polyarticular juvenile idiopathic arthritis (pJIA). Abatacept is available as both intravenous infusion and subcutaneous injection formulations.

---

## 2. Drug Information

| Parameter | Detail |
|-----------|--------|
| **INN (Generic Name)** | Abatacept |
| **DrugBank ID** | DB01281 |
| **Australian Brand Name** | Orencia® |
| **Manufacturer** | Bristol-Myers Squibb |
| **Drug Class** | Selective T-cell co-stimulation modulator (biologic DMARD) |
| **Molecular Type** | CTLA-4-Ig fusion protein |
| **Route of Administration** | Intravenous (IV); Subcutaneous (SC) |
| **Mechanism of Action** | [Data Gap — see §2.1] |

### 2.1 Mechanism of Action (Reconstructed from Literature)

> ⚠️ **Data Gap DG002**: Full MOA data was not retrieved from DrugBank API. The following is reconstructed from published literature.

Abatacept is a soluble fusion protein comprising the extracellular domain of human cytotoxic T-lymphocyte-associated antigen 4 (CTLA-4) linked to the modified Fc portion of human immunoglobulin G1 (IgG1). It selectively modulates T-cell co-stimulation by binding to CD80/CD86 on antigen-presenting cells, thereby blocking interaction with CD28 on T cells. This inhibits T-cell activation, downstream cytokine production (including TNF-α, IL-2, IL-6, and IFN-γ), and the propagation of autoimmune inflammatory cascades.

### 2.2 Current TGA-Approved Indications

- **Rheumatoid arthritis (RA)**: Moderate-to-severe active RA in adults with inadequate response to DMARDs including methotrexate or TNF inhibitors
- **Polyarticular juvenile idiopathic arthritis (pJIA)**: Moderate-to-severe active pJIA in patients aged ≥2 years with inadequate response to prior therapy

### 2.3 International Approvals (Not Yet TGA-Approved for These)

- **Psoriatic arthritis (PsA)**: FDA-approved (2017); EMA-approved
- **Prevention of acute graft-versus-host disease (aGVHD)**: FDA-approved (2021)

---

## 3. Predicted New Indications — Detailed Analysis

---

### 3.1 Rank 6 — Polyarticular Juvenile Rheumatoid Arthritis

| Parameter | Value |
|-----------|-------|
| **TxGNN Score** | 0.9983 (Rank 2,693) |
| **Evidence Level** | **L1** (Multiple Phase 3 RCTs, systematic reviews, meta-analyses) |
| **Decision Stage** | **S3** (Advanced — approved indication globally) |
| **Recommendation** | **Proceed with Guardrails** |

#### 3.1.1 Biological Rationale

Polyarticular JIA is a T-cell-mediated autoimmune arthritis. Abatacept directly inhibits T-cell co-stimulation via CTLA-4-Ig, blocking the key pathogenic mechanism. This represents an extremely strong mechanistic match and is, in fact, an already approved indication — serving as a positive control that validates the TxGNN prediction model.

#### 3.1.2 Clinical Trial Evidence

| NCT ID | Phase | Design | N | Status | Relevance |
|--------|-------|--------|---|--------|-----------|
| **NCT00095173** | Phase 3 | Randomised withdrawal, multinational | 214 | **Completed** | **A** — Pivotal registration study |
| **NCT01844518** | Phase 3 | Open-label, SC formulation | 219 | **Completed** | **A** — PK, efficacy, safety of SC route |
| **NCT01835470** | Phase 3 | Open-label, Japanese paediatrics | 23 | **Completed** | **A** — Regional PK/efficacy data |
| NCT02840175 | Phase 3 | Treatment tapering study | 62 | Completed | B — Maintenance strategy |
| NCT06654882 | Phase 3 | Sequential therapy after TNFi failure | 400 | Recruiting | B — Comparative effectiveness |

#### 3.1.3 Key Published Literature

- **Brunner et al. (2020)** — PMID 33029724: Systematic review of abatacept treatment in pJIA. *Tier 1*.
- **Amarilyo et al. (2016)** — PMID 27989499: Meta-analysis of biologic agents in pJIA via randomised withdrawal trials. *Tier 1*.
- **Ruperto et al. (2023)** — PMID 37453737: Abatacept monotherapy and combination with MTX in pJIA, Phase 3 analysis. *Tier 1*.
- **Nozawa et al. (2025)** — PMID 39972375: All-case post-marketing surveillance in Japanese pJIA patients. *Tier 1*.
- **Zimmer & Horneff (2025)** — PMID 39946290: Safety update on biologics in pJIA. *Tier 2*.

#### 3.1.4 Australian Context

Abatacept (Orencia®) is **already TGA-approved and PBS-listed** for pJIA in Australia. This prediction validates the TxGNN model's ability to identify genuine drug–disease relationships.

#### 3.1.5 Assessment

✅ **Model Validation**: This prediction confirms TxGNN's capacity to rediscover established therapeutic relationships. No further repurposing action is required as this is an approved indication.

---

### 3.2 Rank 4 — Inflammatory Spondylopathy

| Parameter | Value |
|-----------|-------|
| **TxGNN Score** | 0.9984 (Rank 2,613) |
| **Evidence Level** | **L2** (Phase 3 RCT data, clinical practice guidelines) |
| **Decision Stage** | **S2** (Evidence accumulating) |
| **Recommendation** | **Proceed with Guardrails** |

#### 3.2.1 Biological Rationale

Inflammatory spondylopathy is a broad category encompassing psoriatic arthritis (PsA), ankylosing spondylitis (AS), and related conditions. T-cell involvement varies by sub-type:

- **PsA (peripheral)**: T cells play a significant role in synovitis and enthesitis; abatacept is approved for PsA (FDA/EMA, not yet TGA)
- **Axial SpA/AS**: IL-23/IL-17 and TNF-α pathways predominate; T-cell co-stimulation blockade has shown limited efficacy
- **Enthesitis-related JIA**: Emerging data on biologic therapy including abatacept

#### 3.2.2 Clinical Trial Evidence

| NCT ID | Phase | Design | N | Status | Relevance |
|--------|-------|--------|---|--------|-----------|
| **NCT01860976** | **Phase 3** | Randomised, placebo-controlled (SC abatacept in PsA) | 489 | **Completed** | **A** — Pivotal PsA trial |
| **NCT00534313** | Phase 2B | Randomised, double-blind, placebo-controlled (PsA) | 191 | Terminated | Dose-finding in PsA |
| **NCT03419143** | Observational | Long-term real-world (ALTEA, Germany) | 190 | **Completed** | **A** — Real-world effectiveness |
| NCT04106804 | Phase 4 | Bone biomarkers in PsA | 20 | Unknown | A — Mechanistic |
| NCT00558506 | Phase 2 | Open-label pilot (AS) | 30 | Unknown | A — AS-specific but limited efficacy |
| NCT05413044 | Observational | Post-marketing safety (Sweden) | 140,706 | **Completed** | B — Large safety dataset |
| NCT05421442 | Observational | Post-marketing safety (Denmark) | 38,396 | **Completed** | B — Large safety dataset |

#### 3.2.3 Key Published Literature

- **Singh et al. (2019)** — PMID 30499246: ACR/NPF Clinical Practice Guideline for PsA treatment. *Tier 1*.
- **Zuckerman et al. (2025)** — PMID 39992258: Meta-analysis of abatacept and malignancy risk across indications. *Tier 1*.
- **Zizzo et al. (2018)** — PMID 29737909: Biological and clinical profiles of abatacept responders in PsA.
- **Song et al. (2011)** — PMID 21415053: Open-label pilot study of abatacept in AS — limited efficacy observed. *Tier 1*.
- **Torgutalp & Poddubnyy (2018)** — PMID 31171316: Review noting abatacept is not effective in axial SpA.

#### 3.2.4 Australian Context

- **PsA**: Abatacept is **not yet TGA-approved for PsA** in Australia, despite FDA/EMA approval. This represents a genuine repurposing opportunity for Australian clinical practice.
- **Axial SpA**: Evidence suggests abatacept is **not effective** for axial disease. A Phase 2 pilot (NCT00558506) showed limited efficacy and no Phase 3 follow-up occurred.

#### 3.2.5 Assessment

⚠️ **Nuanced Recommendation**: For the PsA sub-type of inflammatory spondylopathy, abatacept has robust Phase 3 evidence and international approval. Australian clinicians and the TGA should consider the existing global regulatory approvals. For axial SpA, the evidence is **negative** — abatacept should not be pursued.

**Suggested Actions**:
1. Monitor for potential TGA submission for PsA indication by Bristol-Myers Squibb
2. Consider inclusion in Australian rheumatology clinical practice guidelines for PsA
3. Do **not** pursue investigation for axial SpA

---

### 3.3 Rank 1 — Rheumatoid Vasculitis

| Parameter | Value |
|-----------|-------|
| **TxGNN Score** | 0.9991 (Rank 1,617) |
| **Evidence Level** | L4 (Case reports only) |
| **Decision Stage** | S1 (Initial screening) |
| **Recommendation** | **Research Question** |

#### 3.3.1 Biological Rationale

Rheumatoid vasculitis (RV) is a severe extra-articular manifestation of RA involving immune complex deposition and T-cell-mediated vascular wall inflammation. Abatacept's inhibition of T-cell activation theoretically targets part of this pathogenic cascade. However, the literature presents **contradictory signals**:

- **Positive signals**: Case reports of rapid clinical improvement with abatacept in RV (Fujii et al., 2012, PMID 22124545; Al Attar & Shaver, 2018, PMID 29930884)
- **Negative signals**: Reports of **new-onset RV during abatacept therapy** (Carvajal Alegria et al., 2016, PMID 27052429; Weber et al., 2018, PMID 30119075)

#### 3.3.2 Clinical Trial Evidence

No clinical trials directly investigating abatacept for rheumatoid vasculitis were identified. The single retrieved trial (NCT07138898) addresses perioperative immunosuppressant management and is of low relevance (Grade C).

#### 3.3.3 Key Published Literature

| PMID | Year | Type | Key Finding |
|------|------|------|-------------|
| 22124545 | 2012 | Case report | Rapid efficacy of abatacept in RV (Tier 2) |
| 29930884 | 2018 | Case report/series | Abatacept as therapeutic option for RV (Tier 2) |
| 27052429 | 2016 | Case report | **New-onset RV during abatacept therapy** (Tier 2) |
| 30119075 | 2018 | Case report | RA-associated orbital vasculitis **during abatacept** (Tier 2) |
| 36418100 | 2023 | Case report | ANCA-associated nephritis during abatacept therapy (Tier 3) |

#### 3.3.4 Assessment

🔬 **Research Question**: The conflicting evidence — both therapeutic benefit and paradoxical induction of vasculitis — makes this an intriguing but unresolved research question. The absence of any controlled trials and the existence of only case-level evidence (L4) precludes clinical translation.

**Suggested Actions**:
1. Formulate as a formal research question for Australian rheumatology research networks (e.g., ARAD — Australian Rheumatology Association Database)
2. Prospective case series or registry-based analysis of RV outcomes in abatacept-treated RA patients
3. Mechanistic studies to understand the paradoxical vasculitis signals

---

### 3.4 Rank 2 — Ankylosing Spondylitis

| Parameter | Value |
|-----------|-------|
| **TxGNN Score** | 0.9991 (Rank 1,622) |
| **Evidence Level** | L3 (Phase 2 open-label pilot study) |
| **Decision Stage** | S1 (Initial screening) |
| **Recommendation** | **Hold** |

#### 3.4.1 Biological Rationale

AS is primarily driven by the HLA-B27-associated IL-23/IL-17 axis and TNF-α signalling. T-cell co-stimulation plays a relatively minor role. A Phase 2 open-label pilot study (Song et al., 2011, PMID 21415053; NCT00558506, n=30) showed **limited efficacy**, and no Phase 3 trial was pursued. Multiple review articles explicitly state that abatacept is **not effective** in axial spondyloarthritis (Sieper, 2016, PMID 27856659; Kiltz et al., 2012, PMID 22450391).

#### 3.4.2 Assessment

🛑 **Hold — Negative Evidence**: Clinical investigation has been conducted and the results were unfavourable. This pathway appears to have been appropriately abandoned. Not recommended for further investigation.

---

### 3.5 Rank 3 — Hypermobility of Coccyx

| Parameter | Value |
|-----------|-------|
| **TxGNN Score** | 0.9987 (Rank 2,187) |
| **Evidence Level** | L5 (No evidence) |
| **Decision Stage** | S0 (Not started) |
| **Recommendation** | **Hold** |

#### Assessment

🛑 **No Mechanistic Plausibility**: Coccygeal hypermobility is a structural/biomechanical condition involving ligamentous laxity or joint instability. There is no immune or inflammatory mechanism. Abatacept has no known effect on these pathways. No clinical trials or literature exist. **Not recommended for investigation.**

---

### 3.6 Rank 5 — Kümmell Disease

| Parameter | Value |
|-----------|-------|
| **TxGNN Score** | 0.9984 (Rank 2,672) |
| **Evidence Level** | L5 (No evidence) |
| **Decision Stage** | S0 (Not started) |
| **Recommendation** | **Hold** |

#### Assessment

🛑 **No Mechanistic Plausibility**: Kümmell disease is post-traumatic vertebral avascular necrosis — a vascular/skeletal condition without immune pathogenesis. Abatacept has no known mechanism to address ischaemic bone necrosis or vascular reconstruction. **Not recommended for investigation.**

---

### 3.7 Rank 7 — Vertebral Disease

| Parameter | Value |
|-----------|-------|
| **TxGNN Score** | 0.9968 (Rank 4,302) |
| **Evidence Level** | L5 (No relevant evidence) |
| **Decision Stage** | S0 (Not started) |
| **Recommendation** | **Hold** |

#### Assessment

🛑 **Overly Broad Category**: "Vertebral disease" is an imprecise disease descriptor encompassing degenerative, infectious, neoplastic, and metabolic aetiologies. All retrieved literature pertains to RA (abatacept's approved indication) rather than vertebral disease per se. No mechanistic rationale exists for the vast majority of vertebral pathologies. **Not recommended for investigation.**

---

### 3.8 Rank 8 — Spondyloarthropathy, Susceptibility To

| Parameter | Value |
|-----------|-------|
| **TxGNN Score** | 0.9965 (Rank 4,613) |
| **Evidence Level** | L4 (Limited indirect evidence) |
| **Decision Stage** | S0 (Not started) |
| **Recommendation** | **Hold** |

#### Assessment

🛑 **Not a Treatable Entity**: "Susceptibility to spondyloarthropathy" represents a genetic predisposition (e.g., HLA-B27 carriage), not a disease suitable for pharmacological intervention. While abatacept modulates T-cell co-stimulation and could theoretically influence disease onset in susceptible individuals, there is no clinical framework for treating genetic susceptibility with immunomodulatory biologics. **Not recommended for investigation.**

---

### 3.9 Rank 9 — Brachydactyly-Syndactyly Syndrome

| Parameter | Value |
|-----------|-------|
| **TxGNN Score** | 0.9950 (Rank 5,948) |
| **Evidence Level** | L5 (No evidence) |
| **Decision Stage** | S0 (Not started) |
| **Recommendation** | **Hold** |

#### Assessment

🛑 **No Mechanistic Plausibility**: This is a congenital skeletal developmental anomaly driven by genetic mutations (e.g., HOXD13, GDF5). It is not an immune-mediated condition. No clinical or preclinical evidence exists. **Not recommended for investigation.**

---

### 3.10 Rank 10 — Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

| Parameter | Value |
|-----------|-------|
| **TxGNN Score** | 0.9948 (Rank 6,083) |
| **Evidence Level** | L5 (No evidence) |
| **Decision Stage** | S0 (Not started) |
| **Recommendation** | **Hold** |

#### Assessment

🛑 **No Mechanistic Plausibility**: This is an extremely rare congenital multi-system developmental syndrome involving ocular coloboma and proximal limb skeletal dysplasia. The condition is genetic/developmental in nature with no immune-mediated component. **Not recommended for investigation.**

---

## 4. Safety Considerations

### 4.1 Known Adverse Effects

> ⚠️ **Data Gap DG001**: TGA-specific Product Information (PI) warnings and contraindications were not retrieved. The following is based on internationally available safety data.

**Common adverse effects** (reported in clinical trials and post-marketing surveillance):
- Upper respiratory tract infections, nasopharyngitis
- Headache, nausea
- Injection site reactions (SC formulation)
- Infusion-related reactions (IV formulation)

**Serious adverse effects**:
- Serious infections (including pneumonia, urinary tract infections, cellulitis)
- Opportunistic infections (tuberculosis screening required prior to initiation)
- Malignancy: A 2025 meta-analysis (Zuckerman et al., PMID 39992258) across disease indications found no significantly increased overall malignancy risk
- Hepatitis B reactivation

**Large post-marketing safety studies**:
- **Swedish SRQ Register** (NCT05413044): n=140,706, completed — evaluated malignancy incidence
- **Danish DANBIO Register** (NCT05421442): n=38,396, completed — post-marketing safety monitoring

### 4.2 Contraindications

- [Data Gap — TGA PI not available]
- Internationally: hypersensitivity to abatacept or any excipient; active serious infections

### 4.3 Drug–Drug Interactions

| Parameter | Status |
|-----------|--------|
| **DDI Query** | Not found (DrugBank API) |
| **Known Class Interactions** | Concurrent use with TNF inhibitors or other biologics is not recommended due to increased infection risk |
| **Live Vaccines** | Contraindicated during and for 3 months following abatacept therapy |

### 4.4 Special Populations

- **Pregnancy**: Limited data; animal studies showed no teratogenicity; Australian category B2 (verify with current TGA PI)
- **Paediatrics**: Approved for pJIA (≥2 years); comprehensive safety data available from Phase 3 trials and post-marketing surveillance
- **Elderly**: No dose adjustment required; increased infection vigilance recommended

---

## 5. Data Gaps and Limitations

| Gap ID | Category | Item | Severity | Impact | Remediation |
|--------|----------|------|----------|--------|-------------|
| DG001 | Drug-Level | TGA PI warnings/contraindications | **Blocking** | Cannot complete S1 safety assessment | Download and parse TGA PI/CMI from TGA website |
| DG002 | Drug-Level | Mechanism of action (structured data) | High | Impacts mechanistic relevance analysis | Query DrugBank API for full pharmacology data |

### Additional Limitations

- **ANZCTR trials**: No Australian/New Zealand clinical trial registry (ANZCTR) searches were performed; relevant Australian investigator-initiated trials may exist
- **Route compatibility**: Not assessed for any predicted indication
- **Australian prescribing patterns**: PBS restrictions and Medicare Benefits Schedule implications not evaluated
- **Aboriginal and Torres Strait Islander health considerations**: Not assessed

---

## 6. Recommendations

### 6.1 Evidence Strength Summary

| Indication | Evidence Strength | Actionability |
|------------|-------------------|---------------|
| Polyarticular JIA | ★★★★★ (L1) | Already approved — model validation |
| Inflammatory spondylopathy (PsA sub-type) | ★★★★☆ (L2) | Potential TGA submission opportunity |
| Rheumatoid vasculitis | ★★☆☆☆ (L4) | Research question — conflicting signals |
| Ankylosing spondylitis | ★★★☆☆ (L3) | Negative evidence — abandoned pathway |
| All others (Ranks 3, 5, 7–10) | ★☆☆☆☆ (L5) | No plausibility — not recommended |

### 6.2 Priority Actions

1. **Immediate**: Resolve Data Gap DG001 by obtaining the current TGA-approved Product Information for Orencia® to enable complete safety profiling
2. **Short-term**: Investigate TGA/PBS status of abatacept for psoriatic arthritis; liaise with Bristol-Myers Squibb Australia regarding potential TGA submission for PsA indication
3. **Medium-term**: Engage with Australian rheumatology research networks (ARAD, ARA) to explore a prospective registry analysis of abatacept outcomes in rheumatoid vasculitis
4. **Model refinement**: The successful identification of pJIA (Rank 6) validates TxGNN predictions for T-cell-mediated autoimmune conditions. However, five of ten predictions (Ranks 3, 5, 7, 9, 10) lacked any mechanistic plausibility, suggesting the model may benefit from incorporating biological pathway annotations as a filtering layer

### 6.3 Relevant Australian Research Institutions

- **Australian Rheumatology Association (ARA)** — national clinical practice guidelines
- **ARAD (Australian Rheumatology Association Database)** — longitudinal registry for outcomes research
- **Monash University Centre for Inflammatory Diseases** — translational immunology research
- **Walter and Eliza Hall Institute (WEHI)** — immunology and autoimmunity
- **NHMRC Clinical Trials Centre, University of Sydney** — clinical trial infrastructure

---

## 7. TxGNN Model Performance Notes

This evidence pack provides an instructive view of TxGNN model behaviour:

- **True positive**: Polyarticular JIA (Rank 6) is a confirmed approved indication — strong validation
- **Partially valid**: Inflammatory spondylopathy (Rank 4) captures the PsA relationship but conflates axial and peripheral disease
- **Interesting signal**: Rheumatoid vasculitis (Rank 1) identifies a plausible but unvalidated immune-mediated target
- **False positive — negative clinical data**: Ankylosing spondylitis (Rank 2) has been clinically tested and found ineffective
- **False positives — no plausibility**: Five predictions (Ranks 3, 5, 7, 9, 10) represent structural/developmental/genetic conditions with no immune pathogenesis

**Overall model precision (clinically actionable predictions)**: 3/10 (30%)

---

## Disclaimer

> **Research Use Only**: This report is generated for research purposes only and does not constitute medical advice. Drug repurposing predictions require clinical validation before therapeutic application. This is not a TGA-approved assessment. All predicted indications are computational hypotheses derived from knowledge graph analysis and require independent clinical and regulatory evaluation before any therapeutic application.
>
> Healthcare professionals should consult the current TGA-approved Product Information for Orencia® (abatacept) and relevant Australian clinical practice guidelines before making any prescribing decisions.
>
> This report has not been reviewed or endorsed by the Therapeutic Goods Administration (TGA), the Australian Rheumatology Association (ARA), or Bristol-Myers Squibb.

---

## Appendix A: Evidence Level Definitions

| Level | Definition | Typical Sources |
|-------|-----------|-----------------|
| **L1** | Multiple Phase 3 RCTs, systematic reviews, or meta-analyses | Pivotal registration trials, Cochrane reviews |
| **L2** | At least one Phase 3 RCT or multiple Phase 2 studies | Randomised controlled trials |
| **L3** | Phase 2 pilot studies or large observational studies | Open-label trials, registry analyses |
| **L4** | Case reports, case series, or expert opinion | Published case literature |
| **L5** | No clinical evidence identified | Computational prediction only |

## Appendix B: Decision Stage Definitions

| Stage | Definition |
|-------|-----------|
| **S0** | Not started — insufficient evidence or plausibility to initiate evaluation |
| **S1** | Initial screening — preliminary evidence review underway |
| **S2** | Evidence accumulating — active investigation warranted |
| **S3** | Advanced — substantial clinical evidence exists or indication is approved |

## Appendix C: Query Log Summary

A total of **33 queries** were executed across 5 data sources (TFDA, DDI, DrugBank, ClinicalTrials.gov, ICTRP, PubMed) on 9 March 2026. All queries returned successfully. Clinical trials were identified for 5 of 10 predicted indications; PubMed literature was retrieved for 6 of 10 indications.

---

*Generated by AuTxGNN — Australia Drug Repurposing Predictions*  
*Report version: v4 | Data cutoff: 3 April 2026*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

