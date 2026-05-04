---
layout: default
title: Avelumab
parent: 僅模型預測 (L5)
nav_order: 69
evidence_level: L5
indication_count: 10
---

# Avelumab
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

# Avelumab: From Merkel Cell Carcinoma to HHV-8 Related Tumour

## One-Sentence Summary

Avelumab (Bavencio®) is a fully human anti-PD-L1 monoclonal antibody with antibody-dependent cellular cytotoxicity (ADCC) activity, approved internationally for Merkel cell carcinoma and urothelial carcinoma maintenance therapy, but not currently registered in Australia.
The TxGNN model predicts it may be effective for **HHV-8 related tumours** (encompassing Kaposi sarcoma, primary effusion lymphoma, and multicentric Castleman disease), supported by a mechanistically plausible viral PD-L1 upregulation pathway and indirect evidence from other checkpoint inhibitors in Kaposi sarcoma, but with **no directly applicable clinical trials or published literature** currently available for this specific combination.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Merkel cell carcinoma; urothelial carcinoma (first-line maintenance therapy post-platinum chemotherapy) — FDA/EMA approved; not registered in Australia |
| Predicted New Indication | Human herpesvirus 8-related tumour (HHV-8 related tumour) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Avelumab is a fully human IgG1 anti-PD-L1 monoclonal antibody that blocks the interaction between PD-L1 on tumour cells and its receptors PD-1 and B7-1 on T cells, restoring the immune system's capacity to recognise and destroy cancer cells. Crucially, avelumab is the only currently approved PD-L1 inhibitor that retains intact Fc-region functionality, enabling natural killer (NK) cells to directly kill PD-L1-expressing tumour cells through ADCC — a mechanism not shared by atezolizumab or durvalumab. Its approved indications (Merkel cell carcinoma, urothelial carcinoma) share the biological features of high PD-L1 expression, T-cell exhaustion, and an immune-responsive tumour microenvironment.

HHV-8 related tumours — particularly Kaposi sarcoma (KS), primary effusion lymphoma (PEL), and multicentric Castleman disease (MCD) — actively exploit viral immune evasion strategies involving the PD-1/PD-L1 checkpoint. HHV-8 viral proteins can upregulate PD-L1 expression on infected tumour cells and within the surrounding immune microenvironment, creating a biologically credible target for PD-L1 blockade. The case for checkpoint inhibition in this setting is supported indirectly by the PD-1/PD-L1 inhibitor class: pembrolizumab has demonstrated an approximately 70% objective response rate in small series of HIV-associated KS, confirming that the PD-1/PD-L1 axis is functionally relevant in HHV-8-driven malignancy.

Avelumab's dual mechanism provides a theoretical advantage in this setting: HHV-8-infected tumour cells that upregulate PD-L1 simultaneously become targets for T-cell reinvigoration (via PD-L1 blockade) and NK-cell-mediated direct killing (via ADCC). However, no clinical data for avelumab specifically in HHV-8-related tumours currently exists. The prediction is classified as mechanistic/preclinical (L4) and requires prospective clinical investigation before any clinical application can be considered.

---

## Clinical Trial Evidence

Currently no clinical trials related to Avelumab in HHV-8 related tumour are registered.

---

## Literature Evidence

Currently no related literature is available for Avelumab in HHV-8 related tumour.

---

## Australia Market Information

Avelumab is **not currently registered on the Australian Register of Therapeutic Goods (ARTG)**. There are no ARTG entries for any avelumab-containing product. Australian clinicians wishing to access avelumab for an individual patient would need to apply through a TGA special access pathway prior to use:

- **Special Access Scheme (SAS) Category C**: For individual patients with a serious medical condition where no alternative registered treatment is suitable
- **Authorised Prescriber Pathway**: For clinicians seeking approval to treat a defined class of patients
- **Clinical Trial Participation**: Via an ANZCTR-registered study

Until Australian registration is obtained, the **US FDA Bavencio® Prescribing Information** and the **EMA Bavencio® Summary of Product Characteristics (SmPC)** should be used as authoritative reference documents for dosing, monitoring, and safety guidance.

---

## Cytotoxicity

Avelumab is an antineoplastic biologic approved for malignant indications (Merkel cell carcinoma and urothelial carcinoma); this section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Immune checkpoint inhibitor (fully human anti-PD-L1 IgG1 monoclonal antibody with ADCC activity; not a conventional cytotoxic chemotherapy agent) |
| Myelosuppression Risk | Low (direct bone marrow suppression is uncommon; rare immune-mediated haematological toxicities — including autoimmune haemolytic anaemia and immune thrombocytopenia — may occur as irAEs) |
| Emetogenicity Classification | Low (monoclonal antibodies have minimal direct emetic potential; infusion-related reactions are the primary acute infusion concern and may require premedication with antihistamine and paracetamol) |
| Monitoring Items | FBC with differential, LFTs (ALT/AST/bilirubin/ALP), TFTs (TSH/free T4), fasting glucose/HbA1c, serum creatinine, urinalysis, cortisol/ACTH stimulation test if adrenal insufficiency is clinically suspected |
| Handling Protection | Standard biohazard precautions for intravenous biologics; avelumab is not typically classified as a cytotoxic hazardous drug under NIOSH or SHPA guidelines — confirm local pharmacy handling classification prior to compounding and administration |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. As avelumab is not currently registered in Australia, the **US FDA Bavencio® Prescribing Information** and the **EMA Bavencio® Summary of Product Characteristics** should be consulted as interim reference documents for the full safety, contraindication, and drug interaction profile.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model identifies a mechanistically plausible link between avelumab's dual PD-L1 blockade and ADCC activity and HHV-8-related tumours, supported by indirect evidence from pembrolizumab in Kaposi sarcoma. However, no direct clinical trial or published literature evidence exists for avelumab in this indication (L4 evidence only), and avelumab has no current TGA registration in Australia — creating both an evidential and a regulatory barrier to clinical use.

**Notable finding from additional predictions:**
The TxGNN model also identifies **prostatic urethra urothelial carcinoma** (Rank 9) as a high-evidence candidate — rated **L1** based on JAVELIN Bladder 100 (Phase 3 RCT, N=700), which established avelumab's overall survival benefit in urothelial carcinoma maintenance (HR=0.76 overall; HR=0.69 in PD-L1+ subgroup, p=0.0003). Prostatic urethral UC shares the same tumour biology as the approved urothelial carcinoma indication, and the evidence supports a **Proceed with Guardrails** recommendation for this sub-indication, pending TGA access pathway resolution. Similarly, **kidney pelvis sarcomatoid transitional cell carcinoma** (Rank 10) has an observational study (NCT05431777, N=79, completed) and merits further research attention (L3 evidence).

**⚠️ Model false positives to exclude:** Ranks 5–8 (adenosine deaminase deficiency, reticular dysgenesis, immunoerythromyeloid hypoplasia, non-severe combined immunodeficiency) are assessed as knowledge graph false positives. PD-L1 inhibition has no mechanistic rationale in severe immunodeficiency and carries substantial risk of harm in these populations. These predictions should be formally excluded from further evaluation.

**To proceed with the HHV-8 related tumour indication, the following steps are required:**

- Design a prospective feasibility study or investigator-initiated trial (IIT) evaluating avelumab in HHV-8-related tumours, with Kaposi sarcoma (classic or HIV-associated) as the most tractable starting population
- Characterise biomarker landscape in HHV-8-related tumour tissue: PD-L1 expression (SP142/28-8 assay), tumour mutational burden (TMB), microsatellite instability (MSI) status, and NK-cell infiltration as an ADCC surrogate
- Assess potential pharmacokinetic and pharmacodynamic interactions with antiretroviral therapy (ART) in HIV-positive patient populations before commencing any clinical use
- Obtain detailed mechanism of action (MOA) data from DrugBank and published pharmacology literature to strengthen the mechanistic rationale
- Submit a TGA Special Access Scheme (SAS) Category C application or pursue the Authorised Prescriber pathway if individual patient access is required prior to formal trial activation
- Review current FDA and EMA Bavencio® prescribing information for full safety, dosing (800 mg IV every 2 weeks), and monitoring protocols before clinical use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

