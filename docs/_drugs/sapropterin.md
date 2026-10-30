---
layout: default
title: Sapropterin
parent: Model Prediction Only (L5)
nav_order: 659
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-30
description: "Sapropterin: predicted new indication Disorder of tyrosine metabolism (evidence level L4). Approved use: Phenylketonuria"
monitor_inn: "Sapropterin"
predicted_indications: ["disorder of tyrosine metabolism", "teratogenic Pierre Robin syndrome", "hyperphenylalaninemia due to tetrahydrobiopterin deficiency"]
---

# Sapropterin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Sapropterin: From Phenylketonuria to Disorder of Tyrosine Metabolism
{: .text-alpha }

## One-Sentence Summary

Sapropterin is a synthetic form of tetrahydrobiopterin (BH4), originally used to treat phenylketonuria (PKU) and other disorders of phenylalanine metabolism.
The TxGNN model predicts it may be effective for **disorder of tyrosine metabolism**, but **no clinical trials** are registered for this term, and the **15 publications** retrieved concern PKU, the original indication, rather than a new one.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Phenylketonuria; disorder of phenylalanine metabolism (approved indication text is not listed for the ARTG entry) |
| Predicted New Indication | Disorder of tyrosine metabolism |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, sapropterin is a synthetic analogue of tetrahydrobiopterin (BH4), the natural cofactor of phenylalanine hydroxylase. This enzyme converts phenylalanine to tyrosine. Its efficacy in BH4-responsive PKU is established.

The link to "disorder of tyrosine metabolism" is indirect. The retrieved literature is about PKU, not primary tyrosine disorders such as tyrosinemia. The ontology appears to group PKU under tyrosine and aromatic amino acid metabolism, so the high score probably reflects the existing indication rather than a genuinely new one. This prediction should be treated with caution.

Other predictions in the list point the same way:
- **BH4-responsive hyperphenylalaninemia/PKU** and **hyperphenylalaninemia due to BH4 deficiency** are effectively on-label or very close to the original indication. They are clinical standard care rather than true repurposing.
- Lower-ranked predictions such as teratogenic Pierre Robin syndrome have no identifiable mechanistic link. Their scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. This prediction has no trial or literature support.

## Clinical Trial Evidence

Currently no related clinical trials registered for disorder of tyrosine metabolism.

For context, the KAMPER registry (NCT01016392) is an observational study of long-term sapropterin safety in PKU. It is not evidence for the predicted indication.

## Literature Evidence

None of the publications below addresses primary tyrosine metabolism disorders. They concern PKU and are shown for context. No RCT of sapropterin in the predicted indication was identified.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29025426](https://pubmed.ncbi.nlm.nih.gov/29025426/) | 2017 | Guideline | Orphanet J Rare Dis | European guidelines on PKU diagnosis and treatment |
| [34784942](https://pubmed.ncbi.nlm.nih.gov/34784942/) | 2021 | Consensus statement | Orphanet J Rare Dis | Italian consensus on PKU management and pharmacological treatment |
| [39237321](https://pubmed.ncbi.nlm.nih.gov/39237321/) | 2025 | Long-term safety study | J Inherit Metab Dis | KAMPER registry final results: long-term safety of sapropterin in 576 participants with PAH deficiency |
| [35899555](https://pubmed.ncbi.nlm.nih.gov/35899555/) | 2022 | Guideline/Consensus | Turk J Pediatr | Expert recommendations on PKU diagnosis, treatment and follow-up in Turkey |
| [20738029](https://pubmed.ncbi.nlm.nih.gov/20738029/) | 2010 | Review | Prescrire Int | Sapropterin helps only a minority of PKU patients |
| [42123950](https://pubmed.ncbi.nlm.nih.gov/42123950/) | 2026 | Review | Nutrients | Nutritional and therapeutic strategies in paediatric PKU |
| [30359206](https://pubmed.ncbi.nlm.nih.gov/30359206/) | 2020 | Review | Nutr Neurosci | Dietary therapeutic approaches in PKU |
| [20123474](https://pubmed.ncbi.nlm.nih.gov/20123474/) | 2010 | Review | Mol Genet Metab | Psychosocial issues and outcomes in maternal PKU |
| [34654619](https://pubmed.ncbi.nlm.nih.gov/34654619/) | 2021 | Registry cohort | Mol Genet Metab | Natural history of PKU in the NBS-PKU Connect registry |
| [26653793](https://pubmed.ncbi.nlm.nih.gov/26653793/) | 2016 | Preclinical (mouse) | Mol Genet Metab | High-dose sapropterin improved monoamine neurotransmitter turnover in murine PKU |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 10086W | Kuvan | Tablet (soluble) containing sapropterin dihydrochloride 100 mg (oral) | Not listed in the data compiled for this report |

## Safety Considerations

- **Contraindications (knowledge graph, not label text)**: neutropenia and agranulocytosis are recorded as contraindicated disease associations.
- **Drug Interactions**: 21 interactions are recorded, all Moderate. Main groups:
  - Vasodilators and nitrates: nitroglycerin, isosorbide dinitrate, isosorbide mononitrate, nitroprusside, nesiritide, hydralazine, minoxidil (oral and topical), alprostadil
  - PDE5 inhibitors: sildenafil, tadalafil, vardenafil
  - Folate-pathway antagonists: methotrexate, pemetrexed, pralatrexate, trimetrexate, trimethoprim, pyrimethamine, proguanil
  - Levodopa

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted new indication has no registered trials and no specific literature. The high score appears to reflect the existing PKU indication rather than a true new use. The closely related BH4-responsive PKU and BH4-deficiency hyperphenylalaninemia are better handled as on-label or established-practice uses than as repurposing candidates.

**To proceed, the following is needed:**
- Clarification of whether "disorder of tyrosine metabolism" refers to a primary tyrosine disorder (such as tyrosinemia) or is an ontology artefact of PKU
- Mechanism of action data, which were unavailable for this report
- TGA Product Information (warnings, contraindications and approved indication text) for the Kuvan ARTG entry
- Reclassification of BH4-responsive PKU and BH4-deficiency hyperphenylalaninemia as on-label indications
- Preclinical or clinical evidence specific to the predicted indication, if it is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

