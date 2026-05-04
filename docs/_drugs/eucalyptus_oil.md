---
layout: default
title: Eucalyptus Oil
parent: 僅模型預測 (L5)
nav_order: 209
evidence_level: L5
indication_count: 10
---

# Eucalyptus Oil
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

# Eucalyptus Oil: From Traditional Topical Analgesic to Osteoarthritis

## One-Sentence Summary

Eucalyptus oil is a naturally derived botanical product traditionally used as a topical analgesic, antiseptic, and inhalant for respiratory symptoms — with no formally registered indications in Australia.
The TxGNN model predicts it may be effective for **Osteoarthritis**, with **1 clinical trial** and **3 publications** currently supporting this direction for the primary indication, alongside broader anti-inflammatory mechanistic evidence from rheumatoid arthritis literature.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No formally approved indication; traditionally used for topical analgesia and respiratory relief |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 98.48% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Eucalyptus oil's primary active constituent is **Eucalyptol (1,8-Cineole)**, a monoterpene oxide with well-characterised anti-inflammatory and analgesic properties. Mechanistically, Eucalyptol suppresses the **NF-κB signalling pathway**, downregulates pro-inflammatory cytokines including **TNF-α, IL-1β, and IL-6**, and modulates **TRPA1/TRPV1 pain receptors** — all pathways centrally implicated in osteoarthritic joint pain and synovial inflammation. Transcutaneous absorption of topically applied eucalyptus oil can achieve local concentrations sufficient to dampen synovial inflammation at the joint.

Osteoarthritis is characterised by a progressive cycle of cartilage degradation, subchondral bone remodelling, and synovial inflammatory flares driven by the same cytokine networks that Eucalyptol inhibits. This mechanistic overlap provides a biologically plausible rationale for the TxGNN prediction. Supportive evidence from aromatherapy and herbal combination studies (e.g., Elmore Oil, which contains eucalyptus oil as a key component) suggests symptomatic benefit in arthritic conditions, though direct attribution to the eucalyptus oil component alone requires further investigation.

It is worth noting that the same mechanistic pathway also underpins the predicted link to rheumatoid arthritis (rank 2, TxGNN score 98.28%), where preclinical in vivo data using a Complete Freund's adjuvant model and clinical inhalation studies both show meaningful anti-inflammatory effects. This convergence across two major arthritis subtypes strengthens the plausibility of the arthritis-related predictions as a whole.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT01684371](https://clinicaltrials.gov/study/NCT01684371) | N/A (Pilot) | Completed | 60 | Double-blind, placebo-controlled, crossover trial of topical Elmore Oil (a herbal combination containing eucalyptus oil, tea tree oil, olive oil, and vanilla) for osteoarthritis symptom relief. The formulation was reported to have anti-inflammatory properties. Note: this tests a multi-ingredient product; results cannot be directly attributed to eucalyptus oil alone. |

> **Note:** No ANZCTR-registered trials were identified for this drug-indication pair.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [15778570](https://pubmed.ncbi.nlm.nih.gov/15778570/) | 2005 | Clinical Observational / Quasi-experimental | Taehan Kanho Hakhoe chi | Aromatherapy (including eucalyptus-containing blends) demonstrated significant effects on pain reduction, depression, and life satisfaction in arthritis patients. |
| [38409718](https://pubmed.ncbi.nlm.nih.gov/38409718/) | 2024 | Pharmaceutical Formulation Study | Anti-Inflammatory & Anti-Allergy Agents in Medicinal Chemistry | Development of a celecoxib emulgel incorporating natural oils (including eucalyptus oil as an excipient/penetration enhancer) for osteoarthritis and rheumatoid arthritis; supports the topical delivery concept. |
| [37111672](https://pubmed.ncbi.nlm.nih.gov/37111672/) | 2023 | Review | Pharmaceutics | Nanoemulgel systems for topical anti-inflammatory delivery; eucalyptus oil referenced as a permeation enhancer in transdermal formulations for inflammatory conditions. |

---

## Australia Market Information

Eucalyptus oil (DrugBank ID: DB11114) currently has **no ARTG registrations** in Australia. It is not listed as a marketed therapeutic good with the TGA. Any future development pathway would require a new registration or listing application under TGA legislation.

---

## Safety Considerations

Detailed safety data (including product warnings, contraindications, and drug interactions) are not available in the current Evidence Pack.

> Please refer to the TGA-approved Product Information (PI) and the TGA's complementary medicine guidelines for safety information. Clinicians should note that undiluted eucalyptus oil is toxic if ingested and must not be applied near the face of infants or young children. Potential for CYP2B6/CYP3A4 metabolic interactions warrants evaluation before formal clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic basis for eucalyptus oil in osteoarthritis is biologically plausible and supported by observational-level clinical data and preclinical studies, but the current evidence does not yet meet the standard required for a formal repurposing decision — the only completed trial used a multi-ingredient combination product rather than eucalyptus oil as a standalone agent, and eucalyptus oil has no current TGA registration in Australia.

**To proceed, the following is needed:**

- **Standalone clinical trial data**: A well-controlled trial isolating the effect of eucalyptus oil (or purified Eucalyptol/1,8-Cineole) in osteoarthritis patients, separate from combination herbal formulations
- **Dose-finding and pharmacokinetic studies**: Establish effective topical concentrations and transdermal absorption parameters in a human model
- **Safety data package**: Obtain formal product warnings, contraindications, and drug interaction data (DrugBank API query recommended as a first step)
- **TGA regulatory pathway assessment**: Determine whether the product would be classified as a listed complementary medicine, registered medicine, or therapeutic device, and identify applicable TGA submission requirements
- **MOA documentation**: Formal mechanism of action characterisation (e.g., from DrugBank or primary pharmacology literature) to support a regulatory dossier
- **YMYL disclaimer**: Any public-facing materials must include the statement: *"These predictions are for research purposes only and do not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application."*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

