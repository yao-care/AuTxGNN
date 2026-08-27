---
layout: default
title: Probenecid
parent: 僅模型預測 (L5)
nav_order: 561
evidence_level: L5
indication_count: 10
---

# Probenecid
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

# Probenecid: From Uricosuric Therapy (Gout) to Renal Hypouricemia

## One-Sentence Summary

> Probenecid is a classic uricosuric agent, traditionally used to lower serum urate in gout/hyperuricemia by blocking renal urate reabsorption (URAT1). The TxGNN model predicts a possible link to **Renal Hypouricemia** (score 99.73%), but the supporting literature — **0 clinical trials** and **20 publications**, mostly describing probenecid used as a diagnostic challenge test rather than a treatment — points to an opposite-direction, likely spurious pharmacological signal. This candidate, and all 9 other candidates predicted for probenecid in this evidence pack, are flagged **Hold**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not supplied in this evidence pack (TFDA/TGA label data is a blocking data gap). Probenecid is generically known as a uricosuric agent for gout/hyperuricemia — general pharmacology knowledge, not a sourced regulatory indication |
| Predicted New Indication | Renal Hypouricemia (hypouricemia, renal) |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed in Australia |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for probenecid is not available in this evidence pack (data gap). Based on general pharmacology knowledge, probenecid inhibits URAT1-mediated urate reabsorption in the renal proximal tubule, which **increases** urinary urate excretion and **lowers** serum urate — the basis for its historic use in gout and hyperuricemia.

Renal hypouricemia is the opposite clinical state: an inherited or acquired defect (typically loss-of-function mutation in SLC22A12/URAT1) that causes **excessive** urate loss and **abnormally low** serum urate. Pharmacologically, probenecid would be expected to worsen, not treat, this condition — it is one of the agents historically used as a diagnostic urate-clearance challenge test in patients already suspected of having the disorder.

Reviewing the underlying literature confirms this: almost all cited papers are case reports or genetic/molecular studies describing renal hypouricemia as a disease entity, with probenecid appearing only as a diagnostic probe (alongside pyrazinamide) to characterise a patient's urate transport defect — not as a therapeutic intervention. This pattern is consistent with TxGNN generating the association through shared URAT1/urate-pathway biology in the knowledge graph, without capturing the direction of the pharmacological effect. The same caution applies to the other 9 ranked candidates for probenecid in this pack (Lesch-Nyhan syndrome, HGPRT deficiency, cholelithiasis, and a cluster of hepatobiliary conditions sharing an identical score of 96.59%, plus "disorder of phenylalanine metabolism," where the cited literature actually concerns the unrelated "probenecid test" for CSF dopamine turnover in Parkinson's disease research) — all are scored **Hold**, and several are explicitly noted as likely non-specific clustering or diagnostic-test confusion rather than genuine treatment signals.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Cohort (molecular analysis) | J Am Soc Nephrol | Genetic study of 32 renal hypouricemia patients establishing SLC22A12/URAT1 loss-of-function as the cause — describes disease mechanism, not probenecid treatment |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clin Rheumatol | Narrative review of hypouricemia aetiology for rheumatologists; no probenecid treatment data |
| [16678460](https://pubmed.ncbi.nlm.nih.gov/16678460/) | 2006 | Review/Case report | Mol Genet Metab | Overview of hereditary renal hypouricemia caused by SLC22A12 mutations |
| [7771493](https://pubmed.ncbi.nlm.nih.gov/7771493/) | 1995 | Case report/Review | Am J Kidney Dis | Exercise-induced acute renal failure in renal hypouricemia; discusses prevention, not probenecid therapy |
| [3813739](https://pubmed.ncbi.nlm.nih.gov/3813739/) | 1987 | Case report | Arch Intern Med | Diabetic patients with renal hypouricemia; probenecid used diagnostically to characterise the urate clearance defect |
| [14655203](https://pubmed.ncbi.nlm.nih.gov/14655203/) | 2003 | Case report | Am J Kidney Dis | Siblings with hereditary renal hypouricemia and exercise-induced acute renal failure |
| [1944743](https://pubmed.ncbi.nlm.nih.gov/1944743/) | 1991 | Case report | Nephron | Type 1 diabetics with renal hypouricemia; uricosuric mechanism study |
| [1656732](https://pubmed.ncbi.nlm.nih.gov/1656732/) | 1991 | Case report | Am J Kidney Dis | Cholangiocarcinoma-associated severe renal hypouricemia; probenecid/pyrazinamide used as diagnostic probes |
| [8341392](https://pubmed.ncbi.nlm.nih.gov/8341392/) | 1993 | Case report | Nephron | Novel renal hypouricemia subtype unresponsive to probenecid/pyrazinamide challenge |
| [7099326](https://pubmed.ncbi.nlm.nih.gov/7099326/) | 1982 | Case report | Nephron | Familial renal hypouricemia; urate excretion paradoxically **decreased** by probenecid (diagnostic test) |

Note: none of the above papers evaluate probenecid as a therapy for renal hypouricemia — it is used only as a diagnostic urate-clearance challenge agent.

## Australia Market Information

Probenecid is not currently registered on the ARTG (0 entries) and is not marketed in Australia.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Detailed warnings, contraindications, and drug interaction data are not available in this evidence pack (blocking data gap — TFDA label not yet sourced).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic direction is inverted — probenecid pharmacologically induces/worsens hypouricemia rather than treating it, and the cited literature describes probenecid only as a diagnostic challenge test in renal hypouricemia patients, not as a therapeutic agent. All 10 TxGNN-predicted indications for probenecid in this pack (including Lesch-Nyhan syndrome, HGPRT deficiency, and a cluster of hepatobiliary conditions sharing an identical score) carry the same Hold recommendation, several flagged as likely non-specific knowledge-graph clustering rather than genuine repurposing signals.

**To proceed, the following is needed:**
- TFDA/TGA-approved Product Information (warnings, contraindications, DDI) — currently a blocking gap
- Confirmed original indication and mechanism-of-action data for probenecid
- Independent pharmacological review of why TxGNN generated this and the other 9 candidate associations, before considering any further evaluation stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

