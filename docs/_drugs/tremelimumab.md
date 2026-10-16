---
layout: default
title: Tremelimumab
parent: Model Prediction Only (L5)
nav_order: 752
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Tremelimumab: predicted new indication Diabetic cataract (evidence level L5). Approved use: Not stated in the ARTG data compiled for this report. Published pharm…"
---

# Tremelimumab
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

# Tremelimumab: From Hepatocellular Carcinoma (Anti-CTLA-4 Immunotherapy) to Diabetic Cataract

## One-Sentence Summary

Tremelimumab is an anti-CTLA-4 monoclonal antibody, an immune checkpoint inhibitor used in cancer treatment. The TxGNN model predicts it may be effective for **diabetic cataract**, but there are **0 clinical trials** and **0 publications** supporting this prediction, and the data compiled for this report found no plausible biological link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the ARTG data compiled for this report. Published pharmacology sources describe use in unresectable hepatocellular carcinoma (in combination with durvalumab). |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 98.49% |
| Evidence Level | L5 (model prediction only) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled record. Based on known pharmacology, tremelimumab is a monoclonal antibody that binds CTLA-4 (CD152) and blocks its interaction with CD80/CD86. This releases an inhibitory brake on T-cell activation and enhances antitumour immunity.

The prediction is difficult to justify biologically. Diabetic cataract is driven by hyperglycaemia-related processes in the lens, such as polyol pathway activation, oxidative stress and protein glycation. CTLA-4 blockade does not address any of these. The high TxGNN score appears to be a knowledge-graph artefact. Nine other cataract subtypes (mature, immature, senile, cortical and others) received near-identical scores of about 98.2-98.4%, which suggests shared graph neighbours rather than disease-specific biology.

There are also reasons to expect harm rather than benefit:
- Checkpoint inhibitors can cause ocular immune-related adverse events, such as uveitis.
- They can induce autoimmune diabetes, which is a concern in a diabetic population.

Other top-ranked predictions are similarly unsupported: diabetic retinopathy (98.19%), senile cataract (98.33%), and several rare cataract types. None has trial or literature evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 15090F | Imjudo | Solution concentrate for I.V. infusion, 300 mg in 15 mL | Not available in the compiled data |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-CTLA-4 monoclonal antibody), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the PI warnings and precautions |
| Monitoring Items | Please refer to the PI. Immune-related adverse events are typically monitored through liver, thyroid and other endocrine function tests, and blood glucose. |
| Handling Protection | Please refer to the PI and local institutional policy for handling of parenteral oncology products |

---

## Safety Considerations

- **Drug Interactions**: The only record compiled is a pharmacology target entry (CTLA-4/CD152), which is not a clinical drug-drug interaction. No clinically graded interactions were identified.
- **Class-related concerns relevant to this prediction** (from the repurposing assessment, not label text):
  - Ocular immune-related adverse events, including uveitis.
  - Autoimmune diabetes.
  - Rare immune-related endocrinopathies.

Warnings and contraindications from the TGA-approved Product Information were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a computational score with no clinical trials or literature, and no plausible mechanism links CTLA-4 blockade to lens opacification. The known toxicity profile (ocular and endocrine immune-related adverse events) and the availability of effective surgical treatment for cataract make the risk-benefit balance unfavourable.

**To proceed, the following is needed:**
- Mechanistic evidence, such as preclinical lens or diabetic eye models, showing a role for CTLA-4 or T-cell checkpoint signalling in cataract formation
- Confirmed mechanism of action data and the approved indication text from the TGA PI
- Warnings and contraindications from the PI to enable safety screening
- Any clinical or observational data on ocular outcomes in diabetic patients treated with checkpoint inhibitors
- Evaluation of route compatibility, since the only Australian presentation is an intravenous infusion and a systemic route for a surgically treatable eye condition is difficult to justify
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

