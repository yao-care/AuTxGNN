---
layout: default
title: Potassium Citrate
parent: 僅模型預測 (L5)
nav_order: 547
evidence_level: L5
indication_count: 10
---

# Potassium Citrate
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

# Potassium Citrate: From Established Urinary Alkalinisation Use to Nephrolithiasis

## One-Sentence Summary

Potassium citrate is a well-known urinary alkaliniser/citrate supplement; the evidence pack's highest-scoring TxGNN prediction (familial visceral myopathy, 99.95%) has **zero supporting evidence** and is flagged as likely model noise. The strongest, actionable signal in this bundle is **nephrolithiasis**, with **35 clinical trials** and **19 publications** identified — though this largely confirms an *existing* established use of the drug rather than a genuinely novel indication.

> Note: This evidence pack bundles 10 TxGNN-predicted indications for potassium citrate. Nine of them (familial visceral myopathy, mitochondrial OXPHOS disorder, Pendred syndrome, cystinosis, hypermanganesemia with dystonia, SLC26A1-related nephrolithiasis susceptibility, nonsyndromic deafness, exocrine pancreatic insufficiency, leukocyte adhesion deficiency) have Evidence Level L4–L5 with "Hold" or "Research Question" status and no or minimal direct evidence. This report focuses on the one candidate with substantive evidence and an actionable recommendation — **nephrolithiasis**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (`original_indications` empty, MOA data gap). Potassium citrate is generically known as a urinary alkaliniser/citrate/potassium supplement. |
| Predicted New Indication | Nephrolithiasis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on known pharmacology, potassium citrate is a citrate/alkalinising salt: its established effect is to raise urinary pH and increase urinary citrate excretion, which chelates calcium and inhibits calcium oxalate/calcium phosphate crystal formation, and also raises urinary pH to help dissolve uric acid stones.

This is a textbook-level mechanism that maps directly onto nephrolithiasis (particularly calcium and uric acid stone prevention/treatment). Unlike a typical TxGNN repurposing hypothesis, the rationale text in this evidence pack notes that **this indication is essentially an existing standard clinical use of the drug rather than a novel prediction** — the model has effectively re-identified a well-established therapeutic role.

Two related but weaker hypotheses appear in the same bundle: **cystinosis** (L4, Research Question) — plausible because nephropathic cystinosis often causes proximal tubular Fanconi syndrome with bicarbonate/citrate wasting, but no trial has tested potassium citrate in this population directly — and **exocrine pancreatic insufficiency** (L4, Research Question) — supported only by a single case report of citrate treating secondary oxalate nephropathy. Both would need dedicated hypothesis-generation work before further evaluation.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01217372](https://clinicaltrials.gov/study/NCT01217372) | Phase 2 | Completed | 203 | LIMONE study — open-label, blinded-endpoint RCT testing citrate/lemon-juice supplementation to prevent recurrence of calcium oxalate nephrolithiasis |
| [NCT06966635](https://clinicaltrials.gov/study/NCT06966635) | Phase 4 | Recruiting | 312 | Sustained-release potassium citrate vs sodium bicarbonate vs control for gout, evaluating alkalinisation effects on uric acid lowering and urinary calculi prevention |
| [NCT05365477](https://clinicaltrials.gov/study/NCT05365477) | Phase 4 | Completed | 56 | Randomised trial of empiric vs selective (metabolic-workup-guided) diet-plus-pharmacologic prevention strategies in high-risk stone formers |
| [NCT00004284](https://clinicaltrials.gov/study/NCT00004284) | Phase 3 | Completed | 300 | Double-blind RCT comparing slow-release potassium phosphate vs potassium citrate for absorptive hypercalciuria and stone recurrence prevention |
| [NCT01754779](https://clinicaltrials.gov/study/NCT01754779) | Phase 2 | Completed | 13 | Evaluated whether citric acid or potassium citrate reduces calcium phosphate saturation in urine of calcium phosphate stone formers |
| [NCT01980004](https://clinicaltrials.gov/study/NCT01980004) | Phase 2 | Withdrawn | 0 | Designed to compare potassium citrate + dietary education vs dietary education alone for calcium phosphate stone recurrence; trial withdrawn, no data |
| [NCT06819553](https://clinicaltrials.gov/study/NCT06819553) | Phase 2/3 | Active, not recruiting | 48 | RCT evaluating oral potassium citrate for reducing ureteral stent encrustation after ureteroscopy for uric acid stones |
| [NCT01329042](https://clinicaltrials.gov/study/NCT01329042) | Phase 4 | Completed | 80 | Evaluated potassium sodium citrate for preventing stone recurrence/residual fragment growth after shockwave lithotripsy and PCNL in calcium oxalate urolithiasis |
| [NCT03258190](https://clinicaltrials.gov/study/NCT03258190) | Phase 2 | Completed | 137 | Lime powder regimen (citrate/citric acid + potassium) tested against standard therapy for urinary metabolic abnormalities and urolithiasis recurrence |
| [NCT00120731](https://clinicaltrials.gov/study/NCT00120731) | N/A | Withdrawn | 0 | Planned study of urinary chemistry and acid-base effects of potassium citrate in children with idiopathic hypercalciuria and urolithiasis; withdrawn |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27915395](https://pubmed.ncbi.nlm.nih.gov/27915395/) | 2017 | Systematic review/meta-analysis | Urolithiasis | Meta-analysis of RCTs on potassium citrate supplementation for preventing stone recurrence before/after shockwave lithotripsy |
| [39206631](https://pubmed.ncbi.nlm.nih.gov/39206631/) | 2024 | Phase II study | Urologia | Oral potassium citrate + magnesium + probiotics reduced crystalluria in stone formers |
| [40978115](https://pubmed.ncbi.nlm.nih.gov/40978115/) | 2025 | Review | Clinical Kidney Journal | Comprehensive update on citrate biology, renal handling, and clinical use in calcium stone disease |
| [33417997](https://pubmed.ncbi.nlm.nih.gov/33417997/) | 2021 | Preclinical (animal model) | Kidney International | Chlorthalidone + potassium citrate reduced calcium oxalate stones and improved bone quality in genetic hypercalciuric rats |
| [30531474](https://pubmed.ncbi.nlm.nih.gov/30531474/) | 2019 | Review | Curr Opin Nephrol Hypertens | Reviews role of citrate therapy specifically in calcium phosphate stone disease |
| [3306318](https://pubmed.ncbi.nlm.nih.gov/3306318/) | 1987 | Review | Miner Electrolyte Metab | Classic paper establishing potassium citrate's role in renal tubular acidosis with calcium stones, hypocitraturic calcium oxalate nephrolithiasis, and uric acid lithiasis |
| [26150027](https://pubmed.ncbi.nlm.nih.gov/26150027/) | 2015 | Review | Arch Ital Urol Androl | CLU Working Group review of dietary/citrate interventions for urinary stone risk factors |
| [40583613](https://pubmed.ncbi.nlm.nih.gov/40583613/) | 2025 | Guideline/Review | Arch Ital Urol Androl | Expert consensus (ESD 2025) on management of urinary stones, including citrate-based prevention |
| [38583757](https://pubmed.ncbi.nlm.nih.gov/38583757/) | 2024 | Cohort | Am J Kidney Dis | Evaluated independent associations between 24-hour urinary chemistries (including citrate) and kidney stone risk |
| [16443041](https://pubmed.ncbi.nlm.nih.gov/16443041/) | 2006 | Review | Lancet | General overview of kidney stone pathophysiology and medical management, including citrate therapy |

## Australia Market Information

Potassium citrate currently has **no ARTG entries** in Australia (market status: not marketed, 0 licenses recorded). No approved local product information is available at this time.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No key warnings, contraindications, or drug interaction data were returned in this evidence pack (DDI query: not found).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Nephrolithiasis is supported by L1-grade evidence (multiple completed Phase 2–4 RCTs, including a Phase 3 comparator trial and a published meta-analysis), and the mechanism is well-established rather than speculative — potassium citrate is already a recognised therapy for calcium and uric acid stone prevention internationally. However, it is currently unregistered in Australia (0 ARTG entries) and safety/MOA documentation is a blocking data gap.

**To proceed, the following is needed:**
- TGA Product Information / label data (currently a Blocking data gap — no ARTG entry to source it from)
- Formal mechanism-of-action documentation (High-severity data gap)
- A regulatory pathway assessment for ARTG registration, since the drug is not currently marketed in Australia
- If pursuing the secondary hypotheses (cystinosis, exocrine pancreatic insufficiency), dedicated clinical evidence generation, as current support is limited to case reports/mechanistic inference only
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

