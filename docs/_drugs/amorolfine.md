---
layout: default
title: Amorolfine
parent: 僅模型預測 (L5)
nav_order: 44
evidence_level: L5
indication_count: 10
---

# Amorolfine
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

# Amorolfine: From Onychomycosis to Drug-Induced Osteoporosis

## One-Sentence Summary

Amorolfine is a morpholine-class topical antifungal agent, internationally recognised for the treatment of onychomycosis (fungal nail infections), though it is not currently registered with the TGA in Australia.
The TxGNN model predicts it may have potential in **drug-induced osteoporosis**, however, there are currently **no clinical trials** and **no published literature** supporting this direction.
This prediction is based on model inference alone and carries an extremely weak mechanistic rationale.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Onychomycosis (fungal nail infections) — not TGA-registered in Australia |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.9978% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Amorolfine is a morpholine-class antifungal that inhibits two enzymes in the fungal ergosterol biosynthesis pathway — ERG24 (sterol Δ14-reductase) and ERG2 (sterol Δ8→Δ7-isomerase). By blocking ergosterol production, it disrupts fungal cell membrane integrity. These target enzymes are highly fungal-specific; their mammalian homologues play only a minor role in human sterol metabolism, and Amorolfine has no established activity against them.

There is a distant theoretical argument connecting sterol metabolism to bone health: statins, which act upstream on the mevalonate/cholesterol pathway, have been observed in some studies to promote osteoblast activity — suggesting a sterol–bone metabolism intersection. Drug-induced osteoporosis itself typically arises from medications such as corticosteroids, proton pump inhibitors, or antiepileptics, none of which share a mechanism with Amorolfine.

In practice, the mechanistic bridge is essentially absent. No published evidence exists that Amorolfine — or its metabolites — influences mammalian sterol synthesis, bone remodelling, calcium homeostasis, or osteoclast/osteoblast activity. Systemic absorption from the topical nail lacquer formulation is negligible. The TxGNN prediction appears to be driven by knowledge graph network topology rather than any meaningful pharmacological overlap, and should be interpreted with caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Amorolfine is not currently listed on the Australian Register of Therapeutic Goods (ARTG). There are no TGA-approved products containing amorolfine at this time.

> **Note for clinicians:** Amorolfine-based products (e.g., Loceryl® 5% nail lacquer) are commercially available in several other countries including the United Kingdom, France, New Zealand, and across Europe for topical treatment of onychomycosis. Australian clinicians wishing to access this product for an approved international indication would need to apply through the TGA's Special Access Scheme (SAS Category B) or the Authorised Prescriber pathway. Any use in a novel repurposed indication would require a specific research protocol and ethics approval.

---

## Safety Considerations

As amorolfine carries no TGA-approved Product Information (PI) in Australia, formal Australian safety data is unavailable. Please refer to international Product Information documents (e.g., the EMA Summary of Product Characteristics or Medsafe NZ data sheet) for full safety information.

Key safety considerations from international labelling include:

- **Topical use only** — current formulations are designed exclusively for nail application; no systemic formulation exists
- Avoid contact with eyes, ears, and mucous membranes
- Flammable formulation — keep away from open flame or heat sources
- **Pregnancy and breastfeeding** — not recommended; systemic safety data are insufficient
- Local skin reactions (burning sensation, erythema, pruritus at application site) have been reported, though systemic adverse effects are rare given minimal percutaneous absorption
- No drug–drug interaction data identified in current evidence databases

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's prediction of amorolfine for drug-induced osteoporosis is entirely unsupported by clinical or preclinical evidence, and the mechanistic rationale is extremely weak. Amorolfine targets fungal-specific sterol biosynthesis enzymes with no demonstrated activity on mammalian bone metabolism. The drug is also not TGA-registered in Australia and exists only as a topical nail formulation with negligible systemic bioavailability, making any systemic indication clinically impractical without significant reformulation.

**To proceed, the following would be required:**

- Preclinical studies (in vitro and animal models) demonstrating any measurable effect of amorolfine or its metabolites on osteoblast/osteoclast activity or bone mineral density
- Identification of a credible mechanistic link between ERG24/ERG2 inhibition and mammalian bone remodelling pathways
- Development of a systemic oral or parenteral formulation, as the current topical formulation provides negligible systemic exposure
- TGA registration or SAS approval for any systemic use
- Independent replication of the TxGNN prediction signal using complementary computational approaches (e.g., structural similarity, transcriptomic profiling) to rule out a false-positive network artefact

---

> **Disclaimer:** This report is intended for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any therapeutic application. All content should be reviewed alongside a TGA-approved or internationally recognised Product Information document before any clinical decision is made.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

