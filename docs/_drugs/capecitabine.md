---
layout: default
title: Capecitabine
parent: Model Prediction Only (L5)
nav_order: 129
evidence_level: L5
indication_count: 1
monitor_inn: "Capecitabine"
predicted_indications: ["gastric adenocarcinoma and proximal polyposis of the stomach"]
last_modified_at: 2026-10-30
description: "Capecitabine: predicted new indication Gastric adenocarcinoma and proximal polyposis of the stomach (evidence level L5). Approved use: Gastric cancer and metastasis from malignant tumour of colon"
---

# Capecitabine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Capecitabine: From Gastric Cancer to Gastric Adenocarcinoma and Proximal Polyposis of the Stomach
{: .text-alpha }

## One-Sentence Summary

Capecitabine is an oral fluoropyrimidine chemotherapy. The TxGNN model predicts it may be useful for **gastric adenocarcinoma and proximal polyposis of the stomach (GAPPS)**, but the data compiled for this report contain **no clinical trials and no publications** on this condition, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastric cancer and metastasis from malignant tumour of colon (relations recorded in the knowledge graph; the Australian licence record contains no indication text) |
| Predicted New Indication | Gastric adenocarcinoma and proximal polyposis of the stomach |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for capecitabine: "Capecitabine is metabolized to fluorouracil in vivo. Both normal and tumor cells metabolize fluorouracil to 5-fluoro-2'-deoxyuridine monophosphate (FdUMP) and 5-fluorouridine triphosphate (FUTP). These metabolites cause cell injury by two different mechanisms." ([DailyMed: Xeloda (capecitabine) prescribing information, H2-Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e702d84d-7162-4751-bf37-d724cc7e45a5), label version 2026-02-05; accessed 2026-11-19.) Based on general pharmacology, capecitabine is a prodrug converted to 5-fluorouracil, which inhibits thymidylate synthase and disrupts DNA and RNA synthesis. This general knowledge is not drawn from the supplied data.

GAPPS is a rare hereditary syndrome associated with APC promoter 1B mutations. No syndrome-specific evidence was supplied, so whether capecitabine's mechanism applies to this setting is unverified.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 8362D | Capecitabine Sandoz | Tablet 500 mg | Not stated in the licence record |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine class) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions. The knowledge graph lists neutropenia, thrombocytopenia, agranulocytosis and anaemia as contraindication relations. |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI. Based on the graph-recorded relations, full blood count, liver function and renal function are relevant. |
| Handling Protection | Follow local cytotoxic drug handling requirements |

## Safety Considerations

- **Contraindication relations in the knowledge graph (not label text):** liver disease, gallbladder disease, thrombocytopenia, infectious disease, neutropenia, agranulocytosis, coronary artery disease, anaemia, macrocytic anaemia, hyperbilirubinaemia, hereditary hyperbilirubinaemia, Gilbert syndrome, impaired renal function, sudden cardiac arrest, heart conduction disease, necrotizing enterocolitis, stomatitis, and dihydropyrimidine dehydrogenase deficiency.
- **Drug interactions:** 100 interactions were found in the interaction query. The main ones listed are:
  - Moderate: metronidazole, tinidazole
  - Minor: aluminium hydroxide, levofloxacin, magaldrate, magnesium carbonate, magnesium hydroxide, magnesium oxide
  - Level unknown: pantoprazole, omeprazole, lansoprazole, glimepiride, doxycycline, morphine, metformin, atropine, prednisone, simvastatin, hydrocortisone, dolasetron

  Only the first 20 are shown in the data compiled for this report.

Warnings and contraindications from the TGA-approved Product Information were not available. Please refer to the PI for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but it comes from the TxGNN model (deep learning) only. There are no trials or publications on GAPPS, and the score may reflect similarities the model learned between related diseases, not biological evidence. Evidence level is L5.

**To proceed, the following is needed:**
- Syndrome-specific clinical or observational evidence in GAPPS
- Mechanism of action data
- TGA Product Information, including indications, warnings and contraindications
- A review of DPD deficiency testing and other safety considerations for this hereditary population

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Xeloda (capecitabine) prescribing information, H2-Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e702d84d-7162-4751-bf37-d724cc7e45a5) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

