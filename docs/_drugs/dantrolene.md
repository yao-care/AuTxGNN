---
layout: default
title: Dantrolene
parent: 僅模型預測 (L5)
nav_order: 138
evidence_level: L5
indication_count: 10
---

# Dantrolene
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

# Dantrolene: From Muscle Spasticity to Malignant Hyperthermia Susceptibility

## One-Sentence Summary

Dantrolene is a skeletal muscle relaxant that has been globally recognised since the 1970s as the sole specific rescue agent for malignant hyperthermia (MH) — a potentially fatal pharmacogenetic anaesthetic emergency — yet it currently holds no registration in Australia, with zero ARTG entries.
The TxGNN model confirms this well-established therapeutic association by ranking **Malignant Hyperthermia Susceptibility** as its top predicted indication with a score of **99.93%**,
supported by **19 publications** including 2 international clinical practice guidelines — highlighting a significant patient safety gap in the Australian healthcare system.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Australian ARTG registration; globally approved for muscle spasticity (upper motor neuron disorders) and malignant hyperthermia |
| Predicted New Indication | Malignant Hyperthermia, Susceptibility To |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L1 (multiple international clinical practice guidelines; randomised controlled trials are ethically impractical for this acute life-threatening emergency) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data was not available from the queried sources for this evidence pack. Based on well-established pharmacology, dantrolene acts directly on the ryanodine receptor type 1 (RyR1) in skeletal muscle sarcoplasmic reticulum, blocking the abnormal and uncontrolled calcium (Ca²⁺) release that drives a malignant hyperthermia crisis. A 2017 study published in the *Proceedings of the National Academy of Sciences* (PMID 28373535) further clarified that this inhibition requires the presence of magnesium ions (Mg²⁺), providing important context for clinical administration protocols.

Malignant hyperthermia susceptibility (MHS) is a pharmacogenetic disorder driven primarily by gain-of-function mutations in the *RYR1* gene (accounting for approximately 70% of cases), with a smaller proportion involving *CACNA1S* mutations. Susceptible individuals appear clinically normal but are at severe risk of a fulminant hypermetabolic crisis — characterised by hyperthermia, muscle rigidity, rhabdomyolysis, and mixed acidosis — when exposed to volatile inhalational anaesthetics (halothane, sevoflurane, desflurane, isoflurane) or the depolarising muscle relaxant succinylcholine. Because dantrolene acts precisely at the defective molecular target — the dysregulated RyR1 calcium release channel — it is the only pharmacological agent capable of rapidly reversing this crisis.

The 2021 Association of Anaesthetists Clinical Practice Guideline (PMID 33399225) and the 2021 European Malignant Hyperthermia Group Consensus Guidelines (PMID 33131754) both mandate dantrolene as the first-line rescue agent, with mortality falling from approximately 70–80% before dantrolene's clinical introduction to under 5% in centres where the drug is promptly accessible. The TxGNN prediction here effectively validates model performance while simultaneously flagging a real-world clinical concern: this life-saving drug is unavailable through standard Australian commercial channels.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered.

> **Why no RCTs exist:** Malignant hyperthermia is a rare, acutely life-threatening anaesthetic emergency. Conducting a placebo-controlled randomised trial in this setting would be ethically and practically impossible — it would require withholding a proven rescue treatment from a patient in a potentially fatal crisis. Evidence for dantrolene in MH is therefore derived from international clinical practice guidelines, observational data, mechanistic studies, and decades of clinical experience spanning from the mid-1970s to the present. Both major 2021 guidelines were developed explicitly to address this evidentiary structure.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33399225](https://pubmed.ncbi.nlm.nih.gov/33399225/) | 2021 | Clinical Practice Guideline | *Anaesthesia* | 2021 Association of Anaesthetists guideline defining MH as a progressive life-threatening hyperthermic reaction under general anaesthesia; dantrolene is the mandatory first-line pharmacological intervention, with dosing and monitoring protocols specified |
| [33131754](https://pubmed.ncbi.nlm.nih.gov/33131754/) | 2021 | Consensus Guideline | *British Journal of Anaesthesia* | European MH Group consensus on perioperative management of MH-susceptible patients; covers preoperative risk stratification, trigger-free anaesthesia, and dantrolene as the central pharmacological agent; addresses residual volatile anaesthetic concerns |
| [39171998](https://pubmed.ncbi.nlm.nih.gov/39171998/) | 2024 | Review | *Critical Care Medicine* | Expert narrative review of clinical epidemiology and management of critically ill MH patients; updates current understanding of MH pathophysiology and intensive care management |
| [40597248](https://pubmed.ncbi.nlm.nih.gov/40597248/) | 2025 | Bibliometric Analysis | *Orphanet Journal of Rare Diseases* | Global bibliometric analysis of MH research from 1975 to 2024; maps publication trends, research hotspots, and provides recommendations for reducing MH mortality in the current era |
| [28373535](https://pubmed.ncbi.nlm.nih.gov/28373535/) | 2017 | Mechanistic Study | *PNAS* | Demonstrates that dantrolene requires Mg²⁺ to arrest MH; directly characterises dantrolene's effect on Ca²⁺ transients triggered by MH-inducing agents, clarifying its molecular mechanism of action on RyR1 |
| [26238698](https://pubmed.ncbi.nlm.nih.gov/26238698/) | 2015 | Review | *Orphanet Journal of Rare Diseases* | Comprehensive pharmacogenetic review of MH covering incidence (1:10,000–1:250,000 anaesthetics), genetics, pathophysiology, and management; reviews dantrolene dosing in acute crises |
| [32008650](https://pubmed.ncbi.nlm.nih.gov/32008650/) | 2020 | Review | *Anesthesiology Clinics* | Current update on MH as an autosomal dominant skeletal muscle calcium release channel disorder; documents mortality improvement from >70% (pre-dantrolene era) to current rates below 5% in well-resourced settings |
| [33863282](https://pubmed.ncbi.nlm.nih.gov/33863282/) | 2021 | Observational Study | *BMC Anesthesiology* | Reports characteristics and outcomes of MH in settings where dantrolene is not readily available (e.g., China); directly demonstrates the life-threatening consequences of dantrolene inaccessibility |
| [17456235](https://pubmed.ncbi.nlm.nih.gov/17456235/) | 2007 | Review | *Orphanet Journal of Rare Diseases* | Foundational Orphanet disease review establishing the diagnostic and management framework for MH, covering RYR1/CACNA1S mutation spectrum and prevalence of genetic susceptibility (~1:3,000) |
| [9538480](https://pubmed.ncbi.nlm.nih.gov/9538480/) | 1998 | Review | *Postgraduate Medical Journal* | Reviews MH as a rare autosomal dominant trait triggered by volatile anaesthetics and succinylcholine; identifies sodium dantrolene as the definitive treatment for the hypermetabolic skeletal muscle reaction, with precautions for susceptible patients |

---

## Australia Market Information

Dantrolene (DrugBank ID: DB01219) currently holds **no ARTG registrations in Australia**. The drug is not available through standard commercial pharmacy channels.

> In current Australian practice, dantrolene injection (Dantrium IV® or equivalent) may be accessed at individual hospital level through the TGA Special Access Scheme (SAS Category B or C), direct importation, or hospital formulary arrangements — but it is not formally registered on the ARTG. The absence of a registered product means there is no standardised, reliably available supply across Australian healthcare settings, including regional hospitals and day surgery centres where general anaesthesia is administered.

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|-------------|-------------|-------------|---------------------|
| — | No ARTG entries found | — | — |

---

## Safety Considerations

As dantrolene is not currently registered in Australia, no TGA-approved Product Information document is available. Please refer to the relevant international prescribing information and the clinical practice guidelines listed above.

Prescribers and anaesthetists should be aware of the following based on international product information and published guidelines:

- **Hepatotoxicity risk** with chronic oral administration (dose-dependent; less clinically relevant for acute IV use in MH)
- **Concomitant calcium channel blockers** (e.g., verapamil): potential for hyperkalaemia and cardiovascular depression when co-administered with IV dantrolene
- **Muscle weakness**: expected pharmacological effect; respiratory muscle monitoring required
- **Acute IV dose for MH rescue**: 2.5 mg/kg repeated every 5–15 minutes as needed (per 2021 international guidelines); total doses exceeding 10 mg/kg may be required in severe cases

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Dantrolene is the internationally mandated sole rescue agent for malignant hyperthermia, endorsed by the Association of Anaesthetists (2021) and the European Malignant Hyperthermia Group (2021), with evidence spanning five decades; its complete absence from the Australian ARTG register represents a preventable patient safety risk in any hospital or day surgery centre administering general anaesthesia.

**To proceed, the following is needed:**

- **TGA Registration:** Submit a formal ARTG registration application for dantrolene sodium for injection (parenteral form) — or expand existing SAS Category B access into a more formalised supply arrangement
- **Supply chain assurance:** Conduct a national audit of current dantrolene IV stock availability across Australian hospitals, day surgery centres, and regional/remote anaesthesia settings
- **Mechanism of action documentation:** Formally document RyR1 inhibition and Ca²⁺ release blocking mechanism in an Australian PI document (DrugBank MOA data to be retrieved and verified)
- **Safety profile retrieval:** Obtain and summarise the full warnings, contraindications, and drug interaction profile from the TGA or relevant international regulatory authority PI (identified as a blocking data gap)
- **Clinical protocol development:** Develop an Australian-specific MH emergency management protocol in collaboration with ANZCA, consistent with 2021 international guidelines
- **Clinician awareness:** Address awareness gaps regarding SAS access pathways for dantrolene among Australian anaesthetists, particularly in non-metropolitan settings
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

