---
layout: default
title: Cyclosporine
parent: Model Prediction Only (L5)
nav_order: 189
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Cyclosporine: predicted new indication Bronchitis (evidence level L5). Approved use: Rheumatoid arthritis, dry eye syndrome, xerophthalmia…"
monitor_inn: "Cyclosporine"
predicted_indications: ["granulomatous disease, chronic, autosomal recessive", "brain aneurysm", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "congenital ichthyosiform erythroderma", "fetal erythroblastosis", "brachydactyly-syndactyly syndrome", "prolapse of lacrimal gland", "excretory apparatus of the lacrimal system anomaly", "bronchitis", "nasolacrimal duct disease"]
---

# Cyclosporine
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

# Cyclosporine: From Dry Eye Disease to Bronchitis (Bronchiolitis Obliterans Syndrome)

## One-Sentence Summary

Cyclosporine is a calcineurin inhibitor originally used for rheumatoid arthritis, dry eye syndrome, xerophthalmia and Sjogren syndrome.
The TxGNN model predicts it may be effective for **bronchitis** (in the available evidence, this maps to bronchiolitis obliterans syndrome after lung or stem cell transplantation),
with **18 clinical trials** and **20 publications** currently supporting this direction. The evidence applies to transplant recipients, not to common bronchitis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, dry eye syndrome, xerophthalmia, Sjogren syndrome (the Australian ARTG entry does not list indication text) |
| Predicted New Indication | Bronchitis (evidence relates to bronchiolitis obliterans syndrome after transplantation) |
| TxGNN Prediction Score | 98.94% |
| Evidence Level | L1 (applies only to bronchiolitis obliterans in transplant recipients) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold (reframe to the transplant population before advancing) |

**Note on the top-ranked prediction:** The highest-scoring prediction by TxGNN was chronic granulomatous disease (score 99.68%). It has only one cohort study on stem cell transplantation, where cyclosporine plays a supportive role, so it is rated L4 (Hold). Bronchitis was selected for this report because it has the strongest clinical trial evidence among the predictions. Other predictions include brain aneurysm (L3), and several rare congenital syndromes and lacrimal conditions with no supporting evidence (L5).

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, cyclosporine is a calcineurin inhibitor that suppresses T cell activation. Its efficacy in immune-mediated and inflammatory conditions of the eye and joints is established, and mechanistically it may be applicable to other T cell-driven inflammatory diseases.

The trials do not address conventional bronchitis. They concern bronchiolitis obliterans syndrome (BOS) and chronic lung allograft dysfunction after lung or haematopoietic stem cell transplantation. BOS is an inflammatory small-airway disease thought to represent chronic rejection or chronic graft-versus-host disease. Inhaled (liposomal) cyclosporine A delivers local calcineurin inhibition to the lung, which may limit the systemic toxicity of oral cyclosporine. The link to the original indications is therefore indirect: a shared immune-mediated mechanism, with the disease mapped to "bronchitis" in the knowledge graph.

---

## Clinical Trial Evidence

Cyclosporine-related trials in bronchiolitis obliterans (up to 10 most relevant shown):

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03656926](https://clinicaltrials.gov/study/NCT03656926) | Phase 3 | Completed | 169 | Liposomal cyclosporine A plus standard of care vs standard of care alone in double lung transplant recipients with CLAD/BOS |
| [NCT03657342](https://clinicaltrials.gov/study/NCT03657342) | Phase 3 | Completed | 62 | Same design in single lung transplant recipients with CLAD/BOS |
| [NCT00755781](https://clinicaltrials.gov/study/NCT00755781) | Phase 3 | Completed | 284 | Cyclosporine inhalation solution to improve BOS-free survival after lung transplantation (prophylaxis) |
| [NCT04039347](https://clinicaltrials.gov/study/NCT04039347) | Phase 3 | Terminated | 164 | Extension study of liposomal cyclosporine A for long-term safety and efficacy in BOS; early termination limits interpretation |
| [NCT01429844](https://clinicaltrials.gov/study/NCT01429844) | Phase 3 | Completed | 274 | Tacrolimus vs cyclosporine (with mycophenolate and steroids) for prevention of BOS after lung transplantation |
| [NCT01334892](https://clinicaltrials.gov/study/NCT01334892) | Phase 2/3 | Terminated | 130 | Aerosolised liposomal cyclosporine A vs placebo for prevention of BOS |
| [NCT01287078](https://clinicaltrials.gov/study/NCT01287078) | Phase 2 | Completed | 25 | Cyclosporine inhalation solution in lung and stem cell transplant recipients with BOS |
| [NCT01650545](https://clinicaltrials.gov/study/NCT01650545) | Phase 1/2 | Completed | 21 | Pilot of aerosol liposomal cyclosporine A for BOS; supports feasibility of inhaled delivery |
| [NCT04107675](https://clinicaltrials.gov/study/NCT04107675) | Phase 2 | Terminated | 6 | Safety and tolerability of two doses of liposomal cyclosporine A vs placebo in BOS after allogeneic stem cell transplantation |
| [NCT01273207](https://clinicaltrials.gov/study/NCT01273207) | Phase 2 | Completed | 7 | Extended access to cyclosporine inhalation solution in lung and stem cell transplant recipients with bronchiolitis obliterans |

Results and primary endpoints for these trials were not included in the data compiled for this report and need verification. No trials registered with ANZCTR were identified.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28662986](https://pubmed.ncbi.nlm.nih.gov/28662986/) | 2017 | Systematic review | J Heart Lung Transplant | Evidence base for CLAD-BOS therapies after first-line immunosuppression |
| [34699688](https://pubmed.ncbi.nlm.nih.gov/34699688/) | 2022 | Review | Am J Transplant | Concept of local immune suppression by inhalation in lung transplant recipients |
| [25359357](https://pubmed.ncbi.nlm.nih.gov/25359357/) | 2014 | Guideline | Eur Respir J | ISHLT/ATS/ERS guideline on diagnosis and management of BOS |
| [23821513](https://pubmed.ncbi.nlm.nih.gov/23821513/) | 2013 | Review | Semin Respir Crit Care Med | Standard and new immunosuppression in lung transplantation; calcineurin inhibitor is a core component |
| [36800551](https://pubmed.ncbi.nlm.nih.gov/36800551/) | 2023 | Review | J Clin Oncol | Novel approaches to chronic graft-versus-host disease |
| [35842078](https://pubmed.ncbi.nlm.nih.gov/35842078/) | 2022 | Review | Transpl Immunol | Overview of clinical trials in lung transplant rejection |
| [9426106](https://pubmed.ncbi.nlm.nih.gov/9426106/) | 1997 | Review | Eur Respir J | New immunosuppressive regimens in lung transplantation |
| [2189665](https://pubmed.ncbi.nlm.nih.gov/2189665/) | 1990 | Review | Clin Chest Med | Obliterative bronchiolitis as late allograft rejection; cyclosporine-based triple therapy more effective than earlier regimens |
| [38563735](https://pubmed.ncbi.nlm.nih.gov/38563735/) | 2024 | Case report | Am J Ther | Cyclosporine-associated organising pneumonia (a safety signal) |
| [37355201](https://pubmed.ncbi.nlm.nih.gov/37355201/) | 2023 | Cohort (pharmacokinetic) | Transplant Cell Ther | Belumosudil affects immunosuppressant pharmacokinetics in chronic GVHD |

Most of the supporting literature consists of reviews. No randomised controlled trial publications were included.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12663L | Ikervis | Eye drops 1 mg per mL, single dose units 0.3 mL, 30 | Indication text not available in the data compiled for this report |

The only registered product is an ophthalmic formulation. No inhaled cyclosporine product is registered, so the route needed for BOS is not currently available in Australia.

---

## Safety Considerations

**Contraindication signals (from the knowledge graph, not product label text):** hypertension, epilepsy, kidney disease, liver disease, gallbladder disease, infectious disease, eye infections and conjunctivitis, hyperbilirubinaemia, hypertriglyceridaemia, thrombocytopenic purpura, pseudotumor cerebri/intracranial hypertension, and cancers including lymphoma and primary central nervous system lymphoma.

**Drug Interactions (100 recorded; examples):**
- **Major:** loperamide
- **Moderate:** rabeprazole, hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide, amphotericin B, bupropion, aprepitant, mesalazine, balsalazide, metronidazole, acetylsalicylic acid, chlorpropamide, cholic acid
- **Minor:** ranitidine, doxycycline

**Additional signal:** A 2024 case report describes cyclosporine-associated organising pneumonia, relevant to any pulmonary use.

For full warnings and precautions, please refer to the TGA-approved Product Information (PI).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Late-phase trials exist for liposomal cyclosporine in BOS, but they concern a transplant-related airway disease, not common bronchitis. The product in Australia is an eye drop with no inhaled formulation, and results, mechanism and safety label data are missing. The strong L1 grade should not be applied to bronchitis.

**To proceed, the following is needed:**
- Reframe the indication to bronchiolitis obliterans syndrome/CLAD in lung or stem cell transplant recipients
- Obtain primary endpoints and results for NCT03656926, NCT03657342, NCT00755781 and NCT04039347 (including reasons for termination)
- Detailed mechanism of action data
- TGA Product Information warnings and contraindications (a blocking data gap)
- Assessment of an inhaled formulation and its regulatory pathway in Australia
- Interaction and safety monitoring plan for transplant populations, including renal function and blood pressure
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

