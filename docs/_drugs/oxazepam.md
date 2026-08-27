---
layout: default
title: Oxazepam
parent: 僅模型預測 (L5)
nav_order: 499
evidence_level: L5
indication_count: 10
---

# Oxazepam
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

# Oxazepam: From Benzodiazepine Anxiolytic/Sedative to Insomnia

## One-Sentence Summary

Oxazepam is a benzodiazepine classically used as an anxiolytic and sedative-hypnotic, and is **not currently marketed in Australia** (0 ARTG entries). The TxGNN model predicts it may be effective for **Insomnia**, with **no registered clinical trials** but **11 supporting publications** — including two direct head-to-head RCTs from the 1980s–2010s — largely confirming a use already well within this drug class's known pharmacology rather than revealing a mechanistically novel indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack — Oxazepam has no ARTG-registered product in Australia. Internationally it is classified as a benzodiazepine anxiolytic/sedative-hypnotic. |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L2 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on established pharmacological knowledge, Oxazepam is a benzodiazepine that acts as a positive allosteric modulator of the GABA-A receptor chloride channel, producing anxiolytic and sedative-hypnotic effects. This is the same underlying pathway that drives its potential utility in insomnia.

The relationship between Oxazepam's known pharmacological class and the predicted indication is very close rather than distant: benzodiazepines with sedative-hypnotic activity are an established treatment category for insomnia, and several of the retrieved publications directly test oxazepam against other hypnotics in patients with chronic or age-related insomnia (e.g., PMID 6691478, PMID 6138067). Notably, TxGNN separately scored a near-duplicate disease-ontology node, "sleep disorder, initiating and maintaining sleep" (96.30%), which the evidence pack itself identifies as the same clinical concept under a different terminology entry — an internal consistency check that corroborates the insomnia signal.

Mechanistically, oxazepam's favourable pharmacokinetic profile supports this link further: it is metabolised solely by hepatic glucuronidation with no active metabolites, making it comparatively suitable for elderly patients or those with hepatic impairment relative to other benzodiazepines — populations in which insomnia and its pharmacological management are common concerns. It is worth flagging directly, however, that this "new indication" substantially overlaps with the drug's already-recognised sedative-hypnotic use in other jurisdictions; the evidence here largely reconfirms known pharmacology rather than surfacing a genuinely novel repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6691478](https://pubmed.ncbi.nlm.nih.gov/6691478/) | 1984 | RCT | The American Journal of Psychiatry | Oxazepam and flurazepam both improved polysomnographic sleep measures in chronic insomnia; unlike flurazepam, oxazepam did not cause substantial daytime sleepiness. |
| [29749262](https://pubmed.ncbi.nlm.nih.gov/29749262/) | 2018 | RCT | The Annals of Pharmacotherapy | Randomised comparison of melatonin vs. oxazepam for anxiety and sleep quality in STEMI patients post-PCI. |
| [17317444](https://pubmed.ncbi.nlm.nih.gov/17317444/) | 2007 | Cohort/Review | Archives of Gerontology and Geriatrics | Effectiveness and safety of hypnotic drugs for insomnia in patients over 70, with comorbid depression/dementia. |
| [29844949](https://pubmed.ncbi.nlm.nih.gov/29844949/) | 2018 | Cohort (retrospective) | PeerJ | Factors associated with long-term benzodiazepine/z-drug use for sleep problems in older populations. |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opinion on Drug Metabolism & Toxicology | Review of anxiolytic drug pharmacokinetics, relevant to benzodiazepine class use in sleep/anxiety disorders. |
| [15633073](https://pubmed.ncbi.nlm.nih.gov/15633073/) | 2005 | Review | Psychiatrische Praxis | Cross-sectional review of BPSD management practice in dementia, including hypnotic/sedative use for sleep disturbance. |
| [36340306](https://pubmed.ncbi.nlm.nih.gov/36340306/) | 2022 | Review | Journal of Clinical and Experimental Hepatology | Alcohol withdrawal management review noting insomnia as a core withdrawal symptom treated with benzodiazepines. |
| [6139491](https://pubmed.ncbi.nlm.nih.gov/6139491/) | 1983 | Case report | JAMA | Withdrawal syndrome after substituting a short-acting (oxazepam) for a long-acting benzodiazepine; relevant to dosing/withdrawal risk in sleep-disorder management. |
| [39544757](https://pubmed.ncbi.nlm.nih.gov/39544757/) | 2024 | Case report | American Journal of Translational Research | Case report on agomelatine-induced sensory abnormality; only tangentially retrieved (low direct relevance to oxazepam/insomnia). |
| [23338224](https://pubmed.ncbi.nlm.nih.gov/23338224/) | 1997 | Review | CNS Drugs | Review of paroxetine for panic disorder; only tangentially retrieved (low direct relevance to oxazepam/insomnia). |

---

## Australia Market Information

Oxazepam has no ARTG-registered products in Australia (0 entries). No market information is available to summarise.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Note that this evidence pack flags the absence of TFDA/TGA label warnings and contraindications as a **Blocking** data gap (DG001) — this must be resolved before any safety evaluation (S1) can proceed. Drug interaction data was queried but not found.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two direct RCTs and several supporting reviews/cohorts (Evidence Level L2) link oxazepam to insomnia management, consistent with its known benzodiazepine pharmacology — but no clinical trials are registered specifically for this indication, the drug is not marketed in Australia, and core safety documentation (MOA, label warnings/contraindications) is still missing.

**To proceed, the following is needed:**
- TGA-approved Product Information / label warnings and contraindications (resolves Blocking gap DG001)
- Detailed mechanism of action documentation from DrugBank or equivalent (resolves High gap DG002)
- Confirmation of drug-drug interaction profile (current query returned "not found")
- If market entry is being considered, a regulatory pathway assessment given the current 0 ARTG entries
- Explicit acknowledgement in any downstream use that the "insomnia" signal substantially overlaps with oxazepam's already-established sedative-hypnotic class effect, rather than representing a mechanistically distant repurposing discovery
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

