---
layout: default
title: Bromazepam
parent: 僅模型預測 (L5)
nav_order: 105
evidence_level: L5
indication_count: 10
---

# Bromazepam
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

# Bromazepam: From Generalised Anxiety Disorder to Migraine Disorder

## One-Sentence Summary

Bromazepam is a benzodiazepine anxiolytic with established international use for generalised anxiety disorder, though it has never been registered in Australia and carries no ARTG entries.
The TxGNN model ranks **Migraine Disorder** as its highest-scoring predicted new indication (99.06%); however, only **1 indirectly relevant clinical trial** and **no direct publications** currently support this direction, placing this prediction at Evidence Level L4.
The Evidence Pack also reveals a notable parallel finding: the **Anxiety** indication (Rank 6) carries Level L1 evidence with a "Proceed with Guardrails" recommendation, largely confirming established pharmacology rather than representing genuine repurposing.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Generalised Anxiety Disorder (established international use; no Australian registration) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data for Bromazepam is not currently available from DrugBank. Based on established pharmacology, Bromazepam is a 1,4-benzodiazepine that acts as a positive allosteric modulator of GABA-A receptors. By binding to the benzodiazepine allosteric site, it enhances chloride ion influx in response to GABA, thereby reducing neuronal excitability. This core mechanism gives rise to its anxiolytic, sedative, anticonvulsant, and muscle-relaxant properties — effects shared across the benzodiazepine class.

The predicted link to migraine disorder is mechanistically indirect. GABA-A receptor enhancement could theoretically reduce the frequency and propagation of cortical spreading depression (CSD) — the wave of neuronal and glial depolarisation widely regarded as the physiological correlate of migraine aura and an upstream trigger of headache pain pathways. By damping neuronal hyperexcitability, GABAergic agents may interrupt CSD initiation or slow its propagation velocity. However, this reasoning is grounded in general GABAergic inhibition principles and lacks Bromazepam-specific preclinical or clinical validation for migraine.

The TxGNN model's overall reliability for this drug can be partially assessed through the **Anxiety** prediction (Rank 6): multiple Bromazepam-specific RCTs dating from the 1970s to 1990s confirm its anxiolytic efficacy (Evidence Level L1), validating the model's capacity to correctly identify known pharmacological targets. The migraine prediction, by contrast, represents a more speculative extrapolation where direct clinical evidence is currently absent, and the mechanistic bridge — while biologically plausible — has not been tested in dedicated studies.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT04410536](https://clinicaltrials.gov/study/NCT04410536) | Phase 4 | Completed | 25 | Home-withdrawal programme for medication overuse headache (MOH) during COVID-19; behavioural approach with one-year follow-up. Bromazepam, if present in this trial, likely functioned as an adjunct for managing withdrawal-related anxiety or sleep disturbance — not as a direct migraine treatment. Trial design does not support causal inference for Bromazepam in migraine. Sample size (n=25) is too small for meaningful efficacy conclusions. |

> No ANZCTR (Australian New Zealand Clinical Trials Registry) trials were identified for this indication.

---

## Literature Evidence

Currently no direct publications supporting Bromazepam use in Migraine Disorder are available.

---

## Australia Market Information

Bromazepam is not registered in Australia and has no ARTG entries. The drug is marketed internationally under brand names including **Lexotan** and **Lexomil** (primarily in Europe and South America) for anxiety disorders, but has never received TGA approval.

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|------------|--------------|-------------|---------------------|
| — | Not registered in Australia | — | No TGA approval on record |

Any clinical use in Australia would require access via the TGA Special Access Scheme (SAS Category B) or Authorised Prescriber pathway, given the absence of an approved product.

---

## Safety Considerations

No TGA-approved Product Information (PI) is available for Bromazepam in Australia, and no drug interaction data was retrievable. Please refer to international reference sources (such as the EU Summary of Product Characteristics for Lexotan) for comprehensive safety information.

As a benzodiazepine, the following class-effect safety considerations are clinically relevant:

- **Dependence and withdrawal**: Physical dependence can develop with regular use beyond 2–4 weeks; abrupt discontinuation may precipitate withdrawal seizures, severe anxiety rebound, and autonomic instability
- **CNS depression**: Impaired psychomotor performance and cognitive function; additive CNS depression with alcohol, opioids, antihistamines, and other sedatives
- **Falls and fracture risk**: Particular concern in elderly patients due to sedation, incoordination, and increased reaction time
- **Respiratory depression**: Caution required in patients with chronic respiratory insufficiency, obstructive sleep apnoea, or neuromuscular disease
- **Paradoxical reactions**: Agitation, disinhibition, aggression, and increased anxiety have been reported, particularly in elderly patients and those with personality disorders
- **Pregnancy and lactation**: Benzodiazepines cross the placenta and are excreted in breast milk; use in pregnancy and breastfeeding requires careful risk–benefit assessment

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While Bromazepam's GABAergic mechanism provides a biologically plausible theoretical basis for migraine prophylaxis via CSD suppression, the evidence base for this specific indication is currently insufficient for clinical translation. Only one indirectly relevant completed trial was identified (n=25, Grade C relevance), and no direct Bromazepam migraine literature exists. The mechanistic hypothesis has not been tested in preclinical CSD models or in any human migraine study.

**Important parallel finding from this Evidence Pack:**
The **Anxiety** indication (Rank 6, Evidence Level L1, 4 clinical trials, 20 publications) carries a **"Proceed with Guardrails"** recommendation and is supported by multiple Bromazepam-specific double-blind RCTs. While this confirms established pharmacology rather than identifying a genuinely novel repurposing opportunity, it raises a separate and clinically relevant question: whether Bromazepam warrants consideration for a Special Access Scheme (SAS) pathway in Australia for anxiety management, given the absence of any current TGA registration despite its established international evidence base.

**To advance the Migraine Disorder indication, the following is needed:**

- **Preclinical validation**: In vivo CSD model studies (e.g., topical KCl application in rodents) to determine whether Bromazepam specifically reduces CSD frequency, threshold, or propagation velocity compared to other benzodiazepines
- **Systematic literature review**: A scoping review of the broader benzodiazepine class in migraine prophylaxis, to assess whether any class-level evidence justifies a Bromazepam-specific programme
- **Pharmacokinetic/pharmacodynamic profiling**: CNS penetration, half-life suitability, and optimal dosing windows for a CNS migraine target
- **Regulatory scoping**: TGA consultation regarding a regulatory pathway for an unlisted indication with no current ARTG registration; consider whether SAS Category B is the appropriate entry point
- **Safety monitoring plan**: Given dependence risk, any future clinical investigation would require a robust monitoring and exit-strategy protocol
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

