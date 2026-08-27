---
layout: default
title: Mianserin
parent: 僅模型預測 (L5)
nav_order: 442
evidence_level: L5
indication_count: 10
---

# Mianserin
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

# Mianserin: From Antidepressant Use to Melancholia (Depressive Subtype)

## One-Sentence Summary

> Mianserin is a tetracyclic antidepressant; the drug's original registered indication and detailed mechanism of action are not captured in the source data (data gap), but literature within this evidence pack confirms it as an established α2-adrenergic antagonist antidepressant.
> Among the TxGNN model's top-10 predictions, most (including the single highest-scoring candidate, benign paroxysmal torticollis of infancy, and four rare genetic syndromes) are flagged by the evidence pack itself as likely knowledge-graph noise with no supporting evidence.
> The strongest-supported candidate is **Melancholia**, a depressive subtype, backed by **direct mianserin randomised controlled trials** (L2 evidence) — though this represents confirmation of mianserin's known antidepressant activity rather than a genuinely novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in source data (data gap); literature in this evidence pack identifies mianserin as a tetracyclic antidepressant for depression |
| Predicted New Indication | Melancholia (depressive subtype) |
| TxGNN Prediction Score | 99.17% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

**Important caveat on ranking:** TxGNN's single highest-scoring prediction (benign paroxysmal torticollis of infancy, 99.49%) and four rare genetic-syndrome predictions (Ohdo syndrome and variants, blepharophimosis–intellectual disability syndrome, Keppen-Lubinsky syndrome, ligneous conjunctivitis) all returned **zero clinical trials and zero literature**. The evidence pack's own rationale explicitly labels these as having "no plausible mechanistic link" and likely reflecting knowledge-graph noise rather than a real pharmacological hypothesis. This report therefore leads with the best-evidenced candidate (melancholia) rather than the raw top-ranked score.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for mianserin was not available from the primary drug record (data gap DG002). However, literature captured in this evidence pack consistently describes mianserin as a **tetracyclic antidepressant** that acts as a presynaptic α2-adrenergic receptor antagonist, increasing central noradrenaline and serotonin release — the same mechanistic class discussed for its close analogue, mirtazapine.

The original indication field for this drug is also empty in the source data. Based on the literature retrieved (e.g. PMID 6346303, "Efficacy and side effects of mianserin, a tetracyclic antidepressant"; PMID 7048075, a mianserin pharmacology monograph), mianserin's established clinical use is as an antidepressant. Melancholia is a recognised subtype of depressive illness, so a prediction linking mianserin to melancholia sits squarely within its known pharmacological class rather than representing a mechanistically distant "new" indication.

This has a direct implication for interpretation: unlike a true repurposing case (e.g. an oncology drug predicted for a cardiovascular indication), this candidate is best understood as **confirmatory evidence of an existing therapeutic domain**, not discovery of a novel use. The genuinely novel high-score predictions in this dataset (rare paediatric and genetic syndromes) carry no mechanistic or evidentiary support at all.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for melancholia (or for any of the other nine predicted indications in this dataset — all clinical trial and ICTRP searches returned zero results).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8773291](https://pubmed.ncbi.nlm.nih.gov/8773291/) | 1995 | RCT | Pharmacopsychiatry | Controlled study of 51 depressive inpatients; mianserin vs amitriptyline showed no significant difference in HAMD outcome, similar tolerability |
| [2864794](https://pubmed.ncbi.nlm.nih.gov/2864794/) | 1985 | RCT | Acta Psychiatr Scand Suppl | Double-blind multicentre trial in 61 depressive patients; mianserin vs nomifensine, no significant differences at baseline or outcome |
| [11294041](https://pubmed.ncbi.nlm.nih.gov/11294041/) | 2001 | RCT | L'Encéphale | Multicentre double-blind trial in geriatric patients (≥60y) with major depression; paroxetine vs mianserin, comparable efficacy and safety |
| [6371875](https://pubmed.ncbi.nlm.nih.gov/6371875/) | 1984 | RCT | Psychopathology | Double-blind, non-crossover trial in 125 general-practice depression patients; trazodone vs mianserin, higher withdrawal rate on mianserin |
| [8249653](https://pubmed.ncbi.nlm.nih.gov/8249653/) | 1993 | RCT | Acta Psychiatr Scand | Double-blind, placebo-controlled crossover study of mianserin in chronic pain with and without depression |
| [27289172](https://pubmed.ncbi.nlm.nih.gov/27289172/) | 2016 | Meta-analysis | Lancet | Network meta-analysis comparing antidepressants (including mianserin's class) for major depressive disorder in children/adolescents |
| [7048075](https://pubmed.ncbi.nlm.nih.gov/7048075/) | 1982 | Review | Mod Probl Pharmacopsychiatry | Mianserin pharmacology and clinical monograph |
| [6346303](https://pubmed.ncbi.nlm.nih.gov/6346303/) | 1983 | Review | Postgrad Med J | Efficacy and side-effect profile of mianserin as a tetracyclic antidepressant |
| [40616802](https://pubmed.ncbi.nlm.nih.gov/40616802/) | 2025 | Review | Prilozi | Discusses α2-autoreceptor/heteroreceptor antagonists (mianserin, trazodone, mirtazapine) in combination antidepressant therapy |
| [3068469](https://pubmed.ncbi.nlm.nih.gov/3068469/) | 1988 | Review | Medicina (Firenze) | General review of mianserin |

---

## Australia Market Information

Mianserin is **not currently registered on the ARTG** (Australian Register of Therapeutic Goods) — 0 entries found. No product, dosage form, or approved-indication information is available for the Australian market.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No TFDA/TGA warnings, contraindications, or drug interaction data were retrievable for this drug in the current evidence pack (flagged as a **Blocking** data gap, DG001) — this must be resolved before any S1 safety review can proceed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Direct mianserin RCT evidence (L2) supports antidepressant efficacy in melancholia-type depression, but this reflects the drug's known pharmacological class rather than a novel repurposing opportunity, and the drug has no current Australian market presence or safety documentation.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/TGA product information for warnings, contraindications, and interactions
- Resolve DG002: confirm mechanism of action and original approved indication via DrugBank/regulatory source
- Clarify regulatory strategy given 0 ARTG entries — no existing Australian registration to build on
- Independently verify whether "melancholia" offers distinct clinical/regulatory value over mianserin's already-established antidepressant use, given the overlap noted above
- Given the top TxGNN-scored candidates (rare paediatric/genetic syndromes) show no mechanistic or evidentiary support, deprioritise or discard these from further development pending stronger signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

