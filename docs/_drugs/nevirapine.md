---
layout: default
title: Nevirapine
parent: Model Prediction Only (L5)
nav_order: 498
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
monitor_inn: "Nevirapine"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
description: "Nevirapine: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Nevirapine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Nevirapine: Feline acquired immunodeficiency syndrome
{: .text-alpha }

## One-Sentence Summary

Nevirapine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, a veterinary condition, but this top-ranked prediction rests on **0 clinical trials** and **1 in vitro publication**, and the publication suggests the feline virus is poorly susceptible to NNRTIs.
The more clinically relevant lower-ranked predictions (congenital HIV and AIDS-related complex) largely match the drug's established HIV use rather than representing true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 (preclinical/biochemical only) |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, nevirapine is an NNRTI that targets lentiviral reverse transcriptase, and its efficacy in HIV-1 infection is established. Feline immunodeficiency virus (FIV) is also a lentivirus, so a mechanistic overlap is conceivable.

However, the one retrieved study (a 2023 biochemical and structural comparison of NNRTIs against feline and human immunodeficiency viruses) indicates that FIV reverse transcriptase is generally poorly susceptible to NNRTIs. The high prediction score is therefore not supported by an established mechanism. This is also a veterinary indication, not a human repurposing target.

The same pattern appears for the second-ranked prediction, simian immunodeficiency virus infection. SIVmac and HIV-2 are intrinsically resistant to NNRTIs, and only engineered SIV/HIV-1 chimeras carrying HIV-1 reverse transcriptase respond to nevirapine. This is useful for animal-model research, not clinical repurposing.


Two further predictions are more clinically interesting, though they largely reflect established HIV uses:
- **Congenital HIV** (Evidence Level L1): nevirapine is established for preventing mother-to-child transmission.
- **AIDS-related complex** (Evidence Level L2): this is a historical term for symptomatic HIV infection, matching the original indication.

---

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked prediction (feline acquired immunodeficiency syndrome). Currently no related clinical trials registered.

For reference, the trials below relate to the two clinically relevant lower-ranked predictions, which essentially describe established HIV use.

**Congenital HIV**

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00102960](https://clinicaltrials.gov/study/NCT00102960) | Phase 3 | Completed | 377 | Randomised open-label trial comparing antiretroviral treatment strategies of different lengths in infants infected at birth |
| [NCT00021671](https://clinicaltrials.gov/study/NCT00021671) | Phase 3 | Completed | 3720 | Antibiotics to reduce chorioamnionitis-related perinatal HIV transmission; nevirapine is not the tested intervention |

**AIDS-related complex**

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00000770](https://clinicaltrials.gov/study/NCT00000770) | Phase 2 | Completed | 400 | Zidovudine + didanosine + double-blind nevirapine versus zidovudine + didanosine |
| [NCT00002324](https://clinicaltrials.gov/study/NCT00002324) | Phase 2 | Completed | 250 | Placebo-controlled trial of nevirapine alone or with zidovudine in asymptomatic HIV-1 infection, measuring CD4 counts and safety |
| [NCT00002347](https://clinicaltrials.gov/study/NCT00002347) | Phase 2 | Completed | 225 | Master protocol of multi-drug antiretroviral combinations, including zidovudine/zalcitabine with nevirapine |
| [NCT00000747](https://clinicaltrials.gov/study/NCT00000747) | Phase 2 | Completed | 10 | Pilot study of nevirapine resistance development in patients with CD4 counts ≥500/mm³ |
| [NCT00000814](https://clinicaltrials.gov/study/NCT00000814) | Phase 1 | Completed | 390 | Zidovudine, didanosine and nevirapine combination in children and adolescents with advanced HIV |
| [NCT00000808](https://clinicaltrials.gov/study/NCT00000808) | Phase 1 | Completed | 49 | Safety and pharmacokinetics of nevirapine in HIV-infected pregnant women and neonates |
| [NCT00000962](https://clinicaltrials.gov/study/NCT00000962) | Phase 1 | Completed | 30 | Rising-dose safety, tolerance and activity study of nevirapine (BI-RG-587) |
| [NCT00000649](https://clinicaltrials.gov/study/NCT00000649) | Phase 1 | Completed | 30 | Pharmacokinetics and safety of nevirapine with zidovudine |

---

## Literature Evidence

**Feline acquired immunodeficiency syndrome (top-ranked prediction)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | In vitro / structural | J Vet Sci | Compared nevirapine, efavirenz and rilpivirine against FIV and HIV reverse transcriptase; FIV reverse transcriptase is generally poorly susceptible to NNRTIs |

**Congenital HIV (established use)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15249569](https://pubmed.ncbi.nlm.nih.gov/15249569/) | 2004 | RCT | JAMA | Nevirapine plus zidovudine at birth to reduce perinatal HIV transmission in an African setting |
| [19236121](https://pubmed.ncbi.nlm.nih.gov/19236121/) | 2009 | Systematic review | Drug Saf | Hepatotoxicity with long- versus short-course prophylactic nevirapine |
| [29912896](https://pubmed.ncbi.nlm.nih.gov/29912896/) | 2018 | Systematic review / network meta-analysis | PLoS One | Comparative safety and effectiveness of perinatal antiretroviral therapies |
| [15794723](https://pubmed.ncbi.nlm.nih.gov/15794723/) | 2005 | Review | Expert Opin Drug Saf | Safety of antiretrovirals in pregnancy, including nevirapine-associated hepatotoxicity in women |

**AIDS-related complex (established use)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17620824](https://pubmed.ncbi.nlm.nih.gov/17620824/) | 2007 | Review | Curr Opin Allergy Clin Immunol | Drug hypersensitivity is far more common in people with HIV |
| [21505298](https://pubmed.ncbi.nlm.nih.gov/21505298/) | 2011 | Pharmacogenomic study | AIDS | Genetic variants associated with nevirapine cutaneous and hepatic adverse events across populations |
| [27067022](https://pubmed.ncbi.nlm.nih.gov/27067022/) | 2016 | In vitro | AIDS Res Hum Retroviruses | Novel RT mutations (L228I, Y232H) cause NNRTI resistance |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10304H | Nevirapine Viatris | Tablet 200 mg (oral) | Not available in the data compiled for this report |

---

## Safety Considerations

The data compiled for this report contain no label-based warnings or contraindications. The following items come from a knowledge graph and drug interaction database, not from product label text.

- **Knowledge-graph contraindication signals**: liver failure, liver disease, drug-induced liver injury, gallbladder disease, chronic hepatitis B and C virus infection, exanthem, Stevens-Johnson syndrome, toxic epidermal necrolysis (Lyell syndrome), rhabdomyolysis and nodular fasciitis.
- **Literature-supported concerns**: hepatotoxicity and severe skin reactions (including with longer-course prophylactic use), and NNRTI resistance emergence after single-dose exposure.
- **Drug interactions**: 100 interactions were identified; the 20 listed are all rated Moderate. They include rabeprazole, bupropion, aprepitant, triamcinolone, dexamethasone, betamethasone, budesonide, clarithromycin, saxagliptin, eliglustat, linagliptin, naldemedine, naloxegol, naltrexone, cisapride, granisetron, nitisinone, ondansetron, orlistat and prednisolone.

Please refer to the TGA-approved Product Information (PI) for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (feline AIDS) is a veterinary indication supported only by in vitro data, and that data suggests FIV is poorly susceptible to nevirapine. There are no clinical trials, so the evidence level is L4.
- The two clinically relevant predictions (congenital HIV and AIDS-related complex) are largely established HIV uses rather than new repurposing opportunities. They could be considered "Proceed with Guardrails" for hepatotoxicity, rash, resistance and interaction risks, but they do not represent novel indications for Australia.

**To proceed, the following is needed:**
- Mechanism of action data for nevirapine, which was not available.
- TGA Product Information warnings and contraindications, which were not available and block safety screening.
- For any veterinary exploration, direct susceptibility testing of FIV reverse transcriptase to nevirapine and, if positive, in vivo studies.
- For perinatal use, a review of current Australian guidelines, since newer regimens (for example dolutegravir-based) have largely replaced nevirapine-based prophylaxis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

