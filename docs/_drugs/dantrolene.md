---
layout: default
title: Dantrolene
parent: Model Prediction Only (L5)
nav_order: 194
evidence_level: L5
indication_count: 10
---

# Dantrolene
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

# Dantrolene: From Malignant Hyperthermia to Malignant Hyperthermia Susceptibility (RYR1-Related Disorders)

## One-Sentence Summary

Dantrolene is a skeletal muscle relaxant originally used to treat malignant hyperthermia of anaesthesia and exercise-induced malignant hyperthermia.
The TxGNN model's top prediction is **malignant hyperthermia, susceptibility to**, which is effectively an on-label indication rather than a true repurposing candidate. It is supported by **0 registered clinical trials** and **18 publications**, including two consensus guidelines. Predictions for the other related muscle disorders rest on much weaker evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Malignant hyperthermia of anaesthesia; exercise-induced malignant hyperthermia (the ARTG indication text is not available) |
| Predicted New Indication | Malignant hyperthermia, susceptibility to |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L1 (assigned on the basis of guideline-endorsed standard of care, not on Phase 3 RCTs) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. The literature does describe dantrolene as inhibiting RyR1-mediated calcium release from the sarcoplasmic reticulum in skeletal muscle. This directly counteracts the uncontrolled calcium release that drives malignant hyperthermia. One 2017 study (PMID 28373535) reports that dantrolene requires magnesium ions to arrest malignant hyperthermia.

The top predicted disease is closely related to the drug's established indication. Malignant hyperthermia susceptibility is the underlying genetic trait, mostly linked to RYR1 mutations, that leads to a malignant hyperthermia crisis. This should be read as confirmation of an existing use, not a new indication. Dantrolene is the standard treatment endorsed in consensus guidelines.

The lower-ranked predictions are mostly other RYR1-related myopathies, such as King-Denborough syndrome, central core disease and multicore myopathies. For these, dantrolene's relevance is limited to preventing and treating malignant hyperthermia crises. There is no evidence that it treats the underlying myopathy. Several periodic paralysis predictions have no supporting evidence and a speculative mechanistic link.

## Clinical Trial Evidence

Currently no related clinical trials registered. The guideline literature notes that placebo-controlled trials would be unethical in a life-threatening emergency, so the evidence base rests on decades of clinical use and expert consensus.

## Literature Evidence

The table shows the most relevant publications for the top-ranked prediction (malignant hyperthermia susceptibility).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33399225](https://pubmed.ncbi.nlm.nih.gov/33399225/) | 2021 | Guideline | Anaesthesia | Association of Anaesthetists (UK) 2020 guideline on malignant hyperthermia |
| [33131754](https://pubmed.ncbi.nlm.nih.gov/33131754/) | 2021 | Guideline | Br J Anaesth | European Malignant Hyperthermia Group consensus on perioperative management of suspected or susceptible patients; notes there is no interventional trial evidence |
| [39171998](https://pubmed.ncbi.nlm.nih.gov/39171998/) | 2024 | Review | Crit Care Med | Narrative review of epidemiology and management of critically ill patients with malignant hyperthermia |
| [26238698](https://pubmed.ncbi.nlm.nih.gov/26238698/) | 2015 | Review | Orphanet J Rare Dis | Malignant hyperthermia is a pharmacogenetic skeletal muscle disorder with an incidence of 1:10,000 to 1:250,000 anaesthetics |
| [32008650](https://pubmed.ncbi.nlm.nih.gov/32008650/) | 2020 | Review | Anesthesiol Clin | Update on a rare, potentially lethal calcium release channel disorder; mortality has improved |
| [28373535](https://pubmed.ncbi.nlm.nih.gov/28373535/) | 2017 | Mechanistic study | PNAS | Dantrolene requires Mg2+ to arrest malignant hyperthermia |
| [9538480](https://pubmed.ncbi.nlm.nih.gov/9538480/) | 1998 | Review | Postgrad Med J | Dantrolene sodium is described as the ultimate treatment |

Evidence for related predictions is much weaker:
- **King-Denborough syndrome:** case reports only, including [1508238](https://pubmed.ncbi.nlm.nih.gov/1508238/) (a hyperthermic episode that responded to dantrolene) and [27918309](https://pubmed.ncbi.nlm.nih.gov/27918309/).
- **Central core disease:** preclinical and review literature, plus a case report of prophylactic dantrolene use ([9539627](https://pubmed.ncbi.nlm.nih.gov/9539627/)).
- **Multicore myopathy, centronuclear myopathy and periodic paralysis:** no direct dantrolene treatment data.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1779P | Dantrium | Capsule containing dantrolene sodium hemiheptahydrate 25 mg (oral) | Not available in the data compiled for this report |

## Safety Considerations

**Contraindications flagged in the knowledge graph** (these are graph associations, not label text): liver disease, gallbladder disease, myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, lung disease and a rare pulmonary disease. Several of these overlap with the predicted new indications, so they need careful clinical consideration.

**Drug interactions:** 72 interactions were identified. Major interactions include:
- Morphine (including liposomal morphine)

Moderate interactions include:
- Dronabinol
- Metoclopramide
- Nabilone
- Naltrexone
- Opium
- Sibutramine
- Ethanol
- Promethazine

Many other interactions have an unknown severity rating. They include proton pump inhibitors, metformin, simvastatin, clopidogrel and clarithromycin.

For warnings and contraindications from the label, please refer to the TGA-approved Product Information (PI).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The top prediction is an established, guideline-endorsed use of dantrolene, not a new repurposing candidate. The L1 rating is a judgment call based on standard of care rather than completed Phase 3 RCTs. The other predictions are either exploratory research questions (King-Denborough syndrome, central core disease, centronuclear myopathy) or should be held (multicore myopathies, periodic paralyses) because they have no direct evidence.

**To proceed, the following is needed:**
- Review of the TGA-approved Product Information, since warnings and contraindications could not be retrieved (a blocking data gap)
- Confirmation of the ARTG-approved indication text
- Mechanism of action data from DrugBank
- For the exploratory myopathy indications, clinical data on dantrolene's effect on the underlying disease, as opposed to malignant hyperthermia prophylaxis alone
- A review of the knowledge-graph contraindications (liver, muscle and lung disease) against any proposed patient group
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

