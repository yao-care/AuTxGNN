---
layout: default
title: Cabergoline
parent: 僅模型預測 (L5)
nav_order: 113
evidence_level: L5
indication_count: 10
---

# Cabergoline
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

---

# Cabergoline: From Hyperprolactinemia/Prolactinoma to Pituitary Adenocarcinoma

## One-Sentence Summary

Cabergoline is a highly selective dopamine D2 receptor agonist established internationally as first-line medical treatment for hyperprolactinemia and prolactinoma; it is not currently listed on the Australian Register of Therapeutic Goods (ARTG), which may reflect a data collection gap rather than actual unavailability.
The TxGNN model predicts it may have activity in **Pituitary Adenocarcinoma** — an extremely rare malignant pituitary tumour defined by the presence of distant metastases — with **0 clinical trials** and **3 publications** retrieved for this specific indication, of which only 1 is directly relevant.

> **Clinical context:** Pituitary adenocarcinoma (malignant, metastasising) is pathologically distinct from the far more common benign pituitary adenoma. The TxGNN model's broader rank-3 prediction for "pituitary cancer/adenoma" carries **L1 evidence** (2 completed Phase 3 RCTs), suggesting the model is correctly identifying cabergoline's strong pituitary tumour biology connection — with the adenocarcinoma-specific signal being an extrapolation to the rarer malignant subtype.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hyperprolactinemia / Prolactinoma (not currently listed on ARTG — possible data gap; verify with TGA) |
| Predicted New Indication | Pituitary Adenocarcinoma |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L4 — Mechanistic basis and indirect case reports only; no dedicated clinical studies |
| Australia Market Status | Not listed on ARTG |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold — Research Question stage |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on well-established clinical knowledge, cabergoline is a selective ergot-derived **dopamine D2 receptor (D2R) agonist**. Its primary mechanism involves direct activation of D2 receptors on pituitary lactotroph cells, suppressing prolactin secretion and causing tumour shrinkage in prolactinomas. Cabergoline also shows efficacy across other pituitary adenoma subtypes — corticotroph adenomas (Cushing's disease), somatotroph adenomas (acromegaly), and non-functioning pituitary adenomas (NFPAs) — where D2R expression has been demonstrated. Recent research has additionally identified anti-proliferative and pro-apoptotic mechanisms via autophagy induction and the HTR2B/Gαq/PLC/PKCγ/STAT3 axis that extend beyond dopamine receptor activation.

Pituitary adenocarcinoma is the most aggressive end of the pituitary neoplasm spectrum, defined strictly by the presence of craniospinal or systemic distant metastases — a criterion that distinguishes it from the far more common benign adenoma. Fewer than 200 cases have been reported in the world literature. The mechanistic rationale is that malignant transformation of a pituitary adenoma may retain D2R expression, and cabergoline's anti-proliferative effects demonstrated in benign adenoma cell lines and clinical trials could theoretically extend to the malignant counterpart. However, D2R expression status in pituitary adenocarcinoma metastatic deposits remains entirely uncharacterised.

The TxGNN model's rank-1 prediction for adenocarcinoma most likely reflects extrapolation from the strong knowledge graph connections underpinning its rank-3 prediction for "pituitary cancer" broadly — where cabergoline has completed Phase 3 RCTs and demonstrated clear efficacy. The biological plausibility is mechanistically sound in principle, but the clinical evidence gap specific to the malignant adenocarcinoma subtype is substantial and represents a genuine research question rather than a near-term clinical repurposing opportunity.

---

## Clinical Trial Evidence

Currently no clinical trials specifically investigating cabergoline for pituitary adenocarcinoma are registered on ClinicalTrials.gov or ICTRP.

> **Context:** Pituitary adenocarcinoma's extreme rarity (global prevalence < 200 documented cases) makes a dedicated randomised controlled trial impractical. Any clinical evidence would need to emerge from compassionate use case series, international pituitary tumour registries, or retrospective cohort analyses. For reference, substantial trial evidence exists for cabergoline in **benign pituitary tumours** (see rank-3 prediction: 19 registered trials including 2 completed Phase 3 RCTs).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [20497940](https://pubmed.ncbi.nlm.nih.gov/20497940/) | 2010 | Case Report | *Endocrine Practice* | Long-term management with octreotide or cabergoline in ectopic ACTH hypersecretion post-bilateral adrenalectomy. Demonstrates cabergoline's capacity for sustained corticotropin suppression in a potentially malignant/ectopic secretory context — the most directly relevant publication retrieved |
| [41760078](https://pubmed.ncbi.nlm.nih.gov/41760078/) | 2026 | Case Report | *Medicine* | MEN1 syndrome with a variant of uncertain pathogenicity. Describes co-existing endocrine tumours in a multiple endocrine neoplasia context; peripheral relevance only — not specific to pituitary adenocarcinoma treatment |
| [33569966](https://pubmed.ncbi.nlm.nih.gov/33569966/) | 2021 | Case Report | *Rev Esp Enferm Dig* | Pancreatic adenocarcinoma incidentally discovered in a patient receiving cabergoline for pituitary adenoma. Co-incidental tumour occurrence; cabergoline not implicated in treatment of the adenocarcinoma — not relevant |

> ⚠️ **Evidence quality alert:** Of 3 retrieved publications, only 1 (PMID 20497940) provides any mechanistic link to the target indication, and even that addresses ectopic (non-pituitary) ACTH secretion. The remaining 2 publications are misleading citations that do not support cabergoline for pituitary adenocarcinoma.

---

## Australia Market Information

No ARTG entries were found for cabergoline in the current TGA data extract (0 registered products).

This result likely represents a **data collection gap** rather than true unavailability. Cabergoline (Dostinex®, Pfizer) holds regulatory approval for hyperprolactinemia and prolactinoma in the USA (FDA), European Union (EMA), and United Kingdom (MHRA), and has been used clinically in Australia. Clinicians should verify current TGA registration status directly at [www.tga.gov.au](https://www.tga.gov.au) and consult the TGA-approved Product Information (PI) before prescribing.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for complete safety information, as formal safety data retrieval for this evidence pack returned no results.

**Key safety signals identified from the broader evidence review (ranked indications 1–10):**

- **Impulse Control Disorders (ICDs):** Multiple prospective studies and systematic reviews (2022–2026) consistently identify ICDs — including pathological gambling, compulsive shopping, hypersexuality, and binge eating — as a recognised and potentially underappreciated adverse effect of dopamine agonist therapy. Prevalence estimates in screened pituitary adenoma populations reach up to 59.8%. Routine structured ICD screening is recommended for all patients on cabergoline, with particular vigilance in those with pre-existing risk factors for impulsive behaviour.

- **Acute angle-closure glaucoma:** A case report (PMID 21347189) documents bilateral acute angle-closure glaucoma following oral cabergoline administration. Patients presenting with acute visual symptoms or eye pain should be assessed promptly.

- **Cardiac valvulopathy:** Long-standing use at high cumulative doses has been associated with concern for cardiac valve abnormalities, though evidence specifically at doses used for pituitary indications (lower than Parkinson's disease doses) has been largely reassuring. Baseline and periodic echocardiography may be warranted for long-term use.

---

## Conclusion and Next Steps

**Decision: Hold — Research Question**

**Rationale:**
The evidence base for cabergoline specifically in pituitary adenocarcinoma is insufficient to support clinical advancement at this time. Only 1 of 3 retrieved publications is tangentially relevant, no clinical trials have been conducted or registered, and the pathobiological distinction between benign pituitary adenoma (where cabergoline has strong L1 evidence) and malignant adenocarcinoma (requiring distant metastases) creates significant mechanistic uncertainty for direct extrapolation.

**To proceed, the following is needed:**

- **D2R expression characterisation:** Immunohistochemical or mRNA-based confirmation of dopamine D2 receptor expression in pituitary adenocarcinoma tissue and metastatic deposits (prerequisite for any mechanistic claim)
- **Registry-based case series:** Systematic review of cabergoline use in histologically confirmed pituitary adenocarcinoma through international pituitary tumour registries (e.g., ERCUSYN, ENSAT)
- **Basic science studies:** Anti-proliferative and pro-apoptotic effects of cabergoline assessed in pituitary adenocarcinoma-derived cell models or patient-derived xenografts
- **TGA Product Information retrieval:** Resolve DG001 data gap — download and parse the PI to complete safety screening (Blocking severity)
- **DrugBank MOA query:** Resolve DG002 data gap — formal MOA documentation via DrugBank API to support mechanistic analysis (High severity)
- **ARTG verification:** Confirm actual TGA registration status of cabergoline (Dostinex®) to correct the apparent data gap in australia_regulatory

> **Broader repurposing signal:** While pituitary adenocarcinoma (rank 1) is a Hold at this stage, the closely related "pituitary cancer/adenoma" prediction (rank 3, TxGNN score 99.04%) carries **L1 evidence** with a **Proceed with Guardrails** recommendation — supported by 19 registered clinical trials and multiple Phase 3 RCTs. This represents the actionable clinical repurposing direction for cabergoline in pituitary tumour oncology.

---

*Report generated: 21 June 2026 | Evidence cut-off: 21 June 2026 | Candidate ID: TW-DB00248-multi v4*
*⚕️ This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require formal clinical validation before therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

