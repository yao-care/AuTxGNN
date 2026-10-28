---
layout: default
title: Diazepam
parent: Model Prediction Only (L5)
nav_order: 212
evidence_level: L5
indication_count: 10
monitor_inn: "Diazepam"
predicted_indications: ["insomnia (disease)", "cauda equina syndrome", "sleep disorder, initiating and maintaining sleep", "attention deficit hyperactivity disorder, inattentive type", "antidepressant type abuse", "hallucinogen abuse", "barbiturate abuse", "specific developmental disorder", "attention deficit-hyperactivity disorder", "obsolete neurogenic bladder (disease)"]
last_modified_at: 2026-10-28
description: "Diazepam: predicted new indication insomnia (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Diazepam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Diazepam: Benzodiazepine (GABA-A positive allosteric modulator) → insomnia (disease)
{: .text-alpha }

## One-Sentence Summary

Diazepam is a benzodiazepine that enhances GABA-A receptor signalling.
The TxGNN model predicts it may be useful for **insomnia (disease)**.
The data compiled for this report contain **no registered clinical trials** and **18 publications**, none of which is a diazepam-specific trial for this condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | insomnia (disease) |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Based on general pharmacology, diazepam is a positive allosteric modulator of GABA-A receptors. It enhances inhibitory neurotransmission and produces sedative-hypnotic effects, which is a plausible basis for use in insomnia. Benzodiazepines as a class are used for short-term insomnia.

The supporting evidence is indirect. The retrieved publications are mostly reviews, herbal medicine and animal studies, pharmacokinetic papers, and discussions of dependence and deprescribing. Diazepam appears mainly as a comparator or a class example. The evidence level is therefore L5 rather than higher, because no cited study directly tests diazepam in insomnia in a way that supports the prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Selected publications from those retrieved (the full set is mostly indirect):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6113175](https://pubmed.ncbi.nlm.nih.gov/6113175/) | 1981 | Double-blind comparison | J Int Med Res | Lormetazepam 1 mg versus diazepam 5 mg over 7 days in 100 out-patients with sleep disorders; lormetazepam was significantly better for time to fall asleep and uninterrupted sleep duration |
| [39581171](https://pubmed.ncbi.nlm.nih.gov/39581171/) | 2024 | Review | Bioorg Chem | GABA-A modulators, including diazepam, in epilepsy, anxiety, insomnia and depression; notes sedation and other side effects |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opin Drug Metab Toxicol | Pharmacokinetics of anxiolytic drugs |
| [31770357](https://pubmed.ncbi.nlm.nih.gov/31770357/) | 2019 | Review | Med Lett Drugs Ther | Cannabis and cannabinoids |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Meta-analysis | Acta Pharm | Tranquilizer therapy in elderly patients with chronic non-communicable diseases |
| [40583063](https://pubmed.ncbi.nlm.nih.gov/40583063/) | 2025 | Cohort | Cell Mol Biol Lett | Long-term benzodiazepine and Z-drug use associated with increased breast cancer risk |
| [32623439](https://pubmed.ncbi.nlm.nih.gov/32623439/) | 2020 | Animal study | Med Sci Monit | Berberine in insomnia rats, with diazepam as a comparator |
| [29479317](https://pubmed.ncbi.nlm.nih.gov/29479317/) | 2018 | Systematic review | Front Pharmacol | Suanzaoren herbal formulae for insomnia (not diazepam) |

The remaining retrieved items cover herbal or food-based animal models, prescribing habits, discontinuation of chronic benzodiazepine use and unrelated topics.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2669L | Diazepam Elixir | Oral liquid 10 mg per 10 mL, 100 mL | Not recorded in the local data |

## Safety Considerations

- **Long-term use signal**: one cohort study (PMID 40583063) reported an association between prolonged benzodiazepine and Z-drug use and breast cancer risk. Other retrieved papers raise concerns about dependence, tolerance, cognitive effects, falls in older adults and altered sleep architecture with chronic use.
- **Drug interactions**: the interaction screen returned 100 entries. Examples include a Major interaction with morphine, and Moderate interactions with bupropion, aprepitant, omeprazole, esomeprazole, cimetidine, clarithromycin, cisapride, clotrimazole, miconazole, dronabinol and metoclopramide.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible and the model score is high, but no registered trial and no diazepam-specific study of insomnia support the prediction. The literature is largely indirect and emphasises dependence and long-term harms.

**To proceed, the following is needed:**
- Controlled trial data for diazepam in insomnia, compared with established hypnotics
- Detailed mechanism-of-action data
- Safety review for short-term versus long-term use, particularly in older adults
- Approved indication and safety text from the TGA Product Information for the registered Australian product
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

