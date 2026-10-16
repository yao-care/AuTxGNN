---
layout: default
title: Fludarabine
parent: Model Prediction Only (L5)
nav_order: 303
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Fludarabine: predicted new indication Plasma cell myeloma (evidence level L5). Approved use: Not available in the data compiled for this report"
---

# Fludarabine
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

# Fludarabine: From Haematological Malignancy Treatment to Plasma Cell Myeloma

## One-Sentence Summary

Fludarabine is a purine nucleoside analogue chemotherapy agent. It is registered in Australia as an intravenous injection, though the data compiled for this report do not include its approved indication text.
The TxGNN model predicts it may be useful for **plasma cell myeloma**, and the evidence is mostly indirect: fludarabine appears in **transplant conditioning and CAR-T lymphodepletion regimens** (**28 listed clinical trials** and **20 publications**), not as a standalone antimyeloma therapy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the ARTG entry has no indication text) |
| Predicted New Indication | Plasma cell myeloma |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L2 (as assigned in the compiled data; supporting trials are mostly Phase 1/2 conditioning studies, not myeloma-specific Phase 3 RCTs) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the compiled data. Based on known information, fludarabine is a purine nucleoside analogue that inhibits DNA synthesis and is cytotoxic to lymphocytes.

In myeloma, fludarabine is used mainly as a **lymphodepleting and conditioning agent**, not as an antimyeloma monotherapy. It is given with cyclophosphamide before BCMA-directed CAR-T therapy, and with busulfan or melphalan before allogeneic stem cell transplant. Its role is supportive: it suppresses the immune system so that cell therapies or donor cells can engraft. Preclinical work also shows direct antimyeloma activity in vitro and in vivo.

The TxGNN prediction is therefore best read as support for fludarabine's role within myeloma treatment regimens, not as evidence that it should be used alone.

**Other predicted indications (for context):**
- **Indolent plasma cell myeloma** (score 99.76%, L2): the same conditioning rationale applies, with supporting transplant trials including one completed Phase 3 trial (NCT00075478, n=87, mixed haematological malignancies).
- **Myelodysplastic syndrome** (score 99.75%, L2): fludarabine is an established conditioning backbone before allogeneic transplant, including Phase 2 trials of busulfan/fludarabine and a randomised Phase 3 trial of treosulfan versus busulfan plus fludarabine.
- **Unclassified myelodysplastic syndrome** (score 99.69%, L3): a single prospective Phase 2 report of treosulfan/fludarabine conditioning, with no dedicated trials.
- **Hyperthyroidism, thyroid hormone resistance, brain small vessel disease, the hematuria-retinal arteriolar tortuosity syndrome, the chromosome 5q deletion and diabetic nephropathy** have no plausible supporting evidence and are likely knowledge-graph artefacts (Hold).

---

## Clinical Trial Evidence

The compiled data list 28 trials for plasma cell myeloma. The most relevant 10 are shown below. In nearly all of them, fludarabine is part of conditioning or lymphodepletion rather than the tested intervention.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03303950](https://clinicaltrials.gov/study/NCT03303950) | Phase 2 | Terminated | 6 | Busulfan, fludarabine and cyclophosphamide conditioning before donor transplant in myeloma or myelofibrosis; terminated early |
| [NCT01008462](https://clinicaltrials.gov/study/NCT01008462) | Phase 2 | Completed | 16 | Sequential autologous then nonmyeloablative haploidentical transplant in high-risk lymphoma, myeloma or CLL |
| [NCT01658319](https://clinicaltrials.gov/study/NCT01658319) | Phase 1 | Completed | 20 | Fludarabine plus methoxyamine (TRC102) in relapsed/refractory haematological malignancies; mixed population |
| [NCT00309842](https://clinicaltrials.gov/study/NCT00309842) | Phase 2 | Completed | 213 | Cyclophosphamide/fludarabine/TBI conditioning for unrelated cord blood transplant; myeloma is a subset |
| [NCT00014508](https://clinicaltrials.gov/study/NCT00014508) | Phase 2 | Completed | Not reported | Autologous transplant followed by mini-allogeneic transplant in myeloma |
| [NCT06045806](https://clinicaltrials.gov/study/NCT06045806) | Phase 3 | Active, not recruiting | 79 | Ide-cel plus lenalidomide maintenance vs lenalidomide alone (KarMMa-9); fludarabine is part of lymphodepletion only |
| [NCT07764978](https://clinicaltrials.gov/study/NCT07764978) | Phase 3 | Recruiting | 750 | BCMA/CD19 CAR-T (AZD0120) consolidation in newly diagnosed myeloma (DURGA-5); fludarabine is background lymphodepletion |
| [NCT06413498](https://clinicaltrials.gov/study/NCT06413498) | Phase 3 | Active, not recruiting | 452 | Anitocabtagene autoleucel vs standard of care in relapsed/refractory myeloma (iMMagine-3) |
| [NCT00909948](https://clinicaltrials.gov/study/NCT00909948) | Phase 1 | Terminated | 7 | Recipient leukocyte infusion after nonmyeloablative transplant; limited evidence on fludarabine |
| [NCT05020444](https://clinicaltrials.gov/study/NCT05020444) | Phase 1 | Active, not recruiting | 16 | TriPRIL CAR-T cells with fludarabine/cyclophosphamide lymphodepletion in relapsed/refractory myeloma |

No ANZCTR trial identifiers were available in the compiled data.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17976186](https://pubmed.ncbi.nlm.nih.gov/17976186/) | 2007 | Preclinical | Eur J Haematol | Fludarabine inhibited the RPMI8226 myeloma cell line in vitro and in vivo, with reduced Akt phosphorylation |
| [38483213](https://pubmed.ncbi.nlm.nih.gov/38483213/) | 2024 | Phase 1 trial | Am J Clin Oncol | Bortezomib, fludarabine and melphalan, with or without total marrow irradiation, as allogeneic transplant conditioning in high-risk myeloma |
| [17310135](https://pubmed.ncbi.nlm.nih.gov/17310135/) | 2007 | Retrospective multicentre analysis | Bone Marrow Transplant | Fludarabine/treosulfan reduced-toxicity conditioning before allogeneic transplant in 34 myeloma patients |
| [37701906](https://pubmed.ncbi.nlm.nih.gov/37701906/) | 2023 | Phase 2 | Leuk Res Rep | Split-dose busulfan, fludarabine and post-transplant cyclophosphamide; 2 myeloma patients, 1-year overall survival 50% for the combined group |
| [40972962](https://pubmed.ncbi.nlm.nih.gov/40972962/) | 2025 | Real-world cohort | Transplant Cell Ther | Fludarabine exposure before ide-cel was associated with toxicities, with notable pharmacokinetic variability |
| [39365257](https://pubmed.ncbi.nlm.nih.gov/39365257/) | 2025 | Cohort | Blood | Standard-of-care cilta-cel in 236 relapsed/refractory myeloma patients (fludarabine is part of lymphodepletion) |
| [38659046](https://pubmed.ncbi.nlm.nih.gov/38659046/) | 2024 | Cohort | J Hematol Oncol | Five-year follow-up of LEGEND-2 CAR-T showing durable responses |
| [35333600](https://pubmed.ncbi.nlm.nih.gov/35333600/) | 2022 | Cohort | J Clin Oncol | Long-term follow-up of combined BCMA and CD19 CAR-T in myeloma |
| [7781758](https://pubmed.ncbi.nlm.nih.gov/7781758/) | 1995 | Report | Eur J Haematol | Fludarabine in plasma cell leukaemia (no abstract available) |
| [1638466](https://pubmed.ncbi.nlm.nih.gov/1638466/) | 1992 | Review | Cancer | Early review of new agents, including a new chemotherapeutic agent, for myeloma and non-Hodgkin lymphoma |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 15144C | Fludarabine Phosphate Injection, USP 50 mg/2 mL (Areva, USA) | Solution for I.V. injection, 50 mg fludarabine phosphate in 2 mL (s19A) | Not stated in the compiled data |

The product is supplied under Section 19A, so it is imported and not a standard fully registered product.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside analogue) |
| Myelosuppression Risk | High (neutropenia, thrombocytopenia and anaemia are well recognised; lymphopenia is expected and is the intended effect in conditioning) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | FBC with differential, renal function (dose adjustment is needed in renal impairment), liver function, and neurological status |
| Handling Protection | Must follow cytotoxic drug handling regulations |

Please also refer to the Product Information (PI) warnings and precautions. The compiled literature notes that high doses are associated with severe neurotoxicity, and that therapy-related myelodysplastic syndrome and acute myeloid leukaemia can follow fludarabine combination chemotherapy.

---

## Safety Considerations

- **Drug Interactions:** A search found 100 recorded interactions, and the main ones with a stated severity are:
  - **Moderate:** metronidazole, rosuvastatin, simvastatin, tinidazole
  - **Minor:** levofloxacin
  - Many others have an unknown severity (for example amphotericin B, cimetidine, famotidine, omeprazole, pantoprazole, metformin, morphine and amoxicillin).

Warnings and contraindications were not available in the compiled data. Please refer to the TGA-approved Product Information (PI) for full safety information, particularly because this is a Section 19A imported product.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Fludarabine has a well-established role in myeloma care as a conditioning and lymphodepleting agent (CAR-T and allogeneic transplant), supported by multiple Phase 2 trials, a completed Phase 3 trial in mixed haematological malignancies, and preclinical antimyeloma activity.
- The evidence does not support fludarabine as a standalone antimyeloma treatment, and the high TxGNN score should not be read that way.

**To proceed, the following is needed:**
- The approved indication text and the PI warnings and contraindications for ARTG 15144C, since these were missing from the compiled data
- Detailed mechanism of action data
- Myeloma-specific efficacy and safety data for fludarabine-based conditioning, as distinct from the CAR-T or transplant product being tested
- Dosing and exposure monitoring plans (fludarabine pharmacokinetics vary widely and exposure has been linked to toxicity after ide-cel), with renal function checks
- A safety monitoring plan for myelosuppression, infection risk, neurotoxicity and secondary myeloid neoplasms
- Confirmation of supply arrangements, given the Section 19A status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

