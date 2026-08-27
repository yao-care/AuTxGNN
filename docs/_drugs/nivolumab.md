---
layout: default
title: Nivolumab
parent: 僅模型預測 (L5)
nav_order: 474
evidence_level: L5
indication_count: 10
---

# Nivolumab
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

# Nivolumab: From Melanoma to Non-Cutaneous Melanoma Subtypes

## One-Sentence Summary

Nivolumab is an anti-PD-1 immune checkpoint inhibitor already established in the treatment of melanoma. The TxGNN model predicts it may also be effective for **non-cutaneous melanoma** — a heterogeneous group covering mucosal, ocular, anorectal and other rare melanoma sites — with **50 clinical trials** and **8 publications** currently identified in support of this direction (though most were designed for melanoma broadly rather than this subtype specifically).

> **Data note:** This evidence pack shows no ARTG entry and no TFDA/TGA Product Information on file for Nivolumab (market status: "not marketed", 0 licences). Given Nivolumab (Opdivo®) is a well-established, internationally approved therapy, this most likely reflects a gap in the underlying data collection rather than true absence from the Australian market — **this should be verified directly against the TGA ARTG register before this report is used for any decision.**

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack — no ARTG-listed indication text was returned (see data note above) |
| Predicted New Indication | Non-cutaneous melanoma |
| TxGNN Prediction Score | 98.41% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed (per this evidence pack — recommend independent TGA verification) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on the supporting evidence that is available, Nivolumab is a fully human anti-PD-1 monoclonal antibody that blocks the PD-1/PD-L1 interaction, restoring T-cell mediated anti-tumour immunity. This mechanism is already well established in melanoma treatment generally — the evidence pack's own rationale notes it is "已核准用於黑色素瘤整體治療" (approved for melanoma treatment overall) in multiple jurisdictions.

"Non-cutaneous melanoma" is not a distinct disease but an umbrella term for melanoma arising outside typical sun-exposed skin — mucosal, ocular/uveal, anorectal, and other rare primary sites. Mechanistically, PD-1 expression and immune evasion pathways are shared across melanoma subtypes, so the rationale for extending Nivolumab's use is biologically plausible.

However, the evidence base is markedly weaker than for cutaneous melanoma. Non-cutaneous subtypes generally carry a lower tumour mutational burden (TMB) and have historically shown inferior response rates to checkpoint inhibition. Much of the supporting evidence identified here is real-world/observational data, basket trials that enrol non-cutaneous melanoma alongside other rare tumours, or individual case reports — rather than subtype-specific randomised trials. This heterogeneity is the main reason the evidence level sits at L2 rather than L1, despite the large trial volume.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02599402](https://clinicaltrials.gov/study/NCT02599402) | Phase 3 | Completed | 533 | CheckMate 401: nivolumab + ipilimumab followed by nivolumab monotherapy vs. combination alone, first-line in unresectable/metastatic melanoma |
| [NCT07221734](https://clinicaltrials.gov/study/NCT07221734) | Phase 3 | Recruiting | 632 | LEON study: biosimilar MB11 vs. reference Opdivo® in previously untreated advanced melanoma |
| [NCT02990611](https://clinicaltrials.gov/study/NCT02990611) | N/A (non-interventional) | Completed | 1,087 | Large national real-world study of nivolumab ± ipilimumab in advanced/adjuvant melanoma settings |
| [NCT03767348](https://clinicaltrials.gov/study/NCT03767348) | Phase 1/2 | Active, not recruiting | 340 | IGNYTE: RP1 oncolytic virus + nivolumab in unresectable melanoma, MSI-H/dMMR tumours and non-melanoma skin cancer |
| [NCT03235245](https://clinicaltrials.gov/study/NCT03235245) | Phase 2 | Active, not recruiting | 271 | EBIN (EORTC): sequential targeted therapy then nivolumab+ipilimumab vs. immediate combination immunotherapy in BRAF V600-mutant melanoma |
| [NCT02977052](https://clinicaltrials.gov/study/NCT02977052) | Phase 2 | Unknown | 186 | OpACIN-neo: optimal neoadjuvant dosing schedule of ipilimumab + nivolumab in stage III melanoma |
| [NCT02637531](https://clinicaltrials.gov/study/NCT02637531) | Phase 1 | Unknown | 219 | IPI-549 monotherapy and combined with nivolumab in advanced solid tumours, including melanoma |
| [NCT03645928](https://clinicaltrials.gov/study/NCT03645928) | Phase 2 | Recruiting | 245 | Autologous tumour-infiltrating lymphocyte (TIL) therapy combined with checkpoint inhibitors in solid tumours |
| [NCT04462406](https://clinicaltrials.gov/study/NCT04462406) | Phase 2 | Active, not recruiting | 150 | PET-Stop: biomarker-driven early discontinuation of anti-PD-1 therapy in advanced melanoma |
| [NCT02593786](https://clinicaltrials.gov/study/NCT02593786) | Phase 1/2 | Completed | 58 | CheckMate 077: nivolumab safety/efficacy in Chinese patients with previously treated advanced/recurrent solid tumours (incl. melanoma) |

*40 additional trials were identified but are not shown here; most are melanoma trials generally rather than non-cutaneous-subtype-specific studies.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26841210](https://pubmed.ncbi.nlm.nih.gov/26841210/) | 2016 | Cohort | J Eur Acad Dermatol Venereol | Single-institution comparison of nivolumab outcomes in cutaneous vs. non-cutaneous melanoma |
| [37887546](https://pubmed.ncbi.nlm.nih.gov/37887546/) | 2023 | Cohort | Curr Oncol | Retrospective multi-centre comparison of anti-PD-1 ± ipilimumab outcomes by age group in advanced melanoma |
| [30510916](https://pubmed.ncbi.nlm.nih.gov/30510916/) | 2018 | Biomarker study | Front Oncol | Serum soluble CD163 explored as a predictive marker of nivolumab response in advanced cutaneous melanoma |
| [30549256](https://pubmed.ncbi.nlm.nih.gov/30549256/) | 2019 | Cohort | Int J Rheum Dis | Development of rheumatic immune-related adverse events associated with good oncological response to PD-1 inhibition |
| [41774417](https://pubmed.ncbi.nlm.nih.gov/41774417/) | 2025 | Case series | Pigment Cell Melanoma Res | Molecular profiling of epidermotropic metastatic melanoma in a patient on adjuvant nivolumab |
| [28171845](https://pubmed.ncbi.nlm.nih.gov/28171845/) | 2017 | Case Report | Int J Surg Case Rep | First reported case of metastatic anorectal amelanotic melanoma responding markedly to nivolumab |
| [34176837](https://pubmed.ncbi.nlm.nih.gov/34176837/) | 2022 | Case Report | Intern Med (Tokyo) | Mediastinal (non-cutaneous) malignant melanoma showing marked shrinkage on nivolumab monotherapy |
| [40236344](https://pubmed.ncbi.nlm.nih.gov/40236344/) | 2025 | Case Report | Cureus | Metastatic melanoma in the transverse colon, managed with surgical resection and systemic immunotherapy |

---

## Australia Market Information

Currently no ARTG entries are recorded for Nivolumab in this evidence pack. Given Nivolumab is internationally approved and marketed (as Opdivo®), this is likely a data collection gap rather than genuine market absence — **please verify directly against the TGA ARTG register** before relying on this field.

---

## Cytotoxicity

Nivolumab is an antineoplastic agent (used across multiple cancer indications, including melanoma), so this section applies — however, it is **not** a conventional cytotoxic chemotherapy agent; it is a checkpoint-inhibitor immunotherapy, which has a materially different toxicity profile.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-1 immune checkpoint inhibitor) — not conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Low — myelosuppression is not a characteristic toxicity of PD-1 blockade; please refer to the PI for confirmed haematological safety data |
| Emetogenicity Classification | Low — checkpoint inhibitors are not classically emetogenic, unlike cytotoxic chemotherapy |
| Monitoring Items | Immune-related adverse event (irAE) surveillance rather than standard cytotoxic monitoring — literature identified in this pack reports myocarditis, colitis, pneumonitis and rheumatic irAEs with nivolumab; thyroid function, liver function, and clinical symptoms of colitis/pneumonitis/myocarditis should be monitored |
| Handling Protection | As a monoclonal antibody, standard cytotoxic drug handling precautions (e.g. closed-system transfer devices) do not automatically apply — follow institutional biologic/monoclonal antibody infusion protocols and the TGA-approved PI |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information — this evidence pack contains no populated key warnings, contraindications, or drug interaction data for Nivolumab (all fields returned as data gaps; DDI query status: not found). This is flagged as a **Blocking** data gap (DG001) that must be resolved before any formal safety assessment.

Separately, literature identified during this evidence review (outside the formal safety fields) reported immune-related adverse events with nivolumab, including fulminant myocarditis, colitis, and pneumonitis — consistent with the known irAE profile of PD-1 inhibitors generally, and worth flagging for clinical awareness pending full PI review.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is sound (shared PD-1 pathway across melanoma subtypes) and one completed Phase 3 RCT (CheckMate 401) plus a large body of trial and real-world evidence supports Nivolumab in melanoma broadly. However, evidence specific to non-cutaneous subtypes is largely indirect — drawn from basket trials, retrospective cohorts, and case reports — rather than subtype-dedicated randomised trials, and known biological differences (lower TMB, generally lower response rates) mean efficacy cannot be assumed to transfer directly from cutaneous melanoma.

**To proceed, the following is needed:**
- TFDA/TGA-approved Product Information — warnings, precautions and contraindications (Blocking gap, DG001)
- Mechanism of action documentation from DrugBank or equivalent source (DG002)
- Independent verification of actual TGA/ARTG registration status for Nivolumab in Australia, given the discrepancy between this evidence pack and its well-established international approval
- Subtype-specific efficacy data (e.g. dedicated mucosal, uveal, or anorectal melanoma trial results) to narrow the current heterogeneous "non-cutaneous melanoma" grouping
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

