---
layout: default
title: Ivacaftor
parent: 僅模型預測 (L5)
nav_order: 371
evidence_level: L5
indication_count: 10
---

# Ivacaftor
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

# Ivacaftor: From Cystic Fibrosis to Rheumatoid Arthritis

## One-Sentence Summary

Ivacaftor (brand name: Kalydeco) is a CFTR potentiator approved internationally for cystic fibrosis (CF) in patients with specific *CFTR* gene mutations, but is not currently registered on the Australian Register of Therapeutic Goods (ARTG).
The TxGNN model predicts it may have potential application in **Rheumatoid Arthritis**, with **1 clinical trial** (indirectly relevant, Grade C) and **1 publication** (animal/mechanistic study, Tier 3) currently identified.
Evidence is limited to model prediction with only tangential mechanistic support — this candidate remains at hypothesis-generation stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cystic fibrosis (patients with specific *CFTR* gating mutations, e.g. G551D) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 96.97% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed in Australia |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on established pharmacology, Ivacaftor is a small-molecule CFTR potentiator: it binds to the CFTR chloride channel protein and increases its open-channel probability in patients carrying specific gating mutations (e.g. G551D). This restores chloride ion transport across epithelial membranes, improving mucociliary clearance and lung function in CF.

The mechanistic link to rheumatoid arthritis is indirect and speculative. CFTR is expressed not only in airway epithelium but also in neutrophils — a key effector cell in RA synovial inflammation. CFTR potentiation in neutrophils may theoretically modulate reactive oxygen species (ROS) production and transepithelial migration capacity, both of which are implicated in RA pathology. One supporting data point comes from animal models of Sjögren's syndrome and autoimmune pancreatitis (PMID 28634110), where CFTR restoration reduced glandular inflammation — suggesting a broader immunomodulatory role for CFTR beyond airway epithelia.

However, this mechanistic chain is three or more steps removed from an RA therapeutic mechanism. There is no direct in vitro, animal, or clinical evidence validating Ivacaftor's effect in RA models. The TxGNN high prediction score most likely reflects the CFTR → immune regulation → systemic inflammation pathway as represented in the knowledge graph, rather than direct therapeutic evidence. This prediction is best treated as a hypothesis-generation signal warranting early mechanistic investigation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT04970225](https://clinicaltrials.gov/study/NCT04970225) | N/A | Completed | 47 | Prospective study examining neutrophil phenotype and function in CF patients, including the impact of CFTR modulator treatment and *Pseudomonas aeruginosa* infection. No RA patients enrolled; no RA outcome measures. Indirectly relevant only through shared neutrophil biology — does not constitute clinical evidence for Ivacaftor in RA. |

> **Note:** The sole identified trial (NCT04970225) was graded **C relevance** — it was conducted in CF patients, not RA patients, and did not measure RA-related outcomes. This trial does not support the RA repurposing hypothesis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [28634110](https://pubmed.ncbi.nlm.nih.gov/28634110/) | 2017 | Animal/Mechanistic Study | *Gastroenterology* | In mouse models of Sjögren's syndrome and autoimmune pancreatitis, restoring CFTR activity in ductal cells reduced glandular inflammation and rescued acinar cell function. Suggests CFTR may play a role in autoimmune inflammation beyond the lung — mechanistically relevant but not RA-specific, and not a human study. |

---

## Australia Market Information

Ivacaftor currently has **no ARTG entries** in Australia. As of the data cut-off (22 June 2026), the drug is not registered or marketed through the Therapeutic Goods Administration (TGA).

> For reference, Ivacaftor (Kalydeco®) is approved by the US FDA and EMA for cystic fibrosis with specific *CFTR* gating mutations. Clinicians and researchers seeking safety and prescribing information should consult the FDA-approved Prescribing Information or the EMA Summary of Product Characteristics, noting that these do not constitute TGA approval.

---

## Safety Considerations

Product Information (PI) warnings and contraindications specific to the Australian/TGA context are not available, as Ivacaftor is not registered on the ARTG.

Please refer to the **FDA-approved Prescribing Information (Kalydeco®)** or **EMA Summary of Product Characteristics** for detailed safety data, including hepatotoxicity monitoring requirements, drug–drug interactions with CYP3A4 modulators, and use in specific populations (paediatric, renal/hepatic impairment).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score to Ivacaftor for rheumatoid arthritis (96.97%), but the biological connection is indirect and unvalidated — no clinical trials, no RA-specific animal models, and no human pharmacological studies support this pairing. The single identified trial and publication are tangentially related through neutrophil biology only, insufficient to advance to clinical consideration.

**To proceed, the following is needed:**

- **Mechanistic validation:** In vitro studies examining Ivacaftor's effect on neutrophil ROS production, NETosis, or transepithelial migration in RA-relevant conditions
- **MOA gap closure:** Confirm Ivacaftor's full pharmacological profile in immune cell subtypes (neutrophils, macrophages) beyond airway epithelium
- **Animal model data:** Ivacaftor testing in established RA animal models (e.g. collagen-induced arthritis) to determine whether CFTR potentiation reduces synovial inflammation
- **Safety profile clarification:** Obtain full prescribing information and assess whether known drug interactions (particularly CYP3A4 pathway) present risks in a typical RA patient population who may be on DMARDs or biologics
- **TGA pathway assessment:** If preclinical data is supportive, evaluate whether a TGA Special Access Scheme or clinical trial application would be feasible given current non-marketed status in Australia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

