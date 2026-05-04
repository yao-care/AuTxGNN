---
layout: default
title: Desvenlafaxine
parent: 僅模型預測 (L5)
nav_order: 148
evidence_level: L5
indication_count: 10
---

# Desvenlafaxine
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

# Desvenlafaxine: From Major Depressive Disorder to Obsessive-Compulsive Disorder

## One-Sentence Summary

Desvenlafaxine (Pristiq®) is a serotonin-norepinephrine reuptake inhibitor (SNRI) and the primary active metabolite of venlafaxine, approved by the US FDA for Major Depressive Disorder (MDD), though not currently registered on the Australian Register of Therapeutic Goods (ARTG).
The TxGNN model predicts it may be effective for **Obsessive-Compulsive Disorder (OCD)**, with **2 clinical trials** and **4 publications** currently informing this direction — however, neither trial directly evaluated desvenlafaxine as an OCD treatment, placing current evidence at a preclinical/mechanistic level only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Major Depressive Disorder (MDD) — FDA-approved; not TGA-registered in Australia |
| Predicted New Indication | Obsessive-Compulsive Disorder (OCD) |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 (Mechanistic/class-effect reasoning; no direct desvenlafaxine OCD trials) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the source database. Based on established pharmacological knowledge, Desvenlafaxine is the principal active metabolite of venlafaxine and belongs to the SNRI class, which works by inhibiting the reuptake of both serotonin and norepinephrine in the central nervous system. Its efficacy in Major Depressive Disorder has been confirmed through multiple Phase 3 randomised controlled trials supporting its FDA approval.

The serotonin reuptake inhibition (SRI) component is the pharmacological cornerstone of OCD treatment. First-line pharmacotherapies for OCD — SSRIs (e.g., fluvoxamine, sertraline) and clomipramine — all exert their therapeutic effect primarily through serotonergic pathways. SNRIs share this serotonergic mechanism, making class-level extrapolation to OCD biologically plausible. Crucially, the parent compound venlafaxine has been evaluated in a published randomised double-blind trial demonstrating comparable efficacy to paroxetine in OCD (PMID 14624187), providing the most relevant — albeit indirect — clinical anchor for this prediction.

As desvenlafaxine's pharmacological activity overlaps substantially with venlafaxine, the TxGNN prediction can be considered mechanistically coherent. Nonetheless, indirect class-effect and parent-compound extrapolation do not substitute for direct clinical evidence: no trial to date has enrolled patients specifically to test desvenlafaxine for OCD, and the relative contribution of its norepinephrine reuptake inhibition (versus serotonergic inhibition) in the context of OCD pathophysiology remains unexplored.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT01527786](https://clinicaltrials.gov/study/NCT01527786) | Phase 3 | Completed | 25 | Functional outcome study in postpartum depression treated with desvenlafaxine. Indication is postpartum depression, not OCD. Included because it uses desvenlafaxine in a mood/anxiety spectrum disorder, but provides no direct OCD efficacy data. |
| [NCT03299166](https://clinicaltrials.gov/study/NCT03299166) | Phase 2/3 | Completed | 426 | Evaluates troriluzole (a glutamate modulator) as adjunctive therapy in OCD patients with inadequate response to prior SSRI, clomipramine, venlafaxine, or **desvenlafaxine** treatment. Desvenlafaxine is listed as a qualifying background medication — not the investigational drug. Provides context for desvenlafaxine's position within OCD treatment pathways. |

> **Important caveat**: Neither trial directly tested desvenlafaxine for OCD. These trials are included as contextual evidence only.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [14624187](https://pubmed.ncbi.nlm.nih.gov/14624187/) | 2003 | RCT | Journal of Clinical Psychopharmacology | First randomised double-blind comparison of **venlafaxine** (SNRI parent compound) versus paroxetine in OCD (n=150); venlafaxine demonstrated comparable efficacy. Strongest indirect evidence for SNRI class in OCD — applicable to desvenlafaxine by pharmacological class extrapolation. |
| [24766145](https://pubmed.ncbi.nlm.nih.gov/24766145/) | 2014 | Systematic Review | Expert Opinion on Pharmacotherapy | Updated review of double-blind trials of serotonergic antidepressants in OCD. Confirms that SRI-mediated serotonergic mechanisms are central to OCD pharmacotherapy; supports theoretical basis for SNRI use. |
| [36686097](https://pubmed.ncbi.nlm.nih.gov/36686097/) | 2022 | Narrative Review | Cureus | Comprehensive review of postpartum depression pathophysiology. Notes that untreated PPD can progress to OCD and anxiety disorders. Provides indirect mechanistic linkage between serotonergic dysregulation and OCD risk — does not directly evaluate desvenlafaxine in OCD. |
| [40224942](https://pubmed.ncbi.nlm.nih.gov/40224942/) | 2025 | Case Series | Psychiatry and Clinical Psychopharmacology | Risperidone augmentation in antidepressant-resistant somatic symptom disorder; describes OCD as a co-occurring condition in treatment-resistant cases. Background relevance only; does not address desvenlafaxine in OCD. |

---

## Australia Market Information

Desvenlafaxine is **not currently registered with the Therapeutic Goods Administration (TGA)** and has no entries on the Australian Register of Therapeutic Goods (ARTG). No TGA-approved Product Information (PI) exists for this drug in Australia.

Clinicians and researchers should consult the **US FDA prescribing information for Pristiq® (desvenlafaxine succinate extended-release tablets)** or the equivalent regulatory label from a jurisdiction where the drug is approved, for dosing, safety, and clinical guidance. The drug is available and approved in the United States, Canada, and several other markets.

---

## Safety Considerations

As desvenlafaxine has no TGA registration, Australian product information is unavailable. Please refer to the **US FDA-approved Pristiq® prescribing information** for complete safety data, including:

- **Black Box Warning** (FDA): Increased risk of suicidal thinking and behaviour in children, adolescents, and young adults with MDD and other psychiatric disorders.
- **Drug Interactions**: Known interactions with MAOIs (contraindicated; risk of serotonin syndrome), linezolid, and intravenous methylene blue. CYP enzyme interaction profile differs from venlafaxine due to reduced CYP2D6 involvement — refer to current FDA label for complete DDI data.
- **Contraindications**: Concomitant use with MAOIs or within 14 days of stopping an MAOI.

No DDI data was retrievable from the local database for this report. For any proposed clinical application, a full DDI review using current interaction databases (e.g., Micromedex, Lexicomp) is essential.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The mechanistic rationale for desvenlafaxine in OCD is plausible based on its SNRI class membership and indirect clinical evidence from the parent compound venlafaxine. However, the absence of any direct desvenlafaxine OCD trials and the low quality/relevance of identified clinical trial evidence places this firmly at L4 — not ready for clinical application or even early-phase off-label use without further foundational research.

**To proceed, the following is needed:**

- **Direct clinical trial**: A dedicated Phase 2 proof-of-concept RCT comparing desvenlafaxine to an established SSRI (e.g., sertraline or fluvoxamine) in adults with OCD, using validated outcome measures (Y-BOCS)
- **MOA characterisation**: Formal retrieval of DrugBank pharmacodynamic data to quantify desvenlafaxine's serotonin-to-norepinephrine reuptake inhibition ratio and assess its relevance to OCD (predominantly serotonergic disorder)
- **Dose-response considerations**: OCD typically requires higher SSRI/SNRI doses than MDD; dose-ranging data in OCD populations is needed
- **TGA regulatory pathway assessment**: If evidence matures, a TGA registration application (or Orphan Drug/Special Access Scheme pathway) would need to be scoped, given the drug is not currently on the ARTG
- **Safety review**: Full DDI and contraindication profile review relevant to the OCD population (including common co-medications such as antipsychotic augmenters, benzodiazepines, and mood stabilisers)
- **Evidence upgrade**: Minimum L3 evidence (observational study or retrospective case series) required before escalating to a formal research question funding application

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application. Data current as of 4 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

