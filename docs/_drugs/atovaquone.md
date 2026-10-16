---
layout: default
title: Atovaquone
parent: High Evidence (L1-L2)
nav_order: 69
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-13
description: "Atovaquone: predicted new indication Toxoplasmosis (evidence level L2). Approved use: Malaria (including Plasmodium falciparum malaria) and pneumocystosis"
---

# Atovaquone
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Atovaquone: From Malaria and Pneumocystosis to Toxoplasmosis

## One-Sentence Summary

Atovaquone is an antiprotozoal drug originally used to treat malaria (including *Plasmodium falciparum*) and pneumocystosis.
The TxGNN model's top-ranked prediction is leprosy, but the best-supported candidate in the data compiled for this report is **Toxoplasmosis** (TxGNN score 86.67%), supported by **3 clinical trials** (one completed Phase 2 randomised open-label trial) and **19 publications**.
The leprosy prediction has no supporting trials and only one unrelated publication, so this report focuses on toxoplasmosis and covers the other predictions briefly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Malaria (including *Plasmodium falciparum* malaria) and pneumocystosis (from the knowledge graph; the ARTG entry carries no indication text) |
| Predicted New Indication | Toxoplasmosis (best-supported candidate; the top-ranked TxGNN prediction is leprosy, score 94.24%, evidence level L5) |
| TxGNN Prediction Score | 86.67% (toxoplasmosis) |
| Evidence Level | L2 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Atovaquone is a hydroxynaphthoquinone that inhibits the parasite mitochondrial cytochrome bc1 complex, disrupting electron transport and pyrimidine synthesis. Detailed mechanism of action data was not available in the structured drug record, so this description comes from the literature reviewed for this report.

Malaria (*Plasmodium*), pneumocystosis and toxoplasmosis are all caused by organisms that depend on this mitochondrial pathway. *Toxoplasma gondii* is an apicomplexan parasite, closely related to *Plasmodium*. The reviews retrieved describe atovaquone as an alternative regimen for toxoplasmic encephalitis, with activity against cyst forms in animal models. This is important because the standard pyrimethamine-sulfadiazine combination does not eradicate tissue cysts.

Caveats: the Phase 2 trial is open-label with a modest sample, the other studies are a non-randomised pilot and a Phase 1 pharmacokinetic study, and primary outcome data were not available. Atovaquone also has variable intestinal absorption, which may limit its use.

**Other predictions (brief):**
- **Ocular toxoplasmosis (score 85.27%, evidence level L3):** Small clinical studies and case reports support atovaquone for retinochoroiditis (for example, a Phase 1 trial in immunocompetent patients, PMID 9917796). There are also reports of reactivation during therapy (PMID 16766403). No registered trials were found. This is best treated as a research question.
- **Leprosy (94.24%, L5):** Model prediction only. The only publication retrieved concerns clofazimine for *Babesia*, not atovaquone for leprosy.
- **Nocardiosis (90.90%, L4):** No evidence of benefit. One cohort report (PMID 29555315) links atovaquone prophylaxis with more nocardial infections, because it replaces TMP-SMX, which is active against *Nocardia*. This points away from repurposing.
- **Facial nerve palsy due to herpes zoster, acne, and myiasis (creeping, wound, furuncular and unspecified):** Predictions only, with no trials or literature and no supported mechanism.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00000794](https://clinicaltrials.gov/study/NCT00000794) | Phase 2 | Completed | 100 | Randomised open-label comparison of atovaquone plus pyrimethamine vs atovaquone plus sulfadiazine for acute toxoplasmic encephalitis in AIDS patients, aiming to avoid the severe toxicity of standard therapy |
| [NCT00001994](https://clinicaltrials.gov/study/NCT00001994) | N/A (pilot) | Completed | Not reported | Salvage treatment with atovaquone (566C80) for CNS toxoplasmosis in HIV patients who failed or could not tolerate pyrimethamine-sulfadiazine |
| [NCT01479361](https://clinicaltrials.gov/study/NCT01479361) | Phase 1 | Completed | 36 | Pharmacokinetic study of atazanavir-ritonavir and efavirenz effects on atovaquone exposure in HIV-infected volunteers (informs dosing and interactions, not efficacy) |

No ANZCTR trials were identified in the data compiled for this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30209035](https://pubmed.ncbi.nlm.nih.gov/30209035/) | 2018 | Review | Clin Microbiol Rev | Treatment of toxoplasmosis; pyrimethamine-sulfadiazine remains the gold standard, with alternatives needed when it fails |
| [7588086](https://pubmed.ncbi.nlm.nih.gov/7588086/) | 1995 | Review | Drugs | Atovaquone as an alternative agent in opportunistic infections (PCP and toxoplasmosis) |
| [11890349](https://pubmed.ncbi.nlm.nih.gov/11890349/) | 2001 | Review | Curr Opin Investig Drugs | Atovaquone is promising against cysts but limited by variable intestinal absorption |
| [9917796](https://pubmed.ncbi.nlm.nih.gov/9917796/) | 1999 | Clinical study (Phase 1) | Ophthalmology | Safety and efficacy of atovaquone for toxoplasma retinochoroiditis in immunocompetent patients |
| [20437247](https://pubmed.ncbi.nlm.nih.gov/20437247/) | 2010 | Clinical study | Graefes Arch Clin Exp Ophthalmol | Whether atovaquone prolongs the disease-free interval of toxoplasmic retinochoroiditis |
| [16766403](https://pubmed.ncbi.nlm.nih.gov/16766403/) | 2006 | Case report | Ocul Immunol Inflamm | Reactivation of retinochoroiditis during atovaquone therapy |
| [25309522](https://pubmed.ncbi.nlm.nih.gov/25309522/) | 2014 | Preclinical (animal) | Front Microbiol | Synergy of diclazuril plus atovaquone in toxoplasmosis |
| [34595988](https://pubmed.ncbi.nlm.nih.gov/34595988/) | 2021 | Preclinical (mouse) | Ultrastruct Pathol | Atovaquone-proguanil in chronic murine toxoplasmosis |
| [29452213](https://pubmed.ncbi.nlm.nih.gov/29452213/) | 2018 | Preclinical | Eur J Pharm Sci | Atovaquone nanoemulsion to improve bioavailability and efficacy in toxoplasmosis |
| [40788706](https://pubmed.ncbi.nlm.nih.gov/40788706/) | 2025 | Retrospective cohort | Gut Microbes | Atovaquone-proguanil associated with reduced colorectal cancer risk, with a proposed *Toxoplasma* link |

No randomised controlled trial publications were retrieved.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 8300W | Wellvone | Oral suspension 750 mg per 5 mL, 210 mL | Not available in the data compiled for this report |

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph (not label text):** liver failure, liver disease, gallbladder disease, hyperglycaemia, chronic diarrhoeal disease. These should be verified against the Product Information.
- **Drug interactions (100 recorded; main moderate-level examples):** metoclopramide, naltrexone, tetracycline and picosulfuric acid. Other recorded interactions have unknown severity (for example metformin, omeprazole, morphine, prednisone and vancomycin). A Phase 1 study (NCT01479361) examined how atazanavir-ritonavir and efavirenz affect atovaquone exposure.
- Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (toxoplasmosis only; Hold for all other predicted indications)

**Rationale:**
- A completed Phase 2 randomised trial and a pilot study directly support atovaquone for toxoplasmic encephalitis, backed by a plausible shared mechanism with its approved antiprotozoal uses. The evidence is limited by open-label design, small size and the absence of Phase 3 data.
- Higher-scoring predictions, such as leprosy and nocardiosis, have no supporting evidence, and the nocardiosis data point the other way.

**To proceed, the following is needed:**
- Primary outcome data from NCT00000794 and NCT00001994
- Review of the TGA Product Information for warnings, contraindications and approved indications (the current ARTG record lacks this text)
- Confirmed mechanism of action data from DrugBank
- Assessment of absorption variability and dosing for toxoplasmosis, and a monitoring plan for patients with liver disease
- Pharmacokinetic and efficacy data for ocular toxoplasmosis if that indication is pursued as a research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

