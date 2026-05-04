---
layout: default
title: Brinzolamide
parent: 僅模型預測 (L5)
nav_order: 102
evidence_level: L5
indication_count: 10
---

# Brinzolamide
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

# Brinzolamide: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Brinzolamide (Azopt®) is a topical carbonic anhydrase inhibitor (CAI) approved internationally for the treatment of open-angle glaucoma and ocular hypertension, but currently holds **no TGA registration** in Australia (0 ARTG entries).
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**, achieving the highest prediction score across all candidates (99.48%);
however, there are currently **no clinical trials** and **no publications** specifically supporting this indication — the prediction is driven by pharmacological class-level knowledge graph connectivity rather than direct clinical evidence for this genetic subtype.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Open-angle glaucoma and ocular hypertension (globally approved; no current TGA registration in Australia) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Brinzolamide is a highly selective inhibitor of carbonic anhydrase isoenzymes CA-II and CA-IV, which are expressed in the ciliary body epithelium of the eye. By blocking these enzymes, Brinzolamide reduces bicarbonate ion (HCO₃⁻) secretion into the aqueous humour, decreasing aqueous humour production and lowering intraocular pressure (IOP) by approximately 15–18% from baseline. This mechanism has been extensively validated in adults with open-angle glaucoma and ocular hypertension across multiple large Phase 3 RCTs — representing the most robust evidence base in the broader candidate list for this drug.

Primary hereditary glaucoma — also known as primary congenital or infantile glaucoma — is caused by mutations in genes such as *CYP1B1* (GLC3A locus) and *LTBP2* (GLC3D locus), leading to maldevelopment of the trabecular meshwork and Schlemm's canal. The resulting impairment of aqueous humour *outflow* causes sustained IOP elevation from infancy, with progressive optic nerve damage and, if untreated, irreversible blindness. Because Brinzolamide acts on the *production* side of aqueous humour dynamics rather than the outflow pathway, it is theoretically capable of complementary IOP lowering even when the outflow tract is structurally abnormal — making the mechanistic link plausible.

However, important clinical caveats must be noted. The standard of care for primary hereditary glaucoma is surgical intervention (goniotomy or trabeculotomy), with medical therapy serving only an adjunctive role to bridge to surgery or manage residual IOP. The target population — predominantly infants and young children — lacks dedicated Brinzolamide safety data; systemic absorption of topically applied CAIs in this age group carries a risk of metabolic acidosis. Furthermore, the TxGNN model's high prediction score reflects strong connectivity between "glaucoma subtype" nodes in the knowledge graph, not direct clinical trial or publication evidence for this specific genetic condition — a critical distinction when interpreting the result for clinical decision-making.

---

## Clinical Trial Evidence

No clinical trials specifically investigating Brinzolamide for primary hereditary glaucoma have been identified.

> Currently no related clinical trials registered for this specific indication.

**Clinical context for prescribers:** While no trials exist for primary hereditary glaucoma specifically, one paediatric trial in the broader evidence base (NCT00061516: Betaxon vs. Azopt® in paediatric glaucoma or ocular hypertension, n=78, Phase 3, Completed) provides limited but relevant reference data for Brinzolamide use in children. Extensive Phase 3 RCT evidence supporting Brinzolamide in adult open-angle glaucoma is available under the related indications ranked 2–4 in this pack (trials up to n=1,184 participants, multiple global sites).

---

## Literature Evidence

No publications specifically investigating Brinzolamide for primary hereditary glaucoma have been identified.

> Currently no related literature available for this specific indication.

---

## Australia Market Information

Brinzolamide currently has **no ARTG (Australian Register of Therapeutic Goods) registration** and is not approved for any indication in Australia.

> Prescribing Brinzolamide in Australia would require approval through the TGA's Special Access Scheme (SAS) or the Authorised Prescriber pathway. Until TGA registration is obtained, clinicians should refer to the US FDA-approved Product Information for Azopt® 1% ophthalmic suspension or the EMA-approved Summary of Product Characteristics (SmPC) for available prescribing and safety guidance.

---

## Safety Considerations

No TGA-approved Product Information is currently available for Brinzolamide in Australia, and all safety fields in this Evidence Pack were unable to be populated from local regulatory sources. Please refer to the TGA-approved Product Information (PI) — or in its absence, the Azopt® international PI — for complete safety information.

**Key safety note from published literature:** A 2025 case report (PMID [39870471](https://pubmed.ncbi.nlm.nih.gov/39870471/)) documents topical Brinzolamide-induced ciliary body effusion presenting with secondary angle closure and myopic shift — a paradoxical adverse reaction that resolved upon drug cessation. This finding is clinically relevant for any patient group with anatomically compromised drainage angles, including congenital glaucoma patients.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite the highest TxGNN prediction score of all candidates (99.48%), there is no clinical trial or published literature evidence specifically supporting Brinzolamide for primary hereditary glaucoma (Evidence Level: L5). The prediction is driven by knowledge graph class-level pharmacological associations. Compounding this, Brinzolamide has no current TGA registration in Australia, the target population (infants and young children) lacks dedicated safety data for this agent, and surgical intervention (goniotomy/trabeculotomy) — not pharmacotherapy — remains the accepted standard of care for this condition.

**To proceed, the following is needed:**
- Obtain TGA registration or SAS/Authorised Prescriber approval before any clinical use of Brinzolamide in Australia
- Retrieve and review the complete Brinzolamide MOA and safety profile from DrugBank (data gap DG002 — high priority)
- Obtain and parse the international Product Information (Azopt® FDA PI or EMA SmPC) for full warnings, contraindications, and any available paediatric use data (data gap DG001 — blocking)
- Conduct a targeted systematic literature review on topical CAI use in paediatric and congenital glaucoma populations, with specific focus on systemic absorption and metabolic acidosis risk in neonates and infants
- Consult a paediatric ophthalmologist regarding the appropriate adjunctive role of medical IOP-lowering therapy in primary hereditary glaucoma in the context of the surgical treatment algorithm
- If broader TGA registration for adult open-angle glaucoma is being considered (supported by L1 evidence across ranks 2–4), a separate regulatory pathway and report would be appropriate given the substantially stronger evidence base for that indication

---

> ⚠️ **Disclaimer:** This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All prescribing decisions should be made in accordance with TGA-approved indications and current clinical guidelines.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

