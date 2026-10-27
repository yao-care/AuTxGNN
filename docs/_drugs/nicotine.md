---
layout: default
title: Nicotine
parent: Model Prediction Only (L5)
nav_order: 500
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Nicotine: predicted new indication Exercise-induced malignant hyperthermia (evidence level L5). Approved use: Nicotine dependence"
monitor_inn: "Nicotine"
predicted_indications: ["exercise-induced malignant hyperthermia", "migraine with brainstem aura", "oppositional defiant disorder (disease)", "migraine disorder", "blepharospasm", "46,XY disorder of sex development due to testicular steroidogenesis defect", "transverse vaginal septum", "longitudinal vaginal septum", "communication disorder", "developmental disorder of mental health"]
---

# Nicotine
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

## Nicotine: From Nicotine Dependence to Exercise-Induced Malignant Hyperthermia
{: .text-alpha }

## One-Sentence Summary

Nicotine is a nicotinic acetylcholine receptor agonist, originally used in nicotine replacement therapy for nicotine dependence (the knowledge graph also lists pellagra and beriberi).
The TxGNN model's top-ranked prediction is **exercise-induced malignant hyperthermia**, but there are **0 clinical trials** and **0 publications** supporting it.
The evidence is model prediction only, so this report also summarises the better-studied lower-ranked predictions (migraine and blepharospasm).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Nicotine dependence (also pellagra and beriberi in the knowledge graph); no approved indication text is available for the Australian product |
| Predicted New Indication | Exercise-induced malignant hyperthermia |
| TxGNN Prediction Score | 83.91% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Nicotine is generally known to act on nicotinic acetylcholine receptors, and its efficacy in managing nicotine dependence is established.

For exercise-induced malignant hyperthermia, a plausible therapeutic link is not established. This condition involves ryanodine receptor and calcium dysregulation in skeletal muscle. Nicotine does act on the neuromuscular junction subtype of nicotinic receptor, but agonism at that site could theoretically be unfavourable. The high score is a graph-based prediction only.

Other predictions were reviewed for context:
- **Migraine (ranks 2 and 4):** Literature supports a biological connection between nicotinic/cholinergic signalling and migraine. However, smoking, nicotine exposure and withdrawal appear mostly as triggers or associated factors, not treatments.
- **Blepharospasm (rank 5):** Nicotine may modulate basal ganglia and sensorimotor gating, which is plausible for focal dystonia. An early report was positive, but a later pilot study did not reproduce it.
- **Oppositional defiant disorder, communication disorder, developmental disorder of mental health (ranks 3, 9, 10):** The evidence describes tobacco and nicotine exposure as a risk factor for adverse neurodevelopmental outcomes. This indicates potential harm, not benefit.
- **Ranks 6–8 (46,XY disorder of sex development, transverse and longitudinal vaginal septum):** No trials or literature, and no identified mechanistic connection.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for the top-ranked prediction (exercise-induced malignant hyperthermia).

Two trials were retrieved for lower-ranked predictions. Both were graded as only indirectly relevant, since neither tests nicotine as a treatment for the predicted condition:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03289676](https://clinicaltrials.gov/study/NCT03289676) | Phase 1 | Completed | 53 | Feasibility of a storytelling communication and HIV-tailored smoking cessation intervention for women living with HIV (rank 9, communication disorder) |
| [NCT04560868](https://clinicaltrials.gov/study/NCT04560868) | Phase 1 | Completed | 57 | Pilot of an mHealth app for smokers ambivalent about quitting (rank 10, developmental disorder of mental health) |

---

## Literature Evidence

Currently no related literature is available for the top-ranked prediction. The most relevant publications for the better-studied predictions are below (migraine and blepharospasm):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9452355](https://pubmed.ncbi.nlm.nih.gov/9452355/) | 1998 | Pilot study | Mov Disord | Nicotine nasal spray was not a reliable treatment for blepharospasm |
| [8691949](https://pubmed.ncbi.nlm.nih.gov/8691949/) | 1996 | Case series/Pilot | Lancet | Early report suggesting benefit of nicotine nasal spray in blepharospasm |
| [40468190](https://pubmed.ncbi.nlm.nih.gov/40468190/) | 2025 | Systematic review/Meta-analysis | J Headache Pain | Association between smoking and primary headaches |
| [26140522](https://pubmed.ncbi.nlm.nih.gov/26140522/) | 2015 | Review | Headache | Tobacco, nicotine and headache; tobacco exposure is linked to headache exacerbation |
| [28920040](https://pubmed.ncbi.nlm.nih.gov/28920040/) | 2017 | Review | Anesth Pain Med | Parasympathetic cholinergic and neuropeptide mechanisms of migraine |
| [16816594](https://pubmed.ncbi.nlm.nih.gov/16816594/) | 2006 | Case report | Eur J Emerg Med | Severe migraine headaches after sudden discontinuation of nicotine gum |
| [19554418](https://pubmed.ncbi.nlm.nih.gov/19554418/) | 2009 | Review | J Headache Pain | Psychiatric comorbidity (including nicotine dependence) in chronic daily headache and migraine |

None of these provides controlled evidence of efficacy.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10076H | nicorette 16hr Invisipatch | Transdermal patch 39.4 mg | Not stated in the data compiled for this report |

---

## Safety Considerations

Product-label warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for safety information.

**Knowledge-graph contraindication signals (not label text):** The knowledge graph links nicotine with contraindication to the following conditions, which should be verified against the PI:
- **Cardiovascular:** acute coronary syndrome, coronary artery disease, myocardial infarction, coronary thrombosis, Prinzmetal angina, hypotensive disorder
- **Endocrine and metabolic:** diabetes mellitus (including type 1), diabetic ketoacidosis, hyperglycaemia, hyperthyroidism (Graves disease, thyrotoxicosis), phaeochromocytoma, gout
- **Gastrointestinal and hepatic:** peptic ulcer disease, liver disease, gallbladder disease
- **Haematological:** thrombocytopenia, blood coagulation disease, haemoglobinopathy
- **Other:** substance abuse/dependence, and several cancers (duodenum, small intestine, heart, adrenal gland, sympathetic paraganglioma)

**Drug interactions:** 100 interactions were identified in total; the first 20 are listed in the data compiled for this report. The main ones with a defined severity are:
- **Moderate:** bupropion
- **Minor:** famotidine, ranitidine (including ranitidine bismuth citrate), cimetidine, nizatidine

Other listed interactions (for example pantoprazole, omeprazole, lansoprazole, metformin, glimepiride, rosiglitazone, morphine, prednisone) have an unknown severity rating.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no clinical trials or literature (evidence level L5), and no plausible mechanistic link. Agonism at the neuromuscular nicotinic receptor could theoretically be unfavourable in malignant hyperthermia. The better-studied predictions are not supported either: migraine evidence is epidemiological, with nicotine mostly a trigger rather than a treatment, and blepharospasm evidence is limited to small, conflicting pilot studies. Some neurodevelopmental predictions suggest potential harm.

**To proceed, the following is needed:**
- Mechanism of action data, to allow proper mechanistic-link analysis
- Product label warnings and contraindications for the Australian product, so safety screening can proceed
- The approved indication text for the Australian registration
- Preclinical or mechanistic studies for the top-ranked prediction before any clinical consideration
- If blepharospasm is pursued as a research question, a properly controlled study to resolve the conflicting early findings
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

