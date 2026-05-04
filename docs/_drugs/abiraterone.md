---
layout: default
title: Abiraterone
parent: 僅模型預測 (L5)
nav_order: 14
evidence_level: L5
indication_count: 10
---

# Abiraterone
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

## Abiraterone — Multi-Indication Prediction Analysis

| Field | Detail |
|---|---|
| **Candidate ID** | TW-DB05812-multi |
| **Report Version** | v4 |
| **Date Generated** | 3 April 2026 |
| **Data Cutoff** | 3 April 2026 |
| **Data Sources Queried** | DrugBank, ClinicalTrials.gov, PubMed, ICTRP, TFDA |

---

## 1. Executive Summary

Abiraterone (DrugBank ID: DB05812) is a selective CYP17A1 inhibitor currently approved internationally for the treatment of metastatic castration-resistant prostate cancer (mCRPC). The TxGNN knowledge graph model generated 10 predicted new indications for abiraterone, spanning migraine subtypes, pulmonary hypertension, leprosy, rheumatoid arthritis, and several rare conditions.

**Overall Assessment: No actionable repurposing candidates identified.**

All 10 predictions received a recommendation of **"Hold"** (9 of 10) or **"Research Question"** (1 of 10 — pulmonary hypertension). The mechanistic rationale linking CYP17A1 inhibition to any of the predicted conditions ranges from non-existent to contradictory. Critically, for several predictions (rheumatoid arthritis, nephrogenic syndrome of inappropriate antidiuresis), the expected pharmacological effect of abiraterone would theoretically *worsen* rather than improve the condition.

**TGA Registration Status:** Abiraterone acetate is registered on the Australian Register of Therapeutic Goods (ARTG) under brand names including Zytiga® (Janssen) for use in combination with prednisone/prednisolone for metastatic castration-resistant prostate cancer and metastatic hormone-sensitive prostate cancer. Multiple generic formulations are also listed. The evidence pack data originates from the Taiwanese regulatory context (TFDA), where abiraterone is listed as "not marketed" with zero licences.

**Key Data Gaps:** TGA/TFDA label warnings, contraindications, and detailed mechanism of action data were not available in this evidence pack, representing a blocking gap for formal safety assessment.

---

## 2. Drug Information

| Parameter | Detail |
|---|---|
| **INN (Generic Name)** | Abiraterone |
| **DrugBank ID** | DB05812 |
| **Australian Brand Names** | Zytiga® (Janssen-Cilag); generic formulations available |
| **Chemical Class** | Steroidal CYP17A1 (17α-hydroxylase/C17,20-lyase) inhibitor |
| **Mechanism of Action** | [Data Gap — not provided in evidence pack] |
| **Known MOA (from literature)** | Irreversible inhibition of CYP17A1, blocking androgen biosynthesis at the adrenal and intratumoral level. Reduces circulating testosterone, DHEA, and androstenedione. Compensatory mineralocorticoid excess occurs due to upstream accumulation of steroid precursors. |
| **TGA-Approved Indications** | Metastatic castration-resistant prostate cancer (mCRPC); metastatic high-risk hormone-sensitive prostate cancer (mHSPC) — in combination with prednisone or prednisolone |
| **ARTG Status** | Registered (multiple entries) |
| **Formulation** | Oral tablets (250 mg, 500 mg) |
| **TFDA (Taiwan) Status** | Not marketed (0 licences) |

---

## 3. Predicted New Indications

### 3.1 Summary Table

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation | Mechanistic Plausibility |
|---|---|---|---|---|---|---|
| 1 | Migraine disorder | 0.988 | L5 | S0 | **Hold** | Very weak |
| 2 | Migraine with or without aura (susceptibility) | 0.988 | L5 | S0 | **Hold** | Very weak |
| 3 | Migraine with brainstem aura | 0.986 | L5 | S0 | **Hold** | Very weak |
| 4 | Leprosy | 0.986 | L5 | S0 | **Hold** | None |
| 5 | Pulmonary hypertension | 0.984 | L4 | S1 | **Research Question** | Weak–contradictory |
| 6 | Nephrogenic syndrome of inappropriate antidiuresis | 0.982 | L5 | S0 | **Hold** | Very weak (harmful direction) |
| 7 | Rheumatoid arthritis | 0.981 | L5 | S0 | **Hold** | Contradictory |
| 8 | Kyphoscoliotic heart disease | 0.981 | L5 | S0 | **Hold** | None |
| 9 | Atrophoderma vermiculata | 0.977 | L5 | S0 | **Hold** | Very weak, speculative |
| 10 | Ulerythema ophryogenesis | 0.975 | L5 | S0 | **Hold** | Very weak, speculative |

### 3.2 Detailed Indication Analyses

---

#### Rank 1 — Migraine Disorder

- **TxGNN Score:** 0.988 (rank 11,869)
- **Evidence Level:** L5 (computational prediction only)
- **Clinical Trials:** None identified (ClinicalTrials.gov: 0; ICTRP: 0)
- **Literature:** None identified (PubMed: 0 results)
- **Mechanistic Assessment:** Very weak. CYP17A1 inhibition reduces androgens. While sex hormone fluctuations (particularly oestrogen) are associated with migraine, abiraterone primarily affects the androgen pathway rather than the core migraine pathophysiology involving CGRP and the trigeminovascular system. Furthermore, known adverse effects of abiraterone — including mineralocorticoid excess, hypokalaemia, and fluid retention — may exacerbate headache.
- **Recommendation:** **Hold.** No supporting evidence. Mechanistic rationale is inadequate.

---

#### Rank 2 — Migraine With or Without Aura (Susceptibility)

- **TxGNN Score:** 0.988 (rank 12,386)
- **Evidence Level:** L5 (computational prediction only)
- **Clinical Trials:** None identified
- **Literature:** 20 PubMed results returned, however **all 20 articles are false positives** — they relate to epilepsy genetics, susceptibility to seizures, and paediatric epilepsy models, with no direct relevance to abiraterone or migraine treatment. The only tangentially relevant paper (PMID 33856647, Gotra et al. 2021) discusses shared genetic and molecular mechanisms between epilepsy and migraine but does not reference the CYP17A1 pathway.
- **Mechanistic Assessment:** Very weak. Same rationale as Rank 1. The literature set does not support any mechanistic connection.
- **Recommendation:** **Hold.** Retrieved literature is not relevant; likely a PubMed keyword matching artefact on the term "susceptibility."

---

#### Rank 3 — Migraine With Brainstem Aura

- **TxGNN Score:** 0.986 (rank 13,674)
- **Evidence Level:** L5
- **Clinical Trials:** None identified
- **Literature:** None identified
- **Mechanistic Assessment:** Very weak. Brainstem aura migraine involves brainstem dysfunction; no known link to androgen biosynthesis inhibition.
- **Recommendation:** **Hold.**

---

#### Rank 4 — Leprosy

- **TxGNN Score:** 0.986 (rank 13,923)
- **Evidence Level:** L5
- **Clinical Trials:** None identified
- **Literature:** None identified
- **Mechanistic Assessment:** No plausible connection. Leprosy is caused by *Mycobacterium leprae* infection and requires antimicrobial therapy (dapsone, rifampicin, clofazimine). CYP17A1 inhibition has no known antimycobacterial activity nor relevant immunomodulatory mechanism for this infection.
- **Recommendation:** **Hold.**

---

#### Rank 5 — Pulmonary Hypertension ⭐ (Highest evidence level in this set)

- **TxGNN Score:** 0.984 (rank 15,720)
- **Evidence Level:** L4
- **Decision Stage:** S1
- **Clinical Trials:** 1 result (NCT01961843) — **false positive.** This is a prostate cancer circulating tumour cell study, unrelated to pulmonary hypertension treatment. Relevance grade: C.
- **Literature:** 5 PubMed results — **all are prostate cancer studies** involving abiraterone. None investigate pulmonary hypertension as a therapeutic target. Key papers include STAMPEDE platform RCTs (PMID 34953525), ACIS trial (PMID 34600602), and a cardio-oncology retrospective study on angiotensin inhibitors during abiraterone therapy (PMID 33869068).
- **Mechanistic Assessment:** Weak to contradictory.
  - Sex hormones have a recognised but complex relationship with pulmonary arterial hypertension (PAH): female sex confers higher incidence, while male sex confers worse prognosis.
  - DHEA (a CYP17A1 downstream metabolite) has shown pulmonary vasculoprotective effects in animal models. Abiraterone *reduces* DHEA, which could theoretically be **harmful** rather than beneficial.
  - CYP17A1 is expressed in pulmonary vascular smooth muscle, but the directionality of effect is uncertain.
- **Recommendation:** **Research Question** — but with significant caveats. The mechanistic direction is potentially counterproductive. This warrants literature monitoring only; no preclinical or clinical investigation is recommended at this stage.

---

#### Rank 6 — Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)

- **TxGNN Score:** 0.982 (rank 16,832)
- **Evidence Level:** L5
- **Clinical Trials:** None identified
- **Literature:** None identified
- **Mechanistic Assessment:** Very weak, potentially harmful. NSIAD results from gain-of-function mutations in AVPR2. Abiraterone's known adverse effect of mineralocorticoid excess can cause fluid retention and electrolyte disturbance, which would likely **worsen** this condition.
- **Recommendation:** **Hold.** Predicted pharmacological effect directionally harmful.

---

#### Rank 7 — Rheumatoid Arthritis

- **TxGNN Score:** 0.981 (rank 17,720)
- **Evidence Level:** L5
- **Clinical Trials:** None identified
- **Literature:** None identified
- **Mechanistic Assessment:** Contradictory. Androgens generally exert immunosuppressive and anti-inflammatory effects. Low androgen states are associated with *increased* rheumatoid arthritis risk. By reducing androgens, abiraterone would theoretically **promote** autoimmune inflammation rather than suppress it.
- **Recommendation:** **Hold.** Mechanistic direction opposes therapeutic intent.

---

#### Rank 8 — Kyphoscoliotic Heart Disease

- **TxGNN Score:** 0.981 (rank 17,838)
- **Evidence Level:** L5
- **Clinical Trials:** None identified
- **Literature:** None identified
- **Mechanistic Assessment:** None. This is a structural/mechanical condition resulting from spinal deformity causing cardiopulmonary restriction. No pharmacological pathway exists through which CYP17A1 inhibition could address thoracic structural abnormalities.
- **Recommendation:** **Hold.**

---

#### Rank 9 — Atrophoderma Vermiculata

- **TxGNN Score:** 0.977 (rank 21,340)
- **Evidence Level:** L5
- **Clinical Trials:** None identified
- **Literature:** None identified
- **Mechanistic Assessment:** Very weak, speculative. This rare follicular keratinisation disorder could theoretically be influenced by reduced sebaceous activity from androgen suppression, but the core pathology is keratinisation abnormality, not androgen excess. Anti-androgen therapy has not been reported in the literature for this condition.
- **Recommendation:** **Hold.**

---

#### Rank 10 — Ulerythema Ophryogenesis

- **TxGNN Score:** 0.975 (rank 22,196)
- **Evidence Level:** L5
- **Clinical Trials:** None identified
- **Literature:** None identified
- **Mechanistic Assessment:** Very weak, speculative. This keratosis pilaris variant involving the eyebrow region shares the same follicular keratinisation disorder spectrum as Rank 9. The androgen connection is equally indirect and unsupported.
- **Recommendation:** **Hold.**

---

## 4. Evidence Summary

### 4.1 Clinical Trial Evidence

| Source | Total Hits | Relevant Hits | Notes |
|---|---|---|---|
| ClinicalTrials.gov | 1 | 0 | 1 false positive (prostate cancer CTC study) |
| ANZCTR / ICTRP | 0 | 0 | No Australian or international registry matches |

No clinical trials were identified investigating abiraterone for any of the 10 predicted indications.

### 4.2 Published Literature

| Source | Total Hits | Relevant Hits | Notes |
|---|---|---|---|
| PubMed | 25 | 0 | 20 epilepsy/genetics papers (false positives from "susceptibility" keyword); 5 prostate cancer papers |

**Critical Observation:** The PubMed literature retrieval contains significant noise. The 20 papers associated with "migraine with or without aura, susceptibility to" are overwhelmingly epilepsy-focused, likely resulting from MeSH term overlap on "susceptibility." The 5 papers associated with pulmonary hypertension are all prostate cancer treatment studies that mention abiraterone but do not investigate pulmonary hypertension as a therapeutic target.

### 4.3 Australian-Specific Studies

No Australian-specific studies were identified for any predicted indication.

---

## 5. Safety Considerations

### 5.1 Known Adverse Effects

> ⚠️ **Data Gap (DG001 — Blocking):** TGA/TFDA label warnings and contraindications were not available in this evidence pack. The information below is derived from general pharmacological knowledge.

**Common adverse effects of abiraterone (from international prescribing information):**
- Mineralocorticoid-related: hypertension, hypokalaemia, fluid retention/oedema
- Hepatotoxicity (elevated ALT/AST)
- Fatigue
- Joint discomfort
- Hot flushes
- Urinary tract infections
- Cardiac disorders (including cardiac failure, atrial fibrillation)

### 5.2 Contraindications

- **[Data Gap]** — TGA Product Information not parsed
- Known international contraindications include: severe hepatic impairment (Child-Pugh C), pregnancy/women of childbearing potential (Category X — teratogenic)

### 5.3 Drug–Drug Interactions

| Parameter | Result |
|---|---|
| DDI Query Status | Not found |
| Total Interactions | 0 (data gap) |

> **Note:** Abiraterone is a known inhibitor of CYP2D6 and CYP2C8. Clinically significant interactions are expected with substrates of these enzymes. Full DDI profiling is a required data gap remediation step.

### 5.4 Safety Concerns Specific to Predicted Indications

| Indication | Safety Concern |
|---|---|
| Migraine (Ranks 1–3) | Mineralocorticoid excess (hypertension, hypokalaemia) may worsen headache; unacceptable risk–benefit for a non-life-threatening condition |
| Pulmonary hypertension (Rank 5) | Fluid retention and cardiac adverse effects could exacerbate haemodynamic compromise |
| NSIAD (Rank 6) | Mineralocorticoid excess would worsen fluid retention — directly counterproductive |
| Rheumatoid arthritis (Rank 7) | Androgen reduction may worsen autoimmune inflammation |
| All indications | Abiraterone's adverse effect profile is acceptable in the context of advanced prostate cancer but disproportionate for the non-oncological conditions predicted |

---

## 6. Data Gaps

| ID | Category | Item | Severity | Impact | Remediation |
|---|---|---|---|---|---|
| DG001 | Drug Level | TGA/TFDA Label Warnings & Contraindications | **Blocking** | Cannot enter S1 safety assessment | Download and parse TGA PI document |
| DG002 | Drug Level | Mechanism of Action (MOA) detail | High | Affects mechanistic association analysis | Query DrugBank API for complete MOA data |

---

## 7. Recommendations

### 7.1 Evidence Strength Assessment

| Metric | Value |
|---|---|
| Predictions at Evidence Level L5 (computational only) | 9 of 10 |
| Predictions at Evidence Level L4 | 1 of 10 (pulmonary hypertension) |
| Predictions with supporting clinical evidence | 0 of 10 |
| Predictions with plausible mechanistic rationale | 0 of 10 |
| Predictions with contradictory mechanistic direction | 3 of 10 (NSIAD, RA, potentially PAH) |

### 7.2 Overall Recommendation

**No repurposing candidates from this prediction set warrant further investigation at this time.**

The TxGNN model assigned high prediction scores (>0.975) to all 10 indications, yet none are supported by:
- Clinical trial evidence
- Relevant published literature
- Plausible mechanistic rationale

This result likely reflects a limitation of graph-based prediction models when applied to drugs with highly specific mechanisms (selective CYP17A1 inhibition) that do not generalise well to non-oncological therapeutic areas.

### 7.3 Suggested Next Steps

1. **Remediate data gaps** — Obtain TGA Product Information for complete safety profiling (DG001) and DrugBank MOA data (DG002) before any further assessment.
2. **No preclinical or clinical investigation recommended** for any of the 10 predicted indications.
3. **Refine PubMed search strategy** — The high false-positive rate in literature retrieval (particularly for "susceptibility"-containing disease terms) suggests the evidence collection pipeline may benefit from improved keyword specificity and relevance filtering.
4. **Model feedback** — These results should be fed back into the TxGNN model evaluation pipeline to assess whether CYP17A1 inhibitors systematically generate low-quality predictions for non-oncological conditions.

### 7.4 Relevant Australian Research Context

- Abiraterone is well-studied in Australian prostate cancer research through the ANZUP (Australian and New Zealand Urogenital and Prostate Cancer Trials Group) network.
- No Australian research groups have published on abiraterone repurposing for any of the predicted indications.
- Pulmonary hypertension research is active at centres including the Victor Chang Cardiac Research Institute (Sydney) and the National Heart Foundation, but there is no indication of interest in CYP17A1-targeted approaches.

---

## 8. Query Log Summary

A total of **33 queries** were executed across 5 data sources on 10 March 2026:

| Source | Queries | Results Found | Relevant Results |
|---|---|---|---|
| TFDA | 1 | 0 | 0 |
| DDI | 1 | 0 | 0 |
| DrugBank | 1 | 1 | 1 |
| ClinicalTrials.gov | 10 | 1 | 0 (false positive) |
| ICTRP | 10 | 0 | 0 |
| PubMed | 10 | 25 | 0 (all false positives) |
| **Total** | **33** | **27** | **1 (DrugBank only)** |

---

> **Research Use Only**: This report is generated for research purposes only and does not constitute medical advice. Drug repurposing predictions require clinical validation before therapeutic application. This is not a TGA-approved assessment.

---

*Generated by AuTxGNN — Australian Drug Repurposing Predictions*
*Report ID: TW-DB05812-multi | Version: v4 | Date: 3 April 2026*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

