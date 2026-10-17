---
layout: default
title: Alemtuzumab
parent: Model Prediction Only (L5)
nav_order: 31
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Alemtuzumab: predicted new indication Syndrome with combined immunodeficiency (evidence level L5). Approved use: Relapsing-remitting multiple sclerosis"
monitor_inn: "Alemtuzumab"
predicted_indications: ["hepatic infarction", "syndrome with combined immunodeficiency", "hepatic veno-occlusive disease", "kidney pelvis sarcomatoid transitional cell carcinoma", "infiltrating bladder urothelial carcinoma sarcomatoid variant", "prostatic urethra urothelial carcinoma", "renal pelvis papillary urothelial carcinoma", "peliosis hepatis", "acquired hemophagocytic lymphohistiocytosis associated with malignant disease", "hemophagocytic syndrome associated with an infection"]
---

# Alemtuzumab
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

# Alemtuzumab: From Relapsing-Remitting Multiple Sclerosis to Syndrome with Combined Immunodeficiency

## One-Sentence Summary

Alemtuzumab is an anti-CD52 monoclonal antibody, originally used to treat relapsing-remitting multiple sclerosis.
Among the ten predictions compiled for this report, the best-supported is **syndrome with combined immunodeficiency**, where alemtuzumab is used as part of conditioning before stem cell transplantation, with **6 clinical trials** and **8 publications** currently supporting this direction.
The top-ranked TxGNN prediction (hepatic infarction) has no supporting evidence, so this report focuses on the best-supported candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relapsing-remitting multiple sclerosis (from the TxGNN knowledge graph; the ARTG indication text is not available) |
| Predicted New Indication | Syndrome with combined immunodeficiency (rank 2 of 10; the best-supported prediction. The rank 1 prediction, hepatic infarction, has no evidence and is not pursued) |
| TxGNN Prediction Score | 93.73% (rank 1, hepatic infarction: 94.44%) |
| Evidence Level | L2 (Phase 2 and Phase 2/3 trials only, with no completed Phase 3 RCT; confounded by multi-drug regimens) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails (as a research question, not a clinical recommendation) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, alemtuzumab is an anti-CD52 antibody that depletes lymphocytes. In multiple sclerosis, this lymphocyte depletion is the basis for its disease-modifying effect.

In primary immunodeficiencies, alemtuzumab is not a disease-modifying therapy. It is used as a lymphodepleting and serotherapy component of reduced-intensity conditioning before allogeneic haematopoietic stem cell transplantation (HSCT). It promotes engraftment and reduces graft rejection and graft-versus-host disease (GVHD). The shared link with multiple sclerosis is therefore lymphocyte depletion, applied here to enable a curative transplant.

The evidence is supportive but confounded. Alemtuzumab is almost always given alongside other agents (for example fludarabine, melphalan, treosulfan or busulfan), so its individual contribution cannot be isolated. Cohorts are also small and heterogeneous.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01182675](https://clinicaltrials.gov/study/NCT01182675) | Phase 2 | Terminated | 7 | HSCT in children with SCID using alemtuzumab plus plerixafor and filgrastim, avoiding toxic chemotherapy conditioning |
| [NCT05463133](https://clinicaltrials.gov/study/NCT05463133) | Phase 1/2 | Recruiting | 50 | Allogeneic HSCT for chronic granulomatous disease with an alemtuzumab, busulfan and TBI-based conditioning regimen plus cytokine antagonists |
| [NCT00152100](https://clinicaltrials.gov/study/NCT00152100) | Phase 1 | Completed | 4 | Haploidentical CD133+ cell transplant in children with SCID; alemtuzumab contribution unclear |
| [NCT00579137](https://clinicaltrials.gov/study/NCT00579137) | Phase 1/2 | Terminated | 3 | CD45 antibody plus alemtuzumab conditioning for HSCT in SCID and other primary immunodeficiencies; directly relevant but very small |
| [NCT01019876](https://clinicaltrials.gov/study/NCT01019876) | Phase 2/3 | Completed | 38 | Risk-adapted reduced-intensity transplant for mixed donor chimerism in non-malignant diseases, including immunodeficiencies |
| [NCT01962415](https://clinicaltrials.gov/study/NCT01962415) | Phase 2 | Recruiting | 100 | Reduced-intensity conditioning for HSCT in paediatric and young adult patients with non-malignant disorders |
| [NCT01652092](https://clinicaltrials.gov/study/NCT01652092) | N/A | Active, not recruiting | 57 | Standard-of-care allogeneic HSCT guideline for primary immune deficiencies |

No ANZCTR trial identifiers are available in the data compiled for this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27543157](https://pubmed.ncbi.nlm.nih.gov/27543157/) | 2016 | Cohort | Biol Blood Marrow Transplant | Alemtuzumab, fludarabine and melphalan reduced-intensity conditioning (n=4) compared with myeloablative busulfan, cyclophosphamide and antithymocyte globulin (n=14) in chronic granulomatous disease |
| [23131490](https://pubmed.ncbi.nlm.nih.gov/23131490/) | 2013 | Cohort | Blood | International survey of HCT in XIAP deficiency (19 patients); outcomes were poor, with most reduced-intensity regimens alemtuzumab-based |
| [26073206](https://pubmed.ncbi.nlm.nih.gov/26073206/) | 2015 | Cohort | Pediatr Transplant | Single-centre HSCT experience in five patients with hyper-IgM syndrome due to CD40L defects |
| [29155317](https://pubmed.ncbi.nlm.nih.gov/29155317/) | 2018 | Cohort | Biol Blood Marrow Transplant | UK experience of treosulfan and fludarabine conditioning in 160 children with primary immunodeficiency |
| [21325599](https://pubmed.ncbi.nlm.nih.gov/21325599/) | 2011 | Cohort | Blood | Treosulfan-based conditioning in 70 children with primary immunodeficiency, with alemtuzumab included in the regimen |
| [19471859](https://pubmed.ncbi.nlm.nih.gov/19471859/) | 2009 | Case report | Immunol Res | FOXP3 expression after reduced-intensity BMT in an infant with IPEX syndrome |
| [18502831](https://pubmed.ncbi.nlm.nih.gov/18502831/) | 2008 | Case report | Blood | EBV-positive immunodeficiency lymphoma after alemtuzumab-CHOP for peripheral T-cell lymphoma (a safety signal) |
| [15590388](https://pubmed.ncbi.nlm.nih.gov/15590388/) | 2004 | Review | Haematologica | Infectious toxicity associated with alemtuzumab |

Most of these publications are cohort studies and case reports. The data compiled for this report contain no RCTs.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10228H | Lemtrada | Solution concentrate for I.V. infusion, 12 mg in 1.2 mL | Not available in the data compiled for this report |

---

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 interacting drugs. Examples include:
  - **Major**: deferiprone and samarium (153Sm) lexidronam.
  - **Moderate**: systemic corticosteroids (hydrocortisone, betamethasone, budesonide, dexamethasone, prednisolone, prednisone, triamcinolone), acetylsalicylic acid, anticoagulants (heparin, argatroban, lepirudin), radiopharmaceuticals (ibritumomab tiuxetan, tositumomab, iobenguane I-131, strontium-89) and palifermin.
- **Infection and lymphoproliferative risk**: The literature compiled for this report describes infectious toxicity with alemtuzumab (PMID 15590388) and an EBV-positive lymphoproliferative disorder after alemtuzumab-containing therapy (PMID 18502831). In transplant settings, hepatic veno-occlusive disease has been reported with alemtuzumab-containing conditioning (PMIDs 22280517 and 20919852). These are reports from combination regimens, so causality cannot be attributed to alemtuzumab alone.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications, as these were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (as a research question only)

**Rationale:**
- Alemtuzumab has a plausible, established role as a lymphodepleting conditioning agent in HSCT for primary immunodeficiencies. The evidence is limited to small Phase 1/2 trials (several terminated with 3 to 7 patients) and cohort studies, in which its effect cannot be separated from other agents. The evidence level is L2.
- The other nine predictions are not recommended for progression: the top-ranked prediction (hepatic infarction) and the urothelial carcinoma and liver vascular predictions have no supporting evidence or plausible mechanism. Hepatic veno-occlusive disease is a transplant complication rather than a treatable indication. Infection-associated haemophagocytic syndrome (L4, case reports only) is a possible secondary research question, with safety concerns. The malignancy-associated HLH subtype (L5) is mechanistically plausible but has no retrieved evidence.

**To proceed, the following is needed:**
- Mechanism of action data to complete the mechanistic-link analysis
- The TGA-approved Product Information (PI) warnings and contraindications, and the approved indication text for the ARTG entry. These are needed before any safety screening can proceed.
- Review of the larger ongoing trials (NCT01962415 and NCT05463133) for alemtuzumab-specific outcomes
- Comparative data separating the contribution of alemtuzumab from that of other conditioning agents
- Confirmation of relevance to the Australian setting (HSCT centre capacity and regulatory pathway), noting that the ARTG-listed product is a Lemtrada formulation, which is not an HSCT-specific presentation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

