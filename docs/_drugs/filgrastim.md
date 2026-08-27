---
layout: default
title: Filgrastim
parent: 僅模型預測 (L5)
nav_order: 276
evidence_level: L5
indication_count: 10
---

# Filgrastim
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

# Filgrastim: From Neutropenia to Primary Release Disorder of Platelets

## One-Sentence Summary

Filgrastim is a recombinant human G-CSF (granulocyte colony-stimulating factor), originally used to treat neutropenia and to mobilise peripheral blood stem cells before transplantation. The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but the supporting evidence is weak: of **14 clinical trials** and **1 publication** retrieved, almost none directly test filgrastim against this disease — most are unrelated haematopoietic stem cell transplant (HSCT) trials that happen to use G-CSF for donor mobilisation.

> **Note:** This evidence pack does not contain original-indication or MOA data for filgrastim (data gaps DG001/DG002). The original indication and mechanism below are stated from established pharmacological knowledge, not from this evidence pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Neutropenia (chemotherapy-induced, congenital/severe chronic) and peripheral blood stem cell mobilisation — *not present in evidence pack, stated from general pharmacological knowledge* |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.99% (rank 87 of predictions) |
| Evidence Level | L4 — but see caveat below |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

**Evidence level caveat:** Although trial and publication counts nominally place this at L4, the evidence pack's own relevance grading marks the assessed trials as "C" (low/tangential relevance) or still pending, and the sole publication addresses donor-mobilisation physiology, not treatment of the predicted disease. The effective disease-specific evidence is closer to **L5 (model prediction only)**.

---

## Why is This Prediction Reasonable?

Filgrastim is a G-CSF receptor agonist. Pharmacologically, it stimulates proliferation and differentiation of granulocyte (neutrophil) precursors in the bone marrow. Its established clinical uses are neutrophil recovery after chemotherapy and mobilisation of donor peripheral blood stem cells before allogeneic/autologous transplantation.

Primary release disorder of platelets is a platelet secretion defect (impaired δ-granule/dense-granule release), governed by an entirely different pathway from G-CSF/granulocyte signalling. There is no known mechanistic overlap between G-CSF receptor activation and platelet granule release machinery.

The evidence pack's own repurposing rationale states this directly: the very high TxGNN score most likely reflects **topological proximity of "blood/haematopoietic system" nodes in the knowledge graph**, rather than a genuine pharmacological relationship. The clinical trials returned are almost all allogeneic HSCT studies where filgrastim is used incidentally as a donor stem-cell mobiliser — not as a treatment being tested against this disease. This should be read as a low-confidence, knowledge-graph-driven signal rather than a mechanistically grounded hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00245037](https://clinicaltrials.gov/study/NCT00245037) | Phase 1/2 | Completed | 147 | Non-myeloablative allogeneic HSCT for haematologic malignancies; filgrastim used for donor mobilisation only — **graded low relevance (C)**, not a therapeutic test for this disease |
| [NCT05170828](https://clinicaltrials.gov/study/NCT05170828) | Phase 1 | Withdrawn | 0 | Cryopreserved unrelated-donor bone marrow transplant study; withdrawn, relevance not yet assessed |
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Phase 2 | Completed | 60 | Allogeneic/syngeneic stem cell transplant for high-risk paediatric sarcomas — **graded low relevance (C)**, HSCT context only |
| [NCT01335932](https://clinicaltrials.gov/study/NCT01335932) | Phase 2 | Completed | 160 | Ganciclovir/valganciclovir for CMV reactivation prevention in lung injury; relevance not yet assessed |
| [NCT01503918](https://clinicaltrials.gov/study/NCT01503918) | Phase 2 | Completed | 124 | Antiviral prophylaxis for CMV reactivation in critical care; relevance not yet assessed |
| [NCT00076752](https://clinicaltrials.gov/study/NCT00076752) | Phase 2 | Completed | 9 | Autologous HSCT for severe systemic lupus erythematosus; relevance not yet assessed |
| [NCT04540120](https://clinicaltrials.gov/study/NCT04540120) | Phase 2 | Terminated | 49 | Dapansutrile for moderate COVID-19 and cytokine release syndrome; relevance not yet assessed |
| [NCT00281879](https://clinicaltrials.gov/study/NCT00281879) | Phase 2 | Terminated | 200 | Unrelated donor HSCT for haematologic malignancies; relevance not yet assessed |
| [NCT00923364](https://clinicaltrials.gov/study/NCT00923364) | Phase 2 | Completed | 19 | Reduced-intensity HSCT for GATA2 mutations; relevance not yet assessed |
| [NCT04047628](https://clinicaltrials.gov/study/NCT04047628) | Phase 3 | Recruiting | 156 | Autologous HSCT vs. best available therapy for treatment-resistant relapsing multiple sclerosis — **graded low relevance (C)**, transplant-strategy trial, not a direct filgrastim efficacy test |

Note: 4 additional trials were returned but are omitted here for space; none were graded as directly relevant to this indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29770133](https://pubmed.ncbi.nlm.nih.gov/29770133/) | 2018 | Cohort | Frontiers in Immunology | G-CSF mobilisation in healthy donors preferentially mobilises lymphocyte subsets — a donor-physiology study, not a treatment-efficacy study for this disease |

---

## Australia Market Information

Filgrastim currently has **no ARTG entries** in the data supplied and is recorded as **not marketed** in this evidence pack. (Note: filgrastim biosimilars are in fact TGA-registered in Australia under other brand names; this evidence pack's regulatory data appears incomplete and should be verified directly against the ARTG before any clinical use.)

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No key warnings, contraindications, or drug interaction data were available in this evidence pack (DG001, Blocking severity — this gap blocks safety pre-screening).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- No trial or publication directly tests filgrastim's efficacy against primary release disorder of platelets; the retrieved trials are almost entirely HSCT studies where filgrastim serves as a donor-mobilisation adjunct, not a treatment under investigation.
- The predicted mechanism (G-CSF/granulocyte stimulation) has no established link to platelet granule-release physiology; the high TxGNN score is most plausibly a knowledge-graph topological artefact rather than a pharmacologically grounded signal.
- A Blocking-severity data gap (missing TFDA/TGA PI warnings and contraindications, DG001) prevents even an initial safety screen (S1).

**To proceed, the following is needed:**
- TGA-approved Product Information (PI) — warnings, contraindications, and DDI data (resolves DG001)
- Confirmed mechanism-of-action data from DrugBank (resolves DG002)
- A disease-specific pharmacological plausibility review, ideally by a haematology specialist, given the mechanistic mismatch noted above
- Verification of actual current ARTG/TGA registration status for filgrastim products in Australia, as the "not marketed" status in this pack looks inconsistent with known market data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

