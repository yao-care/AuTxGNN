---
layout: default
title: Cyclosporine
parent: 僅模型預測 (L5)
nav_order: 133
evidence_level: L5
indication_count: 10
---

# Cyclosporine
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

# Cyclosporine: From Transplant Rejection Prevention to Chronic Granulomatous Disease

## One-Sentence Summary

Cyclosporine is a calcineurin inhibitor (CNI) with a long-established global track record in preventing organ transplant rejection and managing autoimmune conditions, though it does not appear as a registered product in the current Australian ARTG dataset.
The TxGNN model predicts it may be effective for **Chronic Granulomatous Disease, Autosomal Recessive (CGD)**, with **1 clinical trial** and **1 publication** currently supporting this direction.
The overall evidence base for this specific repurposing direction is limited, suggesting further investigation is needed before clinical application.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Organ transplant rejection prevention (globally established; no current ARTG registration found) |
| Predicted New Indication | Granulomatous Disease, Chronic, Autosomal Recessive (CGD) |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L4 |
| Australia Market Status | Not Marketed (no ARTG entries found) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

> ⚠️ **Data Note:** Cyclosporine (e.g., Sandimmun® Neoral®) is a widely used medicine globally and may be available in Australia via the Special Access Scheme (SAS) or as an unregistered product. The absence of ARTG entries likely reflects a data collection gap rather than true non-availability. Clinicians should verify current TGA registration status directly.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Cyclosporine is a calcineurin inhibitor that works by binding to intracellular cyclophilin. The resulting complex inhibits calcineurin — a phosphatase essential for activating NFAT (Nuclear Factor of Activated T Cells) — thereby blocking IL-2 transcription and downstream T-cell proliferation. This produces targeted, potent immunosuppression without the broad cytotoxicity of conventional chemotherapy.

Chronic Granulomatous Disease (CGD), autosomal recessive form, is a rare primary immunodeficiency caused by loss-of-function mutations in NADPH oxidase subunit genes (most commonly *NCF1* encoding p47phox or *NCF2* encoding p67phox). Affected patients suffer recurrent, life-threatening bacterial and fungal infections and form abnormal, dysregulated granulomas. The definitive curative treatment is allogeneic haematopoietic stem cell transplantation (HSCT).

The mechanistic link between Cyclosporine and CGD is **indirect**: Cyclosporine is used as a standard component of graft-versus-host disease (GvHD) prophylaxis within the HSCT conditioning protocol for CGD — it does not directly address the underlying NADPH oxidase defect. The TxGNN high prediction score likely reflects Cyclosporine's well-established integral role in the HSCT management pathway for CGD, captured as a strong association in the knowledge graph, rather than a novel direct treatment mechanism. This distinction is critical for interpreting the clinical relevance of this prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT01917708](https://clinicaltrials.gov/study/NCT01917708) | Phase 1 | Completed | 10 | Single-arm study assessing tolerability of abatacept combined with **cyclosporine and mycophenolate mofetil** as GvHD prophylaxis in children undergoing unrelated donor HSCT for serious non-malignant diseases (including CGD); participants followed for 2 years. Cyclosporine is a background prophylaxis agent, not the experimental intervention. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [22078471](https://pubmed.ncbi.nlm.nih.gov/22078471/) | 2012 | Observational | J Allergy Clin Immunol | Matched related donor (MRD) HSCT demonstrates excellent survival for CGD; safety and efficacy of unrelated donor HSCT also assessed. Cyclosporine used as part of standard conditioning/GvHD prophylaxis, not evaluated as a standalone CGD treatment. |

---

## Australia Market Information

No ARTG product entries were found for Cyclosporine in the current dataset.

> Cyclosporine is a well-established medicine internationally, with approved indications across multiple jurisdictions (FDA, EMA) for prevention of solid organ and bone marrow transplant rejection, rheumatoid arthritis, severe psoriasis, and atopic dermatitis. Australian clinicians requiring Cyclosporine should contact the TGA directly or access it via the **Special Access Scheme Category B (SAS-B)** pathway. Product information for Sandimmun® Neoral® (Novartis) is the primary reference for prescribers.

---

## Safety Considerations

Cyclosporine-specific safety data (product warnings, contraindications, drug interactions) was not retrievable from the Australian TGA dataset for this report. Please refer to the following resources:

- **TGA Special Access Scheme (SAS-B) product information** for Sandimmun® Neoral®
- **Novartis international Product Information (PI)** for full prescribing information
- **NPS MedicineWise / AMH (Australian Medicines Handbook)** for Australian clinical guidance

Key safety areas to review before use in any new indication:
- **Nephrotoxicity** (dose-dependent and cumulative — requires regular renal function monitoring)
- **Hypertension** (very common; antihypertensive therapy frequently required)
- **Neurotoxicity** (tremor, paraesthesia, seizures at higher levels)
- **Immunosuppression-related infections** (bacterial, viral, fungal, opportunistic)
- **Drug interactions** (CYP3A4 substrate and P-glycoprotein substrate — extensive interaction profile with antibiotics, antifungals, anticonvulsants, statins)
- **Malignancy risk** (increased risk of lymphoma and skin cancers with long-term immunosuppression)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The available evidence consists of a single Phase 1 trial (n=10) in which Cyclosporine was used as a background GvHD prophylaxis agent (not as the primary therapeutic target), and one observational publication on HSCT outcomes in CGD. Cyclosporine does not address the underlying NADPH oxidase defect in CGD, and its predicted role appears to reflect a knowledge graph association with HSCT — the curative treatment pathway — rather than a direct mechanistic basis for repurposing. This is insufficient to support a prospective repurposing programme for CGD.

**To proceed, the following is needed:**

- **Clarification of therapeutic intent:** Determine whether the clinical question is (a) optimising Cyclosporine within HSCT GvHD prophylaxis protocols for CGD, or (b) Cyclosporine as a direct disease-modifying therapy for CGD — these are fundamentally different questions.
- **Mechanism of action data:** Obtain full MOA from DrugBank (DB00091) to assess any direct biological plausibility for CGD beyond HSCT adjunct use.
- **TGA registration verification:** Confirm current ARTG status and availability of Cyclosporine in Australia (SAS pathway if unregistered).
- **Paediatric safety profile:** CGD typically presents in childhood; a dedicated safety review for paediatric dosing and monitoring is required.
- **Phase 2/3 evidence:** No Phase 2 or Phase 3 RCTs specifically examining Cyclosporine as direct therapy for CGD were identified. This gap should be addressed before any clinical protocol development.
- **Review of alternative predictions:** The TxGNN model's Rank 9 prediction — **Bronchitis/Bronchiolitis Obliterans Syndrome (BOS)** — is supported by multiple completed Phase 3 trials (NCT00755781, NCT03657342, NCT03656926) and 20+ publications, and represents a substantially higher-evidence repurposing opportunity that warrants priority evaluation ahead of CGD.

---

*This report is generated from the TxGNN model output and evidence collected as of 4 April 2026. Results are for research purposes only and do not constitute medical advice. All repurposing candidates require clinical validation before therapeutic application. Prescribers should refer to current TGA-approved Product Information and consult relevant clinical specialists.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

