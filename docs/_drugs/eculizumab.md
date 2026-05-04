---
layout: default
title: Eculizumab
parent: 僅模型預測 (L5)
nav_order: 177
evidence_level: L5
indication_count: 10
---

# Eculizumab
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

# Eculizumab: From Paroxysmal Nocturnal Haemoglobinuria to Cyclic Hematopoiesis

---

## One-Sentence Summary

Eculizumab is a recombinant humanised monoclonal antibody that inhibits complement protein C5, clinically established for rare complement-mediated haematological conditions including paroxysmal nocturnal haemoglobinuria (PNH) and atypical haemolytic uraemic syndrome (aHUS).
The TxGNN model predicts it may be effective for **Cyclic Hematopoiesis** (cyclic neutropenia), with a prediction confidence of **99.97%**; however, **no registered clinical trials and no directly supporting publications** are currently available for this specific indication, placing this prediction at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Paroxysmal nocturnal haemoglobinuria (PNH) / atypical haemolytic uraemic syndrome (aHUS) *(inferred from literature context; no formal ARTG indication text available)* |
| Predicted New Indication | Cyclic Hematopoiesis (Cyclic Neutropenia) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Eculizumab is a terminal complement inhibitor that selectively binds complement protein C5 with high affinity, blocking its proteolytic cleavage into C5a (anaphylatoxin) and C5b. By preventing C5b, it halts assembly of the terminal complement complex C5b-9 (membrane attack complex, MAC). Its proven clinical efficacy in PNH and aHUS demonstrates that this mechanism can protect haematopoietic and vascular cell populations from complement-driven lysis and thromboinflammation.

Cyclic hematopoiesis (also known as cyclic neutropenia; OMIM #162800) is a rare autosomal dominant bone marrow oscillation disorder caused predominantly by mutations in the *ELANE* gene encoding neutrophil elastase. Neutrophil counts cycle with a period of approximately 21 days, with nadir periods of severe neutropenia lasting 3–6 days. The core pathophysiology is an intrinsic haematopoietic progenitor cycling defect, not peripheral complement-mediated blood cell destruction. In this context, a mechanistic rationale for C5 inhibition is speculative: there is no established evidence that complement MAC-mediated neutrophil lysis drives the cyclical nadir, and the primary lesion resides upstream at the progenitor level.

The high TxGNN prediction score most likely reflects graph-level connectivity between complement pathway nodes and haematological phenotype nodes in the underlying knowledge graph, rather than a validated direct biological mechanism. This finding represents a hypothesis-generating signal that warrants exploratory mechanistic investigation — particularly whether secondary complement activation contributes to accelerated neutrophil apoptosis during the nadir phase — before any clinical repurposing consideration is warranted.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for cyclic hematopoiesis specifically.

> **Note:** A body of literature exists linking Eculizumab to complement-mediated haematological conditions (PNH, aHUS, thrombotic microangiopathies), which informed the mechanistic background discussion above. These publications do not constitute evidence for the predicted indication of cyclic hematopoiesis and are therefore not listed here.

---

## Australia Market Information

No ARTG registrations were identified for Eculizumab in the TGA database query (data cutoff: 4 April 2026).

> Please verify current TGA registration status directly via the [ARTG Public Summary Search](https://www.tga.gov.au/resources/artg), as registration status may have changed after data cutoff.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

> **Note:** Key warnings, contraindications, and drug interaction data were not available in this Evidence Pack. Clinicians should be aware that Eculizumab, as a terminal complement inhibitor, carries a well-documented class risk of life-threatening *Neisseria meningitidis* infection; vaccination requirements and monitoring protocols are detailed in the approved PI.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model generates a statistically high prediction score, but this is unsupported by any clinical trial evidence, any direct mechanistic link between complement C5 inhibition and the pathophysiology of cyclic neutropenia, or any published case data — placing this candidate firmly at Evidence Level L5. Furthermore, Eculizumab currently has no ARTG registration in Australia, and key safety data are unavailable, making progression to any feasibility assessment premature at this stage.

**To proceed, the following is needed:**

- **Mechanistic validation:** Conduct a focused literature and preclinical review to determine whether complement activation (C5a/MAC) contributes to accelerated neutrophil apoptosis or destruction during cyclic neutropenia nadir phases
- **Indirect evidence search:** Broaden PubMed search to include related cyclic neutropenia case reports involving complement markers or autoimmune overlap (e.g., anti-neutrophil antibodies + complement consumption)
- **Regulatory clarification:** Confirm current TGA/ARTG registration status and obtain the approved Product Information (PI) for Eculizumab (Soliris® or equivalent biosimilar)
- **MOA documentation:** Obtain formal DrugBank mechanism of action record to complete the mechanistic assessment
- **Safety baseline:** Extract key warnings and contraindications from the TGA PI prior to any feasibility study design
- **Knowledge graph audit:** Review whether the TxGNN cyclic hematopoiesis node is appropriately differentiated from PNH and other complement-linked haematological nodes to rule out graph-level conflation as the source of the high prediction score

---

*This report is for research reference only and does not constitute medical advice. All repurposing candidates require formal clinical validation before therapeutic application. Data cutoff: 4 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

