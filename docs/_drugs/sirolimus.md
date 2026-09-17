---
layout: default
title: Sirolimus
parent: High Evidence (L1-L2)
nav_order: 633
evidence_level: L2
indication_count: 10
---

# Sirolimus
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

Using the drug-repurposing report template supplied in the prompt — no additional skill fits this task (it's a direct content-generation job against the given Evidence Pack format), so I'm following the template's structure directly.

# Sirolimus: From Organ Transplant Rejection Prophylaxis to Liposarcoma

## One-Sentence Summary

Sirolimus is an mTOR-inhibitor immunosuppressant originally used to prevent rejection after organ (kidney) transplantation. The TxGNN model predicts it may also be effective for **Liposarcoma**, with **5 clinical trials** and **12 publications** currently supporting this direction — though the drug is not currently registered in Australia and key safety documentation is unavailable.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prophylaxis of organ (renal) transplant rejection — not captured in this evidence pack's Australian licence data; based on known drug information |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data was not returned for this candidate. Based on known information, sirolimus (rapamycin) is a macrolide mTOR (mammalian target of rapamycin) inhibitor, originally developed and approved as an immunosuppressant for renal transplant rejection prophylaxis. Mechanistically, mTOR is a central regulator of cell growth, proliferation and survival — the same pathway implicated in tumour growth.

The connection to liposarcoma is supported by two lines of evidence in the pack. First, dedifferentiated liposarcoma tumour tissue shows constitutive activation of the Akt-mTOR and MAPK pathways (PMID 26518767), providing a direct molecular rationale for mTOR blockade in this cancer. Second, sirolimus itself (not just its analogues) has already been trialled directly in liposarcoma: NCT02821507 combined sirolimus with cyclophosphamide in metastatic/unresectable myxoid liposarcoma and chondrosarcoma. Related mTOR inhibitors in the same drug class — temsirolimus, everolimus, and ridaforolimus — have also been tested in advanced sarcoma populations that include liposarcoma subtypes, reinforcing the plausibility of the class effect even though most of the direct clinical evidence to date uses sirolimus analogues rather than sirolimus itself.

Separately, real-world transplant data (PMID 16434506) show that sirolimus reduces rather than promotes cancer incidence compared with calcineurin inhibitors, which is consistent with — though not proof of — an antitumour mechanism that could extend to soft-tissue sarcomas.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | Single-arm trial of sirolimus + cyclophosphamide in metastatic/unresectable myxoid liposarcoma and chondrosarcoma; direct sirolimus use in this indication (Relevance grade A) |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Ribociclib + everolimus (an mTOR inhibitor, not sirolimus) in advanced dedifferentiated liposarcoma and leiomyosarcoma |
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | Completed | 24 | Temsirolimus (Torisel, an mTOR inhibitor) + liposomal doxorubicin in advanced soft tissue and bone sarcomas, including liposarcoma |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | Completed | 46 | Cixutumumab + temsirolimus in paediatric recurrent/refractory solid tumours (sarcoma); paediatric population, not liposarcoma-specific |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Phase 2 | Completed | 216 | Ridaforolimus (AP23573, an mTOR inhibitor analogue) in advanced sarcoma, including liposarcoma subtypes |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | RCT | Clinical Cancer Research | Phase II trial of ribociclib + everolimus (CDK4 + mTOR inhibition) in dedifferentiated liposarcoma and leiomyosarcoma |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Cohort | Tumour Biology | Akt-mTOR and MAPK pathway activation demonstrated in 99 dedifferentiated liposarcoma specimens, with in vitro mTOR inhibitor antitumour activity |
| [37400145](https://pubmed.ncbi.nlm.nih.gov/37400145/) | 2023 | Cohort | Cancer Genomics & Proteomics | Chloroquine + rapamycin combination effective against well-differentiated liposarcoma via autophagy inhibition |
| [36309387](https://pubmed.ncbi.nlm.nih.gov/36309387/) | 2022 | Cohort | In Vivo | Chloroquine + rapamycin arrests tumour growth in a dedifferentiated liposarcoma patient-derived xenograft mouse model |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Review | Cancers | Overview of novel targeted therapeutics in soft tissue sarcoma, including mTOR-pathway agents |
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | Cohort | JASN | Randomised renal transplant trial: sirolimus after cyclosporine withdrawal reduces cancer risk versus continued cyclosporine |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Review | Current Opinion in Oncology | Review of new molecular-targeted agents in clinical trials for advanced sarcomas |
| [26093731](https://pubmed.ncbi.nlm.nih.gov/26093731/) | 2015 | Cohort | Transplantation Proceedings | Cancer screening study in renal transplant recipients on long-term immunosuppression, including mTOR inhibitors |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bulletin du Cancer | Review of targeted treatments for rare connective tissue tumours and sarcomas by molecular subgroup |
| [25519700](https://pubmed.ncbi.nlm.nih.gov/25519700/) | 2015 | Preclinical | Molecular Cancer Therapeutics | MLN0128, an ATP-competitive mTOR kinase inhibitor, shows potent antitumour activity in bone and soft-tissue sarcoma models |

## Australia Market Information

According to this evidence pack, sirolimus currently has **no ARTG (Australian Register of Therapeutic Goods) entries** — market status is recorded as **not marketed**, with 0 total licences on file. Any clinical use in Australia would need to proceed through an alternative access pathway (e.g., Special Access Scheme or Authorised Prescriber) rather than a standard PBS/TGA-registered product, and would need TGA-equivalent product information to be sourced separately.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. This evidence pack could not retrieve key warnings, contraindications, or drug interaction data for sirolimus — including a flagged **blocking data gap** on locally-registered product warnings/contraindications, since the drug is not currently marketed in this jurisdiction.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The strongest direct evidence is a single completed Phase 2, single-arm trial (NCT02821507) rather than a comparative RCT, and most of the supporting sarcoma trial data uses sirolimus *analogues* (everolimus, temsirolimus, ridaforolimus) rather than sirolimus itself. Combined with sirolimus's absence from the Australian market (0 ARTG entries) and a blocking gap in locally-relevant safety/PI data, this candidate is not yet ready for a Go or Guardrails decision.

**To proceed, the following is needed:**
- TGA-equivalent Product Information (warnings, contraindications, drug interactions) — currently a blocking data gap
- Confirmed DrugBank mechanism-of-action and drug classification data
- Clarification of an access pathway for an unregistered product (e.g., Special Access Scheme) if clinical use is contemplated
- Follow-up on maturing results from the ongoing/completed mTOR-inhibitor sarcoma trials to strengthen the sirolimus-specific evidence base
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

