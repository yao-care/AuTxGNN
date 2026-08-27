---
layout: default
title: Chloramphenicol
parent: 僅模型預測 (L5)
nav_order: 143
evidence_level: L5
indication_count: 10
---

# Chloramphenicol
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

# Chloramphenicol: From Broad-Spectrum Antibacterial Use to Conjunctivitis

## One-Sentence Summary

> Chloramphenicol is a long-established broad-spectrum antibacterial agent, historically used against serious bacterial infections such as typhoid fever, meningitis and bacterial conjunctivitis.
> The TxGNN model's top prediction is **Conjunctivitis**, supported by **19 publications** (no registered clinical trials found) —
> however, this signal largely confirms an **already-standard clinical use** (topical chloramphenicol eye drops) rather than representing a genuinely novel indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the evidence pack (0 licenses / no `original_indications` recorded). Chloramphenicol is a broad-spectrum antibacterial historically indicated for serious bacterial infections, including bacterial conjunctivitis, per literature in this pack (PMID 35369683). |
| Predicted New Indication | Conjunctivitis (bacterial) — note: represents an existing, standard clinical use rather than a novel repurposing signal |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L1 |
| Australia Market Status | Not currently marketed in Australia |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed, DrugBank-sourced mechanism of action data is currently unavailable (flagged as a High-severity data gap, DG002). Based on information available within this evidence pack, chloramphenicol is a bacteriostatic antibacterial that binds the bacterial 50S ribosomal subunit and blocks protein synthesis, giving it broad-spectrum activity against the organisms that commonly cause bacterial conjunctivitis (*Staphylococcus*, *Streptococcus*, *Haemophilus*, *Moraxella* species). Topical ophthalmic formulations penetrate corneal and conjunctival tissue well.

Unlike a typical drug-repurposing signal, conjunctivitis is not a mechanistically distant indication from chloramphenicol's established use — topical chloramphenicol eye drops have been standard first-line therapy for bacterial conjunctivitis for decades in several jurisdictions (notably the UK). The TxGNN hit therefore reflects a genuine, well-documented pharmacological relationship rather than a speculative new application. The main clinical question is not "does it work" but "what is the safety profile," given the historical (and still debated) association between topical ocular chloramphenicol and aplastic anaemia (PMID 8800624).

The nine lower-ranked predictions in this evidence pack (diffuse scleroderma, postinfectious vasculitis, post-bacterial disorder, post-infectious syndrome, infective urethral stricture, Chagas cardiomyopathy, infection-related HUS, punctate epithelial keratoconjunctivitis, chronic rhinosinusitis) were also screened. All were scored L3–L5 with a **Hold** recommendation — either no supporting literature/trials, mechanistically implausible pathogen targets (viral, protozoal or fibrotic disease processes unrelated to bacterial ribosomal inhibition), or in two cases (post-infectious syndrome, infection-related HUS) the "signal" actually reflects a **known harm** (chloramphenicol-associated aplastic anaemia; antibiotic-triggered toxin release risk in STEC-related HUS) rather than a treatment opportunity. These are not pursued further in this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for chloramphenicol in conjunctivitis (ClinicalTrials.gov and ICTRP searches both returned 0 results). Supporting evidence for this indication comes from published randomised trials predating, or outside the scope of, modern trial registries (see Literature Evidence below).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38511104](https://pubmed.ncbi.nlm.nih.gov/38511104/) | 2024 | RCT | Curr Ther Res Clin Exp | Compared moxifloxacin and chloramphenicol for bacterial eye infections including conjunctivitis; chloramphenicol remains a relevant comparator despite known toxicity profile. |
| [17947266](https://pubmed.ncbi.nlm.nih.gov/17947266/) | 2007 | RCT | Br J Ophthalmol | Randomised equivalency trial: 2.5% povidone-iodine vs ophthalmic chloramphenicol for preventing neonatal conjunctivitis in a trachoma-endemic area. |
| [11952486](https://pubmed.ncbi.nlm.nih.gov/11952486/) | 2002 | RCT | Acta Ophthalmol Scand | Fucidic acid vs chloramphenicol eye drops in acute neonatal bacterial conjunctivitis; comparable clinical/bacteriological outcomes. |
| [8333258](https://pubmed.ncbi.nlm.nih.gov/8333258/) | 1993 | RCT | Acta Ophthalmol | Fusidic acid viscous eye drops vs chloramphenicol in acute conjunctivitis; no major difference in bacteriological or clinical response. |
| [3554881](https://pubmed.ncbi.nlm.nih.gov/3554881/) | 1987 | RCT | Acta Ophthalmol | Fusidic acid vs chloramphenicol viscous eye drops; clinical success 84% vs 81%, more mild side effects (stinging) with chloramphenicol. |
| [3300139](https://pubmed.ncbi.nlm.nih.gov/3300139/) | 1987 | RCT | Acta Ophthalmol | Fusidic acid superior to chloramphenicol and framycetin eye drops for bacterial conjunctivitis (93% vs 48% vs 74% success). |
| [6188739](https://pubmed.ncbi.nlm.nih.gov/6188739/) | 1983 | RCT (multicentre) | J Antimicrob Chemother | Trimethoprim-polymyxin B vs neomycin-polymyxin B-gramicidin vs chloramphenicol for presumptive bacterial conjunctivitis; all preparations effective with few adverse effects. |
| [32959365](https://pubmed.ncbi.nlm.nih.gov/32959365/) | 2020 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Interventions for preventing ophthalmia neonatorum, including topical chloramphenicol/antibiotic prophylaxis strategies. |
| [16378567](https://pubmed.ncbi.nlm.nih.gov/16378567/) | 2005 | Systematic Review / Meta-analysis | Br J Gen Pract | Cochrane update on topical antibiotics (including chloramphenicol) for acute bacterial conjunctivitis in primary care. |
| [8800624](https://pubmed.ncbi.nlm.nih.gov/8800624/) | 1996 | Review | Drug Safety | Reviews the debated link between ocular chloramphenicol and aplastic anaemia; widely used in the UK for conjunctivitis, rarely in the US. Key safety signal for this indication. |

---

## Australia Market Information

No ARTG entries are recorded for chloramphenicol in this evidence pack, and market status is listed as **not currently marketed in Australia**. Regulatory registration status and product-level information (dosage form, approved indication text) would need to be confirmed directly against the current ARTG/TGA database before any formulary or prescribing decision is made.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information — no key warnings, contraindications, or drug-interaction data were available in this evidence pack (DDI query status: not found).

One safety signal worth flagging from the literature evidence itself: a possible (though disputed) association between topical ocular chloramphenicol and aplastic anaemia (PMID 8800624). This should be specifically addressed once formal PI/TGA safety data is obtained (see DG001 below).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple randomised trials (7) and two Cochrane systematic reviews consistently support chloramphenicol's efficacy in bacterial conjunctivitis, and this use is already clinically established rather than genuinely novel — mechanistic plausibility is high. However, the drug is not currently marketed in Australia (0 ARTG entries), and formal safety/MOA documentation is missing (data gaps DG001–Blocking, DG002–High), so this cannot proceed to formulary or clinical guidance without those gaps closed.

**To proceed, the following is needed:**
- TGA-approved Product Information / registration status confirmation (currently a Blocking data gap — required before any S1 safety assessment)
- Formal DrugBank/manufacturer mechanism-of-action documentation
- Targeted evaluation of the aplastic anaemia signal associated with topical ocular chloramphenicol, to determine whether it warrants a specific warning
- Confirmation of ARTG/import pathway status, since the drug currently has no Australian market presence
- Note: ranks 2–10 in this evidence pack (diffuse scleroderma, postinfectious vasculitis, post-bacterial disorder, post-infectious syndrome, infective urethral stricture, Chagas cardiomyopathy, infection-related HUS, punctate epithelial keratoconjunctivitis, chronic rhinosinusitis) showed weak-to-absent evidence and are recommended **Hold** — no further action needed on these at this time.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

