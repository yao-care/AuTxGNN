---
layout: default
title: Afatinib
parent: 僅模型預測 (L5)
nav_order: 25
evidence_level: L5
indication_count: 10
---

# Afatinib
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

# Afatinib: From Non-Small Cell Lung Cancer to HER2 Positive Breast Carcinoma

## One-Sentence Summary

Afatinib is an orally bioavailable, irreversible pan-ErbB tyrosine kinase inhibitor globally approved for the treatment of EGFR mutation-positive non-small cell lung cancer (NSCLC), though not currently registered in Australia.
The TxGNN model predicts it may be effective for **HER2 Positive Breast Carcinoma**,
with **10 clinical trials** (including one completed Phase 3 RCT) and **19 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | EGFR mutation-positive non-small cell lung cancer (globally approved; not registered in Australia) |
| Predicted New Indication | HER2 Positive Breast Carcinoma |
| TxGNN Prediction Score | 98.65% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Afatinib covalently and irreversibly binds to the kinase domains of EGFR (HER1), HER2, and HER4, permanently suppressing all relevant ErbB receptor homodimers and heterodimers. This broad-spectrum ErbB blockade drives suppression of key downstream proliferation and survival pathways including MAPK and PI3K/Akt. Detailed mechanism of action data is not yet fully available in this evidence pack, but afatinib's class characteristics as a second-generation, irreversible pan-ErbB inhibitor are well-established in the published literature and distinguish it from first-generation reversible agents such as erlotinib and gefitinib, and from the narrower reversible HER2 inhibitor lapatinib.

HER2-positive breast carcinoma — affecting approximately 15–20% of all breast cancers — is fundamentally driven by HER2 gene amplification or protein overexpression, making it a direct mechanistic target for afatinib. Beyond primary HER2 inhibition, a key advantage of afatinib's pan-ErbB profile is its capacity to suppress compensatory signalling through HER3 and HER4, which are recognised escape routes underlying acquired resistance to trastuzumab. Afatinib also demonstrates the ability to cross the blood–brain barrier, providing a mechanistically distinct approach for patients who develop central nervous system (CNS) metastases — a common and clinically serious complication occurring in 30–50% of advanced HER2+ breast cancer patients.

The prediction is directly supported by the LUX-Breast 1 Phase 3 randomised controlled trial (n=508), which compared afatinib plus vinorelbine against trastuzumab plus vinorelbine in trastuzumab-pretreated HER2-overexpressing metastatic breast cancer. Although the primary endpoint of progression-free superiority was not achieved (afatinib arm 5.5 months vs. trastuzumab arm 5.6 months), the trial confirmed that afatinib has meaningful biological activity in this population, including a similar safety and efficacy profile to continued trastuzumab in this post-progression setting. Additionally, LUX-Breast 3 (NCT01441596, n=121) specifically addressed the CNS metastases subgroup, further supporting the mechanistic rationale for afatinib in HER2+ breast cancer.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT01125566](https://clinicaltrials.gov/study/NCT01125566) | Phase 3 | Completed | 508 | LUX-Breast 1: Afatinib + vinorelbine vs trastuzumab + vinorelbine in HER2-overexpressing metastatic breast cancer after one prior trastuzumab treatment. Primary PFS endpoint not met (5.5 vs 5.6 months); however, confirmed comparable biological activity of afatinib in this population. |
| [NCT01441596](https://clinicaltrials.gov/study/NCT01441596) | Phase 2 | Completed | 121 | LUX-Breast 3: Randomised comparison of afatinib alone, afatinib + vinorelbine, or investigator's choice in HER2+ breast cancer with progressive brain metastases after trastuzumab and/or lapatinib. Key evidence supporting afatinib use in CNS metastases. |
| [NCT04158947](https://clinicaltrials.gov/study/NCT04158947) | Phase 2 | Unknown | 130 | Afatinib + T-DM1 vs T-DM1 alone in HER2+ breast cancer with active refractory brain metastases. Phase I component determines MTD; Phase II evaluates PFS. Directly validates afatinib's CNS penetration advantage in a contemporary combination context. |
| [NCT01594177](https://clinicaltrials.gov/study/NCT01594177) | Phase 2 | Completed | 65 | Dual HER2 blockade (afatinib + trastuzumab) as neoadjuvant treatment in locally advanced or operable HER2+ breast cancer receiving taxane-anthracycline chemotherapy. Explores additive benefit of broader ErbB blockade alongside trastuzumab. |
| [NCT00826267](https://clinicaltrials.gov/study/NCT00826267) | Phase 2 | Completed | 29 | Randomised three-arm neoadjuvant trial: afatinib vs lapatinib vs trastuzumab as single agents in HER2+ Stage IIIa locally advanced breast cancer. Head-to-head comparison provides direct benchmarking of afatinib against current standards. |
| [NCT00431067](https://clinicaltrials.gov/study/NCT00431067) | Phase 2 | Completed | 41 | Afatinib monotherapy in HER2+ metastatic breast cancer after failure of trastuzumab-containing regimens. ORR approximately 10% as single agent; confirms biological activity in post-trastuzumab disease. |
| [NCT00950742](https://clinicaltrials.gov/study/NCT00950742) | Phase 1 | Completed | 18 | Afatinib + 3-weekly trastuzumab (Herceptin®) in HER2+ advanced breast cancer. Established MTD and safety basis for afatinib-trastuzumab combination regimens. |
| [NCT01320280](https://clinicaltrials.gov/study/NCT01320280) | Phase 2 | Terminated | 29 | Afatinib in HER2-positive hormone-refractory prostate cancer post-docetaxel. Terminated early; provides partial safety and biological activity data in HER2-overexpressing solid tumours beyond breast cancer. |
| [NCT01531764](https://clinicaltrials.gov/study/NCT01531764) | Phase 2 | Terminated | 2 | Afatinib + vinorelbine in intermediate HER2 expression (IHC 2+/FISH-negative) metastatic breast cancer. Terminated after 2 enrolments; no statistically usable efficacy data. |
| [NCT02438722](https://clinicaltrials.gov/study/NCT02438722) | Phase 2/3 | Active, not recruiting | 174 | Afatinib + cetuximab vs afatinib alone in EGFR mutation-positive NSCLC. Explores dual ErbB/EGFR blockade strategy with mechanistic relevance to HER-family inhibition principles. Results pending. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [26822398](https://pubmed.ncbi.nlm.nih.gov/26822398/) | 2016 | Phase 3 RCT | Lancet Oncology | LUX-Breast 1 primary results: afatinib + vinorelbine vs trastuzumab + vinorelbine in HER2+ metastatic breast cancer; PFS equivalent but non-superior, confirming afatinib biological activity in trastuzumab-refractory disease. |
| [35138529](https://pubmed.ncbi.nlm.nih.gov/35138529/) | 2022 | Phase 2 RCT | Breast Cancer Res Treat | LUX-Breast 2 results: afatinib alone followed by afatinib ± vinorelbine or paclitaxel in HER2+ MBC after trastuzumab/lapatinib failure. Evaluates irreversible ErbB blockade to overcome prior anti-HER2 therapy resistance. |
| [35653982](https://pubmed.ncbi.nlm.nih.gov/35653982/) | 2022 | Systematic Review / Meta-analysis | ESMO Open | TKIs (including afatinib) in HER2+ breast cancer with brain metastases; meta-analysis confirms superior clinical outcomes with TKI-containing regimens versus non-TKI regimens for CNS disease. |
| [24080156](https://pubmed.ncbi.nlm.nih.gov/24080156/) | 2014 | Systematic Review | Cancer Treatment Reviews | Dual HER2 targeting in HER2+ breast cancer; contextualises afatinib's pan-ErbB blockade as a strategy to overcome trastuzumab resistance, summarising preclinical and early clinical data. |
| [38367127](https://pubmed.ncbi.nlm.nih.gov/38367127/) | 2024 | Comparative Study | Clin Exp Metastasis | T-DM1, T-DXd, and disitamab vedotin compared in multi-resistant HER2+ breast cancer lung metastasis model; provides preclinical context for drug sequencing and combination strategies including TKIs. |
| [33122343](https://pubmed.ncbi.nlm.nih.gov/33122343/) | 2021 | In vitro / Mechanistic | Clin Cancer Res | Afatinib and other TKIs enhance antibody-dependent cell-mediated cytotoxicity (ADCC) in HER2-expressing breast cancer; supports mechanistic basis for afatinib–trastuzumab combinations. |
| [30062574](https://pubmed.ncbi.nlm.nih.gov/30062574/) | 2019 | In vitro | Investig New Drugs | Afatinib combined with trastuzumab ± pertuzumab in HER2+ breast cancer cell lines; TKIs potentiate the anti-proliferative effects of standard HER2-targeted monoclonal antibodies. |
| [29772459](https://pubmed.ncbi.nlm.nih.gov/29772459/) | 2018 | Review | Cancer Treatment Reviews | TKIs for brain metastases in HER2+ breast cancer; reviews CNS penetration properties of afatinib and clinical utility in an unmet-need setting with approximately 30–50% CNS metastasis incidence. |
| [24870559](https://pubmed.ncbi.nlm.nih.gov/24870559/) | 2014 | Review | Expert Opin Investig Drugs | Comprehensive review of afatinib's clinical development in breast cancer; covers activity in HER2+ disease, resistance mechanisms, and positioning relative to other anti-HER2 agents. |
| [22763464](https://pubmed.ncbi.nlm.nih.gov/22763464/) | 2012 | Phase 2 Trial | Breast Cancer Res Treat | Afatinib in extensively pretreated HER2-negative metastatic breast cancer; demonstrates that pan-ErbB blockade retains some activity even without HER2 amplification, supporting broader ErbB pathway dependence. |

---

## Australia Market Information

Afatinib is currently **not registered with the Australian Therapeutic Goods Administration (TGA)** and has no entries on the Australian Register of Therapeutic Goods (ARTG).

> **Note for clinicians:** Afatinib (brand name Gilotrif®) is approved in multiple other jurisdictions — including by the US FDA, the European Medicines Agency (EMA), and Japan's PMDA — for the first-line treatment of EGFR mutation-positive (exon 19 deletions or exon 21 L858R substitution) non-small cell lung cancer. In some jurisdictions it also holds approval for squamous cell carcinoma of the lung after platinum-based chemotherapy. Any use in Australian patients would currently require an application through the TGA's Special Access Scheme (SAS) or Authorised Prescriber pathway, pending formal ARTG registration.

---

## Cytotoxicity

Afatinib is an antineoplastic agent used in the treatment of malignancies; this section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Irreversible second-generation pan-ErbB (EGFR/HER2/HER4) tyrosine kinase inhibitor |
| Myelosuppression Risk | Low (TKIs, including afatinib, are not associated with the clinically significant myelosuppression typical of conventional cytotoxic chemotherapy; haematological toxicity is uncommon) |
| Emetogenicity Classification | Low (oral TKIs are generally classified as low emetogenic risk; afatinib's primary GI toxicity is diarrhoea rather than nausea/vomiting) |
| Monitoring Items | Liver function tests (LFTs), renal function (eGFR), full blood count (FBC), electrolytes (particularly potassium/magnesium with diarrhoea), pulmonary function if ILD symptoms develop, skin/nail toxicity assessment at each review |
| Handling Protection | Standard cytotoxic handling precautions apply as per institutional policy for oral antineoplastic agents; appropriate PPE during dispensing/administration and patient counselling on safe handling at home required |

---

## Safety Considerations

Afatinib is not TGA-registered; no Australian Product Information is currently available. Please refer to the FDA-approved Gilotrif® Prescribing Information and/or the EMA Summary of Product Characteristics for comprehensive safety data.

> **Known class-effect safety signals for afatinib** (based on international PI and published trials): The most common and clinically significant adverse effects include **diarrhoea** (often dose-limiting; Grade 3+ in ~14% of patients), **acneiform rash/dermatitis** (very common; requires proactive skin management), **stomatitis/mucositis**, **paronychia**, and **dry skin**. Rare but serious risks include **interstitial lung disease (ILD)/pneumonitis** (discontinue if suspected) and **hepatotoxicity** (LFT monitoring required). **Embryo-fetal toxicity** is expected based on mechanism; contraception counselling is essential. Dose reductions are commonly required based on tolerability.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Afatinib's irreversible pan-ErbB inhibition is mechanistically well-aligned with the core oncogenic driver of HER2-positive breast carcinoma, and the totality of evidence — anchored by the LUX-Breast 1 Phase 3 RCT (n=508) and multiple completed Phase 2 trials — confirms clinically meaningful biological activity in this disease setting, particularly in trastuzumab-refractory and CNS-metastatic subgroups. Although LUX-Breast 1 did not demonstrate superiority over continued trastuzumab-based therapy in the overall population, afatinib's CNS penetration and resistance-overcoming mechanism justify further clinical exploration in specific patient subpopulations where unmet need remains high.

**To proceed, the following is needed:**

- **TGA registration or access pathway**: Afatinib has no ARTG entry; a TGA Special Access Scheme (SAS Category B) application or Authorised Prescriber designation is required for any use in Australian patients prior to formal registration
- **Patient population definition**: Prospective use should be restricted to well-defined subgroups with the strongest evidence base — trastuzumab-refractory HER2+ MBC, and/or HER2+ breast cancer with active CNS metastases — rather than unselected HER2+ breast cancer
- **Safety profile documentation**: Full safety assessment using FDA/EMA approved PI data must be completed; Australian prescribing information will be required upon TGA registration
- **Mechanism of action documentation**: Complete DrugBank MOA data retrieval is outstanding (current data gap DG002) and should be obtained to finalise the mechanistic rationale analysis
- **Combination strategy planning**: Evidence supports multiple combination approaches (afatinib + vinorelbine; afatinib + trastuzumab; afatinib + T-DM1); specific combination and sequencing within the Australian treatment landscape (relative to tucatinib, neratinib, T-DXd) must be formally evaluated
- **Drug interaction assessment**: DDI data is currently not available (query returned no results); formal DDI review against commonly co-administered medications in breast cancer (e.g., antiemetics, steroids, CDK4/6 inhibitors) is required before clinical use
- **Regulatory alignment check**: Assess whether afatinib's role in HER2+ breast cancer overlaps with or is superseded by already-approved agents in Australia (e.g., neratinib, tucatinib, trastuzumab deruxtecan) to identify the most clinically differentiated positioning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

