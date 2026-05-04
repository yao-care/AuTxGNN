---
layout: default
title: Corifollitropin Alfa
parent: 僅模型預測 (L5)
nav_order: 129
evidence_level: L5
indication_count: 10
---

# Corifollitropin Alfa
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

# Corifollitropin alfa: From Controlled Ovarian Stimulation to Gastroduodenitis

## One-Sentence Summary

Corifollitropin alfa (Elonva) is a long-acting recombinant follicle-stimulating hormone (FSH) analogue, clinically used for controlled ovarian stimulation in women undergoing assisted reproductive technology (ART). The TxGNN model predicts it may have potential activity against **Gastroduodenitis**, however **no clinical trials** and **no supporting publications** have been identified for this indication. All ten predicted indications are rated **L5** (model prediction only), and the overall recommendation across the board is **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Australia — known pharmacological use: controlled ovarian stimulation (ART) |
| Predicted New Indication | Gastroduodenitis |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on published pharmacology, Corifollitropin alfa is a chimeric FSH–CTP (chorionic gonadotropin carboxy-terminal peptide) fusion protein that acts as a sustained FSH agonist, binding to FSH receptors (FSHR) on granulosa and Sertoli cells to drive follicular development. Its extended half-life (~65 hours) allows a single subcutaneous injection to replace daily FSH dosing during the first week of ovarian stimulation.

The mechanistic link between FSH receptor signalling and gastroduodenitis is highly speculative. Direct evidence for FSHR expression on gastroduodenal mucosa is extremely limited. The most plausible knowledge graph (KG) inference pathway would run: FSH signalling → pro-inflammatory cytokines (IL-6, TNF-α) → gastric mucosal injury — however this chain has no experimental backing in the published literature, and the rationale is accordingly rated as highly inferential.

It is also noteworthy that the TxGNN score for this prediction is 99.65% (rank 4,598 globally), yet zero clinical trials and zero supporting publications were found. This pattern — high model confidence with no corroborating human evidence — is consistent with graph topology clustering effects rather than genuine biological plausibility. The gastrointestinal cluster (gastroduodenitis, peptic ulcer disease, peptic oesophagitis) appearing together in the top ten predictions further suggests shared disease-ontology adjacency in the KG rather than independent pharmacological signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Corifollitropin alfa is not registered with the Therapeutic Goods Administration (TGA) and holds no ARTG entries. It is not currently available on the Australian market. Note that Elonva is approved in the European Union and other jurisdictions — TGA registration would require a separate application process.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No Australian-specific safety data (warnings, contraindications, or drug interactions) is available in this Evidence Pack. Healthcare professionals should consult the EMA-approved SmPC (Elonva Summary of Product Characteristics) as the closest available reference document.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten TxGNN-predicted indications for Corifollitropin alfa are rated L5 with no clinical trials, no supporting literature, and no established mechanistic basis linking FSH receptor signalling to gastroduodenitis or any of the other predicted conditions. The drug is not registered in Australia (0 ARTG entries), adding a substantial regulatory barrier on top of the absent clinical evidence.

**To proceed, the following is needed:**

- **Mechanism of action (MOA) data** — retrieve from DrugBank API (DB09066) or published FSH receptor pharmacology literature to enable a rigorous mechanistic plausibility assessment
- **Preclinical evidence search** — targeted literature review for FSHR expression in gastroduodenal tissue, or FSH pathway involvement in gastric mucosal inflammation
- **Safety data** — download and parse the EMA SmPC / manufacturer PI for warnings, contraindications, and DDI profile; TFDA monograph review also recommended
- **Broader indication review** — among the ten predictions, pulmonary hypertension (rank 6) has the strongest stated biological rationale (published FSHR expression in pulmonary artery smooth muscle and endothelial cells); this may be a more productive candidate to pursue ahead of gastroduodenitis
- **Australian regulatory pathway assessment** — confirm whether a TGA application is feasible given the drug's off-patent status and current global approval landscape
- **Clinical pharmacologist review** — independent expert assessment of biological plausibility before committing resources to any experimental work

> ⚠️ **Research disclaimer:** This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. Data as of 4 April 2026.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

