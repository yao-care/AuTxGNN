---
layout: default
title: Toripalimab
parent: Model Prediction Only (L5)
nav_order: 741
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Toripalimab: predicted new indication Mixed-type autoimmune haemolytic anaemia (evidence level L5). Approved use: Not available in the data compiled for this report"
---

# Toripalimab
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

# Toripalimab: From an Unspecified Original Indication to Mixed-Type Autoimmune Haemolytic Anaemia

## One-Sentence Summary

Toripalimab is a PD-1 blocking antibody registered in Australia as Zytorvi, but the data compiled for this report do not include its approved indication text.
The TxGNN model predicts it may be effective for **mixed-type autoimmune haemolytic anaemia**, but there are **0 clinical trials** and **0 publications** supporting this prediction.
The prediction is **biologically implausible** and carries a safety concern, because PD-1 blockade is known to cause immune-related haemolysis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the ARTG indication text is blank; the FDA has approved toripalimab for nasopharyngeal carcinoma) |
| Predicted New Indication | Mixed-type autoimmune haemolytic anaemia |
| TxGNN Prediction Score | 93.76% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the compiled data. Based on known pharmacology, toripalimab is a humanised antibody that blocks the binding of PD-1 (CD279) to its ligands PD-L1 and PD-L2 (IC50 around 3.0 nM). This releases the brakes on T-cell activity and enhances immune attack on tumours.

That mechanism argues **against** the prediction. In autoimmune haemolytic anaemia, autoantibodies destroy red blood cells. Enhancing immune activation would be expected to worsen the disease, not treat it. Autoimmune haemolytic anaemia is a recognised immune-related adverse event of checkpoint inhibitors.

The high TxGNN score most likely reflects a shared disease-gene association in the knowledge graph rather than a true therapeutic opportunity. The other top-ranked predictions (idiopathic aplastic anaemia, dermatitis, paroxysmal nocturnal haemoglobinuria, drug-induced and neonatal autoimmune haemolytic anaemia, proteinuria, acne keloid, primary CD59 deficiency, amyopathic dermatomyositis) show the same pattern. Each has either no supporting evidence, no plausible mechanistic link, or evidence pointing towards harm.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for mixed-type autoimmune haemolytic anaemia.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 15125C | Zytorvi | Solution concentrate for I.V. infusion, 240 mg in 6 mL | Not stated in the compiled data |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-1 monoclonal antibody) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI; immune-related adverse events (including haematological, hepatic, endocrine and skin toxicity) are generally monitored for checkpoint inhibitors |
| Handling Protection | Please refer to the PI and local institutional policy |

---

## Safety Considerations

- **Immune-related haemolysis:** Autoimmune haemolytic anaemia is a recognised immune-related adverse event of checkpoint inhibitors. Use of toripalimab in patients with existing autoimmune haemolytic disease raises a significant safety concern.
- **Cutaneous reactions:** Published case reports and a case series describe severe skin reactions with PD-1 inhibitors, including SJS/TEN and lichenoid drug eruption.
- **Myositis:** Checkpoint inhibitors have been associated with inducing myositis and dermatomyositis.
- **Drug interactions:** The only interaction record is the drug's pharmacological target (PD-1, PDCD1), which is not a clinical drug-drug interaction.

For full warnings and contraindications, please refer to the TGA-approved Product Information (PI).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials or literature. The known mechanism of PD-1 blockade points towards worsening autoimmune haemolysis, so there is no rationale for benefit and a clear safety signal.

**To proceed, the following is needed:**
- A credible mechanistic rationale showing how PD-1 blockade could benefit autoimmune haemolysis (none is apparent at present)
- Preclinical or case-based evidence supporting any therapeutic effect
- The TGA-approved indication text and Product Information for Zytorvi, including warnings and contraindications
- Detailed mechanism of action data from DrugBank
- A full safety assessment of immune-related haemolytic events before any further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

