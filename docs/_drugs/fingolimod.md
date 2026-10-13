---
layout: default
title: Fingolimod
parent: Model Prediction Only (L5)
nav_order: 299
evidence_level: L5
indication_count: 10
---

# Fingolimod
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

# Fingolimod: From Relapsing-Remitting Multiple Sclerosis to Borderline Ovarian Serous Tumour

## One-Sentence Summary

Fingolimod was originally used to treat relapsing-remitting multiple sclerosis.
The TxGNN model predicts it may be effective for **borderline ovarian serous tumour**,
but **no clinical trials and no publications** directly support this prediction. This is a model-only (L5) signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relapsing-remitting multiple sclerosis (approved indication text for the Australian entry is not available) |
| Predicted New Indication | Borderline ovarian serous tumour |
| TxGNN Prediction Score | 94.94% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, fingolimod (FTY720) is a sphingosine-1-phosphate (S1P) receptor modulator. It traps lymphocytes in lymph nodes, which is how it reduces relapses in multiple sclerosis.

S1P signalling and sphingolipid metabolism have been implicated in ovarian epithelial tumour biology, so a link to ovarian neoplasms is plausible. This link is speculative. It rests on general knowledge and not on the evidence compiled here. The predicted disease is also a borderline (low malignant potential) tumour, for which systemic immunomodulation has no established rationale.

Other highly ranked predictions are also ovarian neoplasms (for example ovarian papillary cystadenoma, malignant ovarian Brenner tumour and mucinous ovarian cystadenoma). This suggests the model is picking up proximity to ovarian neoplasms in its knowledge graph, and not a drug-specific mechanism.

Preclinical work exists for a related prediction, "serous neoplasm". It is described in the literature section below.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No publications were found specifically for borderline ovarian serous tumour. The following preclinical reports were found for closely related ovarian predictions (serous neoplasm and ovarian benign neoplasm). They are indirect evidence only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30120964](https://pubmed.ncbi.nlm.nih.gov/30120964/) | 2018 | Preclinical (patient-derived xenograft) | Cancer Letters | FTY720 enhanced the anti-tumour activity of carboplatin and tamoxifen in an ovarian cancer model, including drug-resistant cells |
| [30388910](https://pubmed.ncbi.nlm.nih.gov/30388910/) | 2019 | Preclinical (lung cancer; ovarian cancer cells also tested) | Cancer Biology & Therapy | Fingolimod augmented pemetrexed killing of non-small cell lung cancer cells and overcame resistance to ERBB inhibition; the abstract also notes synergy in ovarian cancer cells |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11818B | Gilenya | Capsule 250 micrograms (as hydrochloride) | Not available in the data compiled for this report |

The only route of administration listed is oral.

## Safety Considerations

The TGA-approved Product Information (PI) warnings and contraindications were not available in the data compiled for this report. Please refer to the PI for full safety information.

**Contraindications suggested by the knowledge graph** (drug-disease links in the TxGNN knowledge graph, not label text):
- Liver failure, kidney disease, pyoureter
- Diabetes mellitus, diabetic ketoacidosis
- Lung disease
- Leukopenia
- Uveitis, iris disease, ciliary body disease, panuveitis, macular oedema (retinal and cystoid)
- Atrioventricular block, sick sinus syndrome (including the familial form)

**Drug interactions** (100 interactions were recorded; the main ones are listed):
- **Major:**
  - Corticosteroids: hydrocortisone, prednisone, dexamethasone, betamethasone, budesonide, triamcinolone (including ophthalmic)
  - QT-prolonging or related agents: clarithromycin, levofloxacin, ondansetron, dolasetron, palonosetron, cisapride
- **Moderate:** famotidine, ranitidine, cimetidine, nizatidine, loperamide, naltrexone
- **Minor:** metronidazole

Fingolimod causes lymphocyte sequestration, so immunosuppression and infection risk are relevant to any oncology use.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no clinical trials and no publications directly on borderline ovarian serous tumours. The only related evidence is preclinical, indirect, and concerns chemosensitisation in ovarian cancer and lung cancer models. A borderline tumour also offers little justification for the safety burden of a systemic immunomodulator.

**To proceed, the following is needed:**
- Mechanism of action data for fingolimod, and a specific rationale for borderline serous tumours
- Targeted literature review and preclinical studies in borderline ovarian tumour models
- Review of the TGA Product Information for warnings and contraindications, and the approved indication text for ARTG 11818B
- A safety assessment of immunosuppression, cardiac conduction effects and drug interactions in this population
- Evidence of benefit in the more clinically relevant ovarian malignancies (serous neoplasm and ovarian cancer) before any further work on benign or borderline conditions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

