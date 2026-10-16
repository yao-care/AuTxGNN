---
layout: default
title: Artemether
parent: Model Prediction Only (L5)
nav_order: 61
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Artemether: predicted new indication Acquired angioedema (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "artemether"
predicted_indications: ["acquired angioedema", "Plasmodium falciparum malaria", "malaria", "angioedema", "hereditary angioedema", "nephrogenic syndrome of inappropriate antidiuresis", "acute contagious conjunctivitis", "scleroderma (disease)", "conjunctivitis", "renin-angiotensin-aldosterone system-blocker-induced angioedema"]
---

# Artemether
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

# Artemether: From Malaria Treatment to Plasmodium falciparum Malaria (Top TxGNN Prediction: Acquired Angioedema)

> **Note on indication selection:** The highest-scoring TxGNN prediction (acquired angioedema, 99.90%) has no supporting evidence. The best-evidenced prediction, **Plasmodium falciparum malaria**, is an established use of artemether rather than true repurposing. This report covers both.

## One-Sentence Summary

Artemether is an artemisinin-derivative antimalarial, marketed in Australia as Riamet (artemether 20 mg with lumefantrine 120 mg tablets). The TxGNN model's top-ranked prediction is **acquired angioedema**, with no trials or publications behind it. Its best-supported prediction is **Plasmodium falciparum malaria**, backed by **30 registered clinical trials** and **20 publications**, but this is an existing, approved use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the ARTG indication text is blank; artemether-lumefantrine is used for malaria) |
| Predicted New Indication (top rank) | Acquired angioedema |
| TxGNN Prediction Score (top rank) | 99.90% |
| Best-Evidenced Prediction | Plasmodium falciparum malaria (TxGNN score 99.77%) |
| Evidence Level | Acquired angioedema: L5; P. falciparum malaria: L1 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Acquired angioedema: Hold; P. falciparum malaria: Proceed with Guardrails |

## Why is This Prediction Reasonable?

**Acquired angioedema (top-ranked).** Detailed mechanism of action data is not available in the compiled data. Artemether is an artemisinin derivative whose endoperoxide bridge is activated by heme iron in the parasite, producing free radicals that damage parasite proteins. This pharmacology has no evident connection to bradykinin or complement pathways, which drive angioedema. The same applies to the other angioedema predictions (angioedema, hereditary angioedema, RAAS-blocker-induced angioedema). The high score is a model output only.

**Plasmodium falciparum malaria.** Artemether is a core component of artemether-lumefantrine, a first-line artemisinin combination therapy for uncomplicated falciparum malaria. The mechanism is directly relevant, so this prediction mainly shows that the model recovers a known use. It is not new repurposing.

**Other predictions** (nephrogenic syndrome of inappropriate antidiuresis, conjunctivitis, acute contagious conjunctivitis, scleroderma) have no supporting studies. Artemisinins have only speculative preclinical anti-inflammatory, antiviral or anti-fibrotic activity, and none of it has been tested in these conditions.

## Clinical Trial Evidence

**Acquired angioedema:** Currently no related clinical trials registered.

**Plasmodium falciparum malaria** (selected from 30 registered trials; trials use artemether-lumefantrine):

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00422084](https://clinicaltrials.gov/study/NCT00422084) | Phase 3 | Completed | 1272 | Double-blind comparison of pyronaridine-artesunate vs artemether-lumefantrine in children and adults (Africa, South-East Asia) |
| [NCT05951595](https://clinicaltrials.gov/study/NCT05951595) | Phase 3 | Recruiting | 1680 | Triple ACT (artemether-lumefantrine-amodiaquine) vs standard ACTs, non-inferiority |
| [NCT01082705](https://clinicaltrials.gov/study/NCT01082705) | Phase 3 | Completed | 323 | Efficacy monitoring of ACTs in Tanzanian children aged 6-59 months |
| [NCT00677833](https://clinicaltrials.gov/study/NCT00677833) | Phase 2/3 | Completed | 361 | Azithromycin plus chloroquine vs artemether-lumefantrine in African children |
| [NCT02020330](https://clinicaltrials.gov/study/NCT02020330) | Phase 3 | Completed | 150 | 3-day vs 5-day artemether-lumefantrine in Myanmar |
| [NCT00529867](https://clinicaltrials.gov/study/NCT00529867) | Phase 4 | Completed | 267 | Artemether-lumefantrine suspension vs tablets in Kenyan children under five |
| [NCT01017770](https://clinicaltrials.gov/study/NCT01017770) | Phase 4 | Completed | 340 | Artemether-lumefantrine vs artesunate-amodiaquine in Burkina Faso |
| [NCT03453840](https://clinicaltrials.gov/study/NCT03453840) | Phase 4 | Completed | 305 | Extended-duration artemether-lumefantrine in children, including those with HIV on efavirenz |
| [NCT02637128](https://clinicaltrials.gov/study/NCT02637128) | Phase 4 | Completed | 452 | In vivo efficacy of artemether-lumefantrine and artesunate-amodiaquine in Malawi |
| [NCT01103830](https://clinicaltrials.gov/study/NCT01103830) | Phase 1 | Completed | 287 | QT/QTc effect of Eurartesim vs Riamet, placebo and moxifloxacin in healthy volunteers |

No ANZCTR identifiers were included in the compiled data.

## Literature Evidence

**Acquired angioedema:** Currently no related literature available.

**Malaria** (selected):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1346408](https://pubmed.ncbi.nlm.nih.gov/1346408/) | 1992 | RCT | Lancet | Intramuscular artemether vs chloroquine in Gambian children with severe malaria |
| [31210357](https://pubmed.ncbi.nlm.nih.gov/31210357/) | 2019 | Systematic review | Cochrane Database Syst Rev | Intramuscular artemether for severe malaria compared with quinine and artesunate |
| [25209020](https://pubmed.ncbi.nlm.nih.gov/25209020/) | 2014 | Systematic review | Cochrane Database Syst Rev | Earlier version of the Cochrane review of artemether for severe malaria |
| [35271592](https://pubmed.ncbi.nlm.nih.gov/35271592/) | 2022 | Systematic review/meta-analysis | PLoS One | Efficacy of three ACTs in Sub-Saharan Africa |
| [22548983](https://pubmed.ncbi.nlm.nih.gov/22548983/) | 2012 | Systematic review | Malar J | Safety and efficacy of artemether-lumefantrine in pregnancy |
| [34983552](https://pubmed.ncbi.nlm.nih.gov/34983552/) | 2022 | Systematic review/meta-analysis | Malar J | Safety of dihydroartemisinin-piperaquine vs artemether-lumefantrine in African children |
| [40138574](https://pubmed.ncbi.nlm.nih.gov/40138574/) | 2025 | Cohort | J Infect Dis | Artemether-lumefantrine treatment selects increased pfmdr1 copy number in African infections |
| [40845863](https://pubmed.ncbi.nlm.nih.gov/40845863/) | 2026 | Phase 4 RCT | Lancet Infect Dis | Efficacy of four ACTs in Ugandan children |
| [17402835](https://pubmed.ncbi.nlm.nih.gov/17402835/) | 2007 | Review | Expert Rev Anti Infect Ther | Artesunate, artemether or quinine in severe malaria |
| [40886013](https://pubmed.ncbi.nlm.nih.gov/40886013/) | 2025 | Pharmacokinetic study | AIDS Res Ther | Dolutegravir and artemether-lumefantrine interaction in HIV/malaria |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 9498X | Riamet | Tablet 20 mg-120 mg (oral) | Not recorded in the compiled data |

## Cytotoxicity

Not applicable. Artemether is an antimalarial, not an antineoplastic drug.

## Safety Considerations

- **Contraindication-related conditions (knowledge graph, not label text):** long QT syndrome, familial long QT syndrome, torsades de pointes and potassium deficiency disease. These are consistent with the QT-interval concerns studied in NCT01103830.
- **Drug interactions:** 95 interactions are recorded. Examples classed as **Major**: clarithromycin, cobicistat, amprenavir, apalutamide, atazanavir, boceprevir. Examples classed as **Moderate**: dexamethasone, miconazole, troglitazone, deferasirox, bosentan, brigatinib, bexarotene, armodafinil, amobarbital, aminoglutethimide, fostamatinib, iodide I-123 and I-131, abametapir. The literature also flags CYP-mediated interactions with antiretrovirals such as dolutegravir.
- **Other items:** Label warnings and contraindications were not available. Please refer to the TGA-approved Product Information (PI) for the full safety information.

## Conclusion and Next Steps

**Decision: Hold (acquired angioedema and the other non-malaria predictions); Proceed with Guardrails (P. falciparum malaria)**

**Rationale:**
- The angioedema predictions (L5) rest only on model scores, with no trials, no literature and no plausible mechanism. The same is true for the other non-malaria predictions.
- The malaria prediction (L1) is supported by multiple completed Phase 3 trials and many systematic reviews. It is an established use rather than repurposing.

**To proceed, the following is needed:**
- Retrieve the TGA PI for Riamet, covering approved indications, warnings and contraindications.
- Obtain mechanism of action data from DrugBank.
- For malaria, apply guardrails: use only in combination with lumefantrine, monitor for resistance signals (pfmdr1, artemisinin partial resistance), review QT risk and interacting medicines, and note that artesunate is generally preferred for severe malaria.
- For the angioedema predictions, do not progress without independent biological rationale and preclinical evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

