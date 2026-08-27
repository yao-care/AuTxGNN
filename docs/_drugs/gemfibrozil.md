---
layout: default
title: Gemfibrozil
parent: 僅模型預測 (L5)
nav_order: 309
evidence_level: L5
indication_count: 10
---

# Gemfibrozil
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

# Gemfibrozil: From Dyslipidaemia (Hypertriglyceridaemia) to Rheumatoid Arthritis

## One-Sentence Summary

Gemfibrozil is a fibrate-class lipid-regulating agent, long established for treating hypertriglyceridaemia/dyslipidaemia. The TxGNN model's top-ranked prediction suggests it may be effective for **Rheumatoid Arthritis**, but this is currently supported by **0 clinical trials** and only **4 preclinical/case-level publications**, none of which tested gemfibrozil directly in a rheumatoid arthritis model.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dyslipidaemia / Hypertriglyceridaemia (fibrate class — established use, not sourced from an Australian product licence as the drug is not currently marketed here) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for gemfibrozil is not available in this evidence pack (flagged as a High-severity data gap; remediation requires a DrugBank API query). Based on established, well-documented information, gemfibrozil is a fibrate-class agent that activates PPAR-α (peroxisome proliferator-activated receptor alpha); its efficacy in treating hypertriglyceridaemia and dyslipidaemia is well proven (see literature evidence under other predicted indications in this dossier, e.g. the Helsinki Heart Study referenced in PMID 8736620).

The rheumatoid arthritis prediction rests on the broader pharmacological logic that PPAR agonists as a class can exert anti-inflammatory effects — in animal models, PPAR activation has been linked to suppression of NF-κB signalling and modulation of regulatory T-cell (Treg/Foxp3) activity. However, the most directly relevant mechanistic study identified (PMID 41207105) tested **bezafibrate**, a pan-PPAR agonist, not gemfibrozil, which is a selective PPAR-α agonist — this pharmacological difference means the finding cannot be safely extrapolated to gemfibrozil. The remaining literature consists of a case report on an unrelated dermatological sign, a rat adjuvant-induced arthritis model combining gemfibrozil with steroids, and an EAE (not RA) T-cell study. No clinical trials or gemfibrozil-specific RA studies currently exist, so the mechanistic case remains a research hypothesis rather than a clinically actionable signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30074417](https://pubmed.ncbi.nlm.nih.gov/30074417/) | 2019 | Animal study (rat model) | Modern Rheumatology | Combined gemfibrozil + low-dose prednisolone produced a similar therapeutic effect to full-dose steroid in a rat adjuvant-induced arthritis model |
| [41207105](https://pubmed.ncbi.nlm.nih.gov/41207105/) | 2026 | Animal study | International Immunopharmacology | Bezafibrate (a pan-PPAR agonist, not gemfibrozil) attenuated experimental rheumatoid arthritis via PPAR-γ-dependent anti-inflammatory pathways |
| [20083653](https://pubmed.ncbi.nlm.nih.gov/20083653/) | 2010 | Animal study | Journal of Immunology | Nitric oxide-mediated reduction of Foxp3 (Treg marker) expression following myelin basic protein priming — an EAE autoimmune model, not RA |
| [18039017](https://pubmed.ncbi.nlm.nih.gov/18039017/) | 2007 | Case report | American Journal of Clinical Dermatology | Review of palmar erythema as a marker of systemic disease; not specific to gemfibrozil or RA |

---

## Australia Market Information

Gemfibrozil currently has no ARTG entries and no registered products in Australia (market status: Not Marketed). No product/indication information is available to summarise.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No PI currently exists for this product in Australia, and drug interaction data for gemfibrozil returned no results in this query cycle (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Hold — Research Question**

**Rationale:**
The mechanistic link to rheumatoid arthritis is indirect — the key supporting study used bezafibrate (pan-PPAR agonist), not gemfibrozil (selective PPAR-α agonist) — and no gemfibrozil-specific clinical or preclinical RA data exist. A Blocking-severity data gap (TFDA/PI warnings and contraindications unavailable) also prevents any S1 safety evaluation.

**To proceed, the following is needed:**
- TFDA/PI warnings, precautions and contraindications (Blocking gap — required before any safety review)
- Confirmed mechanism-of-action data from DrugBank (High-severity gap)
- A gemfibrozil-specific (not bezafibrate) preclinical or clinical study in an RA model
- Drug interaction data, currently returning no results

**Note:** This evidence pack contains multiple predicted indications for gemfibrozil. Rank 4, hypoalphalipoproteinemia, has substantially stronger and more directly relevant evidence (Evidence Level L2, decision stage S2, "Proceed with Guardrails") and may warrant a separate evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

