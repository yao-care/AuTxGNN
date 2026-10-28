---
layout: default
title: Travoprost
parent: Model Prediction Only (L5)
nav_order: 751
evidence_level: L5
indication_count: 10
monitor_inn: "Travoprost"
predicted_indications: ["visceral calciphylaxis", "venous thoracic outlet syndrome", "arterial thoracic outlet syndrome", "neurogenic thoracic outlet syndrome", "vascular disease", "angiodysplasia of stomach", "blue toe syndrome", "idiopathic spontaneous coronary artery dissection", "lymphangiectasis", "hemangioendothelioma"]
last_modified_at: 2026-10-28
description: "Travoprost: predicted new indication Visceral calciphylaxis (evidence level L5). Approved use: Open-angle glaucoma and ocular hypertension"
---

# Travoprost
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

## Travoprost: From Open-Angle Glaucoma to Visceral Calciphylaxis
{: .text-alpha }

## One-Sentence Summary

Travoprost is a topical prostaglandin F2-alpha analogue (FP receptor agonist) used as eye drops for open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be relevant to **visceral calciphylaxis**, but **no clinical trials and no publications** directly study this disease, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma and ocular hypertension (relation recorded in the knowledge graph; the ARTG record in the data compiled for this report contains no indication text) |
| Predicted New Indication | Visceral calciphylaxis |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Travoprost is generally understood to be a prostaglandin F2-alpha analogue that acts on the FP receptor to lower intraocular pressure by increasing uveoscleral outflow.

No established link exists between FP receptor agonism and the vascular calcification pathways involved in calciphylaxis. In addition, topical ocular dosing gives minimal systemic exposure. The prediction should be treated as a model-generated hypothesis only, and the similarity to the original indication has not been assessed.

The other top-ranked predictions (venous, arterial and neurogenic thoracic outlet syndrome, vascular disease, gastric angiodysplasia, blue toe syndrome, spontaneous coronary artery dissection, lymphangiectasis and hemangioendothelioma) also have no supporting trials or literature for efficacy. The one partial exception is "vascular disease", discussed below.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for visceral calciphylaxis.

For context, the trials retrieved for the broader prediction "vascular disease" (rank 5) are all in glaucoma or ocular hypertension, the original indication. They do not test a vascular disease treatment. The most relevant of these were:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00308945](https://clinicaltrials.gov/study/NCT00308945) | Phase 4 | Completed | 20 | Travoprost vs latanoprost effects on retinal vascular diameter and choroidal blood flow in glaucoma patients (indirect ocular haemodynamic data only) |
| [NCT00293761](https://clinicaltrials.gov/study/NCT00293761) | Phase 3 | Completed | 109 | Glaucoma therapy in open-angle glaucoma or ocular hypertension |
| [NCT00760539](https://clinicaltrials.gov/study/NCT00760539) | Phase 3 | Completed | 87 | Travoprost/timolol BAK-free vs standard fixed combination for IOP lowering |
| [NCT00672997](https://clinicaltrials.gov/study/NCT00672997) | Phase 3 | Completed | 301 | Travoprost/timolol BAK-free vs standard fixed combination for IOP lowering |
| [NCT01510145](https://clinicaltrials.gov/study/NCT01510145) | Phase 4 | Completed | 191 | BAK-free travoprost after switching from latanoprost |
| [NCT02136589](https://clinicaltrials.gov/study/NCT02136589) | Phase 4 | Completed | 40 | NSAID effect on travoprost-induced conjunctival hyperaemia (a side effect) |

---

## Literature Evidence

Currently no related literature available for visceral calciphylaxis.

Literature retrieved for neighbouring predictions, which does not support efficacy in these conditions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28458346](https://pubmed.ncbi.nlm.nih.gov/28458346/) | 2017 | Database analysis | Biol Pharm Bull | Spontaneous adverse event reports suggest an association between topical PGF2α analogues and blood pressure elevation (a safety signal) |
| [12664369](https://pubmed.ncbi.nlm.nih.gov/12664369/) | 2003 | Preclinical (ex vivo) | Klin Monatsbl Augenheilkd | Travoprost showed no vasoactive properties in isolated porcine ciliary arteries |
| [19107053](https://pubmed.ncbi.nlm.nih.gov/19107053/) | 2008 | Case report | J Fr Ophtalmol | Uveal effusion induced by topical travoprost in a patient with Sturge-Weber-Krabbe syndrome (an adverse event, relevant to hemangioendothelioma rank 10) |
| [25867658](https://pubmed.ncbi.nlm.nih.gov/25867658/) | 2015 | Systematic review | Curr Med Res Opin | Efficacy and tolerability of prostaglandin-timolol fixed combinations in glaucoma |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14549R | Travatan | Eye drops 40 micrograms per mL, 2.5 mL | Not stated in the data compiled for this report |

Only one single-ingredient licence is listed, and its status is valid. The only available dosage form is ophthalmic, which differs from what a systemic condition such as visceral calciphylaxis would likely need.

---

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** The knowledge graph links travoprost to the following conditions as contraindications: uveitis, iris disease, ciliary body disease, panuveitis, iritis, cystoid macular oedema and macular retinal oedema. These should be verified against the Product Information.
- **Blood pressure:** Spontaneous report analyses suggest topical PGF2α analogues may be associated with blood pressure elevation (PMID 28458346). This is a theoretical concern for vascular conditions.
- **Vascular anomalies:** A case report describes uveal effusion with topical travoprost in a patient with Sturge-Weber-Krabbe syndrome, suggesting caution in patients with vascular malformations.
- **Drug interactions:** 49 interactions were identified, all with an unknown severity level. Examples include calcitriol, pantoprazole, sucralfate, morphine, metformin, omeprazole, prednisone, simvastatin and acetylsalicylic acid. Their clinical significance is not established.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. No trials or publications study travoprost in visceral calciphylaxis, there is no plausible mechanistic link, and topical ocular dosing offers little systemic exposure. Evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible biological link between FP receptor agonism and calciphylaxis or vascular calcification
- Preclinical evidence in a relevant model of calciphylaxis
- A route and formulation assessment, since only an ophthalmic product is registered
- The TGA Product Information, to confirm warnings, contraindications and the approved indication text
- Review of the blood pressure signal and vascular safety concerns
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

