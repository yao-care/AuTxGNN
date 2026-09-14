---
layout: default
title: Tislelizumab
parent: 僅模型預測 (L5)
nav_order: 680
evidence_level: L5
indication_count: 10
---

# Tislelizumab
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

# Tislelizumab: From Advanced Solid Tumour Immunotherapy to Predicted Autoimmune/Haematologic Indications — Not Supported by Evidence

## One-Sentence Summary

> Tislelizumab is an anti-PD-1 monoclonal antibody; literature within this evidence pack describes its use in advanced solid tumours (e.g., oesophageal cancer, NSCLC, cervical cancer, metastatic colorectal cancer), but it is **not currently registered in Australia**. The TxGNN model's top-ranked prediction — **mixed-type autoimmune hemolytic anaemia** — has **zero supporting clinical trials or literature**, and the model's own mechanistic assessment flags this as likely graph-topology noise rather than a genuine signal. Across all 10 ranked candidates in this pack, evidence is capped at **L4–L5**, and several are actively **contradicted** by post-marketing literature showing tislelizumab *causes* immune-related tissue injury rather than treating it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided as structured licence data. Literature in this pack describes tislelizumab as an anti-PD-1 monoclonal antibody used for advanced solid tumours (oesophageal cancer, NSCLC, cervical cancer, metastatic colorectal cancer) |
| Predicted New Indication | Mixed-type autoimmune hemolytic anaemia |
| TxGNN Prediction Score | 93.76% |
| Evidence Level | L5 (model prediction only — no clinical trials, no literature) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, no formal mechanism-of-action field is available for this drug (`original_moa: [Data Gap]`). However, literature captured in this evidence pack consistently describes tislelizumab as a humanised IgG4 anti-PD-1 monoclonal antibody that blocks the PD-1/PD-L1 pathway to reactivate anti-tumour T-cell immunity, approved for various advanced solid tumours.

The predicted indication — mixed-type autoimmune hemolytic anaemia — sits at the opposite end of the immunological spectrum from the drug's original use. PD-1 blockade *removes* a brake on T-cell activity to fight cancer; autoimmune haemolysis is a condition where immune tolerance has already failed. The evidence pack's own rationale for this candidate states explicitly: *"TxGNN 高分僅反映知識圖譜中血液/免疫節點的拓樸相似性，無方向性... 機轉上傾向誘發或加重自體免疫溶血，而非治療"* — i.e., the high score reflects proximity of blood/immune nodes in the knowledge graph, not a directional therapeutic relationship, and mechanistically PD-1 blockade would be expected to *worsen*, not treat, this condition.

This concern is reinforced by the two lower-ranked candidates that do have literature (dermatitis, rank 3; proteinuria, rank 6): nearly all of the retrieved papers are **case reports of tislelizumab-induced toxicity** (Stevens-Johnson syndrome/toxic epidermal necrolysis, DRESS syndrome, agranulocytosis, renal thrombotic microangiopathy, ANCA-associated vasculitis) — i.e., evidence that the drug *causes* these conditions as adverse events, not evidence that it treats them. **None of the 10 ranked candidates in this pack has any evidence pointing in the therapeutic direction.**

---

## Clinical Trial Evidence

*For the top-ranked predicted indication (mixed-type autoimmune hemolytic anaemia):*

Currently no related clinical trials registered.

---

## Literature Evidence

*For the top-ranked predicted indication (mixed-type autoimmune hemolytic anaemia):*

Currently no related literature available.

---

## Australia Market Information

Tislelizumab is **not currently marketed in Australia** (0 ARTG entries; `market_status: 未上市`). No licence records are available in this evidence pack.

---

## Cytotoxicity (Antineoplastic Drug)

Tislelizumab is classified here as antineoplastic based on literature evidence describing its use across multiple solid-tumour indications.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-1 immune checkpoint inhibitor monoclonal antibody) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Low for classic dose-dependent myelosuppression; however, case reports in this pack document immune-related **agranulocytosis** (PMID [38910480](https://pubmed.ncbi.nlm.nih.gov/38910480/)) as a rare idiosyncratic event |
| Emetogenicity Classification | Please refer to the Product Information (PI) — no emetogenicity data available in this evidence pack |
| Monitoring Items | Skin/mucosal surveillance (SJS/TEN, DRESS risk), FBC with differential, renal function and urinalysis (proteinuria/TMA risk), liver function |
| Handling Protection | Monoclonal antibody-based immunotherapy; handle per institutional hazardous-drug policy for biologic oncology agents — precaution level typically differs from conventional cytotoxic chemotherapy (confirm against local guidelines, as no TGA PI is available) |

---

## Safety Considerations

Official safety fields (key warnings, contraindications, DDI) are all data gaps in this pack — no TGA Product Information exists as the drug is unregistered. However, the pack's own literature retrieval (attached to lower-ranked candidates, not the top prediction) surfaced a consistent and clinically important **post-marketing safety signal** that should inform any future evaluation of this drug, regardless of indication:

| PMID | Year | Type | Journal | Signal |
|------|------|------|---------|--------|
| [40491908](https://pubmed.ncbi.nlm.nih.gov/40491908/) | 2025 | Disproportionality analysis (FAERS) | Frontiers in Immunology | Systematic post-marketing safety review of immune-related adverse reactions |
| [41346629](https://pubmed.ncbi.nlm.nih.gov/41346629/) | 2025 | Case report | Frontiers in Immunology | SJS/TEN involving >80% body surface area after first infusion |
| [41269056](https://pubmed.ncbi.nlm.nih.gov/41269056/) | 2026 | Systematic review | Cutaneous and Ocular Toxicology | Clinical characteristics of tislelizumab-induced SJS/TEN in Chinese population |
| [38910480](https://pubmed.ncbi.nlm.nih.gov/38910480/) | 2025 | Case report | Current Drug Safety | Toxic epidermal necrolysis with concurrent agranulocytosis |
| [40447060](https://pubmed.ncbi.nlm.nih.gov/40447060/) | 2025 | Case report | Clinical Immunology | DRESS syndrome in a patient with FGFR3 mutation |
| [40528285](https://pubmed.ncbi.nlm.nih.gov/40528285/) | 2025 | Case report | Nephrology (Carlton) | Renal-limited thrombotic microangiopathy (fruquintinib + tislelizumab) |
| [40420929](https://pubmed.ncbi.nlm.nih.gov/40420929/) | 2025 | Case report | World J Clin Cases | ANCA-associated granulomatosis with polyangiitis |
| [37909927](https://pubmed.ncbi.nlm.nih.gov/37909927/) | 2024 | Review | Cutaneous and Ocular Toxicology | Characterisation of cutaneous adverse reactions overall |

These are immune-related adverse events consistent with the drug's PD-1 inhibitor class, not evidence relevant to any repurposing indication in this pack. This should not be read in place of the TGA-approved Product Information, which is not yet available as the drug is unregistered in Australia.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No candidate among the 10 ranked predictions in this pack reaches beyond L4–L5 evidence, and the top-ranked candidate has zero clinical trial or literature support. Where literature does exist for lower-ranked candidates (dermatitis, proteinuria), it consistently documents tislelizumab as the **cause** of the condition (SJS/TEN, DRESS, TMA, vasculitis) rather than a treatment for it — directly contradicting the repurposing hypothesis. The drug is also unregistered in Australia, with no TGA PI, MOA, or licence data available.

**To proceed, the following is needed:**
- Formal mechanism-of-action and TGA/sponsor regulatory data for tislelizumab
- A hypothesis-driven mechanistic rationale for any candidate indication, distinct from raw knowledge-graph proximity
- Preclinical or clinical evidence showing a therapeutic (not adverse) effect in the candidate indication before advancing past S0/S1
- If pursued for Australian market entry at all, this should proceed on the basis of its established oncology indications rather than any candidate in this pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

