---
layout: default
title: Colchicine
parent: 僅模型預測 (L5)
nav_order: 128
evidence_level: L5
indication_count: 10
---

# Colchicine
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

# Colchicine: From Autoinflammatory Conditions to Plasmodium falciparum Malaria

## One-Sentence Summary

Colchicine is a well-established anti-inflammatory alkaloid historically used for acute gout, pericarditis, and Familial Mediterranean Fever (FMF), exerting its effects by binding tubulin and suppressing neutrophil-mediated inflammation.
The TxGNN model predicts it may also be effective against **Plasmodium falciparum malaria** (prediction score 99.60%), based on the parasite's reliance on tubulin-based cell division — a mechanism Colchicine is known to disrupt.
Currently, **no clinical trials** and **6 preclinical or mechanistic publications** support this direction, placing overall evidence at Level **L4**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not specified in current dataset; historically used for gout, pericarditis, and Familial Mediterranean Fever |
| Predicted New Indication | Plasmodium falciparum malaria |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L4 (preclinical and mechanistic studies only) |
| Australia Market Status | Not marketed (no ARTG entries found in current dataset) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on established pharmacological knowledge, Colchicine is a plant-derived alkaloid that binds to the colchicine site on β-tubulin, preventing microtubule polymerisation and thereby halting cell division. Secondary to this, it suppresses neutrophil chemotaxis, inhibits the NLRP3/Pyrin inflammasome, and reduces pro-inflammatory cytokine release — which underpins its efficacy in gout flares, pericarditis, and FMF.

The TxGNN model's prediction for malaria is mechanistically grounded in one key observation: *Plasmodium falciparum* depends on tubulin-based spindle formation (PfTubulin) for intraerythrocytic schizogony. In vitro studies from the late 1980s and early 1990s demonstrated that compounds binding to cytoskeletal proteins — including tubulozoles and Colcemid (a structural colchicine analogue) — can disrupt *P. falciparum* intraerythrocytic development. The effects of Colcemid on parasite protein synthesis, as noted in one study, paralleled those of tubulozoles, suggesting that the colchicine-class binding mechanism may be at least partially active against the parasite.

However, there is a critical limitation: PfTubulin has significant amino acid sequence divergence from human α/β-tubulin. Whether Colchicine itself demonstrates selectivity for the parasite's tubulin — rather than the host's — has not been directly characterised. None of the available literature directly tests Colchicine against *P. falciparum* in a validated antimalarial assay with IC₅₀ data. This prediction is therefore an indirect mechanistic inference, not a direct experimental finding, and must be treated accordingly.

---

## Clinical Trial Evidence

Currently no clinical trials for Colchicine in Plasmodium falciparum malaria are registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [2670249](https://pubmed.ncbi.nlm.nih.gov/2670249/) | 1989 | In vitro | Cell Biology International Reports | Nine tubulin-binding compounds tested against *P. falciparum* in vitro; plasmodial tubulins appear structurally distinct from mammalian proteins; tubulozole-T showed promising antimalarial activity |
| [2655935](https://pubmed.ncbi.nlm.nih.gov/2655935/) | 1989 | In vitro | Cell Biology International Reports | Confirms that cytoskeletal protein-binding substances — including tubulin and actin inhibitors — can inhibit intraerythrocytic *P. falciparum* development in culture |
| [2221861](https://pubmed.ncbi.nlm.nih.gov/2221861/) | 1990 | In vitro | Antimicrobial Agents and Chemotherapy | Tubulozoles tested against *P. falciparum*; Colcemid (colchicine analogue) produced similar effects on parasite protein synthesis, suggesting a shared mechanism of action relevant to the colchicine class |
| [6362934](https://pubmed.ncbi.nlm.nih.gov/6362934/) | 1984 | Clinical/Serological | Clinical and Experimental Immunology | 82% of acute malaria patients showed anti-intermediate filament antibodies; supports the importance of cytoskeletal proteins in malaria pathophysiology and potential as therapeutic targets |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | Mechanistic | Molecular and Cellular Biology | pfmdr1 gene expression linked to reduced chloroquine accumulation in resistant parasites; mechanistic context on *P. falciparum* drug efflux relevant to small-molecule repurposing |
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | In vitro | PLoS ONE | Curcumin disrupts *P. falciparum* microtubule structure, confirming tubulin as a druggable target in the parasite; indirect mechanistic support for the colchicine binding site concept |

---

## Australia Market Information

No ARTG entries for Colchicine were identified in the current dataset. Colchicine is recorded as not currently marketed in Australia based on available regulatory data.

> **Note:** Clinicians should independently verify current ARTG registration status via the [TGA ARTG Public Summary](https://www.tga.gov.au/resources/artg), as real-world availability may differ from the dataset presented here.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for full safety information, including contraindications, drug–drug interactions, and special population warnings.

> Colchicine has a **narrow therapeutic index**. Toxicity — including gastrointestinal effects, myelosuppression, and neuromuscular toxicity — can occur at doses close to therapeutic levels, particularly in the context of renal impairment or concurrent use of CYP3A4/P-glycoprotein inhibitors. These considerations are especially relevant if use outside approved indications is contemplated.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for Colchicine in *Plasmodium falciparum* malaria consists entirely of indirect in vitro studies (1984–2013) using structurally related compounds (tubulozoles, Colcemid) rather than Colchicine itself. There are no clinical trials, no direct antimalarial efficacy data for Colchicine, and the critical question of PfTubulin selectivity over human tubulin remains unanswered — a significant safety concern given Colchicine's narrow therapeutic window and host toxicity profile.

**To proceed, the following is needed:**

- **Direct antimalarial in vitro testing:** Determine IC₅₀ of Colchicine against *P. falciparum* strains (including drug-resistant isolates) using standard SYBR Green or [³H]-hypoxanthine assays
- **Selectivity index assessment:** Calculate SI = mammalian CC₅₀ / parasite IC₅₀ to evaluate whether a therapeutic window exists
- **Structural bioinformatics:** Compare human α/β-tubulin versus PfTubulin colchicine-binding site residues to assess theoretical selectivity
- **Pharmacokinetic modelling:** Determine whether plasma concentrations achievable without host toxicity are sufficient to suppress parasitaemia
- **Full safety dataset retrieval:** Obtain Colchicine Product Information (PI) for contraindications, drug interactions, and special population warnings
- **MOA documentation:** Retrieve complete mechanism of action data from DrugBank (DB01394) and published pharmacology sources

---

> **Secondary finding — high priority:** The Rank 2 prediction, **Familial Mediterranean Fever (FMF)**, carries an evidence level of **L1** with 20 supporting publications — many of which explicitly describe Colchicine as the established gold-standard treatment. This is not a speculative prediction but a well-evidenced, guideline-recommended use. A dedicated evaluation report for the Colchicine–FMF indication is strongly recommended, with a preliminary decision of **Proceed with Guardrails**.

---

*This report is generated for research reference purposes only and does not constitute medical advice. All repurposing candidates require prospective clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

