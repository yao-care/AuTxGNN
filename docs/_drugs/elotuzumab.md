---
layout: default
title: Elotuzumab
parent: 僅模型預測 (L5)
nav_order: 182
evidence_level: L5
indication_count: 10
---

# Elotuzumab
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

# Elotuzumab: From Relapsed/Refractory Multiple Myeloma to Indolent Plasma Cell Myeloma

## One-Sentence Summary

Elotuzumab is a humanised anti-SLAMF7 (CS1) monoclonal antibody approved internationally for relapsed or refractory multiple myeloma (MM) in combination with immunomodulatory agents such as lenalidomide or pomalidomide plus dexamethasone.
The TxGNN model predicts it may be effective for **Indolent Plasma Cell Myeloma**,
with **1 clinical trial** and **2 publications** currently available to support this direction — alongside broader Phase 3 RCT evidence (ELOQUENT-2, ELOQUENT-3) for the MM disease class.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Relapsed/refractory multiple myeloma (internationally approved; not registered in Australia) |
| Predicted New Indication | Indolent Plasma Cell Myeloma |
| TxGNN Prediction Score | 98.62% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Elotuzumab is a humanised IgG1 monoclonal antibody that specifically targets SLAMF7 (also known as CS1, CRACC, or CD319), a glycoprotein highly and selectively expressed on plasma cells — including both actively proliferating myeloma cells and their more quiescent, indolent counterparts. Its therapeutic activity arises from a dual mechanism: first, it directly activates NK cells by binding to SLAMF7 on their surface, significantly enhancing antibody-dependent cellular cytotoxicity (ADCC); second, it disrupts the protective interaction between SLAMF7-expressing myeloma cells and bone marrow stromal cells, removing a key survival signal for the tumour.

The biological rationale for extending Elotuzumab to indolent plasma cell myeloma (PCM) is compelling. SLAMF7 is constitutively expressed on indolent plasma cells at levels comparable to those seen in active MM — meaning the pharmacological target is present regardless of disease tempo. Indolent PCM, while characteristically slow-growing, is increasingly understood to represent an early or low-proliferation phase on the same disease continuum as symptomatic MM, sharing key immunological vulnerabilities.

Supporting this mechanistic reasoning, the landmark ELOQUENT-2 Phase 3 RCT (N=646, relapsed/refractory MM) and ELOQUENT-3 Phase 3 RCT (N=117) have both demonstrated that Elotuzumab-based combinations significantly improve progression-free survival in MM. Although direct prospective RCT evidence specifically targeting indolent PCM is currently lacking, the underlying biology strongly supports plausibility. The TxGNN score of 98.62% reflects the tight knowledge-graph proximity between Elotuzumab's established targets and the molecular pathology of indolent plasma cell disease.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT03019666](https://clinicaltrials.gov/study/NCT03019666) | Phase 1 | Completed | 39 | Evaluated HLA-haploidentical or mismatched related donor NAM-expanded NK cell therapy (not Elotuzumab itself) in relapsed/refractory multiple myeloma and CD20+ NHL; primary endpoint was maximum tolerated dose. Provides indirect mechanistic context: demonstrates NK cell-based immunotherapy is feasible and tolerable in MM, consistent with Elotuzumab's NK-activating mechanism of action. Not direct evidence for Elotuzumab in indolent PCM. |

> **Note:** No clinical trials directly evaluating Elotuzumab in indolent plasma cell myeloma were identified. The broader ELOQUENT trial programme (ELOQUENT-2, ELOQUENT-3) established Elotuzumab efficacy in relapsed/refractory MM more broadly — these are not captured in this specific disease query but are highly relevant context.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [27610224](https://pubmed.ncbi.nlm.nih.gov/27610224/) | 2016 | Review | F1000Research | Summarises major advances in MM diagnosis and management, including revision of diagnostic criteria (formerly ultra-high-risk smouldering MM now considered treatment-requiring MM). Discusses clonal progression and evolution relevant to the indolent-to-active disease spectrum. Relevant background for understanding where indolent PCM sits within the MM disease continuum. |
| [31413971](https://pubmed.ncbi.nlm.nih.gov/31413971/) | 2017 | Observational | Journal of Patient-Centered Research and Reviews | Pilot study examining vaccination patterns in MM patients treated with immunomodulatory drugs. Highlights the immunocompromised state and infection risk in MM, providing indirect safety context for immunotherapy use in this population. Not directly about Elotuzumab efficacy. |

---

## Australia Market Information

Elotuzumab is **not currently registered on the Australian Register of Therapeutic Goods (ARTG)**. No ARTG entries are held for this product in Australia as of the data cutoff date (April 2026).

> For reference: Elotuzumab (Empliciti®) holds regulatory approval from the US FDA and EMA for relapsed/refractory multiple myeloma. Australian clinicians seeking access would currently need to pursue the TGA Special Access Scheme (SAS) or clinical trial pathways.

---

## Cytotoxicity

Elotuzumab is an antineoplastic immunotherapy agent used in the treatment of multiple myeloma. The cytotoxicity section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted immunotherapy — humanised anti-SLAMF7 IgG1 monoclonal antibody; not a conventional cytotoxic agent |
| Myelosuppression Risk | Low to moderate — lymphopenia may occur; significantly lower myelosuppression risk than conventional chemotherapy, though combination regimens (e.g., with lenalidomide) carry additional haematological effects |
| Emetogenicity Classification | Low — monoclonal antibodies carry minimal intrinsic emetogenic potential; infusion-related reactions are the primary acute concern |
| Monitoring Items | Full blood count (FBC) with differential; liver function tests; renal function; infusion reaction monitoring during and after each administration; screen for hepatitis B reactivation prior to treatment |
| Handling Protection | Standard biological/monoclonal antibody handling precautions apply; dedicated cytotoxic drug handling regulations (e.g., closed-system transfer devices) are not typically mandated for monoclonal antibodies, but local pharmacy policy should be followed |

---

## Safety Considerations

Detailed TGA-assessed safety data for Elotuzumab is not available in this Evidence Pack, as the drug is not currently registered in Australia.

Please refer to the TGA-approved Product Information (PI) — or, in the interim, the **US FDA Prescribing Information for Empliciti®** and **EMA Summary of Product Characteristics** — for complete safety information including:
- Infusion-related reactions (occur in approximately 10% of patients; pre-medication required)
- Infection risk (particularly opportunistic infections)
- Second primary malignancies
- Hepatotoxicity
- Embryo-foetal toxicity

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Elotuzumab's mechanism of action is directly and biologically plausible for indolent plasma cell myeloma — SLAMF7 is the validated pharmacological target, expressed on indolent plasma cells at comparable levels to active MM, and the ELOQUENT Phase 3 programme has robustly validated anti-SLAMF7 immunotherapy in the broader MM setting. The TxGNN prediction score of 98.62% reflects strong knowledge-graph support. However, no direct clinical trial evidence for the indolent PCM subtype has been identified, and the drug is not currently registered in Australia, warranting a guarded but proactive approach.

**To proceed, the following is needed:**

- **TGA registration pathway:** Pursue formal TGA registration (or TGA SAS Category B/C access) for compassionate or trial use in Australia; engage Bristol Myers Squibb Australia regarding regulatory strategy
- **Indication-specific trial evidence:** Identify or initiate a prospective study (ideally Phase 2 RCT) specifically evaluating Elotuzumab in indolent/smouldering PCM; review any ongoing ELOQUENT sub-studies or smouldering myeloma-specific arms
- **Mechanism of action (MOA) documentation:** Retrieve complete DrugBank/prescribing information MOA data to support formal submission dossier
- **Safety dossier:** Obtain full TGA-format safety data including TFDA/EMA PI warnings, contraindications, and drug interaction profile; the absence of this data currently blocks a formal S1 safety assessment
- **Australian patient population analysis:** Assess local MM incidence, indolent PCM prevalence, and current standard-of-care landscape to size the clinical opportunity
- **Pharmacoeconomic evaluation:** Given Empliciti's cost as a biologic, an MSAC-style health technology assessment would be required for any PBS listing consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

