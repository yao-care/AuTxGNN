---
layout: default
title: Degarelix
parent: Model Prediction Only (L5)
nav_order: 206
evidence_level: L5
indication_count: 10
---

# Degarelix
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Degarelix: From Prostate Cancer to Hypertrichosis

## One-Sentence Summary

Degarelix is a GnRH receptor antagonist marketed in Australia as Firmagon 80 mg. The data compiled for this report did not include an approved indication text for it. The TxGNN model predicts it may be effective for **hypertrichosis**, but there are **0 clinical trials** and **0 publications** supporting this direction, and the mechanistic rationale is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the ARTG entry has no indication text) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Degarelix is a GnRH receptor antagonist. It suppresses LH and FSH and, as a result, testosterone and downstream androgens.

Hypertrichosis is generally not androgen-dependent (unlike hirsutism), so the link to androgen suppression is weak. The very high TxGNN score is a graph-based prediction with no supporting trial or literature evidence. Hypertrichosis is also a recognised adverse effect of some drugs, and no data suggest degarelix would treat it.

The other top-ranked predictions are similarly poorly supported. They include Ambras-type hypertrichosis, Dandy-Walker malformation syndromes, malformation syndromes with dental involvement, isolated hair shaft abnormalities, allergic and cold urticaria, and familial isolated trichomegaly. They are mostly genetic or developmental conditions with no plausible GnRH-related mechanism, and the scores likely reflect network proximity rather than a real therapeutic link.

Two lower-ranked predictions are mechanistically closer to degarelix's axis but still lack clinical evidence:
- **Central precocious puberty:** GnRH antagonism is plausible and GnRH agonists are standard of care. Degarelix has no paediatric trials and requires depot injections with notable injection-site reactions.
- **Familial male-limited precocious puberty:** This is driven by activating LHCGR mutations downstream of the pituitary, so GnRH blockade would not be expected to control it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2784M | Firmagon 80mg | Powder for injection 80 mg (as acetate), injection set | Not stated in the data compiled |

---

## Cytotoxicity

Degarelix is a hormonal agent, not a conventional cytotoxic, and the data compiled for this report did not classify it as antineoplastic. This section is therefore omitted.

---

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text):** long QT syndrome, familial long QT syndrome, torsades de pointes, liver disease, gallbladder disease, potassium deficiency disease.
- **Drug Interactions:** 100 interactions were identified in total. The first 20 returned include:
  - **Major:** cisapride, dolasetron.
  - **Moderate:** famotidine, loperamide, bisacodyl, clarithromycin, picosulfuric acid, polyethylene glycol (3350 with electrolytes), castor oil, glycerin, granisetron, lactitol, lactulose, levofloxacin, magnesium citrate, magnesium hydroxide, mineral oil, ondansetron, palonosetron.
  - **Minor:** metronidazole.
  - Many of these are QT-prolonging or electrolyte-disturbing agents, which is consistent with the QT-related contraindication signals above.

Label warnings and contraindications were not available. Please refer to the TGA-approved Product Information (PI) for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or publications, and the mechanism does not support efficacy in hypertrichosis, which is generally not androgen-driven.

**To proceed, the following is needed:**
- Approved indication text and PI warnings and contraindications from the TGA/ARTG record
- Detailed mechanism of action data
- Any preclinical or clinical evidence linking GnRH antagonism to hypertrichosis
- If a more plausible candidate is pursued (e.g. central precocious puberty), a paediatric safety and feasibility assessment first
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

