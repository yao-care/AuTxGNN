---
layout: default
title: Alprazolam
parent: 僅模型預測 (L5)
nav_order: 34
evidence_level: L5
indication_count: 10
---

# Alprazolam
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

# Alprazolam: From Anxiety and Panic Disorder to Insomnia

## One-Sentence Summary

Alprazolam is a high-potency triazolo-benzodiazepine with established international use for anxiety disorders and panic disorder, currently not registered on the Australian Register of Therapeutic Goods (ARTG).
The TxGNN model predicts it may be effective for **Insomnia**, with **7 clinical trials** and **18 publications** currently available to inform this direction.
Evidence is predominantly observational and comparative (Evidence Level L3), with significant clinical concerns around physical dependence and sleep architecture disruption limiting its role in chronic insomnia management.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anxiety disorders, panic disorder (established international use; not currently TGA-registered in Australia) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why Is This Prediction Reasonable?

Although detailed mechanism of action data from DrugBank is not available in this Evidence Pack, Alprazolam is a well-characterised benzodiazepine that acts as a positive allosteric modulator of GABA-A receptors. By enhancing inhibitory GABAergic neurotransmission across the CNS — particularly in the amygdala, limbic system, and reticular activating system — it produces anxiolytic, sedative, and hypnotic effects. This profile directly underpins the TxGNN prediction: the same mechanism that reduces hyperarousal in anxiety disorders can shorten sleep onset latency and increase total sleep time in insomnia.

The overlap between anxiety and insomnia is clinically well-established. Cognitive and physiological hyperarousal is a shared pathophysiological feature of both conditions. Alprazolam's rapid GABA-A modulation directly attenuates this state, explaining its documented use in clinical practice for acute insomnia — particularly when comorbid anxiety is present. Several comparative studies in the evidence base (e.g., PMID 33403184) explicitly evaluate alprazolam against other sleep aids, confirming its recognised role as a sedative-hypnotic agent.

However, the prediction carries important clinical caveats. Alprazolam suppresses slow-wave (NREM Stage 3) and REM sleep, disrupting normal sleep architecture with prolonged use. Current Australian and international guidelines — including those from the Therapeutic Guidelines (Australia) and the Royal Australasian College of Physicians — recommend Cognitive Behavioural Therapy for Insomnia (CBT-I) as first-line treatment, with benzodiazepines reserved for short-term adjunctive use only. The L3 evidence classification reflects the absence of large, definitive Phase 3 RCTs evaluating alprazolam as a primary investigational agent for insomnia in a contemporary trial setting.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT01584440](https://clinicaltrials.gov/study/NCT01584440) | Phase 2 | Completed | 220 | Double-blind, double-dummy, placebo-controlled RCT of AVP-923 (dextromethorphan/quinidine) for agitation in Alzheimer's disease; alprazolam included as pharmacological comparator for sedation and sleep-related outcomes |
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | Unknown | 1,400 | Prospective cohort study in Taiwan examining hypnotic medication use patterns (including benzodiazepines) in elderly patients with sleep disorders; evaluates efficacy, safety, pharmacokinetic and pharmacogenetic characteristics, and clinical outcomes |
| [NCT00266409](https://clinicaltrials.gov/study/NCT00266409) | Phase 4 | Completed | 418 | Multicenter, open-label, randomised trial comparing Niravam™ (alprazolam orally-disintegrating tablet) + SSRI/SNRI versus SSRI/SNRI alone in generalised anxiety disorder or panic disorder; primary endpoint time to anxiety symptom response with potential sleep-related secondary outcomes |
| [NCT03327506](https://clinicaltrials.gov/study/NCT03327506) | Phase 4 | Unknown | 128 | Randomised trial comparing hypnosis session versus alprazolam premedication for perioperative anxiety in gynaecological laparoscopy; addresses acute situational anxiety and sleep disruption rather than chronic insomnia |
| [NCT01146600](https://clinicaltrials.gov/study/NCT01146600) | Phase 2 | Completed | 26 | Clarithromycin for hypersomnia (hypothesised GABA-A-mediated endogenous somnogen mechanism); alprazolam used as pharmacological reference agent; limited direct relevance to insomnia as primary indication |
| [NCT01893632](https://clinicaltrials.gov/study/NCT01893632) | Phase 2 | Terminated | 2 | Gabapentin for benzodiazepine dependence treatment in patients with sedative-hypnotic use disorders; terminated early with only 2 participants enrolled — no statistical value |
| [NCT04572750](https://clinicaltrials.gov/study/NCT04572750) | N/A | Completed | 170 | Electronically-delivered patient self-management intervention to promote benzodiazepine cessation in veterans prescribed benzodiazepines for anxiety and sleep difficulties; focuses on safe discontinuation rather than therapeutic efficacy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [33403184](https://pubmed.ncbi.nlm.nih.gov/33403184/) | 2020 | Comparative RCT | Cureus | Head-to-head RCT comparing alprazolam versus melatonin for sleep disorders in end-stage renal disease patients on haemodialysis; evaluates subjective and objective sleep quality, fatigue reduction, and daytime functioning — direct evidence for alprazolam in sleep disorders |
| [39183410](https://pubmed.ncbi.nlm.nih.gov/39183410/) | 2024 | RCT (integrative) | Medicine | Retrospective controlled study (N=116) comparing Du Meridian moxibustion + ear acupuncture versus alprazolam (control arm) in coronary heart disease patients with comorbid insomnia; alprazolam used as active treatment comparator for cardiac patients with sleep disturbance |
| [35041261](https://pubmed.ncbi.nlm.nih.gov/35041261/) | 2022 | RCT | Brain and Behavior | Randomised controlled trial of eszopiclone for sleep quality and cognitive function in elderly patients with Alzheimer's disease and sleep disorders; provides comparative context for sedative-hypnotic drug class efficacy and cognitive risk in sleep-disordered populations |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Meta-analysis | Acta Pharmaceutica (Zagreb) | Systematic review and meta-analysis of tranquiliser use (including benzodiazepines such as alprazolam) in elderly patients with chronic non-communicable diseases; assesses optimal dosing, efficacy outcomes, and adverse effect profiles across study designs |
| [37801512](https://pubmed.ncbi.nlm.nih.gov/37801512/) | 2023 | Mechanistic Study | Aging | Proteomic analysis after 24-day repeated alprazolam administration in mice; identifies mitochondrial dysfunction in hippocampus leading to memory consolidation impairment — critical safety signal for chronic insomnia use |
| [38363887](https://pubmed.ncbi.nlm.nih.gov/38363887/) | 2024 | Cross-sectional | Medicine | Cross-sectional study of insomnia prevalence and influencing factors in COVID-19 survivors; documents alprazolam prescribing patterns in post-COVID insomnia and identifies risk factors associated with insomnia severity |
| [37984023](https://pubmed.ncbi.nlm.nih.gov/37984023/) | 2024 | Retrospective/Predictive Model | Value in Health Regional Issues | Ten-year predictive modelling of benzodiazepine use trends (prescribed for anxiety, insomnia, mood disorders, and epilepsy); highlights long-term safety signals including dependence, Alzheimer's disease risk, falls, and traffic accidents |
| [35493764](https://pubmed.ncbi.nlm.nih.gov/35493764/) | 2022 | Cohort Study | JHEP Reports | Deprescribing benzodiazepines (including zolpidem) reduces falls and fractures in patients with cirrhosis; important safety signal for vulnerable populations where insomnia and sedative-hypnotic use commonly co-occur |
| [25532388](https://pubmed.ncbi.nlm.nih.gov/25532388/) | 2014 | Real-world Analysis | China Journal of Chinese Materia Medica | Real-world analysis of concurrent diseases and medication use in 1,067 insomnia inpatients across 20 hospitals; identifies alprazolam as a commonly co-prescribed sedative-hypnotic and documents comorbidity patterns including hypertension and cerebrovascular disease |
| [15341891](https://pubmed.ncbi.nlm.nih.gov/15341891/) | 2004 | Observational Study | Sleep Medicine | Large managed-care population study examining hypnotic prescription patterns for insomnia treatment; documents the historical shift away from benzodiazepines toward non-hypnotic medications and contextualises alprazolam prescribing trends in insomnia |

---

## Australia Market Information

Alprazolam is **not currently registered on the Australian Register of Therapeutic Goods (ARTG)**. There are no active ARTG entries and the drug is not commercially available in Australia. Alprazolam was previously available in Australia under the brand name Xanax but was voluntarily withdrawn from the market. Under current Australian scheduling, alprazolam is listed as a Schedule 8 Controlled Drug (Appendix D), meaning its prescription is heavily restricted or prohibited in most states and territories.

Any proposed clinical use or investigation of alprazolam in Australia would require:
- TGA **Special Access Scheme (SAS)** Category B approval (or equivalent authorised prescriber pathway)
- State/territory controlled drugs authority approval prior to prescribing

---

## Safety Considerations

Please refer to the TGA Special Access Scheme documentation and the relevant Product Information (PI) for complete safety information, as no TGA-approved safety data is available in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
The TxGNN prediction is mechanistically plausible — alprazolam's GABA-A positive allosteric modulation produces genuine sedative-hypnotic effects capable of improving sleep onset latency and total sleep time. However, the evidence base (L3) consists primarily of observational studies, real-world analyses, and trials where alprazolam served as an active comparator rather than the primary investigational drug for insomnia. Critically, the drug has no current ARTG registration in Australia, is subject to Schedule 8 restrictions, and current guidelines explicitly recommend against benzodiazepines as first-line insomnia treatment due to dependence, tolerance, and sleep architecture disruption. The risk–benefit profile is unfavourable compared to approved first-line options (CBT-I, melatonin, low-dose doxepin, orexin receptor antagonists such as suvorexant).

**To proceed, the following is needed:**
- Assessment of TGA Special Access Scheme (SAS) pathway and state/territory Schedule 8 authority requirements before any clinical investigation in Australia
- A prospective RCT specifically evaluating alprazolam for acute insomnia in a defined population (e.g., patients with comorbid anxiety and insomnia) where the risk–benefit may be more favourable
- Head-to-head comparative data versus current Australian standard-of-care options (CBT-I, melatonin receptor agonists, suvorexant)
- Formal risk–benefit analysis addressing dependence liability, rebound insomnia, and cognitive effects — particularly for elderly patients and those with hepatic or renal impairment
- Retrieval of TGA Product Information (PI) and full safety data including warnings, contraindications, and drug interaction profile via SAS documentation
- Review of contemporary clinical practice guidelines (Therapeutic Guidelines: Psychotropic, Australia) to establish whether any clinical niche exists where alprazolam offers advantage over currently available and registered hypnotics

---

> ⚠️ **Disclaimer:** This report is produced for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. This document does not replace evaluation by a qualified Australian healthcare professional or regulatory assessment by the Therapeutic Goods Administration (TGA).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

