---
layout: default
title: Acetylsalicylic Acid
parent: 僅模型預測 (L5)
nav_order: 21
evidence_level: L5
indication_count: 10
---

# Acetylsalicylic Acid
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

# Acetylsalicylic Acid: From Pain and Cardiovascular Management to Migraine with Brainstem Aura

## One-Sentence Summary

Acetylsalicylic acid (aspirin) is one of medicine's oldest and most versatile agents, widely used for analgesia, antipyresis, and cardiovascular event prevention through its COX-inhibiting and antiplatelet mechanisms.
The TxGNN model predicts it may be effective for **migraine with brainstem aura** — a rare migraine subtype formerly known as basilar migraine — with **no registered clinical trials** and **19 publications** currently exploring this direction.
While biological plausibility exists through prostaglandin and TXA2 suppression, the brainstem aura phenotype carries unique vascular considerations that require prospective validation before clinical application.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No ARTG-registered indication data returned in this dataset; aspirin is a well-established analgesic, antipyretic, anti-inflammatory, and antiplatelet agent |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 |
| Australia Market Status | Not listed in current dataset (ARTG query returned 0 results — direct TGA verification recommended) |
| Number of ARTG Entries | 0 (dataset query; see note below) |
| Recommended Decision | Research Question |

> **Important note on Australian market status:** The regulatory query in this Evidence Pack returned no ARTG entries for acetylsalicylic acid. This is inconsistent with aspirin's well-known widespread availability in Australia as both an over-the-counter and prescription medicine. The absence of entries reflects a data source limitation in this dataset, not the drug's actual market status. Clinicians should verify directly with the [TGA ARTG database](https://www.tga.gov.au/resources/artg).

---

## Why is This Prediction Reasonable?

Although formal MOA data was not retrieved in this Evidence Pack, aspirin's pharmacology is among the most thoroughly characterised in all of medicine. Aspirin irreversibly acetylates cyclo-oxygenase-1 (COX-1) and COX-2 enzymes, suppressing downstream synthesis of prostaglandins and thromboxane A2 (TXA2). This dual action underpins its analgesic, anti-inflammatory, antipyretic, and antiplatelet effects. At low doses, COX-1 inhibition in platelets predominates, effectively blocking TXA2-mediated platelet aggregation and vasoconstriction for the platelet's lifespan.

Migraine with brainstem aura (MBrA, formerly "basilar migraine") is characterised by neurological aura symptoms arising from brainstem or bilateral occipital lobe structures — including diplopia, dysarthria, tinnitus, ataxia, decreased consciousness, and bilateral sensory disturbances — preceding the headache phase. The accepted mechanism involves cortical spreading depression (CSD) extending into brainstem territories, with subsequent trigeminovascular activation and neurogenic inflammation mediated partly by prostaglandins and platelet-derived TXA2. Aspirin's suppression of both prostaglandin-mediated neuroinflammation and TXA2-driven vasoconstriction provides a mechanistically coherent rationale for potential benefit.

A 2014 retrospective study (PMID 25729594) specifically evaluated low-dose aspirin as prophylactic treatment in 95 patients with migraine with aura (per ICHD-II criteria), showing meaningful reductions in attack frequency. A 2025 systematic review (PMID 39989443) further examined antithrombotic drugs — including aspirin — as migraine preventive therapy. However, a critical caveat applies to the brainstem aura subtype: patients with MBrA were historically excluded from clinical trials of vasoconstrictive acute therapies (triptans, ergotamines) due to concerns about basilar artery stroke risk. Whether antiplatelet therapy with aspirin conveys benefit or poses additional risk in this particular subtype remains an open research question requiring dedicated prospective study.

---

## Clinical Trial Evidence

Currently no registered clinical trials for acetylsalicylic acid specifically in migraine with brainstem aura.

> The absence of dedicated trials is clinically significant. Broader clinical trial evidence supports aspirin in acute migraine with or without aura (e.g., PMID 10448545 — IV lysine acetylsalicylate vs sumatriptan), but no trial has prospectively targeted the brainstem aura subtype as a primary endpoint. This gap is a key factor in the L3 evidence classification.

---

## Literature Evidence

| PMID | Year | Study Type | Journal | Key Findings |
|------|------|-----------|---------|-------------|
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Systematic Review | Headache | Evaluates antithrombotic drugs (including aspirin) as migraine preventive therapy; reviews biological plausibility of antiplatelet approaches across migraine subtypes |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Evidence Assessment (Systematic) | Headache | American Headache Society updated evidence review of acute migraine pharmacotherapies; includes aspirin as an established acute treatment option with demonstrated efficacy |
| [25729594](https://pubmed.ncbi.nlm.nih.gov/25729594/) | 2014 | Retrospective Study | Current Health Sciences Journal | 203 migraine-with-aura patients; 95 treated with low-dose ASA showed reduced attack frequency; most directly relevant evidence for aspirin prophylaxis in the aura-migraine spectrum |
| [10448545](https://pubmed.ncbi.nlm.nih.gov/10448545/) | 1999 | Randomised Controlled Trial | Cephalalgia | 278-patient multicentre RCT; IV lysine acetylsalicylate (equivalent to 1g ASA) vs subcutaneous sumatriptan vs placebo for acute migraine with or without aura; ASA demonstrated significant acute efficacy |
| [34384631](https://pubmed.ncbi.nlm.nih.gov/34384631/) | 2021 | Review | Revue neurologique | Comprehensive review of migraine with aura pathophysiology; covers cortical spreading depression mechanism and its pharmacological implications |
| [30291554](https://pubmed.ncbi.nlm.nih.gov/30291554/) | 2018 | Review | Current Pain and Headache Reports | Pathophysiological and clinical differences between migraine with and without aura; informs treatment selection and risk stratification relevant to ASA use |
| [9556832](https://pubmed.ncbi.nlm.nih.gov/9556832/) | 1998 | Review | Schweizerische medizinische Wochenschrift | Reviews migraine treatment mechanisms; notes group studies do not show superiority of ergotamines or sumatriptan over simple analgesics including ASA, particularly with a prokinetic agent |
| [35006660](https://pubmed.ncbi.nlm.nih.gov/35006660/) | 2022 | Guideline Review | FP Essentials | AHA/ASA stroke primary prevention guidelines; provides essential context for aspirin use in patients with migraine with aura who carry an elevated stroke risk |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Observational | Heart (British Cardiac Society) | Clopidogrel (another antiplatelet agent) reduced migraine with aura frequency after transcatheter closure of persistent foramen ovale; supports broader antiplatelet mechanism relevance in aura migraine |
| [34048399](https://pubmed.ncbi.nlm.nih.gov/34048399/) | 2021 | Review | Continuum | Headache in women across the hormonal lifecycle; contextualises migraine with aura treatment considerations including antiplatelet approaches in reproductive-aged women |

---

## Australia Market Information

The regulatory dataset query returned **no ARTG entries** for acetylsalicylic acid. As noted above, this reflects a data source limitation rather than the drug's actual availability in Australia. Aspirin is widely registered and available in Australia in multiple formulations (immediate-release tablets, enteric-coated tablets, soluble formulations) at various doses for pain, fever, and cardiovascular indications.

**Recommended action:** Verify current ARTG registration, approved indications, dosage forms, and access the current TGA-approved Product Information (PI) directly at:
👉 [https://www.tga.gov.au/resources/artg](https://www.tga.gov.au/resources/artg) — search "aspirin" or "acetylsalicylic acid"

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for comprehensive safety information. The safety data fields in this Evidence Pack returned no usable information from the regulatory query.

> **Clinician advisory — specific to migraine with brainstem aura context:**
> Migraine with brainstem aura was historically classified as a contraindication for triptans and combined oral contraceptives due to concerns about basilar artery territory stroke risk. Prescribers considering aspirin for this population should be aware of:
> - Gastrointestinal bleeding risk, particularly at higher doses or with prolonged use
> - The risk–benefit balance of antiplatelet therapy in a population already at elevated cerebrovascular risk
> - Potential interactions with other anticoagulants or NSAIDs
> - The need for individualised patient-level risk stratification before initiating therapy outside approved indications

---

## Conclusion and Next Steps

**Decision: Research Question (Hold)**

**Rationale:**
The TxGNN model assigns a very high confidence score (99.94%), and mechanistic plausibility for aspirin in migraine with brainstem aura is grounded in well-established COX/TXA2 pharmacology. However, current evidence sits at L3 — relying on observational and retrospective data, with no dedicated prospective RCTs for this specific migraine subtype — and the unique neurological risk profile of brainstem aura patients warrants caution before clinical extrapolation.

**To proceed, the following is needed:**

- Prospective RCT specifically enrolling patients with migraine with brainstem aura (currently no trials registered globally)
- A systematic review or meta-analysis specifically examining aspirin prophylaxis in the brainstem aura subtype, separated from broader migraine-with-aura studies
- Stroke risk stratification data for antiplatelet use in this population, particularly in women of reproductive age
- Retrieval and review of the TGA-approved Product Information for aspirin to confirm approved indications, contraindications, and relevant warnings
- MOA data retrieval from DrugBank (currently a data gap) to strengthen mechanistic documentation for regulatory submissions
- Verification of current ARTG registration status and available dosage forms via the TGA database

---

*This report is generated from the TxGNN drug repurposing evidence framework and is intended for research and clinical evaluation purposes only. It does not constitute medical advice or a recommendation to prescribe outside approved indications. All clinical decisions should incorporate full assessment of individual patient risk and current TGA-approved Product Information.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

