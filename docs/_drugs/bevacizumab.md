---
layout: default
title: Bevacizumab
parent: 僅模型預測 (L5)
nav_order: 85
evidence_level: L5
indication_count: 10
---

# Bevacizumab
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

# Bevacizumab: From Anti-VEGF Antineoplastic Therapy to Cystic Neoplasm

## One-Sentence Summary

Bevacizumab is a recombinant humanised anti-VEGF-A monoclonal antibody with well-established international use across multiple solid tumours — including colorectal cancer, ovarian cancer, non-small cell lung cancer, and glioblastoma — however it is **not currently registered** on the Australian Register of Therapeutic Goods (ARTG).
The TxGNN model predicts it may be effective for **Cystic Neoplasm**, which represents the highest evidence-tier prediction (L1) across all 10 TxGNN predictions generated for this drug, with **8 clinical trials** and **20 publications** currently supporting this direction.
This prediction is mechanistically grounded in Bevacizumab's VEGF-A pathway inhibition — a recognised driver of angiogenesis in serous and mucinous cystic ovarian and peritoneal tumours.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Australia (0 ARTG entries); internationally used for colorectal cancer, ovarian cancer, NSCLC, glioblastoma, renal cell carcinoma, and cervical cancer |
| Predicted New Indication | Cystic Neoplasm |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed (not registered on ARTG) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Bevacizumab is a recombinant humanised IgG1 monoclonal antibody that selectively binds to and neutralises Vascular Endothelial Growth Factor A (VEGF-A). By preventing VEGF-A from engaging its receptors VEGFR-1 and VEGFR-2 on tumour vascular endothelial cells, Bevacizumab disrupts the signalling cascades that drive tumour angiogenesis — the formation of new blood vessels that supply oxygen and nutrients to growing tumours. Detailed mechanism of action data was not available in the current dataset; however, Bevacizumab's anti-angiogenic mechanism as a VEGF-A ligand blocker is comprehensively documented in the global literature and forms the direct biological basis for the prediction below.

Cystic neoplasms — particularly serous and mucinous carcinomas of the ovary, peritoneum, fallopian tube, and appendix (including pseudomyxoma peritonei) — are characterised by high VEGF-A expression and robust angiogenic activity. This makes the VEGF-A → VEGFR axis a well-validated therapeutic target within this disease category. Bevacizumab is already incorporated into international treatment guidelines (ESMO, ASCO, NCCN) for high-grade serous ovarian cancer (first-line and recurrent settings) and low-grade serous ovarian cancer, both of which sit within the broad cystic neoplasm spectrum.

The TxGNN prediction therefore reflects an established, biologically and clinically supported relationship rather than a speculative leap. Mechanistically, Bevacizumab's utility in serous and mucinous cystic tumours is directly analogous to its proven role in ovarian cancer. This makes Cystic Neoplasm the most immediately actionable prediction in the current evidence pack, underpinned by a large Phase III RCT (NCT00565851, n=1,052) and a Phase II study specifically enrolling rare solid tumours including cystic subtypes (NCT03074513, n=133).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00565851](https://clinicaltrials.gov/study/NCT00565851) | Phase 3 | Active, Not Recruiting | 1,052 | Phase III RCT comparing carboplatin/paclitaxel/gemcitabine ± bevacizumab, followed by bevacizumab maintenance and secondary cytoreductive surgery, in platinum-sensitive recurrent ovarian, peritoneal primary, and fallopian tube cancer — directly applicable to cystic ovarian tumour subtypes; largest trial in this evidence pack |
| [NCT03074513](https://clinicaltrials.gov/study/NCT03074513) | Phase 2 | Active, Not Recruiting | 133 | Single-arm open-label study of atezolizumab + bevacizumab in rare solid tumours; explicitly designed to capture cystic and unusual tumour subtypes; Bevacizumab is the core anti-angiogenic agent in the combination |
| [NCT00381797](https://clinicaltrials.gov/study/NCT00381797) | Phase 2 | Completed | 97 | Bevacizumab + irinotecan in paediatric recurrent/progressive glioma, medulloblastoma, ependymoma, and low-grade glioma — includes cystic CNS tumour variants; demonstrates Bevacizumab activity in a paediatric cystic tumour context |
| [NCT00023959](https://clinicaltrials.gov/study/NCT00023959) | Phase 1 | Completed | 39 | Bevacizumab + fluorouracil/hydroxyurea with concomitant radiotherapy in poor-prognosis head and neck cancer — foundational safety and dose-range data for Bevacizumab in solid tumours |
| [NCT00101348](https://clinicaltrials.gov/study/NCT00101348) | Phase 1/2 | Completed | 66 | Erlotinib + cetuximab ± bevacizumab across multiple tumour types (renal cell, colorectal, head and neck, pancreatic, NSCLC) — multi-indication safety and efficacy reference for Bevacizumab combinations |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38328890](https://pubmed.ncbi.nlm.nih.gov/38328890/) | 2024 | Retrospective Cohort | Future Oncology | Bevacizumab in recurrent low-grade serous ovarian carcinoma (n=51): ORR 54.1% (CR 10.4%, PR 43.7%), median PFS 15 months — direct efficacy evidence for Bevacizumab in cystic ovarian tumours |
| [37754507](https://pubmed.ncbi.nlm.nih.gov/37754507/) | 2023 | Systematic Review | Current Oncology | Systematic review of bevacizumab in low-grade serous ovarian cancer — establishes evidence base for Bevacizumab activity in a typically chemo-resistant cystic ovarian subtype |
| [37657955](https://pubmed.ncbi.nlm.nih.gov/37657955/) | 2023 | Retrospective Cohort | Clinical Colorectal Cancer | Mitomycin-C + metronomic capecitabine + bevacizumab in unresectable or relapsed pseudomyxoma peritonei — promising results in a rare mucinous cystic condition of appendiceal origin |
| [24978709](https://pubmed.ncbi.nlm.nih.gov/24978709/) | 2014 | Cohort Study | Int J Gynecological Cancer | Bevacizumab ± chemotherapy in recurrent low-grade serous ovarian/primary peritoneal cancer — significant objective responses noted in borderline and low-grade serous cystic tumours |
| [27154293](https://pubmed.ncbi.nlm.nih.gov/27154293/) | 2016 | Translational/Biomarker | Journal of Translational Medicine | GNAS mutations as prognostic biomarkers in pseudomyxoma peritonei treated with metronomic capecitabine + bevacizumab — supports precision use of Bevacizumab in mucinous cystic neoplasms |
| [32494876](https://pubmed.ncbi.nlm.nih.gov/32494876/) | 2020 | Review | Current Oncology Reports | First-line management of advanced high-grade serous ovarian cancer — comprehensive review of VEGF pathway role and Bevacizumab's integration into standard of care for cystic ovarian cancer |
| [27141073](https://pubmed.ncbi.nlm.nih.gov/27141073/) | 2016 | Review | Annals of Oncology | Mucinous epithelial ovarian carcinoma (benign, borderline, malignant spectrum) — provides disease taxonomy critical for interpreting Bevacizumab applicability across cystic neoplasm subtypes |
| [27412268](https://pubmed.ncbi.nlm.nih.gov/27412268/) | 2016 | Phase 2 Trial | Cancer | Weekly paclitaxel + capecitabine + bevacizumab in triple-negative locally advanced/metastatic breast cancer — Phase 2 efficacy and safety data for Bevacizumab-based combination regimens |
| [18796376](https://pubmed.ncbi.nlm.nih.gov/18796376/) | 2008 | Small Cohort | Clinical & Translational Oncology | Oral metronomic cyclophosphamide + bevacizumab in heavily pretreated recurrent ovarian carcinoma — early evidence supporting metronomic Bevacizumab approaches in relapsed disease |
| [29752717](https://pubmed.ncbi.nlm.nih.gov/29752717/) | 2018 | Preclinical Study | International Journal of Cancer | Dose-dense vs conventional paclitaxel ± bevacizumab in ovarian cancer preclinical models — mechanistic and scheduling data relevant to optimising Bevacizumab in cystic ovarian cancer |

---

## Australia Market Information

Bevacizumab is **not currently registered** on the Australian Register of Therapeutic Goods (ARTG). There are no TGA-approved Bevacizumab products available. The drug is available internationally as Avastin® (Roche/Genentech) and biosimilars in multiple markets including the EU, USA, Japan, and Taiwan.

Clinicians wishing to access Bevacizumab for Australian patients should consider the following regulatory pathways:

- **TGA Special Access Scheme (SAS) Category B**: For individual patients with serious or life-threatening conditions where no suitable registered alternative exists
- **TGA Authorised Prescriber scheme**: For practitioners who regularly prescribe Bevacizumab for a specific indication in a defined patient population
- **Clinical trial enrolment**: Via relevant Australian or international trials (e.g., existing Phase II/III ovarian cancer studies)

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | No registered products | — | Bevacizumab currently has no ARTG registration in Australia |

---

## Cytotoxicity

Bevacizumab is an antineoplastic biological agent and its use is confined exclusively to oncology settings. It is classified as a targeted therapy rather than conventional cytotoxic chemotherapy, reflecting its mechanism of action as a ligand-blocking monoclonal antibody rather than a DNA-damaging or anti-mitotic agent.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — recombinant humanised anti-VEGF-A IgG1 monoclonal antibody; non-cytotoxic mechanism of action |
| Myelosuppression Risk | Low (Bevacizumab alone does not cause direct myelosuppression; haematological toxicity arises from co-administered cytotoxic chemotherapy partners) |
| Emetogenicity Classification | Minimal (Bevacizumab itself carries no intrinsic emetogenic potential; overall emetogenic risk is determined by the concurrent chemotherapy regimen) |
| Monitoring Items | Blood pressure every 2–3 weeks (hypertension very common, up to 34%); urine protein/creatinine ratio or 24-hour urine protein before each cycle; FBC and renal function when used with chemotherapy; coagulation parameters; wound healing assessment before each cycle |
| Handling Protection | Standard biological product handling applies; does not require cytotoxic drug handling precautions (no mutagenic or direct genotoxic risk from handling). Standard aseptic intravenous preparation technique required. |

---

## Safety Considerations

Bevacizumab has no TGA-approved Product Information (PI) in Australia. Clinicians should consult the FDA-approved prescribing information, EMA Summary of Product Characteristics (SmPC), or Roche/Genentech product monograph for complete prescribing guidance. Key safety considerations based on international clinical data include:

- **Hypertension**: Occurs in up to 34% of patients (severe in ~8%); antihypertensive therapy is frequently required. Blood pressure monitoring every 2–3 weeks is standard practice.
- **Proteinuria/Nephrotic syndrome**: Monitor urine protein before each cycle; withhold for ≥2g protein/24h; permanently discontinue if nephrotic syndrome develops.
- **Arterial thromboembolic events**: Increased risk of stroke, TIA, and myocardial infarction, particularly in patients aged >65 years or with prior arterial events; use with caution or avoid in high-risk patients.
- **Wound healing impairment**: Do not administer within 28 days of major surgery; delay elective surgery by at least 28 days after the last Bevacizumab dose.
- **Gastrointestinal perforation and fistula**: Rare but potentially fatal; monitor for new abdominal pain, vomiting, or fever; permanently discontinue if GI perforation occurs.
- **Haemorrhage**: Increased bleeding risk across all grades; pulmonary haemorrhage is particularly serious in patients with NSCLC (squamous histology) and should prompt permanent discontinuation.
- **Posterior reversible encephalopathy syndrome (PRES)**: Rare; presents as acute hypertension, headache, visual disturbance, and/or seizures; discontinue Bevacizumab and manage hypertension urgently.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Bevacizumab's anti-VEGF-A mechanism is directly applicable to cystic neoplasms — particularly serous and mucinous ovarian/peritoneal tumours — and is supported by a Phase III RCT (NCT00565851, n=1,052), a Phase II rare tumour trial (NCT03074513, n=133), a systematic review, and multiple retrospective cohort studies demonstrating clinically meaningful response rates. This is the most evidence-rich prediction among the 10 TxGNN candidates for Bevacizumab, and reflects an established biological relationship rather than an exploratory one. Access to Bevacizumab in Australia requires a TGA regulatory pathway given its current non-registration on the ARTG.

**To proceed, the following is needed:**

- **TGA access pathway**: Initiate SAS Category B or Authorised Prescriber application to the TGA before prescribing, as Bevacizumab has no current ARTG registration
- **Histological subtype confirmation**: Clarify whether the cystic neoplasm is serous (high-grade or low-grade), mucinous, or another subtype (e.g., pseudomyxoma peritonei), as evidence strength and dosing rationale vary considerably by tumour biology
- **Biomarker assessment**: VEGF expression analysis; BRCA1/2 mutation and HRD status if ovarian/peritoneal origin (guides combination therapy decisions with olaparib)
- **Full prescribing information review**: Consult FDA or EMA PI for complete dosing schedules, contraindications, and drug interaction guidance prior to commencement
- **MDT review**: Gynaecological oncology MDT (or relevant tumour site team) discussion prior to initiation
- **Patient monitoring plan**: Establish prospective protocols for blood pressure management, proteinuria surveillance, wound healing review, and thromboembolic risk assessment
- **Clinical registry or compassionate use enrolment**: Where possible, enrol patients in a registry or access programme to contribute to the Australian evidence base for this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

