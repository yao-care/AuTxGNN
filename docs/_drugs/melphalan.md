---
layout: default
title: Melphalan
parent: 僅模型預測 (L5)
nav_order: 424
evidence_level: L5
indication_count: 10
---

# Melphalan
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

# Melphalan: From Multiple Myeloma to Gonadal Germ Cell Tumor

## One-Sentence Summary

Melphalan is a nitrogen mustard alkylating agent internationally established for multiple myeloma (and, in some jurisdictions, ovarian cancer). The TxGNN model predicts it may be effective for **Gonadal Germ Cell Tumor**, with **8 clinical trials** and **4 publications** currently supporting this direction — though only one trial and no publications are disease-specific.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple myeloma (established international indication; no ARTG-approved indication text is available — Melphalan is not currently marketed in Australia) |
| Predicted New Indication | Gonadal Germ Cell Tumor |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (data gap DG002). Based on known pharmacology, Melphalan is a bifunctional alkylating agent (nitrogen mustard derivative) that forms DNA interstrand crosslinks, producing cytotoxicity that is most pronounced in rapidly dividing cells — a property shared by germ cell tumours, which are among the most chemosensitive solid tumours known.

Melphalan already has an established role in high-dose chemotherapy conditioning regimens combined with autologous stem cell transplantation (ASCT), including as salvage therapy for relapsed, poor-prognosis germ-cell tumours. This gives the TxGNN prediction a direct clinical precedent rather than a purely computational association: the mechanistic rationale (alkylator activity against a highly chemosensitive tumour type) aligns with real-world high-dose chemotherapy practice.

The strongest supporting evidence is a Phase 2 trial (NCT00936936, n=64) studying high-dose chemotherapy — including melphalan — specifically for poor-prognosis relapsed germ-cell tumours. Most of the remaining trials are non-disease-specific ASCT-conditioning studies that include germ-cell tumour patients as part of a broader solid-tumour population, which supports feasibility and safety of the regimen but not disease-specific efficacy on its own.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00936936](https://clinicaltrials.gov/study/NCT00936936) | Phase 2 | Completed | 64 | Two cycles of high-dose chemotherapy (including melphalan) specifically for poor-prognosis relapsed germ-cell tumours — the only disease-specific trial in this set |
| [NCT00003425](https://clinicaltrials.gov/study/NCT00003425) | Phase 1/2 | Completed | 25 | Escalating-dose melphalan with autologous stem cell support and amifostine cytoprotection in cancer patients (not disease-specific) |
| [NCT00003926](https://clinicaltrials.gov/study/NCT00003926) | Phase 1 | Terminated | 13 | Amifostine cytoprotection with autologous stem cell transplant for high-risk/relapsed paediatric solid and brain tumours |
| [NCT00638898](https://clinicaltrials.gov/study/NCT00638898) | Phase 1 | Completed | 25 | High-dose busulfan, melphalan and topotecan followed by autologous HSCT in advanced/recurrent tumours (not disease-specific) |
| [NCT00536601](https://clinicaltrials.gov/study/NCT00536601) | N/A | Completed | 174 | Pilot study of high-dose chemotherapy regimens ± total-body irradiation before autologous transplant, across haematologic malignancies and selected solid tumours |
| [NCT00060255](https://clinicaltrials.gov/study/NCT00060255) | Phase 2 | Completed | 451 | Eight high-dose chemotherapy regimens ± total-body irradiation before autologous transplant, across haematologic malignancy and selected solid tumours |
| [NCT01272817](https://clinicaltrials.gov/study/NCT01272817) | N/A | Completed | 36 | Nonmyeloablative allogeneic HSCT using melphalan and cladribine (or total lymphoid irradiation) conditioning, across various haematologic conditions |
| [NCT00002750](https://clinicaltrials.gov/study/NCT00002750) | Phase 1 | Completed | 6 | Intrathecal melphalan for recurrent neoplastic meningitis — different route and indication to systemic use in germ-cell tumours |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [13392619](https://pubmed.ncbi.nlm.nih.gov/13392619/) | 1956 | Cohort | Voprosy onkologii | Early clinical experience treating testicular seminoma and its metastases with sarcolysin (melphalan's original name) |
| [4270380](https://pubmed.ncbi.nlm.nih.gov/4270380/) | 1973 | Review | Oncology | Review of chemotherapy approaches for testicular germinal tumours |
| [24913](https://pubmed.ncbi.nlm.nih.gov/24913/) | 1977 | Review | The Urologic Clinics of North America | General review of seminoma management |
| [14151951](https://pubmed.ncbi.nlm.nih.gov/14151951/) | 1964 | Cohort | Acta – Unio Internationalis Contra Cancrum | Effect of hormonal and alkylating drugs on pituitary FSH-stimulating function |

## Australia Market Information

No ARTG entries are currently registered — Melphalan is not marketed in Australia (total ARTG licences: 0).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, nitrogen mustard class) |
| Myelosuppression Risk | High — dose-limiting toxicity; established use in myeloablative high-dose regimens requiring autologous stem cell rescue, as seen throughout the trial evidence above |
| Emetogenicity Classification | Moderate to high (particularly with IV high-dose regimens used in ASCT conditioning) |
| Monitoring Items | Full blood count with differential, renal function, hepatic function, mucositis assessment |
| Handling Protection | Standard cytotoxic drug handling precautions apply (PPE, closed-system transfer devices where available) |

*Specific toxicity grading is not confirmed by product-level data in this pack — please refer to the Product Information (PI) warnings and precautions once available.*

## Safety Considerations

Please refer to the approved Product Information (PI) for safety information. Key warnings, contraindications and drug-drug interaction data were not available in this evidence pack (DG001, blocking severity), and Melphalan currently has no ARTG-registered PI in Australia.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One disease-specific Phase 2 trial (NCT00936936, n=64) supports high-dose melphalan-containing chemotherapy in poor-prognosis relapsed germ-cell tumours, and the mechanistic rationale (alkylator activity against a highly chemosensitive tumour) is sound. However, most remaining trials are non-disease-specific ASCT-conditioning studies, and product-level safety/MOA data is missing.

**To proceed, the following is needed:**
- Product Information / regulatory safety data (warnings, contraindications) — currently a blocking data gap (DG001)
- Confirmed mechanism-of-action documentation (DG002)
- Drug-drug interaction data (currently not found)
- Clarification of the ARTG registration pathway, given Melphalan is not currently marketed in Australia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

