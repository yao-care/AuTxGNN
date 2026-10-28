---
layout: default
title: Ritonavir
parent: Moderate Evidence (L3-L4)
nav_order: 642
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-28
monitor_inn: "Ritonavir"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
description: "Ritonavir: predicted new indication Simian immunodeficiency virus infection (evidence level L4). Approved use: Not recorded in the local data"
---

# Ritonavir
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

## Ritonavir: Simian immunodeficiency virus infection
{: .text-alpha }

## One-Sentence Summary

Ritonavir is an HIV protease inhibitor that is also widely used as a pharmacokinetic booster. Its original indications are HIV infection and AIDS, plus chronic hepatitis C as part of combination regimens.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**, but this is a non-human primate disease used as a research model.
Support is limited to **0 clinical trials** and **10 publications**, mostly preclinical.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L4 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ritonavir is an HIV protease inhibitor and, at low doses, a CYP3A4 inhibitor used to boost other antivirals. Its efficacy in HIV infection is established, and mechanistically it may be applicable to SIV.

SIV is a lentivirus closely related to HIV, and its protease is inhibited by HIV protease inhibitors. An in vitro study found that ritonavir inhibited SIVmac239 with a half-maximal effective concentration (EC50) of about 13 nM, compared with about 25 nM against HIV-1. The high score (0.9992) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

SIV infection occurs in non-human primates and is a research model, not a human indication. The prediction therefore has little direct clinical applicability and is best read as support for ritonavir's activity against lentiviruses.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the publications is an RCT or human clinical study. The table lists the most relevant items and omits a few that are off-topic or have no abstract.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | In vitro | Antimicrob Agents Chemother | SIVmac239 was inhibited by indinavir, saquinavir and ritonavir (ritonavir about 13 nM versus about 25 nM for HIV-1) |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro | Antivir Ther | Compared 16 approved antivirals against HIV-2, SIV and SHIV to guide treatment and post-exposure prophylaxis |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Animal (macaque) | PLoS Pathog | A highly intensified multidrug ART regimen gave long-term viral suppression and restricted the viral reservoir in a simian AIDS model |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Animal (macaque) | J Virol | Quadruple ART produced rapid viral decay in SIVmac251-infected cynomolgus macaques |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Animal | PLoS One | Intensive cART plus the HDAC inhibitor SAHA in SIV-infected rhesus macaques, studying viral reservoirs |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Animal | mBio | Lentiviral infection persisted in the brain despite effective ART |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Animal | J Virol Methods | Oral HAART including lopinavir/ritonavir in SHIV-infected macaques, assessing effects on the CD8 subset |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Methods | Microbes Infect | Built a novel SHIV carrying the HIV-1 protease gene as a model for testing protease inhibitors in vivo |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10273Q | Norvir | Tablet 100 mg | Not specified in the data compiled |

## Safety Considerations

- **Contraindication-related conditions (from the TxGNN knowledge graph, not label text):** The graph links ritonavir to the following conditions. Several, such as long QT syndrome, pancreatitis, liver disease, cirrhosis, hyperglycaemia and diabetes, hyperlipidaemia and cardiac conduction disease, may warrant caution.
  - Cardiac: long QT syndrome, torsades de pointes, sudden cardiac arrest, heart conduction disease, atrioventricular block, cardiomyopathy, coronary artery disease, myocardial ischaemia
  - Hepatic and biliary: liver disease, cirrhosis, gallbladder disease, hyperbilirubinaemia, Gilbert syndrome, chronic hepatitis B
  - Metabolic: diabetes mellitus, diabetic ketoacidosis, hyperglycaemia, hypertriglyceridaemia, familial combined hyperlipidaemia, gout, potassium deficiency
  - Other: pancreatitis, haemophilia
- **Drug interactions:** 100 interactions are recorded, with the following examples.
  - Major: loperamide, triamcinolone, budesonide
  - Moderate: acarbose, metformin, alogliptin, canagliflozin, hydrocortisone, dexamethasone, betamethasone, bupropion, aprepitant, clarithromycin, metronidazole, alosetron, lorcaserin

Please also refer to the TGA-approved Product Information (PI) for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is an animal research model, with no registered clinical trials and only preclinical support (L4), so it is not a human repurposing opportunity. The very high score mainly reflects ritonavir's known activity against lentiviral protease. Two other predictions in the same output are on-label extensions of the HIV indication. These are congenital HIV and AIDS-related complex, both at L1 and suitable for "Proceed with Guardrails". They are worth reviewing separately.

**To proceed, the following is needed:**
- Re-prioritise the candidate list towards human indications, such as congenital HIV, rather than animal models
- Detailed mechanism of action data (MOA)
- The TGA Product Information (warnings, contraindications and approved indications) for the Norvir entry
- A review of the drug interaction burden before any new use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

