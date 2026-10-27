---
layout: default
title: Cocaine
parent: Model Prediction Only (L5)
nav_order: 181
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Cocaine: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not recorded in the ARTG data"
monitor_inn: "Cocaine"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "papillary conjunctivitis", "rhinitis", "irritable bowel syndrome", "anaphylaxis", "neurocirculatory asthenia", "atopic conjunctivitis", "food-dependent exercise-induced anaphylaxis", "pharyngitis"]
---

# Cocaine
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

## Cocaine: From Local Anaesthesia to Cauda Equina Syndrome
{: .text-alpha }

## One-Sentence Summary

Cocaine is a natural-product local anaesthetic and monoamine reuptake inhibitor, with a single ARTG entry in Australia, but no approved indication text is recorded in the data compiled for this report.
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but there are **0 clinical trials** and only **1 publication** (a case report that does not describe cocaine as a treatment).
This prediction appears to be a model artefact and is not supported by evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the ARTG data (pharmacology data describes use as a local anaesthetic in nasal, oral and laryngeal surgery) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on pharmacology information, cocaine acts as a local anaesthetic (sodium channel blockade) and as a monoamine reuptake inhibitor, including at the dopamine transporter (DAT). It also has recorded activity at 5-HT3 receptors.

Cauda equina syndrome is a compressive neurological emergency, typically caused by lumbosacral disc pathology, that presents with urinary retention, faecal incontinence, saddle anaesthesia and lower-limb weakness. Management is surgical decompression. No plausible mechanistic link between cocaine and treatment of this condition was identified. The single publication retrieved is a case report on disc pathology and does not involve cocaine therapy.

The high TxGNN score therefore appears to be a prediction artefact rather than a reflection of a real therapeutic opportunity.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31528422](https://pubmed.ncbi.nlm.nih.gov/31528422/) | 2019 | Case report / Review | Surgical Neurology International | Case report of distal cauda equina syndrome from lumbosacral disc pathology with literature review; does not describe cocaine as a treatment |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 189Y | Not recorded | Not recorded | Not recorded |

## Safety Considerations

- **Disease associations from the knowledge graph** (not label text): the TxGNN knowledge graph lists contraindication links with epilepsy, sudden cardiac arrest, heart conduction disease, thyrotoxicosis, hyperthyroidism and Graves disease.
- **Pharmacological targets**: cocaine has recorded activity at 5-HT3AB, 5-HT3A and the dopamine transporter (DAT). These are target-level pharmacology records, not graded clinical drug interactions.
- **Literature signals**: the retrieved literature repeatedly describes cocaine as a cause of harm, including mucosal necrosis, septal and palatal perforation, bronchospasm, vasculitis (with levamisole-contaminated supply) and upper aerodigestive tract injury. Cocaine is also reported as an allergen, and it carries abuse liability and serious cardiovascular risk.

Please refer to the TGA-approved Product Information (PI) for formal warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported by model output only (L5), with no clinical trials and no literature showing benefit. The mechanism is implausible for a compressive neurological condition, and the safety profile, including cardiovascular risk and abuse liability, argues against pursuing this indication.

The other predicted indications reviewed (obsolete neurogenic bladder, papillary conjunctivitis, rhinitis, irritable bowel syndrome, anaphylaxis, neurocirculatory asthenia, atopic conjunctivitis, food-dependent exercise-induced anaphylaxis and pharyngitis) also lack supporting clinical evidence. Rhinitis reached L4 only because of preclinical and surgical-field literature. All are recommended as Hold.

**To proceed, the following is needed:**
- TGA Product Information with warnings, contraindications and approved indications for ARTG 189Y
- Mechanism of action data to support any mechanistic-link analysis
- Any credible clinical or preclinical evidence of therapeutic benefit in the predicted condition
- A safety and controlled-substance assessment before any further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

