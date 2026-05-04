---
layout: default
title: Benzydamine
parent: 僅模型預測 (L5)
nav_order: 82
evidence_level: L5
indication_count: 10
---

# Benzydamine
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

# Benzydamine: From Oropharyngeal Anti-inflammatory to Common Cold

## One-Sentence Summary

Benzydamine is a topical non-steroidal anti-inflammatory drug with local anaesthetic and analgesic properties, widely used internationally (as Difflam® or Tantum Verde®) for oropharyngeal pain relief, but currently not registered on the Australian Register of Therapeutic Goods (ARTG).
The TxGNN model predicts it may be effective for **Common Cold** (specifically sore throat and acute pharyngitis),
with **2 clinical trials** (including 1 completed Phase 3 RCT with 346 participants) and **4 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Oropharyngeal inflammation and pain relief (topical anti-inflammatory; widely marketed globally but not registered in Australia) |
| Predicted New Indication | Common Cold (Sore Throat / Acute Pharyngitis) |
| TxGNN Prediction Score | 95.80% |
| Evidence Level | L1 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## All Predicted Indications at a Glance

This evidence pack covers 10 predicted indications. The table below summarises all predictions; the remainder of this report focuses on the highest-evidence candidate (Common Cold, Rank 5).

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|------------|----------------|----------------|
| 1 | Benign Prostatic Hyperplasia | 99.26% | L5 | Hold |
| 2 | Headache Disorder | 97.58% | L5 | Hold |
| 3 | Trigeminal Autonomic Cephalalgia | 97.17% | L5 | Hold |
| 4 | Peripheral Vascular Disease | 96.19% | L4 | Research Question |
| **5** | **Common Cold** | **95.80%** | **L1** | **Proceed with Guardrails** |
| 6 | Peripheral Arterial Disease | 95.56% | L5 | Hold |
| 7 | Female Breast Carcinoma | 95.23% | L5 | Hold |
| 8 | Toxocariasis | 95.13% | L5 | Hold |
| 9 | Subarachnoid Haemorrhage | 94.86% | L5 | Hold |
| 10 | Alopecia | 94.82% | L5 | Hold |

> **Why Common Cold is the focus:** Although benzydamine ranks 5th by TxGNN score, it is the only indication with L1-grade clinical evidence (completed Phase 3 RCT) and an actionable recommendation. Ranks 1–3 have no supporting evidence beyond the model prediction. The peripheral vascular disease signal (Rank 4) is historically interesting but rests on 1960s–1970s observational data only.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in the evidence pack. Based on established pharmacological knowledge, benzydamine is a benzimidazole-derived NSAID with three key properties: (1) inhibition of pro-inflammatory cytokines — particularly TNF-α and IL-1β — via a mechanism distinct from classic COX inhibition; (2) mild prostaglandin synthesis suppression through weak COX inhibitory activity; and (3) local anaesthetic effect through sodium channel blockade at peripheral nerve terminals.

Sore throat associated with common cold is characterised by localised mucosal inflammation in the oropharynx, driven by viral or bacterial pathogens that trigger a TNF-α/IL-1β-mediated inflammatory cascade. Benzydamine's cytokine inhibition and local anaesthetic properties act directly at this site of pathology, reducing mucosal oedema, suppressing inflammatory mediators, and providing rapid pain relief on contact. This mechanism-to-indication alignment is unusually direct for a repurposing candidate.

Crucially, this is not a purely theoretical connection. Benzydamine oromucosal formulations under the brand names Difflam® and Tantum Verde® are already registered and in widespread clinical use for sore throat in the United Kingdom, New Zealand, Canada, and across Europe. The TxGNN model is effectively rediscovering a well-validated use that simply lacks an Australian registration — making this the most immediately actionable finding in the entire evidence pack.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03282045](https://clinicaltrials.gov/study/NCT03282045) | Phase 3 | Completed | 346 | Multicentre, single-blind, randomised, placebo-controlled 4-arm study. Evaluated Tantum Verde® spray (benzydamine) against Lysobact Complete Spray®, Pharyngal® spray, and placebo in acute sore throat associated with common cold. Primary outcome was Sore Throat Pain Intensity Scale (STPIS) score. Demonstrated that benzydamine spray achieved clinically meaningful pain reduction versus placebo. This trial is the core L1 evidence basis for this indication. |
| [NCT04899401](https://clinicaltrials.gov/study/NCT04899401) | NA | Completed | 130 | Randomised, open, controlled study of PediaFlù® (dietary supplement) plus standard of care versus standard of care only in children with acute tonsillopharyngitis/rhinopharyngitis. Benzydamine was a component of the combination product rather than the sole investigational agent; findings are not directly attributable to benzydamine alone. Cited for completeness only. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37000110](https://pubmed.ncbi.nlm.nih.gov/37000110/) | 2023 | Phase IV RCT | Medicine | Head-to-head comparison of benzydamine HCl 0.3% oromucosal spray versus benzydamine HCl 3 mg lozenges in patients with acute sore throat. Evaluated time to onset of pain relief following a single dose. Both formulations demonstrated rapid, clinically meaningful analgesia; results support flexibility of dosage form for this indication. |
| [31718214](https://pubmed.ncbi.nlm.nih.gov/31718214/) | 2019 | Comparative Clinical Study | Acta Medica Academica | Pilot study comparing lysozyme-based oral spray versus benzydamine/chlorhexidine oral spray in patients with acute tonsillopharyngitis associated with common cold. Benzydamine arm demonstrated satisfactory efficacy and tolerability; adds to the body of comparative evidence across treatment modalities. |
| [8984600](https://pubmed.ncbi.nlm.nih.gov/8984600/) | 1996 | RCT (Double-blind) | Schweizerische Medizinische Wochenschrift | Randomised, double-blind rhinomanometric study in 60 patients with common cold. Compared benzydamine nasal spray against xylometazoline+S-carboxymethylcysteine and phenylephrine+dimethindene maleate. Assessed nasal patency at 3, 10, 120, 240, 360, and 480 minutes post-application. Provides evidence for the nasal/upper respiratory route of action. |
| [40626097](https://pubmed.ncbi.nlm.nih.gov/40626097/) | 2025 | Methodology Review | Frontiers in Pain Research | Comprehensive review of the sore throat pain model as a validated assay for measuring pharmacological effects in acute pharyngitis over 40+ years of research. Benzydamine features as a reference compound. Contextualises the evidence base and supports the methodological rigour of existing benzydamine sore throat trials. |

---

## Australia Market Information

Benzydamine is currently **not registered** on the Australian Register of Therapeutic Goods (ARTG). There are no current ARTG entries for any benzydamine formulation.

For context, comparable regulatory authorities have approved benzydamine oromucosal formulations:
- **Medsafe (New Zealand):** Difflam® oral rinse and spray registered for sore throat and oropharyngeal inflammation
- **MHRA (United Kingdom):** Difflam® and Tantum Verde® registered for oropharyngeal pain relief
- **Health Canada:** Benzydamine products registered for throat pain

Given the availability of regulatory dossiers from these comparable markets, a TGA registration application could potentially leverage existing international data packages.

---

## Safety Considerations

As benzydamine is not currently registered on the ARTG, no TGA-approved Product Information (PI) is available. Please refer to the Product Information from a comparable regulatory jurisdiction — Medsafe New Zealand or MHRA United Kingdom — for full safety information pending Australian registration.

No drug-drug interaction data was identified in the evidence search. No key warnings or contraindications data were available from the Australian regulatory database.

---

## Notable Secondary Signal: Peripheral Vascular Disease (Rank 4)

Although below the evidence threshold for a primary recommendation, the peripheral vascular disease signal (Rank 4, L4 evidence) is worth noting for completeness.

Six publications from 1967–1976 describe topical and systemic benzydamine use in thrombophlebitis and other inflammatory venous conditions, including one controlled clinical study (PMID [772478](https://pubmed.ncbi.nlm.nih.gov/772478/)) comparing benzydamine with feprazone in a double-blind design. The mechanistic rationale — anti-inflammatory and potential anti-thrombotic properties in vessel wall inflammation — is plausible.

This signal is assessed as a **Research Question** rather than actionable, given the age of the literature, lack of contemporary controlled trials, and the availability of more targeted modern therapies for peripheral vascular disease.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The common cold (sore throat) indication is supported by strong Level 1 evidence including a completed Phase 3 RCT (n=346) and a Phase IV head-to-head trial, aligning directly with benzydamine's well-established international clinical profile as Difflam® and Tantum Verde®. The primary barrier to use in Australia is a regulatory gap, not a clinical or safety gap.

**To proceed, the following is needed:**

- **Regulatory pathway assessment:** Determine whether a TGA abridged application or international recognition pathway is available, leveraging existing UK/NZ regulatory dossiers
- **Product Information review:** Obtain and review the PI from Medsafe New Zealand or MHRA UK as interim safety reference material
- **MOA documentation:** Complete DrugBank API query to formally document mechanism of action (Data Gap DG002)
- **ARTG pre-submission meeting:** Engage TGA Early Advice program to confirm the appropriate application pathway for oromucosal formulations (spray and lozenges)
- **Formulation decision:** Determine which dosage form(s) to prioritise for registration — oromucosal spray and/or lozenges — based on Phase IV data showing both are effective

> **Disclaimer:** This report is intended for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. This analysis reflects the data available as of 5 April 2026.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

