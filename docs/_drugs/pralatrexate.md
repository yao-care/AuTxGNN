---
layout: default
title: Pralatrexate
parent: Model Prediction Only (L5)
nav_order: 593
evidence_level: L5
indication_count: 10
---

# Pralatrexate
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

# Pralatrexate: From Peripheral T-cell Lymphoma to Pleural Adenomatoid Tumor

## One-Sentence Summary

Pralatrexate is an antifolate chemotherapy originally used for **peripheral T-cell lymphoma** and related T-cell and NK-cell lymphomas.
The TxGNN model's top-ranked new prediction is **pleural adenomatoid tumor**, but **no clinical trials or publications** support it.
The better-supported predictions are in the mesothelioma family, where one Phase II trial in pleural mesothelioma has been published.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peripheral T-cell lymphoma (including mature T-cell and NK-cell non-Hodgkin lymphoma and primary cutaneous T-cell lymphoma subtypes). The ARTG entry in the data compiled for this report has no indication text. |
| Predicted New Indication | Pleural adenomatoid tumor |
| TxGNN Prediction Score | 99.91% (model rank 1583) |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Pralatrexate is an antifolate that inhibits dihydrofolate reductase (DHFR) and enters cells efficiently through the reduced folate carrier (RFC-1). Detailed mechanism-of-action data were not available in the data compiled for this report, so this description is based on the drug's known class. Blocking folate metabolism stops tumour cells from making the building blocks for DNA, which is why antifolates work in rapidly dividing lymphoid cancers.

For the lead prediction, the mechanistic case is weak. Adenomatoid tumors are benign lesions arising from mesothelial cells and rarely need systemic treatment. A cytotoxic antifolate has little clinical rationale here. The high score probably reflects proximity to mesothelioma in the knowledge graph rather than a true therapeutic signal.

The mesothelioma predictions are more credible. Pemetrexed, another antifolate, is an established treatment for pleural mesothelioma, and pralatrexate shares its DHFR inhibition and RFC-1 uptake. This is why the pleural epithelioid mesothelioma (rank 4) and pleural mesothelioma (rank 10) predictions were graded L3 rather than L5. The other mesothelioma-related predictions (biphasic, lymphohistiocytoid, sarcomatoid, peritoneal, well-differentiated papillary, and pericardial) have no supporting data.

The relapsing-remitting multiple sclerosis prediction (rank 2) has only a weak theoretical link through antimetabolite immunomodulation. Its toxicity profile and the many approved alternatives argue against it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for pleural adenomatoid tumor. No registered trials were found for any of the other top-ten predictions either.

---

## Literature Evidence

Currently no related literature available for pleural adenomatoid tumor.

The following publications relate to the better-supported mesothelioma predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17409804](https://pubmed.ncbi.nlm.nih.gov/17409804/) | 2007 | Phase II trial (single-arm, per title) | J Thorac Oncol | Pralatrexate in unresectable malignant pleural mesothelioma. The abstract notes that mesothelioma responds to antifolates, that pralatrexate's toxicity is mainly stomatitis, and that it was active in mesothelioma cell lines and xenografts. Full results were not reviewed. |
| [21301589](https://pubmed.ncbi.nlm.nih.gov/21301589/) | 2010 | Review | Cancer Manag Res | Overview of antifolate chemotherapy targeting folic acid synthesis. It supports the mechanism but is not clinical evidence. |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 11271F | Folotyn | Solution for I.V. infusion, 20 mg in 1 mL | Not provided in the data compiled |

Pralatrexate is available in Australia only as an intravenous injection.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antifolate antimetabolite) |
| Myelosuppression Risk | Medium to high. Neutropenia, thrombocytopenia and anaemia are all flagged in the knowledge graph. |
| Emetogenicity Classification | Low (general class knowledge; confirm in the Product Information) |
| Monitoring Items | FBC with differential, renal and liver function, and oral mucosa assessment for stomatitis |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Key Warnings and Contraindications**: Label-based warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI).
- **Knowledge-graph contraindication signals** (not label text): thrombocytopenia, neutropenia, agranulocytosis, anaemia (including macrocytic anaemia), impaired renal function, and stomatitis.
- **Drug Interactions**: The interaction screen returned 100 interactions in total, and the data compiled for this report list 20 of them.
  - **Major**: deferiprone and samarium (153Sm) lexidronam, both likely additive with the drug's myelosuppression.
  - **Moderate**: NSAIDs and salicylates (aspirin, ibuprofen, flurbiprofen, diclofenac, ketorolac, sodium salicylate), glucarpidase, palifermin, pyrimethamine, chloramphenicol, zidovudine, roflumilast, naltrexone, sapropterin, strontium-89 chloride, and tetanus toxoid vaccine.
  - Concomitant NSAID use deserves particular attention because of the renal-function signal.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The lead prediction, pleural adenomatoid tumor, rests on model output alone (L5). It is a benign, rarely treated lesion, so cytotoxic therapy is hard to justify. The mesothelioma-family predictions are more promising, with a single-arm Phase II trial and a shared mechanism with pemetrexed. They still fall short of the evidence needed for a Go decision.

**To proceed, the following is needed:**
- A full-text review of the Phase II mesothelioma trial (PMID 17409804), covering response rate, survival, toxicity and comparison with pemetrexed.
- A decision to redirect the repurposing question to pleural or epithelioid mesothelioma, where the evidence is stronger.
- Mechanism-of-action data for pralatrexate (for example from DrugBank).
- The TGA Product Information, including the approved indication, warnings and contraindications.
- A safety and monitoring plan for myelosuppression, mucositis and renal impairment, and a review of the interacting medicines.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

