---
layout: default
title: Melphalan
parent: Model Prediction Only (L5)
nav_order: 456
evidence_level: L5
indication_count: 10
---

# Melphalan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Melphalan: From Ovarian Cancer to Gonadal Germ Cell Tumour

## One-Sentence Summary

Melphalan is an oral alkylating chemotherapy agent, originally used for ovarian cancer and related ovarian tumours.
The TxGNN model predicts it may be effective for **gonadal germ cell tumour**,
with **7 clinical trials** (most of them small, early-phase or mixed-population studies) and **1 publication** (a 1964 pharmacology study of limited relevance) currently linked to this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian cancer (including ovarian adenocarcinoma and several ovarian tumour subtypes) |
| Predicted New Indication | Gonadal germ cell tumour |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L2 (see note below) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

*Note on evidence level:* The compiled data assign L2, based on one completed Phase 2 trial (NCT00936936, n=64). That trial tests a multi-drug high-dose regimen, and the data compiled for this report do not confirm how much melphalan contributes. It is a single-arm-style investigational study, not a randomised controlled trial, so the evidence is weaker than L2 would normally imply.

## Why is This Prediction Reasonable?

Melphalan is a bifunctional nitrogen mustard alkylating agent. It forms DNA interstrand crosslinks and induces apoptosis in dividing cells. Detailed mechanism of action data were not available in the compiled data, so this description reflects the drug's general pharmacology.

Ovarian cancer and gonadal germ cell tumours both arise in the gonads, and germ cell tumours are generally highly sensitive to DNA-damaging chemotherapy. High-dose melphalan with autologous stem cell rescue is a rational salvage strategy for relapsed or poor-prognosis disease. The very high TxGNN score is consistent with this mechanism.

Other predictions in the same list (for example mucinous adenocarcinomas of the rectum, colon, gallbladder, cervix and endometrium) appear to be driven by shared histology rather than mechanism. They have no clinical or literature support and are not recommended for further pursuit at this stage.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00936936](https://clinicaltrials.gov/study/NCT00936936) | Phase 2 | Completed | 64 | Two cycles of high-dose chemotherapy (gemcitabine, docetaxel, melphalan, carboplatin, then ifosfamide, carboplatin, etoposide) in poor-prognosis relapsed germ-cell tumours; no outcome results in the compiled data |
| [NCT00003425](https://clinicaltrials.gov/study/NCT00003425) | Phase 1/2 | Completed | 25 | Escalating-dose melphalan with autologous stem cell support and amifostine cytoprotection in cancer patients |
| [NCT00060255](https://clinicaltrials.gov/study/NCT00060255) | Phase 2 | Completed | 451 | Eight high-dose chemotherapy regimens with autologous transplant in haematological malignancy and selected solid tumours; germ cell tumours are only a subset |
| [NCT00638898](https://clinicaltrials.gov/study/NCT00638898) | Phase 1 | Completed | 25 | Busulfan, melphalan and topotecan with autologous transplant in advanced and recurrent tumours; melphalan's individual contribution cannot be isolated |
| [NCT00536601](https://clinicaltrials.gov/study/NCT00536601) | N/A | Completed | 174 | High-dose chemotherapy regimens with or without total-body irradiation before autologous transplant in mixed haematological and solid tumours; low specificity |
| [NCT00002750](https://clinicaltrials.gov/study/NCT00002750) | Phase 1 | Completed | 6 | Intrathecal melphalan for neoplastic meningitis; different route and setting |
| [NCT00003926](https://clinicaltrials.gov/study/NCT00003926) | Phase 1 | Terminated | 13 | Amifostine as a chemoprotectant with autologous transplant in paediatric solid tumours; supportive-care focus, not melphalan efficacy |

No ANZCTR trial identifiers were available in the compiled data.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14151951](https://pubmed.ncbi.nlm.nih.gov/14151951/) | 1964 | Pharmacology study | Acta Unio Int Contra Cancrum | Early work on hormonal and alkylating drug effects on pituitary follicle-stimulating function; no abstract available and little relevance to current clinical use |

For the related prediction of ovarian primitive germ cell tumour, the only publication is a single case report (PMID [9251739](https://pubmed.ncbi.nlm.nih.gov/9251739/), 1997) describing successful mega-dose chemotherapy with stem cell rescue in a 13-year-old with a metastatic ovarian primitive neuroectodermal tumour.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 2547C | Alkeran | Tablet 2 mg | Approved indication text not available in the compiled data |

Only an oral tablet is registered. High-dose melphalan regimens with stem cell rescue, as used in the trials above, are typically given intravenously, so route compatibility with the registered product has not been established.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, nitrogen mustard class) |
| Myelosuppression Risk | High (dose-limiting; the knowledge graph links melphalan to leukopenia, neutropenia, thrombocytopenia and anaemia) |
| Emetogenicity Classification | Please refer to the Product Information (PI) |
| Monitoring Items | Full blood count with differential, renal function, liver function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text):** The knowledge graph links melphalan with kidney disease, thrombocytopenia, anaemia (including macrocytic and haemolytic anaemia), leukopenia, neutropenia (including congenital forms), agranulocytosis, interstitial lung disease, pulmonary fibrosis, drug-induced liver injury and vasculitis. These come from graph edges and should be verified against the PI.
- **Drug Interactions (100 recorded; main examples):**
  - Moderate: amphotericin B (conventional, lipid complex, cholesteryl sulfate and liposomal formulations)
  - Minor: cimetidine, levofloxacin, zinc sulfate, zinc gluconate
  - Unknown severity: lansoprazole, omeprazole, pantoprazole, famotidine, dolasetron, granisetron, aspirin, morphine, metformin, vancomycin, prednisone, simvastatin

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications, as label-based safety data were not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale is plausible and the prediction score is high, but the supporting evidence is thin. The key Phase 2 trial uses a multi-drug regimen with no results available in the compiled data, the other trials are small or mixed-population, and the single publication is a 1964 pharmacology study. Melphalan carries significant myelosuppression risk, and the registered Australian product is an oral tablet whereas the supporting studies used high-dose regimens with stem cell rescue. This is best treated as a research question rather than a candidate ready for clinical adoption.

**To proceed, the following is needed:**
- Published results from NCT00936936, and clarification of melphalan's specific contribution within that regimen
- Retrospective or registry data on melphalan in relapsed germ cell tumours, with efficacy and toxicity outcomes
- Mechanism of action data from DrugBank
- TGA Product Information warnings and contraindications (a blocking data gap for safety screening), including the approved indication text for ARTG 2547C
- Assessment of route and formulation compatibility (oral tablet versus intravenous high-dose use)
- A safety monitoring plan covering myelosuppression, renal impairment and pulmonary toxicity, and confirmation of stem cell rescue capability if high-dose use is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

