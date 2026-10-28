---
layout: default
title: Phenoxybenzamine
parent: Model Prediction Only (L5)
nav_order: 568
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
monitor_inn: "Phenoxybenzamine"
predicted_indications: ["primary hereditary glaucoma", "open-angle glaucoma"]
description: "Phenoxybenzamine: predicted new indication Primary hereditary glaucoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Phenoxybenzamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Phenoxybenzamine: Primary hereditary glaucoma
{: .text-alpha }

## One-Sentence Summary

Phenoxybenzamine is an irreversible, non-selective alpha-adrenergic blocker, originally used to manage phaeochromocytoma and related catecholamine-secreting tumours.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**, but there are currently **no clinical trials** and **no publications** supporting this specific prediction. It is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 0.9955 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, phenoxybenzamine irreversibly blocks alpha-adrenergic receptors. This is the basis of its use in phaeochromocytoma, where it counters the effects of excess catecholamines.

Alpha-blockade could theoretically alter aqueous humour dynamics or ocular blood flow. However, primary hereditary glaucoma is largely driven by structural or genetic outflow defects, so the mechanistic link to the original indication is weak. The high TxGNN score is a statistical prediction and is not backed by trials or literature.

**Other predictions.** The next-ranked predictions (all Hold unless stated) are:

- **Open-angle glaucoma** (99.48%): a plausible but unsupported link through intraocular pressure and perfusion. Systemic hypotension and irreversible receptor binding raise safety concerns.
- **Subarachnoid haemorrhage** (97.81%): the most interesting secondary signal. Animal studies suggest that sympathetic or noradrenergic blockade reduces cerebral vasospasm, and one older study reported reversal of experimental spasm with phenoxybenzamine. It is rated L4 and labelled a Research Question, with no human trials.

## Clinical Trial Evidence

Currently no related clinical trials registered for primary hereditary glaucoma or for any of the other top-ranked predicted indications.

## Literature Evidence

Currently no related literature available for primary hereditary glaucoma.


| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [5061](https://pubmed.ncbi.nlm.nih.gov/5061/) | 1976 | Preclinical (dogs) | Annals of Surgery | Effect of alpha and beta blockade on epinephrine-induced pulmonary shunting and insufficiency |
| [935680](https://pubmed.ncbi.nlm.nih.gov/935680/) | 1976 | Preclinical (dogs) | Respiration | Role of adrenergic mechanisms in the pulmonary vascular response to respiratory acidosis |
| [2860882](https://pubmed.ncbi.nlm.nih.gov/2860882/) | 1985 | Preclinical (dogs) | Arch Int Pharmacodyn Ther | Amyl nitrite and phenoxybenzamine pretreatment in acute cyanide poisoning |
| [40771558](https://pubmed.ncbi.nlm.nih.gov/40771558/) | 2025 | Case report | Clinical Case Reports | ECMO-assisted robotic surgery for phaeochromocytoma-induced acute catecholamine cardiomyopathy |
| [10487409](https://pubmed.ncbi.nlm.nih.gov/10487409/) | 1999 | Case report | Am J Med Sci | Phaeochromocytoma in pregnancy with pulmonary oedema and respiratory failure |
| [8664007](https://pubmed.ncbi.nlm.nih.gov/8664007/) | 1996 | Case report | Eur J Cardiothorac Surg | Phenoxybenzamine and prostacyclin used after surgery for raised pulmonary vascular resistance in an infant |

For subarachnoid haemorrhage (fifth-ranked), the preclinical literature includes:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10953871](https://pubmed.ncbi.nlm.nih.gov/10953871/) | 2000 | Preclinical (rabbits) | Wien Klin Wochenschr | Sympathetic exclusion prevented vasospasm after experimental SAH |
| [14603737](https://pubmed.ncbi.nlm.nih.gov/14603737/) | 2003 | Preclinical (rabbits) | Wien Klin Wochenschr | Noradrenergic blockade and vasospasm after SAH |
| [4814376](https://pubmed.ncbi.nlm.nih.gov/4814376/) | 1974 | Preclinical | J Neurosurg | Serotonin- and blood-induced cerebral arterial spasm reversed by phenoxybenzamine |
| [11695705](https://pubmed.ncbi.nlm.nih.gov/11695705/) | 2001 | Preclinical (rabbits) | Auton Neurosci | Morphometric method for cerebral artery response with alpha-blockade and SAH |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1166J | Amdipharm Mercury (Australia) Pty Limited | Capsules containing phenoxybenzamine hydrochloride 10 mg, 30 | Not available in the data compiled for this report |

## Safety Considerations

- **Contraindications suggested by the knowledge graph (not label text):** kidney disease, pyoureter, hypotensive disorder and coronary artery disease. These should be verified against the Product Information.
- **Drug Interactions:** 32 interactions were identified. All of those listed are Moderate severity, including bupropion, morphine, codeine, hydrocodone, opium, SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin), dronabinol, nabilone, promethazine, amifostine, iobenguane (I-123), and the prostacyclin-pathway drugs (epoprostenol, iloprost, selexipag, treprostinil).
- **Clinical concern:** As an irreversible alpha-blocker, systemic hypotension is a key practical concern for any new use, particularly in glaucoma, subarachnoid haemorrhage (cerebral perfusion) and frail patients.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications, as these were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (primary hereditary glaucoma) rests on model output alone (L5), with no trials or literature and a weak mechanistic link. Systemic hypotension is an added safety concern.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank)
- Approved indication text and warnings/contraindications from the TGA Product Information
- Ophthalmic pharmacology evidence (intraocular pressure, ocular perfusion) before any glaucoma work
- For subarachnoid haemorrhage, a preclinical-to-clinical bridging study that addresses cerebral perfusion and hypotension risk, as this is the most promising secondary lead (Research Question)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

