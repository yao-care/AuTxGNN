---
layout: default
title: Pizotifen
parent: 僅模型預測 (L5)
nav_order: 540
evidence_level: L5
indication_count: 10
---

# Pizotifen
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

# Pizotifen: From an Unregistered Status in Australia to Migraine Disorder (Prophylaxis)

## One-Sentence Summary

Pizotifen is a serotonin (5-HT2) receptor antagonist with antihistamine and anticholinergic activity that has never been registered on Australia's ARTG. The TxGNN model's top-ranked prediction is **Migraine Disorder** (prophylaxis), supported by **1 clinical trial** and **20 PubMed records** — but this is not a novel hypothesis: it is pizotifen's long-established traditional indication in other markets, and the model is effectively confirming known pharmacology rather than surfacing a new use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack — Pizotifen has never held an ARTG registration in Australia, so no TGA-approved indication text exists |
| Predicted New Indication | Migraine Disorder (prophylaxis) |
| TxGNN Prediction Score | 98.76% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action data for pizotifen was not returned in this evidence pack (DrugBank query gap). However, the evidence collected for this candidate describes pizotifen as a 5-HT2 serotonin receptor antagonist with additional antihistamine (H1) and anticholinergic activity. This receptor profile maps directly onto the serotonin theory of migraine — cortical spreading depression and trigeminovascular sensitisation — which is the accepted rationale for 5-HT2 antagonists in migraine prophylaxis.

Importantly, the evidence pack's own rationale for this candidate flags that migraine prophylaxis is **pizotifen's traditional, decades-old indication internationally**, not a novel repurposing signal. Several of the supporting publications date from the 1970s–1990s (e.g. comparative trials against metoprolol, cyclandelate, and flunarizine), consistent with an agent whose migraine use is long-standing rather than emerging. The practical significance for Australia is different from a typical repurposing case: the open question here is not "does this mechanism plausibly extend to a new disease," but "why is an internationally recognised migraine prophylactic absent from the ARTG," and what would be needed to bring TGA-quality documentation (PI, safety, DDI) up to a standard suitable for local use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT06158230](https://clinicaltrials.gov/study/NCT06158230) | Phase 2 | Unknown | 140 | Single-blind RCT comparing amitriptyline–propranolol combination vs pizotifen for migraine prophylaxis; asks whether pizotifen outperforms the combination. Status unconfirmed — completion/publication not verified. |

No ANZCTR (Australian) trial identifiers were found for this candidate.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3986895](https://pubmed.ncbi.nlm.nih.gov/3986895/) | 1985 | RCT | Cephalalgia | Double-blind cross-over of pizotifen (0.5mg tid) vs metoprolol (50mg bid) in 35 patients with classical/common migraine; comparable prophylactic effect. |
| [1573338](https://pubmed.ncbi.nlm.nih.gov/1573338/) | 1992 | RCT | Journal of Medicine | Double-blind parallel trial of cyclandelate vs pizotifen in 61 evaluable migraine patients over 12 weeks; comparable efficacy and tolerance. |
| [23416816](https://pubmed.ncbi.nlm.nih.gov/23416816/) | 2013 | RCT | Mymensingh Med J | Compared amitriptyline, pizotifen and propranolol in 90 patients; all reduced attack duration/frequency/severity with no significant between-group difference. |
| [327746](https://pubmed.ncbi.nlm.nih.gov/327746/) | 1977 | RCT | Acta Neurol Scand | Double-blind cross-over of placebo vs Divascan vs pizotifen (3mg/day) in 30 patients; early comparative prophylaxis data. |
| [22683887](https://pubmed.ncbi.nlm.nih.gov/22683887/) | 2012 | Guideline | Can J Neurol Sci | Canadian Headache Society guideline for migraine prophylaxis — evidence-based medication selection framework. |
| [35190383](https://pubmed.ncbi.nlm.nih.gov/35190383/) | 2022 | Review | Arch Dis Child | Narrative review of paediatric migraine management; notes recent large trials of propranolol, pizotifen, topiramate and amitriptyline have generally failed to show robust superiority over placebo in children. |
| [40705288](https://pubmed.ncbi.nlm.nih.gov/40705288/) | 2025 | Cohort | Neurology India | Retrospective study of pizotifen efficacy and tolerance in children with migraine in a Brazilian Amazon cohort. |
| [25217187](https://pubmed.ncbi.nlm.nih.gov/25217187/) | 2014 | Review | Eur J Clin Pharmacol | Review of anti-migraine drug safety in breastfeeding, including pizotifen. |
| [2891428](https://pubmed.ncbi.nlm.nih.gov/2891428/) | 1988 | Review | CMAJ | General migraine therapy review covering beta-blockers, calcium-channel blockers and other prophylactic agents. |
| [6398056](https://pubmed.ncbi.nlm.nih.gov/6398056/) | 1984 | Review | Aust NZ J Med | Review of serotonin antagonists across carcinoid syndrome, migraine, nociception and vascular disease. |

Note: several additional PubMed records were returned for this candidate but were not yet classified by study type (`pending`) in the evidence pack, so they are omitted from this table rather than guessed at.

---

## Australia Market Information

Pizotifen is **not currently registered on the ARTG** (0 entries). No Australian Product Information, brand name, or approved indication text exists for this drug at this time.

---

## Safety Considerations

No safety data (key warnings, contraindications, or drug–drug interactions) were returned for pizotifen in this evidence pack, and because it is not TGA-registered, no Australian Product Information exists to consult. Any clinical use would need to rely on reference-market documentation (e.g. UK/EU SmPC) pending formal Australian evaluation — please do not treat the absence of flagged warnings here as evidence of a clean safety profile.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism (5-HT2 antagonism) and a modest body of older comparative RCTs support pizotifen's efficacy in migraine prophylaxis, and this is an internationally well-established use rather than a speculative new indication. However, the complete absence of Australian registration, PI, MOA documentation, and DDI/contraindication data means this cannot proceed without substantial regulatory and safety work.

**To proceed, the following is needed:**
- Formal DrugBank/manufacturer MOA documentation (currently a data gap)
- TGA/ARTG registration pathway assessment, since pizotifen has never been marketed in Australia
- Reference-market Product Information (safety, contraindications, DDI) as a stopgap pending local approval
- Confirmation of NCT06158230's completion status and any resulting publication
- Explicit framing for stakeholders that this is a confirmatory finding of an established indication, not a novel repurposing signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

