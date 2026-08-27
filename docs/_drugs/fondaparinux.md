---
layout: default
title: Fondaparinux
parent: 僅模型預測 (L5)
nav_order: 293
evidence_level: L5
indication_count: 10
---

# Fondaparinux
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

# Fondaparinux: From Anticoagulation to Heparin-Induced Thrombocytopenia (Primary Platelet Release Disorder)

## One-Sentence Summary

Fondaparinux is a synthetic Factor Xa inhibitor anticoagulant (brand name Arixtra), typically used for prevention and treatment of venous thromboembolic events. The TxGNN model predicts it may be effective for **primary release disorder of platelets** — an ontology term that, based on the supporting evidence, corresponds clinically to **heparin-induced thrombocytopenia (HIT)** — with a **93.06%** TxGNN confidence score, currently supported by **2 clinical trials** and **2 literature references**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (drug-level indication and MOA fields are marked as data gaps; Fondaparinux's general clinical use is as an anticoagulant) |
| Predicted New Indication | Primary release disorder of platelets (clinically interpreted as Heparin-Induced Thrombocytopenia, HIT) |
| TxGNN Prediction Score | 93.06% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed (0 local entries) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Fondaparinux is not available in this evidence pack (flagged as data gap DG002, pending a DrugBank API query). Based on the mechanistic rationale documented for this specific prediction, Fondaparinux is a synthetic pentasaccharide that selectively inhibits Factor Xa via antithrombin III. Critically, unlike unfractionated or low-molecular-weight heparin, it does not form immunogenic complexes with platelet factor 4 (PF4).

This distinguishing feature is precisely why Fondaparinux is relevant to HIT: because HIT is driven by antibodies against PF4/heparin complexes that trigger pathological platelet activation and consumption (a form of platelet release disorder), a non-cross-reactive anticoagulant offers a mechanistically sound alternative once heparin must be withdrawn. This off-label use is already recognised in international guidance (e.g., ASH 2018), which lends external plausibility to the TxGNN prediction beyond the model score alone.

One caveat: the TxGNN disease label "primary release disorder of platelets" is a broad ontology term, and the evidence pack notes it needs confirmation that it precisely maps to HIT rather than other platelet release defects (e.g., δ-storage pool disease), where anticoagulation would not be an appropriate treatment. Of the 10 candidates TxGNN generated for this drug, this is the only one with clinical-trial and literature support (L2); the remaining nine are L5 (model-prediction only), and several carry a theoretical bleeding-risk concern given Fondaparinux's anticoagulant mechanism.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00911300](https://clinicaltrials.gov/study/NCT00911300) | Phase 2 | Completed | 349 | International multicentre, randomised, open-label pilot comparing Fondaparinux vs. heparin/vitamin-K antagonists for anticoagulation around electrical cardioversion; assesses thromboembolic and bleeding event prevention. |
| [NCT01178333](https://clinicaltrials.gov/study/NCT01178333) | N/A (retrospective) | Completed | 668 | Retrospective analysis of patients with a positive heparin PF-4 antibody test (HIT-RADIO), examining incidence and outcomes (platelet counts, thrombosis, amputation, death) — supportive epidemiological context rather than an interventional efficacy trial. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28646118](https://pubmed.ncbi.nlm.nih.gov/28646118/) | 2017 | Review | Blood | Review of direct oral anticoagulants (DOACs, e.g. rivaroxaban) for treatment of serologically confirmed HIT, including the Hamilton clinical experience and literature synthesis — relevant background on non-heparin anticoagulant strategies for HIT, though focused on DOACs rather than Fondaparinux specifically. |
| [30018843](https://pubmed.ncbi.nlm.nih.gov/30018843/) | 2017 | Case report | Journal of the Advanced Practitioner in Oncology | Abstract concerns palliative chemotherapy decision-making in a patient with metastatic adenocarcinoma of unknown origin; content does not appear related to Fondaparinux or platelet release disorders — likely a search/mapping artefact and should be treated with low confidence. |

---

## Australia Market Information

Fondaparinux currently has **no ARTG entries** and is **not marketed** in Australia, so no local product listing or approved-indication text is available in this evidence pack.

---

## Safety Considerations

No key warnings, contraindications, or drug-interaction data were returned for this evidence pack (TFDA/product-label warnings and contraindications are flagged as a **Blocking** data gap — DG001 — which prevents the initial safety review stage; the DDI query also returned no results). Because Fondaparinux is not currently registered locally, there is no TGA/TFDA-approved Product Information to reference directly — safety assessment should draw on the overseas-approved label (e.g., Arixtra PI from a reference regulator) until local documentation is obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic case and supporting Phase 2/retrospective evidence (L2) for using Fondaparinux in HIT are reasonably strong and consistent with existing international off-label guidance. However, a Blocking data gap on safety warnings/contraindications means the candidate cannot yet pass initial safety screening (S1), and the drug is not currently marketed or registered in Australia.

**To proceed, the following is needed:**
- TFDA/overseas product-label warnings and contraindications (DG001 — blocking; source: TFDA official site, PI PDF parsing)
- Confirmed mechanism of action from DrugBank (DG002; source: DrugBank API)
- Confirmation that "primary release disorder of platelets" precisely corresponds to HIT rather than an unrelated platelet release defect
- Local registration pathway assessment, since Fondaparinux currently has zero ARTG entries in Australia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

