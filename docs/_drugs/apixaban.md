---
layout: default
title: Apixaban
parent: Model Prediction Only (L5)
nav_order: 54
evidence_level: L5
indication_count: 1
monitor_inn: "Apixaban"
predicted_indications: ["migraine disorder"]
last_modified_at: 2026-10-27
description: "Apixaban: predicted new indication migraine disorder (evidence level L5). Approved use: Not recorded in the local data"
---

# Apixaban
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Apixaban: Direct factor Xa inhibitor → migraine disorder
{: .text-alpha }

## One-Sentence Summary

Apixaban is an oral direct factor Xa inhibitor (anticoagulant). The TxGNN model predicts it may be relevant to **migraine disorder**, but the supporting evidence is limited to **1 clinical trial** that does not study migraine directly and **3 publications** (two case reports and one retrospective study), with conflicting results.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | migraine disorder |
| TxGNN Prediction Score | 0.9902 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Apixaban is known as a direct factor Xa inhibitor, so it reduces thrombin generation and fibrin clot formation.

A possible link to migraine is the association between migraine with aura and paradoxical embolism through a patent foramen ovale (PFO), as well as prothrombotic states such as antiphospholipid antibodies. In these subgroups, anticoagulation could theoretically reduce microembolic or thrombotic triggers.

This link is hypothetical. The TxGNN score is a model-based ranking, not a validated mechanism. The case reports are contradictory: one describes migraine with aura worsening after starting apixaban, and another describes aura resolving on warfarin but not on apixaban. Any effect may differ between vitamin K antagonists and factor Xa inhibitors.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | PFO closure vs anticoagulants vs antiplatelet therapy for preventing stroke recurrence in patients with PFO. Migraine is not the primary focus or endpoint, and the anticoagulant arm is not specific to apixaban. Indirect context only. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33402037](https://pubmed.ncbi.nlm.nih.gov/33402037/) | 2021 | Retrospective study (75 patients) | Lupus | Antithrombotic therapy in refractory migraine with antiphospholipid antibodies. Some patients may improve, but the specific agents tested need verification. |
| [37582651](https://pubmed.ncbi.nlm.nih.gov/37582651/) | 2023 | Case report with literature review | The Neurologist | Migraine with aura worsened after starting apixaban. The authors note that literature on direct oral anticoagulants in migraine is scarce and controversial. |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Case report | Headache | Migraine with aura resolved on warfarin but returned on apixaban, then resolved again on resuming warfarin. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 10414D | Eliquis | Tablet 5 mg | Not recorded in the local data |

## Safety Considerations

**Drug Interactions** (100 interactions recorded; selected examples):
- **Major**: acetylsalicylic acid, cobicistat, deferasirox, ibritumomab tiuxetan, tositumomab
- **Moderate**: aprepitant, clarithromycin, clotrimazole, dexamethasone, miconazole, rolapitant

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications. Anticoagulation carries a bleeding risk that must be weighed carefully in a condition such as migraine.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No study directly tests apixaban for migraine. The available case reports conflict, and the one trial is about stroke prevention in PFO. The high TxGNN score alone does not justify progressing.

**To proceed, the following is needed:**
- Controlled studies of apixaban or other factor Xa inhibitors in migraine, particularly migraine with aura, PFO or antiphospholipid antibody subgroups
- Mechanism of action data to support the proposed link
- Safety review from the TGA Product Information, including a bleeding risk assessment for a non-thrombotic indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

