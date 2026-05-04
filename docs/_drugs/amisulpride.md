---
layout: default
title: Amisulpride
parent: 僅模型預測 (L5)
nav_order: 41
evidence_level: L5
indication_count: 10
---

# Amisulpride
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

# Amisulpride: From Unregistered Drug to Schizophrenia Treatment in Australia

## One-Sentence Summary

Amisulpride is an atypical antipsychotic widely approved in Europe, the United Kingdom, and other international markets for the treatment of schizophrenia and related psychotic disorders, but is currently not registered with the Therapeutic Goods Administration (TGA) in Australia.
The TxGNN model predicts it may be effective for **Schizophrenia** with a confidence score of **96.05%**,
supported by **50 clinical trials** and **20 publications** — earning the highest evidence rating of **L1**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not currently TGA-registered in Australia; internationally approved for schizophrenia and related psychotic disorders |
| Predicted New Indication | Schizophrenia |
| TxGNN Prediction Score | 96.05% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed (not TGA-registered) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Amisulpride is a selective dopamine receptor antagonist of the substituted benzamide class. Although formal mechanism of action (MOA) data from DrugBank was not available for this report, the extensive published literature provides clear and well-validated mechanistic insight. Amisulpride selectively blocks dopamine D2 and D3 receptors in a dose-dependent, region-specific manner: at low doses (50–300 mg/day), it preferentially blocks presynaptic autoreceptors in the frontal cortex, enhancing dopaminergic transmission and thereby improving the negative symptoms of schizophrenia (anhedonia, flat affect, and social withdrawal). At higher doses (400–800 mg/day), it blocks postsynaptic D2/D3 receptors in mesolimbic areas, reducing dopaminergic hyperactivity and alleviating positive symptoms such as hallucinations and delusions. Additional antagonism at 5-HT7 receptors may further contribute to cognitive improvement.

The dopamine hypothesis of schizophrenia posits that mesolimbic dopaminergic overactivity underlies positive symptoms, while hypodopaminergic activity in the mesocortical pathway drives negative and cognitive symptoms. Amisulpride's unique dose-dependent, dual-region mechanism directly targets both symptom clusters simultaneously — a pharmacological profile that is mechanistically well-matched to the full symptom spectrum of schizophrenia. This alignment is reflected in the TxGNN model's high prediction confidence of 96.05%.

Although Amisulpride is not currently registered in Australia, it has been approved for decades in France (its country of origin), the UK, Germany, and numerous other countries under brand names including Solian. Multiple landmark clinical trials — including the COMBINE study (*Lancet Psychiatry*, 2022), BeSt InTro (*Lancet Psychiatry*, 2020), and OPTiMiSE (*Lancet Psychiatry*, 2018) — have rigorously established its efficacy and tolerability in schizophrenia. It is consistently included in large-scale network meta-analyses as a first-line antipsychotic option, and is specifically recommended for patients with prominent negative symptoms.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01105481](https://clinicaltrials.gov/study/NCT01105481) | Phase 4 | Completed | 273 | 14-week double-blind RCT: Amisulpride augmentation vs. placebo for clozapine-resistant schizophrenia — primary evidence for treatment-resistant use |
| [NCT01246232](https://clinicaltrials.gov/study/NCT01246232) | Phase 4 | Completed | 69 | Amisulpride augmentation in clozapine-unresponsive schizophrenia — confirms augmentation strategy for the most treatment-resistant patients |
| [NCT03510325](https://clinicaltrials.gov/study/NCT03510325) | Phase 3 | Completed | 762 | Sequential multiple-assignment RCT (SMART) comparing antipsychotics in first-episode schizophrenia in real-world settings; includes pharmacoeconomic analysis |
| [NCT04528095](https://clinicaltrials.gov/study/NCT04528095) | Phase 3 | Unknown | 162 | SMART design for treatment-resistant schizophrenia and clozapine-resistant cases; Amisulpride as a comparison arm |
| [NCT01609153](https://clinicaltrials.gov/study/NCT01609153) | Phase 4 | Completed | 328 | COMBINE trial: double-blind RCT of olanzapine + amisulpride combination vs. each monotherapy in acutely ill schizophrenia |
| [NCT01248195](https://clinicaltrials.gov/study/NCT01248195) | Phase 4 | Completed | 479 | OPTiMiSE European multicentre trial: optimising current treatments and exploring novel therapeutic options for schizophrenia |
| [NCT01446328](https://clinicaltrials.gov/study/NCT01446328) | Phase 4 | Completed | 151 | Bergen Psychosis Project 2 (BeSt InTro): pragmatic head-to-head comparison of aripiprazole, amisulpride, and olanzapine over 12 months with minimal exclusion criteria |
| [NCT03451734](https://clinicaltrials.gov/study/NCT03451734) | N/A | Completed | 2,000 | Large Chinese multicentre study across 19 cities: first-episode schizophrenia randomised to 6 antipsychotic groups including amisulpride; 8-week treatment response |
| [NCT01795183](https://clinicaltrials.gov/study/NCT01795183) | Phase 4 | Completed | 316 | Prospective open-label multicentre study evaluating effectiveness and safety of amisulpride specifically in Chinese patients with schizophrenia |
| [NCT00419653](https://clinicaltrials.gov/study/NCT00419653) | Phase 4 | Terminated | 19 | fMRI and DTI study of regional brain activation in schizophrenia with amisulpride, olanzapine, or haloperidol — provides neuroimaging mechanistic evidence |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [23810019](https://pubmed.ncbi.nlm.nih.gov/23810019/) | 2013 | Network Meta-Analysis | *Lancet* | Comprehensive comparison of 15 antipsychotics in schizophrenia; amisulpride ranked among the highest for overall efficacy and all-cause discontinuation |
| [35276079](https://pubmed.ncbi.nlm.nih.gov/35276079/) | 2022 | RCT | *Lancet Psychiatry* | COMBINE trial: amisulpride + olanzapine combination was significantly more effective than either monotherapy in acutely ill schizophrenia patients |
| [39002529](https://pubmed.ncbi.nlm.nih.gov/39002529/) | 2024 | RCT | *Schizophrenia Research* | BeSt InTro substudy: remission rates across amisulpride, aripiprazole, and olanzapine in schizophrenia spectrum disorders — identifies predictors of remission |
| [36253804](https://pubmed.ncbi.nlm.nih.gov/36253804/) | 2022 | RCT | *Military Medical Research* | 12-week double-blind placebo-controlled RCT: amisulpride augmentation significantly improved cognitive performance and psychopathology in clozapine-resistant treatment-refractory schizophrenia |
| [33069317](https://pubmed.ncbi.nlm.nih.gov/33069317/) | 2020 | RCT | *Lancet Psychiatry* | BeSt InTro pragmatic trial: first head-to-head comparison of amisulpride, aripiprazole, and olanzapine in a clinically representative schizophrenia-spectrum sample |
| [30115598](https://pubmed.ncbi.nlm.nih.gov/30115598/) | 2018 | RCT | *Lancet Psychiatry* | OPTiMiSE three-phase switching study: amisulpride and olanzapine compared in first-episode schizophrenia, with non-responders subsequently receiving clozapine |
| [29368205](https://pubmed.ncbi.nlm.nih.gov/29368205/) | 2018 | Systematic Review / Meta-Analysis | *Eur Arch Psychiatry Clin Neurosci* | Antipsychotics for predominant negative symptoms; amisulpride identified as one of the most efficacious agents for negative symptom reduction in schizophrenia |
| [30185173](https://pubmed.ncbi.nlm.nih.gov/30185173/) | 2018 | Meta-Analysis | *BMC Psychiatry* | Amisulpride vs. olanzapine in China: comparable clinical efficacy with more favourable metabolic profile; includes cost-minimisation analysis |
| [12418608](https://pubmed.ncbi.nlm.nih.gov/12418608/) | 2002 | Mechanistic Review | *Curr Med Res Opin* | Amisulpride mechanism: selective presynaptic D2/D3 blockade at low doses enhances dopaminergic transmission; postsynaptic blockade at high doses reduces positive symptoms; clinical outcomes summary |
| [36368055](https://pubmed.ncbi.nlm.nih.gov/36368055/) | 2022 | Narrative Review | *Expert Opin Pharmacother* | Novel antipsychotics and strategies for treatment-resistant schizophrenia; amisulpride discussed as a validated augmentation option for clozapine-resistant cases |

---

## Australia Market Information

Amisulpride is **not currently registered on the Australian Register of Therapeutic Goods (ARTG)**. There are no approved ARTG product entries for amisulpride in Australia.

This contrasts with its regulatory status in multiple international jurisdictions: amisulpride has been approved by the European Medicines Agency (EMA), the UK Medicines and Healthcare products Regulatory Agency (MHRA), and numerous other national regulators for the treatment of schizophrenia, under the brand name Solian and equivalents. Its long track record of international use (over 20 years) and established safety and efficacy data may support an expedited TGA registration pathway.

---

## Safety Considerations

As Amisulpride is not currently registered with the TGA in Australia, no Australian Product Information (PI) is available. Please refer to the European Medicines Agency (EMA) Summary of Product Characteristics (SmPC) or the UK MHRA-approved Product Information for comprehensive safety, warning, and contraindication data.

Based on safety signals consistently reported across clinical trials and literature included in this evidence pack, the following areas warrant particular attention in any Australian clinical implementation plan:

- **Hyperprolactinemia**: Amisulpride is a potent prolactin-elevating antipsychotic. Clinically significant hyperprolactinemia is frequently reported and may require monitoring of prolactin levels at baseline and during treatment (referenced in NCT06040944, NCT04002258, PMID 31552612).
- **QTc Prolongation**: Amisulpride carries a documented QTc-prolonging risk. Baseline and ongoing ECG monitoring is recommended, particularly in patients with pre-existing cardiac conditions or those on concomitant QTc-prolonging medications (NCT04446234).
- **Drug Interactions**: No DDI data was found in the current evidence pack. A formal DDI review should be completed prior to clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Amisulpride has Level 1 evidence supporting its use in schizophrenia, backed by multiple completed Phase 3 and Phase 4 RCTs published in top-tier journals including *The Lancet* and *Lancet Psychiatry*, comprehensive network meta-analyses, and over two decades of international clinical use. The TxGNN prediction confidence of 96.05% is strongly validated by this evidence base, and the mechanistic rationale is well-established. The principal barrier to Australian uptake is the absence of TGA registration, not a lack of clinical evidence.

**To proceed, the following is needed:**
- **TGA registration pathway**: Initiate an ARTG application for amisulpride; given existing EMA and international approvals, an abridged or streamlined registration pathway (via Section 23 or equivalent) may be applicable
- **Mechanism of action data**: Obtain formal MOA documentation from DrugBank (DB06288) to complete pharmacological profile for the regulatory submission
- **Australian Product Information (PI)**: Localise an approved PI document based on the current EMA SmPC for TGA submission and Australian prescriber use
- **Safety monitoring plan**: Develop Australian-specific clinical guidelines for hyperprolactinemia screening (prolactin levels) and QTc monitoring during amisulpride treatment
- **DDI profile completion**: Conduct a full drug interaction review; DDI data was not available in the current evidence pack and constitutes a data gap for prescriber guidance
- **Health economic evaluation**: Commission an Australian-specific cost-effectiveness analysis to support PBS (Pharmaceutical Benefits Scheme) listing consideration

---

*This report is intended for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before implementation. All content should be read in conjunction with current Australian clinical guidelines and TGA-approved prescribing information where available.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

