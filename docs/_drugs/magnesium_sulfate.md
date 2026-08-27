---
layout: default
title: Magnesium Sulfate
parent: 僅模型預測 (L5)
nav_order: 411
evidence_level: L5
indication_count: 3
---

# Magnesium Sulfate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Magnesium Sulfate: TxGNN's "New" Indication Is Already Established Obstetric Practice — Preeclampsia/Eclampsia

## One-Sentence Summary

Magnesium sulfate (DrugBank DB00653) has no original indication or mechanism-of-action data recorded in this evidence pack. The TxGNN model's top prediction — **preeclampsia/eclampsia** — is supported by **80+ clinical trials** and **20 publications**, but as the model's own rationale notes, this is not a novel repurposing signal: magnesium sulfate is already WHO/ACOG-endorsed standard-of-care anticonvulsant therapy for this condition. The evidence pack currently lacks a TGA-approved Product Information document and Australian market registration, which blocks a full safety assessment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (drug-level data gap — no `original_indications` recorded) |
| Predicted New Indication | Preeclampsia/eclampsia |
| TxGNN Prediction Score | 99.9992% (rank 47) |
| Evidence Level | L1 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for magnesium sulfate is not available in this evidence pack (drug-level data gap, High severity — DG002). However, the model's own repurposing rationale for this candidate supplies a specific mechanistic account: magnesium sulfate acts as an **NMDA-receptor antagonist** and **calcium-channel blocker**, reducing neuronal excitability and cerebral vasospasm, while also producing peripheral vasodilation — together lowering blood pressure and seizure risk in preeclampsia/eclampsia.

Importantly, the evidence pack flags that this is **not a genuinely novel hypothesis**. Magnesium sulfate for seizure prophylaxis and treatment in severe preeclampsia/eclampsia is already an internationally established standard of care (WHO, ACOG guidelines), reflected in the large trial volume and landmark systematic reviews below. The TxGNN score here should be read as a **validation of known pharmacology**, not a signal of an unstudied use.

A related note on the evidence pack itself: TxGNN's rank-2 candidate, "toxemia of pregnancy," is an older clinical synonym for the *same* condition as preeclampsia/eclampsia. The model's own annotation states the two disease nodes represent a single clinical entity and should not be scored as independent repurposing hypotheses — worth correcting in the underlying disease vocabulary, as it currently inflates the evidence count by double-listing trials and literature.

---

## Clinical Trial Evidence

Evidence pack contains ~50 retrieved trials for this indication; most are dosing/administration-route studies of an already-approved use rather than new-indication trials. The table below lists those graded A or B relevance (directly on-target, adequately powered or purpose-built PK/monitoring studies):

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00004399](https://clinicaltrials.gov/study/NCT00004399) | N/A | Completed | 2000 | Nimodipine vs. magnesium sulfate for prevention of eclamptic seizures in severe preeclampsia — large comparative RCT |
| [NCT01492608](https://clinicaltrials.gov/study/NCT01492608) | Phase 3 | Completed | 560 | Antenatal magnesium sulphate for prevention of cerebral palsy and death in preterm infants (MASP study) |
| [NCT02317146](https://clinicaltrials.gov/study/NCT02317146) | Phase 2/3 | Completed | 280 | Postpartum magnesium sulfate duration protocol (6 vs. 24 hours) in severe preeclampsia |
| [NCT05283473](https://clinicaltrials.gov/study/NCT05283473) | N/A | Completed | 64 | Serum magnesium concentration pharmacokinetics during standard loading/maintenance dosing in severe preeclampsia |
| [NCT04474704](https://clinicaltrials.gov/study/NCT04474704) | N/A | Completed | 53 | Pilot RCT using non-invasive cardiac monitoring to individualise duration of postpartum magnesium sulfate |

No ANZCTR-registered trials were returned for this indication in the evidence pack.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38865319](https://pubmed.ncbi.nlm.nih.gov/38865319/) | 2024 | RCT (acceptability) | PLoS One | Springfusor pump vs. standard IM/IV administration — acceptability and safety comparison |
| [17441885](https://pubmed.ncbi.nlm.nih.gov/17441885/) | 2007 | Cohort/Observational | J Obstet Gynaecol Res | Ionized vs. total serum magnesium concentrations during therapy in severe preeclampsia-eclampsia |
| [31527059](https://pubmed.ncbi.nlm.nih.gov/31527059/) | 2019 | Implementation/Observational | Glob Health Sci Pract | Health-system factors needed for effective magnesium sulfate delivery in resource-limited settings |
| [9794688](https://pubmed.ncbi.nlm.nih.gov/9794688/) | 1998 | Review | Obstet Gynecol | Foundational review of efficacy, benefits and risks of magnesium sulfate seizure prophylaxis |
| [36413336](https://pubmed.ncbi.nlm.nih.gov/36413336/) | 2023 | Observational | Biol Trace Elem Res | Incidence and risk factors for critical hypermagnesemia during standard dosing regimens |
| [16978425](https://pubmed.ncbi.nlm.nih.gov/16978425/) | 2006 | Review | Obstet Gynecol Surv | Cerebral haemodynamics in preeclampsia — rationale/limits of magnesium sulfate as the sole agent |
| [25353716](https://pubmed.ncbi.nlm.nih.gov/25353716/) | 2015 | Review | Acta Obstet Gynecol Scand | Interventions, including magnesium sulfate access, to reduce preeclampsia/eclampsia mortality in low-resource countries |

**Note on stronger duplicate-entity evidence:** because TxGNN's rank-2 candidate "toxemia of pregnancy" is the same clinical entity as preeclampsia/eclampsia (see above), the evidence pack's literature for that entry contains landmark trials worth citing for evidence-grading purposes: [21069663](https://pubmed.ncbi.nlm.nih.gov/21069663/) (Cochrane systematic review, tier 1) and [12057549](https://pubmed.ncbi.nlm.nih.gov/12057549/) (the Magpie Trial, tier 1 RCT, Lancet 2002) — both directly underpin the L1 evidence-level assignment.

---

## Australia Market Information

No ARTG entries were returned for magnesium sulfate in this evidence pack (`total_licenses: 0`, market status: **not marketed**). This should be verified directly against the TGA/ARTG database, as magnesium sulfate is a long-standing injectable electrolyte/anticonvulsant used in Australian obstetric and critical care practice — its absence here likely reflects a gap in the source query rather than genuine unavailability, and needs confirmation rather than being taken at face value.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No structured warnings, contraindications, or drug-interaction data were returned for magnesium sulfate in this evidence pack — this is flagged as a **Blocking** data gap (DG001), as it prevents a formal safety pre-assessment (S1 stage).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Clinical evidence for magnesium sulfate in preeclampsia/eclampsia is exceptionally strong — a Cochrane systematic review, the landmark Magpie Trial, and multiple completed Phase 2/3 studies confirm established efficacy (evidence level L1). However, this is confirmation of long-standing standard practice rather than a novel repurposing signal, and two blocking/high-severity local data gaps remain unresolved: no TGA Product Information has been retrieved (Blocking), and mechanism-of-action documentation is missing (High). Local market status also shows zero ARTG entries, which needs independent verification before any regulatory or clinical-practice claim is made in the Australian context.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications, drug interactions) — currently blocking safety pre-assessment
- DrugBank-sourced mechanism-of-action data
- Independent confirmation of current ARTG registration status for magnesium sulfate injection in Australia
- Correction of the TxGNN disease vocabulary to merge "preeclampsia/eclampsia" and "toxemia of pregnancy" as a single entity, to avoid double-counting evidence across duplicate nodes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

