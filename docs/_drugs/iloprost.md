---
layout: default
title: Iloprost
parent: Model Prediction Only (L5)
nav_order: 368
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
monitor_inn: "Iloprost"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "pulmonary arteriovenous malformation (disease)", "diffuse alopecia areata"]
description: "Iloprost: predicted new indication Hypotrichosis simplex of the scalp (evidence level L5). Approved use: Not recorded in the local data"
---

# Iloprost
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Iloprost: Hypotrichosis simplex of the scalp
{: .text-alpha }

## One-Sentence Summary

Iloprost is a stable prostacyclin analogue, originally used to treat pulmonary arterial hypertension (PAH). The TxGNN model's top-ranked prediction is **hypotrichosis simplex of the scalp**, but this has no supporting studies. The best-supported prediction is **PAH associated with congenital heart disease**, backed by **19 publications** (no registered clinical trials), most of them observational studies, reviews and case reports.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 0.9945 |
| Evidence Level | L5 (hypotrichosis simplex of the scalp); L3 (PAH-CHD) |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold (top-ranked prediction); Proceed with Guardrails as a research question for PAH-CHD |

**Note on the top-ranked prediction:** No clinical trials or literature support hypotrichosis simplex of the scalp. The direction of effect is also uncertain, because prostaglandin F2α analogues promote hair growth whereas PGD2 inhibits it. The report therefore focuses on the best-supported prediction, PAH-CHD, and summarises the other candidates below.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, iloprost is a stable prostacyclin (IP receptor) agonist. It causes pulmonary vasodilation, inhibits platelet aggregation and limits smooth muscle proliferation.


**Summary of other predictions:**

| Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|
| Pulmonary arteriovenous malformation | 0.9931 | L5 | Not mechanistically sensible, because vasodilation may worsen shunting and hypoxaemia |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Selected publications for PAH associated with congenital heart disease:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31371115](https://pubmed.ncbi.nlm.nih.gov/31371115/) | 2020 | Placebo-controlled, double-blind randomised cross-over pilot study | Int J Cardiol | Nebulised iloprost in Eisenmenger syndrome, addressing limited safety and efficacy data in this group |
| [29426959](https://pubmed.ncbi.nlm.nih.gov/29426959/) | 2018 | Cohort | Pediatr Cardiol | Safety and acute haemodynamic effects of inhaled iloprost in children with PAH-CHD |
| [28608969](https://pubmed.ncbi.nlm.nih.gov/28608969/) | 2017 | Cohort | Clin Exp Pharmacol Physiol | Effect of iloprost on endothelial-dysfunction biomarkers in CHD-PAH |
| [27492657](https://pubmed.ncbi.nlm.nih.gov/27492657/) | 2017 | Cohort | J Cardiol | Effect of long-term inhaled iloprost on right ventricular function in Eisenmenger syndrome |
| [24729548](https://pubmed.ncbi.nlm.nih.gov/24729548/) | 2015 | Cohort | Pediatr Pulmonol | Long-term effects of inhaled iloprost in children with pulmonary hypertension |
| [36010107](https://pubmed.ncbi.nlm.nih.gov/36010107/) | 2022 | Case series | Children (Basel) | Add-on sildenafil, bosentan and iloprost in 5 Eisenmenger syndrome patients followed 2010–2019 |
| [19436672](https://pubmed.ncbi.nlm.nih.gov/19436672/) | 2009 | Review | Vasc Health Risk Manag | Review of inhaled iloprost for paediatric pulmonary hypertension |
| [22621693](https://pubmed.ncbi.nlm.nih.gov/22621693/) | 2012 | Review | Drugs | Treatment of PAH in connective tissue disease, including congenital heart disease as a related group |

For PAH associated with connective tissue disease, the more relevant publications include [27651181](https://pubmed.ncbi.nlm.nih.gov/27651181/) (2017, Respirology, cohort: long-term outcomes of domiciliary intravenous iloprost in idiopathic and CTD-associated PAH) and [25261325](https://pubmed.ncbi.nlm.nih.gov/25261325/) (2015, Eur Respir J, preclinical: iloprost reversed established right ventricular fibrosis in rats).

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 5751Q | Ventavis | Solution for inhalation 20 micrograms (as trometamol) in 2 mL | Not recorded in the data compiled for this report |

## Safety Considerations

- **Contraindication-related conditions (not label text):** liver failure, chronic obstructive pulmonary disease (including severe early-onset), hypotensive disorders, pulmonary oedema and bronchial disease.
- **Drug Interactions:** 100 interactions were identified. Those graded Moderate include epinephrine, acetylsalicylic acid (aspirin), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin), inhaled human insulin, mannitol, ephedrine, fenfluramine, dexfenfluramine, glycerin, papaverine and sibutramine. Interactions with calcitriol, pantoprazole, morphine, metformin and omeprazole have an unknown severity grade.

Please refer to the TGA-approved Product Information (PI) for the full warnings and contraindications, as label-based safety data were not available.

## Conclusion and Next Steps

**Decision: Hold for the top-ranked prediction (hypotrichosis simplex of the scalp); Proceed with Guardrails as a research question for PAH associated with congenital heart disease**

**Rationale:**
- The top-ranked hair-related predictions have no trials or literature and an uncertain direction of effect, so they should not be progressed.
- PAH-CHD and CTD-PAH are mechanistically coherent extensions of the approved indication, supported by observational data (L3). There is no phase 3 randomised evidence, so they remain research questions rather than ready-to-adopt indications.

**To proceed, the following is needed:**
- Confirmation of the approved indication wording and PI-based warnings and contraindications from the TGA record (the ARTG indication text is blank in the compiled data)
- Detailed mechanism of action data (for example from DrugBank)
- Review of whether the current Australian PAH indication already covers PAH-CHD, to determine whether this is a true new indication
- Controlled trial data for iloprost in PAH-CHD and Eisenmenger syndrome
- A safety plan accounting for the contraindication-related conditions (hypotension, pulmonary oedema, COPD, liver failure) and for the interactions listed above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

