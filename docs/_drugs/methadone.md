---
layout: default
title: Methadone
parent: 僅模型預測 (L5)
nav_order: 430
evidence_level: L5
indication_count: 10
---

# Methadone
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

# Methadone: From Opioid Use Disorder / Chronic Pain to Tourette Syndrome

## One-Sentence Summary

Methadone is a long-acting synthetic opioid agonist established for opioid use disorder maintenance therapy and chronic pain management. The TxGNN model predicts it may be effective for **Tourette Syndrome**, with a prediction score of **99.76%**, but this direction is currently supported by only **1 case report** specific to methadone and no registered clinical trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Opioid use disorder maintenance therapy / chronic pain management (general pharmacological knowledge — no approved-indication text available in the evidence pack, as the drug is not marketed in Australia) |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (flagged as a High-severity data gap, DG002). Based on general pharmacological knowledge, methadone is a synthetic μ-opioid receptor full agonist with secondary NMDA-receptor antagonist and monoamine reuptake-inhibiting activity, and its efficacy in opioid dependence and chronic pain is well established.

The evidence pack's own rationale proposes that the opioid system interacts with striatal dopamine regulation, and this could theoretically influence tic expression in Tourette syndrome. However, this mechanistic link rests almost entirely on a single 1992 case report ("Methadone treatment of Tourette's disorder," PMID 1728167). The remaining supporting literature is largely tangential — a review of non-genetic causes of chorea, a cohort study on heroin addiction comorbidity in Tourette patients, and a pharmacology review on opiates in OCD/Tourette syndrome via 5-HT2A/C signalling — none of which directly evaluate methadone as a Tourette treatment.

Given the absence of clinical trials and the reliance on one dated case report, the biological plausibility is not yet matched by clinical evidence strong enough to support progression beyond exploratory screening.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17102981](https://pubmed.ncbi.nlm.nih.gov/17102981/) | 2007 | Basic/pharmacology review | Psychopharmacology | Reviews atypical opiates' role in OCD via 5-HT(2A/C)-mediated behaviour; notes opiate drugs are effective in treatment-refractory OCD and Tourette syndrome |
| [15247538](https://pubmed.ncbi.nlm.nih.gov/15247538/) | 2004 | Review | Current opinion in neurology | Reviews non-genetic causes of chorea; discusses neuropsychiatric mechanisms related to Sydenham's chorea; not specific to methadone |
| [1728167](https://pubmed.ncbi.nlm.nih.gov/1728167/) | 1992 | Case report | The American Journal of Psychiatry | "Methadone treatment of Tourette's disorder" — the only report directly on methadone in Tourette syndrome; abstract unavailable, single-case evidence only |
| [30395551](https://pubmed.ncbi.nlm.nih.gov/30395551/) | 2018 | Cohort | Journal of Psychiatric Practice | Examines heroin addiction comorbidity in Tourette syndrome patients; addresses comorbidity, not treatment |
| [39086469](https://pubmed.ncbi.nlm.nih.gov/39086469/) | 2024 | Review | Palliative Care and Social Practice | Reviews novel analgesics (haloperidol, miragabalin, PEA, clonidine) for neuropathic pain; not specific to methadone or Tourette syndrome |

---

## Australia Market Information

Methadone is currently **not marketed** in Australia under this evidence pack's dataset — no ARTG entries were found (`total_licenses: 0`).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Note: warning/contraindication data collection for this candidate is flagged as a **Blocking** data gap (DG001 — TFDA label warnings/contraindications not yet retrieved), which prevents formal safety pre-screening (S1) at this time.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link is biologically plausible but supported by only one 1992 single-case report specific to methadone in Tourette syndrome, with no clinical trials and no completed safety review (blocked pending label data). This does not meet the threshold to proceed further.

**To proceed, the following is needed:**
- TGA/TFDA-approved Product Information — warnings and contraindications (DG001, blocking)
- DrugBank mechanism of action data (DG002)
- Prospective or controlled studies evaluating methadone specifically in Tourette syndrome
- Consider evaluating **migraine disorder** (rank 8 in this evidence pack) separately — it already carries a more advanced decision stage (S1, "Research Question") with broader literature support (19 PubMed hits including a prospective cohort and an American Headache Society guideline review), and may be a more tractable near-term candidate than Tourette syndrome.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

