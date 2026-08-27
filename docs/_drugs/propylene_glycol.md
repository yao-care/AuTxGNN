---
layout: default
title: Propylene Glycol
parent: 僅模型預測 (L5)
nav_order: 566
evidence_level: L5
indication_count: 10
---

# Propylene Glycol
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

# Propylene Glycol: From Pharmaceutical Excipient to Predicted Bronchitis Indication

## One-Sentence Summary

Propylene glycol (DrugBank DB01839) has no registered therapeutic indication of its own — it is used almost exclusively as a pharmaceutical solvent/excipient in oral, inhaled and topical formulations. The TxGNN model predicts a possible link to **Bronchitis**, but the retrieved evidence — 4 clinical trials and 3 publications — does not actually support this: the trials tested a different drug (cyclosporine), and the literature describes potential lung *harm* from propylene glycol-based e-cigarette vapour, not a treatment benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | None on record — propylene glycol is used as a pharmaceutical excipient/solvent, not as an active therapeutic agent |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Market Status (source: Taiwan TFDA) | Not Marketed |
| Number of Registered Product Entries | 0 |
| Recommended Decision | Hold |

**Note on data source:** the regulatory fields in this Evidence Pack (`taiwan_regulatory`, query source `tfda`) come from Taiwan's TFDA, not Australia's TGA/ARTG. No TGA/ARTG-specific market or product data was available for this evaluation — this should be sourced separately before any Australian regulatory decision is made.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for propylene glycol is not available in this evidence pack. Based on what is known, propylene glycol is not itself a drug with a defined pharmacological indication — it is a small, water-miscible diol used industry-wide as a solvent, humectant and vehicle, including in oral liquids, inhaler formulations, and e-liquid ("vaping") solutions.

Because propylene glycol appears so frequently as a carrier ingredient in respiratory-related formulations and literature, the TxGNN knowledge graph likely picked up a **co-occurrence signal** rather than a genuine pharmacological treatment relationship. This is confirmed by the evidence itself: none of the four retrieved clinical trials tested propylene glycol — all four were trials of inhaled **cyclosporine** for bronchiolitis obliterans, where propylene glycol (if present at all) would only be an inactive formulation component. Similarly, the literature retrieved is dominated by reviews of e-cigarette aerosol (of which propylene glycol is a common constituent) and its potential to *cause or worsen* lung disease — an exposure-harm relationship, which is the opposite direction of a therapeutic claim.

In short, the high TxGNN score reflects proximity in the knowledge graph, not an established mechanism by which propylene glycol would treat bronchitis. This prediction should be treated as hypothesis-generating only.

---

## Clinical Trial Evidence

All four trials below tested **cyclosporine inhalation solution**, not propylene glycol, and are included only because they were retrieved under the "bronchitis/bronchiolitis" disease label. They do not constitute direct evidence for propylene glycol.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00755781](https://clinicaltrials.gov/study/NCT00755781) | Phase 3 | Completed | 284 | Evaluated cyclosporine inhalation solution (CIS), not propylene glycol, for preventing bronchiolitis obliterans syndrome after lung transplant |
| [NCT00938236](https://clinicaltrials.gov/study/NCT00938236) | Phase 3 | Terminated | 17 | Long-term extension of the inhaled-cyclosporine trial; terminated early, unrelated to propylene glycol |
| [NCT01273207](https://clinicaltrials.gov/study/NCT01273207) | Phase 2 | Completed | 7 | Extended-access cyclosporine inhalation for bronchiolitis obliterans post-transplant |
| [NCT01287078](https://clinicaltrials.gov/study/NCT01287078) | Phase 2 | Completed | 25 | Phase II cyclosporine inhalation trial for bronchiolitis obliterans syndrome |

---

## Literature Evidence

None of the three publications studied propylene glycol as a treatment for bronchitis; two concern e-cigarette-related lung harm (propylene glycol as an aerosol constituent) and one is an unrelated animal model of a different compound (quercetin).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26408554](https://pubmed.ncbi.nlm.nih.gov/26408554/) | 2015 | Review | Am J Physiol Lung Cell Mol Physiol | Reviews potential lung harm from chronic e-cigarette use (propylene glycol-based aerosols), including chronic bronchitis risk — a harm signal, not a treatment signal |
| [28983782](https://pubmed.ncbi.nlm.nih.gov/28983782/) | 2017 | Review | Curr Allergy Asthma Rep | Reviews e-cigarette constituents (including propylene glycol) and their possible links to asthma/airway disease |
| [20920189](https://pubmed.ncbi.nlm.nih.gov/20920189/) | 2010 | Animal study | Respiratory Research | Mouse model of COPD/chronic bronchitis treated with quercetin, not propylene glycol — not directly relevant |

---

## Market Information

Propylene glycol has **no product entries** in the Taiwan TFDA data used to build this Evidence Pack (`total_licenses: 0`, market status: Not Marketed). No Australian TGA/ARTG-specific data was available in this pack, so Australian market status and ARTG entries cannot be reported here and should be verified directly against the TGA ARTG database.

---

## Safety Considerations

No structured safety data (key warnings, contraindications, or drug interactions) is currently available in this Evidence Pack — all fields returned as data gaps or "not found." Please refer to the applicable, jurisdiction-specific Product Information (PI) or Safety Data Sheet for propylene glycol-containing products before clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence retrieved for the bronchitis prediction does not actually support it — the clinical trials tested an unrelated drug (cyclosporine), and the literature largely describes potential lung harm from propylene glycol-containing aerosols rather than any treatment benefit. Combined with the absence of an established mechanism of action, this does not meet the bar to advance beyond a model-generated hypothesis.

**To proceed, the following is needed:**
- A confirmed mechanism of action for propylene glycol relevant to airway/respiratory disease (currently a data gap)
- Trials or literature that test propylene glycol itself against bronchitis, not formulations that merely contain it as an excipient
- TFDA-approved PI warnings/contraindications (currently a blocking data gap for any safety review) and, separately, TGA-specific PI/ARTG data if an Australian regulatory pathway is being considered
- For context: of the other TxGNN-predicted indications for this drug, **diabetic retinopathy** (rank 3, evidence level L3) had comparatively more substantive literature, though it too was largely indirect (formulation/vehicle studies rather than PG-specific treatment data) and would need similar scrutiny before being considered a stronger candidate than bronchitis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

