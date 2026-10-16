---
layout: default
title: Eribulin
parent: Model Prediction Only (L5)
nav_order: 264
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Eribulin: predicted new indication Autosomal recessive familial Mediterranean fever (evidence level L5). Approved use: Liposarcoma"
---

# Eribulin
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

# Eribulin: From Liposarcoma to Autosomal Recessive Familial Mediterranean Fever

## One-Sentence Summary

Eribulin is a microtubule dynamics inhibitor, originally used to treat advanced liposarcoma.
The TxGNN model's top-ranked prediction is **autosomal recessive familial Mediterranean fever**, but this has **no clinical trials and no publications** supporting it, so it rests on the model score alone.
The best-supported prediction in the data compiled for this report is **fibroblastic neoplasm** (rank 8), with **1 completed Phase 2 trial** and **8 publications** (mostly preclinical or review).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Liposarcoma (from the knowledge graph; no approved indication text is recorded in the ARTG data) |
| Predicted New Indication | Autosomal recessive familial Mediterranean fever (rank 1) |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

> **Note:** The rank 1 prediction has no supporting studies. Among the ten predictions, fibroblastic neoplasm (score 99.36%) has the strongest evidence (L2, a completed Phase 2 trial) and is the most useful direction to pursue. It is summarised in the sections below.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, eribulin is a microtubule dynamics inhibitor and a cytotoxic oncology drug. Its efficacy in liposarcoma is established, and mechanistically it may be applicable to other soft tissue sarcomas.

**Familial Mediterranean fever (FMF, rank 1).** No mechanistic link is supported by the data. FMF is an autoinflammatory disease driven by pyrin inflammasome dysregulation. Colchicine, another microtubule-targeting agent, is standard FMF therapy, which gives only a loose class-level rationale. Eribulin's cytotoxic toxicity profile is very different, so the high score (0.998) should be treated as a computational signal only.

**Other predictions:**
- **Fibroblastic neoplasm (rank 8):** Soft tissue sarcomas are biologically adjacent to liposarcoma. A completed Phase 2 trial in solitary fibrous tumour and preclinical fibrosarcoma data provide supportive context.
- **Dermatofibrosarcoma protuberans (rank 2):** Plausible as a soft tissue sarcoma, but it is driven by the COL1A1-PDGFB fusion and is usually managed with surgery and imatinib. The only literature is a general review.
- **Ovarian myxoid liposarcoma (rank 5):** A liposarcoma subtype, so extrapolation from the approved indication is reasonable, but there is no site-specific evidence.
- **Mesotheliomas (pleural, peritoneal, biphasic, epithelioid) and cardiac fibrosarcoma:** Plausible antimitotic rationale, but prediction only.
- **Pleural adenomatoid tumour (rank 6):** Generally a benign tumour treated surgically, and likely a spurious association.

## Clinical Trial Evidence

No trials are registered for the rank 1 indication (familial Mediterranean fever). The only trial in the top ten predictions is for **fibroblastic neoplasm** (rank 8):

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03840772](https://clinicaltrials.gov/study/NCT03840772) | Phase 2 | Completed | 16 | ERASING study: eribulin in advanced solitary fibrous tumour (Italian Sarcoma Group). No outcome data were available, so efficacy is unknown. |

## Literature Evidence

No literature is available for the rank 1 indication. The following publications relate to **fibroblastic neoplasm** (rank 8). Soft tissue sarcoma chemotherapy review (PMID 27434055) relates to dermatofibrosarcoma protuberans (rank 2) and is listed last.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38136399](https://pubmed.ncbi.nlm.nih.gov/38136399/) | 2023 | Review | Cancers | Diagnosis and treatment of extrameningeal solitary fibrous tumours, a rare mesenchymal neoplasm. |
| [28284173](https://pubmed.ncbi.nlm.nih.gov/28284173/) | 2017 | Preclinical (xenograft) | Eur J Cancer | Patient-derived solitary fibrous tumour xenografts showed high sensitivity to doxorubicin/dacarbazine and suggested potential effectiveness of trabectedin or eribulin. |
| [38423656](https://pubmed.ncbi.nlm.nih.gov/38423656/) | 2024 | Preclinical (in vitro) | Anticancer Res | Recombinant methioninase and eribulin showed synergy against fibrosarcoma cells but not normal fibroblasts. |
| [39197933](https://pubmed.ncbi.nlm.nih.gov/39197933/) | 2024 | Preclinical (in vitro) | Anticancer Res | Recombinant methioninase increased eribulin efficacy 16-fold in highly eribulin-resistant fibrosarcoma cells. |
| [40295012](https://pubmed.ncbi.nlm.nih.gov/40295012/) | 2025 | Preclinical (in vitro/in vivo) | In Vivo | Eribulin-resistant fibrosarcoma cells became more malignant but were arrested by combining eribulin with methionine restriction in nude mice. |
| [35906852](https://pubmed.ncbi.nlm.nih.gov/35906852/) | 2023 | Case report | Genes Chromosomes Cancer | Response to entrectinib in an NTRK3-fusion peripheral nerve sheath tumour; limited relevance to eribulin. |
| [39625530](https://pubmed.ncbi.nlm.nih.gov/39625530/) | 2024 | Preclinical (cell line) | Human Cell | Establishment of a myxofibrosarcoma cell line; no direct eribulin evidence. |
| [34383271](https://pubmed.ncbi.nlm.nih.gov/34383271/) | 2021 | Preclinical (cell line) | Human Cell | Establishment of another myxofibrosarcoma cell line; no direct eribulin evidence. |
| [27434055](https://pubmed.ncbi.nlm.nih.gov/27434055/) | 2016 | Review | Cancer | General review of soft tissue sarcoma chemotherapy (dermatofibrosarcoma protuberans, rank 2); indirect support only. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10140Q | Halaven | Solution for I.V. injection containing eribulin mesilate 1 mg in 2 mL | Not recorded in the data compiled for this report |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (microtubule dynamics inhibitor) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions. The knowledge graph lists neutropenia, agranulocytosis and thrombocytopenia as contraindication-related conditions. |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Full blood count (with differential), electrolytes (including potassium), ECG for QT prolongation, and neurological assessment for peripheral neuropathy |
| Handling Protection | Follow cytotoxic drug handling requirements |

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text):** long QT syndrome (including familial), thrombocytopenia, potassium deficiency, neutropenia, agranulocytosis, peripheral nervous system disease, peripheral neuropathy and constipation disorder.
- **Drug Interactions:** 100 interactions were identified. Examples shown include:
  - **Major:** dolasetron and cisapride (consistent with QT-prolongation concerns).
  - **Moderate:** clarithromycin, levofloxacin, ondansetron, palonosetron, metronidazole, tinidazole, famotidine, loperamide, simvastatin, rosuvastatin, and several laxatives and bowel-preparation products (bisacodyl, lactulose, lactitol, polyethylene glycol, sodium sulfate, picosulfuric acid, castor oil).

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (familial Mediterranean fever) has no trials or literature, and its mechanistic rationale is weak, so it cannot be supported beyond the model score. The strongest signal is fibroblastic neoplasm (completed Phase 2 trial in solitary fibrous tumour, n=16, no results available), which warrants further investigation as a research question rather than a treatment recommendation.

**To proceed, the following is needed:**
- Published results from the ERASING trial (NCT03840772), including response rate and survival outcomes
- Mechanism of action data (MOA) from DrugBank
- TGA Product Information with approved indication, warnings and contraindications, which is currently missing
- Disease-specific evidence for any other predicted indication before it is considered
- A safety plan covering QT prolongation, myelosuppression, peripheral neuropathy and the interactions listed above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

