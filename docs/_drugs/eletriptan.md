---
layout: default
title: Eletriptan
parent: 僅模型預測 (L5)
nav_order: 181
evidence_level: L5
indication_count: 10
---

# Eletriptan
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

# Eletriptan: From Acute Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Eletriptan (Relpax®) is a second-generation 5-HT₁B/₁D receptor agonist (triptan) globally approved for the acute treatment of migraine headaches with and without aura, although it is not currently registered in Australia.
The TxGNN model predicts it may be effective for **migraine with brainstem aura** (formerly known as basilar-type migraine) — a specific subtype characterised by brainstem symptoms such as vertigo, dysarthria, and diplopia during the aura phase.
This predicted indication is supported by **18 publications**, including Cochrane systematic reviews and multiple RCTs covering triptan use in aura-positive migraine, though no clinical trials have specifically enrolled patients with the brainstem aura subtype.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute migraine (with and without aura) — globally approved; not registered in Australia |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Eletriptan is a selective, high-affinity agonist at the 5-HT₁B and 5-HT₁D serotonin receptor subtypes. Detailed mechanism of action data was not retrievable from the database query for this analysis; however, based on the published literature, eletriptan exerts its anti-migraine effect through two complementary pathways: (1) constriction of dilated cranial blood vessels via 5-HT₁B receptors on vascular smooth muscle, and (2) inhibition of pro-inflammatory neuropeptide release — particularly CGRP and substance P — from trigeminal nerve endings via 5-HT₁D receptors. Eletriptan has been reported to have approximately 6-fold greater affinity for the 5-HT₁D receptor and 3-fold greater affinity for the 5-HT₁B receptor than sumatriptan, with a selectivity profile favouring cranial over coronary vessels.

Migraine with brainstem aura (previously called "basilar-type migraine" under ICHD-2 criteria) shares the core neuroinflammatory substrate of common migraine — cortical spreading depression propagating into brainstem territories — and is characterised by activation of the trigeminal-cervical complex and trigeminovascular signalling pathways. Since eletriptan's primary targets (5-HT₁B/₁D receptors) are expressed in the brainstem raphe nuclei and trigeminal nucleus caudalis, the mechanistic rationale for extending its use to this subtype is scientifically plausible. The TxGNN knowledge graph model captures these receptor-level and disease-network relationships, yielding a near-perfect prediction score of 99.99%.

Historically, triptans were contraindicated in basilar-type migraine due to theoretical concern about vasoconstrictive effects on the posterior circulation (basilar artery), potentially aggravating brainstem ischaemia. This caution has been substantially re-evaluated since the ICHD-3β reclassification in 2013. Growing evidence now suggests that the aura in this subtype is primarily a neuronal phenomenon (cortical spreading depression) rather than haemodynamic, and that the empirical basis for the original blanket contraindication was weak. International headache societies have moved towards a more nuanced position. However, dedicated RCTs specifically enrolling patients with confirmed migraine with brainstem aura remain absent, which limits the evidence grade for this specific indication to L3.

---

## Clinical Trial Evidence

Currently no clinical trials specifically targeting **migraine with brainstem aura** with eletriptan have been registered on ClinicalTrials.gov or the ICTRP network. The historical triptan contraindication for this subtype is likely to have discouraged formal trial design in this population.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Evidence Assessment (AHS Guidelines) | *Headache* | Updated American Headache Society evidence assessment of acute migraine pharmacotherapies; eletriptan assigned Level A evidence for migraine with and without aura |
| [11687056](https://pubmed.ncbi.nlm.nih.gov/11687056/) | 2001 | Cochrane Systematic Review | *Cochrane Database Syst Rev* | Systematic review of eletriptan for acute migraine demonstrating consistent, clinically meaningful efficacy across multiple RCTs at 40 mg and 80 mg doses |
| [15469451](https://pubmed.ncbi.nlm.nih.gov/15469451/) | 2004 | RCT | *European Journal of Neurology* | Directly relevant to this indication: eletriptan 80 mg administered during the aura phase in confirmed migraine-with-aura patients; no significant effect on aura duration, providing unique timing and safety data for aura-phase dosing |
| [12807526](https://pubmed.ncbi.nlm.nih.gov/12807526/) | 2003 | RCT | *Cephalalgia* | Double-blind, placebo-controlled, multicentre RCT (n=446) in patients with prior inadequate sumatriptan response (with and without aura); eletriptan 40/80 mg demonstrated efficacy in this clinically challenging population |
| [11844898](https://pubmed.ncbi.nlm.nih.gov/11844898/) | 2002 | RCT | *European Neurology* | Double-blind, placebo-controlled multicentre RCT; eletriptan 80 mg was superior to ergotamine plus caffeine in treating migraine attacks with and without aura |
| [17501848](https://pubmed.ncbi.nlm.nih.gov/17501848/) | 2007 | RCT | *Headache* | Multidimensional functional assessment; eletriptan produced significant, measurable improvements in work productivity and activity participation during acute migraine episodes |
| [12498013](https://pubmed.ncbi.nlm.nih.gov/12498013/) | 2002 | Drug Review | *Curr Opin Investig Drugs* | Pfizer pharmacological review; documents receptor subtype selectivity data (6× higher 5-HT₁D affinity, 3× higher 5-HT₁B affinity vs sumatriptan) supporting the mechanistic basis for efficacy in aura-positive subtypes |
| [11050304](https://pubmed.ncbi.nlm.nih.gov/11050304/) | 2000 | Pharmacological Study | *European Journal of Pharmacology* | In vitro comparison of vascular contractile effects on human meningeal, coronary, and saphenous vessels; eletriptan demonstrated preferential cranial artery selectivity, relevant to posterior circulation safety considerations |
| [25155004](https://pubmed.ncbi.nlm.nih.gov/25155004/) | 2014 | Case Report | *Rev Port Cardiol* | Case report of non-ST-elevation MI occurring hours after eletriptan use in a patient with pre-existing non-obstructive coronary artery disease and migraine with visual aura; critical safety reference for vasoconstrictive risk in patients with posterior circulation vulnerability |
| [21028917](https://pubmed.ncbi.nlm.nih.gov/21028917/) | 2010 | Review | *Paediatric Drugs* | Review of triptan use in paediatric migraine; provides indirect evidence on eletriptan tolerability in aura-positive migraine across age groups |

---

## Australia Market Information

Eletriptan is **not currently registered on the Australian Register of Therapeutic Goods (ARTG)**. As of the data cut-off (4 April 2026), there are no active product licences in Australia and no ARTG entries. The drug is approved in multiple other jurisdictions under the brand name Relpax® (Pfizer), including the USA, EU, Japan, and others, for the acute treatment of migraine with and without aura.

Any proposed use in Australia would require a formal TGA regulatory pathway, such as:
- A new ARTG registration application (highest route to broad access)
- Special Access Scheme (SAS) Category B for individual patients under specialist supervision
- Authorised Prescriber arrangements for specific clinical contexts

---

## Safety Considerations

Comprehensive safety data was not available from the regulatory or interaction databases queried for this analysis. Please refer to the **TGA Special Access Scheme documentation**, the **FDA-approved Prescribing Information**, or the **EMA Summary of Product Characteristics** for Relpax® (eletriptan hydrobromide) as the primary safety references.

The following safety points are specifically relevant to the predicted indication — migraine with brainstem aura:

- **Posterior circulation vasoconstriction risk**: The historical contraindication for triptans in basilar-type migraine was based on the theoretical risk of basilar artery constriction potentially worsening brainstem ischaemia. While this restriction is being re-evaluated, the absence of dedicated safety data in confirmed migraine with brainstem aura patients means this risk has not been formally excluded.
- **Cardiovascular contraindications**: Eletriptan, like all triptans, is contraindicated in patients with ischaemic heart disease, prior myocardial infarction, Prinzmetal's angina, uncontrolled hypertension, peripheral arterial disease, or prior stroke or TIA. A published case report (PMID 25155004) documents MI after eletriptan use in a patient with non-obstructive coronary disease and migraine with visual aura, underscoring the importance of cardiac risk stratification.
- **CYP3A4 drug interactions**: Eletriptan is primarily metabolised by CYP3A4. Co-administration with potent CYP3A4 inhibitors (including ketoconazole, itraconazole, clarithromycin, erythromycin, and ritonavir) substantially increases eletriptan plasma concentrations; this combination is contraindicated per global labelling. No interaction data was returned from the local DDI database query.
- **Serotonin syndrome**: Caution is warranted with concurrent use of SSRIs, SNRIs, MAOIs, or other serotonergic agents.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Eletriptan has strong, well-established evidence (L1) for the broader acute migraine indication including aura-positive subtypes, and the mechanistic plausibility for migraine with brainstem aura is scientifically credible. The historical contraindication is currently under revision in the international headache medicine community. However, the complete absence of dedicated clinical trial data for this specific subtype, combined with the unresolved safety question around posterior circulation vasoconstriction and the drug's non-registration in Australia, means that a structured, monitored approach is required before any clinical application.

**To proceed, the following is needed:**

- **Regulatory pathway**: Confirm the appropriate TGA access pathway (ARTG registration, SAS Category B, or Authorised Prescriber) before any clinical use in Australia
- **MOA data**: Obtain full mechanism of action, pharmacokinetic, and pharmacodynamic data from DrugBank and the FDA/EMA Product Information
- **Safety data**: Download and review the Relpax® FDA Prescribing Information and/or EMA SmPC for complete contraindications, warnings, and DDI profile; specifically evaluate the revised position on triptan use in migraine with brainstem aura
- **Guideline review**: Assess the current position statements of the Australian Headache Society, the International Headache Society (IHS), and the American Headache Society on triptan use in ICHD-3–confirmed migraine with brainstem aura
- **Targeted literature search**: Conduct a focused systematic search for studies published after the 2013 ICHD-3β reclassification specifically addressing triptan safety and efficacy in migraine with brainstem aura
- **Prospective registry**: Design a prospective patient registry or pragmatic observational study to collect real-world safety and efficacy data in patients with ICHD-3–confirmed migraine with brainstem aura treated with eletriptan under specialist supervision
- **Specialist consultation**: Seek neurology/headache specialist input prior to any clinical use, given the historical contraindication concern and absence of dedicated safety data in this subtype

---

> **⚠️ Disclaimer**: This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates identified by computational models require independent clinical validation before any therapeutic application. All clinical decisions should be made in accordance with current TGA regulations and clinical practice guidelines.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

