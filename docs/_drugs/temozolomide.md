---
layout: default
title: Temozolomide
parent: Model Prediction Only (L5)
nav_order: 705
evidence_level: L5
indication_count: 1
monitor_inn: "Temozolomide"
predicted_indications: ["cauda equina neoplasm"]
last_modified_at: 2026-11-17
description: "Temozolomide: predicted new indication Cauda equina neoplasm (evidence level L5). Approved use: Anaplastic astrocytoma…"
---

# Temozolomide
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

## Temozolomide: From Glioma (Astrocytoma and Glioblastoma) to Cauda Equina Neoplasm
{: .text-alpha }

## One-Sentence Summary

Temozolomide is an oral alkylating chemotherapy drug. The knowledge graph records it for anaplastic astrocytoma, astrocytoma (excluding glioblastoma) and brain glioblastoma.
The TxGNN model predicts it may be useful for **cauda equina neoplasm**, but there are **no registered clinical trials** and only **3 publications** (all case reports, with just one directly relevant), so the evidence is very limited.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anaplastic astrocytoma, astrocytoma (excluding glioblastoma) and brain glioblastoma (relations recorded in the knowledge graph; the Australian licence record contains no approved indication text) |
| Predicted New Indication | Cauda equina neoplasm |
| TxGNN Prediction Score | 0.9930 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (11 of 11 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 11 (valid: 11) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for temozolomide: "Temozolomide is not directly active but undergoes rapid nonenzymatic conversion at physiologic pH to the reactive compound 5-(3-methyltriazen-1-yl)-imidazole-4-carboxamide (MTIC). The cytotoxicity of MTIC is thought to be primarily due to DNA alkylation, mainly at the O 6 and N 7 positions of guanine, which causes DNA double strand breaks and results in programmed cell death." ([DailyMed: Temodar (temozolomide) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=046a9011-3911-4d3f-a15f-fbb56d5aad56), label version 2026-02-20; accessed 2026-11-19.) In general, temozolomide is an oral alkylating agent that methylates DNA (notably at O6-guanine), causing cytotoxic lesions and cell death. It is generally more active in tumours with low MGMT expression (for example, MGMT promoter methylation). This description comes from general pharmacological knowledge, not from the supplied record.

The TxGNN model (deep learning) gives cauda equina neoplasm a score of 0.9930. This score comes from the model and may reflect similarities the model learned between related diseases, not biological evidence.

The TxGNN score is a computational prediction only and does not replace clinical evidence. No MGMT status data for these tumours were available.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29270703](https://pubmed.ncbi.nlm.nih.gov/29270703/) | 2018 | Case report | Eur Spine J | Temozolomide showed remarkable efficacy in a relapsed spinal myxopapillary ependymoma with multiple recurrences and cerebrospinal dissemination |
| [42760727](https://pubmed.ncbi.nlm.nih.gov/42760727/) | 2026 | Case report | Medicine | Nasal NUT carcinoma managed with multimodal treatment including radiotherapy; not specific to cauda equina tumours |
| [18706663](https://pubmed.ncbi.nlm.nih.gov/18706663/) | 2009 | Case report | Neuro-Chirurgie | Neuromeningeal cryptococcosis in a child treated for pontine glioma; not relevant to cauda equina tumours |

Note: The first case report concerns a spinal myxopapillary ependymoma, a tumour type that arises in the cauda equina region. It is a single case and does not directly study cauda equina neoplasm as a defined disease. The other two reports do not address this condition. For this reason the evidence level is capped at L5.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10062N | APO-Temozolomide | Capsule 180 mg | Not stated in the licence record |

The table lists one of 11 valid single-ingredient oral PBS items in the data compiled for this report (APO-Temozolomide and Temizole capsules, 5 mg to 250 mg).

<!-- review:begin au-lic-20261117-temozolomide-1 -->

> **Review correction (2026-11-17)**: Originally stated: "The listing is a single-ingredient oral product (1 valid entry)." Corrected: the earlier wording counted only the PBS items originally collected for this page. The data now include the current PBS items for this ingredient (PBS public data API, Schedule effective 2026-11-01). PBS listing does not show TGA (ARTG) registration status. Source: [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/).

<!-- review:end au-lic-20261117-temozolomide-1 -->

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions. The knowledge graph lists blood-related conditions among its contraindication relations (see below). |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Haematological parameters (FBC with differential), liver function; confirm details in the PI |
| Handling Protection | Follow local cytotoxic drug handling requirements |

## Safety Considerations

- **Contraindication relations recorded in the knowledge graph** (not label text): liver failure, thrombocytopenia, neutropenia, agranulocytosis, anaemia, macrocytic anaemia, pneumocystosis, pancytopenia, lymphopenia, myelodysplastic syndrome, idiopathic aplastic anaemia and aplastic anaemia.
- **Drug Interactions**: 100 interactions were found in the DDI database. The ones listed are mostly of unknown severity. The graded ones are naltrexone (Moderate) and levofloxacin (Minor). Others listed include pantoprazole, omeprazole, lansoprazole, metformin, morphine, prednisone, hydrocortisone and amphotericin B.

Please refer to the TGA-approved Product Information (PI) for authoritative warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a computational score and a single case report in a related tumour type. There are no registered trials, and no cited study directly addresses cauda equina neoplasm as a disease, so the evidence level is L5. The safety profile also cannot be assessed here because label warnings are unavailable.

**To proceed, the following is needed:**
- Review of the TGA Product Information for warnings, contraindications and approved indications
- Mechanism of action data and, ideally, MGMT status data for cauda equina tumours
- Systematic literature review or case series of temozolomide in myxopapillary ependymoma and other cauda equina tumours
- A defined plan for blood count monitoring and for cytotoxic drug handling
- Registration of a prospective study or an expert-panel review before any clinical consideration

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Australian data (the PBS Schedule of the Department of Health and Aged Care, and the TGA's ARTG). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-17 | Corrected: PBS item count updated to the current PBS Schedule | Corrected | [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Temodar (temozolomide) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=046a9011-3911-4d3f-a15f-fbb56d5aad56) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

