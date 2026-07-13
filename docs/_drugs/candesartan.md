---
layout: default
title: Candesartan
parent: 僅模型預測 (L5)
nav_order: 118
evidence_level: L5
indication_count: 10
---

# Candesartan
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

# Candesartan: From Hypertension to Migraine Disorder

## One-Sentence Summary

Candesartan is an angiotensin II type 1 receptor blocker (ARB) primarily established for the treatment of hypertension and heart failure.
The TxGNN model predicts it may be effective for **Migraine Disorder** prevention,
with **3 relevant clinical trials** (including a large Phase 2 multicentre RCT completed in 2024) and **20 publications** — including a 2025 *Lancet Neurology* RCT — currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension / Heart failure |
| Predicted New Indication | Migraine Disorder (Episodic Migraine Prevention) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| Australia Market Status | Not currently listed on the ARTG |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Candesartan is an angiotensin II type 1 receptor (AT1R) blocker. By selectively antagonising AT1R, it prevents angiotensin II from exerting its vasoconstrictive and pro-inflammatory effects. While currently detailed mechanism of action data from DrugBank is unavailable, the biological rationale for migraine prevention is well-supported by the existing literature.

The renin-angiotensin-aldosterone system (RAAS) is implicated in migraine pathophysiology through several pathways. AT1R antagonism can suppress neurogenic inflammation by reducing calcitonin gene-related peptide (CGRP) release, raise the threshold for cortical spreading depression (the electrophysiological correlate of migraine aura), and stabilise cerebrovascular tone — all of which are recognised targets in migraine prevention. Animal studies have demonstrated that RAAS activation lowers the cortical spreading depression threshold, and genetic research has linked ACE insertion/deletion polymorphisms to individual migraine susceptibility.

This mechanistic plausibility is directly supported by clinical evidence: two earlier Phase 2 randomised controlled trials (Tronvik 2003 and Stovner 2014) demonstrated meaningful reductions in migraine frequency with candesartan 16 mg/day. The largest trial to date (NCT04574713, n=450, completed 2024) sought to confirm these findings in a multicentre, binational, placebo-controlled design, with results published in *The Lancet Neurology* in 2025 (PMID 40975098). Multiple international clinical guidelines (AAN, ACP, Canadian Headache Society) already list candesartan as a migraine prophylaxis option, further supporting the reasonableness of this TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT04574713](https://clinicaltrials.gov/study/NCT04574713) | Phase 2 | Completed | 450 | Multicentre, binational, triple-blind, placebo-controlled RCT evaluating candesartan 8 mg and 16 mg/day for episodic migraine prevention. Results published in *Lancet Neurology* 2025 (PMID 40975098). Strongest and largest direct evidence for this indication. |
| [NCT00884663](https://clinicaltrials.gov/study/NCT00884663) | Phase 2/3 | Completed | 72 | Three-arm double-blind RCT comparing candesartan vs propranolol vs placebo for migraine prophylaxis. Rigorous head-to-head design; results published in *Cephalalgia* (Stovner 2014). |
| [NCT04138316](https://clinicaltrials.gov/study/NCT04138316) | Observational | Completed | 85 | Prospective observational study (CandeSpartan) assessing response predictors and tolerability of candesartan in patients with episodic or chronic migraine who had failed ≥3 prior preventive drugs. Results published in *Cephalalgia* 2024 (PMID 38663908). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [40975098](https://pubmed.ncbi.nlm.nih.gov/40975098/) | 2025 | RCT | *The Lancet. Neurology* | Candesartan vs placebo Phase 2 RCT (n=450): evaluated safety, tolerability, and efficacy for episodic migraine prevention. Primary landmark paper for this repurposing direction. |
| [38057728](https://pubmed.ncbi.nlm.nih.gov/38057728/) | 2023 | Systematic Review | *J Headache Pain* | Network meta-analysis of pharmacological interventions for chronic migraine in adults; positions candesartan within the preventive treatment landscape. |
| [37350141](https://pubmed.ncbi.nlm.nih.gov/37350141/) | 2023 | Systematic Review | *Cephalalgia* | Systematic review and meta-analysis of blood pressure-lowering medications for episodic migraine prevention, including ARB class evidence. |
| [39899861](https://pubmed.ncbi.nlm.nih.gov/39899861/) | 2025 | Clinical Practice Guideline | *Annals of Internal Medicine* | American College of Physicians clinical guideline for pharmacologic prevention of episodic migraine in outpatient settings; addresses candesartan's role. |
| [38663908](https://pubmed.ncbi.nlm.nih.gov/38663908/) | 2024 | Observational Cohort | *Cephalalgia* | CandeSpartan study: effectiveness, tolerability, and response predictors for candesartan in real-world migraine practice (PMID corresponds to NCT04138316). |
| [33589682](https://pubmed.ncbi.nlm.nih.gov/33589682/) | 2021 | Retrospective Cohort | *Scientific Reports* | Real-world effectiveness and tolerability of candesartan in migraine (n=all patients, April 2008–February 2019); explores predictors of patient response. |
| [40571531](https://pubmed.ncbi.nlm.nih.gov/40571531/) | 2025 | Scoping Review | *Clinical Therapeutics* | Comprehensive scoping review of candesartan for migraine management; summarises the growing evidence base for this ARB in headache disorders. |
| [31515634](https://pubmed.ncbi.nlm.nih.gov/31515634/) | 2019 | Systematic Review | *Current Pain and Headache Reports* | Systematic review of ACE inhibitors and ARBs for prophylactic migraine treatment in adults; identifies research gaps and provides guidance for future trials. |
| [30600979](https://pubmed.ncbi.nlm.nih.gov/30600979/) | 2019 | Review | *American Family Physician* | Comprehensive review of migraine headache prophylaxis including candesartan; notes that <13% of eligible patients take prophylactic medications. |
| [18759728](https://pubmed.ncbi.nlm.nih.gov/18759728/) | 2008 | Review | *Medical Journal of Australia* | Australian-context review of migraine prophylaxis options; explicitly identifies candesartan as a drug "gaining favour" with "reasonably good but limited" evidence — directly relevant to Australian prescribers. |

---

## Australia Market Information

Candesartan is **not currently listed on the Australian Register of Therapeutic Goods (ARTG)** based on available data. No ARTG entries were identified in the regulatory search conducted on 9 March 2026.

> **Note for Prescribers:** Candesartan cilexetil (the prodrug formulation) is marketed in many comparable jurisdictions (UK, USA, Canada, Japan) under brand names such as Atacand. A discrepancy between this regulatory data and known international availability suggests a data gap in the ARTG lookup. Prescribers should verify current ARTG status directly via the [TGA ARTG search portal](https://www.tga.gov.au/resources/artg) before clinical use.

---

## Safety Considerations

Detailed TGA-approved Product Information (PI) warnings and contraindications were not available in the Evidence Pack. However, the literature search identified the following class-level safety signals relevant to candesartan and ARBs generally:

- **Pregnancy risk (Fetopathy):** Multiple published case series (PMID 15669052, 18412789, 21271514) document oligohydramnios, fetal growth retardation, and pulmonary hypoplasia associated with ARB use during pregnancy — a critical contraindication that must be addressed in any prescribing protocol for women of childbearing age.
- **Pulmonary adverse events:** A case report (PMID 22890134) describes diffuse alveolitis temporally associated with candesartan-hydrochlorothiazide, which resolved on discontinuation.

> For complete safety information including all contraindications, warnings, drug interactions, and special population guidance, please refer to the **TGA-approved Product Information (PI)** for candesartan cilexetil. Given the absence of ARTG registration, the equivalent PI from a comparable regulator (e.g., UK MHRA, Health Canada) should be reviewed as an interim reference.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 multicentre RCT (NCT04574713, n=450, *Lancet Neurology* 2025) provides direct evidence for candesartan in episodic migraine prevention, corroborated by a second completed Phase 2/3 RCT (NCT00884663), real-world cohort data, multiple systematic reviews, and endorsement in international clinical guidelines from AAN, ACP, and the Canadian Headache Society. The mechanistic basis (AT1R-mediated CGRP suppression and cortical spreading depression threshold modulation) is biologically coherent and well-supported. The evidence level (L2) justifies advancing beyond hypothesis, but confirmation in a Phase 3 trial and TGA regulatory pathway remains outstanding.

**To proceed, the following is needed:**

- **Regulatory pathway clarification:** Verify ARTG status; if candesartan cilexetil is indeed not registered in Australia, determine whether a Section 19A import approval, Special Access Scheme (SAS), or new TGA submission is required for off-label prescribing in migraine.
- **Detailed mechanism of action data (MOA):** Obtain full DrugBank entry to confirm AT1R selectivity and secondary pharmacological targets relevant to migraine neurobiology.
- **TGA Product Information (PI):** Download and review the PI or comparable regulatory document to complete the safety assessment, particularly for contraindications (pregnancy), drug interactions (potassium-sparing agents, NSAIDs, lithium), and renal function monitoring requirements.
- **Phase 3 RCT evidence:** The 2025 *Lancet Neurology* paper from NCT04574713 is Phase 2; a full Phase 3 confirmatory trial would be required to support TGA indication registration.
- **Local population considerations:** Assess applicability to the Australian migraine population, including co-morbid hypertension prevalence, where candesartan could offer dual therapeutic benefit.
- **Pharmacoeconomic analysis:** Given availability of subsidised prophylactics on the PBS (e.g., propranolol, topiramate), a cost-effectiveness comparison should be conducted before any PBS listing proposal.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

