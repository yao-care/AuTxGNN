---
layout: default
title: Calcium
parent: 僅模型預測 (L5)
nav_order: 117
evidence_level: L5
indication_count: 10
---

# Calcium
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

# Calcium: From Electrolyte Supplementation to Thrombotic Disease

## One-Sentence Summary

Calcium (DrugBank DB01373) is an essential mineral element widely used clinically as an electrolyte supplement and for bone metabolism support (e.g., hypocalcaemia, osteoporosis supportive care), though it has no formal ARTG registration in Australia under this DrugBank entry.
The TxGNN model predicts it may be relevant to **Thrombotic Disease** with a prediction score of **98.25%**,
however, no clinical trials directly test calcium supplementation as a treatment for thrombosis, and the underlying mechanistic rationale presents a **fundamental biological paradox** that warrants careful scrutiny before any further development is considered.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No ARTG-registered indication (not marketed in Australia under this DrugBank entry) |
| Predicted New Indication | Thrombotic Disease |
| TxGNN Prediction Score | 98.25% |
| Evidence Level | L4 (Mechanistic/Preclinical — no direct interventional trials) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

**Known biological role — calcium as a pro-coagulant cofactor:** Calcium ions (Ca²⁺) are designated "Factor IV" in the classical coagulation cascade. Ca²⁺ is an obligate cofactor for the activation of vitamin K-dependent clotting factors II (thrombin), VII, IX, and X, and simultaneously promotes platelet α- and δ-granule release during platelet activation. This central position in haemostasis is almost certainly why the TxGNN knowledge graph drew a high-confidence edge between calcium and thrombotic disease — the biological association is real and well established.

**The fundamental paradox — direction of intervention:** While the mechanistic link is genuine, the therapeutic direction is the critical problem. Calcium's role in the coagulation cascade is as a **promoter** of clot formation, not an inhibitor. Supplementing calcium would logically be expected to enhance coagulation and potentially worsen thrombotic disease, not treat it. This is consistent with the available literature: PMID 36453103 (Haematologica, 2023) demonstrated that plasma from patients with immune-mediated thrombotic thrombocytopenic purpura (iTTP) triggers calcium- and IgG-dependent endothelial cell activation — placing Ca²⁺ signalling within the **pathogenic mechanism** of thrombosis, not as a therapeutic target. Similarly, PMID 38880165 (Life Sciences, 2024) and PMID 37563135 (Nature Communications, 2023) both show that elevated intracellular Ca²⁺ promotes the pro-coagulant platelet phenotype.

**Why TxGNN predicted this link and why caution is needed:** Knowledge graph-based models capture co-occurrence and topological proximity between nodes — they cannot infer whether an intervention should augment or antagonise a pathway. The model correctly identified that calcium nodes cluster near thrombotic disease nodes in the biomedical knowledge graph, but it cannot distinguish between "calcium causes thrombosis" and "calcium cures thrombosis." Every identified clinical trial in this evidence pack tests **anticoagulant agents** (heparins, direct oral anticoagulants), statins, or complement inhibitors — not calcium supplementation. This prediction warrants a Hold pending a clearly articulated, biologically coherent therapeutic hypothesis.

---

## Clinical Trial Evidence

> **Important note:** None of the trials below directly test calcium supplementation as a therapeutic intervention for thrombotic disease. Trials involving "nadroparin calcium" are testing a low molecular weight heparin salt; the calcium moiety is pharmacologically inactive in that context.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00951574](https://clinicaltrials.gov/study/NCT00951574) | Phase 3 | Completed | 1,166 | Nadroparin calcium vs placebo for VTE prevention in cancer patients on chemotherapy — Phase 3 completed trial; tests heparin, not calcium supplementation |
| [NCT04319627](https://clinicaltrials.gov/study/NCT04319627) | Phase 3 | Recruiting | 2,700 | SAVER trial: rosuvastatin vs placebo for VTE reduction in patients with DVT/PE on anticoagulation — statin intervention, no calcium arm |
| [NCT06513481](https://clinicaltrials.gov/study/NCT06513481) | N/A | Not Yet Recruiting | 914 | Timing of pharmacological VTE prophylaxis in Chinese colorectal cancer surgery — observational cohort, no direct calcium intervention |
| [NCT04833764](https://clinicaltrials.gov/study/NCT04833764) | Phase 1/2 | Unknown | 30 | DVT mechanisms and vein wall fibrosis; adjunctive rosuvastatin with Factor Xa inhibitors to prevent post-thrombotic syndrome |
| [NCT00421538](https://clinicaltrials.gov/study/NCT00421538) | Phase 3 | Completed | 260 | CACTUS-PTS: Nadroparin (LMWH) vs placebo for isolated distal DVT — anticoagulant trial, calcium salt is not the active moiety |
| [NCT07303816](https://clinicaltrials.gov/study/NCT07303816) | Phase 4 | Not Yet Recruiting | 4,000 | STAT-CAT: Rosuvastatin 20 mg vs placebo for 12 months to prevent cancer-associated VTE — large statin prevention trial, no calcium arm |
| [NCT02679664](https://clinicaltrials.gov/study/NCT02679664) | Phase 2 | Unknown | 312 | SAVER pilot: rosuvastatin feasibility for recurrent VTE and post-thrombotic syndrome prevention |
| [NCT06259149](https://clinicaltrials.gov/study/NCT06259149) | N/A | Recruiting | 914 | VTE prevention timing after colorectal cancer surgery — observational, single-centre Chinese cohort |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36453103](https://pubmed.ncbi.nlm.nih.gov/36453103/) | 2023 | Mechanistic / In Vitro | Haematologica | iTTP patient plasma induces calcium- and IgG-dependent endothelial cell activation correlated with disease severity; positions Ca²⁺ as part of the thrombotic pathomechanism, not a therapy target |
| [38880165](https://pubmed.ncbi.nlm.nih.gov/38880165/) | 2024 | Review | Life Sciences | Calcium flux and mitochondrial metabolism in platelet activation; elevated intracellular Ca²⁺ drives the pro-coagulant platelet phenotype and promotes thrombosis |
| [37563135](https://pubmed.ncbi.nlm.nih.gov/37563135/) | 2023 | Basic Science | Nature Communications | MTH1 deficiency impairs platelet calcium mobilisation and reduces arterial/venous thrombosis in vivo, confirming Ca²⁺ as a necessary pro-thrombotic signal |
| [26972052](https://pubmed.ncbi.nlm.nih.gov/26972052/) | 2016 | Translational Study | Cell | Gut microbial metabolite TMAO enhances platelet hyperreactivity and thrombosis potential; calcium-dependent platelet activation is part of the TMAO-driven mechanism |
| [6099583](https://pubmed.ncbi.nlm.nih.gov/6099583/) | 1984 | Classic Review | Progress in Hemostasis and Thrombosis | Foundational description of the Protein C anticoagulant pathway; Ca²⁺-dependent thrombin activation at the endothelial surface is central to coagulation regulation — establishes Ca²⁺ as a pro-coagulant cofactor |
| [22283597](https://pubmed.ncbi.nlm.nih.gov/22283597/) | 2012 | Review | American Journal of Cardiovascular Drugs | Review of calcium intake and cardiovascular disease risk; experimental and epidemiological data suggest excessive calcium supplementation may influence thrombotic markers — a signal in the opposite direction to therapeutic benefit |
| [39796525](https://pubmed.ncbi.nlm.nih.gov/39796525/) | 2024 | Review | Nutrients | Vitamin D deficiency and thrombotic disease risk; discusses vitamin D–calcium–phosphate axis in modulating thrombosis risk; indirect relevance only |

---

## Australia Market Information

Calcium (DrugBank DB01373) has **no ARTG registrations** in Australia under this compound entry. The drug is currently **not marketed** as a prescription pharmaceutical under this designation.

Calcium-containing products (calcium carbonate, calcium citrate, calcium gluconate) are available in Australia as:
- **Listed medicines** (ARTG Category 2) for dietary supplementation — available over the counter
- **Unregistered ingredient** in compounding pharmacy preparations

No formal ARTG prescription product entries were identified for this DrugBank record. There are accordingly no TGA-approved Product Information (PI) documents to reference for this specific entry.

---

## Safety Considerations

No TGA-approved Product Information (PI) is linked to this DrugBank entry in Australia. The following general considerations apply based on the known pharmacology of calcium:

- **Hypercalcaemia risk:** Excessive calcium supplementation can cause hypercalcaemia (nausea, constipation, renal stones, cardiac arrhythmia)
- **Cardiovascular signal:** Epidemiological reviews (PMID 22283597) have raised concerns that high-dose supplemental calcium may increase cardiovascular event risk, potentially including thrombotic events — directly relevant to the predicted indication and supporting a Hold decision
- **Drug interactions:** No DDI data was retrieved for this query

Please refer to TGA-approved Product Information for individual calcium salt products (e.g., calcium carbonate, calcium gluconate) currently listed on the ARTG for applicable safety guidance.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model has captured a real and well-established biological association between calcium and thrombotic disease — Ca²⁺ is genuinely central to the coagulation cascade as Factor IV. However, this association is *pathomechanistic* rather than *therapeutic*: calcium promotes clot formation rather than preventing it, and there is no established therapeutic hypothesis by which calcium supplementation would treat thrombotic disease. All clinically relevant trials in this evidence pack test anticoagulant agents. Epidemiological data even suggest that supplemental calcium may increase cardiovascular and thrombotic risk, the opposite of the desired effect.

**To proceed, the following would need to be established:**

- A biologically coherent and paradox-resolving therapeutic hypothesis (e.g., is the intended intervention calcium *chelation*, calcium *channel modulation*, or a specific downstream signalling target rather than elemental calcium supplementation?)
- Differentiation of whether TxGNN is predicting calcium's role as a drug target versus a treatment agent
- Preclinical studies specifically examining whether calcium supplementation — at physiological or pharmacological doses — reduces thrombotic outcomes in validated animal models
- Mechanistic clarification from DrugBank and literature on whether any calcium formulation or analogue has demonstrated anti-thrombotic rather than pro-thrombotic activity
- TGA regulatory pathway scoping if a coherent repurposing hypothesis is established
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

