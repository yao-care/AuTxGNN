---
layout: default
title: Clopidogrel
parent: Model Prediction Only (L5)
nav_order: 176
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-30
description: "Clopidogrel: predicted new indication Migraine disorder (evidence level L2). Approved use: Acute coronary syndrome, intracranial embolism…"
monitor_inn: "Clopidogrel"
predicted_indications: ["migraine with brainstem aura", "migraine disorder", "osteoarthritis", "tendinitis", "myositis fibrosa", "idiopathic granulomatous myositis", "rheumatoid arthritis"]
---

# Clopidogrel
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Clopidogrel: From Acute Coronary Syndrome to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Clopidogrel is an antiplatelet drug originally used for acute coronary syndrome, intracranial embolism and ST-elevation myocardial infarction.
The TxGNN model's top-ranked prediction is migraine with brainstem aura. The better-supported prediction is **migraine disorder** (rank 2), particularly migraine in patients with a patent foramen ovale (PFO), with **6 registered clinical trials** (3 directly testing clopidogrel or related antithrombotic therapy) and **20 publications** supporting this direction.

The report evaluates **migraine disorder** as the lead indication. The rank 1 entry, migraine with brainstem aura, has no registered trials and relies on extrapolation from PFO-associated migraine with aura. The remaining predictions (osteoarthritis, tendinitis, myositis fibrosa, idiopathic granulomatous myositis, rheumatoid arthritis, osteoarthritis susceptibility, pseudoachondroplasia, fibromyalgia) have no meaningful supporting evidence and are summarised at the end.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute coronary syndrome, intracranial embolism, ST-elevation myocardial infarction (from the knowledge graph; the ARTG entry has no indication text recorded) |
| Predicted New Indication | Migraine disorder (lead candidate; rank 1 was migraine with brainstem aura) |
| TxGNN Prediction Score | 0.9944 (migraine disorder); 0.9944 (migraine with brainstem aura) |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Clopidogrel is an oral antiplatelet agent that is well known to act through P2Y12 receptor antagonism. Its efficacy in acute coronary syndrome and thrombotic events is established.

The proposed link to migraine runs through platelet activation. Migraine with aura is associated with PFO and other right-to-left shunts. Platelet activation and paradoxical microembolism, or release of vasoactive mediators such as serotonin across the shunt, are proposed triggers. Blocking platelet P2Y12 may therefore reduce attacks in this subgroup. Clinical reports also describe new-onset migraine after transcatheter closure of atrial septal defects, and clopidogrel has been associated with improvement in these patients.

The applicability appears limited to a PFO or aura subpopulation. For migraine with brainstem aura specifically, the evidence is extrapolated from migraine with aura generally. P2Y12 receptors have also been implicated in animal models of migraine (microglial activation, nitroglycerin-induced model), but these are preclinical findings only.

---

## Clinical Trial Evidence

Trials for migraine disorder (the rank 1 prediction has no registered trials):

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05546320](https://clinicaltrials.gov/study/NCT05546320) (COMPETE) | Phase 2 | Completed | 1000 | Anticoagulation vs antiplatelet therapy (including clopidogrel) vs migraine therapy in migraine with PFO; results published in 2026 (PMID 42526943) |
| [NCT00799045](https://clinicaltrials.gov/study/NCT00799045) (CANOA) | Phase 4 | Completed | 220 | Clopidogrel added to aspirin to prevent new-onset migraine after transcatheter ASD closure |
| [NCT02938182](https://clinicaltrials.gov/study/NCT02938182) | Phase 4 | Unknown | 50 | Prophylactic effectiveness of clopidogrel in migraine with right-to-left shunt; small, status unverified |
| [NCT04946734](https://clinicaltrials.gov/study/NCT04946734) (SPRING) | Phase 3 | Active, not recruiting | 440 | PFO closure vs medicine for migraine; device trial, medicine is the comparator (context only) |
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) (CLOSE) | Phase 3 | Completed | 664 | PFO closure vs anticoagulants vs antiplatelets for stroke recurrence; migraine not the primary outcome |
| [NCT04100135](https://clinicaltrials.gov/study/NCT04100135) | Not applicable | Terminated | 7 | GORE septal occluder device study; not drug evidence |

No ANZCTR identifiers were included in the data compiled for this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42526943](https://pubmed.ncbi.nlm.nih.gov/42526943/) | 2026 | RCT (multicentre, open label) | BMJ | Efficacy and safety of antithrombotic treatment for migraine prevention in patients with PFO (COMPETE) |
| [26551304](https://pubmed.ncbi.nlm.nih.gov/26551304/) | 2015 | RCT | JAMA | CANOA: clopidogrel plus aspirin vs aspirin alone for migraine after ASD closure |
| [32965476](https://pubmed.ncbi.nlm.nih.gov/32965476/) | 2021 | RCT (1-year follow-up) | JAMA Cardiol | CANOA one-year results after clopidogrel cessation at 3 months |
| [24836213](https://pubmed.ncbi.nlm.nih.gov/24836213/) | 2014 | RCT (pilot) | Cephalalgia | Pilot randomised study of clopidogrel as migraine prophylaxis |
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Systematic review | Headache | Role of antithrombotic drugs in migraine prevention |
| [40144614](https://pubmed.ncbi.nlm.nih.gov/40144614/) | 2025 | Systematic review | Indian J Thorac Cardiovasc Surg | Incidence and management of new-onset headache after transcatheter ASD closure |
| [32848048](https://pubmed.ncbi.nlm.nih.gov/32848048/) | 2020 | Cohort/case series | J Investig Med | Clopidogrel 75 mg/day as add-on prophylaxis in drug-refractory migraine with PFO |
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Retrospective review | Neurology | Off-label thienopyridine therapy in migraineurs with PFO |
| [24770421](https://pubmed.ncbi.nlm.nih.gov/24770421/) | 2014 | Retrospective review | Cephalalgia | Clopidogrel as primary therapy for migraineurs with right-to-left shunt |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Cohort | Heart | Clopidogrel reduced migraine with aura after closure of PFO and ASD |

Related but non-clopidogrel evidence includes a ticagrelor open-label pilot (PMID 30478067) and the PRIMA trial of PFO closure (PMID 26908949), which tested a device rather than a drug.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13365K | Clovix 75 | Tablet 75 mg (as besilate) | Not recorded in the data compiled for this report |

Only one oral single-ingredient product is listed. Migraine is not an approved indication.

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these are not label text): acute liver failure, hepatitis, blood coagulation disease, injury, thrombocytopenic purpura, active peptic ulcer disease and intracranial haemorrhage.
- **Drug interactions:** 100 interactions were identified. Major interactions include:
  - Proton pump inhibitors: rabeprazole, omeprazole, esomeprazole
  - Pioglitazone
  - Loperamide
  - Repaglinide
  - Moderate interactions include acetylsalicylic acid, morphine, bupropion, cimetidine, clarithromycin, lansoprazole and pantoprazole.
- **Bleeding risk:** the literature includes reports of intracerebral haemorrhage with celecoxib co-administration and spontaneous haemarthrosis with clopidogrel plus aspirin. This is relevant to a migraine population, which commonly uses NSAIDs.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Migraine disorder has the strongest support among the predictions (L2). A completed Phase 4 RCT (CANOA), a pilot RCT and a large Phase 2 randomised trial (COMPETE, published in BMJ in 2026) provide clinical signals. However, no Phase 3 RCT directly tests clopidogrel for migraine, the benefit appears confined to PFO or aura subpopulations, and bleeding and drug interaction burdens are significant.

**To proceed, the following is needed:**
- Detailed review of the COMPETE and CANOA results, including bleeding outcomes and effect size in patients with and without PFO
- Phase 3 evidence or a confirmatory trial in a PFO-associated migraine population
- Patient selection criteria (PFO or right-to-left shunt confirmation, refractory migraine) and a bleeding-risk and DDI management plan, especially for PPIs and NSAIDs
- Mechanism of action data and TGA Product Information warnings and contraindications
- Evidence specific to migraine with brainstem aura before any subtype-specific use

**Other predictions (all Hold):**
- **Rheumatoid arthritis and osteoarthritis:** the literature suggests possible harm (clopidogrel-associated inflammatory arthritis) or lower osteoarthritis risk with ticagrelor than with clopidogrel, not clopidogrel benefit.
- **Tendinitis, fibromyalgia and osteoarthritis susceptibility:** the retrieved papers are irrelevant to clopidogrel efficacy.
- **Myositis fibrosa, idiopathic granulomatous myositis and pseudoachondroplasia:** prediction only, with no trials, literature or plausible mechanism.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

