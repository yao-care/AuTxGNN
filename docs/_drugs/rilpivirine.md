---
layout: default
title: Rilpivirine
parent: Model Prediction Only (L5)
nav_order: 634
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "Rilpivirine: predicted new indication Feline acquired immunodeficiency syndrome . The best-evidenced predic… (evidence level L4). Approved use: HIV infectious disease"
monitor_inn: "Rilpivirine"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Rilpivirine
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

## Rilpivirine: From HIV Infection to Feline Acquired Immunodeficiency Syndrome
{: .text-alpha }

## One-Sentence Summary

Rilpivirine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) originally used to treat HIV infection and AIDS.
The TxGNN model's top-ranked prediction is feline acquired immunodeficiency syndrome. However, the best-supported prediction is **simian immunodeficiency virus (SIV) infection**, which has **no registered clinical trials** and **5 publications**, all preclinical or review articles.
Overall, this prediction is largely an extension of the existing HIV indication rather than a new human use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease; AIDS (the ARTG entry has no indication text in the data compiled for this report) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome (top-ranked by TxGNN; veterinary). The best-evidenced prediction is simian immunodeficiency virus infection (rank 2, an animal model of HIV) |
| TxGNN Prediction Score | 0.9997 (both feline AIDS and SIV infection) |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, rilpivirine is an NNRTI that allosterically inhibits HIV-1 reverse transcriptase. Its efficacy in HIV infection is established, and it may be mechanistically applicable to related lentiviral infections.

**Feline AIDS (rank 1):** Feline immunodeficiency virus (FIV) has a reverse transcriptase related to that of HIV. A 2023 biochemical and structural study compared NNRTIs, including rilpivirine, against FIV and HIV enzymes. The evidence is in vitro and indirect, with no in vivo or clinical data in cats. This is a veterinary indication with limited relevance to human drug repurposing.

**SIV infection (rank 2):** SIV and SHIV (a chimeric virus containing HIV-1 reverse transcriptase) are the standard macaque models of HIV, so rilpivirine's mechanism is directly relevant. Macaque studies of long-acting rilpivirine, alone or with cabotegravir, cover resistance selection, post-exposure prophylaxis and sustained remission after early treatment. These data mainly support the existing HIV indication and long-acting formulation development.

Another prediction, a genetic neurodevelopmental disorder, has no evidence or plausible mechanistic link. Its score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered for the lead predicted indications (feline AIDS and SIV infection).

## Literature Evidence

The table lists the 6 publications compiled for the two lead predictions. Preclinical studies are listed first, followed by a review.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | In vitro biochemical/structural study | J Vet Sci | Compared nevirapine, efavirenz and rilpivirine against feline and human immunodeficiency virus reverse transcriptase to assess NNRTI potential for FIV |
| [26438501](https://pubmed.ncbi.nlm.nih.gov/26438501/) | 2015 | Preclinical (macaque) | Antimicrob Agents Chemother | Long-acting rilpivirine selected drug-resistant variants at a low frequency in macaques infected with SIV containing HIV-1 reverse transcriptase |
| [41370971](https://pubmed.ncbi.nlm.nih.gov/41370971/) | 2026 | Preclinical (macaque) | EBioMedicine | Evaluated a single injection of long-acting cabotegravir plus rilpivirine as post-exposure prophylaxis |
| [39632836](https://pubmed.ncbi.nlm.nih.gov/39632836/) | 2024 | Preclinical (macaque) | Nat Commun | Early treatment with long-acting cabotegravir/rilpivirine plus oral emtricitabine/tenofovir alafenamide was studied for SHIV remission |
| [42040962](https://pubmed.ncbi.nlm.nih.gov/42040962/) | 2026 | Preclinical (newborn macaque) | Research Square | Long-acting lenacapavir with cabotegravir achieved sustained virologic remission in early-life SIV infection (rilpivirine not the focus) |
| [29746267](https://pubmed.ncbi.nlm.nih.gov/29746267/) | 2018 | Review | Curr Opin HIV AIDS | Review of cabotegravir for antiretroviral therapy and prevention (indirect for rilpivirine) |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 10298B | Edurant | Tablet 25 mg (as hydrochloride) | Not available in the data compiled for this report |

## Safety Considerations

- **Contraindications and disease associations (knowledge graph, not label text):** The knowledge graph links rilpivirine to long QT syndrome (including familial), torsades de pointes, liver failure, liver disease, fatty liver disease, non-alcoholic steatohepatitis, kidney disease, chronic hepatitis B virus infection, lactic acidosis, Fanconi renotubular syndrome, hypophosphataemia, osteomalacia, rickets, gallbladder disease, obesity disorders and pyoureter. Some of these entries likely reflect class effects of other antiretrovirals, and they should be verified against the label.
- **Drug interactions (100 recorded; main ones shown):**
  - **Major:** famotidine, ranitidine, cimetidine, omeprazole, esomeprazole, rabeprazole, dexlansoprazole, dexamethasone, dolasetron, cisapride. Acid-suppressing drugs are the key concern because rilpivirine absorption depends on gastric acidity.
  - **Moderate:** loperamide, aprepitant, bisacodyl, clarithromycin, magnesium oxide, aluminium hydroxide, calcium carbonate, castor oil, clotrimazole, polyethylene glycol with electrolytes.

For warnings and formal contraindications, please refer to the TGA-approved Product Information (PI).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predictions are either veterinary (feline AIDS) or animal models of the existing HIV indication (SIV/SHIV), supported only by in vitro and macaque data (Evidence Level L4). They do not represent a new human indication, and no clinical trials are registered.

**To proceed, the following is needed:**
- Mechanism of action data and the ARTG approved indication text
- TGA Product Information warnings and contraindications to complete safety screening
- If a human question is pursued, a focus on the human-relevant leads: long-acting rilpivirine in pregnancy and HIV/HCV coinfection (where one cohort suggests possible liver stiffness benefit), neither of which is anti-HCV efficacy
- Verification of knowledge graph contraindications (QT prolongation, hepatic and renal disease) against the PI
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

