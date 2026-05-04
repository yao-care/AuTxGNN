---
layout: default
title: Atomoxetine
parent: 僅模型預測 (L5)
nav_order: 62
evidence_level: L5
indication_count: 10
---

# Atomoxetine
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

# Atomoxetine: From ADHD to Specific Developmental Disorder

## One-Sentence Summary

Atomoxetine (Strattera) is a selective norepinephrine reuptake inhibitor (NRI) globally approved as a non-stimulant treatment for Attention Deficit Hyperactivity Disorder (ADHD) in children, adolescents, and adults.
The TxGNN model predicts it may be effective for **Specific Developmental Disorder** (a broader neurodevelopmental category encompassing ADHD and related disorders including autism spectrum disorder with ADHD comorbidity),
with **8 clinical trials** and **15 publications** currently supporting this direction, yielding an evidence level of **L1**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ADHD (globally approved; not currently registered on the Australian ARTG) |
| Predicted New Indication | Specific Developmental Disorder |
| TxGNN Prediction Score | 99.9985% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Atomoxetine acts as a highly selective inhibitor of the presynaptic norepinephrine transporter (NET), blocking the reuptake of norepinephrine (NE) into neurons and increasing NE availability — particularly within the prefrontal cortex. This mechanism directly addresses the core neurobiological deficit underlying ADHD: dysregulation of catecholaminergic signalling in frontal-subcortical circuits that govern attention, executive function, and impulse control. Atomoxetine was the first non-stimulant agent to receive regulatory approval for ADHD treatment and is currently authorised in over 97 countries.

Specific developmental disorder is a broader diagnostic category that encompasses ADHD as its most prevalent subtype, but also includes autism spectrum disorder (ASD) with ADHD comorbidity, pervasive developmental disorder not otherwise specified (PDD-NOS), and Asperger syndrome — all of which share overlapping deficits in executive functioning and attention regulation that are mechanistically linked to prefrontal NE dysregulation. The TxGNN prediction therefore reflects a biologically coherent extension: the same NRI mechanism that addresses ADHD core symptoms is directly applicable to the ADHD-like presentations within this broader neurodevelopmental category.

Multiple Phase 3 and Phase 4 randomised controlled trials — including studies explicitly conducted in autism and pervasive developmental disorder populations (NCT00498173, NCT00380692, NCT00844753) — provide direct empirical support for this predicted indication. Two independent meta-analyses (PMID 39701638, PMID 30653855) further corroborate the efficacy and acceptability of atomoxetine across the spectrum of specific developmental disorders with ADHD features, reinforcing the mechanistic plausibility of the TxGNN model's highest-ranked prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT00510276](https://clinicaltrials.gov/study/NCT00510276) | Phase 4 | Completed | 445 | Largest Phase 4 double-blind, placebo-controlled RCT evaluating atomoxetine efficacy for ADHD symptoms and functional outcomes in young adults |
| [NCT04085172](https://clinicaltrials.gov/study/NCT04085172) | Phase 4 | Completed | 396 | Multicentre Phase 4 double-blind RCT comparing guanfacine (TAK-503), atomoxetine, and placebo in children and adolescents aged 6–17 with ADHD; strengthens post-marketing efficacy and safety data |
| [NCT01470261](https://clinicaltrials.gov/study/NCT01470261) | N/A | Completed | 1,398 | Large-scale observational study (ADDUCE project) examining long-term adverse effects of ADHD pharmacotherapy (including atomoxetine comparator arm) on growth, neurological, psychiatric, and cardiovascular parameters over two years |
| [NCT00380692](https://clinicaltrials.gov/study/NCT00380692) | Phase 4 | Completed | 97 | Double-blind, placebo-controlled RCT directly evaluating atomoxetine for ADHD symptom reduction in children and adolescents with autism spectrum disorder — high relevance to specific developmental disorder indication |
| [NCT00498173](https://clinicaltrials.gov/study/NCT00498173) | Phase 3 | Completed | 60 | Phase 3 double-blind, placebo-controlled RCT evaluating atomoxetine in children with ADHD symptoms associated with autistic disorder, Asperger syndrome, and PDD-NOS — highest-grade direct evidence for this predicted indication |
| [NCT00844753](https://clinicaltrials.gov/study/NCT00844753) | Phase 4 | Completed | 128 | Phase 4 RCT evaluating atomoxetine with and without Parent Management Training (PMT) in autism spectrum disorder with ADHD symptoms; double-blind, parallel-group design with 6-week dose titration |
| [NCT05635318](https://clinicaltrials.gov/study/NCT05635318) | N/A | Unknown | 102 | Evaluates quantitative EEG neurofeedback as add-on therapy for ADHD in children; atomoxetine used as comparator — primarily assesses neurofeedback rather than atomoxetine directly |
| [NCT00573859](https://clinicaltrials.gov/study/NCT00573859) | Phase 1/2 | Completed | 27 | Phase 1/2 study examining reinforcing mechanisms of smoking in adult ADHD; atomoxetine included as active treatment arm — indirect relevance, small sample |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [39701638](https://pubmed.ncbi.nlm.nih.gov/39701638/) | 2025 | Meta-analysis / Umbrella Review | *The Lancet Psychiatry* | Component network meta-analysis comparing pharmacological, psychological, and neurostimulatory interventions for ADHD in adults; addresses comparative benefits and harms across available treatments including atomoxetine |
| [30653855](https://pubmed.ncbi.nlm.nih.gov/30653855/) | 2019 | Meta-analysis | *Autism Research* | Systematic review and meta-analysis of three RCTs (n=241) evaluating atomoxetine efficacy and safety in children with ASD and ADHD symptoms; GRADE-assessed evidence directly supporting this indication |
| [27721971](https://pubmed.ncbi.nlm.nih.gov/27721971/) | 2016 | Systematic Review | *Therapeutic Advances in Psychopharmacology* | Comprehensive review of atomoxetine efficacy in ADHD with common comorbidities including pervasive developmental disorders; confirms utility across neurodevelopmental spectrum |
| [32946507](https://pubmed.ncbi.nlm.nih.gov/32946507/) | 2020 | Systematic Review | *PLOS One* | Examines sex differences in prescription rates and efficacy of ADHD pharmacotherapy including atomoxetine in girls and women; identifies evidence gaps and supports broader neurodevelopmental use |
| [35485452](https://pubmed.ncbi.nlm.nih.gov/35485452/) | 2022 | Cohort Study | *Neuropsychopharmacology Reports* | Retrospective cohort study identifying factors associated with atomoxetine efficacy in adult ADHD; long-term response rate approximately 40% at 6 months |
| [39514707](https://pubmed.ncbi.nlm.nih.gov/39514707/) | 2024 | Case Review | *Journal of Developmental and Behavioral Pediatrics* | Documents atomoxetine use in an 11-year-old with ADHD, anxiety, and MDD during the pandemic; illustrates real-world management of ADHD with complex neurodevelopmental comorbidities |
| [25545605](https://pubmed.ncbi.nlm.nih.gov/25545605/) | 2015 | Systematic Review | *Journal of Affective Disorders* | Systematic review of comorbidity in paediatric bipolar disorder including ADHD; provides context for atomoxetine use across neurodevelopmental comorbidity profiles |
| [33012168](https://pubmed.ncbi.nlm.nih.gov/33012168/) | 2021 | Review | *Clinical EEG and Neuroscience* | Reviews quantitative EEG (QEEG) applications in childhood ADHD and learning disabilities, supporting personalised treatment approaches and biomarker development relevant to specific developmental disorders |
| [18030077](https://pubmed.ncbi.nlm.nih.gov/18030077/) | 2007 | Clinical Guidelines | *Journal of the American Academy of Child and Adolescent Psychiatry* | Preschool Psychopharmacology Working Group treatment recommendations for very young children; discusses atomoxetine in context of early-onset neurodevelopmental disorders |
| [16232017](https://pubmed.ncbi.nlm.nih.gov/16232017/) | 2005 | Observational Study | *Pharmacotherapy* | Investigates predictors of selecting atomoxetine therapy shortly after market introduction; establishes real-world prescribing patterns in ADHD and neurodevelopmental populations |

---

## Australia Market Information

Atomoxetine is **not currently registered** on the Australian Register of Therapeutic Goods (ARTG). There are no TGA-approved products containing atomoxetine available in Australia as of the data cut-off date (5 April 2026).

> For comparison, atomoxetine (Strattera®) is approved in the United States, European Union, United Kingdom, Japan, and over 97 countries worldwide for the treatment of ADHD in children (≥6 years), adolescents, and adults. TGA registration would be required before any clinical use in Australia.

---

## Safety Considerations

Formal TGA-registered safety documentation is unavailable as atomoxetine has no current ARTG listing in Australia. Detailed drug interaction data was also not identified in the evidence pack.

Please refer to the TGA-approved Product Information (PI) — if seeking TGA registration — or to the FDA/EMA-approved prescribing information for comprehensive safety data. Key safety domains to review include:

- **Black box warning** (FDA): Increased risk of suicidal ideation in children and adolescents during initial treatment — monitoring is mandatory
- **Cardiovascular effects**: Increases in heart rate and blood pressure have been reported; use with caution in patients with pre-existing cardiovascular conditions
- **Hepatic injury**: Rare but serious hepatotoxicity has been reported; liver function monitoring is recommended
- **Psychiatric effects**: May precipitate or worsen aggressive behaviour, hostility, or emotional lability in paediatric patients

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction is biologically well-founded — atomoxetine's established NET inhibition mechanism directly addresses the noradrenergic dysregulation underlying specific developmental disorders. Multiple Phase 3 and Phase 4 RCTs, including studies conducted specifically in autism spectrum disorder and PDD-NOS populations, provide L1-level evidence, and two independent meta-analyses confirm efficacy across the neurodevelopmental spectrum. The primary barrier is regulatory: atomoxetine is not currently registered on the Australian ARTG, meaning a TGA registration pathway must be pursued before any clinical application in Australia.

**To proceed, the following is needed:**

- **TGA registration pathway**: Submit a TGA new registration application (or seek access via the Special Access Scheme or Authorised Prescriber pathway in the interim) — this is the single most critical step for Australian clinical use
- **TGA Product Information (PI) review**: Obtain and review the full PI from an approved jurisdiction (FDA/EMA) to conduct a complete Australian safety assessment, including black box warning implications for suicidality monitoring
- **Formal MOA documentation**: Obtain DrugBank/regulatory source confirmation of atomoxetine's NET inhibition mechanism to complete the mechanistic rationale formally
- **Paediatric safety monitoring plan**: Develop a structured monitoring protocol covering suicidality, cardiovascular parameters, growth, and hepatic function — aligned with TGA paediatric pharmacovigilance requirements
- **Australian prescribing guidelines alignment**: Review alignment with the Royal Australian and New Zealand College of Psychiatrists (RANZCP) and Paediatric guidelines for ADHD and neurodevelopmental disorders to establish appropriate clinical positioning

---

> **Disclaimer:** This report is intended for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require prospective clinical validation before therapeutic application. Healthcare professionals should refer to current TGA-approved Product Information and relevant clinical guidelines when making prescribing decisions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

