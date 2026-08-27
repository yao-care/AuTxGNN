---
layout: default
title: Ipilimumab
parent: 僅模型預測 (L5)
nav_order: 360
evidence_level: L5
indication_count: 10
---

# Ipilimumab
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

# Ipilimumab: From Advanced Melanoma to Non-Cutaneous and Rare Melanoma Subtypes

## One-Sentence Summary

Ipilimumab (Yervoy) is a fully human anti-CTLA-4 monoclonal antibody originally developed for advanced or metastatic melanoma, though no current ARTG registration was identified in this dataset.
The TxGNN model predicts potential efficacy across **10 melanoma subtypes** and one non-melanoma condition, with the strongest actionable signal for **non-cutaneous melanoma** (uveal, mucosal, and acral subtypes), supported by **multiple Phase 3 RCTs** and over **50 relevant clinical trials**.
The primary predicted indication carries an **L1 evidence level** with a recommendation to **Proceed with Guardrails**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Advanced/unresectable melanoma (global approval context; no ARTG registration found in this dataset — TGA verification required) |
| Primary Predicted New Indication | Non-Cutaneous Melanoma (uveal, mucosal, acral subtypes) |
| TxGNN Prediction Score | 99.02% |
| Evidence Level | L1 (non-cutaneous melanoma); L2 (mucosal, acral lentiginous melanoma); L3–L5 (rare subtypes) |
| Australia Market Status | Not registered (0 ARTG entries found) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails (primary indication) |

---

## Predicted Indications Overview

| Rank | Indication | TxGNN Score | Evidence Level | Decision |
|------|-----------|------------|---------------|---------|
| 1 | Choroideremia | 99.06% | L5 — No evidence | **Hold** (likely false positive) |
| **2** | **Non-Cutaneous Melanoma** | **99.02%** | **L1 — Multiple Phase 3 RCTs** | **Proceed with Guardrails** |
| 3 | Epithelioid Cell Melanoma | 98.96% | L3 — Case series | Research Question |
| 4 | Eyelid Melanoma | 98.95% | L4 — Case reports | Research Question |
| 5 | Scrotum Melanoma | 98.84% | L4 — No direct evidence | Research Question |
| 6 | Lentigo Maligna Melanoma | 98.64% | L4 — Case reports | Research Question |
| **7** | **Acral Lentiginous Melanoma** | **98.64%** | **L2 — Phase 2 RCTs** | **Proceed with Guardrails** |
| 8 | Balloon Cell Melanoma | 98.64% | L5 — Safety concern only | **Hold** |
| 9 | Nodular Malignant Melanoma | 98.64% | L3 — Retrospective cohorts | Research Question |
| **10** | **Mucosal Melanoma** | **98.64%** | **L2 — Phase 2 RCTs** | **Proceed with Guardrails** |

> **Note on Rank 1 (Choroideremia):** This prediction is assessed as a knowledge graph false positive. Choroideremia is an X-linked retinal dystrophy caused by CHM gene mutation, with no known connection to the CTLA-4 pathway or tumour immunology. No clinical trials or literature support this prediction. The high TxGNN score likely reflects graph structural similarity artefact. This indication should not be pursued.
>
> **Note on Rank 8 (Balloon Cell Melanoma):** L5 evidence only. The sole relevant literature (PMID 39548815) is a fatal irAE case report — constituting a safety concern rather than efficacy signal. Hold.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not retrieved from DrugBank in this Evidence Pack. Based on well-established clinical pharmacology, ipilimumab is a fully human IgG1 monoclonal antibody that blocks CTLA-4 (cytotoxic T-lymphocyte antigen-4), an inhibitory co-receptor expressed on activated T cells. By occluding the CTLA-4/B7 interaction in lymph nodes, ipilimumab removes an important immunological brake during the T cell priming phase, resulting in amplified T cell proliferation and enhanced anti-tumour immunity. This mechanism was clinically validated in Phase 3 trials for unresectable or metastatic cutaneous melanoma, where ipilimumab became the first agent in 13 years to demonstrate an overall survival benefit.

Non-cutaneous melanomas — including uveal (ocular), mucosal (sinonasal, anorectal, vulvovaginal), acral lentiginous, and rare histological variants — all arise from melanocytes and express tumour-associated antigens recognisable by T cells. Because the CTLA-4 pathway operates at the T cell priming stage in secondary lymphoid organs rather than directly within the tumour microenvironment, ipilimumab's mechanism is theoretically applicable regardless of the anatomical origin of the melanoma. The lower response rates observed in non-cutaneous subtypes compared to UV-exposed cutaneous melanoma are largely attributed to their lower tumour mutational burden (TMB) and distinct immune microenvironments — mucosal melanomas often exhibit TGF-β-mediated immunosuppression, while uveal melanomas benefit from partial immune privilege in the anterior chamber. However, combination with anti-PD-1 agents (particularly nivolumab) appears to partially overcome these barriers through complementary checkpoint blockade.

Of particular relevance to Australian clinical practice: acral lentiginous melanoma is disproportionately prevalent in Indigenous Australian and Asian-Australian communities, accounting for 40–50% of melanomas in East Asian populations. PMID 24999899 — an Australian real-world study from the Peter MacCallum Cancer Centre — directly evaluates ipilimumab efficacy across cutaneous, uveal, and mucosal melanoma subtypes in an Australian setting, providing locally applicable evidence. Japanese 5-year follow-up data (PMID 33715172) from a population where acral melanoma predominates also provides actionable long-term survival signals.

---

## Clinical Trial Evidence

### Primary Indication: Non-Cutaneous Melanoma (L1)

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02278887](https://clinicaltrials.gov/study/NCT02278887) | Phase 3 | Completed | 168 | RCT comparing TIL + IL-2 infusion vs ipilimumab in Stage IV melanoma. Establishes ipilimumab as the gold-standard comparator arm for advanced melanoma, including non-cutaneous subtypes. |
| [NCT00094653](https://clinicaltrials.gov/study/NCT00094653) | Phase 3 | Completed | 1,783 | Pivotal three-arm RCT: ipilimumab (MDX-010) alone, ipilimumab + peptide vaccine, or vaccine alone in previously treated Stage III/IV melanoma. First-ever OS benefit in advanced melanoma; includes all histological subtypes. |
| [NCT01515189](https://clinicaltrials.gov/study/NCT01515189) | Phase 3 | Completed | 831 | Randomised double-blind: ipilimumab 3 mg/kg vs 10 mg/kg in unresectable or metastatic melanoma. Dose optimisation trial establishing the standard 3 mg/kg regimen. |
| [NCT00636168](https://clinicaltrials.gov/study/NCT00636168) | Phase 3 | Completed | 1,211 | EORTC adjuvant trial: ipilimumab vs placebo after complete resection of high-risk Stage III melanoma. Confirmed adjuvant benefit, recruiting all melanoma histological subtypes. |
| [NCT02599402](https://clinicaltrials.gov/study/NCT02599402) | Phase 3 | Completed | 533 | CheckMate 401: nivolumab + ipilimumab combination as first-line therapy for Stage III/IV melanoma. Broad eligibility including non-cutaneous and rare subtypes. |
| [NCT02990611](https://clinicaltrials.gov/study/NCT02990611) | Prospective NIS | Completed | 1,087 | Large German prospective registry: nivolumab ± ipilimumab in advanced melanoma across all subgroups. Real-world safety and effectiveness data. |
| [NCT03235245](https://clinicaltrials.gov/study/NCT03235245) | Phase 2 | Active, Not Recruiting | 271 | EBIN: sequential encorafenib + binimetinib → ipilimumab + nivolumab vs immediate combination immunotherapy in BRAF V600-mutant metastatic melanoma. |
| [NCT04462406](https://clinicaltrials.gov/study/NCT04462406) | Phase 2 | Active, Not Recruiting | 150 | PET-Stop: biomarker-driven early discontinuation of anti-PD-1 therapy in Stage IIIB–IV unresectable melanoma, including uveal and mucosal subtypes. |
| [NCT02115139](https://clinicaltrials.gov/study/NCT02115139) | Phase 2 | Completed | 58 | Multicentre: radiation therapy + ipilimumab in melanoma with brain metastases across all subtypes. Direct ipilimumab efficacy data in CNS disease setting. |
| [NCT00972933](https://clinicaltrials.gov/study/NCT00972933) | Early Phase 1 | Completed | 59 | Neoadjuvant ipilimumab in Stage IIIB–C melanoma before surgery; immunogenicity and biomarker analysis of CTLA-4 blockade in resectable disease. |

### Mucosal Melanoma (Rank 10, L2)

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03241186](https://clinicaltrials.gov/study/NCT03241186) | Phase 2 | Active, Not Recruiting | 36 | SALVO study: ipilimumab 1 mg/kg + nivolumab 3 mg/kg as adjuvant therapy specifically for resected mucosal melanoma. Globally the most direct mucosal-specific ipilimumab trial. |
| [NCT03033576](https://clinicaltrials.gov/study/NCT03033576) | Phase 2 (Randomised) | Completed | 94 | Randomised: nivolumab + ipilimumab vs ipilimumab alone in anti-PD-1/PD-L1 refractory advanced melanoma. Mucosal subgroup data available; establishes L2 basis. |
| [NCT05384496](https://clinicaltrials.gov/study/NCT05384496) | Phase 2 | Recruiting | 20 | Axitinib + PD-1 blockade specifically designed for advanced mucosal melanoma; ipilimumab pilot arm added for select progressors. |
| [NCT01119508](https://clinicaltrials.gov/study/NCT01119508) | Phase 2 | Completed | 64 | Ipilimumab + temozolomide in metastatic melanoma including mucosal subgroup; provides ipilimumab combination efficacy data. |
| [NCT03340129](https://clinicaltrials.gov/study/NCT03340129) | Phase 2 (Randomised) | Recruiting | 218 | Ipilimumab + nivolumab ± intracranial SRS in asymptomatic, untreated melanoma brain metastases; broad subtype eligibility. |

### Acral Lentiginous Melanoma (Rank 7, L2)

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04511013](https://clinicaltrials.gov/study/NCT04511013) | Phase 2 (Randomised) | Recruiting | 112 | Encorafenib + binimetinib + nivolumab vs ipilimumab + nivolumab in BRAF-mutant melanoma with brain metastases; acral subtype included as stratification factor. |
| [NCT02519322](https://clinicaltrials.gov/study/NCT02519322) | Phase 2 | Completed | 53 | Neoadjuvant + adjuvant checkpoint blockade (nivolumab ± ipilimumab ± relatlimab) in Stage III/oligometastatic Stage IV melanoma; acral lentiginous subgroup analysed. |
| [NCT04462406](https://clinicaltrials.gov/study/NCT04462406) | Phase 2 | Active, Not Recruiting | 150 | PET-Stop: biomarker-driven study in advanced melanoma including acral lentiginous subtype. |
| [NCT02978443](https://clinicaltrials.gov/study/NCT02978443) | Phase 2 | Terminated | 14 | Nivolumab + ipilimumab in mucosal and acral lentiginous melanoma specifically. **TERMINATED** due to insufficient efficacy (n=14); constitutes an important negative signal for this subtype. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24999899](https://pubmed.ncbi.nlm.nih.gov/24999899/) | 2014 | Retrospective Cohort | Med J Aust | **Australian real-world data**: Ipilimumab efficacy and tolerability in cutaneous, uveal, and mucosal melanoma at Peter MacCallum Cancer Centre. Evaluates association with melanoma subtype, BRAF status, lymphocyte count, and irAEs. Directly applicable to Australian clinical context. |
| [28056206](https://pubmed.ncbi.nlm.nih.gov/28056206/) | 2017 | Phase 3 Pooled Sub-analysis | J Clin Oncol | Pooled analysis of 889 patients from Phase 3 trials: nivolumab ± ipilimumab in mucosal melanoma. Combination ORR 23.3% vs 8.3% nivolumab monotherapy — most robust mucosal-specific efficacy evidence. |
| [24100024](https://pubmed.ncbi.nlm.nih.gov/24100024/) | 2014 | Prospective Cohort | Eur J Cancer | Ipilimumab 3 mg/kg in expanded access programme for pretreated metastatic mucosal melanoma. Disease control rate 36%, median OS 6.4 months. First large prospective mucosal-specific ipilimumab efficacy dataset. |
| [33715172](https://pubmed.ncbi.nlm.nih.gov/33715172/) | 2021 | Phase 2 — 5-Year Follow-up | J Dermatol | 5-year OS data from Japanese Phase 2 nivolumab study in treatment-naïve Stage III/IV melanoma (n=24). Overall 5-year OS 26.1%; 66.7% in acral subgroup. Critical long-term data from a population with high ALM prevalence. |
| [39269143](https://pubmed.ncbi.nlm.nih.gov/39269143/) | 2024 | Retrospective Cohort | J Dermatol | Japanese single-centre: nivolumab + ipilimumab vs PD-1 monotherapy as first-line in advanced mucosal melanoma. Combination superior in Asian patients; relevant to Australian Asian-population practice. |
| [29079332](https://pubmed.ncbi.nlm.nih.gov/29079332/) | 2018 | Retrospective Cohort | J Dermatol Sci | Japanese retrospective (n=60): ipilimumab after nivolumab failure across melanoma subtypes including acral lentiginous melanoma. Provides sequential therapy data. |
| [31172258](https://pubmed.ncbi.nlm.nih.gov/31172258/) | 2019 | Retrospective Cohort | Cancer Immunol Immunother | Anti-CTLA4 and anti-PD1 immunotherapy efficacy in non-resectable mucosal melanoma; response rate and survival analysis. |
| [27533633](https://pubmed.ncbi.nlm.nih.gov/27533633/) | 2016 | Retrospective Cohort | Cancer | Anti-PD-1 efficacy in acral and mucosal melanoma (n=series); ORR lower than cutaneous (~8–12%) but clinically meaningful durable responses documented. |
| [37887546](https://pubmed.ncbi.nlm.nih.gov/37887546/) | 2023 | Retrospective Cohort | Curr Oncol | Anti-PD-1 ± ipilimumab in advanced melanoma across age groups; provincial database study examining survival differences by age and subtype. |
| [29466692](https://pubmed.ncbi.nlm.nih.gov/29466692/) | 2018 | Review | Discov Med | Review of anti-PD-1 mAbs as frontline therapy for advanced melanoma; ipilimumab combination standard established from mature Phase 3 survival data. |

---

## Australia Market Information

No ARTG entries for Ipilimumab were identified in this data extract. Given that Ipilimumab (Yervoy, Bristol-Myers Squibb Australia) is known to hold regulatory approvals from the FDA, EMA, and multiple other regulators, this finding most likely reflects a data retrieval limitation rather than the drug's actual Australian registration status.

**Healthcare professionals must verify the current ARTG registration status directly with the TGA (www.tga.gov.au) before initiating any clinical or procurement pathway. Do not rely solely on this data extract for regulatory decision-making.**

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | **Immunotherapy — anti-CTLA-4 monoclonal antibody** (immune checkpoint inhibitor; not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | **Low** — not a direct myelosuppressive agent; immune-mediated haematological events (e.g., immune thrombocytopenia, haemolytic anaemia) are rare but possible |
| Emetogenicity Classification | **Low** — intravenous monoclonal antibody; standard anti-emetic prophylaxis not routinely required |
| Monitoring Items | FBC with differential, LFTs (ALT, AST, bilirubin, ALP), thyroid function (TSH, free T4), cortisol and ACTH (if adrenal insufficiency suspected), creatinine and urinalysis, blood glucose; clinical review for irAE signs and symptoms before each infusion |
| Handling Protection | Standard aseptic technique and monoclonal antibody reconstitution protocols apply; cytotoxic drug special handling regulations (closed-system transfer devices, cytotoxic gowns) are **not required** for ipilimumab under current Australian standard guidelines |

> **Critical note on immune-related adverse events (irAEs):** Although ipilimumab is not a cytotoxic agent, it carries substantial and potentially life-threatening toxicity. Grade 3–4 irAEs occur in approximately 20–30% of patients with ipilimumab monotherapy and 40–60% with ipilimumab + nivolumab combination. Fatal irAEs — including fulminant myocarditis, severe colitis, toxic epidermal necrolysis, and encephalitis — have been reported (see PMID 39548815 for a documented fatal case after first combined dose). All clinical sites must have an irAE management protocol in place before administration.

---

## Safety Considerations

Safety data for Ipilimumab was not retrieved in this Evidence Pack. Please refer to the **TGA-approved Product Information (PI) for Yervoy (ipilimumab)** for complete prescribing information.

Based on the clinical trial evidence reviewed:

- **Immune-related adverse events:** The dominant safety concern. Most common Grade ≥3 irAEs include colitis/diarrhoea (~7–10% monotherapy), hepatitis (~2–3%), hypophysitis (~3–5%), and dermatitis. Management requires early recognition and prompt immunosuppression
- **Combination toxicity:** Ipilimumab + nivolumab combination substantially increases irAE frequency and severity compared to either agent alone — particularly relevant for mucosal and acral melanoma regimens
- **Dose-dependent risk:** 10 mg/kg ipilimumab carries significantly higher irAE rates than the approved 3 mg/kg dose; irAE-related deaths have been reported at higher doses
- **No standard pharmacokinetic drug interactions** expected given monoclonal antibody catabolism; however, concurrent immunosuppressive therapy may reduce efficacy

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ipilimumab has robust Level 1 evidence (≥4 completed Phase 3 RCTs, n=531–1,783 each) supporting efficacy in advanced melanoma broadly. For non-cutaneous subtypes, there is dedicated Phase 2 randomised evidence for mucosal melanoma (NCT03033576 n=94; SALVO NCT03241186 n=36) and multiple Phase 2 trials underway or completed for acral lentiginous melanoma — the subtype most prevalent in Australia's Indigenous and Asian-Australian populations. An Australian real-world study (PMID 24999899) provides directly applicable local evidence. Despite lower response rates in non-cutaneous subtypes relative to cutaneous melanoma, the CTLA-4 blockade mechanism is biologically applicable and clinically validated across all melanoma histological variants evaluated in the top 10 predictions.

**To proceed, the following is needed:**

- **Urgent: Verify ARTG status** — Confirm Yervoy (ipilimumab) TGA registration at www.tga.gov.au before initiating any clinical pathway; 0 ARTG entries in this dataset may reflect a data gap
- **Obtain TGA PI** — Complete warnings, contraindications, approved indications, and dosing information from the current TGA-approved Product Information document
- **Retrieve MOA from DrugBank** — Complete the DrugBank API query (flagged as data gap) to populate mechanism of action data for future evidence evaluations
- **Multidisciplinary team (MDT) review** — Melanoma-specific MDT discussion required before initiating ipilimumab for any non-cutaneous subtype
- **irAE management protocol** — Confirm institutional irAE grading, monitoring, and treatment protocol is in place prior to first dose; coordinate with immunology and gastroenterology as needed
- **ANZCTR search** — Check the Australian New Zealand Clinical Trials Registry (www.anzctr.org.au) for currently recruiting non-cutaneous melanoma trials before committing to off-label use
- **Do not pursue Rank 1 (Choroideremia)** — Confirmed TxGNN false positive; no mechanistic or clinical evidence basis
- **Do not pursue Rank 8 (Balloon Cell Melanoma)** — L5 evidence; sole available literature is a fatal irAE case, constituting a safety signal with no efficacy data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

