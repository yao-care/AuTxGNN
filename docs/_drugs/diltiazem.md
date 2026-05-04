---
layout: default
title: Diltiazem
parent: 僅模型預測 (L5)
nav_order: 156
evidence_level: L5
indication_count: 10
---

# Diltiazem
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

# Diltiazem: From Hypertension and Arrhythmia to Cerebrovascular Disorder

## One-Sentence Summary

Diltiazem is a non-dihydropyridine calcium channel blocker with established international use for hypertension, angina pectoris, and atrial fibrillation rate control, though it is not currently registered in Australia.
The TxGNN model predicts it may be beneficial for **Cerebrovascular Disorder** — the highest-evidenced predicted indication (ranked #4, TxGNN score 97.63%) — supported by **6 clinical trials** and **20 publications**, the strongest evidence base across all predictions in this pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension, angina pectoris, atrial fibrillation (established international use; no ARTG registration) |
| Predicted New Indication | Cerebrovascular Disorder |
| TxGNN Prediction Score | 97.63% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on established pharmacology, Diltiazem is a benzothiazepine-class calcium channel blocker that blocks L-type voltage-dependent calcium channels in cardiac and vascular smooth muscle. This reduces systemic vascular resistance, decreases myocardial oxygen demand, slows atrioventricular (AV) nodal conduction, and produces coronary and peripheral vasodilation.

Three indirect but mechanistically coherent pathways link Diltiazem to cerebrovascular disease. First, sustained systemic blood pressure reduction decreases cumulative cerebrovascular damage — the central mechanism behind calcium channel blockers' recognised role in stroke prevention within hypertension management guidelines. Second, inhibition of calcium influx into cerebrovascular smooth muscle can relax cerebral arteries and relieve vasospasm; this was directly demonstrated in a 1985 non-human primate model of chronic cerebrovascular spasm (PMID 2416213), and a human intraoperative study confirmed that a Diltiazem bolus increases internal carotid blood flow velocity during cerebral aneurysm surgery (PMID 8204245). Third, Diltiazem's established role as an atrial fibrillation (AF) rate-control agent is clinically significant: AF is the single most important modifiable risk factor for cardioembolic stroke, and rate control with Diltiazem may translate into reduced cerebrovascular event burden.

The landmark NORDIL trial (Lancet, 2000) provides Level 1 RCT data showing Diltiazem is non-inferior to diuretics and beta-blockers for cardiovascular outcomes — including stroke — in hypertensive patients. The absence of a dedicated randomised trial evaluating Diltiazem specifically for cerebrovascular endpoints remains a genuine evidence gap and the primary barrier to advancing this prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT06783868](https://clinicaltrials.gov/study/NCT06783868) | N/A | Not yet recruiting | 100 | SAVE STROKE Phase II: AF catheter ablation vs rate-control medication in recent stroke patients with new-onset AF; Diltiazem is a likely rate-control comparator; primary endpoint is neurological outcome |
| [NCT05838664](https://clinicaltrials.gov/study/NCT05838664) | N/A | Completed | 2,140,403 | SIFNOS: large French retrospective cohort of AF patients with/without oral anticoagulation (2016–2020); Diltiazem in the AF rate-control cohort provides real-world stroke incidence data at population scale |
| [NCT01176565](https://clinicaltrials.gov/study/NCT01176565) | Phase 3 | Terminated | 1,000 | ATACH-II: intensive vs standard blood pressure reduction in acute intracerebral haemorrhage; calcium channel blockers assessed as an antihypertensive class; terminated early — evidence value reduced |
| [NCT06175663](https://clinicaltrials.gov/study/NCT06175663) | N/A | Unknown | 130 | Midlife hypertension and cerebral small vessel disease MRI biomarkers; Diltiazem not the primary intervention, but the hypertension-to-cerebrovascular damage pathway is directly relevant |
| [NCT03529149](https://clinicaltrials.gov/study/NCT03529149) | Phase 4 | Unknown | 90 | TCD-guided blood pressure management after endovascular thrombectomy; Diltiazem may be among the antihypertensive agents used; status unknown limits usability |
| [NCT02922452](https://clinicaltrials.gov/study/NCT02922452) | Phase 1 | Completed | 16 | Pharmacokinetic DDI study: effect of Diltiazem on BMS-986141 plasma concentrations in healthy volunteers; no cerebrovascular treatment relevance |

> Note: None of the above trials use Diltiazem as a primary cerebrovascular intervention. All evidence is indirect, captured through the antihypertensive and AF rate-control pathways.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [10972367](https://pubmed.ncbi.nlm.nih.gov/10972367/) | 2000 | RCT | Lancet | NORDIL trial: Diltiazem non-inferior to diuretics/beta-blockers for cardiovascular outcomes (including fatal and non-fatal stroke) in hypertensive patients — the primary RCT basis for Diltiazem in stroke risk reduction |
| [41152878](https://pubmed.ncbi.nlm.nih.gov/41152878/) | 2025 | Retrospective Cohort | BMC Medicine | Multinational cohort in non-valvular AF: DOAC plus interacting antiarrhythmic drugs (including Diltiazem) — stroke and bleeding outcomes assessed across multiple countries |
| [37791408](https://pubmed.ncbi.nlm.nih.gov/37791408/) | 2023 | Retrospective Cohort | Eur Heart J Cardiovasc Pharmacother | Nationwide cohort: P-gp/CYP3A4 inhibitors (including Diltiazem) combined with NOACs in AF — stroke and major bleeding outcomes assessed |
| [36149579](https://pubmed.ncbi.nlm.nih.gov/36149579/) | 2023 | Retrospective Cohort | J Interv Card Electrophysiol | Diltiazem co-prescribed with DOACs in AF patients: major bleeding risk quantified in a real-world population |
| [35861836](https://pubmed.ncbi.nlm.nih.gov/35861836/) | 2022 | Retrospective Cohort | J Am Heart Assoc | Concomitant Diltiazem + DOAC use and bleeding risk stratified by kidney function in AF patients (n=4,544) |
| [17309423](https://pubmed.ncbi.nlm.nih.gov/17309423/) | 2007 | Review | Med J Australia | Australian review of AF management: Diltiazem cited as a preferred rate-control agent over digoxin during exercise; AF-to-stroke linkage explicitly discussed |
| [11975840](https://pubmed.ncbi.nlm.nih.gov/11975840/) | 2002 | Review | Heart Disease | AF epidemiology: associations with coronary events, stroke and mortality; Diltiazem's rate-control role reviewed |
| [8204245](https://pubmed.ncbi.nlm.nih.gov/8204245/) | 1994 | Clinical Study | J Clin Anesthesia | Diltiazem bolus (5 mg) increases internal carotid blood flow velocity and local cerebral blood flow during aneurysm surgery — direct human-level evidence of cerebral vasodilatory effect |
| [2416213](https://pubmed.ncbi.nlm.nih.gov/2416213/) | 1985 | Animal Study | Am J Cardiology | Non-human primate model: Diltiazem protects cerebral arteries against chronic vasospasm following subarachnoid haemorrhage — the only direct preclinical evidence for Diltiazem in cerebrovascular disease |
| [4056906](https://pubmed.ncbi.nlm.nih.gov/4056906/) | 1985 | Animal Study | J Neurosurgery | Diltiazem and verapamil infused before middle cerebral artery occlusion in cats — direct preclinical test of calcium channel blockade in acute ischaemic stroke |

---

## Australia Market Information

Diltiazem is **not currently registered** on the Australian Register of Therapeutic Goods (ARTG). There are no approved products, dosage forms, or approved indications on record in Australia.

> Diltiazem is widely available internationally — including the United States, European Union, United Kingdom, and New Zealand — in immediate-release and extended-release oral formulations and as intravenous preparations, approved for hypertension, angina, and atrial fibrillation. Any use in Australia would require either TGA registration or access under the Special Access Scheme (SAS Category B or C).

---

## Safety Considerations

No Australian TGA Product Information (PI) is available, as Diltiazem is not ARTG-registered. The following clinically important signals were identified from the published literature in this evidence pack:

**Drug Interactions:**
- Diltiazem is a moderate inhibitor of both CYP3A4 and P-glycoprotein. Co-prescription with direct oral anticoagulants (apixaban, rivaroxaban, dabigatran, edoxaban) significantly increases DOAC plasma concentrations, potentially elevating bleeding risk. Multiple real-world retrospective cohorts (PMIDs 36149579, 35861836, 37791408, 40326046, 41152878) have examined this interaction; findings on clinical bleeding outcomes are inconsistent, but warrant careful monitoring in any AF patient receiving both agents.
- Diltiazem + simvastatin: CYP3A4 inhibition substantially raises simvastatin exposure; linked in one case report series to fatal intracranial haemorrhage (INR >8) and myopathy following a statin switch (PMID 17304269). Atorvastatin is generally preferred when Diltiazem is co-prescribed.
- Perioperative intravenous Diltiazem in cardiac surgery: associated with increased incidence of postoperative acute renal failure (PMID 9594859); caution advised in patients with pre-existing renal impairment.
- Anaesthetic drug interactions: calcium channel blockers may potentiate cardiovascular depression and neuromuscular blockade with halogenated anaesthetic agents (PMID 2975926).

For complete prescribing information, refer to an approved international Product Information document (e.g., US FDA prescribing information for Diltiazem hydrochloride).

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The TxGNN prediction for cerebrovascular disorder is mechanistically well-grounded — supported by three pharmacological pathways (BP reduction, cerebral vasodilation, AF rate control) — and anchored by the landmark NORDIL RCT and multiple real-world observational cohorts (L3 evidence). However, no clinical trial has yet evaluated Diltiazem as a primary cerebrovascular therapeutic, Diltiazem is not registered in Australia, and the majority of identified evidence is indirect or observational.

**To proceed, the following is needed:**
- Define the specific research question: primary stroke prevention through BP/AF rate control, or acute/subacute cerebrovascular treatment such as post-subarachnoid haemorrhage vasospasm
- Assess the TGA registration pathway or Special Access Scheme eligibility for any proposed Australian clinical use
- Commission a systematic review or individual patient data meta-analysis pooling Diltiazem's stroke-related outcomes from existing antihypertensive and AF rate-control trial data
- Obtain Diltiazem MOA data from DrugBank (DG002 remediation) to complete the mechanistic justification and address the High-severity data gap
- Develop a pharmacovigilance protocol specifically addressing the Diltiazem–DOAC pharmacokinetic interaction, given the high overlap between the cerebrovascular disorder target population and AF patients receiving anticoagulation

---

*This report is generated for research purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before therapeutic application. Data cutoff: 4 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

