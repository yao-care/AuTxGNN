---
layout: default
title: Cyclophosphamide
parent: Model Prediction Only (L5)
nav_order: 188
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Cyclophosphamide: predicted new indication Myeloid leukaemia (evidence level L5). Approved use: Mycosis fungoides and cutaneous T-cell lymphomas, plasma cell myeloma…"
monitor_inn: "Cyclophosphamide"
predicted_indications: ["myeloid leukemia", "ganglioneuroblastoma (disease)", "vertebral anomalies and variable endocrine and T-cell dysfunction", "retroperitoneal neoplasm", "lymph node cancer", "lymphoma, non-Hodgkin, familial", "acute lymphoblastic leukemia (disease)", "myelodysplastic syndrome", "unclassified myelodysplastic syndrome", "refractory cytopenia of childhood"]
---

# Cyclophosphamide
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

# Cyclophosphamide: From Lymphoma and Breast Carcinoma to Myeloid Leukaemia

## One-Sentence Summary

Cyclophosphamide is an alkylating chemotherapy agent originally used for lymphomas, multiple myeloma, neuroblastoma, breast carcinoma and retinoblastoma, among other cancers.
The TxGNN model predicts it may be effective for **myeloid leukaemia**, with **30 clinical trials** and **20 publications** compiled for this prediction.
Most of this evidence reflects cyclophosphamide used inside stem cell transplant conditioning and graft-versus-host disease (GVHD) prevention regimens, not as a stand-alone antileukaemic treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mycosis fungoides and cutaneous T-cell lymphomas, plasma cell myeloma, neuroblastoma, lymphoma, primary CNS lymphoma, breast carcinoma, retinoblastoma (from the knowledge graph; the Australian ARTG entry has no indication text) |
| Predicted New Indication | Myeloid leukaemia |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L1 (as scored in the data compiled for this report; see caveats below) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, cyclophosphamide is a prodrug whose active metabolites (such as phosphoramide mustard) crosslink DNA. This is cytotoxic to rapidly dividing cells, including myeloid blasts.

Its efficacy in lymphoid and other haematological cancers is established, so activity against myeloid malignancies is mechanistically plausible. In practice, cyclophosphamide is already used in myeloablative and reduced-intensity conditioning (busulfan/cyclophosphamide, cyclophosphamide/fludarabine). It is also used as post-transplant cyclophosphamide (PTCy), which selectively depletes alloreactive T cells to prevent GVHD.

An important caveat is that the supporting evidence is for use within transplant regimens, not for stand-alone treatment of myeloid leukaemia. The prediction is best read as support for these transplant roles.

---

## Clinical Trial Evidence

Of the 30 trials compiled, the 10 most relevant are listed below (graded by relevance to cyclophosphamide in myeloid disease).

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00003187](https://clinicaltrials.gov/study/NCT00003187) | Phase 2/3 | Completed | 19 | Randomised unrelated donor marrow transplant trial (conventional vs T-cell-depleted); cyclophosphamide in conditioning; very small sample |
| [NCT04473911](https://clinicaltrials.gov/study/NCT04473911) | Phase 1 | Completed | 25 | Reduced-intensity haploidentical transplant with PTCy and a new GVHD prevention agent |
| [NCT00315705](https://clinicaltrials.gov/study/NCT00315705) | Phase 1/2 | Completed | 50 | Clofarabine + etoposide + cyclophosphamide in paediatric relapsed/refractory acute leukaemia |
| [NCT01350245](https://clinicaltrials.gov/study/NCT01350245) | Phase 2 | Completed | 28 | Two-step haploidentical transplant with cyclophosphamide-containing regimen |
| [NCT02441803](https://clinicaltrials.gov/study/NCT02441803) | Phase 2 | Completed | 11 | Allogeneic transplant as first salvage in primary refractory AML; very small sample |
| [NCT00390793](https://clinicaltrials.gov/study/NCT00390793) | Phase 2 | Completed | 107 | Hyper-CVAD + dasatinib in Ph+ ALL (indirect relevance to myeloid disease) |
| [NCT00576979](https://clinicaltrials.gov/study/NCT00576979) | Phase 1/2 | Completed | 51 | IMRT with etoposide and cyclophosphamide conditioning for poor-risk ALL/AML |
| [NCT04904588](https://clinicaltrials.gov/study/NCT04904588) | Phase 2 | Active, not recruiting | 300 | HLA-mismatched unrelated donor transplant with PTCy, tacrolimus and MMF |
| [NCT00309842](https://clinicaltrials.gov/study/NCT00309842) | Phase 2 | Completed | 213 | Cord blood transplant with cyclophosphamide/fludarabine/TBI myeloablative regimen |
| [NCT07183878](https://clinicaltrials.gov/study/NCT07183878) | Not applicable | Recruiting | 138 | Randomised trial of venetoclax-enhanced BuCy vs standard BuCy conditioning in high-risk AML/MDS |

Most trials test transplant platforms or other agents with cyclophosphamide as a backbone. None isolates cyclophosphamide's own contribution. NCT00003187 is the only Phase 2/3 trial among those graded most relevant, and it is small.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36357773](https://pubmed.ncbi.nlm.nih.gov/36357773/) | 2023 | Systematic review / network meta-analysis | Bone Marrow Transplant | Compared myeloablative conditioning regimens (including Bu/Cy) in adult AML in remission |
| [40905088](https://pubmed.ncbi.nlm.nih.gov/40905088/) | 2026 | Cohort | Haematologica | 217 AML patients with PTCy: 2-year overall survival 77%, event-free survival 72% |
| [38758817](https://pubmed.ncbi.nlm.nih.gov/38758817/) | 2024 | Registry study | Cancer | PTCy vs ATG vs combination for GVHD prevention in haploidentical transplant for AML |
| [40434956](https://pubmed.ncbi.nlm.nih.gov/40434956/) | 2025 | Cohort | Future Oncol | Busulfan-cyclophosphamide vs fludarabine-busulfan conditioning in AML |
| [25345651](https://pubmed.ncbi.nlm.nih.gov/25345651/) | 2015 | Cohort | Am J Hematol | Cyclophosphamide/fludarabine non-myeloablative vs myeloablative transplant in 165 AML patients |
| [36842566](https://pubmed.ncbi.nlm.nih.gov/36842566/) | 2023 | Cohort | Transpl Immunol | PTCy and early mixed donor chimerism in myeloid malignancies |
| [41046309](https://pubmed.ncbi.nlm.nih.gov/41046309/) | 2026 | Registry cohort | Bone Marrow Transplant | Cord blood vs haploidentical transplant with PTCy in AML in first remission |
| [42373850](https://pubmed.ncbi.nlm.nih.gov/42373850/) | 2026 | Cohort | Bone Marrow Transplant | Haploidentical vs mismatched unrelated transplant with PTCy in secondary AML |
| [35955881](https://pubmed.ncbi.nlm.nih.gov/35955881/) | 2022 | Cohort | Int J Mol Sci | PTCy in paediatric AML after matched donor transplant |
| [14662323](https://pubmed.ncbi.nlm.nih.gov/14662323/) | 2003 | Review | Exp Hematol | Busulfan-cyclophosphamide vs TBI-cyclophosphamide conditioning in AML |

No randomised controlled trial of cyclophosphamide in myeloid leukaemia was identified in the compiled literature. The evidence is mostly retrospective cohorts and registry analyses.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1266P | Cyclonex | Tablet 50 mg (anhydrous) | Indication text not available in the compiled data |

Only an oral formulation is listed in the compiled data.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, oxazaphosphorine class) |
| Myelosuppression Risk | High at conventional and transplant doses (neutropenia, thrombocytopenia); consider as a dose-limiting toxicity |
| Emetogenicity Classification | Moderate at standard doses; higher at high doses |
| Monitoring Items | Full blood count with differential, renal and liver function, urinalysis (haemorrhagic cystitis), electrolytes; cardiac monitoring at high doses |
| Handling Protection | Must follow cytotoxic drug handling regulations |

These entries reflect general knowledge of the drug class, since toxicity data were not included in the compiled data. Please refer to the Product Information (PI) warnings and precautions for authoritative details.

---

## Safety Considerations

- **Drug Interactions**: A drug interaction query returned 100 interactions. The 20 shown in the data were mostly moderate. Moderate interactions include:
  - amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms)
  - bupropion
  - aprepitant
  - metronidazole
  - nitisinone
  - sulfonylureas and related glucose-lowering drugs (chlorpropamide, acetohexamide, glimepiride, glipizide, glyburide, tolazamide, tolbutamide)
  - nateglinide, repaglinide and troglitazone

  Minor interactions were noted with levofloxacin and ondansetron.
- **Literature-noted risks**: A paediatric report highlights gonadal toxicity, and an older cohort links cyclophosphamide to bladder and kidney cancer after lymphoma therapy.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Many Phase 1–3 trials and cohort studies support cyclophosphamide as a component of conditioning and GVHD prophylaxis regimens in myeloid leukaemia. The L1 score rests largely on trials where cyclophosphamide is a backbone drug, and no trial isolates its effect. The recommendation should therefore apply to transplant regimens, not to stand-alone use.

**To proceed, the following is needed:**
- Review of the TGA Product Information, including warnings, contraindications and approved indications (ARTG 1266P has no indication text in the compiled data)
- Mechanism of action data confirmed from DrugBank
- Confirmation of the evidence grade, given that most trials use cyclophosphamide as a background drug
- A defined role (conditioning vs PTCy) and an intravenous product, since the only Australian entry listed is an oral tablet
- A safety monitoring plan covering myelosuppression, haemorrhagic cystitis, cardiotoxicity and fertility

---

### Note on Other Predicted Indications

The other predictions in the data have the following status:

- **Acute lymphoblastic leukaemia** (L1, Proceed with Guardrails): supported by a randomised Phase 3 trial (GRAALL-2005) and many Phase 2 studies, but used only within multi-agent regimens.
- **Lymph node cancer** (L1, Proceed with Guardrails): this term mixes lymphoma and node-positive breast cancer, which are largely existing indications, so it is not a distinct repurposing signal.
- **Lymphoma, non-Hodgkin, familial** (L1, Proceed with Guardrails): this is established use rather than true repurposing.
- **Myelodysplastic syndrome** (L2, Proceed with Guardrails): used only in transplant conditioning and PTCy.
- **Refractory cytopenia of childhood** (L2, Research Question): evidence is non-specific and there are paediatric gonadal toxicity concerns.
- **Ganglioneuroblastoma, unclassified myelodysplastic syndrome** (L3, Research Question): evidence is limited to case reports or small series.
- **Retroperitoneal neoplasm** (L4, Hold): evidence is case reports only.
- **Vertebral anomalies with endocrine and T-cell dysfunction** (L5, Hold): there is no mechanistic rationale, and cyclophosphamide's immunosuppression could worsen T-cell dysfunction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

