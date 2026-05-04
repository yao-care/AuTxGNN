---
layout: default
title: Clotrimazole
parent: 僅模型預測 (L5)
nav_order: 123
evidence_level: L5
indication_count: 10
---

# Clotrimazole
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

# Clotrimazole: From Fungal Infections to Acne

## One-Sentence Summary

Clotrimazole is a broad-spectrum synthetic imidazole antifungal, widely known for its topical use in tinea pedis (athlete's foot), vulvovaginal candidiasis, and oropharyngeal candidiasis — although no formal registered indications were returned from the Australian regulatory database for this Evidence Pack.
The TxGNN model predicts it may be effective for **Acne**, with **1 clinical trial** (suspended) and **no supporting published literature** currently identified for this specific direction.
The overall evidence base for this prediction is currently insufficient for clinical translation, and a Hold decision is recommended pending further characterisation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Fungal infections (tinea pedis, vulvovaginal candidiasis, oropharyngeal candidiasis) — based on known pharmacology; no ARTG registration data available |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L3 |
| Australia Market Status | Not listed on ARTG |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Clotrimazole is a synthetic imidazole antifungal that inhibits the fungal CYP51 enzyme (lanosterol 14α-demethylase), thereby disrupting ergosterol biosynthesis and compromising fungal cell membrane integrity. It exerts broad-spectrum fungistatic activity against dermatophytes, *Candida albicans*, and *Malassezia* species. Its efficacy across common superficial fungal infections is well-characterised in the literature.

Acne vulgaris is a multifactorial condition primarily driven by *Cutibacterium acnes* (a bacterium), sebaceous gland dysregulation, and follicular hyperkeratinisation. However, a distinct subtype — pityrosporum folliculitis (fungal acne) — is caused by *Malassezia* overgrowth in sebaceous follicles. Clotrimazole's established activity against *Malassezia* provides the only plausible mechanistic rationale for the TxGNN prediction, and would apply specifically to this fungal acne subtype rather than classic inflammatory acne.

The TxGNN high prediction score most likely reflects shared skin inflammation pathway nodes within the knowledge graph — an indirect association — rather than a direct mechanistic fit for the majority of acne presentations. Clotrimazole has no established antibacterial activity against *C. acnes*, and the single available trial used a three-drug combination (clotrimazole + gentamicin + beclomethasone), making it impossible to attribute any effect to clotrimazole alone. Clinical utility, if any, would be limited to the pityrosporum folliculitis subtype.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | **Suspended** | 80 | Evaluated a three-drug topical combination (Clotrimazole 1% + Gentamicin 0.1% + Beclomethasone 0.025%) in patients with acne presenting as contaminated dermatosis with bilateral symmetrical lesions. The trial was suspended and no results are available; the combination design prevents attribution of any effect to clotrimazole individually. |

---

## Literature Evidence

Currently no related literature available for clotrimazole in acne (disease).

---

## Australia Market Information

Clotrimazole is currently **not listed on the Australian Register of Therapeutic Goods (ARTG)**. No registered products were identified in this Evidence Pack.

> **Important caveat:** This likely reflects a data collection limitation rather than true absence from the Australian market. Clotrimazole-containing topical products (creams, pessaries, troches) are widely available in comparable markets including the UK, USA, Canada, New Zealand, and Europe — many as over-the-counter (OTC) formulations. Clinicians should verify the current ARTG status directly via the [TGA website](https://www.tga.gov.au/resources/artg).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only available clinical trial for clotrimazole in acne was suspended prior to completion and evaluated a three-drug combination, providing no interpretable evidence for clotrimazole's individual contribution. There is no published literature to support this repurposing direction, the mechanistic link to common acne pathophysiology is indirect, and well-established acne therapies already exist across all disease severity levels.

**To proceed, the following is needed:**

- Confirm ARTG listing status for clotrimazole-containing products via the TGA website — this data gap likely reflects a registry query issue rather than genuine non-availability
- Obtain full mechanism of action (MOA) data from DrugBank (DB00257) to allow formal mechanistic analysis
- Narrow the clinical question to **pityrosporum folliculitis** (fungal acne / *Malassezia* folliculitis), which is the only biologically plausible acne subtype for antifungal intervention — standard acne vulgaris should not be the target
- Obtain TGA Product Information (PI) for currently marketed Australian formulations to characterise approved indications, contraindications, and safety warnings
- Conduct a systematic literature review specifically for clotrimazole or azole antifungals in pityrosporum folliculitis before any Phase 2 trial design is contemplated

> **Clinician note:** While the acne prediction is weak, the same Evidence Pack identifies **vulvovaginal candidiasis** (rank 2, evidence level L1) and **superficial mycosis** (rank 9, evidence level L2) as higher-confidence repurposing targets with multiple completed Phase 3 RCTs. These indications warrant a separate, more detailed assessment and may already reflect established off-label or approved use in other jurisdictions.

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. Data as of 4 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

