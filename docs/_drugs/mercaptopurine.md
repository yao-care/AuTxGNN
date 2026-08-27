---
layout: default
title: Mercaptopurine
parent: 僅模型預測 (L5)
nav_order: 427
evidence_level: L5
indication_count: 10
---

# Mercaptopurine
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

# Mercaptopurine: From Acute Lymphoblastic Leukaemia to Myeloid Leukaemia

## One-Sentence Summary

Mercaptopurine (6-MP) is a thiopurine antimetabolite whose established use is in acute lymphoblastic leukaemia (ALL) maintenance therapy. The TxGNN model predicts it may also be effective for **Myeloid Leukaemia**, with **29 clinical trials** and **20 publications** currently identified in this evidence pack supporting further evaluation — though most trials involve 6-MP as part of combination maintenance regimens (particularly for acute promyelocytic leukaemia) rather than as a standalone-tested agent for this indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Lymphoblastic Leukaemia (established antileukaemic maintenance agent — no structured original-indication or ARTG data available in this pack; see note below) |
| Predicted New Indication | Myeloid Leukaemia |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

**Note on data gaps:** The `original_indications` and `original_moa` fields for this drug were empty in the source data (flagged as Data_Level gaps DG002, High severity). The original-indication statement above is derived from the extensive supporting clinical trial and literature evidence within this pack (6-MP as the backbone of ALL maintenance chemotherapy), not from a structured regulatory record.

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data was not available for this drug (data gap DG002). Based on the supporting evidence in this pack, Mercaptopurine is a purine analogue (thiopurine) that inhibits DNA/RNA synthesis after intracellular conversion to thioguanine nucleotides, producing cytotoxicity in rapidly proliferating haematopoietic blasts. This mechanism underlies its long-standing, well-proven role in ALL maintenance therapy.

Myeloid and lymphoid leukaemias share the underlying feature of uncontrolled proliferation of immature haematopoietic precursors, which is the basis for cross-lineage applicability of antimetabolite chemotherapy. Notably, the evidence base already shows 6-MP being used within combination maintenance regimens for acute myeloid leukaemia — particularly acute promyelocytic leukaemia (APL), where it is combined with methotrexate and ATRA in multiple large Phase 3/4 trials (e.g. AIDA, PETHEMA LPA2005) — as well as in early-phase trials combining 6-MP with newer agents (venetoclax, valproic acid) for relapsed/refractory AML and unfit AML/high-risk MDS patients. This existing precedent of use in myeloid disease supports the biological plausibility of the TxGNN prediction, although 6-MP is rarely the primary investigational agent in these regimens.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00408278](https://clinicaltrials.gov/study/NCT00408278) | Phase 4 | Completed | 300 | PETHEMA LPA2005: maintenance therapy with ATRA + low-dose chemotherapy (methotrexate + mercaptopurine) after risk-adapted induction/consolidation for newly diagnosed APL |
| [NCT00180128](https://clinicaltrials.gov/study/NCT00180128) | Phase 4 | Unknown | 80 | AIDA2000 risk-adapted APL therapy; 2-year maintenance with 6-mercaptopurine, methotrexate and ATRA |
| [NCT01064557](https://clinicaltrials.gov/study/NCT01064557) | N/A | Unknown | 1068 | AIDA protocol guideline for newly diagnosed APL, testing intermittent ATRA maintenance vs standard maintenance with methotrexate and 6-mercaptopurine |
| [NCT00465933](https://clinicaltrials.gov/study/NCT00465933) | Phase 4 | Completed | N/A | AIDA regimen for APL in patients >70 years; ATRA maintenance plus methotrexate/mercaptopurine salvage therapy for relapse |
| [NCT06199557](https://clinicaltrials.gov/study/NCT06199557) | Phase 1/2 | Recruiting | 48 | Hydroxyurea + valproic acid, or 6-mercaptopurine + valproic acid, in AML or high-risk MDS patients unfit for standard therapy |
| [NCT05506332](https://clinicaltrials.gov/study/NCT05506332) | Phase 1 | Recruiting | 10 | ApoAML: venetoclax combined with 6-mercaptopurine (purine analogue) as an oral combination for relapsed/refractory AML |
| [NCT00003934](https://clinicaltrials.gov/study/NCT00003934) | Phase 3 | Completed | 420 | Tretinoin + chemotherapy ± arsenic trioxide as consolidation for untreated APL, followed by maintenance with tretinoin alone vs tretinoin + mercaptopurine + methotrexate |
| [NCT00136084](https://clinicaltrials.gov/study/NCT00136084) | Phase 3 | Completed | 238 | Comparison of two multi-agent chemotherapy regimens (different cytarabine dosing) for newly diagnosed AML/myelodysplasia (disease-level evidence; not mercaptopurine-specific) |
| [NCT00866918](https://clinicaltrials.gov/study/NCT00866918) | Phase 3 | Completed | 106 | Risk-adapted arsenic trioxide consolidation for newly diagnosed childhood APL (6-MP not the primary study drug) |
| [NCT00962767](https://clinicaltrials.gov/study/NCT00962767) | Phase 3 | Completed | 168 | Gemtuzumab ozogamicin dosing vs 2-year ATRA + chemotherapy maintenance as post-consolidation treatment for intermediate/high-risk APL |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10497848](https://pubmed.ncbi.nlm.nih.gov/10497848/) | 1999 | RCT | International Journal of Hematology | JALSG-AML92: adding etoposide to daunorubicin/cytarabine/6-MP induction gave no additional benefit in adult AML |
| [9095207](https://pubmed.ncbi.nlm.nih.gov/9095207/) | 1997 | Clinical trial | Cancer Investigation | High-dose IV 6-MP plus intermediate-dose cytarabine was feasible during first AML remission in children (14/17 achieved CR) |
| [26425037](https://pubmed.ncbi.nlm.nih.gov/26425037/) | 2015 | Cohort | Journal of Korean Medical Science | Oral maintenance with 6-MP + methotrexate after consolidation improved leukaemia-free survival in transplant-ineligible AML patients |
| [8174198](https://pubmed.ncbi.nlm.nih.gov/8174198/) | 1994 | RCT | Cancer Chemotherapy and Pharmacology | Nationwide randomised trial: daunorubicin vs aclarubicin combined with BHAC/6-MP/prednisolone in untreated AML (CR 63.7% vs 53.9%) |
| [8558199](https://pubmed.ncbi.nlm.nih.gov/8558199/) | 1996 | RCT | Journal of Clinical Oncology | Randomised comparison of BHAC vs cytarabine (± ubenimex) in combination induction/consolidation for adult AML |
| [1793832](https://pubmed.ncbi.nlm.nih.gov/1793832/) | 1991 | Clinical study | International Journal of Hematology | Intensive individualised induction with BHAC, daunorubicin and 6-MP achieved 71% complete remission in adult AML |
| [5220682](https://pubmed.ncbi.nlm.nih.gov/5220682/) | 1966 | Case series | Minnesota Medicine | Early report of AML treated with 6-MP and cyclophosphamide |
| [4518586](https://pubmed.ncbi.nlm.nih.gov/4518586/) | 1973 | Clinical study | Cancer | Treatment of adult AML with cytarabine in combination with 6-MP |
| [1059498](https://pubmed.ncbi.nlm.nih.gov/1059498/) | 1975 | Clinical study | Cancer | Childhood AML treated with cytarabine, daunorubicin, prednisolone and mercaptopurine or thioguanine (78% initial remission rate) |
| [265178](https://pubmed.ncbi.nlm.nih.gov/265178/) | 1977 | Case series | Blood | Juvenile chronic myeloid leukaemia treated with sequential subcutaneous cytarabine and oral mercaptopurine (3 cases) |

## Australia Market Information

Mercaptopurine is **not currently registered on the Australian Register of Therapeutic Goods (ARTG)** and has no marketed product in Australia (0 ARTG entries, market status: not marketed). Any use in Australia would require sourcing via an unapproved-medicine pathway (e.g. TGA Special Access Scheme or Authorised Prescriber pathway) and referencing overseas-approved Product Information, as no Australian PI exists for this drug.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antimetabolite — thiopurine/purine analogue class) |
| Myelosuppression Risk | High — well documented across the literature evidence, particularly in TPMT- and NUDT15-deficient patients, where risk of severe neutropenia is markedly increased |
| Emetogenicity Classification | Low (consistent with the general antimetabolite/thiopurine class) |
| Monitoring Items | FBC with differential, liver function tests, renal function; TPMT and/or NUDT15 genotype or phenotype testing prior to initiation is strongly supported by the pharmacogenomic literature in this pack |
| Handling Protection | Standard cytotoxic drug handling and disposal precautions required |

## Safety Considerations

No structured TGA/TFDA warnings, contraindications or drug-interaction data were available for this drug in the evidence pack (flagged as data gap DG001, Blocking severity — this currently prevents a formal safety pre-assessment). Please refer to an approved Product Information from a jurisdiction where Mercaptopurine is registered, and obtain specialist haematology/oncology input, before considering clinical use.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple Phase 3/4 trials and mechanistic/clinical literature support 6-MP's use within myeloid leukaemia (largely APL) maintenance regimens, and the TxGNN prediction score is very high (99.94%). However, the drug is unregistered in Australia and a Blocking-severity safety data gap (no TGA-equivalent warnings/contraindications) currently prevents formal safety sign-off.

**To proceed, the following is needed:**
- Product Information (warnings, contraindications) sourced from a jurisdiction where Mercaptopurine is TGA/TFDA-equivalent registered, to resolve the Blocking safety gap (DG001)
- Formal mechanism-of-action documentation (DG002)
- Confirmation of TPMT/NUDT15 testing availability and a monitoring protocol before any clinical use
- A defined access pathway (TGA Special Access Scheme or Authorised Prescriber) given the drug is not marketed in Australia
- Clarification of the specific myeloid leukaemia subtype(s) (the strongest evidence is for APL maintenance rather than AML generally)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

