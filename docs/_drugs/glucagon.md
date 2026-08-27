---
layout: default
title: Glucagon
parent: 僅模型預測 (L5)
nav_order: 316
evidence_level: L5
indication_count: 10
---

# Glucagon
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

# Glucagon: From Hypoglycaemia Management to Irritable Bowel Syndrome

## One-Sentence Summary

Glucagon (DrugBank DB00040) is a pancreatic-derived peptide hormone conventionally used to treat severe hypoglycaemia and, in diagnostic settings, to suppress gastrointestinal motility (e.g. before endoscopy/imaging). The TxGNN model predicts it may be effective for **Irritable Bowel Syndrome (IBS)**, with **11 clinical trials** and **20 publications** identified — though most of this evidence base actually concerns GLP‑1 receptor agonists rather than glucagon itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Severe hypoglycaemia / diagnostic GI motility suppression (general clinical use; not marketed in Australia — no ARTG record available) |
| Predicted New Indication | Irritable Bowel Syndrome |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L3 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for glucagon is not available in this evidence pack. Based on known pharmacology, glucagon activates the glucagon receptor (GCGR), producing a well-recognised clinical effect of relaxing gastrointestinal smooth muscle — the basis for its long-standing off-label diagnostic use to reduce bowel motility before endoscopy and imaging.

The evidence surfaced for this candidate, however, is almost entirely about **GLP‑1 receptor agonists** (ROSE‑010, exendin‑4, liraglutide, dulaglutide, etc.), not glucagon. GLP‑1 and glucagon are both proglucagon-derived peptides but act on distinct receptors (GLP‑1R vs GCGR) with different downstream effects on gut motility and pain signalling. This is a genuine target mismatch: the TxGNN knowledge graph likely linked glucagon to IBS via shared "proglucagon family" nodes rather than via glucagon's own receptor pharmacology.

That said, the mismatch does not make the prediction implausible outright — glucagon's independently established effect of inhibiting GI smooth-muscle motility is mechanistically in the same direction as therapeutic goals in IBS (particularly diarrhoea-predominant or motility-driven subtypes). This gives a plausible, but indirect and currently unproven, rationale that would need dedicated glucagon-specific (not GLP‑1-analogue) evidence to confirm.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Phase 1/2 | Completed | 52 | ROSE-010 (a GLP-1 analogue, not glucagon) reduced gastric emptying delay and improved gastric accommodation without slowing colonic transit in constipation-predominant IBS (IBS-C) |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Phase 1 | Completed | 12 | Compared native GLP-1 with its analogue ROSE-010 on prandial gut motility inhibition; mechanistic, not a glucagon trial |
| [NCT00802971](https://clinicaltrials.gov/study/NCT00802971) | N/A | Completed | 12 | Studied idiopathic reactive hypoglycaemia prevalence and fructo-oligosaccharide effects on glucose variability; no direct IBS or glucagon treatment link |
| [NCT05249023](https://clinicaltrials.gov/study/NCT05249023) | N/A | Completed | 37 | Investigated butyrate's mechanism of action in the human colon, relevant to IBS pathophysiology but not a drug trial |
| [NCT04111263](https://clinicaltrials.gov/study/NCT04111263) | N/A | Completed | 33 | Tested a gut-microbiota-targeted nutritional intervention for GI barrier integrity; unrelated to glucagon |
| [NCT06408610](https://clinicaltrials.gov/study/NCT06408610) | N/A | Completed | 66 | Compared exercise intensity effects on gut dysbiosis and GLP-1 hormone levels in pre-diabetic, obese IBS patients |
| [NCT03256266](https://clinicaltrials.gov/study/NCT03256266) | N/A | Active, not recruiting | 375 | Establishing small intestinal organoids to test nutrient antigens/therapeutic agents; general platform study |
| [NCT06333717](https://clinicaltrials.gov/study/NCT06333717) | N/A | Completed | 33 | Examined whole-grain rye bread's effect on the gut-microbiota-brain axis in healthy subjects |
| [NCT04230655](https://clinicaltrials.gov/study/NCT04230655) | N/A | Unknown | 110 | Low-energy diet ± intragastric balloon for obesity; not IBS/glucagon-specific |
| [NCT06113146](https://clinicaltrials.gov/study/NCT06113146) | N/A | Completed | 41 | Assessed eating rate of ultra-processed foods on dietary intake and metabolic response |

**None of the identified trials tested glucagon itself in IBS.** The most relevant trials (NCT01056107, NCT02731664) involve ROSE-010, a GLP‑1 analogue with a different receptor target.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | RCT | Scandinavian Journal of Gastroenterology | ROSE-010 (GLP-1RA) reduced pain intensity during IBS attacks; cross-analysis identified subpopulations most likely to respond |
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Review | Frontiers in Endocrinology | Systematic review/meta-analysis: GLP-1 receptor agonists and ROSE-010 inhibit the migrating motor complex and reduce GI motility in IBS |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Review | Experimental Physiology | Reviews the role of L-cell-derived GLP-1 in IBS pathophysiology, including stress, microbiota and bile-acid changes |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Review | Advances in Experimental Medicine and Biology | Discusses aerosolised GLP-1 delivery for diabetes and its potential relevance to IBS |
| [21694813](https://pubmed.ncbi.nlm.nih.gov/21694813/) | 2011 | Review | Therapeutic Advances in Gastroenterology | Broad review of IBS treatments beyond fibre/antispasmodics (antidepressants, 5-HT agents, prosecretory agents) |
| [26765585](https://pubmed.ncbi.nlm.nih.gov/26765585/) | 2016 | Review | Expert Opinion on Investigational Drugs | Reviews novel investigational drugs for IBS-C, including incretin-pathway candidates |
| [28215540](https://pubmed.ncbi.nlm.nih.gov/28215540/) | 2017 | Observational | Clinics and Research in Hepatology and Gastroenterology | Found decreased serum GLP-1 correlates with abdominal pain in IBS-C patients; colonic GLP-1 receptor expression measured |
| [31602785](https://pubmed.ncbi.nlm.nih.gov/31602785/) | 2020 | Preclinical (animal) | Neurogastroenterology and Motility | Exendin-4 (GLP-1RA) ameliorated GI dysfunction in a rat model of IBS |
| [31311066](https://pubmed.ncbi.nlm.nih.gov/31311066/) | 2019 | Preclinical (animal) | Neurogastroenterology and Motility | Ghrelin sensitised colonic neurons to exendin-4 (GLP-1RA), relevant to postprandial IBS symptoms |
| [24605036](https://pubmed.ncbi.nlm.nih.gov/24605036/) | 2014 | Observational | World Journal of Gastroenterology | Characterised ileal endocrine cell types (including GLP-1-producing L-cells) in IBS patients |

**All identified literature concerns GLP-1 receptor agonists or endogenous GLP-1 biology — none directly studies glucagon in IBS.**

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. This evidence pack contains no TGA warnings, contraindications, or drug-interaction data for glucagon (a blocking data gap — see Next Steps).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The evidentiary basis for the top-ranked prediction (IBS) is built almost entirely on GLP‑1 receptor agonists — a different molecular target from glucagon's own receptor (GCGR) — so it cannot be directly extrapolated to glucagon.
- TGA safety information (warnings/contraindications) is completely unavailable, which is a blocking gap for any safety pre-assessment.
- Glucagon is currently not marketed in Australia (no ARTG entries), adding a regulatory barrier independent of the scientific question.

**To proceed, the following is needed:**
- TGA-approved Product Information for glucagon (warnings, contraindications, drug interactions) to close the blocking safety data gap
- Glucagon-specific (not GLP-1-analogue) mechanistic or preclinical evidence testing GCGR agonism in IBS models
- Clarification of whether the TxGNN knowledge-graph link reflects a genuine shared pathway or a proglucagon-family artefact
- Assessment of the Australian regulatory pathway, since glucagon has no current ARTG listing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

