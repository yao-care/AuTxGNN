---
layout: default
title: Eribulin
parent: 僅模型預測 (L5)
nav_order: 200
evidence_level: L5
indication_count: 10
---

# Eribulin
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

# Eribulin: From Metastatic Breast Cancer to Autosomal Recessive Familial Mediterranean Fever

## One-Sentence Summary

Eribulin (brand name Halaven) is an internationally approved microtubule dynamics inhibitor used for metastatic breast cancer and unresectable liposarcoma, but is currently not registered with the TGA in Australia.
The TxGNN model predicts it may be effective for **Autosomal Recessive Familial Mediterranean Fever (FMF)**, with a prediction score of **99.82%**.
However, **no clinical trials and no publications** currently support this specific direction, placing this prediction at the lowest evidence tier — model prediction only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Metastatic breast cancer; unresectable or metastatic liposarcoma (based on international approvals — FDA, EMA, PMDA) |
| Predicted New Indication | Autosomal Recessive Familial Mediterranean Fever |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 — Model prediction only, no actual studies |
| Australia Market Status | Not marketed (no ARTG registration) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Eribulin (Halaven, DB08871) is a fully synthetic analogue of halichondrin B, a natural product isolated from the marine sponge *Halichondria okadai*. Although detailed mechanism of action data was not captured in this Evidence Pack, eribulin is well established in the scientific literature as a **non-taxane microtubule dynamics inhibitor**: it binds selectively to the plus ends of growing microtubules, suppresses microtubule dynamic instability, and sequesters free tubulin into non-productive aggregates — ultimately inducing mitotic block and apoptosis in rapidly dividing cells.

Autosomal recessive familial Mediterranean fever (AR-FMF) is a hereditary autoinflammatory condition caused by biallelic loss-of-function mutations in the *MEFV* gene (encoding pyrin), leading to dysregulated NLRP3/pyrin inflammasome activation, excessive IL-1β release, and recurrent episodes of fever and polyserositis. The mechanistic bridge to a cytotoxic anti-tubulin agent may appear counterintuitive, but is worth noting: **colchicine — the gold-standard treatment for FMF — is itself a microtubule inhibitor**. Colchicine suppresses neutrophil chemotaxis and NLRP3 inflammasome priming by disrupting tubulin polymerisation. TxGNN's knowledge graph likely identifies this shared mechanistic class and hypothesises that eribulin's potent microtubule-disrupting activity could similarly modulate neutrophil migration and inflammasome signalling in FMF.

While this is a biologically plausible hypothesis worthy of preclinical exploration, **no clinical or laboratory studies have been conducted to test eribulin specifically in FMF**. More critically, eribulin's cytotoxic potency vastly exceeds that of colchicine, and applying it in a non-oncology population raises serious safety concerns. Established safer alternatives (colchicine, IL-1 inhibitors such as anakinra and canakinumab) already exist for FMF management.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for eribulin in autosomal recessive familial Mediterranean fever.

---

## Literature Evidence

Currently no related literature available for eribulin in autosomal recessive familial Mediterranean fever.

---

## Australia Market Information

Eribulin is **not registered with the Australian Therapeutic Goods Administration (TGA)** and holds no ARTG entries. It is approved in the United States (FDA, 2010), the European Union (EMA, 2011), and Japan (PMDA) for metastatic breast cancer, and subsequently for unresectable or metastatic liposarcoma. Any clinical use in Australia would require a TGA Special Access Scheme (SAS Category B) or Authorised Prescriber pathway.

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|-------------|--------------|-------------|---------------------|
| — | No ARTG entries | — | Not applicable |

---

## Cytotoxicity

Eribulin is a cytotoxic antineoplastic agent (halichondrin class microtubule inhibitor).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — non-taxane microtubule dynamics inhibitor (halichondrin analogue) |
| Myelosuppression Risk | **High** — neutropenia is the primary dose-limiting toxicity; Grade 3/4 neutropenia reported in approximately 50% of patients in pivotal breast cancer trials; febrile neutropenia has been fatal |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Full Blood Count with differential (ANC mandatory prior to each cycle); liver function tests; renal function (eGFR); QTc interval on ECG prior to treatment and during therapy |
| Handling Protection | Must be prepared and administered in accordance with cytotoxic drug handling regulations — appropriate PPE, biological safety cabinet, cytotoxic waste disposal protocol required |

---

## Safety Considerations

No Australian PI exists as eribulin is not TGA-registered. Please refer to the FDA-approved US Prescribing Information or EMA Summary of Product Characteristics for full safety details. Key considerations from internationally available prescribing information include:

- **Neutropenia**: Severe and potentially fatal myelosuppression is the most common serious adverse event. Dose delays and reductions are required for ANC < 1.0 × 10⁹/L.
- **Peripheral Neuropathy**: Sensory and motor neuropathy are common; pre-existing peripheral neuropathy may be significantly worsened.
- **QT Prolongation**: Eribulin prolongs the QT interval. Caution is required in patients with hypokalaemia, hypomagnesaemia, congenital long QT syndrome, or concurrent use of other QT-prolonging agents.
- **Embryo-Foetal Toxicity**: Contraindicated in pregnancy; effective contraception is required during treatment and for a period after the last dose.
- **Hepatic and Renal Impairment**: Dose reductions are required for moderate-to-severe hepatic impairment and mild-to-moderate renal impairment; pharmacokinetics are significantly altered.

> **Additional note for FMF context**: Applying eribulin in a non-oncology population with FMF would demand particular scrutiny of the benefit–risk ratio. The myelosuppression and neurotoxicity profile is generally considered unacceptable when colchicine and IL-1 inhibitors are available, well-tolerated, and effective alternatives.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns a high prediction score (99.82%), this reflects the model's confidence in a mechanistic hypothesis — not clinical evidence. There are no published studies or registered trials of eribulin in FMF, and the drug's severe cytotoxic profile represents a significant safety barrier for a non-cancer population in whom effective, better-tolerated treatments already exist.

**To proceed, the following is needed:**
- Preclinical proof-of-concept data in FMF models (e.g., pyrin-mutant *Mefv* knock-in mice) demonstrating meaningful anti-inflammatory activity at sub-cytotoxic concentrations
- Mechanistic studies directly comparing eribulin's effect on neutrophil migration, NLRP3/pyrin inflammasome priming, and IL-1β secretion against colchicine, to characterise the therapeutic window
- Formal safety/toxicology assessment and therapeutic index modelling for anti-inflammatory versus cytotoxic dose ranges
- Regulatory and ethics consultation regarding feasibility of any Phase 0/first-in-disease study in an FMF population
- TGA Special Access Scheme or Authorised Prescriber registration prior to any compassionate use in Australia

> **Note on other TxGNN predictions:** Among the top-10 predictions in this Evidence Pack, **fibroblastic neoplasm (Rank 8)** carries substantially stronger supporting evidence — 1 completed Phase 2 clinical trial (ERASING, NCT03840772) and 8 peer-reviewed publications — and may represent a more clinically actionable repurposing opportunity for eribulin in Australia. A separate focused evaluation of this indication is recommended.

---

*This report is generated for research purposes only and does not constitute medical advice. Repurposing candidates require clinical validation before application. All content is subject to YMYL (Your Money or Your Life) disclaimer: findings are intended for healthcare professional review and must not be applied in clinical practice without appropriate regulatory and clinical oversight.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

