---
layout: default
title: Palonosetron
parent: Model Prediction Only (L5)
nav_order: 544
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Palonosetron: predicted new indication Migraine disorder (evidence level L5). Approved use: Not recorded in the data compiled for this report (the registered Aus…"
monitor_inn: "Palonosetron"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "migraine with or without aura, susceptibility to", "atrophoderma vermiculata", "ulerythema ophryogenesis", "headache disorder", "trigeminal autonomic cephalalgia", "open-angle glaucoma", "sciatic neuropathy", "primary hereditary glaucoma"]
---

# Palonosetron
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

# Palonosetron: From Chemotherapy-Induced Nausea and Vomiting to Migraine Disorder

## One-Sentence Summary

Palonosetron is a 5-HT3 receptor antagonist, a class of antiemetic used to prevent nausea and vomiting, and it is marketed in Australia as an injection.
The TxGNN model predicts it may be effective for **migraine disorder**, but **no clinical trials** and only **1 case report** (describing palonosetron *causing* migraine-type headache) are linked to this prediction.
The evidence is model prediction only and does not currently support therapeutic use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the data compiled for this report (the registered Australian entry has no indication text). Literature identifies the established use as prevention of chemotherapy-induced nausea and vomiting (CINV) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, palonosetron is a second-generation 5-HT3 receptor antagonist. Its efficacy in preventing chemotherapy-induced nausea and vomiting has been shown in phase 3 trials, and mechanistically it may be applicable to migraine, which involves serotonin signalling and prominent nausea.

The TxGNN score is very high (99.74%), but this should be read cautiously. The only linked publication reports palonosetron *inducing* migraine-type headache, which is a safety signal in the opposite direction to benefit. 5-HT3 antagonists have a plausible but unproven role in migraine and nausea pathways, and no clinical evidence supports palonosetron for migraine treatment or prevention.

Other predictions from the model (for example migraine with brainstem aura, trigeminal autonomic cephalalgia, headache disorder, glaucoma, sciatic neuropathy, and rare skin disorders) also have no supporting trials. Most appear to be knowledge-graph artefacts, likely driven by proximity to the migraine node.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21132477](https://pubmed.ncbi.nlm.nih.gov/21132477/) | 2011 | Case report | Can J Anaesth | Palonosetron-induced migraine-type headache (an adverse effect, not a benefit) |

For the broader headache-related prediction, the linked publications are CINV studies in which headache was reported as an adverse event, not studies of headache treatment. They are not evidence of efficacy in migraine.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 5295Q | Palonosetron Dr.Reddy's | Injection 250 micrograms (as hydrochloride) in 5 mL | Not available in the data compiled |

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 interacting drugs (the first 20 were reviewed). Major-level interactions include:
  - Opioids and related analgesics: fentanyl, alfentanil, tramadol, dextromethorphan
  - Triptans: sumatriptan, almotriptan
  - QT-prolonging or cardiac drugs: amiodarone, amisulpride, amitriptyline, anagrelide
  - Moderate-level interactions include abiraterone, dihydrocodeine, codeine, famotidine, formoterol, adenosine, salbutamol, alfuzosin, propofol and loperamide.
- **Relevant to this prediction**: Triptans, the standard acute migraine treatments, appear among the major interactions, which would matter in any migraine use. A 2026 review also highlights QT prolongation as a class concern for antiemetics (PMID 42748473).

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (evidence level L5). The only linked literature describes palonosetron causing migraine-type headache, which argues against benefit. There are no trials, and no mechanistic data are available.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) and a clear mechanistic rationale for migraine
- The TGA Product Information, to complete warnings, contraindications and the approved indication
- Preclinical or early clinical evidence of efficacy in migraine that addresses the reported headache signal
- A review of interaction risk with triptans and QT-prolonging drugs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

