---
layout: default
title: Dapagliflozin
parent: 僅模型預測 (L5)
nav_order: 180
evidence_level: L5
indication_count: 10
---

# Dapagliflozin
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

# Dapagliflozin: From Type 2 Diabetes to Classic Stiff Person Syndrome

## One-Sentence Summary

Dapagliflozin is a sodium-glucose co-transporter 2 (SGLT2) inhibitor, internationally established for type 2 diabetes and related cardiorenal conditions (this drug is **not currently registered in the Australian ARTG**, so a locally approved indication text is not available in this evidence pack). The TxGNN model predicts it may be effective for **Classic Stiff Person Syndrome**, but this prediction is currently supported by **zero clinical trials and zero publications**, and the evidence pack's own mechanistic review found no known biological link between SGLT2 inhibition and the GAD65/GABA-ergic autoimmune pathology underlying this disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (general pharmacological knowledge; not present in this evidence pack — no ARTG-sourced indication text available, as the drug is not marketed in Australia) |
| Predicted New Indication | Classic Stiff Person Syndrome |
| TxGNN Prediction Score | 98.20% |
| Evidence Level | L5 (model prediction only — no clinical trials or literature) |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on general pharmacological knowledge, dapagliflozin is an SGLT2 inhibitor that reduces renal glucose reabsorption in the proximal tubule; its established efficacy is in glycaemic control, and it also carries cardiorenal protective indications in several jurisdictions. This mechanism operates entirely within renal glucose handling and downstream metabolic/haemodynamic pathways.

Classic Stiff Person Syndrome (SPS), by contrast, is a central nervous system autoimmune disorder driven predominantly by anti-GAD65 (glutamic acid decarboxylase) antibodies that impair GABA-ergic neurotransmission. The evidence pack's own rationale, generated after a targeted literature search, found **no known intersection** between SGLT2 physiology and GAD65 autoimmunity or GABA-ergic signalling. The most plausible explanation offered is that the high TxGNN score reflects an indirect graph relationship — likely routed through a shared "diabetes-associated neuropathy" node in the knowledge graph — rather than any direct mechanistic or clinical evidence.

In short, this is a case where the TxGNN score is high but the underlying biological rationale is weak. The model's statistical association should not be interpreted as evidence of therapeutic plausibility without an identified mechanistic pathway, which is absent here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

No ARTG entries are currently registered for Dapagliflozin in this dataset (market status: Not Marketed, 0 total licences). No product/dosage-form/indication information is available to tabulate.

---

## Safety Considerations

- **Drug Interactions**: A dedicated DDI search returned no results (`query_status: not_found`, 0 interactions on record).

As Dapagliflozin does not currently hold an ARTG registration in Australia, no locally approved TGA Product Information exists for this evidence pack to draw on. Safety information — including key warnings and contraindications — is a **Blocking** data gap (DG001) and must be sourced from overseas regulatory references (e.g., FDA label, EMA SmPC, or the manufacturer's PI in a country where the product is registered) before any safety-related assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Classic Stiff Person Syndrome) has no supporting clinical trials, no supporting literature, and the evidence pack's own mechanistic review identified no plausible biological link to the drug's known pharmacology — this is an L5, statistics-only association. Combined with the drug's non-marketed status in Australia and a Blocking-severity data gap on TFDA/TGA safety labelling, there is currently no basis to advance this candidate beyond hypothesis-generation.

It is worth noting that among the other nine candidates in this evidence pack, none reached a stronger evidence tier: rank 4 (thiamine-responsive dysfunction syndrome / TRMA) reached L4 only via an indirect argument (TRMA patients often have comorbid insulin-dependent diabetes, not that dapagliflozin treats the underlying transporter defect), and rank 9 (pancreatic agenesis) has a single preclinical rat-model publication whose disease model (diet-induced diabetic pancreatic injury) does not match the congenital condition predicted. None of the ten candidates reached a "Go" or "Proceed with Guardrails" recommendation.

**To proceed, the following is needed:**
- Mechanism of action data via DrugBank API query (DG002)
- TFDA/TGA-equivalent Product Information — warnings, contraindications, precautions (DG001, Blocking)
- Confirmation of any pathway toward Australian market registration, since the drug currently has zero ARTG entries
- A dedicated literature/mechanism search specifically probing SGLT2 inhibition in autoimmune/neuro-inflammatory conditions, to confirm the absence of a plausible pathway before this candidate is closed out
- If pursued further, prioritise the TRMA (rank 4) and metabolic-complication lipodystrophy (rank 5) candidates over the top-ranked SPS prediction, as their rationale at least identifies an indirect clinical (not mechanistic) diabetes-comorbidity link
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

