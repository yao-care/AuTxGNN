---
layout: default
title: Flecainide
parent: 僅模型預測 (L5)
nav_order: 279
evidence_level: L5
indication_count: 10
---

# Flecainide
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

# Flecainide: From Cardiac Arrhythmia (Atrial Fibrillation) to Stroke Disorder

## One-Sentence Summary

Flecainide is a Class Ic sodium-channel-blocking antiarrhythmic, used clinically to control atrial fibrillation, atrial flutter, and other cardiac arrhythmias. The TxGNN model predicts it may be effective for **Stroke Disorder**, with **19 clinical trials** and **20 publications** identified, though most of this evidence addresses atrial fibrillation rhythm control rather than a direct anti-stroke effect. Evidence level is **L2**, but the link to stroke is mechanistically indirect and comes with a known cardiac safety history that warrants caution.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established from Australian regulatory data (no ARTG licence on file); described in the supporting literature as a Class Ic antiarrhythmic for atrial fibrillation/flutter and other arrhythmias |
| Predicted New Indication | Stroke Disorder |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA field is a data gap). Based on the supporting literature, flecainide is a Class Ic antiarrhythmic that blocks cardiac sodium channels, used to maintain sinus rhythm in patients with atrial fibrillation (AF), atrial flutter, and ventricular arrhythmias; its efficacy in rhythm control is well established.

Atrial fibrillation is a major cause of cardioembolic stroke. The rationale behind this TxGNN prediction is that by suppressing AF and maintaining sinus rhythm, flecainide may *indirectly* reduce embolic stroke risk — not through any direct cerebrovascular or antithrombotic action. This is reflected in the evidence itself: the EAST-AFNET 4 trial (NCT01288352) tested early rhythm-control therapy (including antiarrhythmic drugs such as flecainide) against usual care for prevention of AF-related cardiovascular complications, including stroke as part of a composite endpoint.

This mechanistic link should be treated cautiously. Flecainide carries a well-documented safety history from the CAST trial, where suppressing ventricular arrhythmias post-myocardial infarction with Class Ic agents increased mortality — meaning its use in structural heart disease or coronary artery disease requires careful risk-benefit assessment, and its proarrhythmic potential is not trivial. The model's "stroke disorder" association most plausibly reflects proximity to AF/rhythm-control biology rather than a genuine, direct antithrombotic or neuroprotective effect.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01288352](https://clinicaltrials.gov/study/NCT01288352) | Phase 4 | Completed | 2,789 | EAST-AFNET 4: early structured rhythm-control therapy (antiarrhythmics incl. flecainide + catheter ablation) vs usual care for prevention of AF-related complications, including stroke as part of a composite endpoint (Grade A relevance) |
| [NCT01646281](https://clinicaltrials.gov/study/NCT01646281) | Phase 4 | Unknown | 70 | Direct flecainide study: effects of vernakalant and flecainide on atrial contractility in AF; reduced contractility post-cardioversion is linked to stroke risk, but the trial's endpoint is cardiac function, not stroke |
| [NCT00911508](https://clinicaltrials.gov/study/NCT00911508) | N/A | Completed | 2,204 | CABANA: catheter ablation vs antiarrhythmic drug therapy (flecainide a possible comparator) for AF; not powered specifically for stroke outcome |
| [NCT05213104](https://clinicaltrials.gov/study/NCT05213104) | Phase 3 | Active, not recruiting | 186 | Direct flecainide study: assesses whether flecainide lowers atrial arrhythmia/tachycardia risk after PFO closure in cryptogenic stroke patients — closest direct link between flecainide and stroke-related pathology, results not yet available |
| [NCT07405671](https://clinicaltrials.gov/study/NCT07405671) | Phase 4 | Not yet recruiting | 988 | Direct flecainide study: safety of flecainide vs standard rhythm-control drugs (sotalol/amiodarone) in AF patients with stable coronary artery disease |
| [NCT00523978](https://clinicaltrials.gov/study/NCT00523978) | Phase 3 | Completed | 245 | STOP AF: cryoablation vs an AF drug (flecainide, propafenone, or sotalol) in patients with paroxysmal AF refractory to drug therapy |
| [NCT05293080](https://clinicaltrials.gov/study/NCT05293080) | Phase 3 | Not yet recruiting | 1,746 | Tests whether early, comprehensive rhythm-control therapy prevents adverse cardiovascular outcomes in patients with acute ischaemic stroke and AF |
| [NCT01447862](https://clinicaltrials.gov/study/NCT01447862) | Phase 4 | Completed | 101 | Vernakalant vs ibutilide for recent-onset AF conversion; does not use flecainide, disease-area relevance only |
| [NCT07270848](https://clinicaltrials.gov/study/NCT07270848) | Phase 4 | Not yet recruiting | 1,898 | Dronedarone for early rhythm control in AF; does not use flecainide, disease-area relevance only |
| [NCT02459574](https://clinicaltrials.gov/study/NCT02459574) | N/A | Completed | 321 | Ablation vs antiarrhythmic therapy for reducing hospital episodes from recurrent AF |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38702961](https://pubmed.ncbi.nlm.nih.gov/38702961/) | 2024 | RCT (EAST-AFNET 4 follow-up) | Europace | Safety/efficacy of long-term sodium-channel-blocker (flecainide/propafenone) therapy for early rhythm control in AF |
| [25430048](https://pubmed.ncbi.nlm.nih.gov/25430048/) | 2014 | Review/Guideline | BMJ Clinical Evidence | Overview of acute AF management and its association with increased stroke risk |
| [37109225](https://pubmed.ncbi.nlm.nih.gov/37109225/) | 2023 | RCT | Journal of Clinical Medicine | Compares carvedilol vs flecainide for idiopathic PVCs from the ventricular outflow tract (cardiac, non-stroke endpoint) |
| [28496906](https://pubmed.ncbi.nlm.nih.gov/28496906/) | 2013 | Cohort | Journal of Atrial Fibrillation | Real-world cohort comparing cardiovascular events, including stroke, across antiarrhythmics (dronedarone vs amiodarone and others) |
| [27159789](https://pubmed.ncbi.nlm.nih.gov/27159789/) | 2016 | Review | Nature Reviews Disease Primers | Comprehensive AF review, noting stroke as a serious AF complication |
| [30067936](https://pubmed.ncbi.nlm.nih.gov/30067936/) | 2018 | Guideline | Medical Journal of Australia | Australian national clinical guidelines for diagnosis and management of AF (directly relevant to the Australian practice context) |
| [39077579](https://pubmed.ncbi.nlm.nih.gov/39077579/) | 2023 | Review | Reviews in Cardiovascular Medicine | Management of AF during pregnancy, including antiarrhythmic and anticoagulant risk-benefit considerations |
| [27884575](https://pubmed.ncbi.nlm.nih.gov/27884575/) | 2017 | Case Report (safety) | The Journal of Emergency Medicine | Brugada ECG pattern unmasked by flecainide overdose in an AF patient |
| [40800559](https://pubmed.ncbi.nlm.nih.gov/40800559/) | 2025 | Case Report (safety) | European Heart Journal Case Reports | Refractory ventricular tachycardia associated with flecainide use ("flecainide fallout") |
| [35114252](https://pubmed.ncbi.nlm.nih.gov/35114252/) | 2022 | Mechanistic study | Journal of Molecular and Cellular Cardiology | Biophysical basis for flecainide's relative atrial selectivity and lower ventricular pro-arrhythmia rate in AF |

## Australia Market Information

Currently no ARTG entries are recorded for flecainide in this evidence pack — flecainide is listed as **not marketed** in Australia in the underlying regulatory data source used to build this report.

## Safety Considerations

Formal TGA-sourced warnings, contraindications, and drug-interaction data are not available in this evidence pack (regulatory PI could not be retrieved — flagged as a **blocking data gap**). However, the supporting literature surfaces safety signals worth noting for context:

- **Proarrhythmic risk**: Flecainide's clinical reputation is shaped by the CAST trial finding that Class Ic agents increased mortality when used to suppress ventricular arrhythmias post-myocardial infarction, making structural/ischaemic heart disease a key risk factor to screen for.
- **Sick sinus node caution**: Class Ic sodium-channel blockade can suppress sinus node conduction; sinus node dysfunction is a recognised relative contraindication.
- **Case-report signals**: overdose-associated Brugada ECG pattern (PMID 27884575) and refractory ventricular tachycardia (PMID 40800559).

Please refer to the TGA-approved Product Information (PI) for authoritative safety information before any clinical use.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted stroke benefit is mechanistically indirect (via AF rhythm control, not a direct anti-stroke effect), the drug is not currently marketed in Australia, and a blocking data gap exists for TGA/PI safety information — combined with flecainide's known proarrhythmic history, this does not yet meet the bar to proceed.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications, drug interactions)
- Confirmed mechanism of action detail (DrugBank MOA is currently a data gap)
- Clarification of whether AF-mediated stroke risk reduction offers meaningful benefit over established anticoagulation-based stroke prevention
- Route/dosage-form compatibility assessment for the Australian formulary, given the drug is not currently marketed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

