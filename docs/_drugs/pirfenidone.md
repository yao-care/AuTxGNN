---
layout: default
title: Pirfenidone
parent: Model Prediction Only (L5)
nav_order: 578
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
monitor_inn: "Pirfenidone"
predicted_indications: ["extracutaneous mastocytoma", "dermatofibrosarcoma protuberans", "aggressive systemic mastocytosis", "heart fibrosarcoma", "conventional fibrosarcoma", "autosomal recessive familial Mediterranean fever", "kidney fibrosarcoma", "hepatic infarction", "fibroblastic neoplasm", "low grade fibromyxoid sarcoma"]
description: "Pirfenidone: predicted new indication Extracutaneous mastocytoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Pirfenidone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Pirfenidone: Extracutaneous mastocytoma
{: .text-alpha }

## One-Sentence Summary

Pirfenidone is an oral antifibrotic originally used to treat idiopathic pulmonary fibrosis and related interstitial pneumonias.
The TxGNN model predicts it may be effective for **extracutaneous mastocytoma** (score 0.9971), but **no clinical trials and no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Extracutaneous mastocytoma |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Pirfenidone is known to be an antifibrotic and anti-inflammatory agent that modulates TGF-β signalling. Its efficacy in idiopathic pulmonary fibrosis is established, but its link to a mast cell neoplasm is not.

Mast cell tumours are generally driven by KIT signalling. No established connection between pirfenidone's pharmacology and this disease was identified, so the high TxGNN score should be treated as a computational hypothesis only.

**Other top-ranked predictions** were also reviewed. All are L5 (prediction only) except fibroblastic neoplasm, which is L4:

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Dermatofibrosarcoma protuberans | 0.9941 | L5 | Loose rationale via fibroblast biology; the PDGFB driver is already targeted by imatinib |
| 3 | Aggressive systemic mastocytosis | 0.9933 | L5 | KIT-driven; no documented link |
| 4 | Heart fibrosarcoma | 0.9929 | L5 | Anti-fibrotic effects are in non-malignant cardiac fibrosis only |
| 5 | Conventional fibrosarcoma | 0.9926 | L5 | Plausible but unsupported |
| 6 | Autosomal recessive familial Mediterranean fever | 0.9925 | L5 | Anti-inflammatory effects are conceptually relevant, but colchicine and IL-1 inhibitors are established |
| 7 | Kidney fibrosarcoma | 0.9924 | L5 | Renal anti-fibrotic data do not extend to malignancy |
| 8 | Hepatic infarction | 0.9924 | L5 | Ischaemic event; no clear link |
| 9 | Fibroblastic neoplasm | 0.9923 | L5 | Preclinical fibroblast data; one safety signal (see below) |
| 10 | Low grade fibromyxoid sarcoma | 0.9919 | L5 | No documented link |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No publications were retrieved for extracutaneous mastocytoma. The only literature identified relates to the rank 9 prediction, fibroblastic neoplasm, and is shown here for context:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12907346](https://pubmed.ncbi.nlm.nih.gov/12907346/) | 2003 | Pilot clinical study | Am J Gastroenterol | Pilot project evaluating pirfenidone for desmoid tumours in familial adenomatous polyposis; outcome details not available in the data compiled |
| [27835939](https://pubmed.ncbi.nlm.nih.gov/27835939/) | 2016 | In vitro | BMC Musculoskelet Disord | Pirfenidone inhibited TGF-β1-mediated activity in Dupuytren's disease-derived fibroblasts |
| [30927912](https://pubmed.ncbi.nlm.nih.gov/30927912/) | 2019 | In vitro | BMC Musculoskelet Disord | Investigated pirfenidone effects on TGF-β1-stimulated non-SMAD signalling in Dupuytren's fibroblasts |
| [35129055](https://pubmed.ncbi.nlm.nih.gov/35129055/) | 2022 | Preclinical | Pharm Dev Technol | Explored pirfenidone as a locally injectable antifibrotic for Dupuytren's disease |
| [29702057](https://pubmed.ncbi.nlm.nih.gov/29702057/) | 2018 | Case report | Perm J | Undifferentiated pleomorphic sarcoma reported after pirfenidone use (safety signal) |
| [32572469](https://pubmed.ncbi.nlm.nih.gov/32572469/) | 2020 | Case report | Rheumatology (Oxford) | Multiple eruptive dermatofibromas aggravated by mycophenolate mofetil and pirfenidone in a patient with systemic sclerosis |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11406H | Pirfenidone Sandoz | Tablet 267 mg (oral) | Not available in the data compiled |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in total. The 20 listed in the data compiled are all rated Moderate. They include bupropion, omeprazole, esomeprazole, lansoprazole, cimetidine, eliglustat, obeticholic acid, oxandrolone, naltrexone, miconazole, nitisinone, glycerol phenylbutyrate, rolapitant, deferasirox, ticlopidine, lumefantrine, disulfiram, primaquine, thiabendazole and ivacaftor.
- **Emerging signal**: Published case reports describe a sarcoma and eruptive dermatofibromas arising or worsening during pirfenidone use. These are low-level evidence, but they run counter to a therapeutic hypothesis in fibroblastic tumours.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications, as these were not available in the data compiled.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). There are no trials or publications for extracutaneous mastocytoma, and no biological link to pirfenidone's antifibrotic mechanism has been documented. Mast cell neoplasms are KIT-driven, and this prediction is not a sensible candidate for repurposing without further support.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) to allow a proper mechanistic cross-check
- The TGA Product Information, including approved indication, warnings and contraindications
- Preclinical evidence (for example mast cell line or KIT-driven models) showing a plausible effect
- Review of the sarcoma and dermatofibroma case reports before any fibroblastic-tumour hypothesis is pursued
- Consideration of fibroblastic neoplasm (L4) as a research question only, given its preclinical support but conflicting safety signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

