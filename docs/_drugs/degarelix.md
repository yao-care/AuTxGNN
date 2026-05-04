---
layout: default
title: Degarelix
parent: 僅模型預測 (L5)
nav_order: 145
evidence_level: L5
indication_count: 10
---

# Degarelix
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

# Degarelix: From Prostate Cancer to Hypertrichosis

## One-Sentence Summary

Degarelix (Firmagon) is a GnRH receptor antagonist approved in multiple jurisdictions for advanced hormone-sensitive prostate cancer, suppressing testosterone to castrate levels by blocking pituitary GnRH receptors.
The TxGNN model predicts it may be effective for **Hypertrichosis (generalised excessive hair growth)**, however the mechanistic basis is weak, with **no clinical trials** and **no supporting publications** currently available for this indication.
Evidence remains at the preclinical/mechanistic reasoning stage only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Advanced hormone-sensitive prostate cancer |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Degarelix is a synthetic decapeptide GnRH receptor antagonist. By competitively blocking GnRH receptors in the anterior pituitary, it rapidly and reversibly suppresses LH and FSH secretion, resulting in a swift reduction of testosterone and oestradiol to castrate levels — critically, without the initial testosterone "flare" associated with GnRH agonists. This makes it particularly suitable for patients with prostate cancer where a testosterone surge could cause acute symptom worsening.

The theoretical rationale connecting Degarelix to hair disorders rests on the well-established role of androgens — particularly dihydrotestosterone (DHT) — in regulating hair follicle cycling. By substantially lowering circulating androgens, a GnRH antagonist could theoretically reduce androgen-dependent excessive hair growth in conditions such as hirsutism or polycystic ovary syndrome (PCOS)-associated hyperandrogenism.

However, there is a fundamental distinction that undermines this prediction: **hypertrichosis** and **hirsutism** are not the same condition. Hypertrichosis is generalised, non-androgen-dependent excessive hair growth, with pathophysiology encompassing congenital genetic variants, drug-induced causes, and paraneoplastic mechanisms — none of which involve the GnRH–gonadal axis. The TxGNN model's high prediction score almost certainly reflects topological proximity of hair-related nodes within the knowledge graph, rather than a biologically meaningful drug–disease relationship. The mechanistic link is assessed as **weak to absent** for true hypertrichosis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Degarelix is **not currently registered with the Therapeutic Goods Administration (TGA)** and holds no ARTG entries. It is not marketed in Australia.

Healthcare professionals seeking prescribing information should refer to:
- The **FDA prescribing information** for Firmagon® (ferring Pharmaceuticals)
- The **EMA Summary of Product Characteristics** (Firmagon, EU/1/08/504)
- The **TGA Unapproved Medicines scheme** (Special Access Scheme or Authorised Prescriber pathway) if clinical use is being considered

---

## Cytotoxicity

Degarelix is used in the treatment of prostate cancer and is therefore assessed under cytotoxicity criteria.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Hormone therapy — GnRH receptor antagonist (not a conventional cytotoxic agent) |
| Myelosuppression Risk | Low (hormone therapy mechanism; myelosuppression is not a primary concern) |
| Emetogenicity Classification | Minimal |
| Monitoring Items | Serum testosterone, PSA, liver function tests, QTc interval (ECG monitoring for prolongation risk), bone mineral density (with long-term use due to androgen deprivation) |
| Handling Protection | Standard pharmaceutical handling procedures; cytotoxic drug handling protocols are **not** required |

---

## Safety Considerations

As Degarelix holds no TGA registration and formal Australian Product Information (PI) is unavailable, complete safety data could not be retrieved.

Please refer to the **FDA Firmagon® Prescribing Information** or **EMA Summary of Product Characteristics** for full safety details. Key areas of known clinical concern based on the drug class include:

- **Injection site reactions** (pain, erythema, swelling) — common with the subcutaneous formulation
- **QTc prolongation** — androgen deprivation therapy is associated with QT interval changes; ECG monitoring is advisable in patients with cardiac risk factors or on concomitant QT-prolonging agents
- **Cardiovascular risk** — androgen deprivation therapy is associated with increased risk of metabolic syndrome, diabetes, and cardiovascular events with long-term use
- **Bone mineral density loss** — androgen suppression accelerates osteoporosis; baseline and periodic bone density monitoring is recommended

No formal Drug–Drug Interaction (DDI) data was retrieved in this evidence pack. Clinicians should exercise caution with co-administration of QT-prolonging medicines.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN prediction (hypertrichosis) lacks a plausible mechanistic basis — hypertrichosis is predominantly non-androgen-dependent, meaning Degarelix's primary mechanism of action is unlikely to be therapeutically relevant. There are no registered clinical trials and no supporting literature for this indication. The high TxGNN score is assessed as a likely knowledge graph topological false positive.

**To proceed, the following is needed:**

- **Disease subtype clarification**: Determine whether the clinical question is actually about *androgen-dependent* hirsutism (e.g., PCOS, congenital adrenal hyperplasia) rather than true hypertrichosis — a different patient population where the mechanistic rationale would be considerably stronger
- **Preclinical evidence**: Mechanistic or in vitro studies demonstrating GnRH receptor involvement in hypertrichosis pathophysiology
- **Safety profiling for new populations**: Existing safety data is derived entirely from adult male prostate cancer patients; data for women, adolescents, or paediatric populations is absent
- **TGA regulatory pathway**: Degarelix is not registered in Australia; any clinical use would require a Special Access Scheme (SAS) application or Authorised Prescriber designation — and any repurposing use would require a separate regulatory strategy
- **Consideration of higher-ranked mechanistic predictions**: Ranks 8–9 in this evidence pack (familial male-limited precocious puberty; central precocious puberty) carry substantially stronger mechanistic rationale for a GnRH antagonist and may represent more viable repurposing candidates for further evaluation

---

> ⚠️ **Disclaimer**: This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates identified through computational modelling require clinical validation before any therapeutic application. All prescribing decisions must comply with current TGA regulations and approved indications.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

