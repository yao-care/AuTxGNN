---
layout: default
title: Ranitidine
parent: High Evidence (L1-L2)
nav_order: 583
evidence_level: L1
indication_count: 10
---

# Ranitidine
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

Using the drug-repurposing report template supplied in the prompt (no additional skill applies — this is a direct data-to-markdown authoring task). Note: the evidence pack labels the local regulatory block `taiwan_regulatory`, but per the AuTxGNN project context this field carries Australian TGA/ARTG data — mapped accordingly below.

# Ranitidine: From Peptic Ulcer Disease to Active Peptic Ulcer Disease

## One-Sentence Summary

Ranitidine is a histamine H2-receptor antagonist historically used to treat peptic ulcer disease and other acid-related gastrointestinal conditions. The TxGNN model's top prediction is **Active Peptic Ulcer Disease**, supported by **1 clinical trial** and **19 publications** — but this signal largely reflects ranitidine's already-established, decades-old use rather than a genuinely novel indication, so it should be read as confirmatory rather than a new repurposing lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack — no ARTG licence text or original-indication data was returned (data gap, see below). Ranitidine is globally established as an H2-receptor antagonist for peptic ulcer disease and related acid-related conditions. |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in this evidence pack. Based on well-established pharmacology, ranitidine is a competitive histamine H2-receptor antagonist that reduces basal and stimulated gastric acid secretion — the same mechanism that underlies its long-standing historical use in peptic ulcer disease.

Because "active peptic ulcer disease" sits within ranitidine's own original indication family, the model's top-ranked prediction is not a genuine repositioning into a new disease area — it is closer to a re-confirmation of the drug's existing pharmacological role. The evidence pack itself flags this explicitly: *"與peptic ulcer disease同一機轉家族...為ranitidine歷史核准適應症之亞型描述，非新適應症"* (same mechanistic family as peptic ulcer disease; a sub-description of ranitidine's historically approved indication, not a new indication).

For pharmacists evaluating this candidate, the more informative repurposing signals in this evidence pack sit further down the ranked list — e.g. gastroduodenitis (rank 6, evidence level L2) and duodenogastric reflux (rank 4, evidence level L3) — where the mechanistic link is plausible but the direct trial evidence is thinner. These may warrant separate secondary review if a genuinely new indication is the goal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Phase 4 | Completed | 320 | Evaluated the effect of various PPIs (and statins) on clopidogrel antiplatelet activity in PCI patients on dual antiplatelet therapy. Relevance graded **C** — the study is focused on drug-interaction pharmacology, not direct treatment of peptic ulcer disease, and is only indirectly related to the ranitidine/ulcer link. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3909374](https://pubmed.ncbi.nlm.nih.gov/3909374/) | 1985 | RCT | Scand J Gastroenterol | Ranitidine 300 mg/day healed 91% of duodenal, 68% of prepyloric, and 81% of gastric corporeal ulcers at 4 weeks; maintenance therapy reduced relapse vs placebo over 1 year. |
| [6317325](https://pubmed.ncbi.nlm.nih.gov/6317325/) | 1983 | Review | Drug Intell Clin Pharm | Early review confirming ranitidine's approval for active duodenal ulcer and gastric hypersecretory conditions; 4–10× more potent than cimetidine on a molar basis. |
| [1976583](https://pubmed.ncbi.nlm.nih.gov/1976583/) | 1990 | Review | Hepato-gastroenterology | Reviews acid suppression as central to peptic ulcer healing; positions H2-antagonists (including ranitidine) within the broader acid-suppression treatment paradigm. |
| [2491360](https://pubmed.ncbi.nlm.nih.gov/2491360/) | 1989 | RCT | J Gastroenterol Hepatol | Randomized double-blind trial (n=270) comparing omeprazole 10/20 mg vs ranitidine 150 mg bid for duodenal ulcer healing and relapse, with weekly endoscopic assessment. |
| [2877570](https://pubmed.ncbi.nlm.nih.gov/2877570/) | 1986 | RCT | Am J Med | Multicentre, double-blind, randomized international study (n=1,031) comparing famotidine vs ranitidine for healing active duodenal ulcer. |
| [1863945](https://pubmed.ncbi.nlm.nih.gov/1863945/) | 1991 | RCT | Clin Ther | Compared famotidine 40 mg vs ranitidine 300 mg nightly for active duodenal ulcer healing (n=160) and 6-month maintenance, including NSAID/aspirin-related ulcers. |
| [3104657](https://pubmed.ncbi.nlm.nih.gov/3104657/) | 1986 | RCT | Klin Wochenschr | Compared nocturnal rioprostil (prostaglandin E1 analogue) vs ranitidine for duodenal ulcer healing. |
| [6317740](https://pubmed.ncbi.nlm.nih.gov/6317740/) | 1983 | Review | J Clin Gastroenterol | Comparative pharmacodynamics/pharmacokinetics of cimetidine and ranitidine; ranitidine 6–8× more potent at reducing gastric acid output. |
| [7863241](https://pubmed.ncbi.nlm.nih.gov/7863241/) | 1994 | Review | Scand J Gastroenterol Suppl | Reviews treatment strategies for symptom resolution, healing and H. pylori eradication in duodenal ulcer patients. |
| [12751338](https://pubmed.ncbi.nlm.nih.gov/12751338/) | 2003 | Study | Sao Paulo Med J | Evaluated ranitidine bismuth citrate + clarithromycin (7 days) for H. pylori eradication in Brazilian peptic ulcer patients. |

---

## Australia Market Information

Ranitidine currently has **0 ARTG entries** and is **not marketed** in Australia per this evidence pack — no product licence records were returned, so no ARTG table can be populated.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (active peptic ulcer disease) overlaps with ranitidine's own historical indication rather than representing a novel therapeutic use, and the product is currently not marketed in Australia (0 ARTG entries). Combined with a blocking data gap on regulatory PI warnings/contraindications, this candidate cannot yet proceed to safety screening.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications) — currently a blocking data gap (DG001)
- Detailed mechanism-of-action documentation (DrugBank) — currently a high-severity data gap (DG002)
- Clarification of whether "active peptic ulcer disease" should be treated as a genuine repurposing candidate or excluded as overlapping with ranitidine's existing use
- If pursuing repurposing rather than re-confirmation, consider prioritising lower-ranked but mechanistically distinct candidates from this pack (e.g. gastroduodenitis, L2; duodenogastric reflux, L3) for separate evaluation
- Confirmation of current Australian market/import status, given the "not marketed" flag and zero ARTG entries
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

