---
layout: default
title: Tapentadol
parent: Model Prediction Only (L5)
nav_order: 701
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Tapentadol: predicted new indication Migraine disorder (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Tapentadol"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "migraine with or without aura, susceptibility to", "atrophoderma vermiculata", "ulerythema ophryogenesis", "insomnia (disease)", "headache disorder", "nephrogenic syndrome of inappropriate antidiuresis", "trigeminal autonomic cephalalgia", "anxiety"]
---

# Tapentadol
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

## Tapentadol: From Pain Management to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Tapentadol is a centrally acting opioid analgesic marketed in Australia as Palexia SR.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are currently **no registered clinical trials** and **no publications directly supporting this use**.
This is a model-only prediction, and the available literature points more towards safety concerns than benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the ARTG entry has no indication text; tapentadol is generally used for pain) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacological knowledge, tapentadol is a mu-opioid receptor agonist and norepinephrine reuptake inhibitor. Its efficacy in pain conditions is established, and the model likely links it to migraine through this analgesic profile.

The high TxGNN score appears to be a graph-based association rather than a mechanistically specific signal. Opioids are generally not recommended for migraine because of the risk of medication-overuse headache, poorer outcomes, and limited efficacy. Related predictions (migraine with brainstem aura, trigeminal autonomic cephalalgia, general headache disorder) appear to be propagated from the same node. Other top-ranked predictions, such as atrophoderma vermiculata and ulerythema ophryogenesis, have no plausible mechanistic link and look like knowledge-graph artefacts.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature was retrieved for "migraine disorder" itself. The closest related items, retrieved for migraine susceptibility and headache disorder predictions, are indirect and do not show efficacy of tapentadol in migraine:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29760569](https://pubmed.ncbi.nlm.nih.gov/29760569/) | 2018 | Cohort | Drug Healthc Patient Saf | Opioids are not recommended for routine migraine treatment because of medication-overuse headache and dependence risks. Concomitant opioid use with triptans or serotonergic antidepressants carries a serotonin syndrome warning. |
| [33689517](https://pubmed.ncbi.nlm.nih.gov/33689517/) | 2021 | Review | Expert Opin Pharmacother | Reviews NSAIDs and acetaminophen as alternatives to opioids for acute pain. |
| [29616344](https://pubmed.ncbi.nlm.nih.gov/29616344/) | 2018 | Review | Curr Pain Headache Rep | Reviews non-opioid therapies for chronic pain. |
| [28729524](https://pubmed.ncbi.nlm.nih.gov/28729524/) | 2017 | Case report | Am J Case Rep | Cardiac arrest after intravenous tapentadol abuse in a patient presenting with headache. This is a safety signal, not evidence of efficacy. |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10091D | Palexia SR | Tablet (modified release) 200 mg (as hydrochloride) | Not stated in the compiled data |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the interaction screen. Examples of **Major** interactions include bupropion, morphine, lorcaserin, diethylpropion, dolasetron, palonosetron and phentermine. Examples of **Moderate** interactions include epinephrine, naloxone, eluxadoline, dronabinol, nabilone, and several anticholinergic agents (hyoscyamine, atropine, glycopyrronium, dicyclomine, trospium).
- **Migraine-specific concerns**: Tapentadol's serotonergic and noradrenergic activity raises a potential serotonin syndrome concern with triptans and serotonergic antidepressants. Opioids also carry a risk of medication-overuse headache.
- **Other**: Published reports describe abuse and nonmedical use of tapentadol.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5), with no trials and no direct literature. Clinical guidance and the indirect literature argue against opioids in migraine because of medication-overuse headache and serotonin syndrome risks, so the risk-benefit balance appears unfavourable.

**To proceed, the following is needed:**
- Mechanism of action data to support a migraine-specific rationale
- Approved indication and safety text from the TGA Product Information (the compiled data contained none)
- Controlled clinical evidence of tapentadol in migraine, compared against current standard therapies
- Assessment of medication-overuse headache and serotonin syndrome risk, particularly with triptans
- Consideration of whether any other predicted indication (for example, pain-related comorbidity) is more clinically plausible
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

