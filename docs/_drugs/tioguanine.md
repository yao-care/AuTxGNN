---
layout: default
title: Tioguanine
parent: 僅模型預測 (L5)
nav_order: 677
evidence_level: L5
indication_count: 10
---

# Tioguanine
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

Using the drug-repurposing-report skill implicitly embedded in this task's system prompt (structured template) — proceeding directly per the specified format.

# Tioguanine: From Acute Leukaemia to Chronic Myelogenous Leukemia, BCR-ABL1 Positive

## One-Sentence Summary

Tioguanine (6-thioguanine) is a purine antimetabolite historically used in the treatment of acute leukaemia. The TxGNN model predicts it may be effective for **Chronic Myelogenous Leukemia, BCR-ABL1 Positive**, with **2 clinical trials** and **20 publications** identified, though most of this evidence is indirect (background chemotherapy in combination regimens or historical cohort data from the 1960s–1990s) rather than trials testing tioguanine directly against this indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute leukaemia (based on known pharmacology of thiopurine antimetabolites; no Australian ARTG-approved indication text is available, as the product is not marketed) |
| Predicted New Indication | Chronic Myelogenous Leukemia, BCR-ABL1 Positive |
| TxGNN Prediction Score | 98.88% |
| Evidence Level | L3 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate. Based on known pharmacology, tioguanine is a purine (thiopurine) analogue that is metabolised intracellularly to thioguanine nucleotides, which are incorporated into DNA and RNA, inhibiting purine synthesis and inducing cell-cycle arrest and apoptosis in rapidly dividing cells. Its efficacy in acute leukaemia (particularly acute myeloid leukaemia) is well established from decades of clinical use.

Chronic myelogenous leukaemia (BCR-ABL1 positive) and acute leukaemia share the same underlying vulnerability — rapidly proliferating myeloid precursor cells — which is mechanistically compatible with an antimetabolite approach. Notably, the literature evidence pack shows that 6-thioguanine has genuine historical precedent in this exact indication: it was one of the first agents used for "chronic granulocytic leukaemia" (the older name for CML) as far back as the 1950s–1960s, and later appeared as a component of combination regimens (e.g., DAT: daunorubicin + cytarabine + thioguanine) used in blast-phase CML and AML/MDS induction therapy — well before tyrosine kinase inhibitors (TKIs, e.g., imatinib) became standard of care in 1998.

The prediction is therefore mechanistically and historically plausible, but it should be understood as a **reintroduction of a superseded therapy** rather than a novel discovery. Current standard-of-care for BCR-ABL1-positive CML is TKI therapy; tioguanine's plausible modern role, if any, would be as an adjunct in TKI-resistant or blast-phase disease, which is a materially different clinical use-case than first-line treatment.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03007147](https://clinicaltrials.gov/study/NCT03007147) | Phase 3 | Active, not recruiting | 475 | Tests imatinib combined with two different chemotherapy backbones in newly diagnosed Ph+ ALL. **Relevance: Low (Grade C)** — does not test tioguanine directly; included only because BCR-ABL1-positive disease overlaps. |
| [NCT06124157](https://clinicaltrials.gov/study/NCT06124157) | Phase 3 | Recruiting | 222 | Tests blinatumomab with dasatinib/imatinib and standard chemotherapy in Ph+/Ph-like B-ALL. **Relevance: Low (Grade C)** — TKI/immunotherapy-focused, tioguanine not a study drug. |

*Neither trial directly evaluates tioguanine; both are included in the evidence pack due to shared BCR-ABL1-positive disease biology.*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [13726513](https://pubmed.ncbi.nlm.nih.gov/13726513/) | 1960 | Cohort | Clin Pharmacol Ther | Original report of 6-mercaptopurine, thioguanine and 6-chloropurine in chronic granulocytic leukaemia (historical foundation for this indication). |
| [7769838](https://pubmed.ncbi.nlm.nih.gov/7769838/) | 1995 | Phase I Trial | Leukemia | Continuous IV infusion 6-TG in relapsed/refractory acute leukaemia, including blast-phase CGL; dose-limiting stomatitis, MTD 120 mg/m²/day. |
| [1869245](https://pubmed.ncbi.nlm.nih.gov/1869245/) | 1991 | Cohort | Hematol Oncol | Oral ETI regimen (etoposide + 6-thioguanine + idarubicin) for induction of advanced acute leukaemia, including myeloid blast crisis of CML. |
| [1958475](https://pubmed.ncbi.nlm.nih.gov/1958475/) | 1991 | RCT (MRC CML trial) | Br J Haematol | MRC CML II trial (busulphan vs busulphan+thioguanine, n=675): thioguanine combination significantly increased non-cirrhotic portal hypertension and ascites — an important safety signal. |
| [2660927](https://pubmed.ncbi.nlm.nih.gov/2660927/) | 1989 | Cohort | Blut | DAT (daunomycin + cytarabine + 6-thioguanine) vs DAV regimen for myeloid blast crisis of CML; 89% blast-clearance response rate, but only 2/9 achieved marrow aplasia with recovery. |
| [1537081](https://pubmed.ncbi.nlm.nih.gov/1537081/) | 1992 | Cohort | Cancer Chemother Pharmacol | Non-aggressive vincristine/cytarabine/thioguanine regimen in 40 patients with CML in blastic transformation; modest remission rates (17–30%), myelosuppression was major toxicity. |
| [15747786](https://pubmed.ncbi.nlm.nih.gov/15747786/) | 2005 | Review | Clin Lab Sci | Historical review of CML therapy milestones, noting 6-thioguanine/busulphan (1953) as an early treatment era prior to TKIs. |
| [15914554](https://pubmed.ncbi.nlm.nih.gov/15914554/) | 2005 | Mechanistic study | Blood | BCR-ABL kinase domain mutation analysis in imatinib-naive CML patients — background biology relevant to disease/TKI-resistance context, not thioguanine-specific. |
| [8098047](https://pubmed.ncbi.nlm.nih.gov/8098047/) | 1993 | In vitro study | J Clin Invest | K562 CML blast cell line drug-resistance study; cytotoxic drug sensitivity data relevant to blast-phase disease biology. |
| [9372003](https://pubmed.ncbi.nlm.nih.gov/9372003/) | 1995 | Review | Curr Opin Hematol | General review of acute leukaemia in children; broader context only, not CML/thioguanine-specific. |

## Australia Market Information

Tioguanine is currently **not marketed** in Australia and has **no ARTG entries**. No product information, brand names, or approved indications are available from Australian regulatory records for this evidence pack.

## Cytotoxicity

Tioguanine is a conventional cytotoxic chemotherapy agent (thiopurine/purine antimetabolite class), meeting the antineoplastic criteria based on its established mechanism and historical use in acute leukaemia.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (thiopurine/purine antimetabolite) |
| Myelosuppression Risk | High — dose-limiting stomatitis and haematological toxicity (leucopenia, thrombocytopenia) reported at doses ≥120 mg/m²/day; grade III/IV cytopenias documented in head and neck cancer trial (PMID 1500270) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Full blood count (FBC) with differential, liver function tests, and monitoring for hepatotoxicity/veno-occlusive disease — the MRC CML trial (PMID 1958475) found thioguanine combination therapy significantly increased non-cirrhotic portal hypertension and ascites, a notable long-term hepatic safety signal specific to this drug |
| Handling Protection | Must follow cytotoxic drug handling regulations (personal protective equipment, closed-system transfer where applicable, dedicated waste disposal) |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Detailed warnings, contraindications, and drug interaction data are not currently available in this evidence pack (this is a Blocking data gap — see Conclusion below).

Note: historical literature (PMID 1958475, 2332518) independently identifies a clinically significant hepatic toxicity signal — non-cirrhotic portal hypertension — associated with thioguanine, particularly in combination regimens. This should be specifically confirmed against the current PI once available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for this indication is Level 3 (observational/historical cohort data, no modern controlled trials), the drug is not currently marketed in Australia, and a Blocking data gap exists for TFDA/TGA-equivalent safety labelling (warnings and contraindications), which prevents initial safety screening (S1). The proposed indication also represents reintroduction of a therapy that has been superseded by TKIs as standard of care for BCR-ABL1-positive CML.

**To proceed, the following is needed:**
- TGA-approved Product Information (PI), including warnings, contraindications, and drug interaction data (Blocking gap)
- Confirmed mechanism of action documentation from DrugBank or equivalent source
- Clarification of the intended clinical niche (e.g., TKI-resistant or blast-phase CML) given that first-line TKI therapy is standard of care
- Assessment of the hepatotoxicity/portal hypertension signal identified in historical MRC trial data before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

