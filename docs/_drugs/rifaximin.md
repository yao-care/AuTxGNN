---
layout: default
title: Rifaximin
parent: Moderate Evidence (L3-L4)
nav_order: 633
evidence_level: L4
indication_count: 10
---

# Rifaximin
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

# Rifaximin: From Hepatic Encephalopathy to Oral Candidiasis

## One-Sentence Summary

Rifaximin is a gut-restricted, minimally absorbed oral antibiotic, originally used for hepatic encephalopathy and hepatic coma.
The TxGNN model predicts it may be effective for **oral candidiasis**, but there are **no registered clinical trials** and only **1 publication**, and that publication suggests rifaximin use may be *associated with more* Candida infections rather than fewer.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hepatic encephalopathy; hepatic coma (the ARTG entry does not list indication text) |
| Predicted New Indication | Oral candidiasis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, rifaximin is a non-absorbed oral antibiotic that acts locally in the gut. Its efficacy in hepatic encephalopathy is established, but it has no known antifungal activity, so a mechanistic link to oral candidiasis is not evident.

The one publication identified (PMID 34180023) points the other way. In patients undergoing allogeneic stem cell transplantation, rifaximin use was associated with micafungin-resistant Candida infections. A plausible explanation is gut microbiome disruption that allows fungal overgrowth, although confounding by underlying disease cannot be excluded. The high TxGNN score therefore looks more like a knowledge-graph artefact than a genuine therapeutic signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | Cohort | Annals of Hematology | In allogeneic stem cell transplant recipients, rifaximin use was associated with micafungin-resistant Candida infections. This is a potential harm signal, not a benefit. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10001J | Xifaxan | Tablet 550 mg | Not available in the data compiled for this report |

## Safety Considerations

- **Conditions flagged as contraindications in the knowledge graph** (not taken from label text): *Clostridium difficile* colitis and perinatal necrotizing enterocolitis.
- **Drug Interactions**: 69 interactions were identified. Those listed below are examples from the data compiled for this report.
  - **Major**: live oral cholera vaccine (*Vibrio cholerae* CVD 103-HgR strain).
  - **Moderate**: warfarin, cyclosporine, tolvaptan, picosulfuric acid, apalutamide, darolutamide, cabozantinib, encorafenib, alpelisib, brigatinib, capmatinib, daclatasvir, ledipasvir, elagolix, elexacaftor, eliglustat, enasidenib, bempedoic acid and istradefylline.
- Product Information warnings and contraindications were not available. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. The single publication suggests a possible adverse association with Candida infection, and rifaximin has no known antifungal activity. The available evidence does not justify further development for this indication.

**To proceed, the following is needed:**
- Evidence of a plausible antifungal or microbiome-based mechanism, together with mechanism of action data for rifaximin.
- Controlled data clarifying whether rifaximin increases or decreases Candida colonisation and infection.
- The approved indication text and PI safety information for the Australian product.

**Other predicted indications:** Among the other top-ranked predictions, only **HIV infectious disease** (L3) has meaningful supporting literature. Studies there show marginal effects on microbial translocation and immune activation, and the one registered trial (NCT01654939) was withdrawn with no participants enrolled. It may merit consideration as a research question, but not as a treatment indication. The remaining predictions have no supporting clinical evidence and should be held.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

