---
layout: default
title: Olmesartan
parent: Model Prediction Only (L5)
nav_order: 523
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Olmesartan: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Not available in the data compiled for this report (olmesartan is an…"
monitor_inn: "Olmesartan"
predicted_indications: ["Prinzmetal angina", "hypotrichosis simplex of the scalp", "migraine disorder", "alopecia", "pulmonary hypertension", "congenital hypotrichosis milia", "diffuse alopecia areata", "migraine with brainstem aura", "kyphoscoliotic heart disease", "open-angle glaucoma"]
---

# Olmesartan
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

## Olmesartan: From Hypertension to Prinzmetal Angina
{: .text-alpha }

## One-Sentence Summary

Olmesartan is an angiotensin II receptor blocker (ARB) that is registered in Australia as an oral tablet. The approved indication text was not available in the data compiled for this report. The TxGNN model predicts it may be effective for **Prinzmetal angina**, but **no clinical trials and no publications** currently support this prediction. The strongest evidence among the top 10 predictions is for **migraine disorder** (3 publications, including a 2019 systematic review of ACE inhibitors and ARBs).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (olmesartan is an ARB, generally used for hypertension) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 0.9984 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, olmesartan is an angiotensin II type 1 (AT1) receptor blocker. It lowers blood pressure and may modestly improve endothelial function.

Prinzmetal (vasospastic) angina is driven mainly by coronary vasospasm. Calcium channel blockers and nitrates are the standard therapy. A link to AT1 blockade is plausible only indirectly, through vascular tone and endothelial effects. The high TxGNN score is a computational prediction only. No trials or literature were found to support it.

**Other predictions in the top 10**

- **Migraine disorder (rank 3)** has the most substantial support. Renin-angiotensin system modulation may reduce migraine frequency through effects on vascular tone, inflammation and sympathetic activity. Evidence is limited to small studies in hypertensive populations. Generalisability to normotensive patients is uncertain.
- **Pulmonary hypertension (rank 5)** has preclinical support only (rat and mouse models). There is no human efficacy data.
- **Open-angle glaucoma (rank 10)** has only indirect evidence.
- **Hair disorders (ranks 2, 4, 6, 7)** have no plausible mechanistic link and no clinical evidence. These predictions appear to arise from network associations rather than relevant biology.
- **Migraine with brainstem aura (rank 8) and kyphoscoliotic heart disease (rank 9)** are speculative extrapolations without direct evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for Prinzmetal angina.

For reference, the only trial retrieved among the top 10 predictions was listed under pulmonary hypertension and is not relevant to that indication:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04330300](https://clinicaltrials.gov/study/NCT04330300) | Phase 4 | Suspended | 2414 | CORONACION: continuation of ACE inhibitors/ARBs in COVID-19. It does not address pulmonary hypertension. |

---

## Literature Evidence

Currently no related literature is available for Prinzmetal angina. The table below lists the most relevant publications found for the other top predictions (migraine and pulmonary hypertension).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31515634](https://pubmed.ncbi.nlm.nih.gov/31515634/) | 2019 | Systematic review | Curr Pain Headache Rep | ACE inhibitors and ARBs for preventing episodic migraine in adults; identifies research gaps and guides future trials (migraine) |
| [16618270](https://pubmed.ncbi.nlm.nih.gov/16618270/) | 2006 | Clinical study | Headache | Effect of olmesartan on migraine frequency and severity in patients with hypertension or prehypertension (migraine) |
| [16942482](https://pubmed.ncbi.nlm.nih.gov/16942482/) | 2006 | Commentary | Headache | Commentary on olmesartan, migraine and blood pressure (migraine) |
| [18209564](https://pubmed.ncbi.nlm.nih.gov/18209564/) | 2008 | Preclinical | J Cardiovasc Pharmacol | Olmesartan medoxomil tested in the rat monocrotaline model of pulmonary hypertension |
| [16336959](https://pubmed.ncbi.nlm.nih.gov/16336959/) | 2005 | Preclinical | Eur J Pharmacol | Olmesartan medoxomil in chronic hypoxic rats, assessing hypoxic pulmonary hypertension |
| [17089097](https://pubmed.ncbi.nlm.nih.gov/17089097/) | 2006 | Preclinical | Naunyn Schmiedebergs Arch Pharmacol | Olmesartan and hypoxia-induced ERK1/2 activation and pro-inflammatory signals in the mouse lung |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13505T | Olmesartan - MYL | Tablet containing olmesartan medoxomil 20 mg | Not available |

---

## Safety Considerations

**Drug Interactions:** The interaction screen identified 94 potential interactions. The main ones are:

- **Major:** potassium bicarbonate and potassium chloride (risk of raised potassium).
- **Moderate:** a range of insulin products, exenatide, hydrocortisone, eluxadoline and polyethylene glycol 3350 with electrolytes.

Warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for these. As with ARBs generally, use in pregnancy is a recognised concern.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Prinzmetal angina prediction rests on a model score alone, with no trials or publications and only an indirect mechanistic link. Calcium channel blockers and nitrates remain the established therapy. Migraine is the more promising direction (L3 evidence, class-level signal), but the data are limited and come from small studies in hypertensive patients.

**To proceed, the following is needed:**
- The approved indication, warnings and contraindications from the TGA Product Information
- Detailed mechanism of action data
- For migraine: a focused review of ARB migraine-prevention studies and, if warranted, a trial in normotensive patients
- For Prinzmetal angina: any human or mechanistic evidence comparing olmesartan with standard vasospasm therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

