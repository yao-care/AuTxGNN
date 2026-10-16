---
layout: default
title: Domperidone
parent: Moderate Evidence (L3-L4)
nav_order: 224
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Domperidone: predicted new indication Headache disorder (migraine-associated symptoms) (evidence level L4). Approved use: Not stated in the ARTG data compiled for this report (general use: dy…"
monitor_inn: "Domperidone"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "Plasmodium falciparum malaria", "common cold", "headache disorder", "allergic urticaria", "trigeminal autonomic cephalalgia", "collagenopathy", "renin-angiotensin-aldosterone system-blocker-induced angioedema", "lymphocytic hypereosinophilic syndrome", "hypertrichosis (disease)"]
---

# Domperidone
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

# Domperidone: From Upper Gastrointestinal Symptoms to Headache Disorder (Migraine)

## One-Sentence Summary

Domperidone is a peripheral dopamine D2/D3 receptor antagonist used to manage dyspepsia, nausea and vomiting. The TxGNN model predicts it may be useful for **headache disorder** (mainly migraine-associated nausea and absorption problems), with **no registered clinical trials** and **19 publications**, mostly narrative reviews and guidelines, currently supporting this direction.

The headache disorder prediction was chosen because it is the only one among the top 10 predictions with a plausible mechanism and a meaningful body of literature. The top-ranked TxGNN prediction (nephrogenic syndrome of inappropriate antidiuresis) has no supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the ARTG data compiled for this report (general use: dyspepsia, heartburn, nausea and vomiting) |
| Predicted New Indication | Headache disorder (migraine-associated symptoms) |
| TxGNN Prediction Score | 96.72% (the top-ranked prediction, nephrogenic SIAD, scores 99.08% but has no supporting evidence) |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails (research question stage) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on known pharmacology, domperidone is a peripheral D2/D3 dopamine receptor antagonist that does not readily cross the blood-brain barrier. It acts as an antiemetic and an upper gastrointestinal prokinetic.

Migraine attacks commonly involve nausea, vomiting and gastric stasis, which can delay absorption of oral analgesics and triptans. Several reviews and guidelines describe domperidone (alongside metoclopramide) as an add-on to improve nausea and potentially enhance drug absorption. This means domperidone treats the **associated symptoms** of migraine rather than the headache itself. It is therefore best viewed as adjunctive therapy, not as a primary headache treatment.

Other predictions (for example nephrogenic SIAD, Plasmodium falciparum malaria, common cold, collagenopathy) have no identified mechanistic link and no supporting clinical data. They are not recommended for further work at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Nineteen publications were retrieved for headache disorder. The most relevant are shown below. Most are narrative reviews or guidelines, and none is a large randomised placebo-controlled trial of domperidone alone.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11191009](https://pubmed.ncbi.nlm.nih.gov/11191009/) | 2000 | Randomised primary care study | Curr Med Res Opin | Fixed combination of domperidone and paracetamol compared with sumatriptan 50 mg in 120 patients with moderate to severe migraine |
| [27837002](https://pubmed.ncbi.nlm.nih.gov/27837002/) | 2016 | Observational safety study | Neurology | Safety of domperidone for nausea associated with dihydroergotamine infusion and headache |
| [23968886](https://pubmed.ncbi.nlm.nih.gov/23968886/) | 2013 | Guideline | Can J Neurol Sci | Canadian Headache Society guideline on acute drug therapy for migraine |
| [19708964](https://pubmed.ncbi.nlm.nih.gov/19708964/) | 2009 | Guideline | Eur J Neurol | EFNS guideline on drug treatment of migraine (revised) |
| [25877672](https://pubmed.ncbi.nlm.nih.gov/25877672/) | 2015 | Review | Headache | Overview of office-based acute migraine therapy in adults |
| [28360580](https://pubmed.ncbi.nlm.nih.gov/28360580/) | 2013 | Review | Noro Psikiyatri Arsivi | Review of acute migraine pharmacological management |
| [10494007](https://pubmed.ncbi.nlm.nih.gov/10494007/) | 1999 | Review | Can J Clin Pharmacol | Prokinetic antiemetics (metoclopramide, domperidone) may improve absorption of analgesics and triptans |
| [12463273](https://pubmed.ncbi.nlm.nih.gov/12463273/) | 2001 | Review | Curr Med Res Opin | Anti-emetics for migraine; domperidone and metoclopramide have an additional prokinetic effect |
| [8749241](https://pubmed.ncbi.nlm.nih.gov/8749241/) | 1995 | Review | Cephalalgia | Antiemetic plus analgesic widely recommended; domperidone 20 mg orally commonly used |
| [9876882](https://pubmed.ncbi.nlm.nih.gov/9876882/) | 1998 | Review | Cephalalgia | Place of antiemetic and prokinetic agents in acute migraine treatment strategies |

Other retrieved items (for example a case report of anaphylaxis to levodropropizine for common cold, and incidental papers for allergic urticaria) are unrelated to domperidone efficacy and were disregarded.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1347X | APO-DOMPERIDONE | Tablet 10 mg (oral) | Not available in the data compiled |

---

## Safety Considerations

- **Cardiac risk (knowledge graph signal):** The TxGNN knowledge graph lists contraindication links with long QT syndrome, familial long QT syndrome and torsades de pointes. Cardiac safety (QT prolongation, arrhythmia) is the main guardrail concern.
- **Hepatic and biliary disease:** The knowledge graph also links domperidone with liver disease and gallbladder disease as contraindications. These come from graph edges, not from product label text.
- **Pharmacology:** Domperidone acts on the D2 and D3 dopamine receptors (DRD2, DRD3). The compiled data did not return specific drug-drug interactions; QT-prolonging and CYP3A4-inhibiting co-medications should be checked against the Product Information.
- **Migraine context:** One cited report (PMID 27837002) examined domperidone safety alongside dihydroergotamine infusion.

Please refer to the TGA-approved Product Information (PI) for formal warnings and contraindications, as these were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (research question stage only)

**Rationale:**
- The headache disorder prediction is biologically plausible. Domperidone helps with migraine-associated nausea and gastric stasis, and multiple guidelines and reviews mention it as an adjunct. However, there are no registered trials, the evidence is mostly narrative, and QT-related cardiac risk requires caution. All other predicted indications should remain on **Hold** (L5, no supporting evidence).

**To proceed, the following is needed:**
- Retrieve the TGA Product Information (warnings, contraindications, approved indications) for APO-DOMPERIDONE, as this data gap blocks safety screening
- Mechanism of action data from DrugBank
- Systematic review of randomised trials of domperidone as an adjunct in acute migraine
- Cardiac safety plan (baseline ECG/QT assessment, review of interacting medicines, limits on dose and duration)
- Clarification of the intended positioning (adjunct for nausea and absorption versus any direct headache claim)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

