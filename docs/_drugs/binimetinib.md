---
layout: default
title: Binimetinib
parent: 僅模型預測 (L5)
nav_order: 89
evidence_level: L5
indication_count: 10
---

# Binimetinib
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

# Binimetinib: From BRAF-Mutant Melanoma to Non-Cutaneous Melanoma

## One-Sentence Summary

Binimetinib (MEK162) is a selective MEK1/MEK2 kinase inhibitor established internationally for BRAF V600E/K mutation-positive unresectable or metastatic melanoma in combination with encorafenib, though it holds no current TGA registration in Australia.
The TxGNN model's highest-ranked prediction (Rank 1: choroideremia, score 98.63%) lacks mechanistic rationale and any clinical support; the most clinically actionable prediction is **Non-Cutaneous Melanoma** (Rank 2, score 98.60%), backed by **multiple Phase 2–3 clinical trials** across melanoma subtypes including two completed Phase 3 programmes.
Evidence is rated **L2**, with the pivotal COLUMBUS and NEMO Phase 3 trials as anchors, and an active 815-patient adjuvant study reinforcing this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | BRAF V600E/K mutation-positive unresectable or metastatic melanoma (FDA-approved as Mektovi®; no TGA registration in Australia) |
| Predicted New Indication | Non-Cutaneous Melanoma |
| TxGNN Prediction Score | 98.60% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the provided Evidence Pack. Based on established pharmacology and contextual information within the evidence package, binimetinib is a potent and selective inhibitor of MEK1 and MEK2 — the kinases immediately downstream of BRAF and RAS in the MAPK (BRAF–MEK–ERK) signalling cascade. By blocking MEK1/2 phosphorylation, binimetinib suppresses ERK activation and downstream pro-proliferative and pro-survival signals in tumour cells harbouring activating mutations in BRAF, NRAS, or other upstream MAPK pathway components.

Cutaneous and non-cutaneous melanoma subtypes (uveal, mucosal, acral, and other anatomically distinct forms) share dysregulated MAPK signalling as a central oncogenic mechanism, though the specific driver mutations differ in frequency. BRAF V600 mutations are present in approximately 40–60% of cutaneous melanomas but only ~5–20% of non-cutaneous subtypes; however, non-cutaneous variants carry higher rates of NRAS and KIT mutations — both of which feed into the MEK–ERK axis. Critically, MEK functions as a convergence node downstream of both BRAF and NRAS, making MEK inhibition mechanistically applicable across these molecular subtypes. The NEMO Phase 3 trial (NCT01763164) specifically evaluated binimetinib in NRAS Q61 mutation-positive melanoma — a population disproportionately enriched with non-cutaneous cases — lending direct clinical relevance to this prediction.

For transparency, the TxGNN Rank 1 prediction (choroideremia, score 98.63%) is noted but not the focus of this report. Choroideremia is an X-linked retinal degenerative condition caused by loss-of-function mutations in the CHM gene (encoding REP-1), with no established link to MEK signalling. The high model score likely reflects indirect topological connections within the knowledge graph rather than biological plausibility. No clinical trials or literature support this prediction, and the recommendation for choroideremia is **Hold**.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT01909453](https://clinicaltrials.gov/study/NCT01909453) | Phase 3 | Completed | 921 | COLUMBUS trial: Encorafenib + binimetinib vs vemurafenib and encorafenib monotherapy in BRAF V600-mutant unresectable/metastatic melanoma; pivotal registration-enabling study demonstrating superior PFS and OS benefit for the combination |
| [NCT01763164](https://clinicaltrials.gov/study/NCT01763164) | Phase 3 | Completed | 402 | NEMO trial: Binimetinib (MEK162) vs dacarbazine in NRAS Q61 mutation-positive advanced unresectable or metastatic cutaneous/unknown-primary melanoma; demonstrated significant improvement in progression-free survival with binimetinib |
| [NCT05270044](https://clinicaltrials.gov/study/NCT05270044) | Phase 3 | Active, not recruiting | 815 | COLUMBUS-AD: Encorafenib + binimetinib vs surveillance as adjuvant therapy in resected Stage IIB/C BRAF V600E/K mutant melanoma; primary endpoint is relapse-free survival; results anticipated to reshape adjuvant practice |
| [NCT04657991](https://clinicaltrials.gov/study/NCT04657991) | Phase 3 | Active, not recruiting | 257 | Encorafenib + binimetinib + pembrolizumab vs pembrolizumab + placebo in previously untreated BRAF V600E/K mutation-positive metastatic or unresectable melanoma; triple combination strategy |
| [NCT03898908](https://clinicaltrials.gov/study/NCT03898908) | Phase 2 | Completed | 48 | Encorafenib + binimetinib before local treatment in BRAF-mutant melanoma brain metastases; two parallel cohorts (asymptomatic and symptomatic); multicentre, directly evaluates an underserved non-cutaneous-extension scenario |
| [NCT03235245](https://clinicaltrials.gov/study/NCT03235245) | Phase 2 | Active, not recruiting | 271 | EBIN study (EORTC): Sequential encorafenib + binimetinib (12 weeks) followed by ipilimumab + nivolumab vs immediate immunotherapy in BRAF V600-mutant unresectable/metastatic melanoma; evaluates optimal treatment sequencing |
| [NCT01781572](https://clinicaltrials.gov/study/NCT01781572) | Phase 1/2 | Completed | 102 | LEE011 (ribociclib) + binimetinib in NRAS-mutant melanoma; Phase 1b established the MTD/RP2D; Phase 2 assessed anti-tumour activity — provides key data on binimetinib in NRAS-driven non-cutaneous-relevant subtype |
| [NCT01320085](https://clinicaltrials.gov/study/NCT01320085) | Phase 2 | Completed | 183 | Single-agent MEK162 (binimetinib) in locally advanced/unresectable or metastatic cutaneous melanoma with BRAF V600 or NRAS mutations; characterised single-agent safety profile and efficacy signals across mutation subtypes |
| [NCT06887088](https://clinicaltrials.gov/study/NCT06887088) | Phase 2 | Recruiting | 33 | ENCEFALO: Encorafenib + binimetinib followed by cemiplimab + fianlimab in BRAF-mutant melanoma with symptomatic brain metastases; evaluates a novel sequential targeted-then-immunotherapy approach for a high-need population |
| [NCT02910700](https://clinicaltrials.gov/study/NCT02910700) | Phase 2 | Active, not recruiting | 52 | TRIBECA arm: Encorafenib + binimetinib + nivolumab triplet in BRAF-mutated Stage III–IV unresectable/metastatic melanoma; ongoing with completion anticipated December 2027 |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [41774417](https://pubmed.ncbi.nlm.nih.gov/41774417/) | 2025 | Case Report | Pigment Cell & Melanoma Research | Molecular profiling used to diagnose epidermotropic metastatic melanoma (EMM) mimicking eruptive primary superficial spreading melanomas in a Stage IIIB nodular melanoma patient; highlights diagnostic complexity of non-standard melanoma presentations and the importance of molecular testing to guide therapy selection in atypical cases |

---

## Australia Market Information

Binimetinib is **not currently registered with the Therapeutic Goods Administration (TGA)** and has no ARTG entries.

| Status Item | Detail |
|-------------|--------|
| ARTG Entries | None — Binimetinib has no current TGA registration |
| Market Status | Not marketed in Australia |
| Alternative Access Pathway | May be accessible for eligible patients via the **TGA Special Access Scheme (SAS Category B)** or the **Authorised Prescriber** pathway, subject to clinical justification |
| Combination Partner | Encorafenib (Braftovi®) TGA/SAS registration status should be independently confirmed, as binimetinib is typically prescribed in combination |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — selective MEK1/MEK2 kinase inhibitor (small molecule, non-cytotoxic mechanism of action) |
| Myelosuppression Risk | Low to Moderate (anaemia and thrombocytopenia reported; markedly less myelosuppressive than conventional cytotoxic chemotherapy) |
| Emetogenicity Classification | Low |
| Monitoring Items | Full blood count (FBC with differential), liver function tests (LFTs), renal function, ophthalmological assessment (retinal pigment epithelial detachment and retinal vein occlusion), ECG (QTc interval), blood pressure, and creatine kinase (CK/CPK) |
| Handling Protection | Classified as a hazardous oral antineoplastic drug — handle in accordance with institutional cytotoxic handling guidelines; avoid crushing or splitting tablets without appropriate PPE |

---

## Safety Considerations

Safety data including key warnings, contraindications, and drug–drug interactions are not available in the current Evidence Pack for the Australian regulatory context.

> Please refer to the **FDA-approved Prescribing Information for Mektovi® (binimetinib)** for complete safety information. Priority areas for clinical review include: cardiomyopathy and decreased left ventricular ejection fraction (LVEF), ocular toxicity (retinal pigment epithelial detachment, retinal vein occlusion — particularly relevant when considering use in uveal melanoma patients), venous thromboembolism, haemorrhage, colitis and gastrointestinal perforation, interstitial lung disease/pneumonitis, hepatotoxicity, dermatological reactions (rash, photosensitivity), and embryo-fetal toxicity. When TGA registration is formally pursued, the Australian Product Information (PI) must be reviewed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Binimetinib has a robust international evidence base in BRAF/NRAS-mutant melanoma, anchored by two completed Phase 3 trials (COLUMBUS and NEMO) and supported by numerous Phase 2 studies directly evaluating its role across melanoma subtypes that overlap with non-cutaneous disease; the mechanistic rationale via MEK pathway convergence is scientifically sound. However, the drug carries no TGA registration in Australia, subtype-specific data for uveal and mucosal melanoma remain limited, and access requires navigation of alternative regulatory pathways before use can be considered.

**To proceed, the following is needed:**

- **Regulatory access**: Initiate a TGA Special Access Scheme (SAS Category B) application or Authorised Prescriber process; consider longer-term formal TGA registration submission
- **Molecular profiling**: Confirm BRAF V600E/K or NRAS Q61 mutation status prior to initiation — mutation-negative cases have substantially lower expected benefit
- **Combination partner**: Verify TGA/SAS availability of encorafenib (Braftovi®), as binimetinib is not used as monotherapy in BRAF-mutant disease under standard-of-care protocols
- **Safety monitoring plan**: Establish baseline and scheduled LVEF assessment, ophthalmological review (slit-lamp and fundoscopy), LFTs, FBC, blood pressure, and QTc monitoring prior to and during treatment
- **Full safety review**: Obtain and review FDA Prescribing Information for Mektovi® until an Australian TGA PI becomes available
- **Clinical trial consideration**: Explore patient eligibility for ongoing Phase 3 trials (NCT05270044 adjuvant study; NCT04657991 triple combination) as a preferred access route where clinically appropriate
- **Evidence monitoring**: Track results from COLUMBUS-AD and the TRIBECA triplet arm — outcomes will materially affect the strength of the repurposing case for non-cutaneous subtypes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

