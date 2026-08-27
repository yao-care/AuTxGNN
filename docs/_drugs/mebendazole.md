---
layout: default
title: Mebendazole
parent: 僅模型預測 (L5)
nav_order: 416
evidence_level: L5
indication_count: 10
---

# Mebendazole
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

# Mebendazole: From Intestinal Helminth Infections to Alveolar Echinococcosis

## One-Sentence Summary

> Mebendazole (DrugBank DB00643) is a benzimidazole anthelmintic, not currently marketed in Australia.
> Among 10 TxGNN-predicted indications reviewed, the model's highest-scoring hit (acne) has no credible supporting evidence and is flagged **Hold** in the evidence review itself.
> The best-supported candidate is **Alveolar Echinococcosis**, backed by **1 completed clinical trial** and **20 publications**, reflecting mebendazole's already-established (if second-line) role in treating this disease.

*Note on candidate selection: this Evidence Pack scored 10 candidate indications. Rather than defaulting to the raw top-ranked prediction (acne, 99.2% score — explicitly annotated in the pack as having "no plausible mechanistic link"), this report focuses on the indication with the strongest verifiable evidence: Alveolar Echinococcosis (rank 5). See "Screened-out candidates" note below.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (data gap); drug class is benzimidazole anthelmintic per mechanistic rationale |
| Predicted New Indication | Alveolar Echinococcosis (*Echinococcus multilocularis* infection) |
| TxGNN Prediction Score | 94.20% (KG rank 44,695 of all drug–disease pairs) |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data was not returned for this query (data gap, DG002). Based on the mechanistic rationale captured in this Evidence Pack, mebendazole is a benzimidazole-class anthelmintic that binds parasitic β-tubulin, inhibiting microtubule polymerisation and blocking glucose uptake in helminths — ultimately causing parasite death.

This mechanism acts directly on the larval (metacestode) stage of *Echinococcus multilocularis*, the causative organism of alveolar echinococcosis. Mebendazole, alongside albendazole, is already used per WHO-IWGE guidance as a chemotherapeutic option for this disease (albendazole is first-line; mebendazole is the alternative for patients who cannot tolerate it). This means the prediction is less a novel repurposing hypothesis and more a **confirmation of existing, published clinical practice** — which is reflected in the evidence pack's own note that this "is not a novel repurposing hypothesis, but confirmation of existing clinical practice."

A related candidate in the same pack, Cystic Echinococcosis (*Echinococcus granulosus*, rank 3, also L3/Proceed with Guardrails), reinforces this biological plausibility: mebendazole was historically the first benzimidazole used for hydatid disease, with a 70-patient cohort study (Teggi et al., 1989) reporting cyst regression in 64.3% of cases.

**Screened-out candidates:** The remaining 8 predictions in this pack (acne, diffuse cutaneous leishmaniasis, hordeolum, inhalational/toxin-mediated botulism, impetigo, Sorsby's fundus dystrophy, demodicidosis) all returned zero clinical trials and zero-to-irrelevant literature, and are explicitly annotated in the pack as lacking a plausible mechanistic link. These should be treated as model noise, not credible repurposing signals.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02876146](https://clinicaltrials.gov/study/NCT02876146) | NA (observational) | Completed | 50 | Prospective study (EchinoVISTA) of parasite viability and follow-up biomarkers in hepatic alveolar echinococcosis patients treated with **albendazole**. Not a direct mebendazole efficacy trial, but confirms benzimidazole-class treatment is standard clinical background therapy for this disease. |

No completed randomised controlled trial of mebendazole specifically (vs. comparator) in alveolar echinococcosis was identified in this pack.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10980173](https://pubmed.ncbi.nlm.nih.gov/10980173/) | 2000 | Comparative/Observational | J Antimicrob Chemother | 35 patients treated long-term with mebendazole or albendazole; outcomes compared across regimens — direct clinical evidence for mebendazole use. |
| [25526545](https://pubmed.ncbi.nlm.nih.gov/25526545/) | 2014 | Review | Parasite | Reviews albendazole and mebendazole as the two established chemotherapeutic options for alveolar echinococcosis and surveys emerging alternatives. |
| [19254162](https://pubmed.ncbi.nlm.nih.gov/19254162/) | 2009 | Review | Expert Rev Anti Infect Ther | Consensus review on benzimidazole (albendazole/mebendazole) use in cystic and alveolar echinococcosis. |
| [9875648](https://pubmed.ncbi.nlm.nih.gov/9875648/) | 1998 | Case Report | J Hepatology | 13-year continuous mebendazole therapy (~45–48 mg/kg/day) in a non-resectable hepatic AE patient; discusses evidence for parasitocidal (not just parasitostatic) effect with long-term dosing. |
| [7197224](https://pubmed.ncbi.nlm.nih.gov/7197224/) | 1981 | Pharmacology Study | Eur J Clin Pharmacol | Compares plasma mebendazole concentrations in animal models vs. humans; establishes that drug levels above 0.25 µmol/L correlate with reduced parasite mass. |
| [40093668](https://pubmed.ncbi.nlm.nih.gov/40093668/) | 2025 | Review | World J Gastroenterol | Current management overview of liver echinococcosis, including chemotherapy and surgical approaches. |
| [39606163](https://pubmed.ncbi.nlm.nih.gov/39606163/) | 2024 | Review | World J Hepatol | Current status of drug therapy for alveolar echinococcosis. |
| [39311470](https://pubmed.ncbi.nlm.nih.gov/39311470/) | 2024 | Review | Parasite | Reviews benzimidazole chemotherapy limitations (parasitostatic effect, hepatotoxicity) and unmet need for curative agents. |
| [34808118](https://pubmed.ncbi.nlm.nih.gov/34808118/) | 2022 | Review | Acta Tropica | Status and prospects of novel treatment options for alveolar and cystic echinococcosis beyond albendazole/mebendazole. |
| [29677189](https://pubmed.ncbi.nlm.nih.gov/29677189/) | 2018 | Review | PLoS Negl Trop Dis | 40+ years of benzimidazole chemotherapy against echinococcosis; reviews pharmacological targets and progress. |

---

## Australia Market Information

Mebendazole is **not currently marketed in Australia** — no ARTG entries were found (0 licenses, data cutoff 2026-08-13). Any clinical use would require TGA Special Access Scheme (SAS) or Authorised Prescriber pathway access to an overseas-registered product.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Full PI warning and contraindication data could not be retrieved in this query (severity: Blocking — this must be resolved before a formal safety assessment can proceed).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Multiple reviews (including two Tier-1 sources) plus mebendazole-specific case and pharmacokinetic data support its use — alongside albendazole — as an accepted, if second-line, treatment for alveolar echinococcosis. This is confirmatory of existing practice rather than a novel hypothesis, but the drug is unregistered in Australia and lacks direct mebendazole-arm RCT data for this indication.
- The TxGNN model's raw top-ranked prediction (acne) has no clinical or mechanistic support and should not be pursued.

**To proceed, the following is needed:**
- TGA-approved PI (warnings, contraindications, DDI) — currently a blocking data gap
- Confirmed DrugBank mechanism-of-action record
- Since mebendazole holds no ARTG entry, a TGA Special Access Scheme / Authorised Prescriber pathway assessment for compassionate/named-patient use
- Consider Cystic Echinococcosis (*Echinococcus granulosus*, rank 3) as a related secondary indication given similar evidence strength (L3, 7 publications including a 70-patient cohort study)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

