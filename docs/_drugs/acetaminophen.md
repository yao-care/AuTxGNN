---
layout: default
title: Acetaminophen
parent: Moderate Evidence (L3-L4)
nav_order: 18
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Acetaminophen: predicted new indication Migraine with brainstem aura (evidence level L4). Approved use: Migraine and headache disorders, common cold…"
monitor_inn: "Acetaminophen"
predicted_indications: ["migraine with brainstem aura", "trigeminal autonomic cephalalgia", "atrophoderma vermiculata", "tendinitis", "idiopathic granulomatous myositis", "myositis fibrosa", "ulerythema ophryogenesis", "fibromyalgia", "inclusion body myositis", "sciatic neuropathy"]
---

# Acetaminophen
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

# Acetaminophen: From Headache and Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Acetaminophen (paracetamol) is a widely used analgesic, listed in the data compiled for this report for migraine, headache disorders, common cold and allergic or vasomotor rhinitis.
The TxGNN model predicts it may be effective for **migraine with brainstem aura**, a subtype of migraine with aura.
There are currently **no registered clinical trials** and **20 publications** retrieved, mostly general migraine reviews, so the prediction rests mainly on extension from established migraine use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine and headache disorders, common cold, allergic and vasomotor rhinitis (the Australian licence entry has no indication text) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, acetaminophen is a simple analgesic and antipyretic. Its efficacy in acute migraine is recognised, and mechanistically it may be applicable to migraine with brainstem aura.

Migraine with brainstem aura is a subtype of migraine with aura. The American Headache Society evidence assessment of acute migraine therapies (2015) supports acetaminophen for acute migraine in general. The link to this subtype is therefore by extension from general migraine.

None of the retrieved literature is specific to brainstem aura, and no trials are registered. The high TxGNN score probably reflects the close network proximity of this subtype to the approved migraine indication, rather than direct evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for migraine with brainstem aura.

---

## Literature Evidence

The 20 retrieved publications are listed in the data compiled for this report. The most relevant are shown below (no RCT specific to brainstem aura was found).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review | Headache | American Headache Society evidence assessment of acute migraine pharmacotherapies, supporting acetaminophen for acute migraine |
| [10321417](https://pubmed.ncbi.nlm.nih.gov/10321417/) | 1999 | RCT-based (3 placebo-controlled trials, retrospective analysis) | Clin Ther | Acetaminophen, aspirin and caffeine combination for menstruation-associated migraine compared with non-menstrual migraine |
| [11318886](https://pubmed.ncbi.nlm.nih.gov/11318886/) | 2001 | Comparative study | Headache | Isometheptene, dichloralphenazone and acetaminophen combination compared with sumatriptan in mild-to-moderate migraine |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Review | Handb Clin Neurol | Status migrainosus as a complication of migraine with or without aura |
| [30470274](https://pubmed.ncbi.nlm.nih.gov/30470274/) | 2019 | Review | Neurol Clin | Acetaminophen as first-line symptomatic treatment for headache in pregnancy |
| [39493026](https://pubmed.ncbi.nlm.nih.gov/39493026/) | 2024 | Review | Cureus | Abortive and prophylactic migraine therapy in pregnancy |
| [16018227](https://pubmed.ncbi.nlm.nih.gov/16018227/) | 2005 | Review | Pediatr Ann | Management of paediatric migraine, including acute treatment |
| [23203776](https://pubmed.ncbi.nlm.nih.gov/23203776/) | 2013 | Review | Curr Treat Options Neurol | Diagnosis and treatment of familial and sporadic hemiplegic migraine, a related aura subtype |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10582Y | Pharmacy Care Paracetamol | Tablet 500 mg (oral) | Not stated in the data compiled for this report |

---

## Safety Considerations

- **Disease-related contraindications (knowledge graph, not label text)**: liver failure, liver disease, cirrhosis of liver, hepatic encephalopathy, hepatic coma and gallbladder disease.
- **Drug Interactions**: 100 interactions were identified. Those listed are mostly Minor. Moderate-level interactions include **activated charcoal**, **glycerol phenylbutyrate** and **naltrexone**. Minor interactions include anticholinergic and antimuscarinic agents (atropine, hyoscyamine, scopolamine, glycopyrronium), H2 blockers (cimetidine, ranitidine), metoclopramide and liraglutide.

Please also refer to the TGA-approved Product Information (PI) for warnings and contraindications, as label text was not available for this report.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Acetaminophen is an established acute treatment for general migraine and is already marketed in Australia, so the prediction is clinically plausible. However, the evidence is at L4: there is no trial or publication specific to brainstem aura, and the model score likely reflects proximity to the approved migraine indication.

**To proceed, the following is needed:**
- Review of the TGA Product Information for warnings, contraindications and approved indications
- Mechanism of action data
- Subtype-specific evidence, such as analyses of aura subtypes in existing acute migraine trials, or a registered study
- Hepatic safety guardrails, including exclusion of patients with liver disease and dose limits to avoid overdose and medication-overuse headache

---

*Other predictions in the data compiled for this report (all lower priority): trigeminal autonomic cephalalgia (Hold, indirect link only), tendinitis (symptomatic pain relief only, L4), fibromyalgia (L3, evidence mainly for the tramadol/acetaminophen combination), sciatic neuropathy (L3, one acute-care RCT of IV paracetamol versus morphine), and several rare skin and muscle disorders with no evidence (L5, Hold).*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

