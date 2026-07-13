---
layout: default
title: Capecitabine
parent: 僅模型預測 (L5)
nav_order: 120
evidence_level: L5
indication_count: 10
---

# Capecitabine
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

# Capecitabine: From Gastric Cancer to Gastric Adenocarcinoma and Proximal Polyposis of the Stomach (GAPPS)

---

## One-Sentence Summary

Capecitabine is an oral fluoropyrimidine prodrug chemotherapy, widely used internationally as a component of standard-of-care regimens for gastric, colorectal, and breast cancer — however, no TGA/ARTG registration data was retrievable in the current dataset, which warrants independent verification.
The TxGNN model predicts it may be effective for **Gastric Adenocarcinoma and Proximal Polyposis of the Stomach (GAPPS)**, an extremely rare hereditary syndrome caused by APC promoter 1B mutations.
Currently, **no clinical trials and no published literature** specifically address this indication — evidence level is **L5 (model prediction only)**, and the recommended decision is **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No TGA/ARTG-approved indication data available in current dataset |
| Predicted New Indication | Gastric Adenocarcinoma and Proximal Polyposis of the Stomach (GAPPS) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Australia Market Status | Not registered (0 ARTG entries in current dataset — see note below) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

> **⚠️ Data Verification Required:** Capecitabine (brand name Xeloda, Roche) is widely known to be TGA-registered and listed on the Australian PBS for colorectal cancer, gastric cancer, and breast cancer. The absence of ARTG entries in this dataset is likely a query limitation rather than a true absence of registration. Australian healthcare professionals should verify current registration status directly via the [TGA ARTG public search](https://www.tga.gov.au/resources/artg).

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, capecitabine is part of the fluoropyrimidine class of cytotoxic chemotherapy. It is an orally administered prodrug that undergoes sequential enzymatic conversion: first to 5′-deoxy-5-fluorouridine (5′-DFUR) via hepatic carboxylesterase, then to active 5-fluorouracil (5-FU) by thymidine phosphorylase (TP) — an enzyme that is preferentially expressed in tumour tissue relative to normal tissue, providing a degree of tumour-selective activation. Active 5-FU then inhibits thymidylate synthase (TS), blocking de novo dTMP synthesis and thereby halting DNA replication. Its efficacy in gastric adenocarcinoma has been established through multiple Phase 3 trials globally (e.g., CLASSIC, RESOLVE), and mechanistically this pathway is applicable wherever TP expression is sufficient to activate the prodrug.

GAPPS is caused by germline point mutations in the APC gene's promoter 1B region, leading to fundic gland polyposis of the proximal stomach and a risk of malignant transformation to gastric adenocarcinoma. The mechanistic link between capecitabine and GAPPS-associated adenocarcinoma is indirect: GAPPS-related cancers are expected to retain the gastric adenocarcinoma phenotype — where TP expression and 5-FU sensitivity have been demonstrated — making the TP → 5-FU → TS inhibition pathway theoretically applicable to any adenocarcinoma arising within this syndrome.

However, the practical applicability of capecitabine to GAPPS is highly uncertain. The syndrome is so rare that the specific molecular characteristics of GAPPS-associated adenocarcinoma — including TP/TS expression levels, Lauren classification (intestinal vs. diffuse), microsatellite instability status, and chemotherapy sensitivity patterns — have not been characterised in any published research. Without this data, it is not possible to confirm whether the TP-mediated activation pathway will function efficiently in tumours arising from this genetic background. The TxGNN model's high score most likely reflects generalised pattern recognition linking capecitabine to gastric adenocarcinoma broadly, rather than specific evidence for GAPPS as a distinct disease entity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for capecitabine in GAPPS.

---

## Literature Evidence

Currently no related literature available for capecitabine in GAPPS.

---

## Australia Market Information

No ARTG entries were retrieved for capecitabine in the current dataset. As noted above, this is likely a data query limitation. Based on publicly available TGA records, capecitabine-containing products (e.g., Xeloda 150 mg and 500 mg tablets) are registered in Australia for the treatment of colorectal cancer, gastric cancer, and breast cancer, and are PBS-listed. Healthcare professionals should consult the TGA ARTG directly for current registration details and the approved Product Information (PI).

---

## Cytotoxicity

Capecitabine is a conventional cytotoxic chemotherapy agent (fluoropyrimidine class). This section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Fluoropyrimidine prodrug (oral 5-FU precursor) |
| Myelosuppression Risk | Moderate — neutropenia, thrombocytopenia, and anaemia occur; generally less myelosuppressive than infusional IV 5-FU; nadir typically at days 10–14 |
| Emetogenicity Classification | Low (single agent); may increase to moderate in combination regimens (e.g., CAPOX with oxaliplatin) |
| Monitoring Items | Full blood count with differential (before each cycle), liver function tests, renal function and eGFR (dose reduction required if CrCl < 50 mL/min; contraindicated if CrCl < 30 mL/min), coagulation studies (INR) if co-prescribed with warfarin |
| Handling Protection | Oral cytotoxic — must be handled in accordance with state/territory cytotoxic safe handling guidelines (e.g., SHPA standards); tablets must not be crushed, split, or dissolved; carers/handlers should avoid direct contact with the tablets |

---

## Safety Considerations

Formal TGA-approved Product Information warnings and contraindication data were not available in this evidence pack. Please refer to the TGA-approved Product Information (PI) for complete safety information.

**Clinically important interactions known for the fluoropyrimidine class:**
- **Warfarin / vitamin K antagonists:** Capecitabine substantially potentiates anticoagulant effect; INR monitoring is mandatory and warfarin dose reduction is typically required
- **Phenytoin:** Capecitabine may increase phenytoin plasma levels; monitor for toxicity and adjust phenytoin dose as needed
- **Allopurinol:** May reduce the efficacy of fluoropyrimidines — avoid concurrent use where possible

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
GAPPS is an extremely rare hereditary syndrome with no published clinical trials, case series, or mechanistic studies evaluating capecitabine specifically in this disease entity. The evidence level is L5 — model prediction only — and the fundamental tumour biology of GAPPS-associated adenocarcinoma (including TP/TS expression and chemotherapy sensitivity) has not been characterised. There is insufficient basis to proceed with clinical planning at this stage.

**To proceed, the following is needed:**
- Histopathological and molecular characterisation of GAPPS-associated gastric adenocarcinoma (TP/TS expression, HER2 status, MSI status, Lauren classification) to assess whether capecitabine's activation pathway is operative in this context
- Registry-based or case series data on systemic chemotherapy outcomes in GAPPS patients who develop gastric adenocarcinoma
- Verification of current TGA ARTG registration status for capecitabine-containing products via the live TGA ARTG database
- Retrieval of the full TGA-approved Product Information (PI) to complete the safety assessment (warnings, contraindications, full DDI profile)
- Formal MOA data from DrugBank (DB01101) to complete the mechanistic analysis

> **Note for context:** While GAPPS (rank 1) is the top TxGNN prediction and carries a Hold recommendation, higher-quality evidence exists for capecitabine in related gastric adenocarcinoma subtypes within this same evidence pack — including gastric tubular adenocarcinoma (rank 3, L3, Proceed with Guardrails, supported by multiple Phase 3 RCTs including CLASSIC PMID 22226517), gastric cardia adenocarcinoma (rank 5, L2), and gastric body carcinoma (rank 8, L2). These indications may warrant separate evaluation reports.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

