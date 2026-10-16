---
layout: default
title: Oxycodone
parent: Model Prediction Only (L5)
nav_order: 538
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Oxycodone: predicted new indication Restless legs syndrome (evidence level L5). Approved use: Not stated in the data compiled for this report"
monitor_inn: "Oxycodone"
predicted_indications: ["methemoglobinemia", "restless legs syndrome", "myofascial pain syndrome", "methemoglobinemia, alpha type", "common cold", "nephrogenic syndrome of inappropriate antidiuresis", "headache disorder", "tendinitis", "idiopathic granulomatous myositis", "myositis fibrosa"]
---

# Oxycodone
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

# Oxycodone: From Opioid Analgesia to Restless Legs Syndrome

## One-Sentence Summary

Oxycodone is an opioid analgesic that is marketed in Australia as an oral capsule.
The TxGNN model predicts it may be effective for **Restless Legs Syndrome (RLS)**,
with **1 completed Phase 3 clinical trial** and **19 publications** currently supporting this direction. The trial and most of the literature concern the prolonged-release oxycodone-naloxone combination rather than oxycodone alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the ARTG entry has no approved indication text) |
| Predicted New Indication | Restless legs syndrome |
| TxGNN Prediction Score | 90.35% |
| Evidence Level | L1 (as assigned in the data compiled for this report; see note below) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

*Note:* Under the stated grading rules, L1 requires at least two completed Phase 3 RCTs. Only one completed Phase 3 RCT is listed, so a stricter reading would place this at L2. Supporting Phase 3 data in the published literature may account for the higher grade, but this should be confirmed.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Oxycodone is a mu-opioid receptor agonist (general pharmacological knowledge, not drawn from the compiled data). Opioids act on the endogenous opioid system and modulate the dopaminergic and sensory pathways implicated in RLS. The literature itself notes that the mechanisms of opioids in RLS are still a matter of speculation.

The link between the original use (pain relief) and RLS is mainly through the shared opioid pathways rather than through a similar disease process. Prolonged-release oxycodone-naloxone has been studied in severe, treatment-refractory RLS. It is approved in Europe as second-line treatment for severe to very severe idiopathic RLS after dopaminergic therapy has failed. Guidelines and evidence-based reviews generally position opioids as a later-line option, after dopamine agonists and alpha-2-delta ligands.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01112644](https://clinicaltrials.gov/study/NCT01112644) | Phase 3 | Completed | 205 | Randomised, double-blind, placebo-controlled, multicentre trial of prolonged-release oxycodone-naloxone (OXN PR) versus placebo in moderate to severe idiopathic RLS with daytime symptoms. The primary aim was to show superior improvement in RLS symptom severity over a 12-week period. |

The trial title is truncated in the data, so its RLS focus should be confirmed from the full record. No ANZCTR trials were identified.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39324694](https://pubmed.ncbi.nlm.nih.gov/39324694/) | 2025 | Guideline | J Clin Sleep Med | American Academy of Sleep Medicine clinical practice guideline on treatment of RLS and periodic limb movement disorder |
| [27355187](https://pubmed.ncbi.nlm.nih.gov/27355187/) | 2016 | Systematic review | Cochrane Database Syst Rev | Cochrane review of opioids for RLS |
| [29756335](https://pubmed.ncbi.nlm.nih.gov/29756335/) | 2018 | Evidence-based review | Mov Disord | Revised review of RCTs; oxycodone/naloxone, pregabalin and gabapentin enacarbil are now considered efficacious |
| [23746768](https://pubmed.ncbi.nlm.nih.gov/23746768/) | 2014 | Meta-analysis | Sleep Med Rev | Meta-analyses of dopaminergic and non-dopaminergic RLS treatments |
| [26135898](https://pubmed.ncbi.nlm.nih.gov/26135898/) | 2015 | Review | CNS Drugs | Oxycodone/naloxone PR is approved in Europe as second-line treatment for severe refractory RLS |
| [26966363](https://pubmed.ncbi.nlm.nih.gov/26966363/) | 2016 | Review | Neuropsychiatr Dis Treat | Role of prolonged-release oxycodone-naloxone in intractable RLS |
| [33985652](https://pubmed.ncbi.nlm.nih.gov/33985652/) | 2021 | Review | Sleep Med Clin | Alpha-2 ligands are first-line; opioids such as oxycodone-naloxone are second-line |
| [27964861](https://pubmed.ncbi.nlm.nih.gov/27964861/) | 2017 | Review | Sleep Med | Opioids relieve sensory and motor RLS symptoms and improve sleep; mechanisms remain uncertain |
| [26215616](https://pubmed.ncbi.nlm.nih.gov/26215616/) | 2015 | Review | Nat Rev Neurol | Current RLS therapies and management of augmentation |
| [30244828](https://pubmed.ncbi.nlm.nih.gov/30244828/) | 2018 | Review | Lancet Neurol | Comorbidities, treatment and pathophysiology in RLS |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12031F | Oxycodone BNM | Capsule containing oxycodone hydrochloride 10 mg | Not stated in the data compiled for this report |

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from a drug-disease knowledge graph, not product label text): liver failure and liver disease, kidney disease, respiratory failure, epilepsy, hypothyroidism, inflammatory bowel disease, substance abuse/dependence, myocardial infarction, sudden cardiac arrest, heart conduction disease, hypotensive disorder, benign prostatic hyperplasia, gallbladder disease, and others.
- **Drug Interactions** (100 interactions recorded; examples of Major level): alvimopan, bupropion, aprepitant, morphine, dexamethasone, cimetidine, clarithromycin and clotrimazole. Moderate-level examples include hyoscyamine, loperamide, atropine, glycopyrronium and eluxadoline.
- **Literature-reported risks**: dependence, misuse, respiratory depression and sleep-disordered breathing, and augmentation or tolerance with long-term use.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

---

## Other Predicted Indications (Brief Note)

The other top-ranked predictions are not supported and are on Hold. Methemoglobinemia (including the alpha type), nephrogenic syndrome of inappropriate antidiuresis, idiopathic granulomatous myositis and myositis fibrosa have no clinical trials or literature and no plausible mechanism. Common cold, headache disorder, tendinitis and myofascial pain syndrome have only indirect or irrelevant evidence, and opioids are generally discouraged for these conditions.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed, randomised, placebo-controlled Phase 3 trial and several reviews and guidelines support prolonged-release oxycodone-naloxone in severe, refractory RLS. However, the evidence relates to the combination product, not the immediate-release oxycodone capsule registered in Australia, and the safety profile requires careful control.

**To proceed, the following is needed:**
- Confirmation of the full trial record (NCT01112644) and its efficacy results
- Clarification of whether evidence for the oxycodone-naloxone prolonged-release combination can be applied to the single-ingredient capsule listed on the ARTG
- Guardrails: reserve for severe, intractable RLS after dopamine agonists and alpha-2-delta ligands have failed; do not use as first-line therapy; use the lowest effective dose; review regularly; monitor for dependence, misuse, respiratory depression and sleep-disordered breathing
- The ARTG approved indication and the TGA Product Information warnings and contraindications
- Mechanism of action data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

