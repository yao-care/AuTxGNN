---
layout: default
title: Deferasirox
parent: 僅模型預測 (L5)
nav_order: 143
evidence_level: L5
indication_count: 10
---

# Deferasirox
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

# Deferasirox: From Chronic Iron Overload to HIV Infectious Disease

## One-Sentence Summary

Deferasirox (brand names: Exjade®, Jadenu®) is an oral iron chelator used internationally for treating chronic iron overload in patients dependent on blood transfusions, including those with beta-thalassemia and other haemolytic anaemias.
The TxGNN model predicts it may be effective for **HIV Infectious Disease**, with **2 mechanistic publications** currently supporting this direction.
Evidence remains at the preclinical stage only, making this a research question rather than an immediately actionable repurposing candidate.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic iron overload (transfusion-dependent; principally beta-thalassemia) |
| Predicted New Indication | HIV Infectious Disease |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L4 |
| Australia Market Status | Not registered (0 ARTG entries found — data gap suspected; verify via TGA ARTG search) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Deferasirox is a tridentate, orally bioavailable iron chelator that selectively binds trivalent iron (Fe³⁺) with high affinity. By sequestering excess intracellular and circulating iron, it blocks the Fenton reaction, reduces the generation of reactive oxygen species, and prevents iron-mediated organ damage in the liver, heart, and endocrine glands.

The biological rationale connecting iron chelation to HIV is provided by a cell-level mechanistic study (PMID 34550543). HIV-1 Tat protein — a critical transactivator required for viral replication — enters cells via receptor-mediated endocytosis and accumulates in endolysosomes. When endolysosomal iron levels are elevated, Tat protein disperses into the cytosol and nucleus, activating the HIV-1 LTR promoter and driving viral transcription. This study demonstrates that **iron restriction promotes Tat oligomerisation**, trapping it within endolysosomes and suppressing LTR transactivation — theoretically inhibiting the HIV-1 replication cycle.

The TxGNN model's high prediction score (0.994) most likely reflects the strong topological connectivity between iron metabolism nodes and HIV-related nodes in the knowledge graph. While the mechanistic hypothesis is biologically plausible, all available evidence is at the in vitro/cellular level. No animal studies or human clinical data exist. Independent validation through a stepwise preclinical programme (in vitro → animal model → Phase 1/2 trials) would be required before any clinical application could be considered.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [34550543](https://pubmed.ncbi.nlm.nih.gov/34550543/) | 2021 | Basic Science / Mechanism Study | Journal of Neurovirology | Endolysosomal iron restriction promotes HIV-1 Tat oligomerisation and upregulates β-catenin expression, thereby suppressing Tat-mediated HIV-1 LTR transactivation; suggests iron chelation may inhibit HIV-1 replication at the cellular level and could be relevant to HIV-associated neurocognitive disorder (HAND) pathogenesis |
| [16529348](https://pubmed.ncbi.nlm.nih.gov/16529348/) | 2006 | Drug Approval Review | Journal of the American Pharmacists Association | Narrative overview of newly approved drugs (ramelteon, tipranavir, nepafenac, and deferasirox) at time of initial FDA approval; provides contextual background on Deferasirox's original approval but does not address HIV repurposing |

---

## Australia Market Information

According to this Evidence Pack, Deferasirox has no current ARTG entries. This is highly likely to represent a **data capture gap** rather than genuine non-registration — Deferasirox (Exjade®) is TGA-approved in other comparable markets (FDA 2005, EMA 2006) and is likely available in Australia via ARTG listing or the Special Access Scheme (SAS).

Clinicians should verify current registration status directly via the [TGA ARTG Public Summary](https://www.tga.gov.au/resources/artg) before making any prescribing or formulary decisions.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for complete safety information. Full safety data (TGA-registered warnings, contraindications, and drug interaction data) are not available in this Evidence Pack.

The following class-level safety signals are well-documented for Deferasirox in the international literature and should be considered during any further evaluation:

- **Renal toxicity**: Acute kidney injury, including fatal cases, has been reported; serum creatinine and eGFR monitoring is mandatory
- **Hepatotoxicity**: Liver failure, including fatal cases, has been reported; LFTs should be monitored regularly
- **Gastrointestinal adverse effects**: Nausea, vomiting, diarrhoea, and abdominal pain are common dose-dependent effects
- **Auditory and ocular toxicity**: High-frequency hearing loss and lens opacities have been reported with long-term use
- **Cytopenias**: Agranulocytosis, neutropenia, and thrombocytopenia have been reported (postmarketing)

*These are general class-effect considerations derived from international regulatory documents, not from the Evidence Pack data. Formal TGA safety data should be obtained before any clinical use.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for Deferasirox in HIV infectious disease consists solely of one in vitro mechanistic study demonstrating iron restriction can suppress HIV-1 Tat-mediated LTR transactivation at the cellular level. There are no registered clinical trials, no animal model data, and no clinical outcome evidence — this represents a biologically plausible hypothesis, not a repurposing candidate ready for clinical evaluation.

**To proceed to a Research Question evaluation (S1), the following is needed:**

- Obtain TGA-approved Product Information (PI) to document approved indications, contraindications, and warnings
- Confirm ARTG registration status and current Australian market availability
- Retrieve full MOA data from DrugBank (DB01609) to enable mechanistic linkage analysis
- Commission or identify in vitro HIV replication assays using Deferasirox at therapeutically relevant iron-chelating concentrations
- Review animal model literature (including SIV primate models) to assess in vivo plausibility
- Conduct a structured drug–drug interaction analysis with standard HIV antiretroviral regimens (NRTIs, NNRTIs, PIs, INSTIs), as iron chelation may affect drug absorption and metabolism
- Consider whether the target population (iron-overloaded HIV patients, e.g., those with co-existing haemoglobinopathy) represents a more tractable niche indication than general HIV treatment

---

> **Disclaimer:** This report is produced for research purposes only and does not constitute medical advice. Drug repurposing candidates require rigorous clinical validation before any therapeutic application. All clinical decisions should reference TGA-approved Product Information and current clinical guidelines.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

