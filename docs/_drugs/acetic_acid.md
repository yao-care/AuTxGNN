---
layout: default
title: Acetic Acid
parent: 僅模型預測 (L5)
nav_order: 20
evidence_level: L5
indication_count: 10
---

# Acetic Acid
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

# Acetic Acid: From Topical Antiseptic to Post-Bacterial Disorder

## One-Sentence Summary

Acetic acid (CH₃COOH) is a simple organic acid with established topical antiseptic properties, used clinically in wound care and otitis externa management, but with no formally registered pharmaceutical indication in Australia.
The TxGNN model predicts it may have applications in **Post-Bacterial Disorder**,
with **0 dedicated clinical trials** and **0 publications** directly supporting this specific direction.

> **Key finding for Australian clinicians:** Among all top 10 TxGNN predictions, **Tinea Corporis (Rank 9)** is the only candidate with meaningful supporting evidence (L4, 20 publications including historical clinical series directly using dilute acetic acid). A dedicated summary is included at the end of this report.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not formally documented (no TGA-registered indication on file) |
| Predicted New Indication | Post-Bacterial Disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for acetic acid is not available in this dataset. Based on well-established pharmacological knowledge, acetic acid is a short-chain carboxylic acid (pKa 4.75) that exerts broad-spectrum antibacterial activity primarily by lowering local pH, disrupting bacterial cell membrane proton gradients, and impairing pH-sensitive bacterial enzymes. It has recognised clinical use as a topical antiseptic — most notably in chronic suppurative otitis media and otitis externa — as well as in wound care, and as a diagnostic agent (visual inspection with acetic acid, VIA, in cervical cancer screening).

"Post-bacterial disorder" is a broad disease category encompassing conditions that arise as sequelae after bacterial infections — including immune-mediated complications (e.g., reactive arthritis, post-streptococcal glomerulonephritis), intestinal dysmotility, and persistent inflammation driven by immune dysregulation rather than active bacterial colonisation. This pathophysiology is fundamentally distinct from the direct pH-mediated antibacterial mechanism of acetic acid: once active infection has resolved, lowering local pH has no established therapeutic target in the immune remodelling phase.

The TxGNN model's high confidence score (99.98%) for this prediction most likely reflects semantic and ontological proximity in the training knowledge graph between "acetic acid," general "infection," and "post-infection" disease nodes, rather than a biologically validated therapeutic pathway. This is a known limitation of graph-based repurposing models when disease categories share topological neighbours without sharing mechanism. No clinical or preclinical evidence was found to support acetic acid as an intervention for post-bacterial disorder.

---

## Clinical Trial Evidence

Evidence search retrieved 18 trials for the query "Acetic acid + post-bacterial disorder." Upon individual review, **no trial used acetic acid as the primary study drug for this indication.** The single most relevant trial is presented below:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT04120259](https://clinicaltrials.gov/study/NCT04120259) | N/A | Completed | 126 | Apple cider vinegar (~5% acetic acid) combined with metformin vs metformin alone in newly diagnosed Type 2 Diabetes — the only retrieved trial using an acetic acid–containing preparation; indication is metabolic management, not post-bacterial disorder |

> **Note on trial count:** The 18 trials retrieved represent search false positives. Other retrieved trials (NCT07386795, NCT07048028, NCT04434365, NCT04036318, NCT02872675, etc.) involve unrelated drugs — prebiotics, berberine, chitosan, antibiotics — or completely unrelated indications (functional constipation, coronary artery disease, STI prevention). No dedicated clinical trial exists for acetic acid in post-bacterial disorder.

---

## Literature Evidence

Currently no related literature available for acetic acid in post-bacterial disorder.

---

## Australia Market Information

Acetic acid (DrugBank ID: DB03166) is currently **not registered on the Australian Register of Therapeutic Goods (ARTG)** as a standalone pharmaceutical product. No ARTG entries are available.

> Acetic acid may be present as an excipient or a component in TGA-registered formulations (e.g., buffered ear drops for otitis externa), but no standalone therapeutic indication has been approved by the TGA. Healthcare professionals considering any use of this compound must refer to available international Product Information documents and applicable TGA regulatory pathways (e.g., Special Access Scheme, clinical trial approval).

---

## Safety Considerations

Please refer to TGA-approved Product Information (PI) and international regulatory sources for full safety information, as no Australian PI data was available in this evidence pack.

> **Important safety signal identified in literature (tinea-related searches):** PMID [37256034](https://pubmed.ncbi.nlm.nih.gov/37256034/) (2023) documents chemical burn injuries resulting from the inappropriate use of undiluted or high-concentration acetic acid (household vinegar) as a folk remedy applied to skin. Any therapeutic application must specify a maximum concentration (typically ≤2–5%), contact duration, and contraindication for application near mucosal surfaces or broken skin to prevent chemical burns.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's 99.98% confidence score for acetic acid in post-bacterial disorder is not supported by any clinical trial or published literature, and there is no plausible direct mechanistic pathway linking acetic acid's pH-lowering antibacterial action to the immune-mediated and tissue-remodelling pathophysiology that characterises post-bacterial sequelae.

**To proceed, the following would be needed:**
- Basic science evidence establishing whether acetic acid (or short-chain fatty acid metabolites) can modulate post-infection immune responses, complement activation, or tissue repair
- Identification of a specific, well-defined sub-condition within "post-bacterial disorder" where acetic acid's pharmacology could plausibly apply
- Preclinical (in vitro / animal model) studies before any clinical trial design is contemplated

---

## Additional Observation: Tinea Corporis (Rank 9 — Highest Evidence Among Top 10 Predictions)

While the top-ranked TxGNN prediction (post-bacterial disorder) has no supporting evidence, **Tinea Corporis** (ringworm) represents the most evidence-supported repurposing candidate across all top 10 predictions and warrants separate attention.

| Item | Content |
|------|---------|
| Predicted Indication | Tinea Corporis (Ringworm / Dermatophytosis) |
| TxGNN Score | 99.25% |
| Evidence Level | **L4** |
| Recommended Decision | **Research Question** |

### Mechanistic Rationale

Acetic acid inhibits dermatophyte growth (Trichophyton, Epidermophyton, Microsporum) by lowering local skin pH to 4–5, disrupting fungal cell membrane proton gradients and inhibiting keratinolytic enzyme activity. This mechanism is directly applicable to superficial dermatophyte infections. Vinegar — whose primary active component is 5% acetic acid — has a documented history of empirical use in tinea infections across multiple cultures.

### Literature Evidence for Tinea Corporis / Related Tinea

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [20983383](https://pubmed.ncbi.nlm.nih.gov/20983383/) | 1946 | Historical Case Series | Arch Dermatol Syphilol | Dilute acetic acid + special iodine for tinea capitis — direct acetic acid intervention with reported clinical outcomes |
| [20996178](https://pubmed.ncbi.nlm.nih.gov/20996178/) | 1946 | Historical Case Series | JAMA | Dilute acetic acid + special iodine for tinea capitis — published in JAMA, supporting the 1946 series |
| [20256868](https://pubmed.ncbi.nlm.nih.gov/20256868/) | 1947 | Historical Case Series (large) | Urol Cutaneous Rev | Larger case series extending dilute acetic acid results in tinea capitis — the most comprehensive of the Strickler series |
| [37012894](https://pubmed.ncbi.nlm.nih.gov/37012894/) | 2023 | Controlled Clinical Trial | Drug Metab Pers Ther | *Terminalia chebula* + vinegar vs terbinafine 1% cream for tinea corporis (non-inferiority RCT) — vinegar (5% acetic acid) is a key component of the test formulation |
| [28947288](https://pubmed.ncbi.nlm.nih.gov/28947288/) | 2023 | Narrative Review / Letter | J Am Acad Dermatol | Vinegar sock soak for tinea pedis and onychomycosis — reviews evidence for acetic acid-containing folk remedies in dermatophyte infections |
| [13616002](https://pubmed.ncbi.nlm.nih.gov/13616002/) | 1958 | Historical Clinical Study | Vestn Dermatol Venerol | Treatment of epidermophytosis (tinea pedis) with increasing concentrations of acetic acid — direct dose-response investigation |
| [16233325](https://pubmed.ncbi.nlm.nih.gov/16233325/) | 2002 | Basic Science | J Biosci Bioeng | Fermentation product of herbs by lactic acid bacteria shows antifungal activity against tinea; organic acids (including acetic acid) identified as active components under low-pH conditions |
| [37256034](https://pubmed.ncbi.nlm.nih.gov/37256034/) | 2023 | Case Series (Safety Signal) | Arch Plast Surg | Chemical burns from folk remedy use of acetic acid on skin — important safety signal for concentration control in any clinical application |

### Decision for Tinea Corporis

**Recommended Decision: Research Question**

**Rationale:** Three historical clinical series (1946–1947) directly document dilute acetic acid efficacy in tinea capitis; a 2023 controlled trial demonstrates non-inferiority of a vinegar-containing formulation vs terbinafine in tinea corporis; and basic science supports the antifungal mechanism via pH inhibition of dermatophytes. Evidence is L4 (preclinical/mechanism/historical case series) and warrants a formal prospective investigation.

**Suggested next steps:**
- Design a Phase 1/2 pilot RCT evaluating topical dilute acetic acid (2–5% w/v) applied once or twice daily vs standard-of-care antifungal cream (e.g., clotrimazole 1% or terbinafine 1%) for mild-to-moderate tinea corporis
- Include skin pH monitoring, mycological cure rates (KOH and culture), and safety outcomes (skin irritation, TEWL)
- Establish safe concentration and contact-time parameters before clinical use, given the documented burn risk at high concentrations (PMID 37256034)
- Australia context: Note no ARTG-registered acetic acid topical product currently exists; a clinical trial application (CTA) to the TGA would be required

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require prospective clinical validation before therapeutic application. Refer to TGA-approved Product Information for safety and prescribing guidance.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

