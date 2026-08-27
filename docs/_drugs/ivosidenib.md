---
layout: default
title: Ivosidenib
parent: 僅模型預測 (L5)
nav_order: 373
evidence_level: L5
indication_count: 10
---

# Ivosidenib
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

# Ivosidenib: From IDH1-Mutated AML to Myelodysplastic/Myeloproliferative Disease

## One-Sentence Summary

> Ivosidenib (TIBSOVO) is a targeted oral IDH1 inhibitor, FDA-approved in the United States for IDH1-mutated Acute Myeloid Leukaemia (AML) and cholangiocarcinoma, but not currently registered with Australia's TGA.
> The TxGNN model predicts it may be effective for **Myelodysplastic/Myeloproliferative Disease (MDS/MPN)** in IDH1-mutated patients,
> with **5 clinical trials** currently supporting this direction — a prediction independently corroborated by the FDA's August 2023 approval of Ivosidenib for IDH1-mutated MDS.

> **Note on TxGNN ranking:** The model's top-ranked prediction (Rank 1: bulbar polio, score 99.31%) and several additional high-scoring entries (Ranks 4–6, 9–10) were assessed as model false positives with no biological connection to the IDH1 metabolic pathway. This report focuses on the highest-evidenced, mechanistically valid prediction: **Rank 7 — Myelodysplastic/Myeloproliferative Disease** (score 98.56%, Evidence Level L2), which warrants clinical evaluation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | IDH1-mutated AML — FDA-approved; not TGA-registered in Australia |
| Predicted New Indication | Myelodysplastic/Myeloproliferative Disease |
| TxGNN Prediction Score | 98.56% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data was not available in the current Evidence Pack. Based on well-established published pharmacology, however, Ivosidenib is a potent, selective, orally administered inhibitor of the mutant isocitrate dehydrogenase 1 (IDH1) enzyme — specifically targeting the recurrent R132 gain-of-function mutations found in haematological malignancies and some solid tumours. In normal cells, IDH1 converts isocitrate to α-ketoglutarate. In IDH1-mutated cells, the enzyme aberrantly produces the oncometabolite 2-hydroxyglutarate (2-HG), which competitively inhibits α-ketoglutarate-dependent dioxygenases — including TET2 (a DNA demethylase) and histone demethylases. The resulting epigenetic hypermethylation silences differentiation genes, blocks normal haematopoietic maturation, and drives clonal expansion. Ivosidenib suppresses mutant IDH1, reduces 2-HG accumulation, and permits partial re-differentiation of malignant myeloid progenitors.

IDH1 mutations occur in approximately 3–5% of MDS patients and in a similar proportion of Chronic Myelomonocytic Leukaemia (CMML) cases — the most common MDS/MPN overlap syndrome. Because the oncogenic mechanism in IDH1-mutated MDS/MPN is identical to that in AML (2-HG-driven epigenetic block of differentiation), the therapeutic rationale for Ivosidenib is mechanistically robust and represents a direct extension of its proven AML biology rather than a speculative extrapolation.

Critically, the FDA validated this logic in August 2023 when it approved Ivosidenib (in combination with azacitidine) for IDH1-mutated MDS — independently corroborating the TxGNN model's prediction. Multiple ongoing Phase 1b/2 and Phase 2 clinical trials provide further clinical data in this disease context. Ivosidenib's absence from the TGA register means Australian patients with IDH1-mutated MDS/MPN currently lack access to a therapy with proven international regulatory standing, representing a meaningful unmet clinical need.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT03471260](https://clinicaltrials.gov/study/NCT03471260) | Phase 1b/2 | Recruiting | 96 | Ivosidenib + Venetoclax ± Azacitidine in IDH1-mutated haematologic malignancies (including MDS/MPN); evaluates optimal dosing, safety, and preliminary efficacy of the combination |
| [NCT04493164](https://clinicaltrials.gov/study/NCT04493164) | Phase 2 | Recruiting | 30 | CPX-351 liposomal chemotherapy + Ivosidenib in IDH1-mutated AML or high-risk MDS; directly investigates Ivosidenib in the MDS disease context |
| [NCT02074839](https://clinicaltrials.gov/study/NCT02074839) | Phase 1 | Recruiting | 291 | Foundational dose-escalation and expansion study of Ivosidenib (AG-120) across IDH1-mutated haematologic malignancies; established the safety profile, PK, and PD characteristics that underpin all subsequent trials |
| [NCT04250051](https://clinicaltrials.gov/study/NCT04250051) | Phase 1 | Active, not recruiting | 2 | Ivosidenib + FLAG chemotherapy (fludarabine, cytarabine, filgrastim) in relapsed/refractory IDH1-mutated AML; very small enrolment (n=2); confirms feasibility in heavily pre-treated myeloid disease |
| [NCT04603001](https://clinicaltrials.gov/study/NCT04603001) | Phase 1 | Active, not recruiting | 260 | LY3410738 — a next-generation covalent IDH1/2 inhibitor (not Ivosidenib) — in IDH1/2-mutated haematologic malignancies; demonstrates ongoing industry investment in IDH1-targeted therapy across the MDS/MPN spectrum |

---

## Literature Evidence

Currently no related literature is available in the queried evidence database for Myelodysplastic/Myeloproliferative Disease. Australian prescribers are encouraged to search PubMed directly using the terms "Ivosidenib MDS", "AG-120 myelodysplastic syndrome", and "IDH1 inhibitor CMML" for current publications.

---

## Australia Market Information

Ivosidenib is not registered on the Australian Register of Therapeutic Goods (ARTG) and is not commercially available in Australia through standard pharmacy channels. As of the data cutoff date (22 June 2026), there are no ARTG entries for any product containing Ivosidenib.

**Potential access pathways for Australian patients:**

| Pathway | Applicable Scenario |
|---------|-------------------|
| Special Access Scheme — Category B (SAS-B) | Individual patient compassionate/unapproved use; application by treating specialist |
| Authorised Prescriber (AP) Scheme | Suitable if treating multiple eligible patients with IDH1-mutated MDS/MPN at a specialist centre |
| Clinical Trial Enrolment | No Australian-based trials currently identified; consider referral to participating international sites |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — selective oral IDH1 inhibitor (small molecule metabolic enzyme inhibitor; not a conventional cytotoxic) |
| Myelosuppression Risk | Low to moderate; Ivosidenib itself is not directly myelosuppressive; transient cytopenias may occur as part of differentiation syndrome or haematopoietic recovery during treatment response |
| Emetogenicity Classification | Low (oral targeted agent; routine antiemetic prophylaxis generally not required per ASCO/MASCC emetogenicity guidelines) |
| Monitoring Items | FBC with differential (at least weekly for the first 4 weeks, then monthly), liver function tests, renal function, serum electrolytes (K⁺, Mg²⁺), ECG with QTc measurement (baseline, Day 8, monthly thereafter), 2-HG levels if accessible for pharmacodynamic confirmation |
| Handling Protection | Standard oral oncolytic handling precautions apply; no inhalation or injection hazard; handle and dispose per institutional oral chemotherapy/antineoplastic safety policy |

---

## Safety Considerations

No TGA Product Information (PI) is available as Ivosidenib has not been registered in Australia. The following is drawn from the FDA-approved TIBSOVO Prescribing Information (Servier Pharmaceuticals), which must be consulted directly before any prescribing decision.

**Key Warnings (FDA-approved label):**
- **Differentiation Syndrome**: A potentially life-threatening complication — characterised by fever, dyspnoea, acute respiratory distress, hypotension, rapid weight gain, pulmonary infiltrates, and pericardial or pleural effusion — has been reported in up to 19% of patients. Requires prompt systemic corticosteroid therapy (e.g., dexamethasone 10 mg IV twice daily), close haematological monitoring, and possible Ivosidenib interruption until symptoms resolve.
- **QTc Prolongation**: Clinically significant QT interval prolongation has been reported; avoid co-administration with strong QTc-prolonging agents; correct hypokalaemia and hypomagnesaemia prior to and during treatment.
- **Guillain-Barré Syndrome**: Cases reported in clinical trials and post-marketing surveillance; discontinue Ivosidenib if this diagnosis is confirmed.

Please refer to the FDA-approved TIBSOVO Prescribing Information for complete contraindications, drug-drug interaction data, special population guidance, and dosing modifications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
In IDH1-mutated MDS/MPN patients, Ivosidenib directly targets the underlying oncogenic driver via a well-characterised mechanism, and the FDA's 2023 MDS approval independently validates the TxGNN prediction — providing a strong international regulatory precedent to support Australian access applications.

**To proceed, the following is needed:**
- **IDH1 mutation testing**: Mandatory patient selection — Ivosidenib is applicable only to IDH1-mutated MDS/MPN patients (~3–5% of cases); validated NGS or allele-specific PCR for IDH1 R132 mutations is required before treatment initiation
- **TGA access pathway activation**: Lodge an SAS-B application (individual patient) or Authorised Prescriber application with clinical justification citing the FDA 2023 MDS approval; obtain TIBSOVO FDA PI as supporting documentation
- **Safety monitoring protocol**: Pre-treatment differentiation syndrome risk assessment, mandatory ECG and electrolyte baseline, weekly FBC protocol for first 4 weeks, and clear institutional escalation pathway for suspected differentiation syndrome
- **MOA documentation**: Retrieve complete Ivosidenib entry from DrugBank API (DG002 remediation) for inclusion in the prescribing dossier and regulatory submission
- **Haematologist oversight**: All MDS/MPN management with Ivosidenib must be conducted under specialist haematology supervision at a centre experienced in managing haematological malignancies and treatment-related differentiation syndrome
- **Electrolyte optimisation prior to treatment initiation**: Correct K⁺ and Mg²⁺ deficiencies before starting therapy to minimise QTc prolongation risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

