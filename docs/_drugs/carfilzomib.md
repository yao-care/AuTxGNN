---
layout: default
title: Carfilzomib
parent: 僅模型預測 (L5)
nav_order: 126
evidence_level: L5
indication_count: 10
---

# Carfilzomib
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

# Carfilzomib: From Multiple Myeloma to Myeloid Leukemia

## One-Sentence Summary

Carfilzomib (Kyprolis) is a second-generation irreversible proteasome inhibitor approved internationally for relapsed/refractory multiple myeloma, though it is not currently registered in Australia.
The TxGNN model identifies **myeloid leukemia** as the most evidence-supported repurposing candidate among 10 predicted indications, with **1 completed Phase 1 clinical trial** (NCT01137747) and **multiple preclinical and mechanistic publications** directly supporting this direction.
While the TxGNN model's top-ranked prediction by score is CMM7 (a rare hereditary melanoma subtype, 99.37%), that indication carries no supporting evidence — myeloid leukemia (97.01%, ranked #8) is the focus of this report as the most clinically actionable candidate.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Relapsed/refractory multiple myeloma (internationally approved; not registered in Australia) |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 97.01% (ranked #8 overall; highest-evidence prediction) |
| Evidence Level | L3 (Phase 1 trial completed + preclinical and mechanistic studies) |
| Australia Market Status | Not registered in Australia |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Carfilzomib belongs to the proteasome inhibitor class and selectively and irreversibly inhibits the chymotrypsin-like activity (β5 subunit) of the 20S proteasome. In multiple myeloma, the extraordinary volume of immunoglobulin production places an extreme burden on the ubiquitin-proteasome system (UPS), making these cells critically dependent on proteasome activity for survival. Carfilzomib overwhelms this system, triggering ER stress accumulation and downstream apoptosis.

Myeloid leukemia cells share a closely related vulnerability. AML cells demonstrate high NF-κB pathway dependence and elevated unfolded protein response (UPR) stress — both of which are directly disrupted by proteasome inhibition. A 2016 review (PMID 27911437) specifically examined the proteasome's role in AML and noted that proteasome inhibitors including carfilzomib induce antiproliferative and proapoptotic effects in primary human AML cells. A 2017 study (PMID 28340282) went further, demonstrating that carfilzomib induces leukemia cell apoptosis via an additional non-proteasome mechanism — inhibiting ELK1/CIP2A and activating the tumour suppressor PP2A — suggesting broader activity than direct proteasomal blockade alone.

Critically, a completed Phase 1 clinical trial (NCT01137747) directly tested escalating doses of Carfilzomib in relapsed AML and ALL patients and has published results (PMID 26674111). Synergistic activity with tyrosine kinase inhibitors in CML models (PMID 24590311) and a 2024 study showing that proteasome inhibition enhances CAR-NK cell efficacy against AML (PMID 39285441) collectively provide a biologically coherent and clinically tested rationale. The mechanistic link between multiple myeloma and myeloid leukemia is thus well-grounded in shared UPS dependency, with the myeloid leukaemia application having crossed from preclinical into early clinical investigation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT01137747](https://clinicaltrials.gov/study/NCT01137747) | Phase 1 | Completed | 18 | Direct dose-escalation trial of Carfilzomib in relapsed AML and ALL; established pharmacokinetics, safety profile, and initial efficacy signals; results published (PMID 26674111) |
| [NCT02551718](https://clinicaltrials.gov/study/NCT02551718) | N/A | Completed | 34 | Pilot study of individualised treatment selection based on ex vivo chemosensitivity assay and genomic profiling in relapsed/refractory acute leukaemia; Carfilzomib included as one of the tested agents |

> **Note:** Two additional trials identified in the Evidence Pack (NCT03530683 — terminated TTI-622/anti-SIRPα antibody trial; NCT01204164 — TG02/CDK inhibitor Phase 1) are not Carfilzomib-specific and have low direct relevance to this repurposing hypothesis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [26674111](https://pubmed.ncbi.nlm.nih.gov/26674111/) | 2016 | Phase 1 Trial | Leukemia & Lymphoma | Phase I study of Carfilzomib in relapsed/refractory AML and ALL; clinical dosing, PK, and early safety/efficacy data established |
| [27911437](https://pubmed.ncbi.nlm.nih.gov/27911437/) | 2016 | Review | Blood Cancer Journal | Comprehensive review of the proteasome's role in AML; supports mechanistic rationale for Carfilzomib in myeloid malignancies |
| [28340282](https://pubmed.ncbi.nlm.nih.gov/28340282/) | 2017 | Basic Science | British Journal of Haematology | Carfilzomib induces leukaemia cell apoptosis via ELK1/CIP2A inhibition and PP2A activation, independent of proteasome inhibition — a novel secondary mechanism |
| [39285441](https://pubmed.ncbi.nlm.nih.gov/39285441/) | 2024 | Preclinical | Journal of Hematology & Oncology | Proteasome inhibition enhances anti-leukaemic efficacy of CAR-NK cells in AML by upregulating activating ligands on tumour cell surface (2024 combination strategy data) |
| [24590311](https://pubmed.ncbi.nlm.nih.gov/24590311/) | 2014 | In vitro | Oncogenesis | Carfilzomib synergises with TKIs in imatinib-sensitive and imatinib-resistant CML; provides rationale for combination approaches in myeloid malignancies |
| [24735925](https://pubmed.ncbi.nlm.nih.gov/24735925/) | 2014 | Basic Science | Cancer Cell | Proteasome inhibitors including carfilzomib evoke latent tumour suppression programmes in MLL-rearranged pro-B leukaemias via MLL-AF4 accumulation |
| [17341267](https://pubmed.ncbi.nlm.nih.gov/17341267/) | 2007 | In vitro | British Journal of Haematology | PR-171 (Carfilzomib) inhibits autocrine- and cytokine-dependent proliferation of primary human AML blasts at nanomolar concentrations |
| [19275578](https://pubmed.ncbi.nlm.nih.gov/19275578/) | 2009 | In vitro | Cardiovascular & Hematological Disorders Drug Targets | Carfilzomib (PR-171) shows antiproliferative and proapoptotic effects on leukaemia cells; synergism with HDAC inhibitors demonstrated |
| [40389585](https://pubmed.ncbi.nlm.nih.gov/40389585/) | 2025 | Preclinical | Scientific Reports | Selective immunoproteasome inhibitor M3258 induces proteotoxic stress and apoptosis in KMT2A::AFF1-driven ALL; supports next-generation proteasome targeting in leukaemia |
| [24418752](https://pubmed.ncbi.nlm.nih.gov/24418752/) | 2014 | Preclinical | Leukemia Research | HIV protease inhibitors induce proteotoxic stress and sensitise AML cells to proteasome inhibitor treatment; supports rational combination strategies for refractory AML |

---

## Australia Market Information

Carfilzomib is **not currently registered in Australia**. There are no ARTG entries. Healthcare professionals wishing to access Carfilzomib for Australian patients would need to consider the TGA Special Access Scheme (SAS) Category B pathway or participation in a clinical trial.

> **International context:** Carfilzomib (brand name Kyprolis) is approved by the FDA (United States) and EMA (Europe) for relapsed/refractory multiple myeloma, including in combination with lenalidomide and dexamethasone (KRd), or daratumumab and dexamethasone (DKd). As of the data cutoff date (21 June 2026), TGA registration has not been obtained.

---

## Cytotoxicity

Carfilzomib is classified as an antineoplastic agent (proteasome inhibitor). This section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — selective, irreversible proteasome inhibitor (20S proteasome, β5 chymotrypsin-like subunit) |
| Myelosuppression Risk | Moderate to High — thrombocytopenia and neutropenia are known class effects; particularly significant in leukaemia patients with compromised marrow reserve |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Full blood count (FBC) with differential; renal function (eGFR, creatinine, urea); liver function tests (LFTs); cardiac assessment (ECG, echocardiogram); blood pressure monitoring at each visit — Carfilzomib carries well-documented cardiovascular toxicity risk including cardiac failure and hypertension |
| Handling Protection | Must be handled per cytotoxic drug handling regulations; standard PPE required for preparation and administration |

---

## Safety Considerations

Detailed safety data (warnings, contraindications, and drug-drug interactions) are not available in this Evidence Pack.

Please refer to the FDA Prescribing Information for Carfilzomib (Kyprolis) for comprehensive safety data, given the absence of a TGA-approved Product Information document.

**Clinical note for Australian prescribers:** Based on international post-marketing surveillance and Phase 3 trial data, Carfilzomib carries a well-characterised risk of serious cardiovascular adverse events — including cardiac failure, acute coronary syndrome, pulmonary hypertension, and hypertension. These risks warrant cardiac baseline assessment and ongoing monitoring, and are of particular relevance in leukaemia patients who may have prior anthracycline exposure or pre-existing cardiac risk factors.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(Myeloid Leukemia indication)*

**Rationale:**
A completed Phase 1 trial (NCT01137747) has directly evaluated Carfilzomib in relapsed AML/ALL with published results, and multiple preclinical studies support the mechanistic basis. However, no Phase 2/3 efficacy data exists, and Carfilzomib is not registered in Australia — early clinical proof-of-concept is present, but the evidence base remains insufficient for standard clinical adoption without additional trial data.

**To proceed, the following is needed:**

- Obtain and review the full published Phase 1 results (PMID 26674111) — dose, response rate, and safety profile in the AML/ALL population
- Retrieve complete mechanism-of-action data from DrugBank (DB08889) to formalise the MOA-to-indication rationale
- Access FDA/EMA Prescribing Information for full safety, contraindication, and drug interaction data — this is a **blocking data gap** before any clinical recommendation can be made
- Conduct a formal cardiac risk assessment framework: Carfilzomib's cardiovascular toxicity profile requires a pre-specified monitoring plan specific to the leukaemia patient population
- Explore TGA Special Access Scheme (SAS) Category B eligibility for compassionate use in refractory AML patients with no remaining standard options
- Identify and monitor international Phase 2 trials in AML/leukaemia for potential Australian site participation

---

## Supplementary: Full TxGNN Prediction Summary

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Notes |
|------|---------|-------------|----------------|----------------|-------|
| 1 | CMM7 (CDKN2A/CDK4-mutated hereditary melanoma) | 99.37% | L5 | Hold | No clinical or preclinical evidence; no biological rationale linking proteasome inhibition to this genetic subtype |
| 2 | Paediatric leptomeningeal melanoma | 99.30% | L5 | Hold | Blood-brain barrier penetration is a major obstacle; no evidence; paediatric safety concerns |
| 3 | Epithelioid cell uveal melanoma | 99.23% | L5 | Hold | Driven by GNAQ/GNA11 mutations; no mechanistic link to proteasome inhibition |
| 4 | Vulvar melanoma | 99.19% | L5 | Hold | Rare mucosal subtype; minimal BRAF mutations; no supporting evidence |
| 5 | Melanoma (general) | 99.03% | L4 | Research Question | In vitro data in B16-F1 cells; computational modelling; no clinical trials; clinical translation from solid tumours historically poor for proteasome inhibitors |
| 6 | Indolent plasma cell myeloma | 97.94% | L4 | Research Question | Mechanistically related to approved MM indication; smouldering MM biology (low proliferation rate) differs; no RCT supporting early intervention |
| 7 | Intellectual disability, autosomal dominant 55, with seizures | 97.82% | L5 | Hold | Neurodevelopmental genetic disease; no biological rationale; Carfilzomib's known peripheral neuropathy risk is a serious concern in this population |
| **8** | **Myeloid leukemia** | **97.01%** | **L3** | **Proceed with Guardrails** | **Primary focus of this report — strongest evidence among all predictions** |
| 9 | Neutrophil immunodeficiency syndrome | 95.11% | L5 | Hold | No biological rationale; proteasome inhibition could worsen infection susceptibility in an already immunocompromised population |
| 10 | CNS melanocytic neoplasm | 93.29% | L5 | Hold | Blood-brain barrier penetration barrier; no clinical or preclinical evidence |

> **Interpretation note:** High TxGNN scores for ranks 1–4 (melanoma subtypes) likely reflect network proximity within the knowledge graph between melanoma biology and haematological malignancy nodes, rather than true mechanistic plausibility. Score alone should not drive prioritisation; evidence level and biological rationale are more reliable guides for clinical decision-making.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

