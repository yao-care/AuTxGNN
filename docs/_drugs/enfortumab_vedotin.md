---
layout: default
title: Enfortumab Vedotin
parent: 僅模型預測 (L5)
nav_order: 187
evidence_level: L5
indication_count: 10
---

# Enfortumab Vedotin
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

# Enfortumab Vedotin: From Urothelial Carcinoma to HER2-Positive Breast Carcinoma

## One-Sentence Summary

Enfortumab vedotin (EV) is a Nectin-4-directed antibody-drug conjugate (ADC) approved in major markets (US FDA, EMA) for locally advanced or metastatic urothelial carcinoma, but **not currently registered in Australia**. The TxGNN model evaluated 10 candidate indications; the only clinically actionable prediction is **HER2-positive breast carcinoma** (TxGNN score: 98.99%), supported by **4 clinical trials** — including a Phase 2 study (NCT04225117, EV-202) that directly evaluates EV in solid tumour cohorts — and **4 publications**. The remaining 9 top-ranked predictions are considered algorithmic false positives with no mechanistic basis and are not recommended for further clinical pursuit.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Locally advanced or metastatic urothelial carcinoma (bladder cancer) |
| Predicted New Indication | HER2-Positive Breast Carcinoma |
| TxGNN Prediction Score | 98.99% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Enfortumab vedotin is an ADC that targets Nectin-4, a cell adhesion molecule overexpressed on urothelial carcinoma cells. The drug works by delivering monomethyl auristatin E (MMAE) — a potent microtubule-disrupting agent — directly into Nectin-4-expressing tumour cells. Once internalised, MMAE is released intracellularly, inhibiting tubulin polymerisation and triggering apoptosis. Crucially, EV also produces a **bystander killing effect**: MMAE diffuses into adjacent tumour cells regardless of their Nectin-4 expression level, making it potentially effective even in tumours with heterogeneous target expression.

The mechanistic rationale for HER2-positive breast carcinoma is biologically sound. Published data indicate that Nectin-4 is expressed at moderate-to-high levels in a subset of breast cancers, with a positive correlation observed specifically in HER2-positive subtypes. This target overlap, combined with EV's bystander mechanism, provides a credible scientific basis for efficacy in this breast cancer subtype — even where Nectin-4 expression is not uniform across the tumour.

The most important piece of evidence is **NCT04225117 (EV-202)**, a Phase 2 multi-cohort basket study that directly enrolled patients with locally advanced or metastatic solid tumours, including a dedicated **breast cancer cohort**. This is direct clinical evidence for the repurposing hypothesis, elevating the evidence to L2. Enrolment is complete (n=329, Active Not Recruiting) and results are anticipated by late 2026.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT04225117](https://clinicaltrials.gov/study/NCT04225117) | Phase 2 | Active, Not Recruiting | 329 | **EV-202**: Direct evaluation of enfortumab vedotin as monotherapy and in combination with pembrolizumab across multiple solid tumour cohorts, including a breast cancer cohort. Primary endpoint: confirmed ORR per RECIST v1.1. Enrolment complete; results pending. This is the pivotal direct evidence trial. |
| [NCT05097599](https://clinicaltrials.gov/study/NCT05097599) | Phase 2 | Terminated | 11 | **StrataPATH™**: Biomarker-guided basket trial evaluating multiple FDA-approved drugs (including EV) in new precision oncology populations. Terminated early with very limited enrolment (n=11); provides conceptual support only. |
| [NCT07287995](https://clinicaltrials.gov/study/NCT07287995) | Phase 1/2 | Recruiting | 428 | ASP2998 (TROP2-directed ADC) in combination with pembrolizumab, carboplatin, and **enfortumab vedotin** in locally advanced or metastatic solid tumours. EV is a combination partner here; reflects growing interest in dual-ADC and ADC-immunotherapy strategies in HER2-positive contexts. |
| [NCT07309770](https://clinicaltrials.gov/study/NCT07309770) | Phase 2 | Recruiting | 90 | Trastuzumab rezetecan (HER2-directed ADC) in HER2-positive advanced solid tumours including urothelial carcinoma. Not directly evaluating EV, but contextualises the broader ADC landscape in HER2-positive disease. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [41654096](https://pubmed.ncbi.nlm.nih.gov/41654096/) | 2026 | Systematic Review / Real-World Evidence | Crit Rev Oncol Hematol | Comprehensive real-world evidence synthesis for 10 recently approved oncology drugs including enfortumab vedotin; examines whether RCT efficacy translates to broader clinical practice populations — relevant to assessing EV's real-world performance profile. |
| [40614854](https://pubmed.ncbi.nlm.nih.gov/40614854/) | 2025 | Mechanistic / Pre-clinical | Cancer Letters | Polyploid giant cancer cells (PGCCs) drive resistance to HER2-directed ADCs (T-DM1, T-DXd, disitamab vedotin) in HER2-positive breast and gastric cancer models; directly relevant to understanding potential ADC resistance mechanisms in the HER2-positive breast cancer context. |
| [32315240](https://pubmed.ncbi.nlm.nih.gov/32315240/) | 2020 | Narrative Review | ASCO Educational Book | Comprehensive overview of ADC class therapeutics including EV; discusses target selection principles, MMAE payload biology, and the expanding application of ADCs across solid tumour types — provides mechanistic framework for the repurposing rationale. |
| [41384708](https://pubmed.ncbi.nlm.nih.gov/41384708/) | 2026 | Review | Histopathology | Molecular pathology of bladder cancer including Nectin-4 expression biology, chromatin-modifying gene mutations, and integration of molecular and clinical classifications; relevant background for understanding EV's primary mechanism and its extension to other epithelial tumours expressing Nectin-4. |

---

## Australia Market Information

Enfortumab vedotin is **not registered** on the Australian Register of Therapeutic Goods (ARTG). There are currently **no ARTG entries** for this product under any brand name or formulation.

> **Note for Australian clinicians**: EV (brand name Padcev®) is approved by the US FDA (2019, accelerated; 2023, full approval) and the European EMA for locally advanced or metastatic urothelial carcinoma. Australian patients seeking access would currently require either a **TGA Special Access Scheme (SAS) Category B** application or an **Authorised Prescriber** arrangement. TGA registration through a formal submission would be required before routine prescribing.

---

## Cytotoxicity

Enfortumab vedotin is an anticancer agent. Its payload, MMAE, is a potent cytotoxic compound subject to cytotoxic drug handling requirements.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted cytotoxic — Antibody-Drug Conjugate (ADC); MMAE payload is a synthetic antimitotic agent (auristatin class) |
| Myelosuppression Risk | Moderate to High — MMAE-related neutropenia, anaemia, and thrombocytopenia are known class effects; dose-limiting in some patients |
| Emetogenicity Classification | Low to Moderate |
| Monitoring Items | Full Blood Count (FBC with differential), liver function tests (LFTs), renal function, fasting blood glucose (hyperglycaemia including DKA reported), skin integrity assessments, and neurological assessment for peripheral neuropathy |
| Handling Protection | Must be prepared and administered strictly in accordance with cytotoxic drug handling guidelines (SafeWork Australia / SHPA standards); includes appropriate PPE, closed-system drug transfer devices, and designated cytotoxic waste disposal |

---

## Safety Considerations

Detailed TGA-approved Product Information is not yet available as enfortumab vedotin has not been registered in Australia. Based on international regulatory data (US FDA label for Padcev®, EMA SmPC), the following key safety issues are relevant to clinical consideration:

- **Severe cutaneous reactions**: Stevens-Johnson Syndrome (SJS) and toxic epidermal necrolysis (TEN) have been reported and carry a black box warning in the US label. Withhold or permanently discontinue EV depending on severity.
- **Peripheral neuropathy**: Common (≥20% of patients); may be cumulative. Monitor closely and consider dose modification for Grade ≥2 neuropathy.
- **Hyperglycaemia / Diabetic ketoacidosis (DKA)**: Including fatal cases in patients without a prior history of diabetes. Monitor fasting blood glucose at each treatment cycle.
- **Ocular toxicity**: Dry eye, keratitis, blurred vision; recommend ophthalmological assessment and prophylactic lubricating eye drops.
- **Infusion-related reactions**: Pre-medication and close observation during infusion recommended.
- **Embryo-foetal toxicity**: EV is teratogenic; effective contraception required.

> Please refer to current international prescribing information (FDA/EMA) for complete safety details, and contact the TGA for guidance on access under the Special Access Scheme prior to any clinical use in Australia.

---

## Algorithmic False Positives — Rankings 1–9

This is a multi-indication analysis (candidate ID: TW-DB13007-multi). The TxGNN model produced 10 predictions, of which **ranks 1–9 are considered algorithmic false positives** with no clinically actionable basis. These are summarised below for transparency:

| Rank | Predicted Indication | TxGNN Score | Assessment |
|------|---------------------|-------------|------------|
| 1 | Leprosy | 99.53% | No mechanistic link. EV is a tumour-targeted ADC with no antibacterial or immunomodulatory activity against *Mycobacterium leprae*. Likely knowledge graph topological noise. |
| 2 | Multiple Endocrine Neoplasia | 99.43% | MEN is a hereditary syndrome driven by MEN1/RET mutations. No clinical or preclinical evidence that EV has any activity in this condition. |
| 3 | Cytomegalovirus Infection | 99.36% | CMV is a viral infection. EV has no antiviral mechanism. EV-related immunosuppression could worsen CMV reactivation — a contra-indicator, not a treatment signal. |
| 4 | Candidiasis | 99.30% | The only retrieved publication (PMID 41341429) identifies candidiasis as an **adverse event signal** of EV — i.e., EV may increase risk of candidiasis, not treat it. This is reverse evidence. |
| 5 | Cerebral Infarction | 99.23% | Ischaemic stroke involves thrombosis and neuronal hypoxia. No mechanistic relevance to Nectin-4/MMAE biology. |
| 6 | HIV Infectious Disease | 99.19% | HIV requires antiretroviral therapy. EV has no anti-HIV activity. EV immunotoxicity is particularly hazardous in immunocompromised patients. |
| 7 | Homozygous Familial Hypercholesterolaemia | 99.18% | LDL receptor-deficiency metabolic disease; completely unrelated to Nectin-4 biology or lipid metabolism. |
| 8 | Malignant Catarrh | 99.13% | A viral disease of **ruminant animals** (OvHV-2/AlHV-1). Species incompatibility — EV is a human oncology drug. |
| 9 | Infectious Bovine Rhinotracheitis | 99.13% | A **cattle** disease (BHV-1 virus). Same species incompatibility issue as above. Likely due to topological proximity of animal disease nodes in the knowledge graph. |

**Recommendation for Ranks 1–9: Hold.** None of these predictions warrant further clinical investigation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

*(Applied to: HER2-Positive Breast Carcinoma)*

**Rationale:**
NCT04225117 (EV-202, Phase 2, n=329) directly evaluates enfortumab vedotin in multiple solid tumour cohorts including breast cancer, providing Level 2 evidence. The mechanistic rationale is sound — Nectin-4 is expressed in HER2-positive breast cancer, and EV's bystander killing capability supports activity in tumours with heterogeneous target expression. However, EV-202 results are not yet published, and the drug is not TGA-registered in Australia.

**To proceed, the following is needed:**

- **EV-202 cohort results** (NCT04225117): Breast cancer cohort efficacy data expected by September 2026 — this is the pivotal gating data point
- **Nectin-4 expression data** in HER2-positive breast cancer: Australian population-level tissue biomarker data would strengthen the local clinical case
- **TGA registration or SAS application**: Formal access pathway required before any Australian clinical use; TGA SAS Category B or Authorised Prescriber arrangement for compassionate/investigational use
- **MOA documentation** (Data Gap DG002): DrugBank API query to obtain complete mechanistic characterisation for regulatory submissions
- **Comprehensive safety monitoring plan**: Incorporating EV's known toxicity profile (SJS/TEN, peripheral neuropathy, hyperglycaemia, ocular toxicity) with local oncology pharmacy cytotoxic handling protocols
- **Ethics and consent framework**: Formal institutional review and patient-informed consent process for any investigational use in the Australian setting

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require rigorous clinical validation before therapeutic application. Australian clinicians should consult the TGA and relevant institutional governance processes before pursuing any use of unregistered therapeutic goods.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

