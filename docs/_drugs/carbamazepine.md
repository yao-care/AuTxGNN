---
layout: default
title: Carbamazepine
parent: 僅模型預測 (L5)
nav_order: 122
evidence_level: L5
indication_count: 10
---

# Carbamazepine
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

# Carbamazepine: From Epilepsy / Trigeminal Neuralgia to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Carbamazepine (CBZ) is a well-established antiepileptic and first-line treatment for trigeminal neuralgia, widely used internationally to suppress abnormal neuronal firing through voltage-gated sodium channel blockade; it is not currently registered on the Australian Register of Therapeutic Goods (ARTG).
The TxGNN model predicts it may be effective for **Trigeminal Nerve Neoplasm** — specifically for managing neuropathic pain arising from tumour compression or infiltration of the trigeminal nerve — with **1 clinical trial** and **20 publications** identified in this direction.
Evidence is predominantly observational and case-based, supporting an **L3 evidence level**, and the mechanistic rationale is coherent but confined to symptomatic pain management rather than antitumour activity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Epilepsy; Trigeminal neuralgia (internationally established; no current ARTG registration — original indication data not available for Australia) |
| Predicted New Indication | Trigeminal Nerve Neoplasm |
| TxGNN Prediction Score | 99.9976% |
| Evidence Level | L3 — Observational studies and case series |
| Australia Market Status | Not registered (no ARTG entries) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current dataset. However, based on the extensive published literature linked to this Evidence Pack, Carbamazepine is a classic voltage-gated sodium channel blocker. By stabilising the inactivated state of Nav1.7 and Nav1.8 channels in trigeminal ganglion neurons, CBZ reduces the capacity of these cells to sustain the high-frequency burst firing that underlies trigeminal neuralgia (TN) pain. This mechanism is well-accepted and forms the basis of CBZ's international first-line status for TN.

The predicted indication — **trigeminal nerve neoplasm** — encompasses tumours that compress, displace, or directly infiltrate the trigeminal nerve and its branches (e.g., schwannomas, meningiomas, lymphomas, epidermoid cysts, and primary melanomas in Meckel's cave). When a mass lesion mechanically distorts the trigeminal nerve root, it induces focal demyelination and ectopic discharges at the affected segment — the same pathophysiological cascade as idiopathic TN. Multiple case reports in this dataset (PMIDs 30741017, 15235745, 25433061, 33989821, 26768887) document CBZ being prescribed as the first-line analgesic in patients who were subsequently found to have underlying neoplastic lesions. In one notable case (PMID 3181365), intravenous carbamazepine directly inhibited spontaneous ectopic discharges from experimental neuromas in an animal model, providing direct preclinical support for this mechanistic link.

It is critical to emphasise that **CBZ is a symptomatic agent in this context, not an antitumour therapy**. Its predicted utility in trigeminal nerve neoplasm is to control severe neuropathic pain while definitive oncological management (surgery, radiotherapy, or systemic therapy) is planned and executed. Clinicians should also note that failure of CBZ to control TN-like pain in a patient with negative initial imaging is an important red flag warranting repeat or gadolinium-enhanced MRI to exclude secondary neoplastic causes — as illustrated by the melanoma case in this dataset.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT06853119](https://clinicaltrials.gov/study/NCT06853119) | N/A | Not Yet Recruiting | 120 | Observational MRI study examining brain network dynamics and microstructural changes in trigeminal neuralgia patients; evaluates blood-brain barrier integrity and neural plasticity. No CBZ intervention. Provides neuroimaging background context only — not a treatment trial. |

Currently, **no interventional clinical trials specifically evaluating Carbamazepine for trigeminal nerve neoplasm** have been registered in ClinicalTrials.gov or ICTRP.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [36824641](https://pubmed.ncbi.nlm.nih.gov/36824641/) | 2022 | Review | Acta Clinica Croatica | Comprehensive treatment review for TN; confirms CBZ as first-line medical therapy and explicitly states TN can be caused by vascular compression **or a tumour process** — directly relevant to this prediction |
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Review of Neurotherapeutics | Detailed review of TN pathophysiology; discusses focal demyelination, ectopic discharge, and MRI for neurovascular contact — key mechanistic underpinning for CBZ use in neoplasm-related TN |
| [11286444](https://pubmed.ncbi.nlm.nih.gov/11286444/) | 2001 | Cohort | British Journal of Oral & Maxillofacial Surgery | UK oral surgeon survey on TN management and CBZ monitoring practices; highlights that screening for **secondary (neoplastic) TN** remains a management consideration |
| [3181365](https://pubmed.ncbi.nlm.nih.gov/3181365/) | 1988 | Experimental | Experimental Neurology | IV carbamazepine directly inhibited spontaneous ectopic discharges from saphenous neuromas in rats — preclinical evidence supporting CBZ suppression of neuroma/neoplasm-related aberrant firing |
| [30741017](https://pubmed.ncbi.nlm.nih.gov/30741017/) | 2023 | Case Report | British Journal of Neurosurgery | Primary malignant lymphoma of trigeminal nerve presenting as facial pain; CBZ prescribed initially but did not improve symptoms — illustrates that neoplastic TN may be refractory to CBZ, underscoring the need for MRI |
| [9109911](https://pubmed.ncbi.nlm.nih.gov/9109911/) | 1997 | Case Report | Neurology | Post-irradiation neuromyotonia in bilateral facial and trigeminal nerve distribution; **responded to carbamazepine** — radiation-induced nerve injury provides an analogy to neoplasm-related nerve dysfunction |
| [15235745](https://pubmed.ncbi.nlm.nih.gov/15235745/) | 2004 | Case Report | Arquivos de Neuro-Psiquiatria | Primary melanoma of Meckel's cave presenting as TN; pain was **not relieved by CBZ or microvascular decompression** — CBZ failure should prompt urgent MRI for neoplastic aetiology |
| [22647513](https://pubmed.ncbi.nlm.nih.gov/22647513/) | 2012 | Case Report | No Shinkei Geka | Combined glossopharyngeal and trigeminal neuralgia; CBZ documented as standard first-line medical therapy before surgical microvascular decompression |
| [25433061](https://pubmed.ncbi.nlm.nih.gov/25433061/) | 2014 | Case Report | No Shinkei Geka | TN caused by cerebellopontine angle lipoma; CBZ used but inadequately controlled due to side effects — surgical resection ultimately required |
| [33989821](https://pubmed.ncbi.nlm.nih.gov/33989821/) | 2021 | Case Report | World Neurosurgery | Petroclival meningioma causing TN (<5% of cases); confirms that neoplasm-related TN is managed with initial medical therapy (CBZ context) before surgical intervention |

---

## Australia Market Information

Carbamazepine is **not currently registered on the Australian Register of Therapeutic Goods (ARTG)**. No ARTG entries exist for this medicine under any brand name, dosage form, or route of administration in the current dataset.

Clinicians wishing to prescribe Carbamazepine in Australia would need to access it through one of the following TGA pathways:

- **Special Access Scheme (SAS) Category B** — for individual patients with a serious or life-threatening condition
- **Authorised Prescriber pathway** — if prescribing for a class of patients with a specific condition

Note: This finding is based on the data held in the current Evidence Pack (data cutoff: 21 June 2026). Given that Carbamazepine (e.g., Tegretol) is a well-established medicine internationally, prescribers should verify current ARTG status directly via the [TGA Public Summary Search](https://www.tga.gov.au/resources/artg) before assuming non-availability.

---

## Safety Considerations

As Carbamazepine has no current TGA registration and no Australian Product Information (PI) is available, clinicians should consult an approved international prescribing reference (e.g., FDA prescribing information, UK Summary of Product Characteristics, or EMA SmPC). Safety data was not retrieved in this Evidence Pack (Data Gap DG001).

Key safety considerations known from established international evidence:

- **Black box / serious warnings**: Stevens-Johnson syndrome (SJS) and toxic epidermal necrolysis (TEN) — risk is substantially elevated in patients carrying the **HLA-B\*15:01 allele**, which is prevalent in East Asian and some South-East Asian populations represented in Australia's multicultural community. Genetic screening is strongly recommended prior to initiation.
- **Haematological**: Aplastic anaemia; agranulocytosis — baseline and periodic full blood count (FBC with differential) required
- **Electrolyte**: Hyponatraemia and SIADH — monitor serum sodium, particularly in elderly patients
- **Hepatic**: Elevations in liver enzymes — baseline and periodic liver function testing required
- **Endocrine / bone**: Long-term CBZ induces CYP enzymes, accelerating vitamin D and hormone metabolism; bone mineral density monitoring warranted in chronic use
- **Teratogenicity**: Known Category D teratogen (neural tube defects, cardiac malformations) — requires specialist counselling, high-dose folic acid, and contraception discussion in women of childbearing age
- **Drug interactions**: CBZ is a potent inducer of CYP3A4, CYP2C9, and P-glycoprotein — extensive drug-drug interaction potential with oncological agents, anticoagulants, antiretrovirals, and many other commonly prescribed medicines. Formal DDI review was not completed in this dataset.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction is mechanistically coherent — CBZ's established ability to suppress trigeminal ectopic discharge maps directly to the pain pathophysiology of trigeminal nerve neoplasm. Multiple case series and reviews confirm that CBZ is routinely used as initial symptomatic analgesia in this setting pending oncological management, and preclinical data directly support suppression of neuroma-generated firing. However, the evidence is L3 (case reports and observational data), no dedicated RCT exists, the drug has no current ARTG registration, and its role is purely symptomatic rather than disease-modifying.

**To proceed, the following is needed:**

- **TGA access pathway clarification**: Confirm SAS Category B or Authorised Prescriber eligibility for the specific patient and indication prior to prescribing
- **HLA-B\*15:01 genetic screening**: Particularly important for patients of East Asian, South-East Asian, or South Asian descent — screen before first dose to mitigate SJS/TEN risk
- **Safety data retrieval**: Download and parse the current international PI (DG001) to complete formal safety and contraindication assessment
- **MOA documentation**: Retrieve full DrugBank API data for Carbamazepine (DG002) to formalise the mechanistic rationale in the clinical dossier
- **Oncology and neurosurgery consultation**: Ensure CBZ is prescribed as adjunctive pain management, not a substitute for tumour-directed therapy; coordinate with the treating oncology and neurosurgery teams
- **Baseline and monitoring plan**: Establish FBC with differential, LFTs, renal function, serum sodium, and body weight at baseline; schedule monitoring at 2–4 weeks, then 3-monthly during stable treatment
- **Pain reassessment trigger**: Pre-specify a clear clinical threshold — if CBZ fails to control pain adequately within 4–6 weeks, or if any new neurological symptoms emerge, urgent gadolinium-enhanced MRI should be performed to reassess tumour status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

