---
layout: default
title: Ziprasidone
parent: High Evidence (L1-L2)
nav_order: 735
evidence_level: L1
indication_count: 10
---

# Ziprasidone
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Ziprasidone: From Bipolar Mania/Schizophrenia to Major Affective Disorder

## One-Sentence Summary

Ziprasidone (DrugBank DB00246) is an atypical antipsychotic historically used for schizophrenia and bipolar mania/mixed episodes, based on literature identifying it as "the fifth atypical antipsychotic approved by FDA for use in bipolar mania and mixed episodes" (PMID 19040553).
The TxGNN model predicts it may also be effective for **Major Affective Disorder** (bipolar depression and treatment-resistant major depressive disorder, used as monotherapy or augmentation), with **29 clinical trials** and **20 publications** currently supporting this direction.
This is the strongest-evidenced candidate among the model's top‑10 predictions for this drug — most other high-scoring predictions (e.g. trichotillomania, hydranencephaly, X-linked myopia) have no supporting trials or literature and are assessed as likely model noise.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (`original_indications` empty). Literature evidence indicates ziprasidone was originally approved for bipolar mania/mixed episodes and schizophrenia (PMID 19040553) |
| Predicted New Indication | Major Affective Disorder (bipolar depression / major depressive disorder, monotherapy or antidepressant augmentation) |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L1 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

Note: Of the 10 TxGNN-ranked candidates in this pack, only **major affective disorder** (rank 3, L1/S3) and **Tourette syndrome** (rank 7, L3/S2, "Research Question") have any supporting clinical trial or literature evidence. The remaining 8 candidates (trichotillomania, hydranencephaly, congenital disorder of glycosylation, X-linked myopia variants, retinal dystrophy, polymicrogyria) are scored L5/S0/Hold — the evidence pack's own annotations flag these as likely knowledge-graph noise with no biologically plausible mechanism.

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data is not available in this evidence pack (flagged as data gap DG002). However, based on the literature evidence collected for the major affective disorder candidate, ziprasidone is a **5-HT2A/D2 receptor antagonist**, a mechanism shared across atypical antipsychotics. This serotonin–dopamine modulating profile is well established as therapeutically relevant not only for psychosis but for mood disorders — it underlies ziprasidone's original approval for bipolar mania/mixed episodes and its subsequent use in bipolar depression and as an antidepressant augmentation agent in treatment-resistant major depressive disorder (MDD).

The relationship between the original indication (bipolar mania) and the predicted new indication (major affective disorder, encompassing bipolar depression and MDD) is a natural pharmacological extension rather than a distant repurposing leap — both fall within the same disease spectrum (bipolar disorder) or share a common downstream neurotransmitter target (serotonergic/dopaminergic dysregulation in mood disorders). This is reinforced by an established treatment-class precedent: multiple second-generation antipsychotics (quetiapine, aripiprazole, olanzapine) already carry regulatory approval for bipolar depression and/or adjunctive MDD treatment, and ziprasidone has been studied extensively in the same clinical context.

That said, `original_indications` and `taiwan_regulatory.licenses` are both empty in this evidence pack, meaning the drug's baseline approved indications and Australian regulatory history cannot be independently verified here. This should be cross-checked against the TGA-approved Product Information before any clinical decision is made.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00141271](https://clinicaltrials.gov/study/NCT00141271) | Phase 3 | Completed | 536 | Randomised, double-blind, placebo-controlled fixed-flexible dose trial of oral ziprasidone in outpatients with Bipolar I Depression |
| [NCT00257166](https://clinicaltrials.gov/study/NCT00257166) | Phase 3 | Completed | 238 | 4-week double-blind, placebo-controlled trial of flexible-dose ziprasidone in children/adolescents (10–17y) with Bipolar I Disorder (manic/mixed) |
| [NCT00483548](https://clinicaltrials.gov/study/NCT00483548) | Phase 3 | Completed | 298 | 6-week double-blind, placebo-controlled trial of ziprasidone as add-on to lithium, valproate or lamotrigine in Bipolar I Depression |
| [NCT00312494](https://clinicaltrials.gov/study/NCT00312494) | Phase 3 | Completed | 680 | 3-week double-blind, placebo-controlled trial of add-on ziprasidone with lithium or divalproex in acute mania |
| [NCT00282464](https://clinicaltrials.gov/study/NCT00282464) | Phase 3 | Completed | 392 | 6-week double-blind, placebo-controlled trial of flexible-dose ziprasidone in outpatients with Bipolar I Depression |
| [NCT00340379](https://clinicaltrials.gov/study/NCT00340379) | Phase 2/3 | Completed | 72 | Head-to-head comparison of ziprasidone monotherapy vs sertraline+haloperidol for psychotic major depression |
| [NCT00555997](https://clinicaltrials.gov/study/NCT00555997) | Phase 2 | Completed | 120 | 12-week randomised, double-blind, placebo-controlled trial of ziprasidone monotherapy for MDD (HAM-D-17 outcome) |
| [NCT00633399](https://clinicaltrials.gov/study/NCT00633399) | Phase 2 | Completed | 458 | Three-phase trial of ziprasidone added to SSRIs for SSRI-non-responsive MDD |
| [NCT00667745](https://clinicaltrials.gov/study/NCT00667745) | Phase 4 | Completed | 283 | LiTMUS effectiveness trial — lithium-optimised treatment for bipolar disorder, with ziprasidone as one adjunctive arm |
| [NCT01053429](https://clinicaltrials.gov/study/NCT01053429) | N/A | Completed | 3391 | Large post-marketing surveillance study of ziprasidone (Zeldox) safety/efficacy in real-world use |

No ANZCTR-registered trials were identified in this evidence pack.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27835715](https://pubmed.ncbi.nlm.nih.gov/27835715/) | 2017 | RCT | J Clin Psychiatry | Cardiac, endocrine, metabolic and motoric effects of adjunctive ziprasidone in MDD non-responders to escitalopram |
| [26085041](https://pubmed.ncbi.nlm.nih.gov/26085041/) | 2015 | RCT | Am J Psychiatry | Efficacy of ziprasidone augmentation of escitalopram in persistent non-psychotic unipolar MDD |
| [24815673](https://pubmed.ncbi.nlm.nih.gov/24815673/) | 2014 | RCT | Int Clin Psychopharmacol | 12-week sequential parallel comparison trial of ziprasidone monotherapy in MDD with/without psychomotor symptoms |
| [28749091](https://pubmed.ncbi.nlm.nih.gov/28749091/) | 2018 | RCT | J Clin Psychiatry | Efficacy of adjunctive ziprasidone for cognitive symptoms of MDD |
| [40808264](https://pubmed.ncbi.nlm.nih.gov/40808264/) | 2025 | Systematic Review | Bipolar Disorders | Pharmacological interventions for MDD/bipolar depression with mixed features |
| [35510505](https://pubmed.ncbi.nlm.nih.gov/35510505/) | 2023 | Review (Meta-analysis) | Psychological Medicine | Efficacy and safety/tolerability of antipsychotics (incl. ziprasidone) in MDD |
| [35993319](https://pubmed.ncbi.nlm.nih.gov/35993319/) | 2022 | Review (Network Meta-analysis) | Psychological Medicine | Efficacy/acceptability of second-generation antipsychotics with antidepressants in unipolar depression augmentation |
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | Review (Network Meta-analysis) | J Affect Disord | Augmentation strategies for treatment-resistant major depression |
| [34238049](https://pubmed.ncbi.nlm.nih.gov/34238049/) | 2021 | Review | J Psychopharmacol | Efficacy/tolerability of antidepressant+SGA combinations vs esketamine vs lithium in MDD |
| [19040553](https://pubmed.ncbi.nlm.nih.gov/19040553/) | 2008 | Review | CNS Neurosci Ther | Ziprasidone in the treatment of affective disorders — drug-specific mechanistic and clinical review |

---

## Australia Market Information

No ARTG entries were found for ziprasidone in this evidence pack (`total_licenses: 0`, `market_status: Not marketed / Not Marketed`). Ziprasidone does not currently appear to be registered for supply in Australia based on the data available here; this should be confirmed directly against the TGA ARTG database before any repurposing pathway is progressed.

---

## Safety Considerations

Structured safety fields (key warnings, contraindications, drug interactions) are not populated in this evidence pack — `safety.key_warnings` and `safety.contraindications` are both marked as data gaps, and the DDI query returned no results. This is recorded in the evidence pack as **data gap DG001, severity Blocking**, with the stated impact "cannot proceed to S1 safety pre-assessment."

Despite the absence of structured safety data, the literature evidence collected for this candidate includes relevant cardiac safety signals worth flagging:
- A reported case of sudden death in a patient with Tourette syndrome during a ziprasidone clinical trial (PMID 15728441)
- A systematic review of cardiac/QTc safety of antipsychotic medications in paediatric and adolescent populations (PMID 39549076)

These are consistent with ziprasidone's well-recognised class-level QT-prolongation risk and support the need for cardiac monitoring (baseline and follow-up ECG) if this indication is pursued clinically.

Please refer to the TGA-approved Product Information (PI) — once ziprasidone's Australian registration status is confirmed — for complete, authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Major affective disorder is supported by L1-level evidence — multiple completed Phase 3 RCTs (bipolar depression, acute mania) plus a substantial body of Phase 2 RCTs and meta-analyses on MDD augmentation — and a coherent, literature-supported mechanistic rationale (5-HT2A/D2 antagonism). However, two blocking-severity data gaps prevent immediate progression: ziprasidone's Australian market status is unclear (0 ARTG entries) and TFDA/TGA-level safety labelling (warnings, contraindications) is entirely absent from this evidence pack.

**To proceed, the following is needed:**
- Resolve data gap DG001 (Blocking): obtain and review the TGA-approved Product Information for warnings, contraindications and monitoring requirements
- Resolve data gap DG002 (High): obtain detailed mechanism-of-action data from DrugBank to confirm the mechanistic rationale above
- Confirm ziprasidone's actual ARTG/TGA registration status and, if unregistered, identify the applicable market-entry or Special Access pathway
- Verify original approved indications directly against DrugBank/TGA records, since `original_indications` was empty in this evidence pack
- Given the QT-prolongation signal identified in the literature, build cardiac monitoring (ECG) into any proposed clinical protocol for this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

