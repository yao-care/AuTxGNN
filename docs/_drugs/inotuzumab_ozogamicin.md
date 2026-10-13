---
layout: default
title: Inotuzumab Ozogamicin
parent: Model Prediction Only (L5)
nav_order: 377
evidence_level: L5
indication_count: 10
---

# Inotuzumab Ozogamicin
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

# Inotuzumab ozogamicin: From B-Cell Acute Lymphoblastic Leukaemia to Drug-Induced Osteoporosis

## One-Sentence Summary

Inotuzumab ozogamicin (Besponsa) is a CD22-directed antibody-drug conjugate that is marketed in Australia for B-cell malignancy treatment.
The TxGNN model predicts it may be effective for **drug-induced osteoporosis** (score 98.2%), but there are currently **0 clinical trials** and **0 publications** that support this prediction.
This is a model-only prediction (Evidence Level L5) and the recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Australian registration data compiled for this report (the drug is a CD22-directed antibody-drug conjugate used in relapsed/refractory B-cell acute lymphoblastic leukaemia, per the literature) |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 98.24% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the data compiled for this report. Based on known information, inotuzumab ozogamicin is an anti-CD22 monoclonal antibody linked to calicheamicin, a DNA-damaging cytotoxic payload. After binding to CD22-expressing B-cells, the complex is internalised and the payload causes double-strand DNA breaks and cell death.

On current evidence the prediction is **not mechanistically plausible**. CD22 is a B-cell marker, and nothing connects this mechanism to bone metabolism. The high TxGNN score reflects a pattern in the knowledge graph, not clinical or laboratory evidence. A cytotoxic drug with known myelosuppressive and hepatotoxic effects would also be an unusual choice for a chronic, non-malignant bone condition.

Other predictions generated for this drug (HER2-positive and other breast cancer subtypes, severe non-proliferative diabetic retinopathy, platelet release disorder, pseudo-von Willebrand disease and infectious bovine rhinotracheitis) also lack a plausible mechanistic rationale and have no supporting trials or literature. The bovine disease is a veterinary condition and is most likely a knowledge-graph artefact.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for drug-induced osteoporosis.

---

## Literature Evidence

Currently no related literature available for drug-induced osteoporosis.

Note: Publications retrieved for the lower-ranked prediction (luminal breast tumours) all concern inotuzumab ozogamicin in B-cell acute lymphoblastic leukaemia. They support its existing use (for example, the Phase 3 INO-VATE study, [PMID 30920645](https://pubmed.ncbi.nlm.nih.gov/30920645/)) and are not repurposing evidence.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Licence 11668D | Besponsa | Powder for I.V. infusion 1 mg | Not stated in the data compiled |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Antibody-drug conjugate with a cytotoxic payload (calicheamicin), targeted therapy |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions (myelosuppression and thrombocytopenia are recognised concerns for this class) |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI; typically includes full blood count and liver function |
| Handling Protection | Follow local cytotoxic drug handling requirements |

---

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 interacting drugs, and 20 were available for review. Most are Moderate, including famotidine, loperamide, bisacodyl, clarithromycin, levofloxacin, palonosetron, granisetron, and several laxatives and bowel preparations. Two are classed as **Major**: **dolasetron** and **cisapride**. Metronidazole is classed as Minor. Many of the flagged drugs are associated with QT prolongation or electrolyte disturbance.

For warnings and contraindications, please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-model score. There are no clinical trials or publications, and no plausible link between CD22-targeted cytotoxic therapy and bone loss. The safety profile also argues against use in a chronic non-malignant condition.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis connecting the drug to bone metabolism, plus supporting preclinical data
- Mechanism-of-action data and the approved indication text from the TGA Product Information
- Warnings and contraindications from the PI, to complete the safety screening
- Any registered clinical studies in the proposed indication, including on ANZCTR
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

