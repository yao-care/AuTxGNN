---
layout: default
title: Haloperidol
parent: 僅模型預測 (L5)
nav_order: 224
evidence_level: L5
indication_count: 10
---

# Haloperidol
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

# Haloperidol: From Psychosis / Schizophrenia to Manic Bipolar Affective Disorder

## One-Sentence Summary

Haloperidol is a first-generation (typical) antipsychotic and potent dopamine D2/D3 receptor antagonist, historically used in the management of schizophrenia and acute psychotic disorders.
The TxGNN model predicts it may be effective for **Manic Bipolar Affective Disorder**,
with **9 clinical trials** and **20 publications** currently supporting this direction — making it the only prediction in this analysis with sufficient evidence to proceed.

> **Note on TxGNN rankings:** TxGNN's top-ranked predictions for Haloperidol (ranks 1–9) cover rare congenital and structural conditions (e.g., congenital disorder of glycosylation, hydranencephaly, CMT1G). All are assessed as L5/Hold due to absent evidence and mechanistic misalignment. This report focuses on rank 10 (Manic Bipolar Affective Disorder) as the sole clinically actionable finding.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Schizophrenia / Acute Psychosis (antipsychotic agent; no current ARTG registration data available) |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed (no ARTG entries found) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Haloperidol is a potent D2/D3 dopamine receptor antagonist (Ki ~1 nM), classified as a first-generation typical antipsychotic. Its primary pharmacological action involves blocking dopaminergic neurotransmission in the mesolimbic pathway, which reduces pathological overactivity in circuits associated with both psychosis and mania. Detailed mechanism of action data from DrugBank was not available in this Evidence Pack; the mechanistic description below is drawn from clinical trial context and published literature within the pack.

Acute manic episodes in bipolar I disorder are characterised by dopaminergic hyperactivation in the prefrontal–limbic circuit. D2 receptor blockade directly counters this hyperexcitability, producing stabilisation of manic symptoms. This rationale is mechanistically sound and well-validated: Haloperidol has been used as an active comparator in at least three completed Phase 3 RCTs for acute bipolar mania, consistently demonstrating clinically meaningful efficacy. A 2022 network meta-analysis in *Molecular Psychiatry* (PMID 34642461) further consolidates its evidence base across randomised controlled trials.

Schizophrenia and bipolar mania share overlapping neurobiology — particularly dopaminergic dysregulation — which explains why antipsychotics effective in psychosis also perform in manic episodes. The 99.83% TxGNN score reflects this pharmacological and phenotypic similarity. The critical caveat is safety: Haloperidol carries substantially higher extrapyramidal side effect (EPS) and tardive dyskinesia risk compared to second-generation antipsychotics, which limits its role in modern first-line bipolar management.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00253162](https://clinicaltrials.gov/study/NCT00253162) | Phase 3 | Completed | 439 | Three-arm RCT: Risperidone vs Placebo vs Haloperidol for bipolar I manic episodes. Directly evaluates Haloperidol efficacy and safety at 3 and 12 weeks — highest relevance. |
| [NCT00253149](https://clinicaltrials.gov/study/NCT00253149) | Phase 3 | Completed | 158 | Add-on therapy RCT: Risperidone vs Placebo vs Haloperidol added to mood stabilisers in acute bipolar mania. Directly assesses Haloperidol add-on strategy. |
| [NCT00129220](https://clinicaltrials.gov/study/NCT00129220) | Phase 3 | Completed | 224 | Double-blind RCT: Olanzapine vs Placebo vs Haloperidol in bipolar I manic or mixed episodes. Rigorous design with Haloperidol as active comparator. |
| [NCT00097266](https://clinicaltrials.gov/study/NCT00097266) | Phase 3 | Completed | 615 | Largest trial in this set: Aripiprazole monotherapy vs comparator in acute bipolar mania. Haloperidol likely included as active comparator arm (confirm in full protocol). |
| [NCT00126009](https://clinicaltrials.gov/study/NCT00126009) | Phase 2 | Completed | 120 | Valproate + Amisulpride vs Valproate + Haloperidol in bipolar I mania over 3 months. Provides combination therapy data. |
| [NCT04327843](https://clinicaltrials.gov/study/NCT04327843) | Phase 3 | Completed | 22 | Long-acting injectable antipsychotic adherence programme for chronic psychotic disorders (Tanzania); Haloperidol likely primary agent. External validity limited by small sample and setting. |
| [NCT03541031](https://clinicaltrials.gov/study/NCT03541031) | N/A | Unknown | 120 | Micronutrient supplementation as adjunct to conventional medications (including antipsychotics) for bipolar disorder. Low direct relevance. |
| [NCT00767715](https://clinicaltrials.gov/study/NCT00767715) | Phase 4 | Terminated | 11 | Olanzapine vs conventional antipsychotics in acute mania; terminated early due to insufficient enrolment. Data unreliable. |
| [NCT06049953](https://clinicaltrials.gov/study/NCT06049953) | N/A | Recruiting | 200 | Observational study of antenatal antipsychotic exposure including Haloperidol. Provides safety data in pregnancy rather than efficacy for mania. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [34642461](https://pubmed.ncbi.nlm.nih.gov/34642461/) | 2022 | Systematic Review / Network Meta-Analysis | *Molecular Psychiatry* | Comprehensive NMA comparing pharmacological interventions for acute bipolar mania across RCTs published to March 2021. Includes Haloperidol efficacy and tolerability data. |
| [22161387](https://pubmed.ncbi.nlm.nih.gov/22161387/) | 2011 | Systematic Review (Cochrane) | *Cochrane Database of Systematic Reviews* | Cochrane review of oxcarbazepine for bipolar acute episodes; Haloperidol used as reference comparator, providing contextual efficacy benchmarking. |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Clinical Guideline / Review | *Acta Psychiatrica Scandinavica* | Evidence-based clinical guidance for bipolar mania management; specifically recommends adding Haloperidol to mood stabilisers in partial responders. |
| [36789916](https://pubmed.ncbi.nlm.nih.gov/36789916/) | 2023 | Comparative Study | *BMJ Mental Health* | Compares antipsychotic dose equivalents between acute mania and schizophrenia. Provides practical dosing guidance for Haloperidol in the manic context. |
| [22134043](https://pubmed.ncbi.nlm.nih.gov/22134043/) | 2012 | RCT | *Journal of Affective Disorders* | Randomised double-blind placebo- and Haloperidol-controlled study of olanzapine in Japanese bipolar I patients with manic/mixed episodes. |
| [18344731](https://pubmed.ncbi.nlm.nih.gov/18344731/) | 2008 | Systematic Review | *Journal of Clinical Psychopharmacology* | Systematic review of antipsychotic-induced EPS in bipolar disorder vs schizophrenia. Highlights Haloperidol's significantly higher EPS burden — critical safety finding. |
| [22070611](https://pubmed.ncbi.nlm.nih.gov/22070611/) | 2012 | Review | *CNS Neuroscience & Therapeutics* | Reviews treatment of refractory bipolar disorder; explicitly names Haloperidol as a recommended add-on option for lithium/valproate partial responders. |
| [3312180](https://pubmed.ncbi.nlm.nih.gov/3312180/) | 1987 | Controlled Trial | *Journal of Clinical Psychiatry* | Double-blind controlled comparison of clonazepam vs Haloperidol in acute mania; demonstrates Haloperidol efficacy while highlighting tardive dyskinesia risk. |
| [369472](https://pubmed.ncbi.nlm.nih.gov/369472/) | 1979 | RCT | *Archives of General Psychiatry* | Five-week double-blind RCT of lithium + Haloperidol vs placebo + Haloperidol in excited schizo-affective patients; supports combination approach. |
| [39756485](https://pubmed.ncbi.nlm.nih.gov/39756485/) | 2025 | Retrospective Analysis | *Journal of Affective Disorders* | Real-world effectiveness of long-acting injectable antipsychotics (including Haloperidol decanoate) in reducing rehospitalisation during bipolar mania. |

---

## Australia Market Information

Haloperidol has **no current ARTG registration** recorded in the available regulatory dataset (0 entries). Clinical use in Australia would therefore require one of the following pathways:

- **Special Access Scheme (SAS)** — Category B notification or Category A authorisation, depending on clinical circumstances
- **Authorised Prescriber** arrangement via the TGA
- **Clinical Trial** supply under a CTN or CTA

> Healthcare professionals should verify current ARTG status directly with the TGA at [tga.gov.au](https://www.tga.gov.au), as the data collection date for this Evidence Pack is 20 April 2026 and registration status may differ.

---

## Safety Considerations

Detailed TGA-specific safety data (PI warnings, contraindications, formal DDI listing) were not available in this Evidence Pack. The following is drawn from published evidence within the pack:

- **Extrapyramidal Side Effects (EPS):** Haloperidol carries substantially higher EPS risk than second-generation antipsychotics, including akathisia, parkinsonism, and acute dystonia. This is a consistent finding across systematic reviews (PMID 18344731) and directly affects treatment suitability in bipolar patients already at risk of motor complications.
- **Tardive Dyskinesia:** Long-term or high-dose use is associated with tardive dyskinesia, including the rare "rabbit syndrome" variant (PMID 39202628). This is irreversible in some patients and requires careful benefit-risk assessment before extended use.
- **QTc Prolongation:** Dose-dependent QTc prolongation is a known class effect; cardiac monitoring is recommended, particularly with high doses or concurrent QT-prolonging medications.

> Please refer to the TGA-approved Product Information (PI) for complete safety information, contraindications, and drug interaction data before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs have validated Haloperidol as an active comparator in acute bipolar I mania, and a 2022 network meta-analysis (*Molecular Psychiatry*) confirms its efficacy in this indication. The mechanistic rationale — D2 receptor blockade suppressing dopaminergic hyperactivation in the manic state — is well-established. However, Haloperidol's unfavourable EPS and tardive dyskinesia profile relative to second-generation antipsychotics limits its role to specific clinical scenarios (e.g., resource-limited settings, treatment-refractory patients, or parenteral use in acute agitation) rather than broad first-line application.

**To proceed, the following is needed:**

- Confirm current Australian ARTG registration status directly with the TGA; if unregistered, determine appropriate access pathway (SAS, Authorised Prescriber)
- Obtain and review the TGA-approved Product Information (PI) for Australian-specific contraindications, warnings, and drug interactions
- Retrieve formal MOA data from DrugBank (DB00502) to complete pharmacological characterisation
- Develop a safety monitoring plan covering: EPS assessment at each visit (e.g., AIMS scale for tardive dyskinesia), baseline and ongoing ECG for QTc, metabolic monitoring
- Engage a specialist psychiatrist to define patient selection criteria — second-generation antipsychotics (e.g., olanzapine, quetiapine, risperidone) are generally preferred first-line for bipolar mania in Australian clinical guidelines
- If considering long-acting injectable formulation (Haloperidol decanoate), review adherence and rehospitalisation evidence from PMID 39756485
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

