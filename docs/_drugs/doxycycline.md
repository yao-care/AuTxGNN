---
layout: default
title: Doxycycline
parent: 僅模型預測 (L5)
nav_order: 170
evidence_level: L5
indication_count: 10
---

# Doxycycline
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

# Doxycycline: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Doxycycline is a broad-spectrum tetracycline antibiotic with well-established efficacy against intracellular bacterial pathogens including *Chlamydia trachomatis*, rickettsia, and *Borrelia* species.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**, with **no clinical trials** and **1 publication** currently supporting this specific direction.
The single available study is a 1992 case series (n=2), placing this prediction firmly at the early research stage — the biological rationale is indirect and requires prospective clinical investigation before any further development.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Broad-spectrum antibacterial use (no ARTG-registered indication found in current data query) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Australia Market Status | Not found in ARTG query (verify against current ARTG database) |
| Number of ARTG Entries | 0 (data gap — TGA query not completed; recommend manual verification) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Doxycycline is not available in this evidence pack. Based on established clinical knowledge, Doxycycline is a tetracycline-class antibiotic that inhibits bacterial protein synthesis by blocking the 30S ribosomal subunit. It is the **WHO first-line treatment for *Chlamydia trachomatis*** (100 mg twice daily for 7 days) and is active against a broad range of intracellular organisms including rickettsia, *Borrelia burgdorferi*, and *Mycoplasma pneumoniae*. It also exerts a secondary anti-inflammatory effect through inhibition of matrix metalloproteinases (MMP-1, MMP-8, MMP-13).

The predicted link to punctate epithelial keratoconjunctivitis rests on the fact that *C. trachomatis* is both the causative organism of chlamydial follicular conjunctivitis and a recognised precipitant of corneal epithelial changes. By eradicating the primary bacterial infection, doxycycline could theoretically prevent progression to corneal involvement. Additionally, doxycycline's MMP-inhibitory properties may provide a secondary layer of corneal-epithelial protection by attenuating matrix degradation.

However, the only available publication (PMID 1424659, 1992) reports **the opposite outcome**: in two patients treated with oral tetracycline or doxycycline for chlamydial follicular conjunctivitis, the follicles resolved but bilateral recurrent punctate epithelial keratitis subsequently developed and persisted. This suggests the corneal lesions may be **immune-mediated** rather than directly infectious — substantially weakening the mechanistic case for doxycycline as a treatment for established punctate epithelial keratoconjunctivitis. The TxGNN score reflects structural similarity in the knowledge graph, not confirmed clinical efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Case Series | *Cornea* | Two patients with chlamydial follicular conjunctivitis treated with oral tetracycline or doxycycline — follicles resolved, but both subsequently developed recurrent bilateral punctate epithelial keratitis with anterior stromal oedema, persisting despite antibiotic treatment; authors suggest immune-mediated rather than directly infectious aetiology |

---

## Australia Market Information

No ARTG entries were returned for Doxycycline in the current data query. This likely reflects a gap in the automated TGA data retrieval rather than true absence from the Australian market — Doxycycline-containing products (e.g., capsule formulations) are in clinical use in Australia. **A manual verification against the current ARTG database is strongly recommended before drawing regulatory conclusions.**

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No key warnings, contraindications, or drug interaction data were retrieved for this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The sole supporting publication is a 32-year-old case series of two patients, which paradoxically documents **treatment failure** — doxycycline cleared the underlying chlamydial infection but did not prevent or resolve the subsequent punctate epithelial keratoconjunctivitis, indicating the corneal pathology is likely immune-mediated and may lie outside the therapeutic scope of an antibiotic. There are no registered clinical trials, no systematic reviews, and no prospective data for this indication.

**To proceed, the following is needed:**

- Prospective clinical studies directly investigating oral or topical doxycycline in punctate epithelial keratoconjunctivitis, particularly of confirmed chlamydial or post-chlamydial origin
- Mechanistic clarification: determine whether the persistent corneal lesion is amenable to antimicrobial therapy, MMP inhibition, or requires a separate immunosuppressive approach (e.g., topical corticosteroids)
- Complete TGA safety data review: retrieve the current Australian Product Information (PI) for Doxycycline to identify key warnings, contraindications, and clinically significant drug interactions
- ARTG verification: confirm current registration status and approved indications via the TGA ARTG portal
- Evidence re-evaluation at ranks 4 (*post-bacterial disorder*), 5 (*post-infectious syndrome*), and 10 (*chronic gingivitis*), each of which carry L2 evidence with a **"Proceed with Guardrails"** recommendation and may represent more viable near-term development priorities than the rank 1 indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

