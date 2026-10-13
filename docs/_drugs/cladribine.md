---
layout: default
title: Cladribine
parent: Model Prediction Only (L5)
nav_order: 167
evidence_level: L5
indication_count: 10
---

# Cladribine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Cladribine: From Hairy Cell Leukaemia and Multiple Sclerosis to Parameningeal Embryonal Rhabdomyosarcoma

## One-Sentence Summary

Cladribine is a purine nucleoside analogue originally used for hairy cell leukaemia and relapsing-remitting multiple sclerosis.
The TxGNN model predicts it may be effective for **parameningeal embryonal rhabdomyosarcoma**,
but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hairy cell leukaemia, hairy cell leukaemia variant, relapsing-remitting multiple sclerosis (from the knowledge graph; the ARTG entry has no indication text) |
| Predicted New Indication | Parameningeal embryonal rhabdomyosarcoma |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Cladribine is generally understood to be a purine nucleoside analogue that resists breakdown by adenosine deaminase and is toxic to lymphocytes and monocytes. Its activity depends on activation by deoxycytidine kinase (dCK).

Its established uses are in lymphoid disease (hairy cell leukaemia) and immune-mediated disease (multiple sclerosis), both linked to lymphocyte sensitivity. Solid tumours such as rhabdomyosarcoma are not generally reported to be sensitive to it, and no disease-specific mechanism has been established.

The top six predictions are all rhabdomyosarcoma subtypes with near-identical scores (0.997-0.998). This likely reflects a single signal from disease-ontology clustering in the knowledge graph rather than independent lines of evidence. A sensible first step would be laboratory data on dCK-dependent sensitivity in rhabdomyosarcoma cell lines.

Other predictions reviewed (none with clinical support):
- **Liver sarcoma** (score 99.70%, L4): the only publication is a 2004 case report of cladribine in smouldering systemic mastocytosis, which is a different disease and only indirect evidence.
- **Skeletal muscle neoplasm** (98.96%): a broad parent category overlapping with the rhabdomyosarcoma predictions.
- **Gestational trophoblastic neoplasm** (98.37%): antimetabolite chemotherapy is established in this disease class, but there is no cladribine-specific evidence.
- **Pleural adenomatoid tumour** (98.07%): a rare benign tumour usually managed surgically, with no plausible mechanistic basis identified.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the lead prediction, currently no related literature available.

The only publication found across the top predictions relates to liver sarcoma and is indirect evidence:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15241520](https://pubmed.ncbi.nlm.nih.gov/15241520/) | 2004 | Case report | Der Hautarzt | Successful cladribine therapy in smouldering systemic mastocytosis, a mast-cell neoplasm rather than liver sarcoma |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11603Q | Mavenclad | Tablet 10 mg | Not stated in the data compiled for this report |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside analogue) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions. Knowledge-graph contraindication links to neutropenia, thrombocytopenia, anaemia and agranulocytosis point to haematological toxicity as a concern |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI; full blood count (with differential), and liver and renal function are generally relevant |
| Handling Protection | Please refer to the PI and local cytotoxic drug handling requirements |

## Safety Considerations

- **Contraindications (knowledge-graph links, not label text)**: kidney disease, pyoureter, thrombocytopenia, neutropenia, agranulocytosis, anaemia (including macrocytic anaemia), peripheral nervous system disease, peripheral neuropathy, and hyperuricaemia.
- **Drug Interactions** (100 interactions recorded; the main ones are listed):
  - **Major**: systemic and other corticosteroids (hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone), deferiprone, and radiopharmaceuticals and radioimmunotherapies (ibritumomab tiuxetan, iobenguane I-131, tositumomab, samarium-153 lexidronam, strontium-89 chloride).
  - **Moderate**: palifermin, dipyridamole, cilostazol, eltrombopag.
  - **Unknown severity**: acetylsalicylic acid.

Please also refer to the TGA-approved Product Information (PI) for full safety information. Label warnings and contraindications were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a high model score with no clinical trials or supporting literature (L5). The clustered rhabdomyosarcoma scores likely reflect ontology structure rather than independent evidence, and there is no established mechanistic rationale for cladribine in solid tumours.

**To proceed, the following is needed:**
- Preclinical data, such as dCK expression and in vitro sensitivity in rhabdomyosarcoma cell lines
- Mechanism of action data to support a mechanistic link
- TGA Product Information warnings and contraindications to allow safety screening
- Review of the haematological toxicity profile against the tolerability expected in a paediatric and young-adult sarcoma population
- Evaluation of route compatibility (only an oral tablet is registered in Australia)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

