---
layout: default
title: Loperamide
parent: Model Prediction Only (L5)
nav_order: 434
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Loperamide: predicted new indication Acute contagious conjunctivitis (evidence level L5). Approved use: Diarrhoeal disease"
monitor_inn: "Loperamide"
predicted_indications: ["acute contagious conjunctivitis", "amebic dysentery", "conjunctivitis", "gastroduodenitis", "pseudomembranous conjunctivitis", "parasitic conjunctivitis", "conjunctival folliculosis", "serous conjunctivitis except viral", "chronic follicular conjunctivitis", "Angelucci syndrome"]
---

# Loperamide
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

## Loperamide: From Diarrhoeal Disease to Acute Contagious Conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Loperamide is an antimotility agent originally used to treat diarrhoeal disease and dysentery.
The TxGNN model predicts it may be effective for **acute contagious conjunctivitis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction appears to be a graph-based artefact rather than a pharmacologically grounded finding.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diarrhoeal disease; dysentery |
| Predicted New Indication | Acute contagious conjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Loperamide is generally understood to be a peripheral mu-opioid receptor agonist acting on gut myenteric neurons, slowing intestinal motility. It is not an anti-infective or an ocular agent.

The review of the prediction found **no plausible mechanistic link** between loperamide and acute contagious conjunctivitis. The high TxGNN score most likely reflects shared infectious-disease and diarrhoea associations in the knowledge graph, not real pharmacology. The same pattern appears across the other top-ranked predictions: several conjunctival terms (parasitic, follicular, serous, pseudomembranous conjunctivitis, conjunctival folliculosis) share identical or near-identical scores, which is consistent with an ontology-driven artefact.

Other predictions in the top 10 were also reviewed. Only two had any literature, and both were safety signals rather than efficacy evidence:
- **Amoebic dysentery:** A 2007 case report described fulminant amoebic colitis following heavy loperamide use. Loperamide treats the symptom, not the *Entamoeba histolytica* infection, and slowing gut transit may worsen invasive disease. This is an overlap with the original symptomatic indication, not a true repurposing opportunity.
- **Gastroduodenitis:** A 2026 case report described loperamide-induced respiratory depression in severe gastrointestinal inflammation, suggesting increased systemic exposure when the gut barrier is compromised.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for acute contagious conjunctivitis.

For context, the literature found for other top-ranked predictions is summarised below (none supports efficacy):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17241255](https://pubmed.ncbi.nlm.nih.gov/17241255/) | 2007 | Case report | J Travel Med | Fulminant amoebic colitis and toxic megacolon after heavy loperamide use (amoebic dysentery prediction) |
| [41924411](https://pubmed.ncbi.nlm.nih.gov/41924411/) | 2026 | Case report | Cureus | Respiratory depression with loperamide in severe chemotherapy-related GI inflammation (gastroduodenitis prediction) |
| [3893119](https://pubmed.ncbi.nlm.nih.gov/3893119/) | 1985 | Review | Am J Med | Non-fluid therapy and chemoprophylaxis of acute diarrhoea (amoebic dysentery prediction) |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 10592L | Gastrex | Capsule containing loperamide hydrochloride 2 mg | Not specified in the data compiled for this report |

---

## Safety Considerations

- **Contraindications (knowledge-graph derived, not label text):** liver disease, gallbladder disease, paralytic ileus, intestinal obstruction, familial visceral myopathy, dysentery, diarrhoeal disease, infectious diarrhoeal disease, intestinal infectious disease.
- **Drug Interactions:** 100 interactions were identified. Examples rated **Major**: abiraterone, ranitidine, fosamprenavir, gemfibrozil. Examples rated **Moderate**: codeine, dihydrocodeine, tramadol (additive opioid or CNS effects), chlorpheniramine, cetirizine, acrivastine, ethanol, salbutamol, galantamine, gemifloxacin.
- **Case-report safety signals:** toxic megacolon in infectious colitis, and systemic opioid effects (respiratory depression) when the gut barrier is inflamed.

Please also refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for acute contagious conjunctivitis rests on model score alone (L5), with no trials, no literature and no plausible mechanism. Loperamide is also an oral gut-acting agent with no ocular route or activity. The remaining top predictions are either similarly unsupported or carry safety concerns.

**To proceed, the following is needed:**
- Mechanism of action data and a credible mechanistic hypothesis for ocular disease
- Preclinical evidence of anti-infective or anti-inflammatory activity in the conjunctiva
- Route-of-administration feasibility assessment (no ocular formulation is available)
- TGA Product Information warnings and contraindications for formal safety screening
- Approved indication text for the ARTG entry
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

