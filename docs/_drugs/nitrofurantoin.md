---
layout: default
title: Nitrofurantoin
parent: Model Prediction Only (L5)
nav_order: 506
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Nitrofurantoin: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Not stated in the data compiled for this report (nitrofurantoin is an…"
---

# Nitrofurantoin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Nitrofurantoin: From Urinary Tract Infection (Presumed) to Rheumatoid Arthritis

## One-Sentence Summary

Nitrofurantoin is an oral antibacterial; the registered indication text was not available in the data compiled for this report, but its established clinical use is for urinary tract infection (UTI).
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but there are **no registered clinical trials** and the **9 publications** retrieved mostly describe adverse events, not therapeutic benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (nitrofurantoin is an antibacterial generally used for UTI) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, nitrofurantoin is a nitrofuran antibacterial whose metabolites damage bacterial DNA and ribosomal proteins. It has no known anti-inflammatory or immunomodulatory action relevant to rheumatoid arthritis (RA).

The prediction is therefore not mechanistically supported. The high TxGNN score (99.89%) appears to reflect an association in the knowledge graph, not evidence of benefit. The retrieved literature concerns drug-induced pulmonary fibrosis, a methotrexate-nitrofurantoin interaction causing irreversible lung fibrosis in an RA patient, RA-associated interstitial lung disease, and antibiotic exposure as a possible trigger of RA flares. The safety signal points in the opposite direction to a therapeutic effect.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | Review | Saudi Med J | Drug-induced pulmonary fibrosis; nitrofurantoin is a recognised cause, and RA is a predisposing disease |
| [25362778](https://pubmed.ncbi.nlm.nih.gov/25362778/) | 2014 | Review | Rev Prat | Drug-induced interstitial lung disease; nitrofurantoin listed among implicated antibiotics |
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | Self-controlled case series | Sci Rep | Association between antibiotic use and RA flares in a UK primary care cohort (n = 31,992) |
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | Case report | Cureus | Methotrexate and nitrofurantoin interaction causing irreversible pulmonary fibrosis in a 94-year-old woman with RA |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | Cohort | Chest | Poor prognosis in RA patients hospitalised for interstitial lung fibrosis (not specific to nitrofurantoin) |
| [41635325](https://pubmed.ncbi.nlm.nih.gov/41635325/) | 2026 | Case report | Cureus | Autoimmune hepatitis versus drug-induced liver injury; nitrofurantoin named as a cause to rule out |
| [8104358](https://pubmed.ncbi.nlm.nih.gov/8104358/) | 1993 | Case report | Rev Pneumol Clin | Gold salt-induced pneumonitis in an RA-treated patient (nitrofurantoin not the focus) |
| [11937933](https://pubmed.ncbi.nlm.nih.gov/11937933/) | 2002 | Case report | Ann Dermatol Venereol | Phenylbutazone-induced sialadenitis; nitrofurantoin mentioned as a rare cause |
| [899886](https://pubmed.ncbi.nlm.nih.gov/899886/) | 1977 | Screening/treatment study | Acta Med Scand | Short-term nitrofurantoin for bacteriuria in middle-aged women; not related to RA |

None of these publications reports a therapeutic benefit of nitrofurantoin in RA.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1692C | Nitrofurantoin BNM | Capsule 50 mg | Not stated in the data compiled for this report |

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** diabetes mellitus, diabetic ketoacidosis, anuria, impaired renal function, peripheral neuropathy and other peripheral nervous system disease, interstitial lung disease, pulmonary fibrosis, G6PD deficiency, drug-induced liver injury, hepatitis, obstructive jaundice, biliary tract disease, vitamin B12 and other B-vitamin deficiency, optic neuritis, *Clostridium difficile* colitis, cystinuria, galactosemia and glycogen storage disease.
- **Literature-based safety signals:** pulmonary fibrosis (including a severe interaction with methotrexate, a drug commonly used in RA), hepatotoxicity including autoimmune-like hepatitis, and haemolysis or methaemoglobinaemia, particularly in G6PD deficiency.
- **Drug interactions:** 100 interactions were identified. The main moderate ones include metronidazole, balsalazide, picosulfuric acid, naltrexone, rosuvastatin and simvastatin. Anticholinergics (for example atropine, hyoscyamine, glycopyrronium) and magnesium-containing antacids are listed as minor.

Please also refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials, no plausible mechanism, and literature that points to harm (pulmonary, hepatic and haematological toxicity, and a dangerous interaction with methotrexate) rather than benefit in RA.

**To proceed, the following is needed:**
- Mechanism of action data and any biological rationale for an anti-inflammatory or immunomodulatory effect in RA
- The approved indication text and the Product Information (warnings and contraindications) for the ARTG entry
- Preclinical or early clinical evidence of benefit in RA
- A safety assessment covering concurrent methotrexate use, lung and liver risk, and renal function in the RA population

Other predicted indications (for example autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome, brain small vessel disease, diabetic nephropathy, sclerosing cholangitis, methaemoglobinaemia and gout) are likewise supported by prediction only, or by adverse-effect literature, and are also on Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

