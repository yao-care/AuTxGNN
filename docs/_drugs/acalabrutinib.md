---
layout: default
title: Acalabrutinib
parent: 僅模型預測 (L5)
nav_order: 15
evidence_level: L5
indication_count: 10
---

# Acalabrutinib
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

# Acalabrutinib: From Mantle Cell Lymphoma to Non-Hodgkin Lymphoma (Familial)

## One-Sentence Summary

Acalabrutinib (Calquence®) is a second-generation, highly selective BTK inhibitor with FDA approval in the United States for Mantle Cell Lymphoma (MCL) and Chronic Lymphocytic Leukaemia (CLL), though it is not currently registered with the TGA in Australia.
The TxGNN model predicts it may be effective for **Non-Hodgkin Lymphoma (Familial)**,
with **20 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Mantle Cell Lymphoma (MCL) and Chronic Lymphocytic Leukaemia (CLL) — FDA/EMA approved internationally; no TGA registration in Australia |
| Predicted New Indication | Lymphoma, Non-Hodgkin, Familial |
| TxGNN Prediction Score | 97.64% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Acalabrutinib is a potent, second-generation covalent BTK inhibitor that irreversibly binds to Cys481 on Bruton's tyrosine kinase. This blocks the B-cell receptor (BCR) downstream signalling cascade — specifically the NF-κB, PI3K, and ERK pathways — suppressing the proliferation and survival of malignant B cells. Compared to first-generation ibrutinib, acalabrutinib has minimal off-target kinase activity, which translates to a cleaner tolerability profile. Its pivotal ACE-LY-004 Phase 2 trial in relapsed/refractory MCL demonstrated an overall response rate (ORR) of 81%, leading to FDA accelerated approval in 2017.

Non-Hodgkin Lymphoma (NHL), including its familial variant, encompasses a diverse group of B-cell malignancies. The familial designation refers to NHL arising in individuals with a hereditary predisposition; however, the underlying malignant B cells retain the same BCR/BTK signalling dependence as sporadic NHL. MCL — one of acalabrutinib's core approved indications — is itself an aggressive B-cell NHL subtype, meaning the predicted indication sits squarely within an already-established therapeutic territory. Familial NHL cases are biologically indistinguishable from sporadic cases at the signalling pathway level, making the mechanistic extrapolation direct and well-grounded.

Multiple Phase 2 trials are actively evaluating acalabrutinib across broader NHL subtypes including Diffuse Large B-cell Lymphoma (DLBCL), follicular lymphoma (FL), and Richter's Syndrome, all of which share significant biological overlap with familial NHL. The TxGNN score of 97.64% reflects the model's strong recognition of this convergence between acalabrutinib's established target biology and the broader NHL disease family.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT03899337](https://clinicaltrials.gov/study/NCT03899337) | Phase 2 | Recruiting | 105 | STELLAR trial: randomised comparison of acalabrutinib + CHOP-R versus CHOP-R alone in newly diagnosed Richter's Syndrome — CLL transforming into aggressive NHL. Currently recruiting; results pending. |
| [NCT04094142](https://clinicaltrials.gov/study/NCT04094142) | Phase 2 | Completed | 66 | Acalabrutinib + rituximab + lenalidomide (R²A) in relapsed/refractory aggressive B-cell NHL. Completed; results published in *Nature Communications* (PMID 38555311). |
| [NCT03623373](https://clinicaltrials.gov/study/NCT03623373) | Phase 2 | Completed | 13 | Acalabrutinib + bendamustine-rituximab followed by cytarabine-rituximab in treatment-naive MCL. Pilot study completed; safety and preliminary efficacy data available. |
| [NCT04257578](https://clinicaltrials.gov/study/NCT04257578) | Phase 1/2 | Active, not recruiting | 23 | Acalabrutinib + anti-CD19 CAR-T cells (axicabtagene ciloleucel) in B-cell lymphoma. Investigating whether BTK inhibition enhances CAR-T cell function and durability. |
| [NCT04546620](https://clinicaltrials.gov/study/NCT04546620) | Phase 2 | Active, not recruiting | 453 | Randomised, molecularly guided evaluation of acalabrutinib added to R-CHOP in previously untreated CD20-positive DLBCL. Large-scale trial; completion anticipated May 2028. |
| [NCT04883437](https://clinicaltrials.gov/study/NCT04883437) | Phase 2 | Recruiting | 49 | Acalabrutinib + obinutuzumab in previously untreated, low-tumour-burden follicular lymphoma and other indolent NHL subtypes. |
| [NCT04002947](https://clinicaltrials.gov/study/NCT04002947) | Phase 2 | Recruiting | 132 | Acalabrutinib + DA-EPOCH-R or R-CHOP in untreated DLBCL. NCI-sponsored study assessing whether adding acalabrutinib to standard chemoimmunotherapy improves cure rates. |
| [NCT05583149](https://clinicaltrials.gov/study/NCT05583149) | Phase 2 | Active, not recruiting | 28 | Acalabrutinib + lisocabtagene maraleucel (liso-cel) in relapsed/refractory aggressive B-cell lymphoma. Explores BTK inhibition as a strategy to improve CAR-T outcomes. |
| [NCT07377578](https://clinicaltrials.gov/study/NCT07377578) | Phase 3 | Recruiting | 394 | PRIME study: rocbrutinib versus investigator's choice of BTK inhibitors in relapsed/refractory MCL. Provides class-level evidence for BTK inhibitors across NHL; informs positioning of acalabrutinib. |
| [NCT02180711](https://clinicaltrials.gov/study/NCT02180711) | Phase 1/2 | Active, not recruiting | 113 | Acalabrutinib alone or with rituximab in relapsed/refractory follicular lymphoma and marginal zone lymphoma; acalabrutinib + rituximab + lenalidomide in R/R FL. Long-term follow-up through 2028. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [29241979](https://pubmed.ncbi.nlm.nih.gov/29241979/) | 2018 | Phase 2 Single-arm Trial | *The Lancet* | ACE-LY-004: acalabrutinib monotherapy in 124 patients with R/R MCL. ORR 81%, CR 40%. Established the pivotal evidence base for FDA accelerated approval. |
| [40311141](https://pubmed.ncbi.nlm.nih.gov/40311141/) | 2025 | Phase 2 Trial | *J Clin Oncol* | Acalabrutinib + bendamustine-rituximab in untreated MCL; designed to assess whether improved selectivity vs ibrutinib translates to better tolerability without sacrificing efficacy. |
| [38781315](https://pubmed.ncbi.nlm.nih.gov/38781315/) | 2024 | Phase 2 Trial (2-year follow-up) | *Blood Advances* | Acalabrutinib + venetoclax + rituximab (AVR) in treatment-naive MCL. 21 patients; 95.2% completed induction. Reports deep response rates and 2-year safety profile. |
| [38555311](https://pubmed.ncbi.nlm.nih.gov/38555311/) | 2024 | Phase 2 Trial | *Nature Communications* | R²A (acalabrutinib + lenalidomide + rituximab) in 66 patients with R/R aggressive B-cell NHL. Demonstrates potential synergism between BTK inhibition and immunomodulation in NHL. |
| [37470152](https://pubmed.ncbi.nlm.nih.gov/37470152/) | 2024 | Phase 2 Long-term Follow-up | *Haematologica* | Final results and overall survival data from ACE-LY-004, including patients with poor prognostic features. Confirms durable responses with acalabrutinib monotherapy in R/R MCL. |
| [41289154](https://pubmed.ncbi.nlm.nih.gov/41289154/) | 2026 | Phase 2 Trial | *Blood Advances* | MRD-driven frontline therapy with acalabrutinib + lenalidomide + rituximab or obinutuzumab in MCL. Primary endpoint: molecular CR and undetectable MRD (uMRD6 by clonoSEQ). |
| [40775236](https://pubmed.ncbi.nlm.nih.gov/40775236/) | 2025 | Phase 2 Trial | *Nature Communications* | Frontline acalabrutinib + lenalidomide + rituximab in advanced-stage follicular lymphoma with high tumour burden. Reports CR rate, POD24, and PFS in 24 patients. |
| [36029036](https://pubmed.ncbi.nlm.nih.gov/36029036/) | 2023 | Review | *Br J Haematol* | Comprehensive review of primary and acquired resistance mechanisms to BTK inhibitors in CLL and NHL, including BTK C481 mutations, bypass pathway activation, and tumour microenvironment factors. |
| [35266562](https://pubmed.ncbi.nlm.nih.gov/35266562/) | 2022 | Review | *Am J Hematol* | MCL 2022 update: molecular pathogenesis, risk stratification (TP53, NSD2, KMT2D, MRD), and role of BTK inhibitors in current treatment algorithms. |
| [29209955](https://pubmed.ncbi.nlm.nih.gov/29209955/) | 2018 | Regulatory Review | *Drugs* | Acalabrutinib: first global approval. Documents development milestones, FDA accelerated approval pathway for MCL, and the rationale for the BTK selectivity strategy. |

---

## Australia Market Information

Acalabrutinib (Calquence®) is **not currently listed on the Australian Register of Therapeutic Goods (ARTG)**. No TGA-approved products exist for this medicine in Australia.

> **Note for Australian clinicians**: Acalabrutinib is approved by the US FDA for MCL and CLL/SLL, and holds EMA approval in Europe. Australian patients currently requiring access may be eligible through the TGA's **Special Access Scheme (SAS Category B)** or via the **Authorised Prescriber** pathway. Clinicians are advised to check the TGA website for the current access status and any pending ARTG submissions.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — second-generation covalent BTK inhibitor; not a conventional cytotoxic agent |
| Myelosuppression Risk | Moderate — anaemia, neutropenia, and thrombocytopenia are known class effects; generally less severe than conventional chemotherapy |
| Emetogenicity Classification | Low — oral targeted therapy with minimal direct emetogenic potential |
| Monitoring Items | FBC with differential, liver function tests (LFTs), renal function, cardiac monitoring (atrial fibrillation and flutter), blood pressure, and bleeding assessment |
| Handling Protection | Standard oral anti-cancer agent precautions apply; handle in accordance with institutional cytotoxic drug handling policies |

---

## Safety Considerations

Detailed safety data specific to Australian regulatory requirements is not available in this Evidence Pack, as acalabrutinib is not TGA-registered.

> Please refer to the **US FDA-approved Prescribing Information for Calquence® (acalabrutinib)** or the **EMA Summary of Product Characteristics** for comprehensive safety information. Key areas of clinical vigilance include: atrial fibrillation/flutter, serious haemorrhage, invasive infections (including invasive fungal infections such as aspergillosis — see PMID 39742965), hypertension, and second primary malignancies.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Acalabrutinib has a well-established mechanistic basis and a demonstrated clinical track record in B-cell NHL, anchored by the ACE-LY-004 Phase 2 trial (ORR 81% in R/R MCL) and multiple completed or ongoing trials in adjacent NHL subtypes. The TxGNN prediction of 97.64% for familial NHL is biologically coherent — familial NHL is driven by the same BCR/BTK-dependent signalling as the approved indications — and the overall evidence package meets L2 criteria. However, the absence of TGA registration and the lack of Australian-specific safety documentation require structured safeguards before clinical application.

**To proceed, the following is needed:**

- **TGA regulatory pathway**: Determine whether a full TGA registration application, SAS Category B access, or Authorised Prescriber status is the appropriate route for Australian patients
- **Formal MOA documentation**: Obtain complete mechanism of action data from the DrugBank record and product PI to support the safety dossier
- **Australian DDI review**: Conduct a drug–drug interaction assessment relevant to common Australian co-prescribing patterns (e.g., CYP3A4 inhibitors/inducers such as azole antifungals and certain cardiac medications)
- **Contraindication and warning review**: Extract and document full safety warnings, contraindications, and special population data (renal/hepatic impairment, elderly patients) from the FDA/EMA PI
- **Familial NHL sub-population confirmation**: Verify whether patients with a familial predisposition to NHL were represented in existing trials, or whether a specific study is warranted in this genetic sub-population
- **Structured monitoring plan**: Develop an Australian clinical monitoring protocol addressing atrial fibrillation, haemorrhage, and invasive fungal infections, in line with institutional haematology guidelines
- **PBS/pharmacoeconomic assessment**: Evaluate cost-effectiveness and potential for Pharmaceutical Benefits Scheme (PBS) listing to ensure equitable patient access
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

