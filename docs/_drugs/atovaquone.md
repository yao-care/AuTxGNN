---
layout: default
title: Atovaquone
parent: 僅模型預測 (L5)
nav_order: 64
evidence_level: L5
indication_count: 10
---

# Atovaquone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Atovaquone: From Malaria/PCP Prophylaxis to Toxoplasmosis

## One-Sentence Summary

Atovaquone is an antiprotozoal agent with established international use in treating and preventing malaria (as Malarone, with proguanil) and *Pneumocystis jirovecii* pneumonia (PCP) — though it is not currently registered in Australia.
The TxGNN model generated **10 new predicted indications**; of these, **Toxoplasmosis** carries the strongest evidence base, supported by **3 clinical trials** (including a completed Phase 2 RCT) and **20 publications**.
This report focuses on toxoplasmosis as the primary actionable repurposing candidate (Evidence Level L2), with a full summary of all 10 predictions provided below.

---

## All Predicted Indications — Summary Table

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-------------|----------------|----------------|
| 1 | Leprosy | 94.24% | L5 | Hold |
| 2 | Nocardiosis | 90.90% | L5 | Hold |
| 3 | Facial nerve palsy (herpes zoster) | 89.16% | L5 | Hold |
| 4 | Acne | 88.00% | L5 | Hold |
| **5** | **Toxoplasmosis** | **86.67%** | **L2** | **Proceed with Guardrails** |
| **6** | **Ocular toxoplasmosis** | **85.27%** | **L3** | **Research Question** |
| 7 | Creeping myiasis | 85.07% | L5 | Hold |
| 8 | Wound myiasis | 85.07% | L5 | Hold |
| 9 | Furuncular myiasis | 85.07% | L5 | Hold |
| 10 | Myiasis | 82.88% | L5 | Hold |

> **Note on Ranks 1–4 and 7–10:** These predictions received a **Hold** recommendation. Leprosy is caused by *Mycobacterium leprae* (a bacterium), and nocardiosis by *Nocardia* spp. — neither is susceptible to Atovaquone's antiprotozoal mechanism. Evidence for herpes zoster and acne is absent. The myiasis variants (insect larvae) are similarly outside Atovaquone's mechanistic scope. These indications are not explored further in this report.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Malaria prevention/treatment; Pneumocystis jirovecii pneumonia (PCP) prevention/treatment |
| Predicted New Indication (Primary) | Toxoplasmosis |
| TxGNN Prediction Score | 86.67% (Rank 5; highest evidence level among all predictions) |
| Evidence Level | L2 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Atovaquone is a hydroxynaphthoquinone compound that works by selectively inhibiting the **mitochondrial cytochrome bc1 complex (Complex III)** in susceptible protozoan parasites. Blocking this key step in the electron transport chain collapses mitochondrial membrane potential, starving the parasite of energy and driving cell death. Crucially, this selectivity is preferential for apicomplexan parasites, which are heavily dependent on mitochondrial respiration — making Atovaquone's therapeutic window considerably safer than many conventional antiprotozoals.

*Toxoplasma gondii* is an apicomplexan parasite — the same taxonomic class as *Plasmodium* (the malaria parasite). The cytochrome bc1 complex target is phylogenetically conserved across apicomplexans, meaning Atovaquone's mechanism of action against malaria translates directly and predictably to *Toxoplasma*. This is one of the most mechanistically coherent repurposing predictions in this dataset. Atovaquone also demonstrates activity against both **tachyzoites** (the acute replicating form) and **bradyzoites** (the chronic cyst form) — a distinct advantage over pyrimethamine and sulfadiazine, which are largely inactive against bradyzoites.

Clinically, this repurposing is not entirely novel: Atovaquone has been used internationally as a **second-line salvage therapy** for toxoplasmosis in patients intolerant to or failing standard treatment (pyrimethamine + sulfadiazine). A completed Phase 2 RCT (NCT00000794, n=100) provides the strongest direct evidence, and multiple retrospective studies and case series — including use in HIV-positive patients and immunosuppressed transplant recipients — have reported clinical response. The TxGNN prediction is therefore mechanistically grounded and supported by real-world clinical experience.

---

## Clinical Trial Evidence

### Toxoplasmosis (Primary)

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00000794](https://clinicaltrials.gov/study/NCT00000794) | Phase 2 | Completed | 100 | **Core evidence:** Phase 2 RCT directly comparing Atovaquone + pyrimethamine vs Atovaquone + sulfadiazine for acute toxoplasmic encephalitis in AIDS patients. Established efficacy and tolerability of Atovaquone-based regimens as alternatives to standard therapy. |
| [NCT00001994](https://clinicaltrials.gov/study/NCT00001994) | Pilot | Completed | N/A | Early pilot study evaluating Atovaquone (then coded 566C80) as salvage therapy for HIV patients with CNS toxoplasmosis who had failed or were intolerant of pyrimethamine-sulfadiazine. Established clinical feasibility. |
| [NCT01479361](https://clinicaltrials.gov/study/NCT01479361) | Phase 1 | Completed | 36 | Pharmacokinetic study assessing the impact of atazanavir/ritonavir and efavirenz on Atovaquone drug exposure. Directly relevant to dose optimisation in HIV-positive patients receiving toxoplasmosis prophylaxis or treatment. |

### Ocular Toxoplasmosis (Secondary Priority — L3)

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01479361](https://clinicaltrials.gov/study/NCT01479361) | Phase 1 | Completed | 36 | PK data from this study informs Atovaquone dosing in HIV-infected patients, including those with ocular manifestations of toxoplasmosis. Not an ocular-specific trial, but provides relevant drug-level guidance. |

---

## Literature Evidence

### Toxoplasmosis (Primary)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [30209035](https://pubmed.ncbi.nlm.nih.gov/30209035/) | 2018 | Comprehensive Review | *Clinical Microbiology Reviews* | Landmark review of toxoplasmosis treatment across decades; Atovaquone identified as a key alternative for patients failing or intolerant to pyrimethamine-sulfadiazine. Covers animal models, clinical practice, and emerging therapies. |
| [7588086](https://pubmed.ncbi.nlm.nih.gov/7588086/) | 1995 | Review | *Drugs* | Comprehensive pharmacology review confirming clinical efficacy of Atovaquone in both PCP and toxoplasmosis; evaluates tolerability relative to conventional regimens. |
| [8305784](https://pubmed.ncbi.nlm.nih.gov/8305784/) | 1993 | Review | *Annals of Pharmacotherapy* | Foundational review covering Atovaquone chemistry, pharmacokinetics, and clinical efficacy across opportunistic infections including toxoplasmosis. |
| [10471572](https://pubmed.ncbi.nlm.nih.gov/10471572/) | 1999 | Animal Study | *Antimicrobial Agents and Chemotherapy* | Demonstrated significant synergistic anti-*Toxoplasma* activity of clindamycin + Atovaquone in a murine acute toxoplasmosis model — supports combination therapy strategies. |
| [34595988](https://pubmed.ncbi.nlm.nih.gov/34595988/) | 2021 | Animal Study | *Ultrastructural Pathology* | Atovaquone-proguanil combination showed histological and ultrastructural efficacy in chronic murine toxoplasmosis — relevant to the challenge of treating tissue cyst forms. |
| [25309522](https://pubmed.ncbi.nlm.nih.gov/25309522/) | 2014 | Animal Study | *Frontiers in Microbiology* | Novel synergistic anti-*Toxoplasma* effect of diclazuril + Atovaquone in animal model; explored potential for prevention of congenital and chronic toxoplasmosis syndromes. |
| [29452213](https://pubmed.ncbi.nlm.nih.gov/29452213/) | 2018 | Formulation/Animal Study | *European Journal of Pharmaceutical Sciences* | Atovaquone nanoemulsion markedly improved bioavailability and *in vivo* efficacy in acute and chronic toxoplasmosis — addresses the known challenge of Atovaquone's poor aqueous solubility. |
| [37683834](https://pubmed.ncbi.nlm.nih.gov/37683834/) | 2023 | Animal Study | *Microbial Pathogenesis* | Investigated miR-146a, BAG-1, IL-6, and IL-10 tissue levels in cerebral toxoplasmosis following Atovaquone + clindamycin treatment; provides mechanistic insight into treatment response monitoring. |
| [40788706](https://pubmed.ncbi.nlm.nih.gov/40788706/) | 2025 | Retrospective Cohort | *Gut Microbes* | Large retrospective cohort (n >100,000) found Atovaquone-proguanil associated with reduced digestive cancer risk, hypothesised to occur via *T. gondii* suppression — novel signal with potential broader implications. |
| [27384853](https://pubmed.ncbi.nlm.nih.gov/27384853/) | 2016 | Case Report | *Japanese Journal of Clinical Hematology* | Successful early diagnosis and Atovaquone-based treatment of disseminated toxoplasmosis following cord blood transplantation in a severely immunocompromised patient. |

### Ocular Toxoplasmosis (Secondary Priority — L3)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [9917796](https://pubmed.ncbi.nlm.nih.gov/9917796/) | 1999 | Retrospective Clinical Study | *Ophthalmology* | Phase I trial evaluating Atovaquone safety and efficacy specifically for ocular toxoplasmosis (retinochoroiditis) in immunocompetent patients — direct evidence for this sub-indication. |
| [19108794](https://pubmed.ncbi.nlm.nih.gov/19108794/) | 2008 | Retrospective Chart Review | *Clinical Therapeutics* | Evaluated adverse drug reactions across treatments for active toxoplasmic chorioretinitis; Atovaquone data included as an alternative agent. |
| [7616727](https://pubmed.ncbi.nlm.nih.gov/7616727/) | 1995 | Case Report | *Klinische Monatsblätter für Augenheilkunde* | Early case report of Atovaquone successfully treating toxoplasma retinochoroiditis in an HIV-infected patient intolerant to standard drugs. |
| [9044964](https://pubmed.ncbi.nlm.nih.gov/9044964/) | 1996 | Case Report | *Klinische Monatsblätter für Augenheilkunde* | First report describing Atovaquone treatment of ocular toxoplasmosis in an immunocompetent patient, noting its activity against both tachyzoites and bradyzoites. |
| [20437247](https://pubmed.ncbi.nlm.nih.gov/20437247/) | 2010 | Retrospective Clinical Study | *Graefe's Archive for Clinical and Experimental Ophthalmology* | Evaluated whether Atovaquone prolongs disease-free intervals in toxoplasmic retinochoroiditis — addresses the key clinical question of secondary prevention. |

---

## Australia Market Information

Atovaquone is **not currently registered with the Therapeutic Goods Administration (TGA)** and holds **no ARTG entries** as a standalone product.

> **Important clarification:** Malarone® (atovaquone 250 mg + proguanil 100 mg) is TGA-registered and marketed in Australia for malaria prevention and treatment. However, atovaquone as a monotherapy (e.g., Mepron® 750 mg/5 mL suspension, as used in PCP and toxoplasmosis) is **not ARTG-listed**.

Clinical use in Australia would require access through one of the following TGA pathways:

| Access Pathway | Details |
|----------------|---------|
| **Special Access Scheme (SAS) — Category B** | For individual patients with serious or life-threatening conditions; requires clinician application and TGA approval |
| **Authorised Prescriber** | For eligible specialists treating a defined class of patients (e.g., infectious disease specialists managing immunocompromised patients) |
| **Clinical Trial** | If a formal Australian trial is initiated for this indication |

---

## Safety Considerations

Specific TGA-approved Product Information for atovaquone monotherapy is unavailable, as the product is not registered in Australia. Based on the published literature and international regulatory data (FDA/EMA):

- **Bioavailability is highly food-dependent:** Atovaquone must be taken with a fatty meal; administration without food can reduce bioavailability by up to 50%
- **Drug interactions of clinical concern:** Rifampicin and rifabutin markedly reduce Atovaquone plasma levels (contraindicated in some guidelines); metoclopramide also reduces absorption; antiretrovirals (particularly efavirenz and atazanavir/ritonavir) alter drug exposure (see NCT01479361)
- **Common adverse effects:** Rash, nausea, diarrhoea, headache, and elevated liver enzymes — generally mild to moderate in severity
- **No myelosuppression** reported — an important advantage over pyrimethamine-based regimens in immunocompromised patients

> For comprehensive safety information, please refer to the FDA-approved Prescribing Information for Mepron® (atovaquone) and the relevant Product Information from EMA-approved jurisdictions.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(for Toxoplasmosis)*

**Rationale:**
Toxoplasmosis is the only predicted indication in this dataset with a mechanistically sound basis and clinically meaningful evidence — a completed Phase 2 RCT, pilot trial data, and extensive observational/case series experience collectively support Atovaquone's role as a second-line treatment. The convergence of phylogenetic relatedness, conserved drug target, and real-world clinical usage makes this repurposing application credible and actionable, particularly for patients intolerant to pyrimethamine-sulfadiazine.

**To proceed, the following is needed:**

- **Regulatory access:** Submit a TGA SAS Category B application for atovaquone monotherapy for clinically indicated toxoplasmosis cases (e.g., immunocompromised patients intolerant to standard treatment)
- **Procurement:** Identify a suitable international supplier for Mepron® (atovaquone 750 mg/5 mL oral suspension), given no Australian supplier exists
- **Drug interaction management:** Establish a monitoring protocol for patients co-prescribed rifampicin, rifabutin, or antiretrovirals — therapeutic drug monitoring of atovaquone plasma levels should be considered
- **MOA documentation:** Source formal drug product information from FDA/EMA for inclusion in clinical governance documentation (DrugBank MOA data was unavailable in this Evidence Pack)
- **Secondary priority — Ocular toxoplasmosis (L3):** Commission a systematic review or prospective case series of Atovaquone for toxoplasmic retinochoroiditis in Australian centres managing immunocompromised patients; existing retrospective data (PMID 9917796, PMID 20437247) provides sufficient preliminary support to justify structured evidence collection

> **Disclaimer:** This report is for research purposes only and does not constitute medical advice. Any clinical repurposing application requires prospective clinical validation and appropriate regulatory approval.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

