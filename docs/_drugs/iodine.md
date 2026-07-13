---
layout: default
title: Iodine
parent: 僅模型預測 (L5)
nav_order: 270
evidence_level: L5
indication_count: 10
---

# Iodine
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

# Iodine: From Broad-Spectrum Antiseptic to Sjogren Syndrome

## One-Sentence Summary

Iodine (Povidone-Iodine/PVP-I, DrugBank DB05382) is a broad-spectrum antimicrobial element used clinically as a topical antiseptic for wound disinfection, surgical site preparation, and ophthalmic infections.
The TxGNN model predicts it may have biological relevance in **Sjogren Syndrome** — an autoimmune exocrine gland disorder — with **no registered clinical trials** and **20 publications** currently available in this area.
However, the available literature describes iodine primarily as a confounder or co-morbidity marker in this condition rather than a therapeutic agent, and the prediction appears to be driven by shared molecular biology (NIS-mediated) rather than direct treatment evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No TGA/ARTG registration on record (clinically used as broad-spectrum topical antiseptic) |
| Predicted New Indication | Sjogren Syndrome |
| TxGNN Prediction Score | 94.09% |
| Evidence Level | L4 |
| Australia Market Status | Not registered |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Iodine (DB05382) from DrugBank. Based on known clinical information, Iodine exerts its antimicrobial effects through the gradual release of free iodine at the site of application, which reacts with and inactivates bacterial, fungal, viral, and protozoal pathogens. Its efficacy as a broad-spectrum antiseptic has been well established across numerous clinical settings, and it has been studied in ophthalmic infections (keratitis), wound care, and surgical antisepsis.

The biological connection to Sjogren Syndrome centres on the **Sodium-Iodide Symporter (NIS)** — a transmembrane protein responsible for active iodide transport. NIS is highly expressed not only in the thyroid gland but also in salivary glands, which are the primary target of autoimmune destruction in Sjogren Syndrome. A 2025 computational immunoinformatics study (PMID 41516079) demonstrated that NIS epitopes are capable of triggering shared T-cell and B-cell immune responses that may link the pathogenesis of Sjogren Syndrome and Hashimoto's Thyroiditis, providing a plausible molecular basis for TxGNN's high prediction score.

Critically, the existing literature does **not** support iodine as a *therapeutic agent* for Sjogren Syndrome. The evidence points in the opposite direction: radioactive iodine (RAI) therapy for thyroid cancer is a documented *cause* of sialadenitis and sicca syndrome that closely mimics Sjogren Syndrome pathology (PMID 35817018, PMID 11337569). The NIS-iodide connection explains why iodine appears biologically related to Sjogren Syndrome in the knowledge graph, but this relationship reflects disease mechanism overlap and potential iatrogenic harm — not a therapeutic opportunity at the current stage of evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Iodine in Sjogren Syndrome.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [41516079](https://pubmed.ncbi.nlm.nih.gov/41516079/) | 2025 | In silico / Immunoinformatics | Int J Mol Sci | Computational analysis of NIS epitopes shows predicted T-cell and B-cell targets shared between Sjogren Syndrome and Hashimoto's Thyroiditis, providing a molecular-level rationale for the iodine–SS connection |
| [35817018](https://pubmed.ncbi.nlm.nih.gov/35817018/) | 2023 | Case series | ORL J Oto-Rhino-Laryngol | Sialendoscopy used to manage chronic sialadenitis caused by both Sjogren Syndrome and RAI therapy; RAI is documented as an independent cause of salivary gland damage |
| [30344785](https://pubmed.ncbi.nlm.nih.gov/30344785/) | 2018 | Diagnostic study | Nucl Med Mol Imaging | Quantitative SPECT/CT with Tc-99m pertechnetate assessed salivary gland dysfunction in SS patients; supports use of nuclear imaging to distinguish iodine-related damage from primary SS |
| [11337569](https://pubmed.ncbi.nlm.nih.gov/11337569/) | 2001 | Prospective cohort | J Nucl Med | High-dose RAI causes sicca syndrome (salivary + lacrimal dysfunction) resembling Sjogren Syndrome in 23% of patients at 3-year follow-up |
| [24899999](https://pubmed.ncbi.nlm.nih.gov/24899999/) | 2011 | Diagnostic study | Nucl Med Mol Imaging | Salivary gland scintigraphy parameters compared between SS patients and thyroid cancer patients post-RAI; functional overlap suggests shared NIS-mediated pathology |
| [12035942](https://pubmed.ncbi.nlm.nih.gov/12035942/) | 2002 | Observational | J Endocrinol Invest | Thyroid hormone autoantibodies more prevalent in primary Sjogren Syndrome than in Hashimoto's thyroiditis, supporting systemic autoimmune overlap involving iodine-metabolising organs |
| [7485204](https://pubmed.ncbi.nlm.nih.gov/7485204/) | 1995 | Observational | Am J Med | Autoimmune thyroid disease present in 45% of primary Sjogren Syndrome patients; prevalence significantly higher than in matched controls |
| [4951717](https://pubmed.ncbi.nlm.nih.gov/4951717/) | 1967 | Observational | Ann Rheum Dis | Reduced salivary flow rates and impaired iodide trapping capacity documented in Sjogren Syndrome patients, providing early evidence of NIS dysfunction in SS |
| [4965427](https://pubmed.ncbi.nlm.nih.gov/4965427/) | 1967 | Case series | Br J Ophthalmol | Historical description of co-occurrence of Sjogren Syndrome and thyroid disease; early clinical evidence of shared autoimmune exocrine-thyroid pathology |
| [3261973](https://pubmed.ncbi.nlm.nih.gov/3261973/) | 1988 | Case report | Arch Intern Med | Silent thyroiditis with marked depression of radioactive iodine uptake in a patient with concurrent Sjogren Syndrome; illustrates the bidirectional interplay between iodine metabolism and SS |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite the high TxGNN prediction score (94.09%), the mechanistic link between Iodine and Sjogren Syndrome reflects a biological association mediated by NIS co-expression in salivary glands — not a demonstrated therapeutic effect. All 20 identified publications describe iodine in the context of co-morbidity, diagnostic imaging, or iatrogenic harm (RAI-induced sialadenitis), and there are no clinical trials testing iodine as a treatment for Sjogren Syndrome. Advancing this candidate without preclinical therapeutic evidence would be premature and potentially counterproductive.

It is also worth noting for the broader drug repurposing programme: within the same evidence pack, **keratitis (rank 7)** presents a substantially stronger case for iodine repurposing (Evidence Level L2, two completed Phase 2 trials with 172–350 participants, one completed Phase 3 effort, and a broad-spectrum mechanistic rationale), warranting a **Proceed with Guardrails** decision for that indication.

**To proceed with Sjogren Syndrome, the following is needed:**

- Preclinical in vitro or in vivo studies specifically testing non-radioactive iodine formulations (e.g. PVP-I, Lugol's) in salivary gland inflammation models
- Mechanistic dose-response clarification: whether therapeutic iodine concentrations could modulate NIS-related immune pathways without inducing glandular cytotoxicity (the Wolff-Chaikoff effect is a particular concern)
- DrugBank MOA data retrieval (currently a data gap, severity High) to determine which iodine form/formulation the model is predicting upon
- Safety boundary analysis to establish a dose range that does not replicate RAI-like salivary gland damage before any clinical hypothesis is generated
- TGA regulatory consultation, as Iodine has no current ARTG registration under DrugBank entry DB05382
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

