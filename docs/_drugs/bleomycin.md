---
layout: default
title: Bleomycin
parent: 僅模型預測 (L5)
nav_order: 93
evidence_level: L5
indication_count: 10
---

# Bleomycin
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

# Bleomycin: From Conventional Cancer Chemotherapy to Cauda Equina Neoplasm

## One-Sentence Summary

Bleomycin is a glycopeptide antibiotic-derived cytotoxic agent, internationally established as a component of combination chemotherapy regimens for Hodgkin lymphoma (ABVD) and germ cell tumours (BEP), though it is not currently registered on the Australian Register of Therapeutic Goods (ARTG).
The TxGNN model predicts it may be effective for **Cauda Equina Neoplasm**, with **0 clinical trials** and **3 publications** currently supporting this specific direction.
Evidence is entirely indirect — this prediction is based on knowledge graph topology rather than direct clinical data, and the overall recommendation is **Hold** pending meaningful preclinical and clinical evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Australia; internationally used in Hodgkin lymphoma (ABVD), testicular/ovarian germ cell tumours (BEP), and squamous cell carcinomas |
| Predicted New Indication | Cauda Equina Neoplasm |
| TxGNN Prediction Score | 99.30% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed (no ARTG entries) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, bleomycin is a glycopeptide antibiotic that induces both single- and double-strand DNA breaks by chelating ferrous iron and generating reactive oxygen species, with preferential activity at the G₂/M phase of the cell cycle. This DNA strand-breaking mechanism underpins its antineoplastic activity across multiple tumour types characterised by rapid proliferation and impaired DNA repair.

Cauda equina neoplasms are a heterogeneous group arising at or below the conus medullaris — most commonly myxopapillary ependymomas, nerve sheath tumours (schwannomas, neurofibromas), and metastatic deposits. Theoretically, rapidly proliferating cauda equina tumours with deficient G₂/M checkpoint function could exhibit sensitivity to bleomycin's DNA-damaging mechanism. A specific biological rationale exists for cauda equina involvement by lymphoma: when lymphoma (e.g., Hodgkin or aggressive non-Hodgkin) involves the cauda equina, bleomycin-containing regimens such as ABVD are biologically appropriate, as evidenced by one of the supporting publications.

However, three critical limitations undermine this prediction as a standalone repurposing candidate: (1) bleomycin has very limited blood–CSF penetration, representing a major pharmacokinetic barrier for any CNS or spinal cord tumour; (2) none of the three supporting publications directly investigates bleomycin in cauda equina tumours — all are indirect references; and (3) the high TxGNN score likely reflects network topology connectivity via shared lymphoma pathways rather than direct mechanistic or clinical evidence specific to this anatomical site.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for bleomycin in cauda equina neoplasm.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|------|------|
| [1720278](https://pubmed.ncbi.nlm.nih.gov/1720278/) | 1991 | Retrospective Cohort | Am J Clin Oncol | CNS involvement evaluated in 277 consecutive aggressive NHL patients treated by Nebraska Lymphoma Study Group; one cauda equina case identified at autopsy. Bleomycin-containing regimens were used in this NHL cohort — indirect relevance only |
| [9440744](https://pubmed.ncbi.nlm.nih.gov/9440744/) | 1998 | Retrospective Series | J Clin Oncol | Evaluated radiotherapy as salvage for CNS germinoma relapsing after primary PEB (carboplatin, etoposide, bleomycin) chemotherapy in a multicentre trial; cauda equina not the primary focus — indirect relevance |
| [31142709](https://pubmed.ncbi.nlm.nih.gov/31142709/) | 2019 | Case Report | Clin Neurology | 17-year-old man with Hodgkin lymphoma presenting with paraneoplastic sensory neuropathy; post-contrast MRI showed enhancement of both trigeminal nerves and the cauda equina; treated with IVIG and subsequent Hodgkin therapy (likely containing bleomycin) — highly indirect relevance |

---

## Australia Market Information

Bleomycin is not currently registered on the Australian Register of Therapeutic Goods (ARTG). No ARTG entries are available for any bleomycin-containing product.

Australian prescribers wishing to use bleomycin for an approved international indication would need to apply through the TGA **Special Access Scheme (SAS Category B or C)** or seek **Authorised Prescriber** status. Internationally, bleomycin is available under various brand names (e.g., Blenoxane) for:

- Hodgkin lymphoma (component of ABVD and other regimens)
- Testicular and ovarian germ cell tumours (component of BEP)
- Squamous cell carcinomas (head and neck, cervix)
- Malignant pleural effusion (intrapleural sclerosing agent)

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — glycopeptide antibiotic class; mechanism: DNA strand-breaking via free radical generation |
| Myelosuppression Risk | Low (bleomycin is notably bone marrow-sparing — a clinically important differentiating feature from most cytotoxics; myelosuppression is rarely dose-limiting) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Pulmonary function tests (PFTs) including DLCO before initiation and after every 2 cycles; cumulative lifetime dose tracking (maximum 400 units — exceeding this significantly increases pulmonary toxicity risk); FBC, renal function (dose reduction required if GFR <50 mL/min; bleomycin is renally cleared) |
| Handling Protection | Must be handled according to cytotoxic drug handling regulations (e.g., SHPA guidelines); standard cytotoxic PPE required during preparation and administration; reconstitution in a dedicated cytotoxic safety cabinet |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

> When applying for bleomycin via the TGA Special Access Scheme, prescribers should review the manufacturer's current PI for comprehensive warnings. Key safety domains requiring attention include pulmonary toxicity (bleomycin pulmonary toxicity, BPT — incidence 10–40%, potentially fatal), acute hyperpyrexic reactions (particularly with first dose in lymphoma patients; test dosing is recommended), cumulative dose limits, and renal dose adjustment requirements.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.30%), the evidence for bleomycin in cauda equina neoplasm is exclusively model-based (L5) — no clinical trials have been conducted, and the three supporting publications provide only highly indirect, contextual evidence involving other tumour types and other anatomical sites.

**To proceed, the following is needed:**

- **Pharmacokinetic data**: Establish bleomycin's CNS/CSF penetration profile — this is the most critical gap, as the blood–CSF barrier likely prevents adequate drug delivery to cauda equina tumours via systemic administration
- **Tumour subtype clarification**: Identify which cauda equina neoplasm subtypes are biologically plausible targets (e.g., lymphomatous involvement vs. primary ependymoma vs. schwannoma), as these have fundamentally different biology and treatment contexts
- **Mechanism of action documentation**: Obtain full MOA data from DrugBank (DB00290) or peer-reviewed sources to support mechanistic rationale
- **Safety profile review**: Obtain complete PI documentation via TGA SAS application before any clinical consideration
- **Intrathecal/intratumoral delivery assessment**: If systemic delivery is not viable, consider whether intrathecal or intratumoral administration (noting Phase I precedent in glioblastoma: PMID 12416544) could bypass the blood–CSF barrier — this would require dedicated study
- **Escalation to L4 evidence**: A structured preclinical study in a cauda equina tumour model is required before any clinical trial design can be contemplated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

