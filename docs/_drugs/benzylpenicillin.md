---
layout: default
title: Benzylpenicillin
parent: 僅模型預測 (L5)
nav_order: 83
evidence_level: L5
indication_count: 10
---

# Benzylpenicillin
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

# Benzylpenicillin: From Bacterial Infections to Pericoronitis

## One-Sentence Summary

Benzylpenicillin (Penicillin G) is one of the oldest and most established β-lactam antibiotics, with a long clinical history of use against susceptible Gram-positive bacteria and anaerobic organisms.
The TxGNN model predicts it may be effective for **Pericoronitis**, with **no registered clinical trials** but **20 supporting publications** currently identified for this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Susceptible bacterial infections (TGA ARTG data not retrieved in automated analysis) |
| Predicted New Indication | Pericoronitis |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L3 |
| Australia Market Status | Not retrieved (0 ARTG entries found) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on ARTG data**: The automated data collection returned 0 ARTG entries for Benzylpenicillin. This likely reflects a data retrieval gap rather than genuine non-availability — Benzylpenicillin is a well-established injectable antibiotic in clinical use globally. Clinical teams should verify current registration status directly via the [TGA ARTG Public Summary](https://www.tga.gov.au/resources/artg) before prescribing.

---

## Why is This Prediction Reasonable?

Benzylpenicillin (Penicillin G) is a naturally occurring β-lactam antibiotic that exerts bactericidal activity by irreversibly binding to penicillin-binding proteins (PBPs) on the bacterial cell wall, thereby inhibiting peptidoglycan cross-linking and triggering cell lysis. Although the automated data pipeline did not retrieve formal MOA documentation (DrugBank query returned incomplete data for this field), benzylpenicillin's mechanism is among the most thoroughly documented in all of antimicrobial pharmacology.

Pericoronitis — acute infection of the soft tissue surrounding a partially erupted wisdom tooth — is caused by a polymicrobial oral flora dominated by aerobic viridans group streptococci alongside obligate anaerobes including *Peptostreptococcus*, *Fusobacterium nucleatum*, *Bacteroides* species, and spirochetes. Benzylpenicillin maintains strong bactericidal activity against Gram-positive streptococci and many of these anaerobic organisms, making its mechanism of action directly applicable to the pathogenic profile of pericoronitis. Contemporary dental infectious disease guidance (Cooper et al., 2022) specifically recommends β-lactam monotherapy as the first-line antibiotic class for non-periodontal dental infections, of which pericoronitis is a primary example.

The principal caveat is the presence of β-lactamase–producing strains in pericoronitis isolates: Sixou et al. (PMID:12789143) documented β-lactamase–producing bacteria in mandibular third molar pericoronitis, meaning benzylpenicillin monotherapy may fail in a clinically significant subset of patients. No head-to-head clinical trial comparing benzylpenicillin directly against current standard-of-care (typically amoxicillin ± metronidazole) exists for this indication. Pathogen-directed stewardship and local resistance data are therefore essential before broad clinical adoption.

---

## Clinical Trial Evidence

Currently no clinical trials for Benzylpenicillin specifically in pericoronitis are registered on ClinicalTrials.gov or ANZCTR (Australian New Zealand Clinical Trials Registry).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35959239](https://pubmed.ncbi.nlm.nih.gov/35959239/) | 2022 | Systematic Review | JAC-Antimicrobial Resistance | β-lactam monotherapy recommended as first-line for non-periodontal dental infections (including pericoronitis); metronidazole reserved only when systemic involvement is confirmed |
| [1873287](https://pubmed.ncbi.nlm.nih.gov/1873287/) | 1991 | Survey/Expert Opinion | Br J Oral Maxillofac Surg | British oral surgeons identify predominantly anaerobic flora in acute pericoronitis; penicillins (amoxycillin) and metronidazole identified as effective antimicrobials |
| [12789143](https://pubmed.ncbi.nlm.nih.gov/12789143/) | 2003 | Microbiology Study | Oral Surg Oral Med Oral Pathol | Characterised predominant flora in pericoronitis; critically identified β-lactamase–producing strains — the primary mechanistic limitation of benzylpenicillin monotherapy |
| [26067725](https://pubmed.ncbi.nlm.nih.gov/26067725/) | 2015 | Retrospective Study | J Contemp Dent Pract | One-year retrospective on odontogenic infection prevalence and management in an emergency dental service; documents antibiotic prescribing patterns |
| [40381916](https://pubmed.ncbi.nlm.nih.gov/40381916/) | 2025 | Surveillance Study | J Infect Chemother | Second Japanese antimicrobial susceptibility surveillance of odontogenic infection isolates (2018 data), including pericoronitis subgroup; provides up-to-date resistance profiles |
| [32591324](https://pubmed.ncbi.nlm.nih.gov/32591324/) | 2020 | Surveillance Study | J Infect Chemother | First Japanese antimicrobial susceptibility surveillance for odontogenic infections (2013 data); 6 pericoronitis samples with penicillin susceptibility data included |
| [16388299](https://pubmed.ncbi.nlm.nih.gov/16388299/) | 2006 | Microbiology Study | Med Oral Patol Oral Cir Bucal | Antibiotic susceptibility of bacteria in odontogenic infections and lower third molar pericoronitis; key resource for spectrum-of-activity data |
| [29693642](https://pubmed.ncbi.nlm.nih.gov/29693642/) | 2018 | Narrative Review | Antibiotics (Basel) | Review of antibiotic prescribing for oro-facial infections in paediatric outpatients; penicillins noted as first-choice class; highlights antibiotic stewardship concerns |
| [21027620](https://pubmed.ncbi.nlm.nih.gov/21027620/) | 1946 | Case Report | Am J Orthod Oral Surg | Submaxillary abscess arising from acute pericoronitis successfully treated by aspiration and instillation of penicillin — earliest direct clinical evidence for penicillin in pericoronitis |
| [36268928](https://pubmed.ncbi.nlm.nih.gov/36268928/) | 2022 | Narrative Review | Eur J Transl Myol | Antibiotic use in odontogenic/endodontic treatment during pregnancy; β-lactams identified as the safer first-line choice, including pericoronitis scenarios |

---

## Australia Market Information

No ARTG entries for Benzylpenicillin were retrieved in the automated data collection underpinning this report. Given that benzylpenicillin is a globally established injectable antibiotic, this is most likely a data retrieval gap rather than an indication that the product is unavailable in Australia.

Clinical teams should independently verify current TGA registration status and retrieve the approved Product Information (PI) directly from the [TGA ARTG Public Summary](https://www.tga.gov.au/resources/artg) prior to any prescribing or formulary decision.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for full safety information, as automated safety data was not retrieved for this report.

> **Critical clinical reminder**: Benzylpenicillin carries a well-established risk of hypersensitivity reactions, ranging from mild rash to life-threatening anaphylaxis. A thorough allergy history — including prior penicillin reactions and cross-reactivity with cephalosporins — is mandatory before use. Emergency resuscitation facilities should be available when administering parenteral benzylpenicillin.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic basis for benzylpenicillin in pericoronitis is well-founded — the drug's β-lactam activity covers the dominant streptococcal and anaerobic pathogens driving this infection — and a systematic review alongside multiple observational and microbiology studies provide L3-level support. However, documented β-lactamase resistance in pericoronitis isolates, the absence of a dedicated RCT for benzylpenicillin in this indication, and unconfirmed TGA ARTG registration status mean that guardrails are necessary before clinical adoption.

**To proceed, the following is needed:**

- **Verify ARTG registration**: Confirm Benzylpenicillin's current TGA listing and obtain the approved Australian Product Information (PI) to define approved dosing, contraindications, and warnings
- **Retrieve formal MOA and safety data**: Complete the DrugBank API query (DG002 remediation) and obtain TFDA/TGA PI warnings (DG001 remediation)
- **Local resistance assessment**: Review Australian oral microbiology resistance data — particularly β-lactamase prevalence in pericoronitis isolates — before recommending benzylpenicillin monotherapy over amoxicillin–clavulanate
- **Antibiotic stewardship alignment**: Clarify pathway for injectable benzylpenicillin versus oral amoxicillin in line with current Australian Therapeutic Guidelines (Oral and Dental) to define where benzylpenicillin adds clinical value
- **Prospective clinical audit**: A small, prospective comparative study of benzylpenicillin versus standard-of-care antibiotics in pericoronitis within an Australian dental or maxillofacial setting would upgrade the evidence level to L2 and strengthen the repurposing case

---

> **Disclaimer**: This report is intended for research reference purposes only and does not constitute medical advice. All drug repurposing candidates identified by TxGNN require clinical validation before therapeutic application. Prescribers should consult current Australian Therapeutic Guidelines and TGA-approved Product Information.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

