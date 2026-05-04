---
layout: default
title: Aripiprazole
parent: 僅模型預測 (L5)
nav_order: 55
evidence_level: L5
indication_count: 10
---

# Aripiprazole
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

# Aripiprazole: From Schizophrenia / Bipolar Disorder to Major Affective Disorder

## One-Sentence Summary

Aripiprazole is a second-generation (atypical) antipsychotic with well-established use in schizophrenia and bipolar I disorder, acting as a dopamine system stabiliser through D2/D3 partial agonism combined with 5-HT1A partial agonism and 5-HT2A antagonism.
The TxGNN model predicts it may be effective for **Major Affective Disorder** (encompassing bipolar disorder and major depressive disorder),
with **over 50 clinical trials** and **20 publications** currently supporting this direction — including multiple large-scale pivotal Phase 3 trials.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from ARTG registry (no entries identified in this dataset) |
| Predicted New Indication | Major Affective Disorder |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L1 |
| Australia Market Status | Not identified in dataset (0 ARTG entries) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the formal drug record for this Evidence Pack. Based on information embedded in the prediction rationale and the broader scientific literature, aripiprazole is a dopamine system stabiliser — a D2/D3 receptor partial agonist and 5-HT1A partial agonist with concurrent 5-HT2A antagonism. Unlike traditional antipsychotics that fully block D2 receptors, aripiprazole's partial agonism provides bidirectional modulation: dampening dopaminergic hyperactivity in psychotic states while potentiating signalling in hypodopaminergic states such as depression and anhedonia. This mechanistic profile is fundamentally different from conventional antipsychotics and underpins its utility across a spectrum of neuropsychiatric conditions.

Major affective disorder is characterised by dysregulation of precisely those monoaminergic circuits that aripiprazole modulates — prefrontal-limbic dopamine and serotonin pathways, reward processing networks involving the nucleus accumbens, and hypothalamic-pituitary-adrenal stress axis interactions. Both bipolar disorder (manic and depressive phases) and treatment-resistant major depressive disorder (TRD-MDD) involve disrupted dopamine-serotonin balance that aripiprazole's receptor profile is well-positioned to address. The drug's stabilising rather than blocking action allows it to function across the mood spectrum without precipitating the depressogenic effects seen with full D2 antagonists.

The clinical plausibility of this prediction is reinforced by aripiprazole's FDA approval as adjunctive treatment for MDD and as a first-line agent for bipolar I mania and maintenance — evidence that goes well beyond repurposing hypothesis into established clinical practice in multiple jurisdictions. The VAST-D trial (n=1,522), one of the largest augmentation studies ever conducted in depression, confirmed aripiprazole's superiority in symptom remission. The TxGNN model's score of 99.62% therefore reflects a high-confidence computational validation of what is already a clinically substantiated therapeutic direction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT00095758](https://clinicaltrials.gov/study/NCT00095758) | Phase 3 | Completed | 1,200 | 14-week DBPC pivotal trial assessing aripiprazole as adjunctive treatment to ongoing antidepressant therapy in MDD; core registration-quality evidence for FDA adjunctive MDD approval |
| [NCT01421342](https://clinicaltrials.gov/study/NCT01421342) | Phase 3 | Completed | 1,522 | VAST-D trial: compared aripiprazole augmentation vs bupropion augmentation vs bupropion switch in Veterans with MDD unresponsive to first-line antidepressants; aripiprazole augmentation demonstrated superior remission rates |
| [NCT00876343](https://clinicaltrials.gov/study/NCT00876343) | Phase 3 | Completed | 586 | DBPC trial: aripiprazole vs placebo as adjunctive therapy co-administered with SSRI or SNRI in patients with MDD; confirmed efficacy of adjunctive strategy |
| [NCT03423680](https://clinicaltrials.gov/study/NCT03423680) | Phase 3 | Recruiting | 390 | Ongoing confirmatory DBPC trial: aripiprazole adjunctive to mood stabiliser in bipolar I or II disorder with a major depressive episode; scheduled completion December 2025 |
| [NCT02046564](https://clinicaltrials.gov/study/NCT02046564) | Phase 3 | Completed | 412 | ASC-01 (fixed aripiprazole/sertraline combination) vs sertraline monotherapy in MDD patients with incomplete SSRI response; evaluated fixed-dose combination strategy |
| [NCT00261443](https://clinicaltrials.gov/study/NCT00261443) | Phase 4 | Completed | 1,270 | Long-term combination treatment (aripiprazole + lithium or valproate) in bipolar I outpatients partially non-responsive to mood stabiliser monotherapy |
| [NCT00277212](https://clinicaltrials.gov/study/NCT00277212) | Phase 4 | Completed | 1,169 | DBPC: aripiprazole combined with lamotrigine for long-term maintenance in bipolar I disorder following recent manic or mixed episode |
| [NCT01567527](https://clinicaltrials.gov/study/NCT01567527) | Phase 3 | Completed | 731 | DBPC maintenance trial: aripiprazole intramuscular depot formulation in bipolar I disorder; primary endpoint was time to recurrence of any mood episode |
| [NCT00110461](https://clinicaltrials.gov/study/NCT00110461) | Phase 3 | Completed | 296 | DBPC: two doses of aripiprazole in children and adolescents with bipolar I disorder, manic or mixed episode; extends evidence to paediatric populations |
| [NCT00102518](https://clinicaltrials.gov/study/NCT00102518) | Phase 3 | Completed | 325 | Open-label flexible-dose safety study (2–30 mg) in adolescents with schizophrenia and children/adolescents with bipolar I disorder; long-term tolerability data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | Systematic Review / Network Meta-analysis | J Affect Disord | NMA of augmentation strategies in adult TRD; aripiprazole ranked among the most efficacious and well-tolerated augmentation agents across multiple comparisons |
| [38669232](https://pubmed.ncbi.nlm.nih.gov/38669232/) | 2024 | Systematic Review / Meta-analysis of RCTs | PLoS One | Largest meta-analysis of RCTs evaluating aripiprazole or bupropion augmentation and switching in TRD and MDD; confirmed comparable efficacy with distinct tolerability profiles |
| [35510505](https://pubmed.ncbi.nlm.nih.gov/35510505/) | 2023 | Systematic Review / Meta-analysis | Psychol Med | Comprehensive meta-analysis of antipsychotics as monotherapy and adjunctive therapy for MDD; aripiprazole among the most extensively studied and efficacious agents |
| [38219278](https://pubmed.ncbi.nlm.nih.gov/38219278/) | 2024 | Systematic Review / Network Meta-analysis | Neuropsychopharmacol Rep | Frequentist NMA comparing brexpiprazole vs aripiprazole vs placebo specifically in Japanese MDD patients inadequately responsive to antidepressants; relevant to Asia-Pacific prescribing |
| [34167174](https://pubmed.ncbi.nlm.nih.gov/34167174/) | 2021 | Systematic Review / Meta-analysis | Prim Care Companion CNS Disord | Long-term (≥6 months) efficacy and tolerability of adjunctive aripiprazole for MDD; remission was the primary outcome; supports sustained benefit beyond acute trials |
| [37746943](https://pubmed.ncbi.nlm.nih.gov/37746943/) | 2023 | Systematic Review / Network Meta-analysis | Medicine | NMA comparing 4 atypical antipsychotics (aripiprazole, quetiapine, olanzapine, brexpiprazole) as adjunctive treatment for MDD; ranked efficacy and safety profiles |
| [37149344](https://pubmed.ncbi.nlm.nih.gov/37149344/) | 2023 | Review | Psychiatr Clin North Am | Pharmacotherapy review for TRD; aripiprazole and brexpiprazole identified as most widely studied and guideline-endorsed augmentation agents; practical prescribing guidance included |
| [36855876](https://pubmed.ncbi.nlm.nih.gov/36855876/) | 2023 | Review | Am J Psychiatry | Contextualises antipsychotic augmentation within the evolving TRD landscape including esketamine and other novel agents; aripiprazole as the established comparator benchmark |
| [37815563](https://pubmed.ncbi.nlm.nih.gov/37815563/) | 2023 | Review | JAMA | Comprehensive JAMA review of bipolar disorder diagnosis and treatment (estimated 40 million affected globally); aripiprazole cited as a key evidence-based maintenance agent |
| [36961650](https://pubmed.ncbi.nlm.nih.gov/36961650/) | 2023 | RCT (Open-label) | CNS Drugs | Pivotal pharmacokinetic and safety study of aripiprazole 2-month ready-to-use long-acting injectable (Ari 2MRTU 960) in schizophrenia and bipolar I; supports extended-interval dosing formulation development |

---

## Australia Market Information

No ARTG entries for aripiprazole were identified in this dataset (0 entries returned). This may reflect a data gap rather than true absence from the Australian market. Healthcare professionals should verify current TGA registration status, approved indications, and PBS listing status via the [TGA ARTG public portal](https://www.tga.gov.au/resources/artg) before any clinical or research application.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for complete safety information, including warnings, contraindications, and drug interactions.

> **Note:** Aripiprazole's partial D2 agonist mechanism is associated with a known risk of impulse control disorders (including pathological gambling, hypersexuality, and compulsive behaviours) in some patients. This is a class-specific concern distinct from full antagonist antipsychotics and should be specifically addressed in patient counselling and monitoring protocols.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction for aripiprazole in major affective disorder is supported by Level 1 evidence — multiple completed Phase 3 RCTs including a large-scale effectiveness trial (VAST-D, n=1,522), at least six independent meta-analyses and network meta-analyses, and FDA approval already granted for adjunctive MDD and bipolar I treatment in the United States. This prediction aligns with established global clinical practice rather than constituting a speculative repurposing candidate.

**To proceed, the following is needed:**

- **Verify Australian regulatory status**: Confirm current ARTG registration and approved indications via the TGA portal — the 0-entry result in this dataset likely reflects a data collection gap for a drug that is commercially available in Australia
- **Obtain TGA-approved Product Information (PI)**: Detailed Australian dosing, warnings, contraindications, and special population guidance must be obtained before clinical use
- **Clarify the repurposing question**: If aripiprazole already holds relevant TGA-approved indications, the clinical pathway becomes an off-label prescribing or PBS authority question rather than a formal repurposing submission — the appropriate regulatory and reimbursement pathway should be confirmed
- **Establish a safety monitoring protocol**: At minimum, this should include baseline metabolic parameters (weight, fasting glucose, lipid profile), regular monitoring for akathisia and extrapyramidal symptoms, and patient education on impulse control disorder risk
- **Review PBS authority requirements**: Confirm whether adjunctive MDD and/or bipolar disorder maintenance indications are covered under the PBS and whether streamlined or authority prescriptions apply in the Australian context
- **Formalise the MoA data gap**: Request DrugBank API query to populate the formal `drug.original_moa` field for complete regulatory documentation

---

> ⚠️ **Disclaimer**: This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. Healthcare professionals should refer to current TGA-approved prescribing information and exercise independent clinical judgement.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

