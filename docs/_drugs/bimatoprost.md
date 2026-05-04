---
layout: default
title: Bimatoprost
parent: 僅模型預測 (L5)
nav_order: 87
evidence_level: L5
indication_count: 10
---

# Bimatoprost
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

# Bimatoprost: From Glaucoma/Ocular Hypertension to Malformation Syndrome with Odontal and/or Periodontal Component

## One-Sentence Summary

Bimatoprost is a synthetic prostamide F2α analogue originally used to lower intraocular pressure in patients with open-angle glaucoma or ocular hypertension, and is separately FDA-approved for promoting eyelash growth in hypotrichosis (Latisse).
The TxGNN model predicts it may have activity in **malformation syndrome with odontal and/or periodontal component** — a rare disease category characterised by structural abnormalities of the teeth and periodontium.
However, **0 clinical trials** and **no bimatoprost-specific publications** were identified for this indication; the 20 retrieved literature items represent general periodontitis background literature only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Open-angle glaucoma / Ocular hypertension (known clinical use; no ARTG registration identified) |
| Predicted New Indication | Malformation syndrome with odontal and/or periodontal component |
| TxGNN Prediction Score | 99.997% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, bimatoprost is a synthetic prostamide F2α analogue that binds prostaglandin FP receptors and prostamide-specific receptors in ocular tissues, reducing aqueous humour production and thereby lowering intraocular pressure. Its hair-growth-promoting properties — the basis for its use in eyelash hypotrichosis — are thought to arise from prostaglandin FP receptor-mediated stimulation of the anagen phase of the hair follicle cycle.

The theoretical link to odontal and periodontal conditions rests on the broader role of prostanoids in inflammation. Prostaglandins, particularly PGE2, are well-established mediators of periodontal pathogenesis: they drive osteoclast-mediated alveolar bone resorption, sustain the chronic inflammatory microenvironment, and are produced in elevated amounts in inflamed gingival tissue. As a prostamide analogue, bimatoprost may interact with these same inflammatory pathways, which could explain why TxGNN's knowledge graph identified a topological association between bimatoprost and this disease cluster.

It is important to emphasise, however, that this mechanistic bridge is highly speculative. No published studies — clinical or preclinical — have directly investigated bimatoprost in odontal or periodontal malformation syndromes. The TxGNN prediction score reflects graph-level connectivity rather than direct experimental evidence, and the disease entity itself ("malformation syndrome with odontal and/or periodontal component") represents a heterogeneous rare-disease category that would require precise phenotypic definition before any translational work could begin.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this specific indication.

---

## Literature Evidence

The 20 publications below were retrieved via the evidence pipeline using a broad "bimatoprost + periodontal/odontal malformation" query. **None of these papers specifically study bimatoprost in this indication** — they represent general periodontitis background literature identified as contextually related to the predicted disease category. They are included here for completeness to characterise the disease landscape.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38907216](https://pubmed.ncbi.nlm.nih.gov/38907216/) | 2024 | Review | J Nanobiotechnology | Biomaterial-mediated macrophage immunotherapy as an emerging strategy in periodontitis; highlights role of innate immune modulation in disease resolution |
| [38362600](https://pubmed.ncbi.nlm.nih.gov/38362600/) | 2024 | Observational | J Dent Res | Periodontitis associated with oral-gut microbial dysbiosis; periodontal therapy partially restores microbial composition |
| [37452425](https://pubmed.ncbi.nlm.nih.gov/37452425/) | 2023 | Research | Adv Sci | Melatonin-engineered M2 macrophage-derived exosomes mediate anti-inflammatory reprogramming and improve outcomes in periodontitis models |
| [37435999](https://pubmed.ncbi.nlm.nih.gov/37435999/) | 2023 | Review | Periodontol 2000 | Systematic review of complications in regenerative periodontal surgery; technical and biological pitfalls in managing intrabony and furcation defects |
| [36883660](https://pubmed.ncbi.nlm.nih.gov/36883660/) | 2023 | Review | J Dent Res | Gingival fibroblasts act as sentinel innate immune cells in periodontal pathogenesis; respond to bacterial signals via pattern recognition receptors |
| [35688447](https://pubmed.ncbi.nlm.nih.gov/35688447/) | 2022 | Clinical Guideline | J Clin Periodontol | EFP S3-level clinical practice guideline for treatment of Stage IV periodontitis; covers surgical and prosthetic sequelae management |
| [35420698](https://pubmed.ncbi.nlm.nih.gov/35420698/) | 2022 | Systematic Review | Cochrane Database Syst Rev | Cochrane review: periodontal treatment modestly improves HbA1c in people with diabetes; reinforces bidirectional periodontitis-diabetes relationship |
| [22057194](https://pubmed.ncbi.nlm.nih.gov/22057194/) | 2012 | Review | Diabetologia | Landmark review on diabetes as a major risk factor for periodontitis (~threefold increased susceptibility); discusses bidirectional inflammatory mechanisms |
| [20599785](https://pubmed.ncbi.nlm.nih.gov/20599785/) | 2010 | Review | Biochem Pharmacol | Complement system deregulation as a driver of periodontal immunopathology; potential therapeutic target in disease modification |
| [18673013](https://pubmed.ncbi.nlm.nih.gov/18673013/) | 2008 | Review | J Periodontol | Biologic systems model of periodontal inflammation integrating microbial, systemic immune, and gingival inflammatory mediator profiles |

---

## Australia Market Information

No ARTG entries were identified for bimatoprost in the regulatory query conducted on 9 March 2026.

> **Important note for reviewers**: This result warrants independent verification against the current TGA ARTG public database. Bimatoprost-containing products — including ophthalmic solutions for glaucoma (e.g., Lumigan, Ganfort) and eyelash growth formulations (e.g., Latisse) — are registered in comparable markets (US FDA, EMA). An updated TGA search using product brand names and the ingredient name "bimatoprost" is recommended before concluding the drug is absent from the Australian market.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

> No drug interaction data, key warnings, or contraindication data were returned in this evidence pack. A targeted review of the TGA PI documents and ARTG entries (once confirmed) is required before any clinical safety assessment can be completed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model produces a very high prediction score (99.997%) for bimatoprost in odontal/periodontal malformation syndrome; however, this signal is currently unsupported by any bimatoprost-specific clinical trials or direct mechanistic research for this indication. The retrieved literature reflects general periodontitis science rather than drug-disease evidence. The biological rationale — prostanoid involvement in periodontal inflammation — is plausible but remains hypothetical. Combined with the absence of Australian market registration, this candidate does not yet meet the threshold for active development.

**To proceed, the following is needed:**

- **Regulatory verification**: Confirm current ARTG status by searching the TGA public register using brand names (Lumigan, Latisse, Ganfort) and the INN "bimatoprost"
- **MOA data retrieval**: Obtain full mechanism of action details from DrugBank (DB00905) to enable a rigorous mechanistic plausibility assessment
- **Safety data retrieval**: Download and parse the TGA Product Information PDF to extract current warnings, contraindications, and precautions
- **Targeted literature search**: Conduct a focused PubMed/MEDLINE search for ("bimatoprost" OR "prostamide") AND ("periodontal" OR "periodontitis" OR "odontal" OR "dental malformation") to identify any direct evidence not captured in the current pipeline
- **Disease phenotyping**: Clarify which specific rare disease entities are grouped under "malformation syndrome with odontal and/or periodontal component" (ORPHA classification) to assess biological plausibility at a disease-specific level
- **Preclinical evidence review**: If direct clinical evidence remains absent after the above steps, evaluate whether bimatoprost has been studied in periodontal inflammation animal models before any translational decision is made

---

*This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All website pages should include YMYL disclaimer language consistent with TGA regulatory expectations.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

