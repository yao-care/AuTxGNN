---
layout: default
title: Riociguat
parent: 僅模型預測 (L5)
nav_order: 594
evidence_level: L5
indication_count: 10
---

# Riociguat
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

# Riociguat: From Pulmonary Arterial Hypertension to Connective Tissue Disease–Associated PAH

## One-Sentence Summary

> Riociguat is a soluble guanylate cyclase (sGC) stimulator internationally approved for Pulmonary Arterial Hypertension (WHO Group 1) and CTEPH, though it is not currently marketed in Australia.
> Among the ten candidate indications in this evidence pack, the TxGNN model's highest-scoring prediction (Ambras-type hypertrichosis, 94.9%) has **no supporting clinical or literature evidence** and is assessed as a likely false-positive pairing.
> The best-supported repurposing signal instead points to **Pulmonary Arterial Hypertension associated with Connective Tissue Disease (PAH-CTD)**, backed by **12 publications**, including **Phase 3 RCT subgroup data from PATENT-1/PATENT-2 and the REPLACE trial**, with a closely related extension to **PAH associated with Congenital Heart Disease (PAH-CHD)** also supported by PATENT-1 subgroup data and one ongoing Phase 4 trial.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary Arterial Hypertension (WHO Group 1) / CTEPH — internationally approved indication (referenced in supporting literature); not currently registered in Australia |
| Predicted New Indication | Pulmonary Arterial Hypertension associated with Connective Tissue Disease (related indication: PAH associated with Congenital Heart Disease) |
| TxGNN Prediction Score | 91.55% (PAH-CTD) / 92.58% (PAH-CHD) |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

**Note on TxGNN ranking**: This evidence pack contains 10 candidate indications for Riociguat. The two highest raw TxGNN scores (Ambras-type hypertrichosis, 94.9%; a periodontal malformation syndrome, 94.4%) returned zero relevant clinical or mechanistic evidence and are scored L5/Hold — these are treated in this report as non-actionable, high-score false positives rather than the headline finding. The candidates selected above have materially weaker raw scores but substantially stronger, mechanistically coherent evidence.

---

## Why is This Prediction Reasonable?

Riociguat is a soluble guanylate cyclase (sGC) stimulator that increases cGMP production independently of nitric oxide availability, producing pulmonary and systemic vasodilation. This is its established mechanism of action in its approved indication, Pulmonary Arterial Hypertension (WHO Group 1) and CTEPH — detailed formal MOA documentation was not available in this evidence pack (data gap DG002), but the mechanism is consistently referenced across the supporting literature below.

PAH-CTD and PAH-CHD are not new diseases but **etiological subgroups of WHO Group 1 PAH** — the same NO–sGC–cGMP pathway dysfunction underlies pulmonary vascular remodelling regardless of whether the trigger is connective tissue disease (e.g. systemic sclerosis) or an unrepaired congenital shunt. Because Riociguat's action is downstream of and independent from the underlying cause, its efficacy is expected to generalise across PAH aetiologies — this is exactly what the pivotal PATENT-1/PATENT-2 programme's prospectively planned subgroup analyses were designed to test, and both subgroups showed benefit consistent with the overall PAH population.

By contrast, the top TxGNN-scored candidates in this pack (hypertrichosis, odontal/periodontal malformation syndromes, Dandy-Walker syndrome, hair shaft abnormality) are structural or developmental disorders with no plausible connection to the sGC-cGMP vasodilatory pathway, and the literature returned for these candidates (e.g. general periodontitis microbiology papers) does not mention Riociguat or its mechanism at all — consistent with a knowledge-graph embedding artefact rather than a genuine biological signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT07356778](https://clinicaltrials.gov/study/NCT07356778) | Phase 4 | Recruiting | 36 | Evaluates sotatercept add-on therapy in PAH associated with unrepaired congenital shunts (ASD/VSD/PDA, incl. Eisenmenger syndrome); Riociguat is not the investigational agent but represents background/comparator PAH pulmonary vasodilator therapy in this population (relevance graded C — indirect) |

No trials specifically investigating Riociguat in PAH-CTD were identified in this pack; efficacy in this subgroup is supported instead by prospectively planned subgroup analyses of the PATENT-1/PATENT-2 registration trials (see Literature Evidence).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26135803](https://pubmed.ncbi.nlm.nih.gov/26135803/) | 2015 | RCT (PATENT-1 CHD subgroup) | Heart | Riociguat improved exercise capacity and haemodynamics in the PAH-CHD subgroup of the pivotal PATENT-1/PATENT-2 trials |
| [27457511](https://pubmed.ncbi.nlm.nih.gov/27457511/) | 2017 | RCT (PATENT-1 CTD subgroup) | Annals of the Rheumatic Diseases | Prospectively planned subgroup analysis showing safety and efficacy of Riociguat in PAH-CTD |
| [28671485](https://pubmed.ncbi.nlm.nih.gov/28671485/) | 2017 | Case series (REPLACE trial) | Pulmonary Circulation | Case series on switching from PDE-5 inhibitors to Riociguat in PAH-CTD patients |
| [38378970](https://pubmed.ncbi.nlm.nih.gov/38378970/) | 2024 | Systematic Review/Meta-analysis | Internal and Emergency Medicine | Meta-analysis of RCT subgroup/post-hoc data for PAH-CTD treatment, including functional class, survival and 6MWD outcomes |
| [40331647](https://pubmed.ncbi.nlm.nih.gov/40331647/) | 2025 | Cohort | Kardiologiia | Long-term observational survival data in PAH associated with connective tissue/rheumatic diseases |
| [35412560](https://pubmed.ncbi.nlm.nih.gov/35412560/) | 2022 | Review | JAMA | General diagnosis and treatment review of PAH, relevant background context |
| [37765060](https://pubmed.ncbi.nlm.nih.gov/37765060/) | 2023 | Review | Pharmaceuticals (Basel) | Review of treatment advances in PAH-CTD, including sGC stimulators |
| [33131480](https://pubmed.ncbi.nlm.nih.gov/33131480/) | 2020 | Review | Kardiologiia | Review of Riociguat's role in PAH associated with systemic connective tissue disease |
| [27941129](https://pubmed.ncbi.nlm.nih.gov/27941129/) | 2017 | Guideline | Annals of the Rheumatic Diseases | EULAR systemic sclerosis treatment recommendations, referencing PAH management |
| [39985455](https://pubmed.ncbi.nlm.nih.gov/39985455/) | 2025 | Preclinical/mechanistic | Rheumatology (Oxford) | Describes next-generation sGC activator (avenciguat) building on Riociguat's established PAH mechanism, noting potential antifibrotic effects relevant to CTD |

---

## Australia Market Information

Riociguat has **0 ARTG entries** and is currently **not marketed in Australia**. No product listings, dosage forms, or Australian-approved indication text are available in this evidence pack.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No structured safety warnings, contraindications, or drug interaction data were available in this evidence pack (TFDA/TGA labelling data collection is flagged as a **blocking** data gap — DG001).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two mechanistically coherent PAH subgroup indications (CTD and CHD aetiology) are supported by prospectively planned Phase 3 RCT subgroup analyses from the PATENT-1/PATENT-2 registration programme, consistent with Riociguat's established PAH mechanism of action — this meets L2 evidence criteria. However, the drug is not currently registered in Australia and formal safety/labelling data could not be retrieved, so full evaluation cannot yet proceed to a Go decision.

**To proceed, the following is needed:**
- TGA/PI safety data (warnings, contraindications, DDI) — currently blocking (DG001)
- Formal mechanism-of-action documentation from DrugBank or sponsor dossier (DG002)
- Confirmation of local (Australian) regulatory pathway, given 0 current ARTG entries
- Dedicated efficacy/safety data for the PAH-CTD and PAH-CHD subgroups beyond post-hoc/subgroup analyses, ideally a prospective Australian or regional cohort
- Clarification that the top TxGNN-ranked candidates in this pack (hypertrichosis, periodontal malformation, Dandy-Walker syndrome, hair shaft abnormality) require no further action given absence of any supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

