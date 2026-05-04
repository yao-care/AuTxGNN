---
layout: default
title: Granisetron
parent: 僅模型預測 (L5)
nav_order: 220
evidence_level: L5
indication_count: 10
---

# Granisetron
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

以下是根據 Evidence Pack 生成的完整評估報告：

---

# Granisetron: From Chemotherapy-Induced Nausea and Vomiting to Manic Bipolar Affective Disorder

## One-Sentence Summary

Granisetron is a selective 5-HT3 receptor antagonist widely approved in multiple countries (including the US, EU, and Japan) for prevention of nausea and vomiting associated with chemotherapy, radiotherapy, and surgery — however, it is currently **not registered in Australia**.
The TxGNN model predicts it may be effective for **Manic Bipolar Affective Disorder**, with **0 clinical trials** and **0 publications** currently supporting this specific direction.
This prediction is based entirely on computational modelling and should be treated as an early-stage hypothesis only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prevention of chemotherapy-induced and radiotherapy-induced nausea and vomiting (based on international registrations; no TGA record) |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed in Australia |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Granisetron is a selective 5-HT3 (serotonin type 3) receptor antagonist. The 5-HT3 receptor is a ligand-gated ion channel found throughout the central and peripheral nervous systems. Granisetron's well-established antiemetic action is primarily mediated via blockade of 5-HT3 receptors in the gastrointestinal tract and chemoreceptor trigger zone (CTZ) of the brainstem. Detailed mechanism of action data specific to its central nervous system effects was not available in the current dataset; the following rationale is based on published pharmacology of the 5-HT3 receptor class.

The predicted link to bipolar affective disorder (manic phase) rests on the broad expression of 5-HT3 receptors in limbic structures, particularly the amygdala and hippocampus — regions strongly implicated in mood regulation and the neurobiology of affective disorders. Serotonergic dysregulation is one of the central neurobiological hypotheses for bipolar disorder, and 5-HT3 receptor modulation could theoretically influence limbic circuit excitability. The 5-HT3 receptor's role as an ionotropic channel also makes it functionally distinct from the G-protein-coupled serotonin receptors targeted by conventional mood stabilisers, which may represent a novel mechanistic angle.

At the drug class level, ondansetron (another 5-HT3 antagonist) has been investigated in scattered animal experiments related to mood disorders and has occasional case report data for affective symptoms. However, granisetron itself has **no human clinical trial data** for the manic phase of bipolar disorder. The mechanistic link is plausible but speculative, and the TxGNN prediction should be interpreted as a hypothesis-generating signal requiring further validation rather than actionable clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Granisetron is currently **not registered with the TGA** and has no ARTG entries. There are no approved products available in Australia.

For reference, granisetron is registered in multiple other jurisdictions for:
- Prevention of nausea and vomiting associated with initial and repeat courses of emetogenic cancer chemotherapy
- Prevention and treatment of postoperative nausea and vomiting (PONV)

Any future pathway into the Australian market would require TGA registration (either full evaluation or via a recognised comparable overseas regulator pathway).

---

## Safety Considerations

All safety data for this candidate — including key warnings, contraindications, and drug-drug interactions — were not available in the current evidence dataset.

Please refer to regulatory prescribing information from approved jurisdictions (e.g., the US FDA prescribing information, EMA Summary of Product Characteristics) for complete safety details until an Australian Product Information (PI) is available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.62%) for granisetron in manic bipolar affective disorder, but this prediction rests solely on computational knowledge graph modelling with **zero supporting clinical trials or published literature**. Evidence level L5 means the signal cannot be acted upon clinically without substantial additional groundwork.

**To proceed, the following is needed:**

- **MOA confirmation**: Obtain granisetron's full mechanism of action and CNS pharmacology data from DrugBank (DB00889) and published primary literature, with specific focus on limbic 5-HT3 receptor distribution and blood-brain barrier penetration
- **Class-level evidence search**: Conduct a targeted PubMed search for 5-HT3 antagonist class effects in bipolar disorder, mania, or mood stabilisation (including ondansetron and palonosetron data as surrogate class evidence)
- **Preclinical data review**: Identify animal model studies (e.g., amphetamine-induced hyperactivity, mania-relevant paradigms) testing 5-HT3 receptor blockade
- **PK/PD feasibility assessment**: Evaluate granisetron's CNS bioavailability, receptor occupancy at therapeutic doses, and dosing strategy suitability for a psychiatric indication
- **TGA registration pathway**: If downstream evidence supports advancement, assess TGA registration requirements for a new indication (including whether an overseas registered product could be evaluated under the Comparable Overseas Regulator pathway)
- **Safety data gap remediation**: Obtain and review Australian-relevant prescribing information or equivalent international PI before any clinical planning proceeds
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

