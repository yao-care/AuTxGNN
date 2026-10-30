---
layout: default
title: Enzalutamide
parent: Model Prediction Only (L5)
nav_order: 256
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-30
monitor_inn: "Enzalutamide"
predicted_indications: ["prostate leiomyoma", "Brenner tumor", "fibroma of prostate", "benign reproductive system neoplasm", "benign prostate phyllodes tumor"]
description: "Enzalutamide: predicted new indication Prostate leiomyoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Enzalutamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Enzalutamide: Prostate leiomyoma
{: .text-alpha }

## One-Sentence Summary

Enzalutamide is an androgen receptor inhibitor originally used to treat prostate cancer.
The TxGNN model's top-ranked prediction with substantive evidence is **Prostate leiomyoma** (score 0.9957), with **36 clinical trials** and **20 publications** supporting this direction.
This is effectively an on-label use rather than true repurposing, so it validates the model rather than revealing a new indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Prostate leiomyoma |
| TxGNN Prediction Score | 0.9957 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in the data compiled for this report. From the trial and literature records, enzalutamide is a second-generation androgen receptor (AR) antagonist. It blocks androgen binding to the receptor, prevents nuclear translocation of the receptor, and blocks receptor binding to DNA.

"Prostate neoplasm" is the broader category that contains prostate cancer, the drug's established indication. The high prediction score therefore reflects ontology proximity to the approved use. Phase 3 trials support enzalutamide across the prostate cancer disease spectrum: metastatic hormone-sensitive disease (ARCHES), non-metastatic castration-resistant disease (PROSPER), post-chemotherapy metastatic castration-resistant disease (AFFIRM) and biochemically recurrent disease (EMBARK).

Several other high-scoring predictions are rare or benign prostate tumours (fibroma of prostate, benign prostate phyllodes tumour) or unrelated conditions (Brenner tumour). These have no trial or literature evidence, and no androgen receptor dependency has been shown. Their scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, so they should not be pursued without new evidence.

---

## Clinical Trial Evidence

Trials registered for prostate neoplasm (up to 10 most relevant shown; the full set contains 36 trials):

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02446405](https://clinicaltrials.gov/study/NCT02446405) (ENZAMET) | Phase 3 | Active, not recruiting | 1125 | Enzalutamide vs conventional non-steroidal antiandrogen with first-line ADT in metastatic prostate cancer. Led in part by Australian investigators. |
| [NCT06551324](https://clinicaltrials.gov/study/NCT06551324) (MEVPRO-1) | Phase 3 | Active, not recruiting | 600 | Mevrometostat plus enzalutamide vs enzalutamide or docetaxel in mCRPC after abiraterone |
| [NCT02987543](https://clinicaltrials.gov/study/NCT02987543) (PROfound) | Phase 3 | Completed | 387 | Olaparib vs enzalutamide or abiraterone in mCRPC with HRR gene mutations |
| [NCT03834493](https://clinicaltrials.gov/study/NCT03834493) (KEYNOTE-641) | Phase 3 | Terminated | 1244 | Pembrolizumab plus enzalutamide vs placebo plus enzalutamide in mCRPC |
| [NCT06136624](https://clinicaltrials.gov/study/NCT06136624) (OMAHA-003) | Phase 3 | Recruiting | 1310 | Opevesostat vs abiraterone or enzalutamide in mCRPC after prior NHA and taxane |
| [NCT06496581](https://clinicaltrials.gov/study/NCT06496581) (PEACE-6) | Phase 3 | Recruiting | 500 | Standard of care with or without 177Lu-PSMA-617 in de novo mHSPC. Enzalutamide is background therapy. |
| [NCT05393791](https://clinicaltrials.gov/study/NCT05393791) (ANZadapt) | Phase 2 | Recruiting | 168 | Adaptive vs continuous abiraterone or enzalutamide in mCRPC (Australia and New Zealand) |
| [NCT07512076](https://clinicaltrials.gov/study/NCT07512076) | Phase 2 | Not yet recruiting | 26 | Enzalutamide dose optimisation in elderly patients with advanced prostate cancer |
| [NCT03641560](https://clinicaltrials.gov/study/NCT03641560) | Phase 4 | Completed | 52 | Safety and efficacy of enzalutamide in Indian patients with post-docetaxel mCRPC |
| [NCT07751133](https://clinicaltrials.gov/study/NCT07751133) | Phase 3 | Recruiting | 1500 | Reduced-dose vs standard-dose ARPI in metastatic prostate cancer (overall survival non-inferiority) |

No ANZCTR identifiers were included in the data compiled for this report. ENZAMET and ANZadapt have Australian involvement, so ANZCTR cross-registration should be checked.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31329516](https://pubmed.ncbi.nlm.nih.gov/31329516/) | 2019 | RCT | J Clin Oncol | ARCHES: enzalutamide plus ADT in metastatic hormone-sensitive prostate cancer |
| [29949494](https://pubmed.ncbi.nlm.nih.gov/29949494/) | 2018 | RCT | N Engl J Med | Enzalutamide delayed metastasis in non-metastatic castration-resistant prostate cancer |
| [22894553](https://pubmed.ncbi.nlm.nih.gov/22894553/) | 2012 | RCT | N Engl J Med | AFFIRM: increased survival with enzalutamide after chemotherapy |
| [41124201](https://pubmed.ncbi.nlm.nih.gov/41124201/) | 2026 | RCT | N Engl J Med | EMBARK: improved survival with enzalutamide in biochemically recurrent prostate cancer |
| [42223064](https://pubmed.ncbi.nlm.nih.gov/42223064/) | 2026 | RCT | N Engl J Med | PARP inhibitor plus androgen-signalling inhibition plus ADT in metastatic prostate cancer |
| [41633900](https://pubmed.ncbi.nlm.nih.gov/41633900/) | 2026 | Post hoc analysis | Eur Urol | ARCHES 5-year survival with enzalutamide plus ADT |
| [40439959](https://pubmed.ncbi.nlm.nih.gov/40439959/) | 2025 | Comparative analysis | Adv Ther | Overall survival with apalutamide vs enzalutamide in mCSPC |
| [32534790](https://pubmed.ncbi.nlm.nih.gov/32534790/) | 2020 | Review | Trends Cancer | Treatment advances in advanced prostate cancer |
| [39275993](https://pubmed.ncbi.nlm.nih.gov/39275993/) | 2024 | Review | Expert Rev Anticancer Ther | Current uses and resistance mechanisms of enzalutamide |
| [38859590](https://pubmed.ncbi.nlm.nih.gov/38859590/) | 2024 | Preclinical | Adv Sci | Enzalutamide sensitises CRPC cells to copper-mediated cell death |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 10174L | Xtandi | Capsule 40 mg (oral) | Not specified in the data compiled for this report |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted hormonal therapy (androgen receptor inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI. Seizure risk, falls and fatigue should be considered clinically. |
| Handling Protection | Please refer to the PI and local handling policies |

---

## Safety Considerations

Label warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for these.

- **Drug Interactions**: 100 interactions were listed, mainly moderate. The major-level interactions identified were:
  - Bupropion
  - Dolasetron
  - Eliglustat

  Moderate interactions include famotidine, rabeprazole, omeprazole, hydrocortisone, dexamethasone, clarithromycin, aprepitant, loperamide, saxagliptin, linagliptin and empagliflozin. Enzalutamide is known to be a strong CYP3A4 inducer and also affects CYP2C8, so a full medication review is needed before use.
- **Clinical considerations from the evidence review**: seizure risk, falls and fatigue, and caution in elderly patients. For the benign prostate neoplasm prediction, sexual dysfunction would also need assessment, as safety in that population has not been evaluated.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for prostate neoplasm, as on-label prostate cancer use). **Hold** for all other predicted indications (susceptibility label, prostate leiomyoma, Brenner tumour, prostate fibroma, benign and malignant phyllodes tumours).

**Rationale:**
- Multiple large Phase 3 RCTs support enzalutamide across prostate cancer disease states, and it is already marketed in Australia as Xtandi. The prediction confirms existing use rather than identifying a new indication.
- The novel predictions have no clinical or literature evidence, and a mechanistic link is not established.

**To proceed, the following is needed:**
- Mechanism of action data to be retrieved (DrugBank)
- Product Information warnings and contraindications to be retrieved from the TGA, since the safety screening could not be completed
- The approved indication text for ARTG 10174L, for comparison with the predicted indication
- Confirmation of the ARTG entry count, as only one entry was found
- A safety monitoring plan for elderly patients and those on interacting medicines
- For any novel indication (such as benign prostate neoplasms), preclinical or early-phase evidence of androgen receptor dependency and a benefit-risk assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

