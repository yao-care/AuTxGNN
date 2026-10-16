---
layout: default
title: Cholecalciferol
parent: Model Prediction Only (L5)
nav_order: 158
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
description: "Cholecalciferol: predicted new indication Familial isolated hypoparathyroidism due to impaired PTH secretion (evidence level L5). Approved use: Osteoporosis, postmenopausal osteoporosis, vitamin D de…"
monitor_inn: "cholecalciferol"
predicted_indications: ["familial isolated hypoparathyroidism due to impaired PTH secretion", "acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "Dahlberg-Borer-Newcomer syndrome", "hypophosphatemic rickets", "renal osteodystrophy", "renal tubular acidosis"]
---

# Cholecalciferol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Cholecalciferol: From Osteoporosis and Vitamin D Deficiency to Renal Osteodystrophy

## One-Sentence Summary

Cholecalciferol (vitamin D3) is used to treat vitamin D deficiency and related bone and mineral disorders, including osteoporosis, rickets and osteomalacia. The TxGNN model predicts it may be useful for **familial isolated hypoparathyroidism** (highest score), but the best-supported prediction is **renal osteodystrophy**, with **2 clinical trials** and **20 publications** pointing in this direction. Most other predictions rest on model output alone or on non-specific literature.

---

## Quick Overview

The report was written for the top-ranked prediction. Because renal osteodystrophy is the only prediction with trial evidence, it is shown alongside.

| Item | Content |
|------|------|
| Original Indication | Osteoporosis, postmenopausal osteoporosis, vitamin D deficiency, rickets, osteomalacia, hypoparathyroidism (the ARTG entry lists no indication text) |
| Predicted New Indication (rank 1) | Familial isolated hypoparathyroidism due to impaired PTH secretion |
| TxGNN Prediction Score (rank 1) | 99.79% |
| Evidence Level (rank 1) | L5 |
| Best-Supported Prediction | Renal osteodystrophy (score 99.11%, Evidence Level L2) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Rank 1: Hold. Renal osteodystrophy: Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, cholecalciferol is a pro-hormone. It is converted in the liver to 25-hydroxyvitamin D, then in the kidney to active calcitriol. Calcitriol promotes intestinal absorption of calcium and phosphate and supports bone mineralisation and PTH regulation.

**Rank 1 (familial isolated hypoparathyroidism):** Hypoparathyroidism is already among cholecalciferol's original indications, so the link is plausible. However, the score is a model prediction only, with no trials or literature. In practice, active vitamin D analogues (calcitriol, alfacalcidol) are used rather than native cholecalciferol, because 1-alpha-hydroxylation is PTH-dependent.

**Renal osteodystrophy:** Vitamin D deficiency in chronic kidney disease (CKD) contributes to secondary hyperparathyroidism and bone disease. Cholecalciferol replenishes 25-OH vitamin D, which supports local calcitriol synthesis and may lower PTH. This fits well with its existing bone and mineral indications.

**Other predictions:**
- Acromesomelic dysplasia (Campailla-Martinelli type) and craniofacial conodysplasia: no mechanistic link is evident. These are probably graph-proximity artefacts.
- Dahlberg-Borer-Newcomer syndrome: the retrieved literature is general vitamin D material and does not address this disease.
- Hypophosphataemic rickets: relevant mainly where vitamin D deficiency coexists. Standard care is phosphate plus active vitamin D, or burosumab.
- Renal tubular acidosis: relevant to the bone and mineral complications, not the acidosis itself.

---

## Clinical Trial Evidence

Trials were available only for renal osteodystrophy (the other predictions have none registered in the data compiled).

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00285467](https://clinicaltrials.gov/study/NCT00285467) | Not specified | Completed | 55 | Cholecalciferol vs doxercalciferol for secondary hyperparathyroidism in CKD stages 3-4. The outcome is a PTH surrogate, not bone endpoints. |
| [NCT00752401](https://clinicaltrials.gov/study/NCT00752401) | Phase 3 | Unknown | 200 | VITA-D: randomised, placebo-controlled cholecalciferol in vitamin D-deficient kidney transplant recipients. The population is indirect and no results are reported. |

No ANZCTR identifiers were available in the data compiled.

---

## Literature Evidence

Selected publications for renal osteodystrophy, the best-supported prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34747516](https://pubmed.ncbi.nlm.nih.gov/34747516/) | 2022 | RCT (secondary analysis) | J Bone Miner Res | Cholecalciferol attenuated bone loss in incident kidney transplant recipients (n=193). |
| [35200136](https://pubmed.ncbi.nlm.nih.gov/35200136/) | 2022 | Prospective controlled study | Clin Nephrol | Effect of vitamin D sterols on bone histology in pre-dialysis CKD. |
| [38397979](https://pubmed.ncbi.nlm.nih.gov/38397979/) | 2024 | Clinical study | Biomedicines | Efficacy and safety of high-dose cholecalciferol in haemodialysis patients. |
| [39597015](https://pubmed.ncbi.nlm.nih.gov/39597015/) | 2024 | Observational study | Medicina (Kaunas) | Haemodialysis patients may benefit from cholecalciferol targeting high 25(OH)D. |
| [30274806](https://pubmed.ncbi.nlm.nih.gov/30274806/) | 2019 | Review | Nefrologia | Role of native vitamin D in pre-dialysis CKD remains unclear. |
| [33922902](https://pubmed.ncbi.nlm.nih.gov/33922902/) | 2021 | Review | Nutrients | Vitamin D effects on bone and cardiovascular system in CKD and transplant recipients. |
| [30297082](https://pubmed.ncbi.nlm.nih.gov/30297082/) | 2018 | Workshop report | Am J Kidney Dis | Vitamin D in CKD stages 3-4 remains controversial. |
| [20671739](https://pubmed.ncbi.nlm.nih.gov/20671739/) | 2010 | Review | Kidney Int Suppl | Kidney bone disease and mortality in CKD. |

For hypophosphataemic rickets, the evidence is reviews and case reports (for example [38337700](https://pubmed.ncbi.nlm.nih.gov/38337700/), a 2024 review of rickets types and vitamin D treatment). For renal tubular acidosis it is case reports only, including a report of vitamin D3 overdose in a child with distal tubular acidosis ([14575620](https://pubmed.ncbi.nlm.nih.gov/14575620/)). For the rank 1-3 predictions, no related literature is available. The rank 4 literature is non-specific.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13835E | Fosamax Plus 70 mg/140 mcg | Oral tablet: alendronate sodium 70 mg with colecalciferol 140 micrograms | Not stated in the data compiled |

---

## Safety Considerations

**Contraindications suggested by the knowledge graph** (these are model-derived associations, not label text). Conditions listed include:
- Hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease and hyperparathyroidism
- Kidney disease and liver disease
- Sarcoidosis
- Primary hyperoxaluria
- Several others, such as hypertension, diabetes mellitus and prostate cancer

**Drug interactions:** 56 interactions were identified. Major-level interactions are with other vitamin D compounds and analogues: calcifediol, calcitriol, dihydrotachysterol and doxercalciferol (risk of additive hypercalcaemia). Moderate-level interactions include:
- Thiazide diuretics (bendroflumethiazide, chlorothiazide, chlorthalidone)
- Barbiturates and carbamazepine
- Bile acid sequestrants (cholestyramine, colestipol, colesevelam)
- Digoxin and digitoxin

**Specific cautions from the literature:**
- Unmonitored vitamin D can worsen nephrocalcinosis and hypercalciuria in distal renal tubular acidosis.
- In CKD, serum calcium, phosphate and PTH should be monitored to avoid hypercalcaemia, adynamic bone disease and vascular calcification.
- The only registered product is a combination with alendronate. Safety of the combination must be considered separately, so please refer to the TGA-approved Product Information (PI).

---

## Conclusion and Next Steps

**Decision: Hold for the rank 1 prediction (familial isolated hypoparathyroidism); Proceed with Guardrails for renal osteodystrophy**

**Rationale:**
- The top-scoring prediction has no supporting trials or literature (L5), and standard care uses active vitamin D analogues. Ranks 2-4 have no credible mechanistic link.
- Renal osteodystrophy has a coherent mechanism, one completed trial and supporting literature. The evidence is moderate and indirect: there is no completed Phase 3 trial directly on renal osteodystrophy outcomes, so L2 is assigned conservatively. Hypophosphataemic rickets and renal tubular acidosis remain research questions (L4).

**To proceed, the following is needed:**
- Results from the VITA-D trial (NCT00752401), or a completed Phase 3 trial with bone endpoints in CKD
- Detailed mechanism of action data
- Package insert warnings and contraindications for the Australian product, because current safety data are incomplete
- A monitoring plan (calcium, phosphate, PTH) stratified by CKD stage
- Clarification of the role of native cholecalciferol versus active vitamin D analogues, and of the suitability of the alendronate combination product for these populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

