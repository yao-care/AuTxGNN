---
layout: default
title: Theophylline
parent: Model Prediction Only (L5)
nav_order: 718
evidence_level: L5
indication_count: 10
---

# Theophylline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Theophylline: From Asthma to Thrombotic Disease

## One-Sentence Summary

Theophylline is a long-established bronchodilator, used for asthma, bronchitis, emphysema and related chronic airway diseases.
The TxGNN model predicts it may be useful for **thrombotic disease** (score 99.6%), but the data compiled for this report contain **no clinical trials** and **no publications that test theophylline in thrombosis**. The prediction rests on the computational score and a plausible but unproven platelet mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma, bronchitis, emphysema and related lung disease (from the TxGNN knowledge graph; the ARTG indication text is not available in the data) |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 (model prediction only) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Theophylline is a non-selective phosphodiesterase (PDE) inhibitor and an adenosine receptor antagonist. Its efficacy in airway disease is well established.

In platelets, PDE inhibition can raise cyclic AMP (cAMP), which generally reduces platelet aggregation. That is the plausible link to thrombosis. The idea is not proven for theophylline. Adenosine also lowers platelet reactivity through cAMP, so theophylline's adenosine antagonism could work against any antiplatelet effect. The net effect in people is unknown.

The original indication (airway disease) and thrombotic disease are very different conditions. The high score therefore reflects network proximity in the knowledge graph rather than clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the retrieved papers tests theophylline for thrombosis. Most are indirect, off-target or methodological. There are no randomised trials. The most relevant items are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Crit Rev Biochem | Describes thromboxane A2 and prostacyclin balance in platelets and vessels. Prostacyclin raises platelet cAMP and inhibits aggregation, which is the background for the PDE-inhibition idea. |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | Laboratory study | Gen Pharmacol | Milrinone (a different PDE inhibitor) reduced human platelet aggregation and interacted with adenosine, which acts through cAMP. This supports the mechanism class, not theophylline itself. |
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Pharmacokinetic review | Clin Pharmacokinet | Covers ticlopidine, a different antiplatelet drug. Not about theophylline. |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Laboratory method | Br J Haematol | Radioimmunoassay for platelet factor 4. Theophylline is used only as a sample additive to prevent platelet activation in vitro. |
| [4776567](https://pubmed.ncbi.nlm.nih.gov/4776567/) | 1973 | Clinical report | Minerva Cardioangiol | Theophylline nicotinate derivative in chronic obliterating peripheral arteriopathy. No abstract is available and it is a different compound. |
| [5136470](https://pubmed.ncbi.nlm.nih.gov/5136470/) | 1971 | Clinical report | Cardiologia Pratica | Cardiocirculatory effects of a theophylline nicotinic ester in cerebral and peripheral angiopathies. No abstract is available and it is a different compound. |
| [5605983](https://pubmed.ncbi.nlm.nih.gov/5605983/) | 1967 | Clinical report | Ann Ottalmol Clin Ocul | Electroretinographic assessment of theophylline nicotinate in retinal vascular disease. No abstract is available. |
| [6241135](https://pubmed.ncbi.nlm.nih.gov/6241135/) | 1984 | Laboratory study | Cor Vasa | Theophylline was used as a tool to define T-cell subsets in patients with myocardial infarction, peripheral arterial disease and thrombophlebitis. This is not a treatment study. |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Analytical method | Anal Chim Acta | Aptasensor for detecting theophylline. It confirms the drug's narrow safe concentration range but is unrelated to thrombosis. |
| [14144216](https://pubmed.ncbi.nlm.nih.gov/14144216/) | 1964 | Clinical report | Orv Hetil | Use of a xanthine-type preparation in cerebral circulatory disease. No abstract is available and the evidence is very old. |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2614N | Nuelin | Oral solution 133.3 mg per 25 mL, 500 mL | Not provided in the data compiled for this report |

Only an oral formulation is listed. No injectable or other route is recorded.

---

## Safety Considerations

Product Information (PI) warnings and contraindications are not available in the data compiled for this report. Please refer to the TGA-approved PI.

- **Knowledge-graph contraindication signals** (from drug–disease links, not label text): hypertension, liver failure and liver disease, epilepsy, anxiety and other mental disorders, porphyria, kidney disease, thyroid disease (hypothyroidism), peptic ulcer disease, open-angle glaucoma, diabetes and diabetic ketoacidosis, benign prostatic hyperplasia, gallbladder disease, thrombocytopenia, neutropenia and agranulocytosis. These signals need verification against the PI.
- **Drug interactions:** 100 interactions were identified; 20 are shown in the data.
  - **Major:** bupropion.
  - **Moderate:** H2 blockers (famotidine, ranitidine, cimetidine), proton pump inhibitors (omeprazole, rabeprazole), clarithromycin, tetracyclines (doxycycline, tetracycline, minocycline), corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), activated charcoal, picosulfuric acid and polyethylene glycol bowel preparations.
  - **Minor:** ephedrine.
- **Other signals:** A pharmacogenetic study (NCT03015090) examined CYP1A2 variation and theophylline metabolism. Theophylline has a narrow therapeutic window, so any new use would need concentration monitoring.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score and an unproven platelet cAMP mechanism. There are no trials, and no retrieved paper tests theophylline in thrombosis. Theophylline's adenosine antagonism may also oppose an antiplatelet effect, and established antithrombotic drugs are available.

**To proceed, the following is needed:**
- Mechanistic data: in vitro platelet aggregation and thrombosis models with theophylline at clinically achievable concentrations.
- A structured literature review for clinical thrombosis outcomes, including any bleeding or thrombotic events in existing theophylline users.
- Mechanism-of-action data and TGA PI safety information for Nuelin.
- A safety plan covering narrow therapeutic index, CYP1A2 variability and interactions if a clinical study is ever considered.

**Other predictions:** For other predicted indications in the same dataset, such as allergic rhinitis (a small Phase 2 trial, NCT01132781, and a nasal challenge study, PMID 9648963) and tracheal disease, more human evidence exists than for thrombotic disease. They may warrant separate review. "Obstructive lung disease" is essentially the original indication and is not true repurposing.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

