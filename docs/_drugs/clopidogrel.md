---
layout: default
title: Clopidogrel
parent: 僅模型預測 (L5)
nav_order: 122
evidence_level: L5
indication_count: 10
---

# Clopidogrel
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

# Clopidogrel: From Cardiovascular Disease Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

Clopidogrel is a thienopyridine-class P2Y12 receptor antagonist antiplatelet drug established for the prevention of atherothrombotic events, including myocardial infarction and ischaemic stroke.
The TxGNN model predicts it may be effective for **migraine with brainstem aura** (formerly basilar-type migraine) as its top-ranked repurposing candidate (score: 99.44%), with the closely related broader indication of **migraine disorder** (Rank 2) supported by **8 clinical trials** (including 2 completed Phase 4 studies) and **20 publications**.
Current evidence for the brainstem aura-specific subtype is at Level L3, consisting primarily of observational studies and literature from the broader PFO-associated migraine with aura population.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cardiovascular disease prevention (atherothrombotic events: myocardial infarction, ischaemic stroke, peripheral arterial disease) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L3 (observational studies and systematic review; no clinical trials specific to this subtype) |
| Australia Market Status | Not marketed (no ARTG entries found in current dataset — see data note below) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current dataset. Based on well-established pharmacology, Clopidogrel is a thienopyridine prodrug that irreversibly binds to the P2Y12 ADP receptor on platelets, blocking ADP-mediated platelet activation and aggregation. It is metabolised to its active form via CYP2C19 and is the most widely used P2Y12 inhibitor in cardiovascular medicine.

**Migraine with brainstem aura** is characterised by brainstem-origin neurological aura symptoms — including vertigo, tinnitus, diplopia, dysarthria, bilateral paraesthesiae, bilateral visual disturbance, and reduced consciousness — preceding or accompanying typical migraine headache. This subtype has a particularly close association with patent foramen ovale (PFO): the posterior cerebral circulation (brainstem, cerebellum, occipital cortex) is supplied by the vertebrobasilar system, and platelet microemboli passing through a PFO can directly enter this territory, triggering posterior circulation transient ischaemic events or initiating cortical spreading depression (CSD) in brainstem structures.

Three mechanistic pathways support the biological plausibility of Clopidogrel in this indication: **(1) Central neuroinflammation suppression** — P2Y12 receptors are expressed on microglial cells in the trigeminal nucleus caudalis (TNC); Clopidogrel can inhibit ADP-induced RhoA/ROCK pathway activation in these cells, reducing neurogenic inflammation relevant to migraine chronification (PMID 31722730); **(2) Serotonin regulation** — platelet activation triggers mass 5-HT release followed by a sharp drop in plasma serotonin, a well-established migraine trigger; antiplatelet therapy attenuates this mechanism; **(3) PFO/ASD-mediated embolism blockade** — in structurally mediated migraine, Clopidogrel disrupts the passage of platelet aggregates and vasoactive substances (serotonin, thromboxane A2) that bypass pulmonary filtration and enter cerebral arteries. The brainstem aura subtype is mechanistically most compelling given its posterior circulation distribution and stronger epidemiological PFO association compared to cortical aura subtypes. However, no Phase 2/3 clinical trials have specifically enrolled patients with this diagnostic subtype, and the existing evidence is derived from aggregate "migraine with aura" populations.

---

## Clinical Trial Evidence

No clinical trials specifically targeting **migraine with brainstem aura** are currently registered on ClinicalTrials.gov or ICTRP.

The following trials for the closely related indication of **migraine disorder** (TxGNN Rank 2) provide supporting evidence for the antiplatelet–PFO–migraine pathway directly relevant to brainstem aura:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT00799045](https://clinicaltrials.gov/study/NCT00799045) | Phase 4 | Completed | 220 | **CANOA Trial**: Clopidogrel + Aspirin vs Aspirin alone after transcatheter ASD closure — directly evaluates Clopidogrel combination in preventing new-onset migraine post-procedure |
| [NCT05546320](https://clinicaltrials.gov/study/NCT05546320) | Phase 4 | Unknown | 1,000 | **COMPETE Trial**: Three-arm comparison of anticoagulation vs antiplatelet (including Clopidogrel) vs migraine-specific therapy in PFO-associated migraine — highest direct clinical relevance |
| [NCT02938182](https://clinicaltrials.gov/study/NCT02938182) | Phase 4 | Unknown | 50 | Prospective trial directly evaluating Clopidogrel monotherapy for migraine relief in right-to-left shunt patients |
| [NCT04946734](https://clinicaltrials.gov/study/NCT04946734) | Phase 3 | Active, not recruiting | 440 | **SPRING Trial**: Multicentre RCT comparing PFO closure vs medical therapy (drug arm includes Clopidogrel) for migraine alleviation |
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | PFO closure vs anticoagulation vs antiplatelet therapy (Clopidogrel arm) for stroke prevention — migraine as secondary endpoint, extractable data |
| [NCT02777359](https://clinicaltrials.gov/study/NCT02777359) | Phase 2 | Unknown | 100 | High-risk PFO closure vs medical therapy (standard Clopidogrel protocol) — drug arm provides migraine improvement data |
| [NCT04100135](https://clinicaltrials.gov/study/NCT04100135) | Device study | Terminated | 7 | GORE CARDIOFORM device trial for migraine — terminated due to insufficient enrolment; minimal relevance |
| [NCT02670161](https://clinicaltrials.gov/study/NCT02670161) | Phase 4 | Enrolling by invitation | 3,300 | Pragmatic neurology EMR quality improvement study covering multiple neurological disorders including migraine; not Clopidogrel-specific |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [26908949](https://pubmed.ncbi.nlm.nih.gov/26908949/) | 2016 | RCT | *European Heart Journal* | **PRIMA Trial**: Multicentre RCT of percutaneous PFO closure vs antiplatelet therapy (including Clopidogrel) in medically refractory migraine with aura — provides comparator-arm antiplatelet data |
| [24836213](https://pubmed.ncbi.nlm.nih.gov/24836213/) | 2014 | Pilot RCT | *Cephalalgia* | First pilot RCT directly testing Clopidogrel as prophylactic treatment for migraine (general migraine population including aura subgroup) |
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Systematic Review | *Headache* | Comprehensive review of antithrombotic drugs as migraine preventives — specifically covers Clopidogrel across aura subtypes including brainstem aura |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Observational | *Heart* | Key early clinical observation: Clopidogrel reduces frequency of migraine with aura after transcatheter PFO/ASD closure |
| [32848048](https://pubmed.ncbi.nlm.nih.gov/32848048/) | 2020 | Cohort/Case Series | *J Investig Med* | Clopidogrel 75 mg/day as add-on prophylaxis for drug-refractory PFO-migraine (including aura subgroup; 56.8% of patients had confirmed PFO) — positive outcomes at 3 and 6 months |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Open-label Pilot | *Neurology* | **TRACTOR Study**: Ticagrelor (P2Y12 class; same target as Clopidogrel) for refractory PFO-migraine — provides class-level mechanistic validation |
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Retrospective Review | *Neurology* | Retrospective review of thienopyridine therapy (Clopidogrel and prasugrel) in PFO migraineurs — reports clinical outcomes across the drug class |
| [24770421](https://pubmed.ncbi.nlm.nih.gov/24770421/) | 2014 | Retrospective Review | *Cephalalgia* | Clopidogrel as primary therapy for migraineurs with right-to-left shunt lesions — demonstrates reduction in migraine with aura frequency |
| [15966922](https://pubmed.ncbi.nlm.nih.gov/15966922/) | 2005 | Case Series | *J Interv Cardiol* | Intense migraine developed after ASD closure in 5/13 patients — dramatic pain relief achieved almost immediately after 300 mg Clopidogrel loading dose |
| [22992406](https://pubmed.ncbi.nlm.nih.gov/22992406/) | 2012 | Case Report/Review | *Cephalalgia* | De novo migraine after ASD closure — antiplatelet drugs including Clopidogrel associated with migraine amelioration; documents thienopyridine class effect |

---

## Australia Market Information

No ARTG entries for Clopidogrel were identified in the current dataset.

> **⚠️ Data Quality Note**: Clopidogrel is a well-established antiplatelet agent with longstanding global clinical use. The absence of ARTG entries in this dataset is highly likely to reflect a data extraction gap rather than genuine absence from the Australian market. Prescribers should verify current registration status directly via the [TGA ARTG Public Summary](https://www.tga.gov.au/resources/artg) and consult the TGA-approved Product Information (PI) before any clinical use.

---

## Safety Considerations

No safety data was retrieved for Clopidogrel in the current dataset.

> Please refer to the TGA-approved Product Information (PI) for complete safety information. Key areas to review include:
>
> - **Bleeding risk**: Major, life-threatening bleeding including intracranial haemorrhage and GI bleeding — particularly relevant when considering use in migraine patients who may also be taking NSAIDs or triptans
> - **Pharmacogenomics**: CYP2C19 poor metabolisers have significantly reduced antiplatelet response ("Clopidogrel resistance"); genotyping relevant for any repurposing protocol
> - **Contraindications**: Active pathological bleeding; hypersensitivity to Clopidogrel or any excipient
> - **Drug interactions**: Proton pump inhibitors (especially omeprazole — CYP2C19 inhibition), aspirin (combined bleeding risk), NSAIDs, anticoagulants, and CYP2C19 inhibitors/inducers
> - **Population-specific risks**: Migraine patients are typically younger adults with a different cardiovascular risk baseline than standard Clopidogrel users — bleeding risk-benefit assessment must be recalibrated for this population

---

## Conclusion and Next Steps

**Decision: Hold (Research Question) — for migraine with brainstem aura specifically**

> *Note: For the closely related indication of **migraine disorder** (TxGNN Rank 2, Evidence Level L2), two completed Phase 4 trials (CANOA, n=220; NCT02938182, n=50) and the ongoing Phase 3 SPRING trial (n=440) support a recommendation of **Proceed with Guardrails**, particularly for PFO-associated migraine with aura.*

**Rationale:**
Migraine with brainstem aura is the most mechanistically compelling subtype for Clopidogrel repurposing given its strong association with PFO, posterior circulation embolism, and brainstem CSD. However, no clinical trials have enrolled patients specifically diagnosed with brainstem aura, and the published evidence pool reports aggregate "migraine with aura" outcomes without subgroup analyses sufficient to isolate this subtype. The current evidence base supports a research question requiring subtype-specific prospective investigation before clinical application.

**To proceed, the following is needed:**

- **For brainstem aura-specific advancement:**
  - Retrospective subgroup analysis of existing PFO-migraine trial datasets (CANOA, SPRING) to extract brainstem aura outcomes using ICHD-3 diagnostic classification
  - Prospective registry or cohort study specifically enrolling patients with ICHD-3-confirmed migraine with brainstem aura and TCD/echocardiography-confirmed PFO
  - Neuroimaging protocol (DWI/FLAIR MRI) to characterise posterior circulation involvement at baseline

- **For the broader migraine indication (Rank 2 — Proceed with Guardrails):**
  - Full clinical review of CANOA trial results (PMID 26551304; PMID 32965476) and COMPETE trial design (PMID 38109984)
  - CYP2C19 genotyping protocol for patient stratification to identify likely non-responders
  - Bleeding risk stratification framework adapted for the migraine patient demographic (typically younger, lower baseline cardiovascular risk)
  - Patient selection criteria defining the PFO-confirmed vs non-PFO migraine subpopulations

- **Dataset gaps to address before any clinical use:**
  - Retrieve TGA-approved Product Information and confirm ARTG registration status
  - Obtain mechanism of action data from DrugBank (DB00758)
  - Retrieve current drug interaction database entries
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

