---
layout: default
title: Dimethyl Fumarate
parent: 僅模型預測 (L5)
nav_order: 157
evidence_level: L5
indication_count: 10
---

# Dimethyl Fumarate
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

# Dimethyl Fumarate: From Relapsing-Remitting Multiple Sclerosis to Progressive Multiple Sclerosis

## One-Sentence Summary

Dimethyl fumarate (DMF, known internationally as Tecfidera®) is an oral disease-modifying therapy with established immunomodulatory and neuroprotective properties, approved in multiple countries for the treatment of relapsing-remitting multiple sclerosis (RRMS).
The TxGNN model predicts it may be effective for **Progressive Multiple Sclerosis**, with **18 clinical trials** and **19 publications** currently supporting this direction.
Notably, one completed Phase 2 randomised controlled trial (NCT02959658) has directly investigated DMF in primary progressive MS, placing the evidence at **Level L2**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Relapsing-Remitting Multiple Sclerosis (RRMS) — based on international regulatory approvals reflected in evidence pack literature |
| Predicted New Indication | Progressive Multiple Sclerosis |
| TxGNN Prediction Score | 90.67% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack. Based on known pharmacological information referenced in the evidence pack's repurposing rationale, DMF (and its primary active metabolite monomethyl fumarate/MMF) acts through two key pathways: activation of the Nrf2/ARE (Nuclear factor erythroid 2-related factor 2/Antioxidant Response Element) pathway, which reduces oxidative stress damage and provides neuroprotection to neural tissue; and inhibition of NF-κB signalling, which suppresses pro-inflammatory cytokine production and attenuates neuroinflammation. DMF also consistently produces immunomodulatory effects, including reductions in certain T-cell and B-cell subsets that drive autoimmune activity in MS.

Both RRMS and progressive MS (encompassing primary progressive MS [PPMS] and secondary progressive MS [SPMS]) share the core pathological features of neuroinflammation and demyelination, with the progressive forms additionally characterised by greater neurodegeneration and ongoing axonal loss. Historically, disease-modifying therapies have shown stronger efficacy in the relapsing than the progressive phase; however, the chronic inflammatory component that persists — particularly in active SPMS and PPMS — remains a plausible therapeutic target for DMF's anti-inflammatory and Nrf2-mediated neuroprotective mechanisms. The mechanistic overlap with the approved RRMS indication is therefore high, with the primary difference being the relatively greater contribution of neurodegeneration in progressive forms.

The repurposing rationale is directly supported by clinical investigation beyond modelling alone. NCT02959658 was a completed randomised, placebo-controlled Phase 2 trial of DMF specifically in PPMS (published as PMID 34429340), with a subsequent open-label extension reporting longer-term observations (PMID 36586351). A real-world cohort study (PMID 33996142) has also assessed DMF safety and effectiveness specifically in the progressive MS population. This places the prediction on substantially firmer ground than a purely model-driven candidate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT02959658](https://clinicaltrials.gov/study/NCT02959658) | Phase 2 | Completed | 54 | Randomised, double-blind, placebo-controlled trial of DMF directly in primary progressive MS (PPMS). Primary endpoint was reduction in CSF neurofilament light chain concentration. Most directly relevant evidence for this indication; published results available (PMID 34429340). |
| [NCT02430532](https://clinicaltrials.gov/study/NCT02430532) | Phase 3 | Terminated | 58 | Phase 3 RCT of DMF (BG00012) vs placebo in secondary progressive MS (SPMS), targeting disability accumulation not related to relapses. Terminated early with only 58 of planned participants enrolled; early termination limits interpretability. |
| [NCT02683863](https://clinicaltrials.gov/study/NCT02683863) | Phase 4 | Completed | 20 | Open-label PK/biomarker study in SPMS patients assessing whether DMF or MMF penetrates the CNS by measuring drug concentrations in cerebrospinal fluid — directly relevant to assessing neuroprotective potential in progressive disease. |
| [NCT03092544](https://clinicaltrials.gov/study/NCT03092544) | Phase 4 | Unknown | 57 | Investigates indirect neuroprotective mechanisms of Tecfidera® (DMF) in both RRMS and progressive MS patients, including gut microbiome analysis. Direct mechanistic relevance to progressive MS; status requires confirmation. |
| [NCT03535298](https://clinicaltrials.gov/study/NCT03535298) | Phase 4 | Active, not recruiting | 800 | DELIVER-MS: Compares early intensive vs escalation DMT strategies in RRMS; DMF is one of the escalation-arm comparator therapies. Provides real-world treatment outcome data applicable to treatment strategy decisions. |
| [NCT03193866](https://clinicaltrials.gov/study/NCT03193866) | N/A (Observational) | Completed | 3,526 | COMBAT-MS: Large real-world comparative effectiveness study of rituximab vs multiple DMTs including DMF across relapsing MS subtypes. Completed 2022; largest observational safety/efficacy dataset including DMF. |
| [NCT07138833](https://clinicaltrials.gov/study/NCT07138833) | Phase 4 | Not yet recruiting | 50 | Open-label multicentre study of DMF enteric-coated capsules in relapsing MS (RMS), which per 2017 McDonald criteria explicitly includes active SPMS — broadens the applicable patient population for efficacy data. |
| [NCT02739542](https://clinicaltrials.gov/study/NCT02739542) | Phase 4 | Completed | 87 | ARISE: Randomised trial of Tecfidera® (DMF) in radiologically isolated syndrome to delay first clinical attack; supports the neuroprotective hypothesis underlying the progressive MS rationale. |
| [NCT03500328](https://clinicaltrials.gov/study/NCT03500328) | N/A | Active, not recruiting | 900 | TREAT-MS: Pragmatic trial evaluating early aggressive vs escalation therapy in MS; DMF used as a reference comparator, providing indirect safety and effectiveness context in long-term disability outcomes. |
| [NCT04260711](https://clinicaltrials.gov/study/NCT04260711) | N/A | Unknown | 130 | DOT-MS: Assesses whether safely discontinuing first-line DMTs (including DMF) is possible in stable relapsing MS; disability progression and quality of life are secondary endpoints of relevance. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [34429340](https://pubmed.ncbi.nlm.nih.gov/34429340/) | 2021 | RCT | *Neurol Neuroimmunol Neuroinflamm* | Primary results of the Phase 2 placebo-controlled RCT of DMF in PPMS. Primary endpoint (CSF neurofilament light chain reduction) was not met; however, the trial established safety feasibility and provided exploratory efficacy data in this population. |
| [36586351](https://pubmed.ncbi.nlm.nih.gov/36586351/) | 2023 | Open-label extension | *Mult Scler Relat Disord* | Open-label extension of NCT02959658; longer-term observations in PPMS patients treated with DMF, including exploratory biomarker and clinical outcomes beyond the placebo-controlled phase. |
| [33996142](https://pubmed.ncbi.nlm.nih.gov/33996142/) | 2021 | Real-world cohort | *Mult Scler J Exp Transl Clin* | Real-world safety and effectiveness analysis of DMF specifically in the progressive MS population; highlights the limited evidence base and characterises the effectiveness signal in this underserved group. |
| [34465252](https://pubmed.ncbi.nlm.nih.gov/34465252/) | 2022 | Long-term extension | *Mult Scler* | ENDORSE study: Up to 13 years of DMF safety and efficacy data in RRMS (n included from DEFINE/CONFIRM). Key long-term safety resource covering lymphopenia trends, infection events, and sustained clinical outcomes. |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | Network meta-analysis | *Cochrane Database Syst Rev* | Updated Cochrane network meta-analysis of immunomodulators and immunosuppressants for RRMS; contextualises DMF's comparative benefit-risk within the full armamentarium of available DMTs. |
| [29686116](https://pubmed.ncbi.nlm.nih.gov/29686116/) | 2018 | Clinical practice guideline | *Neurology* | AAN practice guideline recommendations for DMT use in adults with MS, including specific guidance on progressive forms; provides authoritative treatment selection framework. |
| [35182510](https://pubmed.ncbi.nlm.nih.gov/35182510/) | 2022 | Cohort study | *Lancet Neurol* | Validates serum neurofilament light chain (sNfL) as an individual-level prognostic biomarker for MS disease activity; directly relevant to monitoring DMF treatment response in progressive MS at the patient level. |
| [33091427](https://pubmed.ncbi.nlm.nih.gov/33091427/) | 2021 | Review | *Pharmacol Ther* | Comprehensive review of DMF-induced lymphopenia in MS: molecular mechanisms driving lymphocyte depletion, risk stratification criteria, and clinical implications for PML surveillance. Essential safety reference. |
| [32808554](https://pubmed.ncbi.nlm.nih.gov/32808554/) | 2022 | Case series / Safety report | *Mult Scler* | Detailed clinical characteristics of nine PML cases in DMF-treated MS patients; estimates PML incidence at 0.02 per 1,000 patients. Identifies severe, persistent lymphopenia as the primary risk factor. |
| [27433310](https://pubmed.ncbi.nlm.nih.gov/27433310/) | 2016 | Review | *Ther Adv Chronic Dis* | Review of DMF in MS after more than 2 years of real-world use across >190,000 patients; covers clinical efficacy, tolerability profile, and patient selection considerations including monitoring parameters. |

---

## Australia Market Information

Dimethyl fumarate is **not currently registered on the Australian Register of Therapeutic Goods (ARTG)**. No ARTG entries exist as of the data cutoff (April 2026).

> **Note for clinicians**: Should access be sought for individual patients, the TGA Special Access Scheme (SAS) or Authorised Prescriber pathway may apply. In the interim, the US FDA-approved prescribing information for Tecfidera® (dimethyl fumarate delayed-release capsules 120 mg and 240 mg) and the EMA-approved Summary of Product Characteristics are available as reference sources for dosing, safety monitoring, and contraindications.

---

## Safety Considerations

No structured safety data (key warnings, contraindications, or drug interactions) is available from the current evidence pack for the Australian regulatory context.

Based on the clinical literature reviewed, the following safety signals are clinically significant and require proactive management:

- **Progressive multifocal leukoencephalopathy (PML)**: A rare but potentially fatal opportunistic CNS infection caused by JC virus reactivation. Estimated incidence in DMF-treated MS patients is 0.02 per 1,000 patients (PMID 32808554). Risk is predominantly associated with severe, sustained lymphopenia.
- **Lymphopenia**: DMF consistently reduces total lymphocyte counts. Severe lymphopenia (Grade 3, <500 cells/mm³) persisting beyond 6 months significantly elevates PML risk and requires dose interruption or discontinuation (PMID 33091427).

Please refer to the internationally approved prescribing information (FDA or EMA PI for Tecfidera®) for complete safety information, including full contraindications, precautions, and drug interactions until an Australian PI becomes available.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 randomised controlled trial (NCT02959658 / PMID 34429340) directly investigated DMF in primary progressive MS, and a real-world cohort study (PMID 33996142) has additionally characterised its use in progressive MS — together representing Level L2 evidence with a mechanistic rationale closely aligned to the approved RRMS indication. Although the primary endpoint of NCT02959658 was not met, the mechanistic basis (Nrf2-mediated neuroprotection, NF-κB-mediated anti-inflammatory effects) and the established long-term safety profile in RRMS provide a reasonable foundation for pursuing this indication under careful clinical governance.

**To proceed, the following is needed:**

- **TGA registration or access pathway**: DMF is not ARTG-registered; a TGA registration application, Special Access Scheme (SAS Category B or C), or Authorised Prescriber designation would be required before clinical use in Australia.
- **Complete safety data review**: Obtain and review the full international prescribing information (FDA/EMA-approved PI for Tecfidera®) covering contraindications, drug-drug interactions, and pregnancy/lactation categories.
- **Lymphopenia and PML monitoring protocol**: Establish a standardised lymphocyte monitoring plan (e.g., full blood count with differential at baseline, 3 months, 6 months, then every 6–12 months) with pre-defined thresholds for dose modification and JC virus antibody testing.
- **Specialist MS neurologist input**: Engage a neurologist with MS expertise to assess patient-level suitability and to distinguish between active SPMS (which overlaps with the US FDA's approved "relapsing forms of MS" indication) and non-active PPMS where the evidence is weaker.
- **Detailed review of Phase 2 PPMS trial secondary and exploratory endpoints**: Given the primary endpoint was not met, a thorough assessment of MRI lesion activity, disability progression, and CSF biomarker data from NCT02959658 and its open-label extension (PMID 36586351) is warranted before committing to clinical use in PPMS specifically.

---

*This report is for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation prior to therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

