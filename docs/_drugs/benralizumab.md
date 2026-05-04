---
layout: default
title: Benralizumab
parent: 僅模型預測 (L5)
nav_order: 78
evidence_level: L5
indication_count: 10
---

# Benralizumab
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

# Benralizumab: From Severe Eosinophilic Asthma to Atopic Dermatitis

> ⚠️ **Disclaimer**: This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application.

---

## One-Sentence Summary

Benralizumab (Fasenra®) is a monoclonal antibody targeting the interleukin-5 receptor alpha (IL-5Rα), approved internationally as add-on maintenance treatment for severe eosinophilic asthma. The TxGNN model predicts it may be effective for **Atopic Dermatitis (Dermatitis)**, with **6 clinical trials** and **20 publications** identified in this direction — however, the pivotal Phase 2 randomised controlled trial (HILLIER study, n=194) was terminated early, and published results confirmed no significant efficacy in an unselected atopic dermatitis population, indicating that patient stratification by eosinophilic phenotype is likely critical.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Severe eosinophilic asthma (international approvals; not registered in Australia) |
| Predicted New Indication | Dermatitis (Atopic Dermatitis) |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The mechanistic rationale for benralizumab in atopic dermatitis (AD) is biologically coherent and well-grounded. Benralizumab binds with high affinity to IL-5Rα and, through antibody-dependent cell-mediated cytotoxicity (ADCC), achieves near-complete and rapid depletion of eosinophils and basophils. In AD, eosinophils are established central effectors of Type 2 (Th2) inflammation: IL-5 drives their differentiation and survival in bone marrow, and activated eosinophils infiltrate AD skin lesions to release potent inflammatory mediators including major basic protein (MBP), eosinophil cationic protein (ECP), IL-4, and IL-13. Basophils similarly contribute as an abundant early source of IL-4. The pharmacological logic of targeting IL-5Rα in AD is therefore mechanistically sound and clearly distinct from a purely speculative prediction.

The connection between benralizumab's approved indication (severe eosinophilic asthma) and atopic dermatitis is strong from an immunological standpoint: both are Th2-polarised atopic diseases sharing the same core inflammatory axis (IL-4, IL-5, IL-13, IgE), and both belong to the "atopic march" spectrum. Elevated blood and tissue eosinophilia is prominent in both conditions. TxGNN's knowledge graph appropriately identifies this mechanistic adjacency, reflected in its high prediction score of 99.16%.

However, the clinical evidence tells a more complex story. The HILLIER Phase 2 RCT (NCT04605094, n=194) was terminated early due to lack of primary efficacy, and the published results in JEADV (PMID 37178404) confirmed that benralizumab does not significantly improve signs or symptoms of moderate-to-severe AD in an unselected patient population. Despite this, 2025 translational data (PMID 40781582) confirmed that benralizumab does deplete IL-5Rα-bearing cells within AD skin lesions, demonstrating clear pharmacodynamic proof of concept. This dissociation between target engagement and clinical response strongly suggests that the issue lies in **patient selection rather than mechanism**: eosinophil-high AD subpopulations and related eosinophil-driven skin conditions — such as Drug Reaction with Eosinophilia and Systemic Symptoms (DRESS, NCT06734884) — may represent more appropriate and higher-probability targets for this agent.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04605094](https://clinicaltrials.gov/study/NCT04605094) | Phase 2 | Terminated | 194 | **HILLIER study** — Multicentre, randomised, double-blind, placebo-controlled RCT of benralizumab in moderate-to-severe atopic dermatitis. Early termination is a decisive negative signal; published results (PMID 37178404) confirmed lack of efficacy on disease signs and symptoms in an unselected population. The most critical data point for this repurposing indication. |
| [NCT03563066](https://clinicaltrials.gov/study/NCT03563066) | Phase 2 | Completed | 20 | Proof-of-concept study of benralizumab in atopic dermatitis, examining eosinophil, basophil, and ILC2 depletion in skin lesions. Provides mechanistic evidence of target engagement in skin tissue; underpowered to evaluate clinical outcomes. |
| [NCT06734884](https://clinicaltrials.gov/study/NCT06734884) | Phase 2 | Not Yet Recruiting | 96 | Benralizumab in Drug Reaction with Eosinophilia and Systemic Symptoms (DRESS) — a rare, severe eosinophil-driven skin reaction with no established standard treatment. Mechanistic fit stronger than for broad AD. Planned start January 2025; completion September 2029. |
| [NCT04126499](https://clinicaltrials.gov/study/NCT04126499) | Observational | Completed | 28 | Retrospective observational study of benralizumab in severe eosinophilic asthma (Spanish individualised access programme). Provides real-world safety context and patient characteristics; indirectly relevant to dermatology comorbidities. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37178404](https://pubmed.ncbi.nlm.nih.gov/37178404/) | 2023 | Phase 2 RCT — Negative | Journal of the European Academy of Dermatology and Venereology | **Critical**: Benralizumab showed no significant improvement in signs and symptoms of moderate-to-severe AD (HILLIER trial primary outcome). Primary negative finding for broad atopic dermatitis indication. |
| [38695680](https://pubmed.ncbi.nlm.nih.gov/38695680/) | 2024 | Phase 2 Trial Summary | Immunotherapy | Plain-language summary of the HILLIER study confirming negative efficacy outcomes in the unselected moderate-to-severe AD population. |
| [40781582](https://pubmed.ncbi.nlm.nih.gov/40781582/) | 2025 | Mechanistic / Translational | Clinical and Translational Allergy | Benralizumab depletes IL-5Rα-bearing cells in AD skin lesions — pharmacodynamic proof of concept confirming direct target engagement in skin tissue despite the negative HILLIER clinical outcome. Key finding for hypothesis refinement. |
| [39234416](https://pubmed.ncbi.nlm.nih.gov/39234416/) | 2024 | Mechanistic Study | The Journal of Allergy and Clinical Immunology: Global | Effect of benralizumab on skin inflammation after intradermal allergen challenge in patients with moderate-to-severe AD; supports biological activity in the cutaneous compartment. |
| [39600395](https://pubmed.ncbi.nlm.nih.gov/39600395/) | 2024 | Systematic Review / Clinical Update | Allergologie Select | Comprehensive update on biologics for atopic diseases, urticaria, and angioedema, including benralizumab; contextualises benralizumab within the current therapeutic landscape and emerging competing agents. |
| [36355314](https://pubmed.ncbi.nlm.nih.gov/36355314/) | 2023 | Review | Dermatology and Therapy | Safety of combining dupilumab with other monoclonal antibodies including benralizumab; relevant for patients with overlapping atopic comorbidities requiring dual biologic therapy. |
| [36411004](https://pubmed.ncbi.nlm.nih.gov/36411004/) | 2023 | Narrative Review | Immunology and Allergy Clinics of North America | Biologics including benralizumab in women with allergic diseases (asthma, rhinitis, AD) during pregnancy and lactation; safety overview for special populations. |
| [35987486](https://pubmed.ncbi.nlm.nih.gov/35987486/) | 2022 | Safety Review | The Journal of Allergy and Clinical Immunology: In Practice | Safety of benralizumab (among 7 FDA-approved biologics) in atopic diseases during pregnancy; covers maternal and fetal outcomes across published case series and registry data. |
| [31690400](https://pubmed.ncbi.nlm.nih.gov/31690400/) | 2019 | Narrative Review | Allergy and Asthma Proceedings | Anti-IL-5 biologics (mepolizumab, reslizumab, benralizumab) reviewed for severe asthma, atopic dermatitis, and chronic urticaria; provides the pre-HILLIER rationale for cross-indication use. |
| [36270814](https://pubmed.ncbi.nlm.nih.gov/36270814/) | 2023 | Case Report (Adverse Event) | Therapie | Benralizumab-induced **interstitial granulomatous dermatitis** — a paradoxical cutaneous adverse reaction. Particularly important for clinicians considering this agent in dermatological settings; highlights a potential treatment-related cutaneous risk. |

---

## Australia Market Information

Benralizumab is **not currently registered** on the Australian Register of Therapeutic Goods (ARTG). There are no ARTG entries for this medicine.

Benralizumab is available internationally as **Fasenra®** (AstraZeneca/Kyowa Kirin) and is approved in multiple jurisdictions — including the United States (FDA, 2017), European Union (EMA, 2018), and Japan (PMDA) — for the add-on maintenance treatment of severe eosinophilic asthma in adults.

Australian healthcare professionals wishing to access this medicine for approved or unapproved indications should consider:
- **TGA Special Access Scheme (SAS) Category B** — for individual patients with unmet clinical need
- **TGA Authorised Prescriber** pathway — for clinicians wishing to treat a class of patients on an ongoing basis

---

## Safety Considerations

No Australian TGA-approved Product Information (PI) is currently available, as benralizumab is not registered in Australia. Please refer to the international **Fasenra® Product Information** (available from AstraZeneca or the FDA/EMA labelling) for comprehensive prescribing information.

A safety signal of particular relevance to dermatological use: a published case report (PMID 36270814, 2023) documented **benralizumab-induced interstitial granulomatous dermatitis** — a paradoxical cutaneous adverse reaction — which clinicians should be aware of when considering use in patients with skin conditions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pivotal Phase 2 HILLIER RCT (NCT04605094, n=194) was terminated early, and published results confirmed no clinically meaningful benefit of benralizumab in an unselected moderate-to-severe atopic dermatitis population — representing a decisive negative signal for broad use in this indication. Although pharmacodynamic proof of concept (eosinophil depletion in skin lesions) has been confirmed, this has not translated into clinical efficacy in the general AD population. The drug is also not registered in Australia, and no TGA-approved Product Information is available.

**To proceed, the following is needed:**

- **Patient stratification analysis**: Examination of the HILLIER trial dataset for treatment response in patients with high baseline blood eosinophil counts (≥300 cells/μL) or confirmed tissue eosinophilia — the subgroup most likely to benefit from IL-5Rα blockade
- **DRESS indication monitoring**: Await results from NCT06734884 (benralizumab in DRESS), which represents a stronger mechanistic fit and may define a clinically viable, niche use case
- **Biomarker-driven trial design**: Any future investigator-initiated trial should incorporate pre-specified eosinophil count thresholds and skin biopsy endpoints as response-predictive biomarkers
- **TGA regulatory pathway**: Initiate SAS Category B application or TGA registration assessment if use in a specific Australian patient cohort is clinically justified
- **Full safety review**: Comprehensive review of international Fasenra® PI for warnings, contraindications (including helminth infection risk), and special population considerations prior to any off-label use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

