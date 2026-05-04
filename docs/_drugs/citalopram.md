---
layout: default
title: Citalopram
parent: 僅模型預測 (L5)
nav_order: 111
evidence_level: L5
indication_count: 10
---

# Citalopram
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

# Citalopram: From Major Depressive Disorder to Obsessive-Compulsive Disorder

---

## One-Sentence Summary

Citalopram is a highly selective serotonin reuptake inhibitor (SSRI) with a well-established global track record in treating major depressive disorder, though it is currently not registered on the Australian Register of Therapeutic Goods (ARTG).
The TxGNN model predicts it may be effective for **Obsessive-Compulsive Disorder (OCD)**, with **30 clinical trials** and **16 publications** currently supporting this direction — including direct citalopram studies dating to 1999 and a substantial body of evidence from escitalopram, its pharmacologically active S-enantiomer.
The mechanistic rationale is strong, the evidence base is clinically meaningful, and the prediction score is exceptionally high.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Australia; globally approved for Major Depressive Disorder |
| Predicted New Indication | Obsessive-Compulsive Disorder (OCD) |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L2 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

While detailed mechanism of action data was not available from the Australian regulatory dataset, citalopram's pharmacology is well characterised in the global literature. Citalopram is a highly selective inhibitor of the serotonin transporter (5-HTT), blocking serotonin reuptake at the presynaptic membrane and thereby increasing synaptic serotonin concentrations in limbic and cortico-striatal brain regions. Its selectivity for 5-HTT is among the highest in the SSRI class, with minimal affinity for histamine, muscarinic, or adrenergic receptors — which contributes to a relatively clean side-effect profile.

The pathophysiology of OCD involves hyperactivity within the cortico-striato-thalamo-cortical (CSTC) circuit, a loop critically regulated by serotonergic inputs from the dorsal raphe nucleus. Dysregulation of 5-HT neurotransmission in this circuit is thought to contribute to the persistence of intrusive thoughts and repetitive compulsive behaviours. By augmenting synaptic serotonin, SSRIs are believed to restore inhibitory tone within the CSTC loop, leading to a reduction in OCD symptom severity. This is the same mechanism underlying citalopram's established antidepressant effect, making the cross-indication application mechanistically coherent rather than speculative.

Critically, direct clinical evidence for citalopram in OCD dates to 1999 (PMID 10471169; PMID 10572334), predating many modern OCD treatment guidelines. Escitalopram — the active S-enantiomer of citalopram — has since been evaluated in multiple Phase 2–4 clinical trials specifically targeting OCD, and systematic reviews confirm SSRIs as first-line pharmacotherapy for the condition. The TxGNN model's high-confidence prediction (rank 3,728 of ~17,000 diseases, score 99.74%) is therefore well-supported by established science.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT00086645](https://clinicaltrials.gov/study/NCT00086645) | Phase 2 | Completed | 149 | **Direct citalopram study**: Evaluated citalopram vs placebo for repetitive/compulsive behaviours in children with autism spectrum disorders — the most direct available efficacy evidence for citalopram itself in OCD-core symptomatology. |
| [NCT00305500](https://clinicaltrials.gov/study/NCT00305500) | Phase 3 | Completed | 100 | Open-label Phase 3 study of high-dose escitalopram (up to 50 mg/day) in OCD outpatients over 18 weeks; evaluated tolerability and efficacy via Y-BOCS. Supports the dose-response relationship in OCD. |
| [NCT00723060](https://clinicaltrials.gov/study/NCT00723060) | Phase 4 | Completed | 176 | Randomised, double-blind comparison of conventional-dose (20 mg) vs high-dose (40 mg) escitalopram in OCD; efficacy assessed by Y-BOCS, HAM-D, HAM-A, CGI, and OCI-R. One of the largest escitalopram-specific OCD trials. |
| [NCT03993535](https://clinicaltrials.gov/study/NCT03993535) | Phase 4 | Completed | 250 | Multisite naturalistic follow-up (US, Brazil, India, Netherlands) of OCD patients; investigated clinical, neurocognitive, and neuroimaging predictors of SSRI treatment response — provides real-world effectiveness data. |
| [NCT02022709](https://clinicaltrials.gov/study/NCT02022709) | Phase 4 | Completed | 78 | Compared SSRIs, exposure and response prevention (ERP), and combined therapy in Chinese OCD patients; also identified biological and psychological predictors of SSRI response in a non-Western population. |
| [NCT00215137](https://clinicaltrials.gov/study/NCT00215137) | Phase 2 | Completed | 14 | Pilot study evaluating safety and efficacy of escitalopram in OCD; early Phase 2 evidence specifically targeting the active enantiomer. |
| [NCT00116532](https://clinicaltrials.gov/study/NCT00116532) | Phase 4 | Completed | 30 | Assessed escitalopram efficacy in OCD and explored optimal treatment dose; provides additional Phase 4 effectiveness data. |
| [NCT00456937](https://clinicaltrials.gov/study/NCT00456937) | Phase 4 | Completed | 15 | Open-label study of escitalopram (up to 20 mg/day) in patients with comorbid schizophrenia and OCD; demonstrated exploratory evidence for SSRI benefit in a complex, difficult-to-treat population. |
| [NCT04336228](https://clinicaltrials.gov/study/NCT04336228) | Phase 4 | Active, not recruiting | 46 | Investigates serotonin's role in compulsive behaviour using sub-chronic escitalopram; examines how 5-HT modulation affects the balance between habitual and goal-directed control — directly relevant to OCD neuroscience. |
| [NCT01936051](https://clinicaltrials.gov/study/NCT01936051) | N/A | Completed | 12 | PK-PD modelling of escitalopram plasma concentrations and serotonin transporter occupancy in OCD patients; also examined the influence of ABCB1 gene polymorphisms on drug levels — informs precision dosing. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [10471169](https://pubmed.ncbi.nlm.nih.gov/10471169/) | 1999 | Clinical Case Series / Open Trial | Int Clin Psychopharmacol | **Landmark direct citalopram study**: Reports citalopram's efficacy in OCD; establishes the SSRI–OCD mechanistic link and provides the earliest direct clinical evidence for citalopram specifically in this indication. |
| [10572334](https://pubmed.ncbi.nlm.nih.gov/10572334/) | 1999 | Randomised Open-label Trial | European Psychiatry | **Direct citalopram RCT**: Randomised comparison of citalopram alone vs citalopram + clomipramine in 16 treatment-resistant OCD patients; confirms citalopram efficacy even in refractory cases. |
| [12839522](https://pubmed.ncbi.nlm.nih.gov/12839522/) | 2003 | Open-label Clinical Study | Psychiatry Clin Neurosci | **Direct citalopram in paediatric OCD**: 8-week open-label study in 15 children and adolescents (aged 6–17) treated with citalopram 20–30 mg/day; demonstrated significant Y-BOCS improvement and good tolerability. |
| [35121274](https://pubmed.ncbi.nlm.nih.gov/35121274/) | 2022 | Systematic Review / Network Meta-Analysis | J Psychiatric Research | Compared pharmacological and psychological treatments in paediatric OCD; SSRIs confirmed as effective first-line pharmacotherapy, supporting use of citalopram-class agents in children and adolescents. |
| [38703743](https://pubmed.ncbi.nlm.nih.gov/38703743/) | 2024 | Systematic Review | Comprehensive Psychiatry | Examined long-term safety and tolerability of off-label high-dose SRIs (including citalopram-class drugs) in OCD; supports extending dosing beyond standard limits in treatment-refractory patients with appropriate monitoring. |
| [28477500](https://pubmed.ncbi.nlm.nih.gov/28477500/) | 2017 | Meta-Analysis | J Affective Disorders | Confirmed that OCD shows a lower placebo response than other anxiety disorders, underscoring the genuine and specific pharmacological signal of SSRIs in OCD treatment — strengthening the pharmacological rationale. |
| [12607204](https://pubmed.ncbi.nlm.nih.gov/12607204/) | 2000 | Mechanistic Review | World J Biological Psychiatry | Reviewed serotonergic mechanisms underpinning OCD, drawing on neuroimaging, neuroimmunology, and pharmacological challenge data; provides the foundational biological rationale for SSRI use in this condition. |
| [22305974](https://pubmed.ncbi.nlm.nih.gov/22305974/) | 2012 | Review / Clinical Guidelines | BMJ Clinical Evidence | Comprehensive OCD clinical guidelines review; confirms SSRIs as first-line pharmacotherapy across the lifespan, with strong evidence in both episodic and chronic OCD phenotypes. |
| [32982805](https://pubmed.ncbi.nlm.nih.gov/32982805/) | 2020 | Meta-Review | Frontiers in Psychiatry | Meta-review of antidepressant use in children and adolescents across multiple conditions, including OCD; addresses suicidality signals and provides paediatric benefit-risk context relevant to clinical decision-making. |
| [35818708](https://pubmed.ncbi.nlm.nih.gov/35818708/) | 2022 | Systematic Review | Expert Opinion Pharmacotherapy | Systematically evaluated pharmacotherapy for OCD-spectrum conditions; contextualises the SRI class evidence base across related obsessive-compulsive presentations. |

---

## Australia Market Information

Citalopram is currently **not registered on the Australian Register of Therapeutic Goods (ARTG)**. The TGA database search (conducted 9 March 2026) identified zero ARTG entries for citalopram.

> **Note for prescribers**: Citalopram is approved in multiple comparable regulatory jurisdictions — including the United States (FDA, 1998 for MDD), the United Kingdom (MHRA), Canada (Health Canada), and the European Union (EMA) — where it is indicated for major depressive disorder and, in several markets, anxiety disorders. In Australia, access to unregistered medicines may be sought via the **TGA Special Access Scheme (SAS Category B or C)** or through an **Authorised Prescriber** arrangement, subject to individual patient circumstances and clinical justification.

---

## Safety Considerations

No TGA-approved Australian Product Information (PI) is available for citalopram given its absence from the ARTG, and no drug–drug interaction data were returned by the evidence collection system.

Based on the well-characterised international safety profile, prescribers should be aware of the following key considerations:

- **QTc prolongation**: Citalopram causes dose-dependent prolongation of the cardiac QT interval. In 2011–2012, the FDA and EMA issued safety communications restricting maximum doses (FDA: 40 mg/day in most adults; 20 mg/day in patients aged >60 years, those with hepatic impairment, or those taking CYP2C19 inhibitors). Baseline and follow-up ECG monitoring is recommended in at-risk patients.
- **Serotonin syndrome**: Concomitant use with MAOIs, other serotonergic agents (triptans, tramadol, linezolid, St John's Wort), or high-dose tryptophan carries a risk of serotonin syndrome and is generally contraindicated or requires close monitoring.
- **Paediatric suicidality**: A class-wide FDA black box warning applies to all antidepressants regarding increased risk of suicidal ideation in children, adolescents, and young adults aged up to 24 years. Close clinical monitoring is required, particularly during initial treatment and dose changes.

Please refer to the FDA-approved or EMA-approved Product Information for the complete safety, contraindication, and drug interaction profile until Australian TGA registration is obtained.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Citalopram has direct clinical evidence for OCD efficacy dating to 1999, a mechanistically coherent serotonergic rationale perfectly aligned with established OCD pathophysiology, and strong supporting evidence from escitalopram (its active enantiomer) across multiple Phase 2–4 trials. The TxGNN prediction score is exceptionally high (99.74%), and the assigned evidence level of L2 reflects at least one completed Phase 3 trial in OCD using the closely related active enantiomer. The primary barrier to use in Australia is the absence of ARTG registration rather than any pharmacological or clinical efficacy concern.

**To proceed, the following is needed:**

- **TGA regulatory pathway assessment**: Determine the most appropriate access mechanism — SAS Category B/C or Authorised Prescriber — and document clinical justification for each individual patient
- **Formal MOA and safety documentation**: Retrieve the complete DrugBank-sourced mechanism of action, contraindication, and warning data to support a full S1 safety evaluation
- **QTc risk management plan**: Establish a baseline ECG protocol and ongoing cardiac monitoring schedule, particularly for patients with pre-existing cardiac risk factors or those on QT-prolonging co-medications
- **Drug interaction screening**: Conduct a patient-level drug–drug interaction review using an Australian clinical decision support tool (e.g., MIMS, NPS MedicineWise) given the absence of DDI data in the current evidence pack
- **Paediatric safety review**: If use in children or adolescents with OCD is being considered, a formal paediatric benefit-risk assessment is required, referencing the FDA black box warning and the network meta-analysis data (PMID 35121274)
- **Reference PI sourcing**: Obtain the current FDA or EMA-approved PI to serve as the primary safety reference document pending Australian registration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

