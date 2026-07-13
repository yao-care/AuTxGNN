---
layout: default
title: Isoniazid
parent: 僅模型預測 (L5)
nav_order: 276
evidence_level: L5
indication_count: 10
---

# Isoniazid
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

# Isoniazid: From Tuberculosis to Conjunctivitis

## One-Sentence Summary

Isoniazid (INH) is a foundational first-line antituberculosis agent with over 70 years of clinical use for the treatment and prevention of *Mycobacterium tuberculosis* infection.
The TxGNN model predicts it may be effective for **Conjunctivitis**, with **1 clinical trial** and **20 publications** identified in support — the majority being historical case reports of tuberculous conjunctivitis managed as part of standard TB therapy.
Overall, this prediction represents an extension of the existing anti-TB indication to an ocular anatomical site rather than a genuinely novel application.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Tuberculosis (treatment and prevention) |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed (no ARTG entries identified) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the DrugBank record associated with this evidence pack. Based on well-established pharmacological knowledge, Isoniazid is a prodrug activated by the mycobacterial catalase-peroxidase enzyme KatG. The active species then inhibits InhA (enoyl-acyl carrier protein reductase) — an enzyme critical to mycolic acid biosynthesis. Mycolic acids are essential structural components of the *Mycobacterium tuberculosis* cell wall, and their disruption leads to bactericidal activity. This mechanism is highly specific to the *Mycobacteriaceae* family.

The link between isoniazid and conjunctivitis is anatomical rather than mechanistic. The predicted indication most likely refers to **tuberculous conjunctivitis** — direct infection of the ocular conjunctiva by *M. tuberculosis* — or **phlyctenular keratoconjunctivitis**, a well-recognised hypersensitivity reaction to mycobacterial antigens occurring in individuals with active or prior TB. Historical literature from the 1950s to 1970s documented isoniazid as part of antituberculosis regimens in managing these ocular manifestations, and a 1965 controlled study (PMID 14253168) specifically examined isoniazid prophylaxis for reducing phlyctenular keratoconjunctivitis incidence in high-risk populations.

It is important to note that this constitutes an **extension of the original TB indication to an ocular site**, not a novel repurposing pathway. The TxGNN knowledge graph likely captures this association through co-occurrence of "infection", "mycobacterium", and "conjunctival disease" nodes, which inflates the topological prediction score. Isoniazid is already incorporated into standard antituberculosis regimens used to treat tuberculous conjunctivitis; a dedicated new-indication development programme is not required for this application.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04094012](https://clinicaltrials.gov/study/NCT04094012) | Phase 3 | Completed | 490 | Pragmatic multicentre RCT comparing 3HP (weekly high-dose rifapentine + isoniazid × 12 doses) versus 1HP (daily rifapentine + isoniazid × 28 days) for latent TB infection (LTBI) prevention. Conjunctivitis was not a primary endpoint; this trial provides safety and tolerability data for INH-containing LTBI regimens but offers only indirect background evidence for the predicted indication. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [14253168](https://pubmed.ncbi.nlm.nih.gov/14253168/) | 1965 | Clinical Study | Am Rev Respir Dis | Isoniazid prophylaxis significantly reduced the incidence of phlyctenular keratoconjunctivitis among Alaskan Eskimo children with high TB exposure — the most direct evidence for INH preventing a conjunctival TB complication. |
| [5103251](https://pubmed.ncbi.nlm.nih.gov/5103251/) | 1971 | Clinical Study | Ann Oculist | Examined local (topical and systemic) use of isoniazid in treating ocular tuberculosis, including conjunctival involvement; early supporting evidence for INH efficacy at the ocular site. |
| [33607832](https://pubmed.ncbi.nlm.nih.gov/33607832/) | 2021 | Case Report | Medicine | Paediatric patient with primary sinonasal tuberculosis presenting as phlyctenular keratoconjunctivitis; resolved with standard anti-TB therapy (including isoniazid), illustrating TB as a current cause of conjunctival disease. |
| [26692731](https://pubmed.ncbi.nlm.nih.gov/26692731/) | 2015 | Case Report | Middle East Afr J Ophthalmol | Tuberculous conjunctivitis in an anophthalmic socket in a woman with prior miliary TB; managed successfully with antituberculosis drugs including INH. |
| [17133069](https://pubmed.ncbi.nlm.nih.gov/17133069/) | 2006 | Case Report | Cornea | *M. tuberculosis* presenting as chronic red eye and conjunctivitis confirmed on biopsy; responded to standard TB treatment incorporating isoniazid. |
| [10641112](https://pubmed.ncbi.nlm.nih.gov/10641112/) | 1999 | Observational | Oftalmologia | 28 cases of tuberculous keratoconjunctivitis, including 13 children with primary TB — all had positive tuberculin tests and radiological TB evidence, reinforcing the mycobacterial aetiology. |
| [25433746](https://pubmed.ncbi.nlm.nih.gov/25433746/) | 2014 | Case Series | Can J Ophthalmol | Conjunctival phlyctenulosis as a presenting sign of impending clinical tuberculosis; authors advocate early initiation of TB treatment including INH upon diagnosis. |
| [14089390](https://pubmed.ncbi.nlm.nih.gov/14089390/) | 1964 | Case Report | Arch Ophthalmol | Historical case series of primary tuberculosis of the conjunctiva, demonstrating that conjunctival TB can occur without systemic TB and responds to antituberculosis agents. |
| [32674602](https://pubmed.ncbi.nlm.nih.gov/32674602/) | 2020 | Case Report | Clin Pediatrics | Unexpected mycobacterial cause of conjunctivitis identified in an adolescent; highlights the need to consider TB aetiology in atypical or treatment-refractory conjunctivitis. |
| [1363080](https://pubmed.ncbi.nlm.nih.gov/1363080/) | 1992 | Review | Optom Clin | Review of ocular adverse effects of systemic drugs; notes conjunctivitis and blepharoconjunctivitis associated with antineoplastic agents, sulfonamides, and isotretinoin — contextual background for drug-related ocular disease. |

---

## Australia Market Information

No ARTG (Australian Register of Therapeutic Goods) entries for Isoniazid were identified in this evidence pack. Isoniazid is an WHO Essential Medicine and is recognised internationally as a core component of first-line TB treatment regimens (HRZE/HR). In Australia, access may be available via the **TGA Special Access Scheme (SAS Category B)** or through state-based TB services and hospital formularies. Clinicians requiring this medicine should contact the TGA or their institutional pharmacy.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

> **Prescriber note**: Isoniazid has well-documented safety concerns established in the global literature, including hepatotoxicity (risk increases with age and concurrent alcohol use), peripheral neuropathy secondary to vitamin B6 (pyridoxine) antagonism — pyridoxine co-prescription is standard practice — and drug interactions with rifampicin, phenytoin, and other hepatotoxic agents. These are not formally derived from the data fields of this evidence pack but are integral to clinical decision-making.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for isoniazid in conjunctivitis reflects the drug's **existing** anti-TB activity applied to tuberculous conjunctivitis — an ocular manifestation of *M. tuberculosis* infection — rather than a novel therapeutic mechanism or indication. Isoniazid is already the standard of care in this setting as part of TB combination regimens. The evidence base consists entirely of historical case reports and observational data (L4), with no dedicated clinical trials examining isoniazid specifically for conjunctivitis as a standalone target.

**To proceed, the following is needed:**

- **Clarify the clinical question**: If the intent is to treat *tuberculous* conjunctivitis, this is already standard practice within existing TB regimens — no repurposing programme is warranted
- **If non-tuberculous conjunctivitis is the target**: Mechanistic justification and preclinical evidence are required, as no relevant data currently exists and INH's antimicrobial spectrum does not extend to the common causative organisms (adenovirus, *S. pneumoniae*, *H. influenzae*)
- **Confirm TGA access pathway**: Identify whether an ARTG entry exists under alternative product names, or establish an SAS application process for Australian clinical use
- **Obtain TGA Product Information**: Formal safety, contraindication, and DDI data are unavailable in this evidence pack and must be sourced prior to any clinical evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

