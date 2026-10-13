---
layout: default
title: Romosozumab
parent: Model Prediction Only (L5)
nav_order: 648
evidence_level: L5
indication_count: 10
---

# Romosozumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Romosozumab: From Postmenopausal Osteoporosis to Obsolete Vitamin D Deficiency

## One-Sentence Summary

Romosozumab is an anti-sclerostin antibody originally used to treat osteoporosis in postmenopausal women.
The TxGNN model's top-ranked prediction is **"obsolete vitamin D deficiency"**, but there are **0 clinical trials** and **0 publications** supporting it. The signal is likely an artefact of the knowledge graph rather than a real therapeutic opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Postmenopausal osteoporosis; osteoporosis (from knowledge-graph indication data, as no approved indication text was available for the ARTG entry) |
| Predicted New Indication | Obsolete vitamin D deficiency |
| TxGNN Prediction Score | 97.83% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, romosozumab is a monoclonal antibody that inhibits sclerostin. This increases bone formation and reduces bone resorption, and its efficacy in osteoporosis is established.

The link to the predicted indication is weak. Romosozumab does not correct vitamin D status. It acts on bone-forming pathways, not on vitamin D supply or metabolism. The disease term is also flagged as obsolete in the ontology, so the high score probably reflects shared bone-and-mineral-metabolism annotations in the knowledge graph rather than a real therapeutic opportunity. The prediction should not be treated as a credible repurposing candidate on its own.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form |
|---------|------|------|
| ARTG 12301K | Evenity | Injection 105 mg in 1.17 mL single use pre-filled syringe |

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (not taken from label text): hypercalcaemia, nephrocalcinosis and phosphorus metabolism disease.
- **Drug Interactions**: 29 interactions were recorded. The detailed list covers 20 drugs:
  - **Major**: etelcalcetide.
  - **Moderate**:
    - Systemic corticosteroids, such as hydrocortisone, prednisone, prednisolone, methylprednisolone, dexamethasone, betamethasone, triamcinolone, budesonide, deflazacort and fludrocortisone.
    - Anti-angiogenic and oncology agents, such as bevacizumab, ramucirumab, axitinib, pazopanib, cabozantinib, regorafenib, dasatinib, lenalidomide and pomalidomide.

Label-based warnings and contraindications were not available for this report. Please refer to the TGA-approved Product Information (PI) for full safety information, including the cardiovascular warning and hypocalcaemia risk.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no trial or literature support and no plausible mechanism. The disease term is obsolete, so this looks like a knowledge-graph artefact rather than a real opportunity.

**To proceed, the following is needed:**
- Nothing further is recommended for this prediction unless a credible mechanistic rationale emerges.
- Label-based safety data (PI warnings and contraindications) and mechanism of action data from DrugBank, for any future evaluation.

**Other predictions for this drug with more evidence:**
- **Osteoporosis in patients with impaired renal function** (score 91.5%, Evidence Level L3, Proceed with Guardrails).
  - Supporting evidence includes a completed Phase 1 study (NCT01833754, n=24), post hoc analyses of the FRAME and ARCH Phase 3 trials in mild-to-moderate CKD, and a meta-analysis across CKD stages.
  - Evidence in advanced CKD (stages 4-5, dialysis) is limited. Reviews raise concerns about adynamic bone disease, hypocalcaemia and cardiovascular risk.
  - Suggested guardrails: restrict to mild-to-moderate impairment, correct calcium and vitamin D and exclude CKD-MBD before treatment, monitor calcium, and screen for prior myocardial infarction or stroke.
- **Pregnancy- and lactation-associated osteoporosis** (score 92.9%, Evidence Level L4, Research Question).
  - Evidence is limited to case reports and case series, plus a 2026 international position statement.
  - Use during pregnancy or lactation is not established. Any use would be confined to the postpartum, non-lactating setting, with cardiovascular risk screening.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

