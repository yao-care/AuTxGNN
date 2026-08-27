---
layout: default
title: Chlorambucil
parent: 僅模型預測 (L5)
nav_order: 142
evidence_level: L5
indication_count: 10
---

# Chlorambucil
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

Using the report template supplied in this conversation (no additional skill needed — the full specification is already given), I'll generate the report directly from the Evidence Pack JSON.

A structural note before the report: `predicted_indications[0]` (rank 1, TxGNN score 99.72%) is the **pregerminal centre (IGHV-unmutated) molecular subtype of CLL/SLL** — this is a prognostic subgroup of chlorambucil's own established indication, not a genuinely new disease. It also has zero dedicated trials and only one review-level citation. I've followed the extraction rules strictly (title/summary/tables all built from `predicted_indications[0]`), while flagging this nuance clearly so it isn't mistaken for a novel repurposing signal.

---

# Chlorambucil: From Chronic Lymphocytic Leukaemia/Small Lymphocytic Lymphoma to Pregerminal Centre (IGHV-Unmutated) CLL/SLL

## One-Sentence Summary

Chlorambucil is a nitrogen mustard alkylating agent with a decades-long track record in chronic lymphocytic leukaemia (CLL) and small lymphocytic lymphoma (SLL). The TxGNN model's top-ranked node refines this to the **pregerminal centre (IGHV-unmutated) molecular subtype of CLL/SLL** — a poorer-prognosis population — but this specific subtype currently has **no dedicated clinical trials** and only **one review-level publication** addressing it directly. Because this is a molecular refinement of an existing indication rather than a genuinely new disease target, and because Australian safety documentation is entirely absent, the evidence supporting action at this stage is preliminary.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Lymphocytic Leukaemia (CLL) / Small Lymphocytic Lymphoma (SLL) — chlorambucil's established, decades-old indication |
| Predicted New Indication | Pregerminal Centre (IGHV-Unmutated) CLL/SLL — a molecularly-defined, poorer-prognosis subtype of the same disease |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L2 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, chlorambucil is a nitrogen mustard alkylating agent, part of the classic alkylating-agent class of cytotoxic chemotherapy; its efficacy in chronic lymphocytic leukaemia/small lymphocytic lymphoma has been proven over decades of use, and mechanistically it may be applicable to the pregerminal centre (IGHV-unmutated) subtype of the same disease.

The predicted "new" indication is not a distinct disease — it is a molecular stratification node within CLL/SLL, defined by unmutated immunoglobulin heavy-chain variable-region (IGHV) genes. This subtype is recognised as carrying a worse prognosis than the IGHV-mutated ("post-germinal centre") counterpart. Because the disease entity itself is identical to chlorambucil's existing indication, there is a plausible mechanistic basis for activity. However, classic chlorambucil trials were largely conducted before routine IGHV stratification became standard practice, so this specific node has no dedicated trial registrations, and it is not established whether treatment response differs meaningfully by IGHV mutation status — some literature on chemoresistance suggests alkylating-agent response may be attenuated in IGHV-unmutated disease.

Broader disease-level evidence for chlorambucil in CLL/SLL as a whole is substantial (including multiple completed Phase 3 RCTs found elsewhere in this evidence pack, e.g. against ibrutinib, obinutuzumab combinations, and fludarabine). That evidence supports the parent indication but does not, on its own, confirm efficacy specifically within the IGHV-unmutated subgroup — which is the actual node TxGNN scored.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12577769](https://pubmed.ncbi.nlm.nih.gov/12577769/) | 2003 | Review | Nederlands Tijdschrift voor Geneeskunde | Discusses risk-adapted treatment strategies for CLL and describes the discovery of two molecular subtypes — a pregerminal centre (unmutated IGHV) subtype and a post-germinal centre (mutated IGHV) subtype — noting that CLL is not uniformly indolent and that a substantial proportion of patients require treatment and die of disease-related causes. |

## Australia Market Information

Chlorambucil currently has **no registered ARTG entries** and is **not marketed in Australia**. There is no TGA-approved Product Information on file to reference for local dosing, indications, or safety warnings. Any clinical use would need to proceed through the Special Access Scheme (SAS) or an equivalent unapproved therapeutic goods pathway, with sourcing from an overseas-registered product.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (nitrogen mustard alkylating agent) |
| Myelosuppression Risk | Moderate–High — a Phase 2 study in haematological malignancies (PMID 3307632) reported myelosuppression as a treatment-limiting toxicity; class-wide risk is well recognised for alkylating agents |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions — no local toxicity dataset available to classify confidently |
| Monitoring Items | Full blood count with differential (regular, given myelosuppression risk), liver and renal function; CNS toxicity has been reported at high doses (PMID 3179770) |
| Handling Protection | Yes — must be handled per cytotoxic drug handling regulations as a conventional chemotherapy agent |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No TFDA/TGA warnings, contraindications, or drug-drug interaction data were available in this evidence pack (DDI query returned no results). This is flagged as a **blocking data gap (DG001)** — safety documentation must be obtained before this candidate can advance to formal initial safety evaluation (S1).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction is a molecular subtype of chlorambucil's own existing indication rather than a novel disease target, and this specific subtype currently has zero dedicated trials and only one review-level citation. Combined with the absence of any TGA-approved Product Information (a blocking gap) and chlorambucil having zero ARTG entries in Australia, there is insufficient basis to proceed even under guardrails at this time.

**To proceed, the following is needed:**
- TGA-approved Product Information or TFDA label data (warnings, contraindications) — resolves blocking gap DG001
- Verified mechanism of action data from DrugBank or an equivalent primary source — resolves gap DG002
- IGHV-mutation-stratified outcome data specific to chlorambucil (or alkylator-based regimens generally), to determine whether efficacy genuinely differs in the pregerminal centre/unmutated subgroup
- Consideration of whether the disease-level indication (CLL/SLL as a whole, supported by multiple Phase 3 RCTs elsewhere in this evidence pack) is the more appropriate framing — noting this would represent confirmation of an existing indication rather than a new repurposing candidate
- Confirmation of a feasible Australian access pathway (e.g. Special Access Scheme) given the current absence of ARTG registration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

