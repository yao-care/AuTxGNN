---
layout: default
title: Acetaminophen
parent: 僅模型預測 (L5)
nav_order: 18
evidence_level: L5
indication_count: 10
---

# Acetaminophen
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

# Acetaminophen: From Pain and Fever Management to Migraine with Brainstem Aura

## One-Sentence Summary

Acetaminophen (paracetamol) is a widely used over-the-counter analgesic and antipyretic indicated for the relief of pain and fever across diverse clinical settings.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura**, with **0 registered clinical trials** and **20 publications** currently supporting this direction.
Evidence is largely extrapolated from general migraine studies rather than this specific subtype, positioning this as a research question requiring dedicated investigation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | General pain and fever management (analgesic/antipyretic) — no ARTG indication data retrieved in this Evidence Pack |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L3 |
| Australia Market Status | Not retrieved (data gap — see Australia Market Information section) |
| Number of ARTG Entries | 0 (data retrieval limitation — see below) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, acetaminophen (paracetamol) exerts its analgesic effect primarily through central mechanisms: inhibition of COX enzymes in the central nervous system (particularly the COX-3 isoform), modulation of the descending serotonergic and noradrenergic pain inhibition pathways, and possible interaction with the endocannabinoid system via fatty acid amide hydrolase (FAAH) inhibition. These central mechanisms are broadly relevant to migraine pathophysiology, which involves trigeminovascular activation, neuroinflammation, and altered descending pain modulation.

Migraine with brainstem aura (formerly called basilar-type migraine) is a recognised subtype of migraine with aura under the International Classification of Headache Disorders (ICHD-3), characterised by aura symptoms originating from the brainstem — such as dysarthria, vertigo, tinnitus, hypacusia, diplopia, and ataxia — occurring before the headache phase. Mechanistically, it shares the core pathway of cortical spreading depression and trigeminovascular sensitisation with other forms of migraine with aura. The American Headache Society (AHS) Evidence Assessment (PMID 25600718) assigns acetaminophen a **Grade B recommendation** for acute migraine treatment broadly, and pregnancy-specific guidelines consistently list it as the **first-line analgesic** when triptans and NSAIDs are unsuitable (PMID 30470274; PMID 39493026).

The main gap in the evidence is the absence of trials or subgroup analyses specifically targeting migraine with brainstem aura as a distinct entity. Clinical guidance does not currently identify this subtype as contraindicated for acetaminophen; rather, the evidence is extrapolated from general migraine with or without aura populations. An RCT (PMID 11318886) comparing an isometheptene/dichloralphenazone/acetaminophen combination against sumatriptan showed comparable efficacy for mild-to-moderate migraine **with or without aura**, lending the closest analogue to direct support. The TxGNN prediction is mechanistically plausible but requires subtype-specific clinical validation before implementation as a dedicated indication.

---

## Clinical Trial Evidence

Currently no clinical trials specifically registered for acetaminophen in migraine with brainstem aura.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Clinical Guideline / Evidence Assessment (AHS) | *Headache* | Updated AHS evidence assessment of acute migraine pharmacotherapies; acetaminophen assigned **Grade B** recommendation for acute migraine treatment |
| [9482363](https://pubmed.ncbi.nlm.nih.gov/9482363/) | 1998 | RCT (×3 placebo-controlled) | *Archives of Neurology* | Acetaminophen/aspirin/caffeine combination vs placebo across three randomised trials: statistically significant pain relief and functional improvement in migraine |
| [11318886](https://pubmed.ncbi.nlm.nih.gov/11318886/) | 2001 | RCT | *Headache* | Isometheptene/dichloralphenazone/acetaminophen vs sumatriptan for mild-to-moderate migraine with or without aura: comparable efficacy and safety |
| [10321417](https://pubmed.ncbi.nlm.nih.gov/10321417/) | 1999 | Retrospective RCT Analysis | *Clinical Therapeutics* | Acetaminophen/aspirin/caffeine combination for menstruation-associated migraine: benefits consistent with non-menstrual migraine across three placebo-controlled trials |
| [39493026](https://pubmed.ncbi.nlm.nih.gov/39493026/) | 2024 | Systematic Review | *Cureus* | Abortive and prophylactic therapies for migraine in pregnancy; acetaminophen recommended as first-line abortive treatment, particularly in first trimester |
| [30470274](https://pubmed.ncbi.nlm.nih.gov/30470274/) | 2019 | Review | *Neurologic Clinics* | Headache in pregnancy and puerperium; acetaminophen identified as **first-line symptomatic treatment**, with recommended monitoring for progressive headache |
| [37123778](https://pubmed.ncbi.nlm.nih.gov/37123778/) | 2023 | Review | *Cureus* | Migraine management in pregnancy and breastfeeding; acetaminophen recommended; reviews four-stage migraine classification including aura subtypes |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Review | *Handbook of Clinical Neurology* | Status migrainosus (>72 h migraine attack); reviews treatment approaches including role of non-opioid analgesics such as acetaminophen in rescue management |
| [33525313](https://pubmed.ncbi.nlm.nih.gov/33525313/) | 2021 | Review | *Neurology International* | Ubrogepant as CGRP antagonist for acute migraine; contextualises acetaminophen as standard non-prescription first-line for mild-to-moderate migraine |
| [9556832](https://pubmed.ncbi.nlm.nih.gov/9556832/) | 1998 | Review | *Schweizerische Medizinische Wochenschrift* | Migraine treatment overview; group studies indicate analgesics (including acetaminophen) are not inferior to ergot derivatives or sumatriptan, particularly when combined with a prokinetic |

---

## Australia Market Information

> ⚠️ **Data Retrieval Limitation**: The Evidence Pack reports **0 ARTG entries** and a market status of "not retrieved" for acetaminophen in Australia. This almost certainly reflects a query limitation rather than actual market absence. Acetaminophen — marketed in Australia under the INN **paracetamol** — is one of the most extensively registered medicines on the ARTG, with hundreds of listed products across multiple dosage forms and sponsors (e.g., Panadol, Panamax, Dymadon, and numerous generics). A direct TGA ARTG search is strongly recommended to confirm current registration status, approved indications, and relevant Product Information (PI) documents.

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|-------------|-------------|-------------|---------------------|
| — | No data retrieved | — | Please search the TGA ARTG directly at [www.tga.gov.au/resources/artg](https://www.tga.gov.au/resources/artg) |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No Drug-Drug Interaction (DDI) data or specific warnings were returned in this Evidence Pack.

Key safety considerations known from the literature that are relevant to this indication:

- **Hepatotoxicity**: Maximum recommended dose in adults is 4,000 mg/day; reduce in hepatic impairment, alcohol dependency, or malnutrition
- **Pregnancy use**: Acetaminophen is generally considered the safest analgesic in pregnancy and is commonly recommended for migraine management during all trimesters; however, emerging epidemiological data regarding prolonged in-utero exposure warrants discussion with the treating team
- **Triptans in brainstem aura**: Note that **triptans are relatively contraindicated** in migraine with brainstem aura due to theoretical vasoconstrictive risk — acetaminophen does not carry this restriction, which may further support its role in this specific subtype

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Acetaminophen has an established Grade B evidence base for acute migraine broadly, and is the preferred analgesic for migraine in pregnancy. However, no clinical trials have specifically enrolled patients with **migraine with brainstem aura** as a distinct subtype, and the existing evidence is entirely extrapolated from general migraine with or without aura populations. Until dedicated evidence exists for this subtype, this represents a research question rather than a ready-to-implement indication.

**To proceed, the following is needed:**

- **MOA verification**: Retrieve full mechanism of action data from DrugBank to formally document the relevance of central COX inhibition and serotonergic pathway activation to brainstem aura pathophysiology
- **ARTG data retrieval**: Conduct a direct TGA ARTG search using the INN "paracetamol" to retrieve current registration status, approved indications, and Product Information documents — the 0-entry result in this Evidence Pack is a known data gap
- **Subtype-specific evidence**: Identify any published subgroup analyses or case series specifically reporting acetaminophen outcomes in migraine with brainstem aura (ICHD-3 criteria: 1.2.2)
- **Contraindication clarification**: Confirm whether current TGA-approved PI or AHS/Australian headache guidelines list any acetaminophen-specific precautions for brainstem aura, given that vasoconstrictive agents (triptans, ergotamines) are already restricted in this subtype
- **Prospective research pathway**: Consider a pharmacoepidemiology study or prospective registry linking paracetamol use to outcomes in confirmed migraine with brainstem aura patients, using existing Australian headache clinic cohorts

---

*⚕️ This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require rigorous clinical validation before therapeutic application. Refer to TGA-approved Product Information for prescribing guidance.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

