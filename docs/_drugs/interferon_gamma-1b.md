---
layout: default
title: Interferon Gamma-1B
parent: 僅模型預測 (L5)
nav_order: 269
evidence_level: L5
indication_count: 10
---

# Interferon Gamma-1B
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

# Interferon gamma-1b: From Chronic Granulomatous Disease to Heart Disease

## One-Sentence Summary

Interferon gamma-1b (Actimmune®) is a recombinant human Type II interferon approved internationally for chronic granulomatous disease (CGD) and severe malignant osteopetrosis, but is **not registered with the TGA or marketed in Australia**.
The TxGNN model predicts potential relevance to **Heart Disease** with a score of **99.99%**, however the retrieved evidence — 50 clinical trials and 5 publications — contains no studies directly testing interferon gamma-1b as a cardiac treatment.
Evidence is classified as **L4** (mechanistic rationale only), and the recommended decision is **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic Granulomatous Disease (CGD) and severe malignant osteopetrosis (international approval only — not TGA registered) |
| Predicted New Indication | Heart Disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 (mechanistic/indirect — no direct cardiac trials) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on published international literature, interferon gamma-1b is a recombinant form of the endogenous human Type II interferon. It activates macrophages and phagocytes, enhances intracellular killing of pathogens (including catalase-positive organisms), and modulates both innate and adaptive immune responses. Its proven efficacy in CGD derives from restoring deficient NADPH oxidase function and augmenting neutrophil respiratory burst activity.

The mechanistic rationale for heart disease operates through two indirect pathways. First, IFN-gamma has well-documented **anti-fibrotic properties**: it inhibits TGF-β signalling, suppresses fibroblast proliferation, and reduces collagen synthesis — mechanisms theoretically relevant to cardiac fibrosis underlying dilated cardiomyopathy or diastolic dysfunction. Second, in the CGD setting where IFN-gamma-1b is already approved, cardiac infectious complications — including constrictive Aspergillus pericarditis and prosthetic valve endocarditis with organisms such as *Mycobacterium chimaera* — are documented disease manifestations, providing indirect real-world exposure to cardiac-adjacent use. Friedreich ataxia hypertrophic cardiomyopathy represents a third speculative pathway, as IFN-gamma promotes frataxin expression in preclinical FRDA models.

**A critical safety concern must be acknowledged upfront:** IFN-gamma can also activate Th1 pro-inflammatory pathways in cardiac tissue, and immune-mediated myocarditis has been documented in interferon therapy contexts. The net effect on cardiac tissue — anti-fibrotic benefit versus pro-inflammatory toxicity — has not been characterised in any prospective cardiac trial. The TxGNN prediction likely reflects network connectivity through CGD-cardiac complication and FRDA pathways rather than direct cardiac efficacy evidence.

---

## Clinical Trial Evidence

> ⚠️ **Important:** None of the 50 retrieved clinical trials directly test interferon gamma-1b for a heart disease indication. All trials were assessed as Grade C (irrelevant to this drug–disease pair). The most contextually informative trials are listed below for background only.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03888664](https://clinicaltrials.gov/study/NCT03888664) | Phase 2 | Completed | 12 | Open-label pilot of γIFN (interferon gamma-1b) in Friedreich ataxia (FRDA). IFN-gamma promotes frataxin expression in vitro and in vivo. FRDA involves hypertrophic cardiomyopathy as a major manifestation — most directly relevant cardiac-adjacent trial using the actual study drug. |
| [NCT02948426](https://clinicaltrials.gov/study/NCT02948426) | Phase 1 | Terminated | 18 | Intraperitoneal autologous monocytes stimulated ex vivo with Actimmune® (interferon gamma-1b) and Sylatron in recurrent ovarian cancer. Directly uses interferon gamma-1b; trial was terminated. Demonstrates feasibility and safety signals for the drug, though no cardiac indication. |
| [NCT05463133](https://clinicaltrials.gov/study/NCT05463133) | Phase 1/2 | Recruiting | 50 | Allogeneic haematopoietic stem cell transplant for CGD with alemtuzumab/busulfan conditioning combined with IL-6 ± IFN-gamma antagonists. Relevant to CGD — the approved indication for IFN-gamma-1b — and CGD patients experience cardiac complications including pericarditis. |
| [NCT01739777](https://clinicaltrials.gov/study/NCT01739777) | Phase 1/2 | Completed | 30 | Umbilical cord mesenchymal stem cells by intravenous infusion in dilated cardiomyopathy heart failure. Tests cell-based immune therapy in a cardiac indication; demonstrates proof-of-concept for immune-modulation in heart failure, but does not use IFN-gamma-1b. |
| [NCT00201123](https://clinicaltrials.gov/study/NCT00201123) | Phase 2 | Completed | 89 | IFN-gamma modulation of pulmonary immune response to *Mycobacterium tuberculosis* in HIV/AIDS patients. Directly tests IFN-gamma administration in humans; provides in-human safety and pharmacodynamic context for the study drug. |

---

## Literature Evidence

> **Note:** The 5 retrieved publications are contextually indirect. None report IFN-gamma-1b tested specifically for heart disease as a primary endpoint.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [28990950](https://pubmed.ncbi.nlm.nih.gov/28990950/) | 2017 | Case Report | Turk Kardiyoloji Dernegi Arsivi | CGD child developed constrictive Aspergillus pericarditis with congestive heart failure, managed with pericardiectomy. Illustrates cardiac infectious complications in the CGD population where IFN-gamma-1b is the approved prophylactic therapy. |
| [31020218](https://pubmed.ncbi.nlm.nih.gov/31020218/) | 2018 | Case Report | European Heart Journal Case Reports | First Spanish report of healthcare-associated *M. chimaera* prosthetic valve infective endocarditis following cardiac surgery. Highlights a high-mortality cardiac infectious complication where IFN-gamma augmentation of macrophage killing may theoretically be relevant. |
| [37180421](https://pubmed.ncbi.nlm.nih.gov/37180421/) | 2022 | Systematic Review | Therapeutic Advances in Rare Disease | Systematic review of therapeutic interventions in Friedreich ataxia, which causes progressive hypertrophic cardiomyopathy. IFN-gamma-1b is among agents assessed for frataxin induction — indirect cardiac pathway. |
| [29456196](https://pubmed.ncbi.nlm.nih.gov/29456196/) | 2018 | Case Report | Journal of Cystic Fibrosis | IFN-gamma therapy improved *Exophiala dermatitidis* airway persistence and prevented respiratory decline in a CF patient. Demonstrates immunological activity of exogenous IFN-gamma in a rare fungal infection setting (analogous to CGD susceptibility). |
| [21131468](https://pubmed.ncbi.nlm.nih.gov/21131468/) | 2011 | Validation Study | American Journal of Respiratory and Critical Care Medicine | Validation of the 6-minute walk test (6MWT) in idiopathic pulmonary fibrosis. Indirect methodological context: IFN-gamma-1b was trialled (and failed) in IPF, and 6MWT is also a standard functional endpoint in heart failure trials. |

---

## Safety Considerations

Interferon gamma-1b is not registered with the TGA in Australia and no Australian Product Information (PI) is available. Please refer to the **international prescribing information** (e.g., Actimmune® US Full Prescribing Information or Imukin® European SmPC) for comprehensive safety data.

**Mechanistic safety signal directly relevant to the cardiac indication:**

- **IFN-gamma-induced myocarditis risk:** IFN-gamma activates Th1 inflammatory pathways; immune-mediated cardiac inflammation and cardiomyopathy have been reported with interferon therapies. Any prospective cardiac investigation would require mandatory cardiac monitoring including echocardiography, ECG, and serial cardiac biomarkers (troponin I/T, BNP/NT-proBNP) at baseline and throughout treatment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a TxGNN prediction score of 99.99%, there are no clinical trials testing interferon gamma-1b directly for any heart disease indication, and the mechanistic anti-fibrotic rationale is counterbalanced by a well-recognised pro-inflammatory myocarditis risk in cardiac tissue. The model prediction most likely reflects indirect network connections through CGD-cardiac complication and Friedreich ataxia-cardiomyopathy pathways, not a validated therapeutic signal.

**To proceed, the following is needed:**

- **Preclinical cardiac safety data:** Murine models of cardiac fibrosis or cardiomyopathy with IFN-gamma-1b treatment, including histological fibrosis grading and echocardiographic functional endpoints, to establish whether anti-fibrotic or pro-inflammatory effects predominate in cardiac tissue
- **MOA clarification in cardiac context:** Systematic characterisation of IFN-gamma signalling in cardiomyocytes and cardiac fibroblasts — specifically the balance between TGF-β inhibition (anti-fibrotic) and CXCL10/Th1 activation (pro-inflammatory)
- **Cardiac adverse event mining:** Retrospective review of cardiac adverse events in existing CGD and osteopetrosis clinical trial datasets where IFN-gamma-1b was administered long-term
- **Target population identification:** Define a clinically meaningful sub-population (e.g., CGD patients with cardiac fibrosis on imaging, or FRDA patients with early hypertrophic cardiomyopathy) where benefit-risk may be more favourable and a pilot study hypothesis can be constructed
- **TGA regulatory pathway:** Since interferon gamma-1b is not marketed in Australia, any future clinical investigation would require either a new TGA registration application or access via the Special Access Scheme (SAS Category B or C), with relevant overseas regulatory precedents (FDA/EMA approvals for CGD) to support the application
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

