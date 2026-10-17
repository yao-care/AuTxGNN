---
layout: default
title: Sirolimus
parent: Model Prediction Only (L5)
nav_order: 677
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Sirolimus: predicted new indication Liposarcoma (evidence level L5). Approved use: Renal cell carcinoma and lymphangioleiomyomatosis"
monitor_inn: "Sirolimus"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "uterine corpus perivascular epithelioid cell tumor", "benign PEComa", "lymphangiomyoma", "vulva sarcoma"]
---

# Sirolimus
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Sirolimus: From Renal Cell Carcinoma and Lymphangioleiomyomatosis to Liposarcoma

## One-Sentence Summary

Sirolimus is an mTOR inhibitor, listed among its original indications for renal cell carcinoma and lymphangioleiomyomatosis (LAM).
The TxGNN model's top-ranked prediction is **liposarcoma**, supported by **1 Phase 2 clinical trial** and **7 publications**, mostly reviews with indirect relevance.
Among the 10 predicted indications, the best-supported one is **lymphangiomyoma (LAM-related disease)**, with **9 clinical trials** including a completed Phase 3 trial. This is closer to confirming an existing use than true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal cell carcinoma and lymphangioleiomyomatosis (from the knowledge graph; the ARTG indication text is blank) |
| Predicted New Indication | Liposarcoma (rank 1) |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 for liposarcoma (L1 for the best-supported prediction, lymphangiomyoma) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold for liposarcoma (treat as a research question); Proceed with Guardrails for lymphangiomyoma/LAM |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, sirolimus inhibits mTORC1, a central regulator of cell growth and proliferation. Its efficacy in LAM and its use in renal cell carcinoma support the idea that mTOR-driven tumours may respond.

For liposarcoma, the data report that PI3K/AKT/mTOR pathway activation occurs in soft tissue sarcomas. One completed single-arm Phase 2 trial tests sirolimus combined with cyclophosphamide, but no results were provided. A single-arm design cannot separate sirolimus's effect from its partner drug. The supporting literature is largely reviews and transplant cancer-risk studies, which are only indirectly relevant.

The related predictions follow a clearer pattern:
- **LAM / lymphangiomyoma:** TSC1/TSC2 mutations cause mTORC1 hyperactivation, which sirolimus inhibits directly. This is backed by randomised Phase 3 evidence.
- **PEComa family (benign PEComa, uterine PEComa, lung PEComa):** These tumours commonly carry TSC1/TSC2 loss, giving a plausible rationale. Evidence is mostly case reports and reviews, and for the uterine and lung entries it is largely extrapolated from other sites or from LAM.
- **Renal cell carcinoma subtypes (TFE3-translocation, unclassified, neuroblastoma-associated) and ovarian myxoid liposarcoma and vulva sarcoma:** These have no direct trials or literature and appear to reflect graph propagation from related nodes.

## Clinical Trial Evidence

**Liposarcoma (rank 1)**

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | Single-arm, multicentre trial of sirolimus plus cyclophosphamide in metastatic or unresectable myxoid liposarcoma and chondrosarcoma. No efficacy results provided. |

**Lymphangiomyoma / LAM (rank 5, the best-supported prediction)**

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00414648](https://clinicaltrials.gov/study/NCT00414648) | Phase 3 | Completed | 89 | MILES: efficacy and safety of sirolimus in LAM (pivotal evidence) |
| [NCT03150914](https://clinicaltrials.gov/study/NCT03150914) | Phase 3 | Active, not recruiting | 60 | MELODY: early, long-term low-dose sirolimus to prevent progression in early LAM |
| [NCT00457808](https://clinicaltrials.gov/study/NCT00457808) | Phase 2 | Completed | 25 | Rapamycin for angiomyolipomas in tuberous sclerosis complex (TSC) and sporadic LAM |
| [NCT00490789](https://clinicaltrials.gov/study/NCT00490789) | Phase 2 | Unknown | 14 | Sirolimus for renal angiomyolipomas in TSC or sporadic LAM |
| [NCT03253913](https://clinicaltrials.gov/study/NCT03253913) | Phase 2 | Completed | 25 | RESULT: resveratrol plus sirolimus in LAM (single-agent contribution not isolated) |
| [NCT03304678](https://clinicaltrials.gov/study/NCT03304678) | Phase 2 | Completed | 33 | Blood biomarkers of sirolimus sensitivity in LAM (indirect for efficacy) |
| [NCT02432560](https://clinicaltrials.gov/study/NCT02432560) | N/A | Recruiting | 600 | MIDAS: long-term durability and safety of mTOR inhibitors in LAM |
| [NCT01687179](https://clinicaltrials.gov/study/NCT01687179) | Phase 1 | Completed | 14 | Hydroxychloroquine plus sirolimus in TSC/LAM (safety of the combination) |
| [NCT02061397](https://clinicaltrials.gov/study/NCT02061397) | Phase 1/2 | Completed | 10 | Simvastatin safety in LAM/TSC patients already on sirolimus or everolimus |

No clinical trials are registered for the other predicted indications, apart from two LAM-related studies (NCT02432560, NCT02061397) mapped to lung PEComa. No ANZCTR identifiers were available in the data compiled for this report.

## Literature Evidence

**Liposarcoma (rank 1)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | RCT (secondary analysis) | J Am Soc Nephrol | Sirolimus after early cyclosporine withdrawal reduced cancer risk in adult renal transplant recipients |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Review | Curr Opin Oncol | Rationale and results of molecular-targeted agents in advanced sarcomas |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Review | Cancers | Novel therapeutics in soft tissue sarcoma |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bull Cancer | Targeted treatment of rare connective tissue tumours and sarcomas |
| [26093731](https://pubmed.ncbi.nlm.nih.gov/26093731/) | 2015 | Review | Transplant Proc | Cancer screening in renal transplant patients on long-term immunosuppression |

**LAM and PEComa-related evidence (ranks 4, 5, 9)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32059669](https://pubmed.ncbi.nlm.nih.gov/32059669/) | 2020 | Systematic review / meta-analysis | Respir Res | Efficacy and safety of pharmacological treatments for LAM |
| [36642366](https://pubmed.ncbi.nlm.nih.gov/36642366/) | 2023 | Clinical study | Chest | Safety and efficacy of combined resveratrol and sirolimus in LAM |
| [25329516](https://pubmed.ncbi.nlm.nih.gov/25329516/) | 2014 | Clinical study | Am J Respir Crit Care Med | Sustained effects of sirolimus on lung function and cystic lesions in LAM |
| [37773307](https://pubmed.ncbi.nlm.nih.gov/37773307/) | 2024 | Prospective cohort | World J Pediatr | Sirolimus promoted disappearance of renal angiomyolipoma in children with TSC |
| [28177188](https://pubmed.ncbi.nlm.nih.gov/28177188/) | 2017 | Systematic review | Liver Int | Management of hepatic angiomyolipoma |
| [34123648](https://pubmed.ncbi.nlm.nih.gov/34123648/) | 2021 | Case report | Cureus | Nab-sirolimus response after everolimus failure in uterine PEComa |
| [26645891](https://pubmed.ncbi.nlm.nih.gov/26645891/) | 2016 | Case reports | Anti-Cancer Drugs | Neoadjuvant or adjuvant sirolimus in two malignant PEComas |
| [32257249](https://pubmed.ncbi.nlm.nih.gov/32257249/) | 2020 | Case report | Oxf Med Case Rep | Initial response to sirolimus in malignant abdominal PEComa with liver metastasis |
| [28576480](https://pubmed.ncbi.nlm.nih.gov/28576480/) | 2017 | Case report | J AAPOS | Orbital PEComa in a child: sirolimus stopped at week 3 because of tumour progression |
| [39489895](https://pubmed.ncbi.nlm.nih.gov/39489895/) | 2024 | Phase 2 single-arm trial (nintedanib, not sirolimus) | Lancet Respir Med | Nintedanib in LAM, as an alternative where sirolimus toxicity or resistance limits use |

The single paper linked to vulva sarcoma (PMID 20922700) concerns skin cancer in renal transplant recipients and is not evidence of efficacy in that disease.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13860L | Rapamune | Tablet 0.5 mg (oral) | Indication text not available in the data compiled for this report |

## Cytotoxicity

Sirolimus's original indications include renal cell carcinoma, but it is an mTOR inhibitor (targeted therapy) rather than a conventional cytotoxic agent. Detailed cytotoxicity data are not available in the data compiled for this report. Please refer to the Product Information (PI) warnings and precautions.

## Safety Considerations

Key warnings and contraindications from the label were not available. Please refer to the TGA-approved Product Information (PI) for these.

- **Knowledge-graph contraindication signals** (not label text) include: hypertension, kidney disease, liver disease, gallbladder disease, hyperglycaemia and diabetes mellitus, diabetic ketoacidosis, hyperlipidaemia and hypertriglyceridaemia, stroke and cerebrovascular disorders, hyperbilirubinaemia, interstitial lung disease, infections (including pneumocystosis and cytomegalovirus infection), cancer, pericardial effusion, and progressive multifocal leukoencephalopathy.
- **Drug interactions:** 100 interactions were identified. Those listed include:
  - **Major:** amphotericin B (including lipid complex), mesalazine, balsalazide, clarithromycin.
  - **Moderate:** antidiabetic agents (acarbose, metformin, pioglitazone, alogliptin, albiglutide, canagliflozin, dapagliflozin, chlorpropamide), corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), aprepitant, cimetidine.

## Conclusion and Next Steps

**Decision: Hold for liposarcoma (research question); Proceed with Guardrails for lymphangiomyoma/LAM**

**Rationale:**
- **Liposarcoma** has only one completed single-arm Phase 2 trial with no reported results, and the literature is mostly indirect. The evidence is too weak to support a new use, so this remains a research question (L3).
- **Lymphangiomyoma/LAM** has randomised Phase 3 evidence (MILES, MELODY ongoing) and long-term safety follow-up (MIDAS). LAM is already among sirolimus's original indications, so this is confirmation of an existing use rather than true repurposing.
- **Benign PEComa** (L3) and **lung PEComa** (L2) have case-level or LAM-derived evidence only. **Ovarian myxoid liposarcoma, uterine PEComa, the three renal cell carcinoma subtypes and vulva sarcoma** rest on model prediction alone (L5) and should be held.

**To proceed, the following is needed:**
- Published results from NCT02821507, with a comparison that separates sirolimus's contribution from cyclophosphamide.
- Mechanism of action data and the TGA-approved Product Information, including warnings, contraindications and the approved indication text for ARTG 13860L (the label safety data gap is blocking for safety screening).
- Confirmation of the ARTG-approved indications against LAM and renal cell carcinoma.
- For any LAM use: a monitoring plan covering infection and immunosuppression risk, pneumonitis, metabolic effects (glucose, lipids), renal function, drug interactions (especially clarithromycin, a major interaction, and other CYP3A4/P-gp-affecting drugs) and trough-level monitoring.
- Prospective evidence for the PEComa-family entries beyond case reports.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

