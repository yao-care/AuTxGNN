---
layout: default
title: Anastrozole
parent: 僅模型預測 (L5)
nav_order: 48
evidence_level: L5
indication_count: 10
---

# Anastrozole
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

# Anastrozole: From Postmenopausal ER-Positive Breast Cancer to Female Breast Carcinoma

## One-Sentence Summary

Anastrozole is a third-generation aromatase inhibitor internationally established for the treatment of hormone receptor-positive breast cancer in postmenopausal women, but it is not currently registered with the Australian Therapeutic Goods Administration (TGA).

The TxGNN model predicts it may be effective for **Female Breast Carcinoma** broadly — encompassing adjuvant, neoadjuvant, advanced, and chemoprevention settings — with **50+ clinical trials** and **20 publications** currently supporting this direction.

The overall evidence base is among the strongest available for any cancer indication, anchored by landmark Phase 3 trials including ATAC and IBIS-II.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (Anastrozole is not currently registered in Australia; internationally approved for hormone receptor-positive early and advanced breast cancer in postmenopausal women) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L1 |
| Australia Market Status | Not Registered |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Anastrozole selectively inhibits the aromatase enzyme (CYP19A1), which is responsible for the final step of oestrogen biosynthesis in peripheral tissues — including fat, muscle, liver, and breast tumour stroma. By suppressing circulating and local oestrogen levels, anastrozole deprives oestrogen receptor-positive (ER+) breast cancer cells of their primary growth signal, leading to cell cycle arrest and tumour regression. This mechanism is direct, well-characterised, and underpins its worldwide clinical adoption.

In postmenopausal women, where the ovaries have ceased to be the dominant oestrogen source, peripheral aromatisation becomes the principal oestrogen supply pathway. Anastrozole's targeted blockade at this point makes it especially effective in this population. The landmark ATAC trial (>9,000 postmenopausal women, 5-year adjuvant therapy) demonstrated statistically significant improvement in disease-free survival compared to tamoxifen, establishing anastrozole as a preferred adjuvant agent. The IBIS-II prevention trial further demonstrated a sustained 49% reduction in breast cancer incidence in high-risk women followed for over 10 years.

The TxGNN model's prediction for "female breast carcinoma" is strongly supported: it encompasses ER+ early-stage adjuvant therapy, neoadjuvant downsizing for operable disease, first-line treatment for advanced/metastatic disease, chemoprevention of ductal carcinoma in situ (DCIS), and combination strategies with CDK4/6 inhibitors (palbociclib, abemaciclib, ribociclib) or other novel agents. For triple-negative breast cancer (TNBC), which lacks ER expression, the mechanistic rationale is weak in monotherapy but anastrozole has been explored in combination approaches targeting co-drivers such as HDAC inhibition. The TGA has not yet registered anastrozole in Australia despite robust global evidence — making this a high-priority regulatory consideration.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT01953588](https://clinicaltrials.gov/study/NCT01953588) | Phase 3 | Active, Not Recruiting | 1,473 | ALTERNATE trial: neoadjuvant anastrozole vs fulvestrant vs combination in Stage II/III ER+/HER2- breast cancer; directly evaluates anastrozole as pre-surgical endocrine therapy |
| [NCT00143390](https://clinicaltrials.gov/study/NCT00143390) | Phase 3 | Completed | 298 | Exemestane vs anastrozole as initial hormonal therapy in advanced/recurrent breast cancer; confirms non-inferiority and establishes anastrozole's clinical role in this setting |
| [NCT02338310](https://clinicaltrials.gov/study/NCT02338310) | Phase 3 | Active, Not Recruiting | 4,486 | POETIC trial: perioperative aromatase inhibitor (including anastrozole) followed by standard adjuvant therapy; evaluates Ki67 as a predictor of time to recurrence |
| [NCT00635713](https://clinicaltrials.gov/study/NCT00635713) | Phase 3 | Completed | 588 | Double-blind RCT comparing fulvestrant 125/250 mg vs anastrozole 1 mg in advanced breast cancer; key benchmark trial for anastrozole's efficacy in the advanced setting |
| [NCT04711252](https://clinicaltrials.gov/study/NCT04711252) | Phase 3 | Active, Not Recruiting | 1,370 | SERENA-4: camizestrant + palbociclib vs anastrozole + palbociclib as first-line therapy in ER+/HER2- advanced breast cancer; uses anastrozole as the active comparator gold standard |
| [NCT02206984](https://clinicaltrials.gov/study/NCT02206984) | Phase 2 | Completed | 201 | Endocrine response in invasive lobular carcinoma (ILC); supports anastrozole benefit in this distinct breast cancer subtype |
| [NCT00256217](https://clinicaltrials.gov/study/NCT00256217) | Phase 2 | Completed | 42 | Anastrozole chemoprevention in DCIS and early invasive breast cancer in postmenopausal women; complementary to IBIS-II prevention data |
| [NCT04075604](https://clinicaltrials.gov/study/NCT04075604) | Phase 2 | Completed | 23 | Neoadjuvant nivolumab + palbociclib + anastrozole in ER+/HER2- breast cancer; evaluates novel immunotherapy combination with anastrozole as the endocrine backbone |
| [NCT01234532](https://clinicaltrials.gov/study/NCT01234532) | Phase 2 | Terminated | 5 | Entinostat + anastrozole in triple-negative breast cancer; exploratory HDAC combination strategy; early termination limits conclusions |
| [NCT04767594](https://clinicaltrials.gov/study/NCT04767594) | N/A (Observational) | Active, Not Recruiting | 1,409 | PERFORM: real-world prospective cohort of HR+/HER2- advanced breast cancer on palbociclib + endocrine therapy (including anastrozole); provides safety and effectiveness data in routine clinical practice |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31839281](https://pubmed.ncbi.nlm.nih.gov/31839281/) | 2020 | Phase 3 RCT (Prevention) | *Lancet* | IBIS-II long-term follow-up: anastrozole reduces breast cancer incidence by 49% in high-risk postmenopausal women; sustained benefit beyond the 5-year treatment period |
| [15639680](https://pubmed.ncbi.nlm.nih.gov/15639680/) | 2005 | Phase 3 RCT | *Lancet* | ATAC trial 5-year results: anastrozole significantly improves disease-free survival vs tamoxifen in postmenopausal women with localised breast cancer (HR 0.87); fewer serious adverse effects |
| [28614542](https://pubmed.ncbi.nlm.nih.gov/28614542/) | 2017 | Systematic Review | *Rev Assoc Med Bras* | Comprehensive review of anastrozole in chemoprevention and treatment; confirms potent, selective aromatase inhibition with favourable pharmacokinetics and superior efficacy over tamoxifen across multiple settings |
| [24716940](https://pubmed.ncbi.nlm.nih.gov/24716940/) | 2014 | Meta-analysis of RCTs | *Asian Pac J Cancer Prev* | Meta-analysis comparing fulvestrant 250 mg vs anastrozole 1 mg in advanced breast cancer; provides pooled efficacy and tolerability data supporting anastrozole's established role |
| [20923259](https://pubmed.ncbi.nlm.nih.gov/20923259/) | 2010 | Drug Review | *Expert Opin Drug Safety* | Safety profile review of anastrozole in the adjuvant setting; multiple RCTs show greater efficacy than tamoxifen; highlights musculoskeletal and bone density considerations |
| [16439860](https://pubmed.ncbi.nlm.nih.gov/16439860/) | 2006 | Review | *Oncology* | Reviews anastrozole across the full breast cancer continuum — from advanced disease to early cancer and prevention; outlines survival benefits and tolerability advantages |
| [16761927](https://pubmed.ncbi.nlm.nih.gov/16761927/) | 2006 | Review | *Expert Rev Anticancer Ther* | ATAC-focused clinical update; confirms anastrozole's significant efficacy and tolerability advantages as initial adjuvant treatment in postmenopausal hormone receptor-positive breast cancer |
| [14687437](https://pubmed.ncbi.nlm.nih.gov/14687437/) | 2003 | Review | *Curr Med Res Opin* | Overview of anastrozole's evolving role in breast cancer management; confirms superiority over megestrol acetate and medroxyprogesterone as second-line treatment, and comparability to tamoxifen as first-line |
| [21508387](https://pubmed.ncbi.nlm.nih.gov/21508387/) | 2011 | Pharmacodynamic Study | *Anticancer Research* | Characterises anastrozole's effect on steroid sulfatase activity and serum androgen concentrations; provides mechanistic insight into the broader hormonal milieu altered by aromatase inhibition |
| [41024216](https://pubmed.ncbi.nlm.nih.gov/41024216/) | 2025 | Case Report / Mechanism Study | *J Med Case Reports* | Documents a case where anastrozole-induced hormonal changes (decreased oestrogen, increased dihydrotestosterone) may have contributed to development of apocrine mammary carcinoma and follicular lymphoma; highlights importance of long-term monitoring |

---

## Australia Market Information

Anastrozole is currently **not registered** with the Australian TGA and has no active ARTG entries in the database queried. There are no approved product entries to display.

> **Note for clinicians:** Despite the absence of TGA registration at the time of this data extract, anastrozole is widely approved by comparable international regulators including the US FDA, EMA (Europe), PMDA (Japan), and Health Canada. Generic anastrozole is available globally. The absence of ARTG entries may reflect a data collection gap rather than a clinical availability gap — TGA registration status should be verified directly via the [TGA ARTG Public Summary](https://www.tga.gov.au/resources/artg).

---

## Cytotoxicity

Anastrozole is an anticancer drug but is **not a conventional cytotoxic agent**. It acts via targeted endocrine modulation rather than direct DNA damage or cell killing.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Non-cytotoxic — Targeted endocrine therapy (Third-generation non-steroidal aromatase inhibitor) |
| Myelosuppression Risk | Low — Aromatase inhibitors do not cause clinically significant myelosuppression; bone marrow toxicity is not a recognised class effect |
| Emetogenicity Classification | Minimal — Oral tablet; nausea is uncommon and rarely clinically significant |
| Monitoring Items | Bone mineral density (DEXA scan at baseline and periodically — AI-induced bone loss is a key concern); lipid profile; liver function tests (if clinically indicated); musculoskeletal symptom assessment (arthralgia, myalgia) |
| Handling Protection | Standard oral medication precautions apply; NOT classified as a cytotoxic drug requiring specialised handling under hazardous drug regulations — standard dispensing and administration procedures are appropriate |

---

## Safety Considerations

Specific safety data (TGA-approved warnings, contraindications, and drug interaction records) were not available in this Evidence Pack.

> Please refer to the TGA-approved Product Information (PI) and the internationally available manufacturer's PI (e.g., Arimidex® PI) for comprehensive safety information, including known musculoskeletal effects, bone density loss, cardiovascular considerations, and interactions with oestrogen-containing products and tamoxifen.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for anastrozole in female breast carcinoma is among the most robust in oncology — multiple completed Phase 3 RCTs (ATAC, IBIS-II, and others) demonstrate superiority over tamoxifen in postmenopausal ER-positive disease, and the mechanistic rationale (CYP19A1 inhibition → oestrogen suppression → ER+ tumour regression) is well-established and directly validated. The primary barrier is the absence of current TGA registration in Australia, not a lack of efficacy evidence.

**To proceed, the following is needed:**

- **TGA Registration Verification:** Confirm whether anastrozole is registered in Australia under the ARTG (the current data showing 0 entries may reflect a data collection gap — anastrozole generics are widely marketed internationally)
- **Formal MOA Documentation:** Obtain DrugBank API data for official mechanism of action, drug categories, and toxicity classifications to complete the evidence dossier
- **TGA Product Information (PI) Review:** Retrieve and review the TGA-approved or internationally available PI for complete warnings, contraindications, special population data (pregnancy, renal/hepatic impairment), and drug interactions
- **Bone Health Management Plan:** Given the well-documented risk of AI-induced bone loss, any Australian clinical programme should include a DEXA monitoring protocol and bisphosphonate co-prescription criteria (as evaluated in NCT00122356 with alendronate)
- **Population Stratification:** Clarify the intended patient population — ER+ vs TNBC vs prevention — as the mechanistic rationale and evidence strength differ substantially across these subgroups
- **Regulatory Pathway Assessment:** If TGA registration is confirmed absent, determine whether a TGA submission, compassionate access application, or reliance pathway (based on FDA/EMA approval) is the most efficient route to market authorisation

---

*This report is generated for research purposes only. Drug repurposing candidates require clinical validation before therapeutic application. All treatment decisions must be made by qualified healthcare professionals in accordance with current TGA-approved guidelines. Data cutoff: 5 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

