---
layout: default
title: Posaconazole
parent: 僅模型預測 (L5)
nav_order: 544
evidence_level: L5
indication_count: 10
---

# Posaconazole
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

# Posaconazole: From Antifungal Therapy to Pneumocystosis

## One-Sentence Summary

Posaconazole is a triazole antifungal agent whose original indication data is not available in this evidence pack (posaconazole is not currently registered in Australia). The TxGNN model predicts it may be effective for **Pneumocystosis (Pneumocystis jirovecii infection)**, but the supporting evidence is indirect — **2 clinical trials** (neither evaluating posaconazole as the primary study drug) and **5 publications** (mostly reviews/guidelines discussing posaconazole prophylaxis in fungal disease generally), and the drug pack itself flags a mechanistic caveat.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack — no ARTG licence text exists (drug is unregistered in Australia). Internationally, posaconazole is known as a broad-spectrum triazole antifungal. |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L4 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data (`original_moa`) is not populated in this evidence pack. Based on the information available, posaconazole is a triazole antifungal that inhibits CYP51 (lanosterol 14α-demethylase), blocking fungal ergosterol synthesis — the mechanism underlying its established activity against *Candida* and *Aspergillus* species.

For pneumocystosis, however, the mechanistic fit is weaker than for a typical fungal repurposing signal. *Pneumocystis jirovecii*'s cell membrane is predominantly cholesterol-based rather than ergosterol-dependent in the conventional sense, so azole activity against it is theoretically limited. Clinically, posaconazole's role in this space has mainly been as a prophylactic alternative for patients who cannot tolerate TMP-SMX, rather than as a mechanism-driven first-line treatment.

Given this, the high TxGNN score should be read as a graph-based association rather than a validated pharmacological rationale — the drug pack's own relevance grading (Grade C) on both supporting trials reflects that posaconazole appears only as a background/comparator prophylactic agent, not as the therapeutic focus of either study.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | Active, not recruiting | 602 | Rezafungin (echinocandin) vs. standard antimicrobial regimen for prevention of invasive fungal disease post allogeneic transplant; posaconazole appears only as part of the standard-of-care comparator, not the study drug (relevance grade C). |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Platform trial comparing GVHD prophylaxis regimens post mismatched unrelated donor transplant; posaconazole is likely one antifungal-prophylaxis option, not a pneumocystosis treatment endpoint (relevance grade C). |

*Note: Neither trial directly evaluates posaconazole efficacy against pneumocystosis; both use it as background prophylaxis in transplant settings.*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2025 | Review/Guideline | The Lancet Infectious Diseases | 2025 update to UK best-practice recommendations for diagnosing serious fungal disease; general diagnostic landscape, not posaconazole-specific efficacy data. |
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Review | Swiss Medical Weekly | Overview of invasive candidiasis, aspergillosis, cryptococcosis and *Pneumocystis* pneumonia; notes mould-active posaconazole prophylaxis has reduced invasive candidiasis in high-risk haemato-oncology patients (not a pneumocystosis efficacy claim). |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Review/Guideline | Chinese Journal of Tuberculosis and Respiratory Diseases | 2025 Chinese clinical practice guideline for invasive pulmonary fungal disease diagnosis/management; general guideline, not posaconazole-pneumocystosis specific. |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Cohort | Transplant Infectious Disease | Retrospective review of infectious complications in acute GVHD after liver transplant; describes antimicrobial management patterns broadly. |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review (PK) | Clinical Pharmacokinetics | Pulmonary epithelial lining fluid penetration of anti-infective agents, including antifungals; pharmacokinetic context only, no efficacy data for pneumocystosis. |

## Australia Market Information

Posaconazole currently has **no ARTG entries** and is **not marketed in Australia** (`total_licenses: 0`). No approved indication text is available for reference.

## Safety Considerations

No key warnings, contraindications, or drug interaction data are available in this evidence pack, and because posaconazole is unregistered in Australia, no TGA-approved Product Information exists to reference. Any safety assessment would need to draw on overseas regulatory PI (e.g. FDA/EMA labelling) pending local registration.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic case for posaconazole in pneumocystosis is contested rather than confirmatory — *Pneumocystis* is atypical for azole targets, and the only cited trials use posaconazole solely as background prophylaxis rather than as the studied intervention. Combined with the drug's unregistered status in Australia, the evidence does not support progressing beyond a research question at this stage.

**To proceed, the following is needed:**
- Original indication and MOA data for posaconazole (currently marked as data gaps DG001/DG002)
- TFDA/TGA-equivalent warnings and contraindications before any S1 safety screening can occur
- Direct pharmacodynamic or clinical evidence of posaconazole activity against *Pneumocystis jirovecii*, rather than trials where it appears only as comparator/background prophylaxis
- Consideration of the ARTG registration pathway, since posaconazole is not currently marketed in Australia
- For context, rank 2 in this evidence pack (vulvovaginal candidiasis, L3 evidence) has a substantially stronger mechanistic fit — *Candida* is posaconazole's on-target pathogen — and may warrant separate evaluation as a higher-confidence candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

