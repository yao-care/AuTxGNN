---
layout: default
title: Escitalopram
parent: 僅模型預測 (L5)
nav_order: 203
evidence_level: L5
indication_count: 10
---

# Escitalopram
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

# Escitalopram: From Major Depression to Dysthymic Disorder, OCD, and Agoraphobia

## One-Sentence Summary

Escitalopram is a highly selective serotonin reuptake inhibitor (SSRI) with established international use in major depressive disorder and anxiety-spectrum conditions, but currently not listed on the Australian Register of Therapeutic Goods (ARTG). The TxGNN model assigns high prediction scores for **Dysthymic Disorder** (98.55%), **Obsessive-Compulsive Disorder** (98.36%), and **Agoraphobia** (96.90%), supported by a combined pool of over 40 clinical trials and 40 publications across these three indications; the highest-ranked model prediction — Ohdo syndrome and variants — carries no supporting clinical evidence and is recommended as Hold.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not listed on ARTG (drug is internationally established for major depressive disorder and anxiety disorders) |
| Primary Predicted New Indication | Dysthymic Disorder |
| TxGNN Prediction Score | 98.55% (Dysthymic Disorder) · 98.36% (OCD) · 96.90% (Agoraphobia) |
| Evidence Level | L2 — all three actionable indications |
| Australia Market Status | Not listed on ARTG |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails (Dysthymic Disorder, OCD, Agoraphobia) · Hold (remaining predictions) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on established pharmacological knowledge, escitalopram is the S-enantiomer of citalopram — the most selective SSRI currently available. It acts by blocking the serotonin transporter (SERT), thereby increasing synaptic serotonin concentrations across limbic and cortical regions critical to mood and anxiety regulation.

**Dysthymic Disorder (Persistent Depressive Disorder, PDD):** Dysthymia shares the same core serotonergic pathophysiology as major depressive disorder — chronic low-grade SERT dysfunction leading to insufficient serotonin tone. Escitalopram's mechanism directly targets this deficit, and its pharmacokinetic profile (long half-life, linear kinetics) suits the prolonged pharmacological support that PDD's chronic course demands. The disease is now classified as Persistent Depressive Disorder in DSM-5, but the underlying serotonergic rationale is unchanged.

**Obsessive-Compulsive Disorder (OCD):** OCD involves hyperactivity in the orbitofrontal cortex–basal ganglia–thalamus circuit, with serotonergic and glutamatergic dysregulation. Escitalopram reduces excess serotonin signal transmission through SERT inhibition and may modulate prefrontal cortical function via 5-HT2C/2A receptor downregulation. Notably, escitalopram received European Medicines Agency (EMA) approval for OCD in 2007, based on two Phase 3 trials — providing strong regulatory precedent in a comparable market. Evidence from PMID 40457233 further shows that memantine (NMDA antagonist) augmentation of escitalopram improves executive function outcomes in OCD, supporting a dual serotonergic–glutamatergic mechanistic hypothesis.

**Agoraphobia:** Agoraphobia co-occurs with panic disorder in 70–80% of cases and shares amygdala–anterior cingulate serotonergic dysfunction and HPA axis hyperreactivity. Escitalopram reduces fear conditioning and amygdala hyperresponsiveness through SERT inhibition. Animal model evidence (PMID 32594260) confirms that serotonergic treatment normalises dopaminergic neuron activity in the periaqueductal grey — a region directly implicated in escape behaviour, which is central to agoraphobic avoidance.

---

## Clinical Trial Evidence

### Dysthymic Disorder

| Trial Number | Phase | Status | Enrolment | Key Findings |
|------------|------|--------|----------|------------|
| [NCT00220701](https://clinicaltrials.gov/study/NCT00220701) | Phase 4 | Completed | 36 | 12-week double-blind, placebo-controlled study of escitalopram (max 20 mg/day) directly in dysthymic disorder, with 12-week open-label extension; primary endpoint: superiority over placebo in depression severity, psychosocial, temperamental, and cognitive functioning |
| [NCT00234312](https://clinicaltrials.gov/study/NCT00234312) | Phase 4 | Completed | 40 | Head-to-head flexible-dose comparison of escitalopram vs sertraline specifically in dysthymic disorder and double depression; efficacy and safety primary endpoints |
| [NCT00296712](https://clinicaltrials.gov/study/NCT00296712) | Phase 4 | Completed | 55 | Combined escitalopram and bupropion as first-line treatment for depression in relatively medication-naïve patients; results informative for initiating therapy in chronic depressive states |
| [NCT01189812](https://clinicaltrials.gov/study/NCT01189812) | Phase 2 | Completed | 80 | DBRPCT of citalopram plus lithium vs citalopram plus placebo in depressive mood disorders; fixed-dose design provides dose-response data applicable to dysthymia spectrum |
| [NCT01973283](https://clinicaltrials.gov/study/NCT01973283) | Phase 4 | Completed | 100 | Open antidepressant treatment (citalopram or duloxetine) in older adults with depressive symptoms and frailty syndrome; long-term efficacy data in chronic depressive states |
| [NCT00080158](https://clinicaltrials.gov/study/NCT00080158) | Phase 2/3 | Completed | 120 | Three-arm comparison of treatments for depressed adolescents who had attempted suicide; high population specificity limits generalisability to dysthymia |

### Obsessive-Compulsive Disorder

| Trial Number | Phase | Status | Enrolment | Key Findings |
|------------|------|--------|----------|------------|
| [NCT00723060](https://clinicaltrials.gov/study/NCT00723060) | Phase 4 | Completed | 176 | Prospective, randomised, active-controlled, double-blind multi-centre trial comparing conventional dose (20 mg) vs high dose (40 mg) escitalopram in OCD; primary outcome Y-BOCS score |
| [NCT00305500](https://clinicaltrials.gov/study/NCT00305500) | Phase 3 | Completed | 100 | Open-label prospective study of high-dose escitalopram (up to 50 mg/day) in OCD; dose titration based on Y-BOCS response over 18 weeks — reflects the clinical principle that OCD requires higher SERT occupancy (>80%) than depression |
| [NCT00116532](https://clinicaltrials.gov/study/NCT00116532) | Phase 4 | Completed | 30 | Assessment of escitalopram efficacy and optimal dosing in OCD outpatients |
| [NCT00215137](https://clinicaltrials.gov/study/NCT00215137) | Phase 2 | Completed | 14 | Pilot safety and effectiveness study of escitalopram in OCD; early proof-of-concept for the indication |
| [NCT00368862](https://clinicaltrials.gov/study/NCT00368862) | Phase 4 | Completed | 80 | Active-comparator RCT of memantine vs escitalopram; NMDA antagonist comparison provides mechanistic insights for combination therapy approaches |
| [NCT00115011](https://clinicaltrials.gov/study/NCT00115011) | Phase 4 | Completed | 30 | Escitalopram in self-injurious skin picking (OCD-spectrum disorder); supports broad efficacy across compulsive behaviour phenotypes |
| [NCT01936051](https://clinicaltrials.gov/study/NCT01936051) | N/A | Completed | 12 | PK/PD modelling of plasma concentration vs SERT occupancy in OCD patients; includes ABCB1 pharmacogenomics — mechanistic validation study |
| [NCT00456937](https://clinicaltrials.gov/study/NCT00456937) | Phase 4 | Completed | 15 | Open-label escitalopram in schizophrenia comorbid with OCD; safety and efficacy in complex presentations |
| [NCT02022709](https://clinicaltrials.gov/study/NCT02022709) | Phase 4 | Completed | 78 | Efficacy of SSRIs vs exposure and response prevention (ERP) and combined therapy in Chinese OCD patients; identifies biological and psychological predictors of treatment response |
| [NCT04336228](https://clinicaltrials.gov/study/NCT04336228) | Phase 4 | Active, not recruiting | 46 | Mechanistic study of central serotonin system status in compulsive behaviour and effects of sub-chronic escitalopram; investigating cognitive and brain activation changes |

### Agoraphobia

| Trial Number | Phase | Status | Enrolment | Key Findings |
|------------|------|--------|----------|------------|
| [NCT03522844](https://clinicaltrials.gov/study/NCT03522844) | Phase 4 | Completed | 276 | First large RCT comparing Mindfulness-Based Stress Reduction (MBSR) vs escitalopram (described as gold-standard SSRI) for anxiety disorders including agoraphobia; high-quality real-world comparative effectiveness data |
| [NCT00711737](https://clinicaltrials.gov/study/NCT00711737) | N/A | Completed | 27 | Open-label 6-month metabolic safety study in patients with depression, GAD, or panic disorder with or without agoraphobia treated with escitalopram |
| [NCT05210140](https://clinicaltrials.gov/study/NCT05210140) | N/A | Unknown | 148 | CYP2C19 genotype-guided personalised dosing study in patients receiving escitalopram, including those with agoraphobia; pharmacogenomics data for dose optimisation |

---

## Literature Evidence

### Dysthymic Disorder

| PMID | Year | Type | Journal | Key Findings |
|-----|------|------|--------|------------|
| [21811192](https://pubmed.ncbi.nlm.nih.gov/21811192/) | 2010 | RCT | Int Clin Psychopharmacol | Published results of NCT00220701: 12-week DBRPCT of escitalopram (max 20 mg/day) vs placebo in 36 outpatients with DSM-diagnosed dysthymic disorder; core evidence for this specific indication |
| [21527126](https://pubmed.ncbi.nlm.nih.gov/21527126/) | 2011 | Meta-analysis | J Clin Psychiatry | Meta-analysis of placebo-controlled RCTs of antidepressants in dysthymic disorder; compared response and remission rates between dysthymia and MDD to determine antidepressant utility |
| [19820552](https://pubmed.ncbi.nlm.nih.gov/19820552/) | 2009 | Review/RCT | J Psychiatr Pract | Investigation of whether dual antidepressant therapy as initial treatment improves remission rates; escitalopram included as treatment arm — only 30–40% of patients remit at 8 weeks with monotherapy |
| [29683474](https://pubmed.ncbi.nlm.nih.gov/29683474/) | 2018 | Cochrane Review | Cochrane Database Syst Rev | Cochrane systematic review of antidepressants for depression in people with cancer; covers broad depressive spectrum including dysthymic presentations |
| [25647343](https://pubmed.ncbi.nlm.nih.gov/25647343/) | 2015 | Mechanistic Study | Psychoneuroendocrinology | Escitalopram treatment shifts immune profile toward Th2 responses and increases innate immunity modulators in depressed patients; relevant to chronic inflammatory hypothesis of persistent depression |
| [21448115](https://pubmed.ncbi.nlm.nih.gov/21448115/) | 2011 | Case Series | Psychiatria Danubina | Clinical management of dysthymia complicated by allergic reactions to sertraline and escitalopram during a three-year treatment period; real-world switching strategy experience |

### Obsessive-Compulsive Disorder

| PMID | Year | Type | Journal | Key Findings |
|-----|------|------|--------|------------|
| [17240120](https://pubmed.ncbi.nlm.nih.gov/17240120/) | 2007 | RCT | Eur Neuropsychopharmacol | Landmark relapse prevention trial: 468 OCD patients treated open-label; 320 responders randomised to escitalopram vs placebo for 24 weeks — significant advantage for escitalopram in time to relapse (p<0.001) |
| [17407626](https://pubmed.ncbi.nlm.nih.gov/17407626/) | 2007 | RCT | Curr Med Res Opin | Randomised, placebo-controlled, paroxetine-referenced, fixed-dose 24-week study of escitalopram in OCD; one of two pivotal trials supporting EMA approval |
| [40457233](https://pubmed.ncbi.nlm.nih.gov/40457233/) | 2025 | RCT | BMC Psychiatry | DBRPCT of memantine augmentation of escitalopram in OCD; memantine improves executive function outcomes in patients not fully responding to escitalopram alone — supports SERT + NMDA dual approach |
| [35121274](https://pubmed.ncbi.nlm.nih.gov/35121274/) | 2022 | Meta-analysis | J Psychiatr Res | Network meta-analysis comparing pharmacological and psychological treatments in children and adolescents with OCD; SSRIs versus CBT and combined strategies |
| [38703743](https://pubmed.ncbi.nlm.nih.gov/38703743/) | 2024 | Systematic Review | Compr Psychiatry | Long-term safety and tolerability of off-label high-dose SRIs in OCD; addresses key clinical question of dose escalation beyond standard 20 mg escitalopram |
| [18345966](https://pubmed.ncbi.nlm.nih.gov/18345966/) | 2008 | Review | Expert Rev Neurother | Expert review of escitalopram's EMA OCD approval (2007); covers acute efficacy (10–20 mg/day), relapse prevention data, and positioning among OCD pharmacotherapies |
| [18567973](https://pubmed.ncbi.nlm.nih.gov/18567973/) | 2008 | Clinical Study | CNS Spectr | Analysis of OCD symptom dimension response to 12 weeks escitalopram vs placebo; not all OCD dimensions respond equally — relevant for patient selection |
| [34313207](https://pubmed.ncbi.nlm.nih.gov/34313207/) | 2022 | RCT Sub-analysis | CNS Spectr | BDNF Val66Met polymorphism moderates escitalopram and paroxetine response in OCD; 40–60% of patients do not respond adequately to SSRIs — pharmacogenomics stratification opportunity |
| [28477500](https://pubmed.ncbi.nlm.nih.gov/28477500/) | 2017 | Meta-analysis | J Affect Disord | OCD shows reduced placebo response compared to other anxiety disorders; implications for clinical trial design and interpretation of effect sizes |
| [17603402](https://pubmed.ncbi.nlm.nih.gov/17603402/) | 2007 | Open-label Trial | CNS Spectr | Open-label pilot of escitalopram in OCD (n=21); approximately 40% non-response rate confirms need for augmentation strategies alongside SSRI use |

### Agoraphobia

| PMID | Year | Type | Journal | Key Findings |
|-----|------|------|--------|------------|
| [35045991](https://pubmed.ncbi.nlm.nih.gov/35045991/) | 2022 | Network Meta-analysis | BMJ | Network meta-analysis of panic disorder with or without agoraphobia — identifies individual SSRIs with highest remission and lowest adverse events; directly relevant to escitalopram positioning |
| [38014714](https://pubmed.ncbi.nlm.nih.gov/38014714/) | 2023 | Cochrane Network Meta-analysis | Cochrane Database Syst Rev | Comprehensive Cochrane network meta-analysis of pharmacological treatments for panic disorder in adults; definitive evidence synthesis for this class |
| [14658946](https://pubmed.ncbi.nlm.nih.gov/14658946/) | 2003 | RCT | J Clin Psychiatry | DBRPCT of escitalopram in panic disorder; significant efficacy over placebo with good tolerability — foundational efficacy evidence in panic spectrum including agoraphobia |
| [37676054](https://pubmed.ncbi.nlm.nih.gov/37676054/) | 2023 | Systematic Review | Expert Rev Neurother | Systematic review of pharmacological management of panic disorder in older patients; important for dose considerations in elderly populations |
| [16953656](https://pubmed.ncbi.nlm.nih.gov/16953656/) | 2006 | Review | CNS Drugs | Comprehensive review of escitalopram in GAD, social anxiety disorder, panic disorder with or without agoraphobia, and OCD — summarises efficacy across the full anxiety spectrum |
| [32594260](https://pubmed.ncbi.nlm.nih.gov/32594260/) | 2020 | Preclinical | Brain Struct Funct | Escitalopram normalises periaqueductal grey (PAG)-induced anticipatory fear behaviour and dopaminergic neuron hyperactivity in rodent agoraphobia model — mechanistic basis for anti-agoraphobic effect |
| [17017830](https://pubmed.ncbi.nlm.nih.gov/17017830/) | 2006 | Clinical Study | J Clin Psychiatry | Post-hoc analysis of remission thresholds for panic disorder and anxiety disorders using CGI and disorder-specific scales from escitalopram trials; defines clinical response benchmarks |
| [32087339](https://pubmed.ncbi.nlm.nih.gov/32087339/) | 2020 | Trial Protocol | Contemp Clin Trials | TAME trial design: first non-inferiority RCT of MBSR vs escitalopram for anxiety disorders including agoraphobia — escitalopram used as gold-standard comparator |
| [22090798](https://pubmed.ncbi.nlm.nih.gov/22090798/) | 2011 | Review | Neuropsychiatr Dis Treat | Summary of pharmacological treatments for complex agoraphobia based on clinical trials from 2000 onwards; positions SSRIs as primary pharmacotherapy |
| [17694478](https://pubmed.ncbi.nlm.nih.gov/17694478/) | 2007 | Clinical Study | Pharmacopsychiatry | Quality of life improvement in panic disorder with escitalopram, citalopram, or placebo; outcomes beyond symptom count relevant to treatment value assessment |

---

## Australia Market Information

Escitalopram is currently **not listed on the Australian Register of Therapeutic Goods (ARTG)**. No ARTG entries were identified in the regulatory data search conducted for this report.

> **Important note for clinicians:** This report is based on available regulatory data at the time of search (April 2026). Escitalopram is approved in numerous comparable regulatory markets (EU, USA, UK, Canada) under brand names including Lexapro and Cipralex. Healthcare professionals should verify the current ARTG registration status directly via the TGA website (www.tga.gov.au) and confirm access pathways (e.g., Special Access Scheme or Authorised Prescriber arrangements) before any clinical use.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) or applicable international Product Information for safety information. No Australian-specific safety data (key warnings, contraindications, or drug-drug interactions) were available in the current Evidence Pack.

> For context, escitalopram's internationally documented safety concerns include: dose-dependent QTc interval prolongation, serotonin syndrome risk with concomitant serotonergic or MAO-inhibiting agents, increased suicidality risk in paediatric and young adult populations (under 25 years), and neonatal adaptation syndrome with third-trimester use. These should be reviewed from current international PI documents until an Australian PI is confirmed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails — Dysthymic Disorder, OCD, and Agoraphobia**
**Decision: Hold — Ohdo Syndrome and Variants, Blepharophimosis–Ohdo Type, Benign Paroxysmal Torticollis of Infancy, Histrionic Personality Disorder, Schizoid Personality Disorder, Schizotypal Personality Disorder**

**Rationale:**

- **Dysthymic Disorder:** A completed Phase 4 DBRPCT (NCT00220701, n=36) directly studied escitalopram in dysthymic disorder, with the published paper (PMID 21811192) and a supporting meta-analysis (PMID 21527126) confirming antidepressant benefit in this population. Evidence meets L2 criteria. The relatively small sample size (n=36) is the primary limitation.
- **OCD:** Multiple completed Phase 3 and 4 trials — including two pivotal trials supporting EMA approval in 2007 — provide the strongest evidence base of the three indications. The European regulatory precedent and a 2025 published RCT (PMID 40457233) further strengthen this finding. Evidence meets L2 criteria and approaches L1 given the breadth of evidence.
- **Agoraphobia:** A large Phase 4 comparative effectiveness trial (NCT03522844, n=276) and two high-quality network meta-analyses (BMJ 2022; Cochrane 2023) provide robust indirect evidence, primarily through the panic disorder–agoraphobia comorbidity pathway. Evidence meets L2 criteria.
- **Hold indications:** Ohdo syndrome variants, blepharophimosis–Ohdo type, benign paroxysmal torticollis of infancy, and cluster A personality disorders (histrionic, schizoid, schizotypal) carry no mechanistic rationale directly linking SERT function to disease pathology and have zero supporting clinical studies. High TxGNN scores in these conditions likely reflect non-specific knowledge graph connectivity via shared symptom nodes (e.g., intellectual disability, behavioural disturbance) rather than disease-specific predictions.

**To proceed, the following is needed:**

- Confirm current ARTG registration status directly via the TGA website — escitalopram may be listed under a trade name not captured in the current data search
- Obtain and review TGA-approved or applicable international Product Information for full contraindication, warning, and drug interaction data before clinical use
- **Dysthymic Disorder:** Consider pursuing or identifying a larger confirmatory RCT given the small sample size (n=36) of the primary trial; review Medicare item numbers for chronic depression management
- **OCD:** Review current Australian and New Zealand clinical psychiatry guidelines for SSRI use in OCD, including dose escalation protocols (evidence supports doses up to 40–50 mg for treatment-resistant cases)
- **Agoraphobia:** Clarify whether agoraphobia is a standalone registered indication internationally or only approved as "panic disorder with agoraphobia" — this affects labelling and regulatory pathway
- Establish a pharmacovigilance plan covering QTc monitoring (baseline and follow-up ECG), serotonin syndrome prevention, and suicidality surveillance (especially for patients under 25 years)
- Commission a formal health technology assessment for any indication being considered for TGA registration or Special Access Scheme use in Australia

---

*This report is intended for research and evaluation purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. Data cutoff: 4 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

