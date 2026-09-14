---
layout: default
title: Sumatriptan
parent: 僅模型預測 (L5)
nav_order: 646
evidence_level: L5
indication_count: 10
---

# Sumatriptan
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

# Sumatriptan: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Sumatriptan is a well-established 5-HT1B/1D receptor agonist used for the acute treatment of migraine and cluster headache. The TxGNN model predicts it may also be effective for **migraine with brainstem aura**, a migraine subtype, but this direction is currently supported by **0 clinical trials** and **18 publications**, none of which specifically test sumatriptan in this subtype. Notably, this subtype has historically been flagged as a relative safety concern for triptans rather than an efficacy gap.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute treatment of migraine (with/without aura) and cluster headache — established global indication; no Australian ARTG record is available to confirm local labelling |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Sumatriptan is a selective 5-HT1B/1D receptor agonist. It acts on the trigeminovascular system to inhibit neurogenic inflammation and cranial vasodilation — the mechanism underlying its established efficacy in typical migraine. (Note: detailed formal MOA documentation was not retrievable from DrugBank for this evidence pack — see data gap DG002 — the mechanism above reflects well-established pharmacology of the triptan class rather than a pack-sourced MOA field.)

Migraine with brainstem aura (formerly "basilar-type" or "basilar" migraine) is a subtype of migraine involving symptoms referable to the brainstem or bilateral hemispheres, thought to involve the vertebrobasilar circulation. Because sumatriptan's core mechanism is already central to migraine treatment, the mechanistic overlap between the original and predicted indications is real — both are migraine syndromes sharing trigeminovascular and serotonergic pathophysiology.

However, this is precisely where the mechanism becomes double-edged rather than simply supportive. Triptan-induced vasoconstriction, while beneficial in typical migraine, raises a theoretical ischaemic risk when applied to a subtype involving the vertebrobasilar circulation. This is why sumatriptan and other triptans have historically been listed as relatively contraindicated in migraine with brainstem (basilar) aura and hemiplegic migraine in product labelling. In other words, the high TxGNN score here most plausibly reflects proximity in the knowledge graph (same drug class, same broad disease family) rather than a genuine efficacy signal — the open question is one of safety, not efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1313746](https://pubmed.ncbi.nlm.nih.gov/1313746/) | 1992 | RCT | Cephalalgia | Double-blind, placebo-controlled trial of oral sumatriptan 200mg in acute treatment of classical migraine (migraine with aura) |
| [11903526](https://pubmed.ncbi.nlm.nih.gov/11903526/) | 2001 | Review | Headache | Reviews triptan use specifically in basilar migraine and migraine with prolonged aura — the most directly relevant source, addressing use in this subtype |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Clinical Study | Neurology | Found reduced efficacy of sumatriptan in migraine with aura compared with migraine without aura |
| [25841027](https://pubmed.ncbi.nlm.nih.gov/25841027/) | 2015 | Commentary | Neurology | Discusses whether presence of aura predicts migraine severity and treatment response |
| [8559405](https://pubmed.ncbi.nlm.nih.gov/8559405/) | 1996 | Study | Neurology | Examines subcutaneous sumatriptan effects specifically in relation to the migraine aura phase |
| [21469920](https://pubmed.ncbi.nlm.nih.gov/21469920/) | 2011 | Review | Expert Review of Neurotherapeutics | Reviews needle-free subcutaneous sumatriptan (Sumavel DosePro), approved for acute migraine with or without aura and cluster headache |
| [23657930](https://pubmed.ncbi.nlm.nih.gov/23657930/) | 2014 | RCT | Phytotherapy Research | Double-blind RCT comparing ginger powder vs sumatriptan for acute treatment of common migraine (without aura) |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review/Guideline | Headache | American Headache Society evidence assessment of acute migraine pharmacotherapies, including triptans |
| [11318886](https://pubmed.ncbi.nlm.nih.gov/11318886/) | 2001 | Comparative Study | Headache | Compares isometheptene/dichloralphenazone/acetaminophen combination with sumatriptan succinate for mild-to-moderate migraine with or without aura |
| [8536293](https://pubmed.ncbi.nlm.nih.gov/8536293/) | 1995 | Review | Cephalalgia | Critical review of clinical experience with sumatriptan in migraine and cluster headache management |

Note: none of the above studies specifically enrolled or analysed patients with migraine with brainstem aura as a defined subgroup; relevance is inferred from general migraine-with-aura and triptan-class literature.

---

## Australia Market Information

No ARTG entries were identified. Sumatriptan-containing products are not currently marketed in Australia according to the data available in this evidence pack.

---

## Safety Considerations

TGA-sourced key warnings, contraindications, and drug interaction data were not available in this evidence pack (this is flagged as a **Blocking** data gap — DG001 — pending retrieval of the TGA-approved Product Information).

One safety signal is available directly from the mechanistic analysis in this evidence pack and is clinically important: because migraine with brainstem aura involves the vertebrobasilar circulation, triptan-induced vasoconstriction carries a theoretical ischaemic risk. This subtype has historically been listed as a relative contraindication for triptans in product labelling. This is a safety consideration specific to this candidate indication, not a general sumatriptan warning.

Please refer to the TGA-approved Product Information (PI), once available, for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, and the mechanistic link between sumatriptan and migraine subtypes is genuine, but no clinical trial or literature evidence specifically evaluates sumatriptan in migraine with brainstem aura. More importantly, the known theoretical vascular risk in this subtype means this candidate has a safety question to resolve, not an efficacy question — proceeding without addressing that would be inappropriate.

**To proceed, the following is needed:**
- TGA-approved Product Information for sumatriptan, specifically contraindication/warning language regarding basilar-type or hemiplegic migraine (resolves DG001)
- Confirmed mechanism of action data from DrugBank (resolves DG002)
- Targeted literature or case-series search specifically on triptan use (or avoidance) in migraine with brainstem aura, rather than general migraine-with-aura literature
- Specialist neurology input on whether the historical vascular-risk contraindication still holds under current diagnostic criteria for this subtype
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

