---
layout: default
title: Abemaciclib
parent: Moderate Evidence (L3-L4)
nav_order: 13
evidence_level: L4
indication_count: 10
---

# Abemaciclib
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Abemaciclib: From Breast Cancer to Rheumatoid Arthritis

## One-Sentence Summary

Abemaciclib (Verzenio) is an oral CDK4/6 inhibitor marketed in Australia; the data compiled for this report did not include approved indication text, but the literature identifies its established use as hormone receptor-positive, HER2-negative breast cancer.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but there are **no registered clinical trials** and only **2 publications** (one observational study and one preclinical study) for this direction.
The evidence is at the model-prediction and early preclinical stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the ARTG data compiled for this report (literature indicates HR+/HER2- breast cancer) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 97.32% |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Abemaciclib is a known inhibitor of cyclin-dependent kinases 4 and 6 (CDK4/6), which control progression through the cell cycle. Based on this class effect, it is plausible that it could be applicable to rheumatoid arthritis (RA).

RA is characterised by overgrowth (hyperplasia) of fibroblast-like synoviocytes in the joint lining. These cells proliferate rapidly and resist apoptosis. Blocking cell-cycle progression could, in principle, slow this proliferation and also modulate immune cell cycling. This is the main mechanistic rationale linking an anticancer CDK4/6 inhibitor to an autoimmune joint disease.

The supporting literature is limited. One observational study examined immune-mediated diseases in breast cancer patients taking CDK4/6 inhibitors, and one preclinical study tested an abemaciclib-loaded nanoplatform against synoviocytes. Neither is a clinical efficacy study in RA patients. Notably, the observational study also raises the possibility that CDK4/6 inhibitors may trigger autoimmune reactions, so the direction of effect is uncertain.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for rheumatoid arthritis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40504547](https://pubmed.ncbi.nlm.nih.gov/40504547/) | 2025 | Cohort | The Oncologist | Investigated pre-existing and emerging autoimmune diseases in HR+/HER2- breast cancer patients on CDK4/6 inhibitors plus endocrine therapy, noting these drugs may both enhance antitumour immunity and trigger autoimmune reactions |
| [42289719](https://pubmed.ncbi.nlm.nih.gov/42289719/) | 2026 | Preclinical | Journal of Nanobiotechnology | A pH-responsive nanoplatform loaded with abemaciclib was designed to induce cell cycle arrest and apoptosis in RA fibroblast-like synoviocytes |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11868P | Verzenio | Tablet 150 mg | Not available in the compiled data |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (CDK4/6 kinase inhibitor) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI; typically includes FBC, liver function and renal function |
| Handling Protection | Please refer to the PI and local cytotoxic drug handling policies |

---

## Safety Considerations

Label warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for these.

**Drug Interactions:** 100 interactions were recorded in total; 20 are shown in the data compiled. Major-level interactions include:
- Clarithromycin
- Cobicistat
- Deferiprone
- Samarium (153Sm) lexidronam
- Lumacaftor

Moderate-level interactions include aprepitant, clotrimazole, dexamethasone, metformin, metreleptin, naltrexone, troglitazone, deferasirox, palifermin, strontium chloride Sr-89, ticagrelor, roflumilast, chloramphenicol, erythromycin and fluconazole.

**Other safety signals from the literature:** Pharmacovigilance and review articles describe cardiovascular concerns with CDK4/6 inhibitors, including QTc prolongation, thromboembolic events and atrial arrhythmia, as well as reports of kidney injury with abemaciclib. These should be weighed in a population such as RA patients, who often have elevated cardiovascular risk.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score (97.32%) is supported only by a plausible cell-cycle mechanism, one observational study in breast cancer patients and one preclinical nanoplatform study. There are no clinical trials in RA, and the safety signals (cardiovascular, immune-related) are a concern for long-term use in a chronic non-malignant disease. This is best treated as a research question rather than a candidate for clinical development at present.

**To proceed, the following is needed:**
- Mechanism of action data and a clear mechanistic link to RA synovial biology
- In vivo preclinical studies (for example, arthritis animal models) using abemaciclib itself, rather than a nanoplatform formulation
- Approved indication text and safety information (warnings and contraindications) from the TGA Product Information
- A risk-benefit assessment of cardiovascular and immune-related safety in an RA population
- If preclinical results are supportive, a registered early-phase trial (ClinicalTrials.gov or ANZCTR)

**Other predicted indications (for reference):** Amyotrophic lateral sclerosis (97.23% not applicable; score 96.23%, L4) has preclinical evidence of reduced TDP-43 accumulation but no clinical trials. Heart disease (L4) is supported mainly by literature on cardiotoxicity, which argues against benefit. Multiple endocrine neoplasia (L4) has only a terminated, non-interpretable Phase 1 platform trial. The remaining predictions (hyperthyroidism, thyroid hormone resistance, homozygous familial hypercholesterolemia, Laubry-Pezzi syndrome, Pierre Robin syndrome with chromosomal anomaly, Jeune syndrome situs inversus) are model predictions only (L5) with no supporting evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

