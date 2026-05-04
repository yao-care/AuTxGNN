---
layout: default
title: Asenapine
parent: 僅模型預測 (L5)
nav_order: 58
evidence_level: L5
indication_count: 10
---

# Asenapine
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

# Asenapine: From Schizophrenia and Bipolar Mania to Major Affective Disorder

## One-Sentence Summary

Asenapine is a second-generation (atypical) antipsychotic approved overseas for the acute treatment of schizophrenia and manic/mixed episodes of Bipolar I Disorder, but not currently registered on the Australian ARTG.
The TxGNN model predicts it may be effective for **Major Affective Disorder** (specifically Bipolar I — manic and mixed episodes),
with **3 completed Phase 3 clinical trials** and **19 publications** (including a meta-analysis of RCTs) supporting this direction.

> **Note on TxGNN Prediction Rankings:** TxGNN generated 10 predictions for Asenapine. The 9 highest-scored predictions (Ranks 1–9, including retinal dystrophy, various myopia subtypes, and rare neurological conditions) are all graded **L5 — Hold** with no supporting clinical or preclinical evidence specific to asenapine; their high TxGNN scores likely reflect knowledge graph topological artefacts rather than genuine biological plausibility. This report focuses on **Rank 10 (Major Affective Disorder)**, which carries L1 evidence and the only **"Proceed with Guardrails"** recommendation in this evidence pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Schizophrenia (acute); Bipolar I Disorder — Manic/Mixed Episodes (FDA-approved 2009; not ARTG-registered in Australia) |
| Predicted New Indication | Major Affective Disorder (Bipolar I — Manic and Mixed Episodes) |
| TxGNN Prediction Score | 99.57% (Rank 10 of TxGNN candidates) |
| Evidence Level | L1 (3 completed Phase 3 RCTs) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Asenapine is a second-generation antipsychotic with a broad multi-receptor pharmacological profile that directly supports its utility in major affective disorders. Its defining characteristic is a higher binding affinity for serotonin 5-HT₂A receptors relative to dopamine D₂ receptors — a property shared with effective atypical antipsychotics used in mood disorder management. Its rapid D₂ receptor dissociation kinetics reduce the risk of extrapyramidal side effects compared with first-generation agents, which improves tolerability in both acute and maintenance phases of bipolar disorder.

Several distinct receptor mechanisms collectively underpin its efficacy across the affective spectrum: D₂ receptor antagonism provides the core antimanic action; 5-HT₂C antagonism contributes synergistic antidepressant properties; H₁ antagonism delivers sedation and sleep normalisation during acute manic episodes; and α₂ adrenergic antagonism promotes noradrenaline release, potentially supporting recovery during depressive phases of bipolar disorder. Its unique sublingual formulation achieves a T_max of approximately one hour with approximately 35% bioavailability, offering faster onset compared with swallowed oral antipsychotics — a practical advantage in acute inpatient manic presentations. Asenapine also exhibits activity at NMDA and AMPA receptor sites, further distinguishing its receptor profile from other second-generation agents.

Critically, this TxGNN prediction does not represent a speculative therapeutic leap. Asenapine is **already FDA-approved** for adults with acute Bipolar I manic/mixed episodes (approved 2009) and for children and adolescents aged 10–17 years (approved 2015). The prediction reflects a well-validated, guideline-supported clinical application. The complete absence of Australian ARTG registration represents a **market access gap**, not an evidence gap, making this the most immediately actionable drug repurposing finding in this evidence pack.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01244815](https://clinicaltrials.gov/study/NCT01244815) | Phase 3 | Completed | 404 | 3-week double-blind, placebo-controlled RCT in paediatric patients aged 10–17 years with acute manic/mixed episodes of Bipolar I Disorder; three fixed-dose asenapine arms vs placebo; primary endpoint YMRS change from baseline. Largest paediatric RCT; foundational trial supporting FDA paediatric approval (2015). |
| [NCT00145470](https://clinicaltrials.gov/study/NCT00145470) | Phase 3 | Completed | 326 | 12-week double-blind, placebo-controlled RCT evaluating asenapine as add-on to lithium or valproate in adults with acute manic/mixed Bipolar I episodes. Directly supports combination use with mood stabilisers — the most common real-world prescribing scenario. |
| [NCT01349907](https://clinicaltrials.gov/study/NCT01349907) | Phase 3 | Completed | 322 | 50-week open-label, flexible-dose extension of NCT01244815 in paediatric patients; evaluates long-term safety and tolerability of asenapine in children and adolescents with Bipolar I Disorder following completion of the core 3-week trial. |
| [NCT02600741](https://clinicaltrials.gov/study/NCT02600741) | N/A | Completed | 296 | 12-month RCT of caregiver psychoeducation and skills training in patients receiving antipsychotics (including oral asenapine) for schizophrenia/schizoaffective disorders; primary outcome: reduction in treatment failures (hospitalisations, ER visits, suicide attempts). Indirect relevance to asenapine pharmacotherapy efficacy. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [23719049](https://pubmed.ncbi.nlm.nih.gov/23719049/) | 2013 | Meta-Analysis of RCTs | Int Clin Psychopharmacol | Pooled analysis of 4 RCTs confirms asenapine significantly reduces YMRS scores vs placebo in bipolar mania; demonstrates consistently favourable tolerability across adult trials |
| [29170943](https://pubmed.ncbi.nlm.nih.gov/29170943/) | 2018 | Systematic Review | Paediatric Drugs | Comprehensive review of asenapine in paediatric Bipolar I and schizophrenia; confirms FDA-approved sublingual dosing (2.5–10 mg BID) in ages 10–17 for acute manic/mixed episodes; summarises paediatric safety database |
| [20420486](https://pubmed.ncbi.nlm.nih.gov/20420486/) | 2010 | Pharmacology Review | Expert Rev Neurother | Detailed receptor binding profile (5-HT₂A, D₂, H₁, α₂, NMDA/AMPA), sublingual pharmacokinetics (T_max ~1h, bioavailability ~35%), and clinical trial outcomes in adult bipolar mania |
| [20135021](https://pubmed.ncbi.nlm.nih.gov/20135021/) | 2009 | Drug Review | Drugs of Today | Post-FDA-approval review covering mechanism of action, clinical trial programme, and positioning of asenapine in the treatment landscape for schizophrenia and bipolar mania |
| [37815563](https://pubmed.ncbi.nlm.nih.gov/37815563/) | 2023 | Narrative Review | JAMA | Contemporary JAMA review of bipolar disorder (affecting ~40 million people worldwide); contextualises place of atypical antipsychotics in current diagnostic and treatment algorithms; highlights global unmet need |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Clinical Review | Acta Psychiatr Scand | Evidence-based clinical guidance for managing bipolar mania; reviews mood stabilisers and antipsychotics and offers tentative suggestions for choice of agents; useful for positioning asenapine in Australian treatment guidelines |
| [28741044](https://pubmed.ncbi.nlm.nih.gov/28741044/) | 2017 | RCT | CNS Drugs | Open-label RCT comparing asenapine with olanzapine in borderline personality disorder; suggests clinical utility of asenapine in affective dysregulation presentations beyond Bipolar I |
| [28141623](https://pubmed.ncbi.nlm.nih.gov/28141623/) | 2017 | Comparative Review | J Clin Psychopharmacol | Quantifies activating and sedating adverse effects of second-generation antipsychotics including asenapine; provides absolute risk increase and number-needed-to-harm estimates for somnolence and related effects |
| [40430486](https://pubmed.ncbi.nlm.nih.gov/40430486/) | 2025 | Review | Pharmaceuticals | 2025 overview of new and repurposed agents in psychiatric disorders; discusses evolving indications for asenapine and unmet needs in treatment-resistant bipolar disorder and schizophrenia |
| [35141987](https://pubmed.ncbi.nlm.nih.gov/35141987/) | 2022 | Case Report | Psychogeriatrics | Successful asenapine augmentation of escitalopram in major depressive disorder with psychotic features; suggests potential utility of asenapine across a broader range of affective presentations beyond bipolar I |

---

## Safety Considerations

Asenapine is not registered on the Australian ARTG and no TGA-approved Product Information exists. For full safety assessment, please refer to:

- **FDA Prescribing Information (Saphris®):** Includes a **Black Box Warning** for increased mortality in elderly patients with dementia-related psychosis when treated with antipsychotics. Additional warnings cover neuroleptic malignant syndrome (NMS), tardive dyskinesia, metabolic changes (hyperglycaemia, dyslipidaemia, weight gain), QT prolongation, orthostatic hypotension, and hypersensitivity reactions. Oral hypoaesthesia and paraesthesia are specific to the sublingual route.
- **EMA Summary of Product Characteristics (Sycrest®):** European prescribing information with broadly comparable warnings; may be more relevant to an Australian regulatory submission context.

**Drug interactions:** No DDI data were captured in this evidence pack. Clinically relevant pharmacokinetic interactions are documented in the FDA PI and include CYP1A2 inhibitors (e.g., fluvoxamine can increase asenapine plasma concentrations) and CYP2D6 interactions. Review of a current interaction database (e.g., Micromedex, Australian Medicines Handbook) is recommended prior to any clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Asenapine has robust L1-level evidence — three completed Phase 3 RCTs in adults and children — for Bipolar I Disorder manic/mixed episodes, and holds FDA approval for both adult and paediatric (10–17 years) populations. Its absence from the Australian ARTG is a market access issue rather than an evidence gap, making this one of the most actionable drug repurposing opportunities in the current evidence pack for Australian patients with bipolar disorder who have limited access to this agent.

**To proceed, the following is needed:**

- **Regulatory pathway assessment:** Evaluate options for TGA registration via a standard market authorisation application. In the interim, clinicians may consider the TGA Special Access Scheme (SAS Category B for individual patients, or SAS Category C for broader prescriber access) with a clinical justification referencing the FDA/EMA approval basis.
- **Full safety documentation:** Obtain the current FDA Prescribing Information (Saphris®) and EMA SPC (Sycrest®) to complete a formal Australian context safety assessment, with particular attention to the dementia-related psychosis Black Box Warning and the sublingual route-specific adverse effects.
- **Mechanism of action data:** Retrieve the full DrugBank pharmacology record (DB06216) to formally document asenapine's receptor profile in this evidence pack and address the current MOA data gap.
- **Comparative effectiveness positioning:** Assess asenapine against currently ARTG-listed atypical antipsychotics for acute bipolar mania (e.g., olanzapine, quetiapine, aripiprazole, ziprasidone) to define clinical differentiation, patient population fit, and formulary positioning.
- **ANZCTR search:** Conduct a targeted Australian New Zealand Clinical Trials Registry search to identify any locally registered trials involving asenapine in mood or affective disorders.
- **Paediatric access pathway:** Given the established FDA paediatric approval for ages 10–17 years, assess the specific unmet need in this population within Australia, where paediatric bipolar disorder pharmacotherapy options remain limited.

---

*⚠️ Disclaimer: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. Data cut-off: 5 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

