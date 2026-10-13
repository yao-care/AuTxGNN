---
layout: default
title: Benzydamine
parent: Model Prediction Only (L5)
nav_order: 88
evidence_level: L5
indication_count: 10
---

# Benzydamine
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

# Benzydamine: From Local Oropharyngeal Inflammation and Pain to Benign Prostatic Hyperplasia

## One-Sentence Summary

Benzydamine is a locally acting anti-inflammatory and analgesic agent, marketed in Australia as a mouth and throat rinse (Difflam).
The TxGNN model predicts it may be effective for **benign prostatic hyperplasia (BPH)**, with a score of 99.3%,
but **no clinical trials and no publications** currently support this prediction, so it is a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the product is a mouth and throat rinse) |
| Predicted New Indication | Benign prostatic hyperplasia |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Based on general knowledge, benzydamine is a locally acting NSAID-like agent with local anaesthetic and membrane-stabilising properties. It is used as a rinse or spray for painful inflammatory conditions of the mouth and throat.

No mechanistic link between benzydamine and benign prostatic hyperplasia is supported by the data compiled. BPH is mainly driven by hormonal and smooth-muscle mechanisms, and benzydamine's topical anti-inflammatory profile does not clearly map onto these. The high TxGNN score is a computational association only, and the available rinse formulation would not deliver meaningful exposure to the prostate.

For context, the other top-ranked predictions were also reviewed. Most have no supporting evidence (headache disorder, trigeminal autonomic cephalalgia, peripheral arterial disease, female breast carcinoma, toxocariasis, subarachnoid haemorrhage, alopecia). Two have limited indirect signals:
- **Peripheral vascular disease (rank 4, L4):** 1960s–70s reports of topical benzydamine in inflammatory phlebopathies and thrombophlebitis of the lower limbs. This relates to superficial venous inflammation, not peripheral vascular disease in general, and the literature is old and of uncertain quality.
- **Common cold (rank 5, L4):** Recent studies in acute sore throat. This supports symptomatic relief of sore throat, which is an existing use, not treatment of the viral infection itself.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for benign prostatic hyperplasia.

---

## Literature Evidence

Currently no related literature available for benign prostatic hyperplasia.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1121B | Difflam | Mouth and throat rinse containing benzydamine hydrochloride 22.5 mg per 15 mL, 500 mL | Not stated in the data compiled |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No warnings, contraindications or drug interaction records were available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The BPH prediction rests on a model score alone, with no clinical trials, no literature, no established mechanism and no supporting route of exposure. The evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data for benzydamine, and a plausible biological rationale for BPH
- Preclinical or clinical studies in BPH or prostatic inflammation
- Assessment of route and formulation compatibility, since the only Australian product is a mouth and throat rinse
- Product Information warnings, precautions, contraindications and interaction data
- The approved indication text for the ARTG entry
- For the lower-ranked candidates, verification of study design in the sore throat studies and the older venous inflammation reports before treating them as evidence of a new use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

