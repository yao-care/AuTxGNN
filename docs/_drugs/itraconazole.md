---
layout: default
title: Itraconazole
parent: Model Prediction Only (L5)
nav_order: 397
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-17
monitor_inn: "Itraconazole"
predicted_indications: ["pneumocystosis"]
description: "Itraconazole: predicted new indication Pneumocystosis (evidence level L5). In Australia: 2 PBS items (2 currently listed)"
---

# Itraconazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Itraconazole: Pneumocystosis
{: .text-alpha }

## One-Sentence Summary

Itraconazole is a triazole antifungal originally used for systemic fungal infections such as candidiasis, aspergillosis, histoplasmosis, blastomycosis and sporotrichosis.
The prediction is best treated as a model signal rather than an evidence-backed lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 0.9934 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (2 of 2 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for itraconazole: "In vitro studies have demonstrated that itraconazole inhibits the cytochrome P450-dependent synthesis of ergosterol, which is a vital component of fungal cell membranes." ([DailyMed: Sporanox (itraconazole) prescribing information, Janssen Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a4d555fa-787c-40fb-bb7d-b0d4f7318fd0), label version 2026-07-13; accessed 2026-11-19.) Itraconazole is a triazole antifungal; this class inhibits CYP51 (lanosterol 14-alpha-demethylase), blocking ergosterol synthesis in fungal cell membranes. This is general class knowledge rather than data from the compiled record.

For pneumocystosis, the mechanistic link is weak. *Pneumocystis jirovecii* is fungal, but its membrane contains very little ergosterol (cholesterol is the main sterol), so the azole target is poorly relevant. The retrieved literature consists of general reviews on prophylaxis in transplant, HIV and neutropenic populations and histoplasmosis papers; none shows itraconazole efficacy against Pneumocystis.

By contrast, the lower-ranked predictions are mechanistically more coherent, because the pathogens are ergosterol-containing fungi (see the table of other predictions in the Conclusion).

---

## Clinical Trial Evidence

Currently no related clinical trials registered for pneumocystosis.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00000639](https://clinicaltrials.gov/study/NCT00000639) | NA | Completed | 400 | Amphotericin B with flucytosine vs amphotericin B alone in AIDS-associated cryptococcal meningitis, followed by a fluconazole vs itraconazole comparison |
| [NCT00012467](https://clinicaltrials.gov/study/NCT00012467) | Phase 2 | Completed | 60 | Interferon-gamma 1b added to standard antifungal therapy; the agents in standard therapy cannot be confirmed from the truncated title |

---

## Literature Evidence

The most relevant publications retrieved for pneumocystosis are listed below. None demonstrates efficacy of itraconazole against Pneumocystis.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | Randomised placebo-controlled trial (Phase III) | HIV Medicine | Itraconazole capsules for prevention of deep fungal infections in immunodeficient HIV patients; the abstract excerpt does not report a Pneumocystis outcome |
| [15250025](https://pubmed.ncbi.nlm.nih.gov/15250025/) | 2004 | Review | Clin Infect Dis | Antimicrobial prophylaxis in febrile neutropenia; trimethoprim-sulfamethoxazole is highly effective against Pneumocystis pneumonia |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Review | BMJ Clin Evid | Primary and secondary prophylaxis of opportunistic infections in HIV |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review | Clin Pharmacokinet | Penetration of antifungal and other anti-infective agents into pulmonary epithelial lining fluid |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | Therapy and prophylaxis of systemic protozoan infections, including Pneumocystis |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Review | Semin Respir Infect | Infection after lung transplantation |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Review | Curr Clin Top Infect Dis | Prophylaxis and treatment of infection in bone marrow transplant recipients |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | Cohort | Transplant Proc | Invasive fungal infections after kidney transplantation |
| [2233233](https://pubmed.ncbi.nlm.nih.gov/2233233/) | 1990 | Clinical review | Medicine | Disseminated histoplasmosis in AIDS |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | Case report and review | Front Immunol | *T. marneffei* and *P. jirovecii* coinfection in a child with a STAT1 mutation |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10732W | Lozanoc | Capsule 50 mg (oral) | Not available in the data compiled |

Two current PBS items were identified, and the identifiers are as recorded in the data compiled for this report (PBS item codes, not ARTG numbers).

<!-- review:begin au-lic-20261117-itraconazole-1 -->

> **Review correction (2026-11-17)**: Originally stated: "Only one registered product was identified, and the identifier is as recorded in the data compiled for this report (it should be verified against the ARTG)." Corrected: the earlier wording counted only the PBS items originally collected for this page. The data now include the current PBS items for this ingredient (PBS public data API, Schedule effective 2026-11-01). PBS listing does not show TGA (ARTG) registration status. Source: [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/).

<!-- review:end au-lic-20261117-itraconazole-1 -->

---

## Safety Considerations

Safety text from the Australian Product Information was not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

**Disease associations flagged in the knowledge graph (not label text):** long QT syndrome and torsades de pointes, congestive heart failure, cardiomyopathy and other myocardial disorders, coronary artery disease, liver disease and drug-induced liver injury, kidney disease, chronic obstructive pulmonary disease, peripheral neuropathy, hearing loss and vision disorders, and potassium deficiency. These should be verified against the PI.

**Drug interactions (DDInter, 100 interactions recorded; selected examples):**
- **Major:** loperamide, triamcinolone, budesonide
- **Moderate:** famotidine, ranitidine, cimetidine, omeprazole, rabeprazole, hydrocortisone, dexamethasone, betamethasone, alosetron, aprepitant
- **Minor:** metformin, pioglitazone, chlorpropamide, amphotericin B

Itraconazole is a CYP3A4 inhibitor, so extensive interactions are expected. Acid-suppressing drugs can also reduce absorption of some formulations.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction, pneumocystosis, has no clinical trials and no supporting literature. It also has a weak mechanistic basis, because *Pneumocystis* has little ergosterol. Evidence level is L5.
- The score appears to reflect the drug's antifungal class rather than a real therapeutic signal.

**Other predictions in the data compiled:**

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|

**To proceed, the following is needed:**
- Verification of the intervention arms in NCT00012467 and NCT00000639
- The Australian PI warnings, contraindications and approved indication text for ARTG 10732W
- A cardiac, hepatic and drug-interaction risk assessment before any new use is considered

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Australian data (the PBS Schedule of the Department of Health and Aged Care, and the TGA's ARTG). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-17 | Corrected: PBS item count updated to the current PBS Schedule | Corrected | [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Sporanox (itraconazole) prescribing information, Janssen Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a4d555fa-787c-40fb-bb7d-b0d4f7318fd0) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

