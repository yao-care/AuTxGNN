---
layout: default
title: Armodafinil
parent: 僅模型預測 (L5)
nav_order: 56
evidence_level: L5
indication_count: 10
---

# Armodafinil
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

# Armodafinil: From Excessive Sleepiness to Insomnia

## One-Sentence Summary

Armodafinil (Nuvigil®) is a non-amphetamine wakefulness-promoting agent — the R-enantiomer of modafinil — approved internationally for excessive sleepiness associated with narcolepsy, obstructive sleep apnoea (OSA), and shift work disorder, though it is not currently registered in Australia.
The TxGNN model predicts it may be effective for **Insomnia**, with **12 clinical trials** and **19 publications** currently supporting this direction.
Evidence strength is rated **L1**, with multiple completed randomised controlled trials directly investigating armodafinil in insomnia-specific populations.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Excessive sleepiness (narcolepsy, OSA, shift work disorder) — not registered in Australia |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on published pharmacology, armodafinil is a selective dopamine transporter (DAT) inhibitor that elevates synaptic dopamine concentrations in the prefrontal cortex and striatum. It also activates the noradrenaline, histamine, and orexin (hypocretin) pathways to promote sustained, natural-feeling wakefulness. This mechanism is distinct from traditional amphetamine-class stimulants, which act via broad monoamine release rather than selective reuptake inhibition.

The link between a wakefulness-promoting drug and insomnia treatment is counterintuitive but mechanistically grounded in the two-process model of sleep regulation. A recognised subtype of insomnia involves chronic cortical hyperarousal combined with a weakened homeostatic sleep drive (Process S). By robustly consolidating daytime wakefulness and alertness, armodafinil may help rebuild nocturnal sleep pressure by evening, indirectly improving sleep initiation and maintenance. This rationale has been specifically tested as an adjunct to cognitive behavioural therapy for insomnia (CBT-I), where daytime sleepiness — a common side effect of sleep restriction therapy — can undermine patient adherence and outcomes.

Clinical evidence supports this hypothesis most strongly in oncology settings. Patients recovering from chemotherapy frequently experience a syndrome of co-occurring insomnia and cancer-related fatigue, where the disrupted wake–sleep cycle responds poorly to CBT-I alone. Armodafinil has been directly investigated in this population across multiple trials (NCT01019187, NCT01011218, NCT01091974). Separately, the treatment of insomnia comorbid with sleep-disordered breathing (NCT02552303) has also been studied, targeting patients with residual insomnia despite CPAP use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT01019187](https://clinicaltrials.gov/study/NCT01019187) | Phase 2 | Completed | 226 | Randomised Phase II trial of CBT-I ± armodafinil for insomnia and fatigue in cancer survivors post-chemotherapy; primary insomnia-targeted armodafinil study |
| [NCT01091974](https://clinicaltrials.gov/study/NCT01091974) | Phase 2 | Completed | 138 | Four-arm RCT of CBT-I and armodafinil in breast cancer patients with post-chemotherapy sleep disturbances; evaluates insomnia outcomes across behavioural and pharmacological arms |
| [NCT02552303](https://clinicaltrials.gov/study/NCT02552303) | N/A | Completed | 39 | Direct study of armodafinil, CBT-I, or combination for sleep continuity in insomnia comorbid with obstructive sleep apnoea; also evaluated CPAP adherence |
| [NCT01011218](https://clinicaltrials.gov/study/NCT01011218) | Phase 2 | Completed | 70 | Pilot study of BBT-I or CBT-I ± armodafinil 150 mg/day in breast cancer patients with insomnia; four-arm design providing preliminary dose-response data |
| [NCT01080807](https://clinicaltrials.gov/study/NCT01080807) | Phase 4 | Completed | 385 | Post-marketing RCT of armodafinil 150 mg in shift work disorder; assessed clinical condition late in shift including commute safety, with functional outcomes |
| [NCT01072630](https://clinicaltrials.gov/study/NCT01072630) | Phase 3 | Completed | 492 | Largest completed Phase 3 double-blind RCT of armodafinil (150 and 200 mg/day) as adjunctive therapy in bipolar I major depression; provides robust safety and tolerability dataset |
| [NCT01072929](https://clinicaltrials.gov/study/NCT01072929) | Phase 3 | Completed | 433 | Double-blind, placebo-controlled Phase 3 study of armodafinil adjunctive therapy in bipolar I depression; parallel-group fixed-dosage design |
| [NCT01305408](https://clinicaltrials.gov/study/NCT01305408) | Phase 3 | Completed | 399 | Third independent Phase 3 RCT of armodafinil 150 mg/day in bipolar I depression; combined with the two sibling trials, total n >1,300 |
| [NCT01121536](https://clinicaltrials.gov/study/NCT01121536) | Phase 3 | Terminated | 867 | 6-month open-label safety extension in bipolar I disorder; largest enrolment of any armodafinil trial, providing the most extensive long-term safety data despite early termination |
| [NCT00678691](https://clinicaltrials.gov/study/NCT00678691) | Phase 4 | Completed | 55 | 8-week double-blind RCT of armodafinil augmentation for fibromyalgia fatigue; indirect evidence supporting armodafinil's utility across fatigue- and sleep-adjacent conditions |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [18729534](https://pubmed.ncbi.nlm.nih.gov/18729534/) | 2008 | Evidence-Based Review | Drugs | Comprehensive review of modafinil (armodafinil's parent compound) across approved and investigational uses based on double-blind RCTs; covers sleep disorders, fatigue, and cognition |
| [24312590](https://pubmed.ncbi.nlm.nih.gov/24312590/) | 2013 | Systematic Review & Meta-analysis | PLoS ONE | Meta-analysis of modafinil for fatigue and excessive daytime sleepiness in neurological disorders; methodology directly applicable to armodafinil as its longer-acting R-enantiomer |
| [22021174](https://pubmed.ncbi.nlm.nih.gov/22021174/) | 2011 | Systematic Review (MDS Task Force) | Movement Disorders | Movement Disorder Society EBM update on non-motor PD treatments, including wake-promoting agents for sleep and arousal disorders |
| [27010071](https://pubmed.ncbi.nlm.nih.gov/27010071/) | 2016 | Systematic Review | Parkinsonism & Related Disorders | SR of pharmacological interventions for daytime sleepiness and sleep disorders in Parkinson's disease; includes evidence on modafinil/armodafinil |
| [17181377](https://pubmed.ncbi.nlm.nih.gov/17181377/) | 2006 | Narrative Review | Drugs | Shift work sleep disorder: burden of illness, co-morbidities, and pharmacological management options including armodafinil/modafinil |
| [24138359](https://pubmed.ncbi.nlm.nih.gov/24138359/) | 2013 | Narrative Review | Medical Journal of Australia | Australian-specific review: approximately 1.5 million Australian shift workers affected; discusses insomnia, circadian disruption, sleep apnoea, and shift work disorder management |
| [21904092](https://pubmed.ncbi.nlm.nih.gov/21904092/) | 2011 | Narrative Review | Postgraduate Medicine | Emerging theories and therapies for shift work disorder; covers pharmacological management of sleep/wake dysregulation in shift workers |
| [39535843](https://pubmed.ncbi.nlm.nih.gov/39535843/) | 2024 | Narrative Review | Expert Opinion on Pharmacotherapy | Pharmacological and non-pharmacological management of sleep disturbances in Parkinson's disease; covers wake-promoting agents and their role in sleep disorder subtypes |
| [24272458](https://pubmed.ncbi.nlm.nih.gov/24272458/) | 2014 | Narrative Review | Neurotherapeutics | Treatment of sleep disorders in Parkinson's disease, including insomnia; preliminary evidence for CBT, light therapy, and wake-promoting agents |
| [20166851](https://pubmed.ncbi.nlm.nih.gov/20166851/) | 2010 | Narrative Review | Expert Opinion on Emerging Drugs | Emerging treatments for narcolepsy and related disorders; reviews armodafinil's pharmacological profile and positioning relative to modafinil |

---

## Australia Market Information

Armodafinil is **not registered on the Australian Register of Therapeutic Goods (ARTG)** and holds no current TGA marketing authorisation. There are **0 ARTG entries** for this drug.

Australian clinicians wishing to use armodafinil would need to explore access through one of the following TGA pathways:

- **Special Access Scheme Category B (SAS-B)**: Approval required from TGA for individual patients on a case-by-case basis
- **Authorised Prescriber (AP) pathway**: For clinicians regularly treating a defined patient population who wish to prescribe an unapproved product on an ongoing basis

Note: Modafinil (the racemic parent compound of armodafinil) is registered in Australia under multiple ARTG entries and may serve as a practical alternative pending any armodafinil registration application.

---

## Safety Considerations

A clinically important safety signal has been identified in the published literature:

- **Serious Skin Reactions — Stevens-Johnson Syndrome (SJS)**: A case of SJS following armodafinil initiation has been reported in the literature (PMID [29734973](https://pubmed.ncbi.nlm.nih.gov/29734973/), 2018), in a 21-year-old woman. Although SJS/toxic epidermal necrolysis (TEN) is listed as a risk on armodafinil's international product label, this was the first published case report. Clinicians should counsel patients to seek immediate medical attention for any new rash, blistering, or mucosal involvement, particularly within the first few weeks of therapy.

For comprehensive safety information — including full prescribing warnings, contraindications, and drug interactions — please refer to the **FDA-approved Nuvigil® Prescribing Information**, as no TGA-approved Product Information (PI) currently exists for Australia. Particular attention should be paid to known modafinil class interactions, including:
- CYP3A4/5 induction (may reduce efficacy of hormonal contraceptives and cyclosporin)
- CYP2C19 inhibition (may increase plasma levels of phenytoin, diazepam, propranolol)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 2 RCTs directly investigate armodafinil for insomnia in specific populations (cancer survivors, insomnia comorbid with sleep-disordered breathing), and a high-quality meta-analysis of the closely related modafinil provides mechanistic and pharmacological support. The biological rationale — strengthening daytime wakefulness to rebuild homeostatic sleep drive overnight — is plausible and has been tested in clinical settings. However, armodafinil is not registered in Australia, detailed local MOA and safety data are absent, and existing RCTs target specific insomnia subgroups rather than primary insomnia in the general population.

**To proceed, the following is needed:**
- **Regulatory pathway**: Determine appropriate TGA access route (SAS-B or Authorised Prescriber); consider whether modafinil (ARTG-registered) is a practical near-term alternative
- **MOA documentation**: Retrieve full mechanism of action data from DrugBank (DB06413) to formally support the mechanistic rationale for insomnia
- **Safety profile review**: Obtain and review FDA Nuvigil® PI in full, paying particular attention to SJS/TEN risk, psychiatric adverse events (anxiety, agitation), cardiovascular effects, and pregnancy category
- **Drug interaction assessment**: Formal DDI review, particularly for CYP3A4 induction and CYP2C19 inhibition — relevant to patients on hormonal contraceptives, anticoagulants, or antiepileptics
- **Target population definition**: Clarify the clinical indication scope — primary insomnia vs. insomnia comorbid with cancer fatigue, hypersomnolence, or sleep-disordered breathing — as efficacy evidence differs substantially across subgroups
- **Prospective evidence**: Consider initiating a Phase 2 RCT or prospective observational study specifically in primary insomnia (non-oncology) to close the evidence gap for the broader indication

> **Disclaimer**: This report is intended for research and clinical planning purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

