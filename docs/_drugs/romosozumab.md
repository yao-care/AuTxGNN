---
layout: default
title: Romosozumab
parent: 僅模型預測 (L5)
nav_order: 606
evidence_level: L5
indication_count: 10
---

# Romosozumab
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

# Romosozumab: From Postmenopausal Osteoporosis to Osteoporosis Management in Chronic Kidney Disease

## One-Sentence Summary

Romosozumab is a sclerostin-inhibiting monoclonal antibody established (per the trials cited in this evidence pack) for postmenopausal osteoporosis. Of the 10 TxGNN-predicted indications screened, most have no supporting evidence and several are mechanistically implausible or contradictory; the one with genuine clinical support is **osteoporosis management in patients with impaired renal function (CKD)**, backed by **1 completed Phase 1 trial** and **15 publications**, including post-hoc analyses of the FRAME/ARCH Phase 3 RCTs and a meta-analysis.

> **Note on methodology:** The highest TxGNN score in this pack (97.8%, "obsolete vitamin D deficiency") is not used as the headline finding — that disease term is itself flagged obsolete in the ontology and has zero supporting evidence. This report leads with the candidate with the strongest evidence, per pharmacological review practice, and lists all 10 screened candidates below for transparency.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed via TFDA/ARTG records (drug not registered); cited literature (FRAME, ARCH trials) indicates postmenopausal osteoporosis at high fracture risk |
| Predicted New Indication | Osteoporosis in patients with impaired renal function (CKD) |
| TxGNN Prediction Score | 91.50% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails (renal-impairment population only) |

### All 10 Screened Candidates

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-------------|-----------------|-----------------|
| 1 | Obsolete vitamin D deficiency | 97.83% | L5 | Hold |
| 2 | Calcium-alkali syndrome | 97.44% | L5 | Hold |
| 3 | Primary bone dysplasia (defective mineralization) | 97.27% | L5 | Hold |
| 4 | Severe nonproliferative diabetic retinopathy | 95.01% | L5 | Hold |
| 5 | Renal osteodystrophy | 94.28% | L3 | Research Question |
| 6 | Osteomalacia | 93.47% | L4 | Hold |
| 7 | Pregnancy-associated osteoporosis | 92.86% | L4 | Research Question |
| 8 | Autosomal dominant neovascular inflammatory vitreoretinopathy | 92.43% | L5 | Hold |
| 9 | Worth syndrome | 92.37% | L5 | Hold (mechanistically contraindicated — see below) |
| **10** | **Impaired renal function disease** | **91.50%** | **L2** | **Proceed with Guardrails** |

---

## Why is This Prediction Reasonable?

Detailed, TFDA/DrugBank-sourced mechanism-of-action data is flagged as a data gap in this pack. Based on the cited literature (e.g. PMID 29846712, PMID 34822428), romosozumab is a humanised monoclonal antibody against **sclerostin**, an osteocyte-secreted inhibitor of the Wnt/β-catenin pathway. By blocking sclerostin, romosozumab both stimulates osteoblast-mediated bone formation and reduces bone resorption — a "dual-acting" mechanism distinct from purely anti-resorptive agents (bisphosphonates, denosumab).

Chronic kidney disease (CKD) commonly causes CKD-Mineral and Bone Disorder (CKD-MBD), in which sclerostin levels are compensatorily elevated and fracture risk is substantially higher than in the general population (cited reviews report 18–32% of CKD patients also have osteoporosis, with >2.5x fracture risk). Since osteoporosis and CKD frequently co-occur, and romosozumab is partly renally cleared, the clinically meaningful question is not a genuinely new indication but **whether the existing osteoporosis indication remains safe and effective when renal function is impaired**.

This is supported directly: a dedicated Phase 1 PK/PD/safety study in Stage 4 and dialysis-dependent patients (NCT01833754) was completed, and post-hoc subgroup analyses of the pivotal FRAME and ARCH trials (PMID 35466448, PMID 35639174) specifically examined mild-to-moderate CKD subpopulations. However, the mechanism is not without caveats — cited literature (PMID 29846712, PMID 34822428) warns that anti-sclerostin therapy may show attenuated bone efficacy and increased hypocalcaemia risk in advanced CKD (eGFR <30 mL/min), and one candidate in this same pack (Worth syndrome, an LRP5 gain-of-function sclerosing bone disorder) illustrates that blocking sclerostin can worsen disease when the underlying pathway is already overactive — underscoring that this is a guardrailed extension, not a mechanism-free assumption.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01833754](https://clinicaltrials.gov/study/NCT01833754) | Phase 1 | Completed | 24 | Single 210 mg SC dose in healthy subjects vs. Stage 4 renal impairment vs. Stage 5 (haemodialysis) — evaluated safety, tolerability, and immunogenicity |

No ANZCTR-registered trials were identified in the supplied data for this indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35466448](https://pubmed.ncbi.nlm.nih.gov/35466448/) | 2022 | RCT subgroup (post hoc, FRAME/ARCH) | J Bone Miner Res | Efficacy/safety of romosozumab in postmenopausal women with osteoporosis and mild-to-moderate CKD |
| [35639174](https://pubmed.ncbi.nlm.nih.gov/35639174/) | 2022 | RCT subgroup (post hoc, FRAME) | J Bone Miner Metab | Japanese subpopulation analysis confirming efficacy/safety in mild-to-moderate CKD |
| [38972312](https://pubmed.ncbi.nlm.nih.gov/38972312/) | 2024 | Meta-analysis of RCTs | Kidney Blood Press Res | Comparative efficacy/safety of anti-osteoporotic agents across CKD stages 3–5 |
| [34231877](https://pubmed.ncbi.nlm.nih.gov/34231877/) | 2021 | Cochrane systematic review | Cochrane Database Syst Rev | Pharmacological interventions vs. placebo/usual care for osteoporosis in CKD stages 3–5D |
| [35304747](https://pubmed.ncbi.nlm.nih.gov/35304747/) | 2022 | PK/PD study | J Clin Pharmacol | Romosozumab exposure ~31–43% higher in Stage 4 RI and ESRD-on-dialysis vs. normal renal function |
| [36330828](https://pubmed.ncbi.nlm.nih.gov/36330828/) | 2023 | Cardiovascular safety study | J Bone Miner Res | Cardiovascular safety of romosozumab specifically in postmenopausal women with CKD |
| [40669844](https://pubmed.ncbi.nlm.nih.gov/40669844/) | 2025 | Meta-analysis/Review | Renal Failure | Adynamic bone disorder biomarkers in CKD — relevant to low-turnover bone risk with anti-sclerostin therapy |
| [41171457](https://pubmed.ncbi.nlm.nih.gov/41171457/) | 2026 | Narrative review | Osteoporos Int | Efficacy/safety of romosozumab in CKD and osteoporosis |
| [40457078](https://pubmed.ncbi.nlm.nih.gov/40457078/) | 2025 | Review | Curr Osteoporos Rep | Diagnosis and management of osteoporosis in CKD |
| [29846712](https://pubmed.ncbi.nlm.nih.gov/29846712/) | 2019 | Review/Opinion (caution) | Nephrol Dial Transplant | Cautions that sclerostin blockade in CKD-MBD may show attenuated efficacy and elevated hypocalcaemia risk in advanced CKD |

---

## Australia Market Information

Romosozumab currently has **0 ARTG entries** — the product is not marketed or TGA-registered in Australia. No TGA-approved Product Information exists to reference.

---

## Safety Considerations

- **Data gap flagged as Blocking**: TFDA/PI warnings and contraindications for romosozumab are not available in this evidence pack (`DG001`), which blocks a formal S1 safety review — this must be resolved (e.g. via TGA PI, since the drug is TGA-unregistered, or via the equivalent approved-market PI such as US/EU labelling) before clinical use is considered.
- **Signal from cited literature (not a formal DDI/warning source)**: advanced CKD (eGFR <30 mL/min) patients on anti-sclerostin therapy show a higher reported rate of hypocalcaemia (PMID 34822428).
- **Signal from cited literature**: a dedicated cardiovascular safety analysis in CKD patients exists (PMID 36330828) — romosozumab carries a known class concern around cardiovascular events that should be specifically reviewed once formal PI/warning data is obtained.
- A formal drug-interaction database query returned no results (`not_found`) — this should not be read as "no interactions confirmed," only that none were retrievable in this query.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (limited to osteoporosis management in patients with impaired renal function/CKD; **Hold** on the other 9 screened candidates)

**Rationale:**
The renal-impairment candidate is supported by a dedicated Phase 1 PK/safety trial plus multiple post-hoc RCT subgroup analyses and a meta-analysis (L2), and represents a population-safety extension of an already-established mechanism rather than a mechanistically speculative new indication. All other candidates in this pack are either unsupported by any trial/literature evidence (L5) or rest on single case reports/preclinical signals (L4) — several (e.g. "obsolete vitamin D deficiency," Worth syndrome) are mechanistically implausible or contraindicated and should not be pursued.

**To proceed, the following is needed:**
- Resolve the Blocking data gap: obtain TFDA/PI (or equivalent overseas PI, given the drug is not TGA-registered) warnings and contraindications before any S1 safety sign-off
- Confirm official mechanism-of-action documentation via DrugBank/manufacturer labelling (currently a data gap)
- Formal DDI screening (current query returned no data)
- For the renal-impairment indication specifically: monitor hypocalcaemia and cardiovascular risk parameters per the flagged literature signals, particularly in eGFR <30 mL/min patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

