---
layout: default
title: Dornase Alfa
parent: Model Prediction Only (L5)
nav_order: 226
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Dornase Alfa: predicted new indication Ethmoid sinusitis (evidence level L5). Approved use: Cystic fibrosis"
monitor_inn: "Dornase alfa"
predicted_indications: ["ovarian melanoma", "eumycotic mycetoma", "ethmoid sinusitis", "equine infectious anemia", "epilepsy with generalized tonic-clonic seizures", "epiglottitis", "epidural abscess", "epidemic pleurodynia", "ephemeral fever", "enzootic pneumonia of calves"]
---

# Dornase Alfa
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

## Dornase alfa: From Cystic Fibrosis to Ethmoid Sinusitis
{: .text-alpha }

## One-Sentence Summary

Dornase alfa is a recombinant human DNase I, originally used to treat cystic fibrosis.
The TxGNN model's top-ranked prediction is **ovarian melanoma**, but it has no supporting evidence. The most biologically plausible candidate in the top 10 is **ethmoid sinusitis**, which has only **1 indirect publication** and **no registered clinical trials**.

> **Note on indication selection:** All ten predictions share an uninformative TxGNN score of 50%. The rank 1 prediction (ovarian melanoma) has no clinical or literature evidence and no credible mechanism. This report therefore centres on ethmoid sinusitis (rank 3), the only prediction with any supporting literature and a plausible mechanism. The other nine predictions are summarised below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cystic fibrosis |
| Predicted New Indication | Ethmoid sinusitis (rank 3; the rank 1 prediction, ovarian melanoma, has no evidence) |
| TxGNN Prediction Score | 50% (uninformative; identical across all ten predictions) |
| Evidence Level | L4 (ethmoid sinusitis); L5 for the other nine predictions |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold (ethmoid sinusitis is a research question only) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, dornase alfa is a recombinant human DNase I that breaks down extracellular DNA, including DNA released by neutrophils. This reduces the viscosity of thick, DNA-rich mucopurulent secretions. Its efficacy in cystic fibrosis lung disease is established.

Chronic rhinosinusitis is very common in people with cystic fibrosis. Their sinus secretions are neutrophil-dominated and DNA-rich, much like the airway secretions that dornase alfa is designed to thin. That makes a mechanism in sinus disease biologically plausible.

However, the only retrieved paper is a review of chronic rhinosinusitis *in cystic fibrosis patients*, the original indication population. It gives indirect support only. It does not show that dornase alfa works for ethmoid sinusitis, and no trials were identified.

**The other nine predictions are not supported:**

| Rank | Predicted Indication | Evidence Level | Assessment |
|------|------|------|------|
| 1 | Ovarian melanoma | L5 | No evidence. A speculative link to tumour-associated neutrophil extracellular traps exists, but nothing specific to this disease |
| 2 | Eumycotic mycetoma | L5 | No evidence. A theoretical effect on viscous DNA in grains is unsupported; antifungals and surgery remain standard care |
| 4 | Equine infectious anaemia | L5 | Veterinary disease with no plausible mechanism; likely a knowledge-graph artefact |
| 5 | Epilepsy with generalised tonic-clonic seizures | L5 | No plausible mechanism; an inhaled, locally acting enzyme has minimal systemic exposure |
| 6 | Epiglottitis | L5 | Acute airway emergency; mucolytics have no established role and nebulised agents could carry risk |
| 7 | Epidural abscess | L5 | Inhaled therapy is not applicable to a spinal infection; standard care is drainage plus antibiotics |
| 8 | Epidemic pleurodynia | L5 | Self-limiting viral illness with no unmet need this drug would address |
| 9 | Ephemeral fever | L5 | Bovine viral disease; likely a graph artefact |
| 10 | Enzootic pneumonia of calves | L5 | Veterinary disease; outside human repurposing scope |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27393775](https://pubmed.ncbi.nlm.nih.gov/27393775/) | 2016 | Review | J Allergy Clin Immunol Pract | Chronic rhinosinusitis is highly prevalent in cystic fibrosis and contributes significantly to morbidity and CF lung disease. Nasal polyps in CF are more neutrophilic, with fewer eosinophils. Indirect support only; not specific to ethmoid sinusitis or dornase alfa efficacy. |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 5704F | Pulmozyme | Solution for inhalation 2.5 mg (2,500 units) in 2.5 mL | Not listed in the data compiled for this report |

---

## Safety Considerations

- **Drug Interactions**: One moderate-level interaction is recorded, with inhaled rapid-acting human insulin (source: DDInter).

No warning or contraindication text was available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predictions carry an uninformative TxGNN score of 50%. Nine have no clinical or literature evidence, and several are veterinary diseases or have no plausible mechanism. Ethmoid sinusitis is biologically plausible, but the only supporting paper is an indirect review in cystic fibrosis patients, so it remains a research question rather than a candidate ready to proceed.

**To proceed, the following is needed:**
- Mechanism of action data for dornase alfa
- Product Information warnings and contraindications (a blocking gap for safety screening)
- Evidence on dornase alfa in non-CF chronic rhinosinusitis, such as a systematic literature search followed by pilot or exploratory trials
- Assessment of route compatibility, since the inhaled formulation may not suit sinus delivery (for example, nasal or sinus-directed administration would need evaluation)
- The approved indication text from the ARTG entry, to confirm the original indication against the TGA record
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

