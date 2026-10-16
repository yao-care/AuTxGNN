---
layout: default
title: Flunitrazepam
parent: Model Prediction Only (L5)
nav_order: 305
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Flunitrazepam: predicted new indication Insomnia . Best-supported new candidate: alcohol withdrawal delirium (evidence level L5). Approved use: Not stated in the data compiled for this report . Publi…"
monitor_inn: "Flunitrazepam"
predicted_indications: ["insomnia (disease)", "migraine disorder", "migraine with brainstem aura", "anxiety", "anxiety disorder", "alcohol withdrawal delirium", "migraine with or without aura, susceptibility to", "agoraphobia", "benign paroxysmal torticollis of infancy", "atrophoderma vermiculata"]
---

# Flunitrazepam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Flunitrazepam: From Insomnia to Insomnia (Existing Use), with Alcohol Withdrawal Delirium as the Best-Supported New Direction

## One-Sentence Summary

Flunitrazepam is a benzodiazepine hypnotic registered in Australia as Hypnodorm 1 mg tablets and used for severe insomnia.
The TxGNN model's top prediction is **insomnia**, which is an existing use rather than true repurposing. The most plausible genuinely new indication is **alcohol withdrawal delirium**, supported by **no registered clinical trials** and only a handful of older, small clinical reports (about 3 publications of direct relevance).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the ARTG entry has no indication text). Published sources describe use as a hypnotic for severe insomnia |
| Predicted New Indication | Insomnia (top-ranked prediction; already an established use). Best-supported new candidate: alcohol withdrawal delirium |
| TxGNN Prediction Score | 99.89% (insomnia); 99.50% (alcohol withdrawal delirium) |
| Evidence Level | L3 (insomnia and alcohol withdrawal delirium); L5 for most other predictions |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold (for repurposing); Proceed with Guardrails only for a focused research question in alcohol withdrawal delirium |

---

## Why is This Prediction Reasonable?

Flunitrazepam is a benzodiazepine. It acts on GABA-A receptors (including the α1, α2, α3 and α5 subunits), enhancing inhibitory neurotransmission and producing sedative-hypnotic effects. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description is based on receptor-binding data and general pharmacology.

**Insomnia:** The top prediction reflects the drug's existing use. It is marketed as a hypnotic in many countries, so this is not a new indication.

**Alcohol withdrawal delirium:** Chronic alcohol exposure alters GABA-A and NMDA receptor function, and withdrawal produces GABAergic hypofunction. Benzodiazepines are standard therapy for this condition, so a mechanistic link is strong. However, flunitrazepam offers no clear advantage over established agents such as diazepam or lorazepam, and it carries abuse concerns.

**Other predictions:** Migraine entities, benign paroxysmal torticollis of infancy and atrophoderma vermiculata are prediction-only, with no supporting literature or trials. Their scores likely reflect network proximity in the knowledge graph rather than biological rationale. Anxiety, anxiety disorder and agoraphobia have only class-level or indirect support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered, for any of the predicted indications.

---

## Literature Evidence

**Alcohol withdrawal delirium (best-supported new indication)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8214408](https://pubmed.ncbi.nlm.nih.gov/8214408/) | 1993 | Open clinical trial | Alcohol Clin Exp Res | IV flunitrazepam infusions in 25 patients with alcohol withdrawal delirium |
| [6123125](https://pubmed.ncbi.nlm.nih.gov/6123125/) | 1981 | Clinical report | Psychiatr Pol | Flunitrazepam in delirium tremens |
| [42267](https://pubmed.ncbi.nlm.nih.gov/42267/) | 1979 | Preliminary report | Activitas Nervosa Superior | Flunitrazepam in delirium tremens |
| [1329785](https://pubmed.ncbi.nlm.nih.gov/1329785/) | 1992 | Preclinical | Alcohol Alcohol | GABA-A receptor changes with alcohol dependence |

**Insomnia (existing use)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6108205](https://pubmed.ncbi.nlm.nih.gov/6108205/) | 1980 | Review | Drugs | Pharmacology and therapeutic use; fast-onset hypnotic effect |
| [6114852](https://pubmed.ncbi.nlm.nih.gov/6114852/) | 1981 | Review | Drugs | Triazolam review; flunitrazepam noted as longer acting |
| [430730](https://pubmed.ncbi.nlm.nih.gov/430730/) | 1979 | Clinical study | JAMA | Rebound insomnia after withdrawal of flunitrazepam and other benzodiazepines |
| [8519370](https://pubmed.ncbi.nlm.nih.gov/8519370/) | 1993 | Clinical pharmacology | Eur Respir J | Single-dose effects on blood gases and breathing in severe COPD |
| [20171127](https://pubmed.ncbi.nlm.nih.gov/20171127/) | 2010 | Clinical pharmacology | Sleep Med Rev | Hypnotics impair balance and standing steadiness (fall risk) |

**Anxiety and anxiety disorder (indirect only)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6108205](https://pubmed.ncbi.nlm.nih.gov/6108205/) | 1980 | Review | Drugs | Hypnotic effect predominates over anxiolytic effect |
| [9169981](https://pubmed.ncbi.nlm.nih.gov/9169981/) | 1997 | Review | J Clin Psychopharmacol | Abuse liability of flunitrazepam |
| [40704033](https://pubmed.ncbi.nlm.nih.gov/40704033/) | 2025 | Systematic review | Front Psychiatry | Network meta-analysis of adverse events of insomnia drugs |

The remaining retrieved papers on anxiety focus on abuse, toxicity, memory impairment and driving, not efficacy. No flunitrazepam-specific efficacy evidence was found for anxiety disorder, agoraphobia or migraine.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 4216X | Hypnodorm | Tablet 1 mg (oral) | Not stated in the data compiled for this report |

---

## Safety Considerations

- **Drug interactions / pharmacology:** The interaction data compiled for this report list target-binding information only, not drug-drug interactions. Flunitrazepam binds GABA-A receptor α1, α2, α3 and α5 subunits.
- **Alcohol and CNS depressants:** Published studies show that alcohol potentiates the depressant effects of flunitrazepam (rat study, 2024).
- **Rebound insomnia and withdrawal:** Rebound insomnia has been documented after withdrawal of flunitrazepam.
- **Abuse and misuse:** The literature documents high abuse liability, use as a "date rape" drug, and involvement in fatal intoxications.
- **Cognitive and psychomotor effects:** Dose-related memory and psychomotor impairment, anterograde amnesia, paradoxical agitation or aggression in some users, and impaired driving ability are reported.
- **Older people:** Increased sensitivity to benzodiazepines, impaired balance and increased fall risk.
- **Respiratory disease:** Particular caution is needed in severe COPD, given the depressant effects on respiratory control.

For labelled warnings and contraindications, please refer to the TGA-approved Product Information (PI).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Insomnia is an existing use, so it is not a repurposing opportunity. Alcohol withdrawal delirium is the best-supported new direction, but evidence is limited to small, older, largely uncontrolled reports with no registered trials, and flunitrazepam has no clear advantage over established benzodiazepines. Abuse liability, rebound effects and fall risk further limit any recommendation. Other predictions (migraine, atrophoderma vermiculata, benign paroxysmal torticollis of infancy) are model outputs without supporting evidence.

**To proceed, the following is needed:**
- The ARTG approved indication text and the PI warnings and contraindications for Hypnodorm (currently missing)
- Mechanism of action data from DrugBank
- A comparative review against diazepam and lorazepam for alcohol withdrawal delirium, including an Australian clinical guideline check
- Any trial registrations (including ANZCTR) in alcohol withdrawal; none were found in the data compiled
- A risk assessment covering controlled-substance status, abuse potential and monitoring requirements in hospital settings
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

