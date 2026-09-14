---
layout: default
title: Voriconazole
parent: 僅模型預測 (L5)
nav_order: 727
evidence_level: L5
indication_count: 10
---

# Voriconazole
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

# Voriconazole: From Invasive Fungal Infections to Multidrug-Resistant Tuberculosis

## One-Sentence Summary

Voriconazole is a triazole antifungal, pharmacologically used to treat invasive fungal infections such as invasive aspergillosis and serious *Candida* infections. The TxGNN model predicts it may be effective for **multidrug-resistant tuberculosis (MDR-TB)**, but this direction is currently supported only by **0 clinical trials** and **3 incidental case reports**, with no mechanistic basis identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Invasive fungal infections (e.g. invasive aspergillosis, candidaemia) — triazole antifungal class; not confirmed in local regulatory data |
| Predicted New Indication | Multidrug-resistant tuberculosis (MDR-TB) |
| TxGNN Prediction Score | 98.67% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the evidence pack (`original_moa: [Data Gap]`). However, supplementary information in the repurposing rationale confirms Voriconazole is a **triazole antifungal** that inhibits fungal **CYP51 (14α-lanosterol demethylase)**, blocking ergosterol synthesis in fungal cell membranes.

This mechanism has **no known activity against mycobacterial cell wall synthesis**, and there is no established pharmacological pathway linking Voriconazole to *Mycobacterium tuberculosis*. The evidence pack itself states explicitly: *"與 MDR-TB 無直接藥理關聯" (no direct pharmacological relationship with MDR-TB)*.

The three literature citations retrieved for this prediction describe **fungal infections coexisting with, or mimicking, tuberculosis** (e.g. aspergilloma in an MDR-TB patient; drug-resistant fungal pathogens) — not any therapeutic effect of Voriconazole on *M. tuberculosis*. This pattern is consistent with a **knowledge-graph co-occurrence artefact** (shared clinical context — immunocompromised/diabetic patients, drug resistance terminology) rather than a genuine repurposing signal. The high TxGNN score should therefore be interpreted with caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18992166](https://pubmed.ncbi.nlm.nih.gov/18992166/) | 2008 | Case Report | Cases Journal | MDR-TB coexisting with aspergilloma/invasive aspergillosis in a diabetic patient; Voriconazole relevant to the fungal co-infection, not the TB itself |
| [37145297](https://pubmed.ncbi.nlm.nih.gov/37145297/) | 2023 | Case Report / In vitro | Braz J Microbiol | Photodynamic inactivation of multidrug-resistant *Fonsecaea nubica* (fungal, not mycobacterial) |
| [39359062](https://pubmed.ncbi.nlm.nih.gov/39359062/) | 2024 | Basic Research | Virulence | Genetic diversity of fluconazole-resistant *Candida krusei*; unrelated to TB |

**Note:** None of these publications report use of Voriconazole for treating tuberculosis or MDR-TB. They are included in the evidence pack due to shared "multidrug-resistant" and infectious-disease context.

---

## Australia Market Information

Voriconazole currently has **no ARTG entries** in the evidence pack (`total_licenses: 0`, market status: **Not marketed**). No dosage form or approved indication data is available locally.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No drug interaction, warning, or contraindication data was available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction carries a high TxGNN score but has **no mechanistic plausibility** (antifungal CYP51 inhibition vs. mycobacterial biology) and **no supporting clinical or preclinical evidence** — the retrieved literature only reflects incidental co-occurrence of fungal infection and TB terminology, not a therapeutic signal. This corresponds to Evidence Level L5 and does not meet the threshold to advance past S0.

**To proceed, the following is needed:**
- Confirmed mechanism of action data (MOA) for Voriconazole (currently a data gap, DG002)
- TFDA/TGA-equivalent Product Information — warnings, contraindications, and DDI data (currently a blocking data gap, DG001)
- Preclinical evidence of any anti-mycobacterial activity (in vitro MIC data against *M. tuberculosis*, including MDR/XDR strains)
- Clarification of Voriconazole's actual approved indications and Australian regulatory/market status, since no ARTG record currently exists

**Note on other candidates in this evidence pack:** Ranks 2–10 (cysticercosis, Ambras hypertrichosis, Dandy-Walker syndrome, periodontal malformation syndrome, bovine/avian tuberculosis, tuberculoma, tuberculous ascites, isolated hair shaft abnormality) all carry **L4–L5 evidence** with **no clinical trials** and either no literature or literature unrelated to a genuine drug-disease mechanism. None are recommended to proceed; all are flagged **Hold** in the source data.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

