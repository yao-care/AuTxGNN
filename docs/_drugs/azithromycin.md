---
layout: default
title: Azithromycin
parent: 僅模型預測 (L5)
nav_order: 73
evidence_level: L5
indication_count: 10
---

# Azithromycin
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

# Azithromycin: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Azithromycin is a macrolide antibiotic with broad-spectrum activity against a wide range of bacterial pathogens, commonly used to treat community-acquired pneumonia, skin and soft tissue infections, and sexually transmitted infections. The TxGNN model predicts it may be effective for **Hyperamylasemia** (elevated serum amylase), with **no clinical trials** and **no publications** currently providing direct supporting evidence for this specific indication. At this stage, the prediction is classified as evidence level **L5** — model prediction only — and a **Hold** decision is recommended pending mechanistic validation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from TGA registration data (see note below) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 (Model prediction only — no clinical studies identified) |
| Australia Market Status | Not marketed (no ARTG entries found in dataset) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

> **Data note:** No TGA registration data was retrieved for azithromycin in this dataset (query returned 0 results). This is likely a data retrieval gap — azithromycin (e.g., Zithromax®) is a widely used antibiotic in Australian clinical practice. Clinicians should verify current ARTG registration status directly via the [TGA ARTG database](https://www.tga.gov.au/resources/artg).

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Azithromycin is a macrolide antibiotic that inhibits bacterial protein synthesis by binding irreversibly to the 50S ribosomal subunit, thereby blocking translocation of peptidyl-tRNA. Beyond its antimicrobial effect, azithromycin is well-recognised for secondary immunomodulatory and anti-inflammatory properties — including suppression of pro-inflammatory cytokine production (IL-6, IL-8, TNF-α), inhibition of neutrophil recruitment, and modulation of macrophage activity. This dual antimicrobial–anti-inflammatory profile underpins its established use in chronic inflammatory airway conditions such as cystic fibrosis and bronchiectasis.

Hyperamylasemia — defined as persistently elevated serum amylase — most commonly reflects acute pancreatitis, parotitis, or other pancreatic and salivary gland pathology. A secondary infectious aetiology (e.g., mumps, bacterial parotitis, or infectious pancreatitis) could theoretically create an indirect pharmacological rationale, whereby azithromycin's antibacterial and anti-inflammatory actions might reduce glandular inflammation and consequently normalise amylase levels. However, this remains speculative.

As documented in the repurposing rationale within the Evidence Pack, there is **no established mechanistic link** between azithromycin's known actions and amylase regulation. The TxGNN knowledge graph prediction likely reflects indirect network associations rather than a direct therapeutic mechanism. This prediction should be considered hypothesis-generating only and requires mechanistic validation before further development.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

No TGA registration data was found for azithromycin in this dataset (0 ARTG entries returned). This is inconsistent with azithromycin's known availability in Australia and is likely a data retrieval issue. Please verify directly via the TGA ARTG public search portal before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

> No safety data (key warnings, contraindications, or drug interactions) was available in this Evidence Pack. Clinicians should consult the current TGA-approved PI for azithromycin, noting in particular the class-specific risks of QT prolongation, hepatotoxicity, and *C. difficile*-associated diarrhoea that are well-characterised for macrolide antibiotics.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or published literature evidence directly linking azithromycin to hyperamylasemia, and no clear mechanistic pathway has been established to support this indication. This remains a model-only prediction at the lowest evidence level (L5), and proceeding without foundational mechanistic data would not be appropriate.

**To proceed, the following is needed:**
- Mechanistic studies establishing a causal relationship between azithromycin and amylase normalisation (e.g., in vitro pancreatic or salivary gland cell models)
- Preclinical in vivo data exploring azithromycin's effect on experimentally induced hyperamylasemia
- A plausible clinical sub-population hypothesis (e.g., infectious or inflammatory aetiology of hyperamylasemia where azithromycin's dual activity could be leveraged)
- Retrieval of azithromycin's full TGA Product Information and DrugBank MOA entry (DB00207) to complete the safety and mechanistic assessment
- Verification of current ARTG registration status via the TGA database to establish the regulatory baseline for any future repurposing application

---

> **Disclaimer:** This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require prospective clinical validation before therapeutic application. All content should be interpreted in conjunction with current TGA-approved prescribing information.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

