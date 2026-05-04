---
layout: default
title: Ibrutinib
parent: 僅模型預測 (L5)
nav_order: 236
evidence_level: L5
indication_count: 10
---

# Ibrutinib
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

# Ibrutinib: From B-Cell Malignancies to Polyclonal Hypergammaglobulinaemia

## One-Sentence Summary

Ibrutinib is a first-in-class Bruton's Tyrosine Kinase (BTK) inhibitor with established international approvals for multiple B-cell malignancies — including chronic lymphocytic leukaemia (CLL), mantle cell lymphoma (MCL), and Waldenström's macroglobulinaemia (WM) — though it is **not currently registered with the Australian TGA**.
The TxGNN model predicts ibrutinib may be effective for **Polyclonal Hypergammaglobulinaemia** (prediction score 91.75%), however this prediction is currently supported by **no clinical trials and no published literature**, placing it at the earliest evidence stage (L5 — model prediction only).
Of note, TxGNN also predicts strong potential for **Waldenström's Macroglobulinaemia** (rank 2, L1) and **Marginal Zone Lymphoma** (rank 8, L1), both with completed Phase 3 RCT evidence — these represent significantly more actionable repurposing opportunities for Australian clinical consideration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not currently TGA-registered; ibrutinib is internationally established for B-cell malignancies (CLL/SLL, MCL, WM, MZL) — original indication data unavailable in Australian regulatory records |
| Predicted New Indication | Polyclonal Hypergammaglobulinaemia |
| TxGNN Prediction Score | 91.75% |
| Evidence Level | L5 (model prediction only — zero clinical trials, zero publications) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Polyclonal hypergammaglobulinaemia is characterised by the overproduction of immunoglobulins by multiple distinct B-cell clones simultaneously. This is fundamentally different from monoclonal gammopathies such as Waldenström's macroglobulinaemia, where a single aberrant clone predominates. The condition typically arises as a secondary, reactive phenomenon in the context of chronic infections (e.g., HIV, viral hepatitis), systemic autoimmune diseases (e.g., systemic lupus erythematosus, rheumatoid arthritis, Sjögren's syndrome), or chronic inflammatory states.

The mechanistic basis for ibrutinib in this setting is indirect. Ibrutinib irreversibly binds to the Cys481 residue of BTK, blocking B-cell receptor (BCR) downstream signalling cascades — specifically NF-κB and PI3K/AKT pathway activation — thereby suppressing B-cell proliferation and immunoglobulin secretion. In theory, this broad suppression of BCR-dependent B-cell activity could attenuate the polyclonal immunoglobulin hypersecretion driving the elevated globulin levels. However, because polyclonal hypergammaglobulinaemia is typically a reactive rather than a neoplastic condition, its underlying biology is meaningfully different from the malignant clonal B-cell expansion that ibrutinib has proven efficacy against.

Currently, no clinical trials or human studies directly investigate ibrutinib for polyclonal hypergammaglobulinaemia. The TxGNN score of 91.75% reflects modelled biological pathway similarity — likely attributable to shared BTK and BCR biology — but cannot be interpreted as clinical efficacy evidence. This prediction requires dedicated preclinical validation before any clinical translation is considered.

> **Note on MOA data gap**: Detailed mechanism of action data is not available in the current Evidence Pack (flagged as High-severity data gap DG002). Based on known scientific literature, ibrutinib is a covalent, irreversible inhibitor of Bruton's Tyrosine Kinase (BTK), with primary activity against malignant B-cell clones dependent on BCR signalling for survival and proliferation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for polyclonal hypergammaglobulinaemia.

---

## Literature Evidence

Currently no related literature available for polyclonal hypergammaglobulinaemia.

---

## Australia Market Information

Ibrutinib currently has **no ARTG entries** in the Australian Register of Therapeutic Goods and is classified as **not marketed** in Australia. Australian clinicians wishing to access this medicine would need to apply through the TGA's **Special Access Scheme (SAS Category B or C)** or **Authorised Prescriber** pathway, supported by evidence from international regulatory approvals.

For reference, ibrutinib has received the following international regulatory approvals:

| Jurisdiction | Approved Indications (selected) |
|---|---|
| FDA (USA) | CLL/SLL, MCL, WM, relapsed/refractory MZL, cGVHD |
| EMA (Europe) | CLL/SLL, MCL, WM, relapsed/refractory MZL |
| PMDA (Japan) | CLL/SLL, MCL, WM (WM with rituximab) |

*Verification of current TGA status is recommended, as this data reflects the Australian regulatory database as of the report cutoff date (2026-04-20). A data gap in Australian-specific prescribing information (labelled DG001, Blocking severity) has been identified.*

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | **Targeted therapy** — BTK inhibitor (small molecule covalent kinase inhibitor); NOT classified as conventional cytotoxic chemotherapy |
| Myelosuppression Risk | **Low to moderate**; neutropenia, thrombocytopenia, and anaemia have been reported in clinical trials, generally less severe than with cytotoxic regimens; severity may increase in combination with anti-CD20 agents |
| Emetogenicity Classification | **Low** — oral targeted agent with low emetogenic potential per MASCC/ESMO guidelines |
| Monitoring Items | Full blood count with differential (monthly initially, then periodically), liver function tests, renal function, ECG and cardiac assessment (atrial fibrillation risk), blood pressure monitoring |
| Handling Protection | Standard oral antineoplastic handling precautions apply; ibrutinib capsules/tablets should not be crushed or opened; healthcare workers should avoid contact with broken tablets — refer to institutional cytotoxic handling protocols |

---

## Safety Considerations

As ibrutinib has no current ARTG listing in Australia and the TGA-specific Product Information is unavailable (data gap DG001, Blocking severity), **please refer to the most current international Product Information** — specifically the FDA-approved Prescribing Information for Imbruvica® or the EMA-approved Summary of Product Characteristics — for comprehensive safety data prior to any clinical use.

Key safety signals established through international clinical trials and post-marketing surveillance include:

- **Haemorrhage**: Ibrutinib inhibits collagen-induced platelet aggregation via off-target TEC kinase inhibition. Major haemorrhagic events including intracranial haemorrhage, subdural haematoma, and gastrointestinal bleeding have been reported. Concomitant use with anticoagulants or antiplatelet agents significantly increases bleeding risk and requires careful clinical judgement.
- **Atrial Fibrillation and Flutter**: Clinically significant atrial fibrillation occurs in approximately 6–16% of patients depending on the indication and duration of therapy; highest risk in patients with pre-existing cardiac disease, hypertension, or acute infections. Cardiac monitoring is recommended.
- **Hypertension**: New-onset or worsening hypertension has been reported across ibrutinib trials; regular blood pressure monitoring and antihypertensive management may be required.
- **Serious and Opportunistic Infections**: Fatal and serious infections — including Pneumocystis jirovecii pneumonia, cryptococcal meningitis, aspergillosis, and bacterial sepsis — have occurred. Consider antimicrobial prophylaxis per institutional guidelines.
- **Second Primary Malignancies**: Including non-melanoma skin cancers and other solid tumours; skin surveillance recommended.
- **Embryo-Foetal Toxicity**: Ibrutinib may cause foetal harm; effective contraception required during treatment and for a defined washout period.

---

## Notable TxGNN Predictions with Established Evidence

While the primary TxGNN rank 1 prediction (polyclonal hypergammaglobulinaemia) is currently unsupported by clinical data, two additional predictions in this evidence pack carry substantive clinical trial evidence relevant to Australian practice:

### Waldenström's Macroglobulinaemia (Rank 2 — L1 Evidence)

TxGNN score 91.16%. Ibrutinib is the most extensively studied oral targeted therapy for WM. The iNNOVATE Phase 3 RCT ([NCT02165397](https://clinicaltrials.gov/study/NCT02165397), n=181, completed) demonstrated superior PFS for ibrutinib plus rituximab versus rituximab alone, establishing L1 evidence and supporting FDA/EMA registration. A head-to-head Phase 3 trial versus zanubrutinib (ASPEN; [NCT03053440](https://clinicaltrials.gov/study/NCT03053440), n=201, completed) further characterises ibrutinib's role in this disease. **Recommendation: Proceed with Guardrails.**

### Marginal Zone Lymphoma (Rank 8 — L1 Evidence)

TxGNN score 87.96%. Ibrutinib received FDA approval in 2017 for relapsed/refractory MZL following at least one anti-CD20-based therapy. The SELENE Phase 3 trial ([NCT01974440](https://clinicaltrials.gov/study/NCT01974440), n=403, completed) evaluated ibrutinib plus chemoimmunotherapy in R/R FL and MZL. Multiple Phase 2 studies including the pivotal PCYC-1121 trial ([NCT01980628](https://clinicaltrials.gov/study/NCT01980628), n=63, completed) demonstrate an overall response rate of approximately 48–58% in R/R MZL. **Recommendation: Proceed with Guardrails.**

---

## Conclusion and Next Steps

**Decision: Hold** *(for polyclonal hypergammaglobulinaemia)*

**Rationale:**
The TxGNN model identifies polyclonal hypergammaglobulinaemia as a biologically plausible target on the basis of shared B-cell receptor signalling biology, but this remains a theoretical extrapolation with no supporting human clinical data. The reactive, non-clonal nature of polyclonal hypergammaglobulinaemia means the disease mechanism does not align clearly with ibrutinib's established anti-neoplastic mechanism of action in malignant B-cell conditions.

**To proceed, the following is needed:**
- Preclinical proof-of-concept studies in validated models of polyclonal B-cell hyperactivation (e.g., autoimmune disease models, chronic infection models with elevated polyclonal IgG/IgA/IgM)
- Mechanistic studies clarifying whether BTK inhibition reduces polyclonal immunoglobulin production in reactive conditions, independent of cytotoxic B-cell depletion
- Resolution of the MOA data gap (DG002) through DrugBank API query and review of ibrutinib pharmacology literature
- Phase 1/2 clinical safety and signal-finding data in a defined polyclonal hypergammaglobulinaemia patient population
- TGA Special Access Scheme application to enable clinical use in Australia, given the current absence of any ARTG registration (0 entries)
- Resolution of Australian-specific prescribing information gaps (DG001): TGA warnings, contraindications, and drug-drug interaction data must be obtained from international PI documents and confirmed against TGA requirements

> **Clinical prioritisation note for Australian healthcare professionals**: If ibrutinib access via TGA Special Access Scheme is being considered, the Waldenström's Macroglobulinaemia and Marginal Zone Lymphoma indications carry significantly stronger evidence (both L1, multiple Phase 3 RCTs) and represent more clinically defensible repurposing targets in the near term.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

