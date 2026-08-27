---
layout: default
title: Magnesium
parent: 僅模型預測 (L5)
nav_order: 410
evidence_level: L5
indication_count: 10
---

# Magnesium
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

# Magnesium: From Mineral/Electrolyte Supplementation to Migraine Disorder

## One-Sentence Summary

Magnesium is an essential mineral used clinically across a range of established roles (e.g., electrolyte replacement, eclampsia prophylaxis), though no single original indication is recorded in this evidence pack.
The TxGNN model predicts it may be effective for **Migraine Disorder** (prophylaxis and acute treatment),
with **several clinical trials (including a Phase 3 RCT)** and **20 supporting publications (including a meta-analysis of RCTs)** currently backing this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — magnesium has broad, well-established clinical uses (e.g., electrolyte replacement, eclampsia prophylaxis), but no single approved indication is recorded in this evidence pack |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 98.03% |
| Evidence Level | L2 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this magnesium record is not available in DrugBank. Based on known pharmacology, magnesium acts as an **NMDA-receptor antagonist and voltage-gated calcium-channel modulator**. Through these actions it can suppress cortical spreading depression (CSD) — the electrophysiological event underlying migraine aura — and stabilise cerebral vascular tone.

Migraine patients frequently show reduced cerebrospinal fluid and serum magnesium levels, giving a plausible causal link between magnesium deficiency and migraine susceptibility. This mechanistic relationship is not speculative: magnesium is already recognised by the American Headache Society as an option for migraine prophylaxis, and intravenous magnesium sulfate is used in some emergency departments as an adjunct for acute attacks.

A 2016 meta-analysis of randomised controlled trials (PMID 26752497) found that both intravenous and oral magnesium reduced migraine frequency and severity, and this is reinforced by a body of mechanistic reviews (2015–2025) consistently linking magnesium status to migraine pathophysiology. Together, the mechanistic plausibility and the existing (if heterogeneous) trial evidence support the TxGNN prediction.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05967442](https://clinicaltrials.gov/study/NCT05967442) | Phase 3 | Completed | 157 | RCT evaluating IV magnesium sulfate vs. metoclopramide/prochlorperazine for acute migraine and headache in the emergency setting |
| [NCT06904287](https://clinicaltrials.gov/study/NCT06904287) | Phase 3 | Recruiting | 100 | Evaluating whether adding magnesium to prochlorperazine improves migraine pain relief in the emergency department |
| [NCT03190044](https://clinicaltrials.gov/study/NCT03190044) | N/A | Unknown | 82 | RCT of a fixed combination (magnesium, parthenium, andrographis, CoQ10, riboflavin) as migraine prophylaxis |
| [NCT01756209](https://clinicaltrials.gov/study/NCT01756209) | Phase 4 | Completed | 160 | Acetaminophen/ibuprofen with vs. without magnesium prophylaxis for primary childhood migraine |
| [NCT04759040](https://clinicaltrials.gov/study/NCT04759040) | N/A | Completed | 120 | RCT of "Migraineguard" supplement (CoQ10, magnesium, riboflavin, feverfew, skullcap, black pepper) for migraine prevention |
| [NCT02901756](https://clinicaltrials.gov/study/NCT02901756) | N/A | Completed | 132 | Prospective observational study of CoQ10 + feverfew + magnesium for migraine prophylaxis |
| [NCT04463875](https://clinicaltrials.gov/study/NCT04463875) | N/A | Completed | 113 | Real-world prospective study of magnesium + vitamin B2 + feverfew + andrographis + CoQ10 for episodic migraine prophylaxis |
| [NCT07147972](https://clinicaltrials.gov/study/NCT07147972) | Phase 3 | Not yet recruiting | 100 | Comparing nutraceuticals (magnesium, riboflavin, CoQ10) vs. conventional prophylactic therapy for migraine |
| [NCT06274255](https://clinicaltrials.gov/study/NCT06274255) | N/A | Unknown | 60 | Observational comparison of serum magnesium levels between migraine patients and controls, correlated with attack frequency/duration |
| [NCT01010711](https://clinicaltrials.gov/study/NCT01010711) | N/A | Unknown | 76 | Dietary supplement (CoQ10 + minerals, including magnesium) for migraine in children and adolescents |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26752497](https://pubmed.ncbi.nlm.nih.gov/26752497/) | 2016 | Meta-analysis of RCTs | Pain Physician | IV and oral magnesium reduce acute and prophylactic migraine outcomes across pooled RCT data |
| [25916335](https://pubmed.ncbi.nlm.nih.gov/25916335/) | 2015 | RCT | J Headache Pain | Multicentre double-blind RCT showing a magnesium + riboflavin + CoQ10 supplement improves migraine symptoms |
| [29131326](https://pubmed.ncbi.nlm.nih.gov/29131326/) | 2018 | Systematic Review | Headache | Systematically evaluates the evidence base for magnesium in migraine prophylaxis |
| [40005053](https://pubmed.ncbi.nlm.nih.gov/40005053/) | 2025 | Review | Nutrients | Overview of magnesium deficiency's role in migraine pathophysiology and its disability burden |
| [31691193](https://pubmed.ncbi.nlm.nih.gov/31691193/) | 2020 | Review | Biol Trace Elem Res | Reviews magnesium's role in migraine pathophysiology, including neuronal electric potential regulation |
| [35268064](https://pubmed.ncbi.nlm.nih.gov/35268064/) | 2022 | Review | Nutrients | Discusses magnesium deficiency's link to cortical spreading depression and glutamatergic neurotransmission in migraine |
| [32878232](https://pubmed.ncbi.nlm.nih.gov/32878232/) | 2020 | Review | Nutrients | Reviews mechanisms, bioavailability, and therapeutic efficacy of magnesium (incl. magnesium pidolate) for headache |
| [30600979](https://pubmed.ncbi.nlm.nih.gov/30600979/) | 2019 | Guideline/Review | Am Fam Physician | Migraine prophylaxis guidance, situating nutraceuticals including magnesium among preventive options |
| [40378325](https://pubmed.ncbi.nlm.nih.gov/40378325/) | 2025 | Review | Am Fam Physician | Updated migraine prophylaxis review covering indications and preventive treatment goals |
| [29882776](https://pubmed.ncbi.nlm.nih.gov/29882776/) | 2018 | Review | Nutrients | Reviews magnesium's role in neurological disorders, including its protective effect against excitotoxicity |

## Australia Market Information

No ARTG (Australian Register of Therapeutic Goods) entries are recorded in this evidence pack for this magnesium product record — market status is listed as **Not Marketed**. This reflects the specific product record evaluated here; it does not necessarily indicate that all magnesium-containing products are absent from the Australian market. Current ARTG status should be verified directly with the TGA before any clinical use is considered.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Migraine disorder has the strongest evidence among magnesium's predicted new indications — a Phase 3 RCT, a meta-analysis of RCTs, and consistent mechanistic support (NMDA antagonism, CSD suppression) meeting the L2 evidence threshold. However, this drug record currently carries a **Blocking** data gap (no TFDA/TGA-equivalent Product Information warnings or contraindications on file), which prevents a full safety pre-assessment, and it is not currently registered (0 ARTG entries) in Australia.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications) for the specific magnesium formulation under consideration — currently a Blocking data gap
- Formal drug interaction (DDI) data — current query returned no results
- Detailed mechanism-of-action documentation from DrugBank to support formal S1 safety review
- Confirmation of ARTG registration status and route/dosage form suitability for migraine prophylaxis or acute treatment
- Clarification of the "original indication" baseline, since none is currently on file for this record
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

