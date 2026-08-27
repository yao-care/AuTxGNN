---
layout: default
title: Nitrazepam
parent: 僅模型預測 (L5)
nav_order: 472
evidence_level: L5
indication_count: 10
---

# Nitrazepam
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

# Nitrazepam: From Insomnia to Sleep Disorder, Initiating and Maintaining Sleep

## One-Sentence Summary

Nitrazepam is a long-established benzodiazepine hypnotic, marketed internationally (e.g. Mogadon in the UK) for the short-term treatment of insomnia, but it is **not currently registered in Australia** (no ARTG entry). The TxGNN model's top prediction for this drug is **Sleep Disorder, Initiating and Maintaining Sleep** — clinically synonymous with insomnia — meaning this is less a novel repurposing signal and more a confirmation of the drug's already well-documented use, supported by **20 publications** and its class-level pharmacology. No clinical trials specific to this indication were located in the evidence pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in formal regulatory data; internationally established as a hypnotic for short-term insomnia treatment (not TGA-registered) |
| Predicted New Indication | Sleep disorder, initiating and maintaining sleep (insomnia) |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action documentation is not available in this evidence pack (data gap). However, based on the evidence supplied, nitrazepam is a classical **1,4-benzodiazepine** that acts as a **positive allosteric modulator of the GABA-A receptor**, producing sedative-hypnotic effects — the core and original pharmacological action of this drug class.

The predicted indication (sleep disorder, initiating and maintaining sleep) is not a mechanistic extrapolation to a new disease area but a direct match to nitrazepam's long-standing clinical role as a hypnotic. Multiple decades of literature (e.g. comparative studies against triazolam, flurazepam, temazepam and loprazolam) confirm its efficacy in inducing and maintaining sleep, consistent with GABAergic sedation.

Because this "new" indication overlaps with the drug's already-recognised use overseas, the prediction should be read as **validating** TxGNN against known ground truth rather than surfacing a genuinely novel therapeutic hypothesis. The practical question for Australia is one of **market entry/registration**, not of new-indication research.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6135296](https://pubmed.ncbi.nlm.nih.gov/6135296/) | 1983 | RCT (double-blind cross-over) | Acta Psychiatrica Scandinavica | Nitrazepam 5mg vs triazolam 0.25mg in 26 geriatric inpatients; similar sleep quantity/quality and psychomotor performance, no significant difference between drugs |
| [7037262](https://pubmed.ncbi.nlm.nih.gov/7037262/) | 1981 | PK study | Clinical Pharmacokinetics | Review of nitrazepam's clinical pharmacokinetic profile |
| [4892037](https://pubmed.ncbi.nlm.nih.gov/4892037/) | 1969 | Review | British Medical Journal | In 27 patients, nitrazepam overdose (up to 80 tablets) caused only drowsiness; double-blind trial found it as effective as butobarbitone as a hypnotic — concluded safe and effective |
| [1125532](https://pubmed.ncbi.nlm.nih.gov/1125532/) | 1975 | Case report/Review (dependence) | The British Journal of Psychiatry | Documents nitrazepam (Mogadon) dependence |
| [4712500](https://pubmed.ncbi.nlm.nih.gov/4712500/) | 1973 | Review | British Medical Journal | Nitrazepam and effects on the subconscious/sleep architecture |
| [238826](https://pubmed.ncbi.nlm.nih.gov/238826/) | 1975 | Review | Drugs | Overview of sleep physiology and hypnotic drug effectiveness, including benzodiazepines |
| [19450355](https://pubmed.ncbi.nlm.nih.gov/19450355/) | 2007 | Review | BMJ Clinical Evidence | Up to 40% of adults have insomnia; reviews risk factors and treatment approaches including hypnotics |
| [7725291](https://pubmed.ncbi.nlm.nih.gov/7725291/) | 1995 | Review | Tidsskrift for den Norske Lægeforening | Reviews classification, diagnosis and treatment of insomnia, including hypnotic therapy |
| [20467592](https://pubmed.ncbi.nlm.nih.gov/20467592/) | 2010 | Review | Drugs of Today | Reviews benzodiazepine and non-benzodiazepine hypnotics' effects on sleep induction/maintenance vs newer serotonergic agents |
| [2874007](https://pubmed.ncbi.nlm.nih.gov/2874007/) | 1986 | Review (comparator drug) | Drugs | Review of loprazolam, a comparator hypnotic benzodiazepine, contextualising nitrazepam's therapeutic class |

---

## Australia Market Information

Nitrazepam has **no ARTG entries** and is **not currently marketed in Australia**. No product name, dosage form, or approved indication text is available from local regulatory sources.

---

## Safety Considerations

No drug-specific safety data (warnings, contraindications, or drug interactions) is available in this evidence pack — nitrazepam is not TGA-registered, so no Australian Product Information exists. Prescribers considering this drug should refer to overseas regulatory documentation (e.g. UK MHRA, EU SmPC) for benzodiazepine class safety information, including known risks of dependence, tolerance, residual sedation, and withdrawal, pending formal TGA assessment.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence level (L1) reflects a large, mature literature base and an RCT directly comparing nitrazepam to another hypnotic, but this indication is effectively confirmatory of an already-established overseas use rather than a novel repurposing finding. Since nitrazepam has zero ARTG entries, the real decision is a market-entry evaluation, not a new-indication research question — hence guardrails rather than an unconditional "Go."

**To proceed, the following is needed:**
- TFDA/TGA-equivalent product label, warnings and contraindications (Blocking data gap — required before any S1 safety assessment)
- Formal mechanism-of-action documentation from DrugBank or equivalent source
- A drug interaction (DDI) dataset, as the current query returned no results
- A regulatory pathway assessment for ARTG registration, since Nitrazepam is currently unavailable in Australia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

