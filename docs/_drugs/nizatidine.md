---
layout: default
title: Nizatidine
parent: High Evidence (L1-L2)
nav_order: 509
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-13
description: "Nizatidine: predicted new indication Active peptic ulcer disease (evidence level L1). Approved use: Gastric ulcer, peptic ulcer disease…"
monitor_inn: "Nizatidine"
predicted_indications: ["duodenal obstruction", "gastroduodenitis", "multiple endocrine neoplasia", "leather-bottle stomach", "duodenitis", "gastrin secretion abnormality"]
---

# Nizatidine
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

## Nizatidine: From Gastric Ulcer and Peptic Ulcer Disease to Active Peptic Ulcer Disease
{: .text-alpha }

## One-Sentence Summary

Nizatidine is an H2-receptor antagonist originally used for gastric ulcer, duodenal ulcer, peptic ulcer disease and gastro-oesophageal reflux disease.
The TxGNN model predicts it may be effective for **active peptic ulcer disease**, but this is essentially an on-label use rather than true repurposing.
No clinical trials are registered in the data compiled for this report, but **20 publications** (including several randomised, placebo-controlled trials) support the indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastric ulcer, peptic ulcer disease, gastro-oesophageal reflux disease, oesophagitis, dyspepsia, duodenal ulcer (from knowledge graph indication data; no approved indication text is recorded for the ARTG entry) |
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, nizatidine is an H2-receptor antagonist. It blocks histamine-driven gastric acid secretion and reduces basal, nocturnal and stimulated acid output. Acid suppression is the core mechanism behind ulcer healing.

The predicted indication overlaps almost completely with nizatidine's established uses (gastric ulcer, duodenal ulcer, peptic ulcer disease). The prediction therefore reflects consistency with existing knowledge rather than a new therapeutic direction. The literature includes randomised, placebo-controlled, multicentre trials in active duodenal ulcer and benign gastric ulcer, as well as maintenance-therapy studies.

### Other Predicted Indications (for context)

The model also produced lower-ranked predictions. Their support is much weaker:

| Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|
| Duodenitis | 97.85% | L3 | Mechanistically sound (acid-peptic condition near duodenal ulcer), but evidence addresses ulcer disease rather than duodenitis; Proceed with Guardrails |
| Gastroduodenitis | 99.58% | L3 | Studies on NSAID-induced gastroduodenal lesions; study designs unclear; Research Question |
| Gastrojejunal ulcer | 99.94% | L4 | Indirect evidence extrapolated from peptic ulcer data; PPIs generally preferred; Research Question |
| Peptic ulcer perforation, duodenal obstruction, duodenogastric reflux, multiple endocrine neoplasia, leather-bottle stomach, gastrin secretion abnormality | 97.7–99.9% | L5 | No supporting clinical evidence, or no plausible mechanism; Hold |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Selected publications for active peptic ulcer disease (priority to randomised trials):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1526089](https://pubmed.ncbi.nlm.nih.gov/1526089/) | 1992 | RCT | Clin Pharmacol Ther | Eight-week, multicentre, double-blind comparison of nizatidine 150 mg twice daily and 300 mg at bedtime versus placebo in healing active benign gastric ulcer |
| [2570656](https://pubmed.ncbi.nlm.nih.gov/2570656/) | 1989 | RCT | Clin Pharmacol Ther | Two-phase, placebo-controlled trial of nizatidine 150 mg twice daily for duodenal ulcer healing and recurrence |
| [7960687](https://pubmed.ncbi.nlm.nih.gov/7960687/) | 1994 | RCT | Isr J Med Sci | Nizatidine 300 mg nightly versus placebo for 4 weeks in 55 patients with active duodenal ulcer; healing and mucosal inflammatory mediators assessed |
| [2892259](https://pubmed.ncbi.nlm.nih.gov/2892259/) | 1987 | RCT | Scand J Gastroenterol Suppl | One-year maintenance in 513 patients with healed duodenal ulcer; 12-month recurrence 34% with nizatidine versus 64% with placebo |
| [7863254](https://pubmed.ncbi.nlm.nih.gov/7863254/) | 1994 | Open clinical study | Scand J Gastroenterol Suppl | Maintenance nizatidine in healed duodenal ulcer, with quality-of-life assessment |
| [2905640](https://pubmed.ncbi.nlm.nih.gov/2905640/) | 1988 | Review | Drugs | Pharmacodynamic and pharmacokinetic properties and therapeutic use in peptic ulcer disease |
| [2184124](https://pubmed.ncbi.nlm.nih.gov/2184124/) | 1990 | Review | Gastroenterol Clin North Am | Overview of medical therapy of peptic ulcer disease; nizatidine is safe and effective but has no new properties of clinical importance |
| [2892253](https://pubmed.ncbi.nlm.nih.gov/2892253/) | 1987 | Safety summary | Scand J Gastroenterol Suppl | Safety assessment in about 3,800 nizatidine-treated individuals in US and European trials |
| [1355465](https://pubmed.ncbi.nlm.nih.gov/1355465/) | 1992 | Review | Gastroenterol Clin North Am | Control of gastric acid secretion by H2-receptor antagonists and H+/K+-ATPase inhibitors |
| [26883979](https://pubmed.ncbi.nlm.nih.gov/26883979/) | 2016 | Preclinical (rat) | Life Sci | Gastroprotective effects of several H2 antagonists on ibuprofen-induced gastric ulcer |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14306Y | Tazac | Capsule 150 mg (oral) | Not recorded in the data compiled for this report |

## Safety Considerations

- **Contraindication signals from the knowledge graph** (not label text): liver disease, gallbladder disease, impaired renal function, and gastric cancer/neoplasm (including diffuse gastric adenocarcinoma and linitis plastica). These should be checked against the TGA Product Information.
- **Drug interactions** (100 interactions recorded; examples shown):
  - Major: atazanavir, dasatinib
  - Moderate: acalabrutinib, bosutinib, brigatinib, cefditoren, cefpodoxime, cefuroxime, ceritinib, chlorpropamide, dabrafenib, dacomitinib
  - Minor: ketorolac, ibuprofen, diclofenac, alendronic acid, axitinib, cyanocobalamin, magnesium oxide, oxaprozin

  Many of the major and moderate interactions probably reflect reduced absorption of drugs that need an acidic gastric environment (for example some kinase inhibitors, atazanavir and some cephalosporins). This is an inference, not stated in the data.
- A published safety review reports that long-term low-dose H2-antagonist maintenance appears safe over several years (PMID 1679672).

Warnings and contraindications from the approved label were not available. Please refer to the TGA-approved Product Information (PI) for complete safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The top prediction is effectively an established, on-label use supported by several randomised, placebo-controlled trials. It is not a novel repurposing opportunity. The evidence is literature-based only; no registered trials were supplied, and most of the studies date from the 1980s and 1990s. Duodenitis is the only lower-ranked prediction with partially supportive evidence. The others are indirect or unsupported and should be held.

**To proceed, the following is needed:**
- The TGA-approved Product Information for Tazac, including approved indications, warnings and contraindications (the label review was a blocking data gap)
- Mechanism of action data from DrugBank
- Confirmation of the ARTG-approved indications against the predicted indication
- Comparison with current guidelines, as PPIs are generally preferred for many acid-related conditions
- A review of the interaction list, particularly for drugs that need gastric acid for absorption
- Direct evidence for duodenitis if that indication is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

