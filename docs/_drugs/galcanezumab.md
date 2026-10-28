---
layout: default
title: Galcanezumab
parent: Model Prediction Only (L5)
nav_order: 327
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
monitor_inn: "Galcanezumab"
predicted_indications: ["heparin cofactor 2 deficiency", "antithrombin deficiency type 2", "factor 5 excess with spontaneous thrombosis"]
description: "Galcanezumab: predicted new indication Heparin cofactor 2 deficiency (evidence level L5). Approved use: Not recorded in the local data"
---

# Galcanezumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Galcanezumab: Heparin cofactor 2 deficiency
{: .text-alpha }

## One-Sentence Summary

Galcanezumab is an anti-CGRP monoclonal antibody originally used to prevent migraine.
The TxGNN model predicts it may be effective for **migraine with brainstem aura**, a migraine subtype,
with **no registered clinical trials** specific to this subtype but **20 publications** supporting the broader anti-CGRP direction (including Phase 3 RCT data in episodic migraine).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Heparin cofactor 2 deficiency |
| TxGNN Prediction Score | 0.9950 |
| Evidence Level | L5 (based on Phase 3 RCTs in broader migraine; subtype-specific evidence is limited) |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

**Note on other predictions:** The model ranked several coagulation-related conditions highest by score (heparin cofactor 2 deficiency 0.9950, antithrombin deficiency type 2 0.9941, factor 5 excess with spontaneous thrombosis 0.9941). None has any supporting trial or publication, and none has a plausible link to CGRP blockade. These scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. They are rated **Hold**.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, galcanezumab is a humanised monoclonal antibody that binds calcitonin gene-related peptide (CGRP) and inhibits its activity. CGRP is a key mediator of trigeminovascular activation in migraine.

Migraine with brainstem aura is a subtype of migraine, and galcanezumab is already used for migraine prevention. This is therefore an extension within the original indication rather than true repurposing. Emerging literature on anti-CGRP antibodies in migraine aura and in genetic or hemiplegic migraine (for example PMID 38091211, 40341526, 41618146) is supportive but not definitive.

Subtype-specific efficacy in brainstem aura has not been established in dedicated trials, and patients with these aura subtypes have often been excluded from RCTs.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for migraine with brainstem aura in the data compiled for this report. No ANZCTR identifiers were identified.

---

## Literature Evidence

The compiled data include 20 publications. The most relevant are listed below (RCTs first, then reviews and observational studies).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29813147](https://pubmed.ncbi.nlm.nih.gov/29813147/) | 2018 | RCT | JAMA Neurol | EVOLVE-1 Phase 3 trial of galcanezumab for prevention of episodic migraine |
| [33549036](https://pubmed.ncbi.nlm.nih.gov/33549036/) | 2021 | RCT (pooled post-hoc, Phase 3) | J Headache Pain | EVOLVE-1, EVOLVE-2 and REGAIN: effect on migraine severity and symptoms in episodic and chronic migraine |
| [36266558](https://pubmed.ncbi.nlm.nih.gov/36266558/) | 2023 | RCT (secondary analysis) | Neurol Ther | Japanese Phase 2 trial: effect on migraine severity and associated symptoms |
| [32504377](https://pubmed.ncbi.nlm.nih.gov/32504377/) | 2020 | Review | Drugs | Galcanezumab significantly more effective than placebo in episodic and chronic migraine prevention, and in episodic cluster headache |
| [41618146](https://pubmed.ncbi.nlm.nih.gov/41618146/) | 2026 | Systematic review | J Headache Pain | Effectiveness and safety of anti-CGRP antibodies in hemiplegic migraine (individual patient analysis) |
| [38091211](https://pubmed.ncbi.nlm.nih.gov/38091211/) | 2024 | Observational cohort (pilot) | Neurol Sci | Pilot study of anti-CGRP antibodies for migraine aura |
| [38332541](https://pubmed.ncbi.nlm.nih.gov/38332541/) | 2024 | Case series | CNS Neurosci Ther | Effect of anti-CGRP therapy on migraine aura |
| [40341526](https://pubmed.ncbi.nlm.nih.gov/40341526/) | 2025 | Case series | Headache | Two genetic conditions with prominent migraine responded to CGRP antagonist therapy |
| [37366160](https://pubmed.ncbi.nlm.nih.gov/37366160/) | 2023 | Case series | Headache | Anti-CGRP antibodies in hemiplegic migraine |
| [42390441](https://pubmed.ncbi.nlm.nih.gov/42390441/) | 2026 | Cohort (pharmacoepidemiology) | Cephalalgia | Cerebrovascular risk (ischaemic stroke/TIA) with CGRP antibodies versus onabotulinumtoxinA |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12469G | Emgality | Injection 120 mg in 1 mL pre-filled pen | Not available in the compiled data |

---

## Safety Considerations

- **Vascular safety:** A case report describes cerebral artery vasoconstriction after a galcanezumab loading dose (PMID 39365416), and CGRP blockade carries theoretical ischaemic concerns. A real-world cohort study has examined stroke/TIA risk against onabotulinumtoxinA (PMID 42390441), and a multinational cohort study has examined glaucoma risk with CGRP inhibitors (PMID 42090640). Caution is warranted in brainstem aura, where ischaemic concerns are theoretical.

Please refer to the TGA-approved Product Information (PI) for full warnings, contraindications and drug interaction information. No drug interaction records were found in the compiled data.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Galcanezumab already has Phase 3 RCT support in migraine and is marketed in Australia. Migraine with brainstem aura is a migraine subtype, so this is an in-class extension. Subtype-specific evidence is limited to small observational studies and case series. All other model predictions (coagulation and skin conditions) lack any supporting evidence or mechanistic plausibility and should be held.

**To proceed, the following is needed:**
- Subtype-specific efficacy data for brainstem aura (a dedicated trial or well-designed registry)
- Mechanism of action data and the approved indication text for the ARTG entry
- Review of the PI for warnings and contraindications
- A cardiovascular and cerebrovascular monitoring plan, given the theoretical ischaemic concerns
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

