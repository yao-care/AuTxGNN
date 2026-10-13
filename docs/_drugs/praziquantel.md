---
layout: default
title: Praziquantel
parent: Model Prediction Only (L5)
nav_order: 597
evidence_level: L5
indication_count: 10
---

# Praziquantel
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

# Praziquantel: From Schistosomiasis and Liver Fluke Infections to Uterine Corpus Epithelioid Leiomyosarcoma

## One-Sentence Summary

Praziquantel is an anthelmintic originally used to treat opisthorchiasis, schistosomiasis, enterobiasis and trichinosis.
The TxGNN model predicts it may be effective for **uterine corpus epithelioid leiomyosarcoma** (the top-ranked prediction), but **no clinical trials and no publications** currently support this prediction.
The best-supported alternative among the top ten predictions is *Plasmodium falciparum* malaria, which has **2 related trials** (both indirect) and **one recent randomised trial** of praziquantel in asymptomatic infection.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Opisthorchiasis, schistosomiasis, enterobiasis, trichinosis (the ARTG entry carries no indication text) |
| Predicted New Indication | Uterine corpus epithelioid leiomyosarcoma |
| TxGNN Prediction Score | 97.28% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Praziquantel is known to act on schistosome calcium channels (TRPM_PZQ) and to disrupt the parasite's outer surface layer (tegument). This pharmacology has no established relevance to leiomyosarcoma biology.

The original indications are parasitic infections, and the predicted indication is a soft-tissue cancer. There is no clear biological bridge between them. The high score appears to be a graph-based signal, probably driven by shared sarcoma-class neighbours in the knowledge graph rather than by pharmacology. The same pattern appears for retroperitoneal sarcoma, uterine myxoid leiomyosarcoma, anal leiomyosarcoma, small intestinal sarcoma, leiomyosarcoma and dermatofibrosarcoma protuberans. None has any trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered for uterine corpus epithelioid leiomyosarcoma.

For context, the second-ranked prediction (*P. falciparum* malaria) has two registered trials. Both are indirect, studying co-infection and not praziquantel as an antimalarial.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02769013](https://clinicaltrials.gov/study/NCT02769013) | N/A | Completed | 380 | Effect of neglected tropical disease control on *P. falciparum* transmission in a co-endemic area |
| [NCT00347113](https://clinicaltrials.gov/study/NCT00347113) | N/A | Completed | 620 | Effect of schistosome and soil-transmitted helminth infection and anthelminthic treatment on malaria and anaemia in Tanzanian children |

## Literature Evidence

Currently no related literature available for uterine corpus epithelioid leiomyosarcoma.

The most relevant publications for the best-supported alternative predictions are below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41159886](https://pubmed.ncbi.nlm.nih.gov/41159886/) | 2026 | Randomised trial (double-blind, placebo-controlled) | J Infect Dis | Praziquantel for *P. falciparum* infection in asymptomatic Gabonese adults (full-text verification of results needed) |
| [10531774](https://pubmed.ncbi.nlm.nih.gov/10531774/) | 1998 | Small clinical series | JPMA | 8 of 10 malaria patients reported cured on praziquantel 30 mg/kg/day; two severe cases did not respond |
| [38265982](https://pubmed.ncbi.nlm.nih.gov/38265982/) | 2024 | Scoping review | PLoS Negl Trop Dis | Efforts to integrate malaria and schistosomiasis control programs |
| [9455057](https://pubmed.ncbi.nlm.nih.gov/9455057/) | 1997 | Clinical comparison | Kansenshogaku Zasshi | Bithionol versus praziquantel in fascioliasis (*Fasciola hepatica*) |
| [8218685](https://pubmed.ncbi.nlm.nih.gov/8218685/) | 1993 | Case reports and review | Clin Infect Dis | Praziquantel ineffective in two fascioliasis cases; bithionol appeared effective |
| [31847422](https://pubmed.ncbi.nlm.nih.gov/31847422/) | 2019 | Case report | Trop Med Infect Dis | *Gnathostoma spinigerum* emerged through the skin after praziquantel; anecdotal |

For fascioliasis, triclabendazole is the established drug of choice and praziquantel has shown poor efficacy. For gnathostomiasis, a nematode infection, praziquantel is not expected to work. Standard therapy is albendazole or ivermectin.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 15199Y | Praziquantel Tablets, USP 600 mg (Endo, USA) | Tablet 600 mg (s19A) | Not stated in the data compiled for this report |

This is a single, valid, oral product supplied under the Section 19A pathway (imported product not otherwise registered).

## Safety Considerations

- **Contraindications suggested by the knowledge graph (not label text):** epilepsy, liver disease, gallbladder disease, heart disease and cardiovascular disease.
- **Drug Interactions:** 83 interactions were identified. Those flagged **Major** in the data include:
  - Apalutamide
  - Phenobarbital
  - Carbamazepine

  Other listed interactions are Moderate (for example dexamethasone, bosentan, armodafinil, bexarotene, deferasirox) or Minor (cimetidine, albendazole). Enzyme-inducing drugs are a recurring theme.

Please refer to the TGA-approved Product Information (PI) for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, uterine corpus epithelioid leiomyosarcoma, is supported only by a graph-based score. There are no trials, no literature and no plausible mechanistic link. The malaria signal (evidence level L3) is more interesting but remains a research question, as existing trials are indirect and the key 2026 trial needs full-text review. Fascioliasis and gnathostomiasis are not recommended because better standard therapies exist.

**To proceed, the following is needed:**
- Mechanism of action data to assess any biological link to sarcoma
- For malaria: full-text review of PMID 41159886 and confirmation of the trial design, dose and outcomes
- Preclinical data (for example cell-line or animal studies) before any consideration of leiomyosarcoma
- The TGA PI warnings, contraindications and approved indication text for the ARTG entry
- A review of interaction risk with enzyme-inducing drugs for any proposed use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

