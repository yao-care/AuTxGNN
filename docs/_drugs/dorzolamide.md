---
layout: default
title: Dorzolamide
parent: 僅模型預測 (L5)
nav_order: 166
evidence_level: L5
indication_count: 10
---

# Dorzolamide
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

# Dorzolamide: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Dorzolamide is a topical carbonic anhydrase inhibitor (CAI) established globally for lowering intraocular pressure (IOP) in open-angle glaucoma and ocular hypertension, though it is not currently registered in Australia.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**,
with **1 completed Phase 2 clinical trial** (n=37) and **no peer-reviewed publications** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Open-angle glaucoma and ocular hypertension (established global use; not currently registered in Australia) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. However, based on well-established pharmacological knowledge, Dorzolamide is a selective inhibitor of carbonic anhydrase II (CA-II) in the ciliary body epithelium. By blocking CA-II, it reduces bicarbonate secretion into the posterior chamber, which suppresses aqueous humour production and lowers IOP by approximately 17–26%. This mechanism is direct, well-characterised, and has been replicated across decades of clinical use in open-angle glaucoma — a condition in which chronically elevated IOP drives progressive optic nerve damage.

Primary hereditary glaucoma (including congenital and juvenile-onset forms associated with mutations such as CYP1B1 or MYOC) shares the same core pathological driver: elevated IOP causing irreversible optic neuropathy. Since Dorzolamide acts specifically on the IOP-generating mechanism rather than on a disease-specific molecular target, its mechanistic rationale extends naturally to hereditary glaucoma. This is further supported by clinical practice, where Dorzolamide is already used in paediatric glaucoma patients as adjunctive therapy following surgical failure — precisely the population studied in the one identified trial.

It is important to note, however, that hereditary glaucoma often involves structural developmental anomalies of the trabecular meshwork (e.g., trabeculodysgenesis in congenital glaucoma), meaning that IOP elevation may be less amenable to purely pharmacological management compared to adult open-angle glaucoma. Whether CAI-mediated IOP reduction achieves equivalent optic nerve protection in genetically-defined subtypes requires dedicated larger-scale research. Notably, TxGNN also assigns high confidence scores to Dorzolamide for broader open-angle glaucoma indications (ranks 6 and 7), for which an extensive body of Phase 3 evidence already exists — reinforcing the biological plausibility of the hereditary glaucoma prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Phase 2 | Completed | 37 | Compared IOP-lowering efficacy of latanoprost (prostaglandin analogue) versus dorzolamide (CAI) in paediatric primary hereditary glaucoma refractory to surgical procedures; both drugs assessed for safety. The protocol was amended mid-study, reducing the target from 96 to 68 eyes. Small sample size and single-trial status limit generalisability, but this is the most direct available clinical evidence for this indication. |

---

## Literature Evidence

Currently no related literature available specifically for primary hereditary glaucoma and Dorzolamide.

---

## Australia Market Information

Dorzolamide is **not currently registered on the Australian Register of Therapeutic Goods (ARTG)**. There are no ARTG entries for this drug. Clinicians wishing to prescribe Dorzolamide in Australia would need to access it via the **TGA Special Access Scheme (SAS) – Category B** or through the **Authorised Prescriber** pathway, both of which require individual clinical justification.

Internationally, Dorzolamide (Trusopt®) and its fixed combination with timolol (Cosopt®) are approved in jurisdictions including the USA (FDA), European Union (EMA), and Japan (PMDA) for open-angle glaucoma and ocular hypertension. This regulatory status in comparable markets may support a future TGA submission.

---

## Safety Considerations

Please refer to the TGA Special Access Scheme documentation or international equivalent product labelling (e.g., FDA prescribing information for Trusopt®/Cosopt®) for complete safety information, as no TGA-approved Product Information is currently available.

Based on internationally available information, clinicians should be aware of the following considerations:

- **Sulfonamide class**: Dorzolamide is a sulfonamide derivative. Patients with known sulfonamide hypersensitivity should be evaluated carefully before use.
- **Renal impairment**: Dorzolamide and its metabolite accumulate in red blood cells and are renally excreted; it is generally not recommended in patients with severe renal impairment (CrCl < 30 mL/min) per international labelling.
- **Corneal endothelium**: Long-term topical use may have implications for corneal endothelial function, particularly in patients with pre-existing corneal disease — a relevant consideration in paediatric hereditary glaucoma management.
- **Paediatric use**: The identified trial population comprised paediatric patients; age-appropriate dosing and safety monitoring should follow international paediatric ophthalmology guidelines.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the mechanistic basis for Dorzolamide in primary hereditary glaucoma is biologically plausible — shared IOP-lowering pathway, and direct clinical precedent in paediatric glaucoma management — the available evidence is limited to a single small Phase 2 trial (n=37) with no supporting peer-reviewed literature specific to hereditary glaucoma. Furthermore, the drug is not registered in Australia, creating a regulatory barrier to routine clinical use.

**To proceed, the following is needed:**

- **Regulatory pathway**: Initiate TGA Special Access Scheme (Category B) application or explore a formal ARTG registration submission, citing FDA/EMA approvals as comparable overseas regulatory evidence
- **Clinical evidence**: Conduct or identify Phase 2/3 randomised controlled trials specifically designed for primary hereditary glaucoma subtypes (congenital, juvenile-onset) with adequate sample sizes and long-term optic nerve endpoints
- **Genotype-stratified analysis**: Investigate whether specific genetic subtypes (e.g., CYP1B1 vs. MYOC mutations) predict differential IOP response to CAI therapy
- **Safety documentation**: Obtain TGA-approved Product Information (or equivalent) to confirm warnings, contraindications, and drug interactions for Australian clinical governance purposes
- **MOA confirmation**: Retrieve formal DrugBank mechanistic data to complete the mechanistic justification file
- **Paediatric considerations**: Confirm age-appropriate formulations are accessible via Australian importation or compounding pathways, given the predominantly paediatric nature of primary hereditary glaucoma

> **Research disclaimer**: This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. Healthcare professionals should exercise independent clinical judgement and refer to approved product labelling.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

