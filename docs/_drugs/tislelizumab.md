---
layout: default
title: Tislelizumab
parent: Model Prediction Only (L5)
nav_order: 731
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Tislelizumab: predicted new indication Mixed-type autoimmune hemolytic anemia (evidence level L5). Approved use: Not available in the data compiled for this report . Published source…"
---

# Tislelizumab
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

# Tislelizumab: From Oncology Use to Mixed-Type Autoimmune Hemolytic Anemia

## One-Sentence Summary

Tislelizumab (Tevimbra) is an anti-PD-1 antibody used in cancer immunotherapy, with approvals for conditions such as oesophageal squamous cell carcinoma in other jurisdictions.
The TxGNN model predicts it may be effective for **mixed-type autoimmune hemolytic anemia**, but **no clinical trials and no publications** currently support this prediction.
The mechanism of action points in the opposite direction, because PD-1 blockade enhances immune activation and can cause immune-related haemolysis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the ARTG entry has no indication text). Published sources describe oncology uses, including oesophageal squamous cell carcinoma and classical Hodgkin lymphoma in other jurisdictions. |
| Predicted New Indication | Mixed-type autoimmune hemolytic anemia |
| TxGNN Prediction Score | 93.76% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Tislelizumab is known to be a humanised IgG4 monoclonal antibody that blocks PD-1 (PDCD1/CD279). This releases the brake on T-cell activity and so restores anti-tumour immunity.

The prediction is difficult to justify mechanistically. Autoimmune hemolytic anemia is driven by autoantibody-mediated destruction of red cells, and treatment is directed at suppressing the immune response. Enhancing T-cell activity through PD-1 blockade would be expected to worsen autoimmunity, not treat it. Immune checkpoint inhibitors are themselves associated with immune-related haemolytic anaemia.

The high TxGNN score likely reflects a drug-disease association in the knowledge graph rather than a therapeutic relationship. Other top-ranked predictions show the same pattern: idiopathic aplastic anaemia (score 93.76%), dermatitis (93.69%), paroxysmal nocturnal haemoglobinuria (93.67%), drug-induced autoimmune haemolytic anaemia (93.67%), proteinuria (93.07%) and amyopathic dermatomyositis (92.79%). Most are immune-mediated or haematological conditions where PD-1 blockade is expected to be neutral or harmful.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

For context, the other top-ranked predictions (dermatitis and proteinuria) returned only publications describing tislelizumab as a cause of skin and renal adverse events, including Stevens-Johnson syndrome/toxic epidermal necrolysis. None supports a therapeutic role.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14756P | Tevimbra | Solution concentrate for I.V. infusion, 100 mg in 10 mL | Not available in the compiled data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-1 monoclonal antibody), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions. Immune-mediated haematological toxicity, including haemolytic anaemia and agranulocytosis, has been reported with PD-1 inhibitors. |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI. Full blood count, liver, renal and thyroid function are commonly monitored with checkpoint inhibitors. |
| Handling Protection | Please refer to the PI and local institutional policy |

## Safety Considerations

- **Immune-related adverse events:** Published reports describe severe cutaneous reactions with tislelizumab, including Stevens-Johnson syndrome/toxic epidermal necrolysis and DRESS syndrome. They also describe renal toxicity (thrombotic microangiopathy, granulomatosis with polyangiitis) and agranulocytosis.
- **Drug interactions:** The only interaction record is its pharmacological target, PD-1 (PDCD1). No interacting drugs were identified.

Please refer to the TGA-approved Product Information (PI) for formal warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5), with no trials or literature. The mechanism suggests PD-1 blockade could worsen autoimmune haemolysis, and checkpoint inhibitors are known to cause it. The safety signal is directionally opposite to therapeutic benefit.

**To proceed, the following is needed:**
- Mechanistic or preclinical evidence supporting a benefit of PD-1 blockade in autoimmune haemolytic anaemia
- Detailed mechanism of action data
- The approved indication text and the warnings and contraindications from the TGA Product Information
- A review of the immune-related haemolysis risk before any further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

