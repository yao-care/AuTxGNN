---
layout: default
title: Topotecan
parent: 僅模型預測 (L5)
nav_order: 687
evidence_level: L5
indication_count: 10
---

# Topotecan
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

# Topotecan: From Ovarian Cancer / Small Cell Lung Cancer to Female Breast Carcinoma

## One-Sentence Summary

Topotecan is a camptothecin-derived topoisomerase I inhibitor used internationally as a cytotoxic chemotherapy agent, most established for platinum-refractory ovarian cancer and relapsed small cell lung cancer (per literature within this evidence pack); a structured original-indication record was not available in the regulatory dataset. The TxGNN model predicts it may also be effective for **Female Breast Carcinoma**, with **5 clinical trials** and **20 publications** currently associated with this direction — though several older trials specifically testing topotecan in breast cancer reported limited efficacy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in structured regulatory data; literature evidence in this pack describes topotecan as an established second-line therapy for small cell lung cancer and platinum-refractory ovarian cancer |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap DG002). Based on known pharmacology referenced in the evidence pack, topotecan is a semisynthetic camptothecin analogue that inhibits topoisomerase I, preventing DNA religation after single-strand breaks. This produces double-strand breaks during DNA replication, triggering apoptosis in rapidly dividing cells — a mechanism broadly applicable across many solid tumour types.

Breast carcinoma, like the tumour types topotecan is already used against, is a rapidly proliferating solid tumour, which provides a plausible mechanistic rationale for cross-indication activity. Indeed, this hypothesis has already been tested clinically: multiple Phase II trials in the 1990s–2000s (CALGB, infusional dosing studies, paclitaxel combinations) evaluated topotecan specifically in advanced/metastatic breast cancer.

However, the historical clinical evidence is mixed rather than confirmatory — one Phase II trial explicitly concluded "no evidence of increased efficacy" (PMID 9413954), and topotecan has never progressed to a registered breast cancer indication despite decades of investigation. More recent mechanistic work (e.g. TFDP1 as a target in triple-negative breast cancer, MYC-driven synthetic lethality via R-loop accumulation) has renewed interest, particularly in molecularly-defined subgroups such as TNBC, but this remains largely preclinical.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | Terminated | N/A | TIME regimen (topotecan + ifosfamide/mesna + etoposide) with autologous stem cell rescue in metastatic breast cancer; topotecan a direct study drug, but trial terminated without positive readout |
| [NCT02282020](https://clinicaltrials.gov/study/NCT02282020) | Phase 3 | Completed | 266 | Olaparib vs. physician's choice chemotherapy in gBRCA-mutated ovarian cancer; captured via disease co-occurrence only, no confirmed direct topotecan arm |
| [NCT04739800](https://clinicaltrials.gov/study/NCT04739800) | Phase 2 | Active, not recruiting | 120 | Durvalumab + olaparib + cediranib combinations in platinum-resistant ovarian/peritoneal/fallopian cancer; topotecan's role in the regimen not confirmed |
| [NCT04279509](https://clinicaltrials.gov/study/NCT04279509) | N/A | Unknown | 35 | Organoid-based high-throughput drug-screen assay for refractory solid tumours; translational/preclinical signal only, not a therapeutic trial |
| [NCT02419495](https://clinicaltrials.gov/study/NCT02419495) | Phase 1 | Terminated | 221 | Selinexor combined with multiple standard chemo/immunotherapy regimens in advanced malignancies; topotecan's specific involvement in this arm unconfirmed |

*Note: Most trials above were retrieved via disease co-occurrence rather than confirmed direct evaluation of topotecan in breast cancer; only NCT00006032 has a directly documented topotecan-containing regimen for this indication.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9413954](https://pubmed.ncbi.nlm.nih.gov/9413954/) | 1997 | Phase II (single-arm) | British Journal of Cancer | Infusional topotecan in advanced breast cancer/NSCLC; concluded no evidence of increased efficacy |
| [10362325](https://pubmed.ncbi.nlm.nih.gov/10362325/) | 1999 | Phase II (single-arm, CALGB) | American Journal of Clinical Oncology | Topotecan monotherapy in previously-treated advanced breast cancer; modest antitumour activity observed |
| [9626200](https://pubmed.ncbi.nlm.nih.gov/9626200/) | 1998 | Phase II | Journal of Clinical Oncology | Paclitaxel + topotecan + G-CSF in stage IV breast cancer; evaluated efficacy, safety, and pharmacokinetic interactions |
| [11455218](https://pubmed.ncbi.nlm.nih.gov/11455218/) | 2001 | Pilot study | Onkologie | Topotecan as primary chemotherapy for breast cancer brain metastases |
| [40300683](https://pubmed.ncbi.nlm.nih.gov/40300683/) | 2025 | Mechanistic study | International Journal of Biological Macromolecules | Identifies TFDP1 as a therapeutic target for topotecan in triple-negative breast cancer |
| [26623560](https://pubmed.ncbi.nlm.nih.gov/26623560/) | 2015 | Preclinical (in vivo) | Oncotarget | Metronomic topotecan + pazopanib shows potent efficacy in preclinical TNBC models |
| [9445630](https://pubmed.ncbi.nlm.nih.gov/9445630/) | 1997 | Review | Gynäkologisch-geburtshilfliche Rundschau | Reviews new cytotoxic agents, including topotecan, in the breast cancer treatment landscape |
| [37987734](https://pubmed.ncbi.nlm.nih.gov/37987734/) | 2023 | Mechanistic study | Cancer Research | Topoisomerase I inhibition in MYC-driven cancer promotes R-loop-mediated synthetic lethality |
| [27444351](https://pubmed.ncbi.nlm.nih.gov/27444351/) | 2016 | Mechanistic study | Phytomedicine | Natural compound MHP-1 restores topotecan sensitivity via EMT/TGF-β regulation in breast cancer cells |
| [15836850](https://pubmed.ncbi.nlm.nih.gov/15836850/) | 2005 | In vitro mechanistic | Journal of Surgical Research | Quercetin modulates topotecan cytotoxicity via oxidative stress in MCF-7/MDA-MB-231 cell lines |

---

## Australia Market Information

Topotecan is currently **not registered on the Australian Register of Therapeutic Goods (ARTG)** — market status "Not Marketed", 0 ARTG entries recorded in this evidence pack. No product listing or TGA-approved indication text is available for extraction.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (topoisomerase I inhibitor, camptothecin class) |
| Myelosuppression Risk | High — literature in this pack documents dose-limiting neutropenia and thrombocytopenia (e.g. PMID 8617580: median nadir neutrophil count 1.55 × 10⁹/L, platelets 20,500/mm³) |
| Emetogenicity Classification | Low to moderate (typical for this drug class; TGA-specific PI data not available — please confirm against Product Information) |
| Monitoring Items | Full blood count with differential, renal function (topotecan is renally cleared), liver function |
| Handling Protection | Requires standard cytotoxic drug handling precautions (closed-system transfer, PPE) as with other IV antineoplastic agents |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Key warnings, contraindications and drug interaction data were not available in this evidence pack (data gap DG001 — blocking).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A blocking data gap exists for TGA/product-label safety information (DG001), and the mechanism of action record is also incomplete (DG002). Topotecan is not currently registered in Australia, and historical Phase II evidence specifically in breast cancer has been inconsistent — several trials reported no clear efficacy advantage despite decades of investigation, even though newer mechanistic work (e.g. TFDP1/TNBC) suggests a possible molecularly-defined subgroup worth re-examining.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications, drug interactions) to resolve DG001
- Confirmed mechanism of action documentation to resolve DG002
- Clarification of ARTG/import pathway status, given the drug is not currently marketed in Australia
- Updated, subtype-stratified clinical evidence (e.g. TNBC) given that historical unselected-population trials showed limited benefit
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

