---
layout: default
title: Tirofiban
parent: Moderate Evidence (L3-L4)
nav_order: 730
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Tirofiban: predicted new indication Primary release disorder of platelets (evidence level L4). Approved use: Acute coronary syndrome"
---

# Tirofiban
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Tirofiban: From Acute Coronary Syndrome to Primary Release Disorder of Platelets

## One-Sentence Summary

Tirofiban is a glycoprotein IIb/IIIa inhibitor, originally used to treat acute coronary syndrome.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but there are **no registered clinical trials** and only **3 publications**, none of which test tirofiban as a treatment for this condition.
The signal is best read as a model artefact, and the mechanistic direction is questionable.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute coronary syndrome (from the TxGNN knowledge graph; no approved indication text is available for the Australian entry) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 96.27% |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, tirofiban blocks the GPIIb/IIIa (alpha-IIb-beta-3) receptor, the final common pathway of platelet aggregation. This is why it is used in acute coronary syndrome and percutaneous coronary intervention.

Primary platelet release disorders involve defective granule secretion, a different defect from the one tirofiban targets. Blocking aggregation would not correct a secretion defect and would likely add to bleeding risk. The retrieved literature covers tirofiban in acute coronary syndrome, PCI and tirofiban-induced thrombocytopenia, not treatment of release disorders.

The high TxGNN score is therefore likely a network-association artefact. An antiplatelet agent proposed for a bleeding-type disorder is a questionable direction.

### Other Predicted Indications (for context)

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Glanzmann thrombasthenia | 96.25% | L5 | The disease is a deficiency of GPIIb/IIIa, the very target tirofiban inhibits. Tirofiban would mimic and aggravate the disease. Likely false positive. |
| 3 | Rheumatoid arthritis | 95.26% | L5 | Speculative link only. The sole paper is a case report of myocardial infarction after adalimumab. |
| 4 | Trigeminal autonomic cephalalgia | 94.67% | L5 | No mechanistic rationale, trials or literature. |
| 5 | Headache disorder | 94.53% | L5 | Loose link via platelet activation in migraine. No trials or literature. |
| 6 | Pseudo-von Willebrand disease | 94.34% | L5 | The defect is in GPIb-alpha, not GPIIb/IIIa. Bleeding risk would rise. |
| 7 | Congenital prothrombin deficiency | 93.99% | L5 | A coagulation factor deficiency. Tirofiban would add bleeding risk. |
| 8 | Thromboangiitis obliterans | 92.16% | L4 | Plausible antithrombotic rationale but no direct evidence. Could be framed as a research question. |
| 9 | Female breast carcinoma | 91.40% | L5 | Hypothesised platelet-tumour interactions only. Bleeding risk is a concern. |
| 10 | Cholecystolithiasis | 91.10% | L5 | No plausible mechanistic link. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16682384](https://pubmed.ncbi.nlm.nih.gov/16682384/) | 2006 | Clinical study | Eur Heart J | ELISA-2 trial comparing dual vs. triple antiplatelet pre-treatment in non-ST-elevation acute coronary syndrome. Concerns the original indication, not release disorders. |
| [16287613](https://pubmed.ncbi.nlm.nih.gov/16287613/) | 2005 | Clinical/laboratory study | Platelets | Tirofiban-induced thrombocytopenia is caused by drug-dependent antibodies against GPIIb/IIIa. Associated with platelet activation and more ischaemic events. This is a safety finding. |
| [12204495](https://pubmed.ncbi.nlm.nih.gov/12204495/) | 2002 | Clinical study | J Am Coll Cardiol | TOPSTAR trial of troponin release after elective PCI with or without tirofiban. Concerns cardiac intervention, not release disorders. |

None of these publications evaluates tirofiban as a treatment for primary platelet release disorders.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 8350L | Aggrastat | Solution concentrate for I.V. infusion, 12.5 mg (as hydrochloride) in 50 mL | Not available in the data compiled for this report |

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (disease associations, not label text): thrombocytopenia, blood coagulation disease, stroke disorder, cerebrovascular disorder, susceptibility to ischaemic stroke, cerebral infarction, injury, brain cancer, brain neoplasm, intracranial haemorrhage, and arteriovenous malformation.
- **Drug interactions** (100 recorded; main ones shown):
  - **Major:** abciximab, deferasirox, acalabrutinib, ibritumomab tiuxetan, tositumomab (including I-131), trastuzumab emtansine.
  - **Moderate:** acetylsalicylic acid, ketorolac (including ophthalmic), ibuprofen, dexfenfluramine, fenfluramine, sibutramine.
- **Specific concern for the predicted indication:** tirofiban-induced thrombocytopenia has been documented in the literature above, and added antiplatelet effect is likely harmful in bleeding disorders.

Please also refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no trials and no literature testing tirofiban for primary platelet release disorders. The mechanism (inhibiting platelet aggregation) points in the wrong direction for a bleeding-type disorder and would likely increase bleeding risk. The top-ranked predictions in the wider list (Glanzmann thrombasthenia, pseudo-von Willebrand disease, prothrombin deficiency) appear to be false positives. Thromboangiitis obliterans is the only prediction with a plausible mechanistic basis, and it could be framed as a research question.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank).
- Safety information from the TGA-approved PI, including warnings, contraindications and approved indication text for ARTG 8350L.
- Preclinical or mechanistic evidence that tirofiban could benefit a platelet secretion defect, which seems unlikely.
- If any repurposing direction is pursued, a prioritised review of thromboangiitis obliterans, including a literature search for GPIIb/IIIa inhibitors in peripheral ischaemic disease.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

