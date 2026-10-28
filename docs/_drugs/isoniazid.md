---
layout: default
title: Isoniazid
parent: Model Prediction Only (L5)
nav_order: 393
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
monitor_inn: "Isoniazid"
predicted_indications: ["conjunctivitis"]
description: "Isoniazid: predicted new indication Conjunctivitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Isoniazid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Isoniazid: Conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Isoniazid is an antimycobacterial drug originally used to treat pulmonary tuberculosis.
The TxGNN model predicts it may be effective for **conjunctivitis**, but there are **no registered clinical trials** and the **12 publications** retrieved are mostly case reports, adverse-effect reviews and tuberculosis-related ocular reports, so the evidence is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 0.9936 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Isoniazid is a long-established antituberculosis agent. Its efficacy in pulmonary tuberculosis is well proven, and it acts against mycobacteria.

The literature does not show isoniazid treating conjunctivitis in general. It links the drug to the eye mainly through:
- Tuberculosis-related ocular disease, such as phlyctenular keratoconjunctivitis and primary conjunctival TB, where isoniazid acts through its antimycobacterial activity.
- Ocular adverse effects of systemic drugs.
- Reactive arthritis with conjunctivitis after intravesical BCG therapy.

The high TxGNN score probably reflects these TB and BCG associations rather than a general anti-conjunctivitis effect. Any benefit would be limited to a narrow, mycobacteria-driven subset of eye disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14253168](https://pubmed.ncbi.nlm.nih.gov/14253168/) | 1965 | Cohort/prophylaxis study | Am Rev Respir Dis | Isoniazid prophylaxis and phlyctenular keratoconjunctivitis among Eskimos in Alaska |
| [33607832](https://pubmed.ncbi.nlm.nih.gov/33607832/) | 2021 | Case report | Medicine | Phlyctenular keratoconjunctivitis in a child with primary sinonasal tuberculosis |
| [10641112](https://pubmed.ncbi.nlm.nih.gov/10641112/) | 1999 | Case series | Oftalmologia | 28 cases of tuberculous keratoconjunctivitis, 13 of them in children with primary TB |
| [14089390](https://pubmed.ncbi.nlm.nih.gov/14089390/) | 1964 | Case report | Arch Ophthalmol | Primary tuberculosis of the conjunctiva |
| [5103251](https://pubmed.ncbi.nlm.nih.gov/5103251/) | 1971 | Not classified | Ann Ocul | Local use of isoniazid in ocular tuberculosis |
| [1363080](https://pubmed.ncbi.nlm.nih.gov/1363080/) | 1992 | Review | Optom Clin | Ocular side effects of systemic drugs, including conjunctivitis |
| [10084171](https://pubmed.ncbi.nlm.nih.gov/10084171/) | 1999 | Case report | Rev Rhum (Engl Ed) | Isoniazid for refractory arthropathy after intravesical BCG |
| [12226788](https://pubmed.ncbi.nlm.nih.gov/12226788/) | 2002 | Case report | Dtsch Med Wochenschr | Chronic reactive arthritis with conjunctivitis after BCG |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1554T | Arrow Pharma Pty Ltd | Tablet 100 mg (oral) | Not listed in the data compiled for this report |

## Cytotoxicity

Isoniazid is not an antineoplastic drug, so this section does not apply.

## Safety Considerations

- **Contraindications and cautions from the knowledge graph** (these are drug-disease associations, not label text): liver failure, acute liver failure, hepatitis, liver disease, gallbladder disease, porphyria (including inherited porphyria and porphyrin metabolism disorders), diabetes mellitus, diabetic ketoacidosis, gout, peripheral neuropathy and other peripheral nervous system disease, substance abuse/dependence, and slow acetylator status.
- **Drug interactions** (100 recorded; examples shown): moderate interactions include antidiabetic agents (metformin, pioglitazone, alogliptin, canagliflozin, dapagliflozin, acarbose, albiglutide, chlorpropamide), metronidazole, budesonide, vitamin D analogues (cholecalciferol, calcifediol, calcitriol), alosetron and picosulfuric acid. Minor interactions include corticosteroids (hydrocortisone, triamcinolone, dexamethasone, betamethasone).
- **Other literature signals**: the retrieved papers describe isoniazid-associated hepatotoxicity and neuropathy (particularly in slow acetylators, linked to pyridoxine depletion), as well as rhabdomyolysis in a case report.

The TGA-approved Product Information (PI) warnings and contraindications were not available in the data compiled for this report. Please refer to the PI for the authoritative safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output and sparse, mostly historical or adverse-effect literature, with no registered clinical trials. Isoniazid's use in the eye is confined to tuberculosis-driven disease, and a general benefit in conjunctivitis is not supported.

**To proceed, the following is needed:**
- Mechanism of action data and a clear mechanistic rationale for ocular use
- Definition of a narrow target population (for example, tuberculous or phlyctenular keratoconjunctivitis), with evidence in that group
- Review of the TGA Product Information for warnings and contraindications (a blocking gap for safety screening)
- A safety plan covering hepatotoxicity, peripheral neuropathy, acetylator status and drug interactions

---

**Other predicted indications (for context):**
Several other predictions are also on Hold with a similar lack of supporting evidence.
- A small 1988 study of rifampicin with or without isoniazid exists.
- However, *M. leprae* has a non-functional katG gene and isoniazid is not part of standard WHO multidrug therapy. It is flagged as a research question.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

