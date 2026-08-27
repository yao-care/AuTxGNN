---
layout: default
title: Latanoprost
parent: 僅模型預測 (L5)
nav_order: 387
evidence_level: L5
indication_count: 10
---

# Latanoprost
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

# Latanoprost: From Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Latanoprost is a prostaglandin F2α (PGF2α) analogue whose established, worldwide use is in glaucoma and ocular hypertension. The TxGNN model predicts it may also be effective for **Primary Hereditary Glaucoma**, a rarer genetic subtype, and this is best understood as an extension of its existing use rather than a novel repurposing hypothesis. Currently **1 completed Phase 2 clinical trial** and **no published literature** support this specific indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — no Taiwan licence record exists (market status: Not marketed, 0 ARTG/TFDA entries). Latanoprost's globally recognised original use is glaucoma / ocular hypertension, per the mechanistic rationale in this evidence pack. |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Latanoprost is a PGF2α receptor agonist. It lowers intraocular pressure by increasing uveoscleral (uveal-scleral) outflow of aqueous humour — this is the standard, well-established pharmacological mechanism underlying its use in glaucoma treatment. (Formal DrugBank-curated MOA text was not available in this evidence pack; the mechanism above is drawn from the repurposing rationale supplied alongside the prediction.)

Primary Hereditary Glaucoma is a genetic subtype within the same broad glaucoma disease category that latanoprost already treats. The evidence pack itself flags this explicitly: this is **not a novel mechanistic hypothesis**, but rather an extension of an already-proven indication into a hereditary/paediatric subgroup. Because the drug's IOP-lowering mechanism is disease-subtype-agnostic (it acts on aqueous outflow regardless of the underlying genetic cause of raised pressure), extrapolation to hereditary glaucoma is pharmacologically reasonable and is directly supported by a completed paediatric trial (below).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Phase 2 | Completed | 37 | Evaluated the ocular hypotensive effect and safety of latanoprost vs dorzolamide in patients with primary paediatric glaucoma refractory to surgery. |

*No ANZCTR-registered trials were identified for this indication.*

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication represents a mechanistically well-grounded extension of latanoprost's known glaucoma-lowering effect into a hereditary subtype, supported by one completed Phase 2 paediatric trial (L2 evidence). However, safety documentation (warnings, contraindications, drug interactions) and formal local regulatory status are currently unavailable, so this cannot yet move to unconditional approval.

**To proceed, the following is needed:**
- TFDA/TGA-approved Product Information, including warnings and contraindications (currently a Blocking data gap)
- Formal DrugBank-curated mechanism of action record
- Confirmation of drug interaction (DDI) profile — current query returned no results
- Additional trial or registry evidence specific to hereditary glaucoma subtypes beyond the single paediatric study identified
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

