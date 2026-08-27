---
layout: default
title: Pimecrolimus
parent: 僅模型預測 (L5)
nav_order: 536
evidence_level: L5
indication_count: 10
---

# Pimecrolimus
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

# Pimecrolimus: From Atopic Dermatitis to Seborrheic Dermatitis

## One-Sentence Summary

Pimecrolimus is a topical calcineurin inhibitor originally developed for inflammatory skin disease, most notably atopic dermatitis (per literature in the evidence pack; no TGA-approved indication text is available because the product does not currently hold an ARTG registration).
The TxGNN model predicts it may also be effective for **seborrheic dermatitis**, with **1 completed clinical trial** and **18 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic dermatitis (sourced from literature in this evidence pack, e.g. PMID 16033622; no ARTG-approved indication text is available) |
| Predicted New Indication | Seborrheic dermatitis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed (no current ARTG registration) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data was not returned by the DrugBank query for this evidence pack. However, the literature retrieved for this candidate consistently describes pimecrolimus as an ascomycin-derivative calcineurin inhibitor that selectively targets T cells and mast cells — it inhibits T-cell proliferation and the release of IL-2, IL-4, interferon-gamma and TNF-alpha, and also inhibits mast cell degranulation (PMID 16033622). This anti-inflammatory, non-steroidal mode of action is why it was developed for atopic dermatitis.

Seborrheic dermatitis and atopic dermatitis are both chronic, relapsing inflammatory dermatoses driven substantially by cytokine-mediated cutaneous inflammation, even though their underlying triggers differ (Malassezia-associated irritant response in seborrheic dermatitis vs. barrier/immune dysregulation in atopic dermatitis). Because calcineurin inhibitors act downstream on the inflammatory cascade rather than on a disease-specific trigger, the mechanistic rationale for extending pimecrolimus to seborrheic dermatitis is plausible.

This is further supported by real-world evidence: pimecrolimus 1% cream has already been studied off-label for seborrheic dermatitis in multiple randomized and open-label trials as an alternative to corticosteroids and antifungals, avoiding the skin atrophy risk associated with prolonged topical steroid use (e.g. PMID 20000875, PMID 22142161), which reinforces the reasonableness of the TxGNN prediction.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00403559](https://clinicaltrials.gov/study/NCT00403559) | Phase 2 | Completed | 113 | 4-week randomised, double-blind, parallel-group, active-comparator-controlled study exploring pimecrolimus (Elidel) effectiveness for seborrheic dermatitis |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22142161](https://pubmed.ncbi.nlm.nih.gov/22142161/) | 2012 | Systematic Review (RCTs) | Expert Review of Clinical Pharmacology | Pimecrolimus 1% cream is well tolerated and effective for seborrheic dermatitis, with efficacy comparable to corticosteroids/antimycotics |
| [36072203](https://pubmed.ncbi.nlm.nih.gov/36072203/) | 2022 | Systematic Review (RCTs) | Cureus | Reviews calcineurin inhibitors among four treatment categories for facial seborrheic dermatitis |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematic Review | American Journal of Clinical Dermatology | Reviews topical treatment options (antifungals, keratolytics, corticosteroids) for facial seborrheic dermatitis |
| [34910320](https://pubmed.ncbi.nlm.nih.gov/34910320/) | 2022 | RCT | Clinical and Experimental Dermatology | Randomised blinded trial comparing pimecrolimus 1% cream vs. sertaconazole 2% cream for facial seborrheic dermatitis |
| [23715821](https://pubmed.ncbi.nlm.nih.gov/23715821/) | 2013 | Comparative study | Irish Journal of Medical Science | Compares efficacy of sertaconazole 2% cream vs. pimecrolimus 1% cream in seborrheic dermatitis |
| [18677657](https://pubmed.ncbi.nlm.nih.gov/18677657/) | 2009 | RCT | Journal of Dermatological Treatment | Open, randomised, prospective comparison of pimecrolimus 1% cream vs. ketoconazole 2% cream |
| [20000875](https://pubmed.ncbi.nlm.nih.gov/20000875/) | 2010 | Open-label study | American Journal of Clinical Dermatology | Pimecrolimus 1% cream effective and well tolerated for resistant facial seborrheic dermatitis |
| [28589618](https://pubmed.ncbi.nlm.nih.gov/28589618/) | 2018 | Study | Journal of Cosmetic Dermatology | Compares different treatment-duration regimens of pimecrolimus 1% cream for facial seborrheic dermatitis |
| [19255921](https://pubmed.ncbi.nlm.nih.gov/19255921/) | 2009 | Study | Journal of Dermatological Treatment | Close follow-up study reporting cure/remission times and side-effect profile of pimecrolimus in seborrheic dermatitis |
| [16033622](https://pubmed.ncbi.nlm.nih.gov/16033622/) | 2005 | Review | International Journal of Clinical Practice | Reviews pimecrolimus mechanism of action and use in dermatology beyond atopic dermatitis |

## Australia Market Information

No ARTG entries were found for pimecrolimus in this evidence pack (total_licenses = 0). Based on available data, pimecrolimus is not currently marketed in Australia; any progression toward this indication would need to start from establishing (or confirming) product registration status directly with the TGA.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information — key warnings, contraindications, and drug interaction data were not returned for this candidate, and a TGA/TFDA label warning search remains an open, blocking data gap (DG001) before a safety pre-assessment can be completed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While efficacy signals for seborrheic dermatitis are reasonably supported (1 completed Phase 2 RCT plus multiple additional RCTs and systematic reviews in the literature, meeting evidence level L2), the absence of any TGA-approved Product Information and the lack of a current ARTG registration mean the safety pre-assessment (S1) cannot be completed — this is a blocking gap, not merely a preference.

**To proceed, the following is needed:**
- TGA-approved Product Information / label warnings and contraindications (currently missing — DG001, Blocking)
- Confirmed mechanism-of-action data from DrugBank to support the mechanistic-link analysis (currently missing — DG002, High)
- Confirmation of current ARTG/registration status for pimecrolimus in Australia (or identification of an equivalent registered product)
- A formal drug-interaction (DDI) query, as the current query returned no data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

