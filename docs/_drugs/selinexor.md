---
layout: default
title: Selinexor
parent: Model Prediction Only (L5)
nav_order: 665
evidence_level: L5
indication_count: 10
---

# Selinexor
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

# Selinexor: From an Unspecified Original Indication to Drug-Induced Osteoporosis

## One-Sentence Summary

Selinexor (Xpovio) is an oral inhibitor of exportin-1 (XPO1) that is marketed in Australia. The approved indication text was not available in the data compiled for this report.
The TxGNN model ranks **drug-induced osteoporosis** as its top prediction, but **no clinical trials and no publications** support it.
The evidence is model prediction only, so the recommendation is **Hold**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.22% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Selinexor is known as an XPO1 (exportin-1, also called CRM1) inhibitor. It blocks nuclear export of tumour-suppressor proteins and has been developed as an anticancer agent, mainly in haematological malignancies.

No established mechanistic link between XPO1 inhibition and bone metabolism or drug-induced osteoporosis is supported by the data. The high TxGNN score (99.22%) is not corroborated by any trial or publication. It should be treated as a hypothesis only.

Other lower-ranked predictions are mostly oncology indications, which are more consistent with selinexor's known biology. The most clinically developed of these is squamous cell lung carcinoma, where two selinexor trials exist but neither produced usable results. None of them is the lead prediction assessed here.

## Clinical Trial Evidence

Currently no related clinical trials registered for drug-induced osteoporosis.

## Literature Evidence

Currently no related literature available for drug-induced osteoporosis.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13085Q | Xpovio | Tablet 20 mg (oral) | Not available in the compiled data |

The licence is a valid single-ingredient product. Note that the licence number was supplied in this format and could not be verified against the register.

## Cytotoxicity

Selinexor is an anticancer agent, but the compiled data contain no cytotoxicity details. Please refer to the Product Information (PI) warnings and precautions. Selinexor is an XPO1 inhibitor (targeted therapy), not a conventional cytotoxic, so handling and monitoring requirements should be confirmed in the PI.

## Safety Considerations

No label warnings or contraindications were available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for safety information.

**Drug interactions:** 81 interactions were identified in the DDInter database. Examples of those flagged **Major** include:
- Deferiprone
- Samarium (153Sm) lexidronam
- Adalimumab
- Baricitinib
- Certolizumab pegol
- Cladribine
- Clozapine

Examples flagged **Moderate** include strontium chloride Sr-89, roflumilast, chloramphenicol, zidovudine, azathioprine, anakinra and several vaccines. Many of the listed agents are immunosuppressive or myelosuppressive, so concurrent use needs careful review. Only 20 of the 81 interactions were visible in the data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone. There are no trials or publications for drug-induced osteoporosis, and no plausible mechanistic link to bone metabolism is supported by the data. A key safety data gap (label warnings and contraindications) also remains unresolved.

**To proceed, the following is needed:**
- The approved indication text and Product Information (warnings and contraindications) for Xpovio, from the TGA/PBS sources
- Mechanism of action data (e.g. from DrugBank)
- Preclinical or mechanistic evidence linking XPO1 inhibition to bone metabolism
- A targeted literature search for selinexor and bone effects or osteoporosis
- A benefit-risk review given the drug's toxicity profile and the large number of interactions
- Consideration of better-supported alternative indications (for example, further evaluation of the lung carcinoma trial data) before investing in this prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

