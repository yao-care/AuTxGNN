---
layout: default
title: Amiodarone
parent: 僅模型預測 (L5)
nav_order: 40
evidence_level: L5
indication_count: 10
---

# Amiodarone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Amiodarone: From Ventricular Arrhythmia to Catecholaminergic Polymorphic Ventricular Tachycardia

## One-Sentence Summary

Amiodarone is a broad-spectrum antiarrhythmic agent (Vaughan-Williams Class III) used globally for life-threatening ventricular arrhythmias and atrial fibrillation, though no ARTG registration was found in this dataset.
The TxGNN model predicts it may be effective for **Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT)**, a rare inherited arrhythmia disorder triggered by adrenergic stimulation.
Currently, there are **no registered clinical trials** and **10 publications** (predominantly case reports and descriptive cohort studies) supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available — no ARTG entries found in this dataset |
| Predicted New Indication | Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT) |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L4 (Mechanism/preclinical basis; no clinical trials for this indication) |
| Australia Market Status | Not marketed (no ARTG registration found) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Amiodarone is a well-established broad-spectrum antiarrhythmic agent with a uniquely complex pharmacological profile. Although detailed mechanism of action data was not available in this Evidence Pack, amiodarone is known clinically to combine properties of all four Vaughan-Williams classes: it primarily blocks potassium channels (IKr, IKs) to prolong action potential duration and effective refractory period (Class III), while also exhibiting sodium channel blockade (Class I), L-type calcium channel blockade (Class IV), and non-competitive beta-adrenergic receptor antagonism (Class II). This multi-channel inhibition is what makes it one of the most versatile antiarrhythmic agents currently available.

CPVT is caused by mutations in the RYR2 gene (or less commonly CASQ2), which result in abnormal calcium release from the sarcoplasmic reticulum (SR) under adrenergic stimulation. This produces delayed afterdepolarisations (DADs) and triggered ventricular tachycardia. In principle, amiodarone's beta-adrenergic blockade could reduce the sympathetic triggers for calcium release, and its L-type calcium channel inhibition may attenuate the overall calcium load — both of which could theoretically dampen CPVT episodes.

However, amiodarone does not directly address the core pathological mechanism: it cannot correct the SR calcium leak caused by dysfunctional RYR2 channels. Current international guidelines (including those from the Heart Rhythm Society and the European Society of Cardiology) preferentially recommend beta-blockers as first-line therapy and flecainide as an adjunct, given flecainide's direct RYR2-blocking properties. Amiodarone is generally reserved for refractory arrhythmic storm scenarios, and even in that setting, case report evidence suggests inconsistent and often limited efficacy. The high TxGNN score most likely reflects shared cardiac electrophysiology nodes within the knowledge graph rather than strong clinical translatability.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Amiodarone in catecholaminergic polymorphic ventricular tachycardia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Systematic Review | *Life (Basel)* | Systematic review of CPVT clinical characteristics, genetic findings (predominantly RYR2), and arrhythmic outcomes in Chinese patients; notes differences from Western cohorts |
| [39076628](https://pubmed.ncbi.nlm.nih.gov/39076628/) | 2022 | Retrospective Cohort | *Reviews in Cardiovascular Medicine* | Healthcare resource utilisation and costs in CPVT; provides clinical and economic context for management burden |
| [26513538](https://pubmed.ncbi.nlm.nih.gov/26513538/) | 2015 | Review | *Expert Opinion on Pharmacotherapy* | Comprehensive review of pharmacological treatment for ventricular arrhythmias; discusses amiodarone's role as rescue therapy |
| [22553997](https://pubmed.ncbi.nlm.nih.gov/22553997/) | 2012 | Case Series | *PACE* | Flecainide successfully suppressed ICD-induced arrhythmic storming in CPVT; highlights superiority of flecainide over amiodarone in this context |
| [37852665](https://pubmed.ncbi.nlm.nih.gov/37852665/) | 2023 | Case Report | *BMJ Case Reports* | Child with out-of-hospital cardiac arrest from CPVT received 40 defibrillation shocks; multimodal pharmacotherapy including amiodarone used with partial response |
| [22218697](https://pubmed.ncbi.nlm.nih.gov/22218697/) | 2012 | Case Report | *Anesthesia & Analgesia* | Neonate with long QT syndrome and refractory VT managed with lidocaine, esmolol, and amiodarone plus pacing; illustrates amiodarone use in neonatal refractory arrhythmia |
| [17125720](https://pubmed.ncbi.nlm.nih.gov/17125720/) | 2006 | Case Report | *Revista Española de Cardiología* | Arrhythmic storm induced by ICD discharge in a CPVT patient; documents the clinical management challenge and limited pharmacological options |
| [39735866](https://pubmed.ncbi.nlm.nih.gov/39735866/) | 2024 | Case Report | *Frontiers in Cardiovascular Medicine* | Successful CPVT resolution via bilateral cardiac sympathetic denervation in a teenager after failure of multiple drug therapies; contextualises surgical fallback |
| [29668588](https://pubmed.ncbi.nlm.nih.gov/29668588/) | 2018 | Case Report | *Medicine* | Six-year delayed CPVT diagnosis in a child with RYR2 c.7580T>G mutation; underscores diagnostic challenges and the need for early genetic testing |
| [30116135](https://pubmed.ncbi.nlm.nih.gov/30116135/) | 2018 | Case Report/Review | *Turk Pediatri Arsivi* | CPVT as a rare cause of sudden cardiac arrest in a 2-year-old; clinical overview of diagnosis and acute management |

---

## Australia Market Information

Based on the data available in this Evidence Pack, amiodarone does not have registered ARTG entries. No product information could be extracted.

> **Note for clinicians:** The absence of ARTG entries in this dataset may reflect a data query limitation. Amiodarone is widely used in Australian clinical practice (e.g., under brand names such as Cordarone and Aratac in international markets). Clinicians are strongly advised to verify current registration status directly via the [TGA ARTG public portal](https://www.tga.gov.au/resources/artg) before making any prescribing decisions.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

> Amiodarone carries a well-recognised complex safety profile internationally, including pulmonary toxicity, thyroid dysfunction (both hypo- and hyperthyroidism due to its high iodine content), hepatotoxicity, corneal microdeposits, photosensitivity, peripheral neuropathy, and proarrhythmic risk (including QT prolongation and torsades de pointes). Drug-specific safety data was not available in this Evidence Pack and clinicians should consult the current TGA-approved PI or the most recent product prescribing information before use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.78%), the mechanistic analysis reveals that amiodarone cannot directly correct the core RYR2-mediated SR calcium leak pathology of CPVT, and available clinical evidence is limited to case reports and small cohort studies (Evidence Level L4). Current CPVT treatment guidelines preferentially recommend beta-blockers and flecainide, with amiodarone considered only in refractory arrhythmic storm where its benefit remains uncertain. Additionally, amiodarone is not currently registered with the TGA based on available data, creating further regulatory barriers for use in Australia.

**To proceed, the following is needed:**
- A structured systematic review specifically examining amiodarone outcomes in genotype-confirmed CPVT patients, compared with standard-of-care (beta-blockers ± flecainide)
- Mechanistic studies (in vitro or animal model) clarifying amiodarone's effect on RYR2-mediated calcium handling
- Verification of TGA registration status directly via the ARTG portal; if unregistered, a regulatory pathway assessment would be required
- Drug-drug interaction analysis for amiodarone combined with beta-blockers and flecainide (the standard CPVT regimen), given amiodarone's extensive CYP2D6 and CYP3A4 inhibition profile
- MOA data retrieval from DrugBank (DB01118) to complete the mechanistic link assessment

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application. Healthcare professionals should consult current TGA-approved prescribing information and relevant clinical guidelines for patient management decisions.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

