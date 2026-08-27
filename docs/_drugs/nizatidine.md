---
layout: default
title: Nizatidine
parent: 僅模型預測 (L5)
nav_order: 475
evidence_level: L5
indication_count: 10
---

# Nizatidine
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

# Nizatidine: From Unregistered H2-Receptor Antagonist to Active Peptic Ulcer Disease

## One-Sentence Summary

Nizatidine is a histamine H2-receptor antagonist that has no current Australian (TGA/ARTG) registration record in this dataset — it is not marketed locally.
The TxGNN model predicts it may be effective for **Active Peptic Ulcer Disease**, a use that is mechanistically consistent with its known drug class,
with **0 clinical trials** and **19 publications** currently identified in the evidence base.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established — no ARTG licence record exists for Nizatidine in this dataset (drug not marketed in Australia) |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available from the structured drug record (original MOA field: data gap). However, the repurposing rationale attached to this prediction supplies the pharmacological basis directly: **Nizatidine is a histamine H2-receptor antagonist that directly inhibits histamine-stimulated gastric acid secretion, promoting ulcer healing** — described as a core pharmacological action of the drug, not an inferential association.

Because no original approved indication is on record for Nizatidine in Australia, there is no local precedent to compare against. Mechanistically, however, acid suppression via H2-receptor blockade is the well-established therapeutic basis for treating active peptic ulcer disease as a drug class effect — this is not a novel biological hypothesis but a restatement of nizatidine's known primary pharmacology.

This is therefore less a case of cross-indication repurposing and more a case of the model correctly identifying the drug's core, class-defining use — which is reflected in the strength and consistency of the supporting literature below.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1526089](https://pubmed.ncbi.nlm.nih.gov/1526089/) | 1992 | RCT | Clin Pharmacol Ther | 8-week multicentre RCT: nizatidine 150 mg BID or 300 mg nocte vs placebo in healing active benign gastric ulcer |
| [2892259](https://pubmed.ncbi.nlm.nih.gov/2892259/) | 1987 | RCT | Scand J Gastroenterol Suppl | 1-year maintenance RCT (n=513): duodenal ulcer recurrence 34% (nizatidine) vs 64% (placebo) at 12 months |
| [1982108](https://pubmed.ncbi.nlm.nih.gov/1982108/) | 1990 | RCT | Hepato-gastroenterology | 8-week RCT comparing nizatidine (150 mg BID or 300 mg nocte) with ranitidine in gastric ulcer; comparable healing rates |
| [2570656](https://pubmed.ncbi.nlm.nih.gov/2570656/) | 1989 | RCT | Clin Pharmacol Ther | Two-phase, placebo-controlled, double-blind multicentre RCT: nizatidine 150 mg BID for duodenal ulcer healing |
| [7960687](https://pubmed.ncbi.nlm.nih.gov/7960687/) | 1994 | RCT | Isr J Med Sci | Double-blind, randomised, placebo-controlled trial of nizatidine 300 mg on duodenal ulcer healing and mucosal inflammatory mediators |
| [15683433](https://pubmed.ncbi.nlm.nih.gov/15683433/) | 2005 | RCT | J Gastroenterol Hepatol | Multicentre randomised controlled study comparing nizatidine and famotidine for maintenance therapy of erosive esophagitis |
| [1344473](https://pubmed.ncbi.nlm.nih.gov/1344473/) | 1992 | RCT | Med Pregl | Prospective, randomised, double-blind, multicentric comparison of nizatidine vs ranitidine in duodenal ulcer treatment |
| [8103616](https://pubmed.ncbi.nlm.nih.gov/8103616/) | 1993 | RCT | Acta Gastroenterol Belg | Prospective randomised study of H2 blockers (including nizatidine) and omeprazole on peptic secretion in duodenal ulcer |
| [2905640](https://pubmed.ncbi.nlm.nih.gov/2905640/) | 1988 | Review | Drugs | Review of nizatidine's pharmacodynamic/pharmacokinetic properties and therapeutic use in peptic ulcer disease |
| [2184124](https://pubmed.ncbi.nlm.nih.gov/2184124/) | 1990 | Review | Gastroenterol Clin North Am | Overview of medical therapy for peptic ulcer disease, including newer H2-receptor antagonists such as nizatidine |

---

## Australia Market Information

Nizatidine has no ARTG entries on record — it is not currently marketed in Australia.

---

## Safety Considerations

Nizatidine is not currently marketed in Australia, so no TGA-approved Product Information exists locally to draw from. No key warnings, contraindications, or drug interaction data were found in this evidence pack (DDI search returned no results). Prescribers considering access via an alternative pathway (e.g. Special Access Scheme) should consult an overseas-approved Product Information for full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The literature base is strong and consistent — eight randomised controlled trials support nizatidine's efficacy in active peptic ulcer disease, and the mechanism (H2-receptor blockade suppressing gastric acid secretion) is well-established, not speculative. However, nizatidine has no current ARTG registration in Australia, which is a material access barrier independent of the clinical evidence strength.

**To proceed, the following is needed:**
- TGA-approved Product Information — warnings, precautions and contraindications are currently unavailable (Blocking data gap)
- Confirmation of detailed mechanism-of-action data via DrugBank (High-priority data gap)
- Clarification of regulatory pathway, since Nizatidine currently has zero ARTG entries — TGA registration or Special Access Scheme approval would be required before local clinical use
- Route-of-administration compatibility assessment (currently unassessed/pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

