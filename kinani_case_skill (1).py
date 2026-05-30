# -*- coding: utf-8 -*-
"""
KINANI FAMILY – INTERNATIONAL PROTECTION CASE AI SKILL
Purpose  : Legal analysis, risk assessment and argument generation
Based on : Case file, court decisions, international law and country conditions
Date     : 20.05.2026
Author   : Attorney Yusuf BIÇAKCI
"""

from datetime import datetime
from typing import List, Dict, Any
import json


class KinaniCaseSkill:
    def __init__(self):

        # === CASE BASIC INFORMATION ===
        self.case_info: Dict[str, Any] = {
            "case_name": "Kinani Family – International Protection Case",
            "applicants": [
                {
                    "name": "Kifah Hasan Dahham",
                    "relation": "Mother",
                    "birth_year": 1959,
                    "nationality": "Iraqi"
                },
                {
                    "name": "Sarah Salim Jaafar Al-Kinani",
                    "relation": "Daughter",
                    "birth_date": "2002-12-01",
                    "nationality": "Iraqi"
                }
            ],
            "legal_representative": "Attorney Yusuf BIÇAKCI",
            "file_number_first_instance": "2024/1174 – 2025/165",
            "file_number_appeal": "2025/2104 – 2026/1777",
            "first_instance_decision": "In favor of applicants – annulment of the rejection decision",
            "appeal_decision": "Appeal dismissed the case",
            "disputed_act": "Rejection of international protection application",
            "disputed_act_number": "49024",
            "disputed_act_date": "2024-10-09",
            "respondent_institution": "Afyonkarahisar Provincial Directorate of Migration Management"
        }

        # === VICTIM INFORMATION ===
        self.victim_info: Dict[str, Any] = {
            "full_name": "Salim Caafer El-Kinani (Salim Jaafar Al-Kinani)",
            "profession_period_1": "UN Interpreter (1991–2001, approx. 10 years)",
            "profession_period_2": "Senior Political Advisor to Prime Minister Iyad Allawi",
            "political_position": "Parliamentary candidate of Iraqi National Accord Party",
            "assassination_date": "2005-01-27",
            "assassination_place": "Baghdad, Iraq",
            "assassination_method": "Kidnapped, filmed, and publicly executed",
            "perpetrator": "Al-Qaeda in Iraq (Jamaat al-Tawhid wal-Jihad) led by Abu Musab al-Zarqawi",
            "reason_declared": "He was called 'Allawi's man' and accused of treason",
            "threat_to_family": "Family members are targeted for the same reason"
        }

        # === EVIDENCE & SOURCES ===
        self.evidence_sources: List[Dict[str, str]] = [
            {
                "source": "Reuters / Yahoo News",
                "date": "2005-01-27",
                "title": "Zarqawi group in Iraq claims beheading of Allawi aide",
                "type": "News"
            },
            {
                "source": "Al-Riyadh Newspaper (Saudi Arabia)",
                "date": "2005-01-27",
                "title": "Senior Iraqi official executed by Al-Qaeda",
                "type": "News"
            },
            {
                "source": "BBC News",
                "date": "2005-01-27",
                "title": "Iraqi Allawi aide killed by insurgents",
                "type": "News"
            },
            {
                "source": "The New York Times",
                "date": "2005-01-27",
                "title": "Zarqawi group executes Iraqi politician",
                "type": "News"
            },
            {
                "source": "EUAA Report",
                "date": "2023-01 to 2026-01",
                "title": "Iraq: Activities of Asa'ib Ahl al-Haq in relation to coercion, extortion, and property-related practices",
                "type": "Country of Origin Information Report"
            }
        ]

        # === LEGAL BASES ===
        self.legal_bases: List[str] = [
            "Law No. 6458 on Foreigners and International Protection – Articles 61, 62, 63, 78/3-4",
            "European Convention on Human Rights – Article 3 (Prohibition of Torture and Inhuman Treatment)",
            "1951 Refugee Convention – Article 1A(2) (Well-founded fear of persecution)",
            "Turkish Constitution – Articles 17 and 90 (Right to life and protection of international agreements)"
        ]

        # === APPEAL COURT ERRORS ===
        self.appeal_court_errors: List[Dict[str, str]] = [
            {
                "error_number": "1",
                "summary": "Misidentification of victim's profile",
                "appeal_claim": "Applicant does not fit the target profile of Asa'ib Ahl al-Haq (AAH); the group only targets activists and journalists.",
                "rebuttal": (
                    "According to the EUAA report (January 2023 – January 2026), AAH's target profile is not limited "
                    "to activists and journalists. It also includes persons who previously cooperated with US and coalition "
                    "forces, and their family members. The victim was not merely a UN interpreter; he was Prime Minister "
                    "Allawi's most trusted political advisor, right-hand man, and parliamentary candidate – placing him "
                    "at the center of AAH's and AQI's target list."
                )
            },
            {
                "error_number": "2",
                "summary": "Misinterpretation of the 11-year gap (2005–2016)",
                "appeal_claim": "The applicant continued her life without any problems for 11 years after her husband's death in 2005.",
                "rebuttal": (
                    "This assessment ignores the gradual strengthening of the threat source over time. AAH was founded "
                    "in 2006 (one year after the victim's assassination), entered parliament in 2018 with 15 seats, was "
                    "designated as a terrorist organization by the US State Department in January 2020, and by 2026 holds "
                    "27 parliamentary seats. The 2005–2016 period was not 'problem-free' but rather a preparatory period "
                    "during which the threat source was gaining power. The applicant's fear materialized precisely when "
                    "this growth reached its peak in 2016."
                )
            },
            {
                "error_number": "3",
                "summary": "Misinterpretation of martyr status and pension",
                "appeal_claim": "The state's recognition of the victim as a martyr and the payment of a martyr pension to the family proves that the applicant benefits from state protection in her country.",
                "rebuttal": (
                    "A martyr pension is not a protective measure directed at the individual; on the contrary, it is "
                    "evidence that the Iraqi State has officially acknowledged and registered that the victim was killed "
                    "by a terrorist organization for political reasons. This registration confirms that the mother applicant "
                    "is the widow of a government official martyred for political reasons, and the daughter applicant is "
                    "his orphan – both of which clearly fall within the 'membership in a particular social group' category "
                    "under Article 1A(2) of the 1951 Geneva Convention."
                )
            },
            {
                "error_number": "4",
                "summary": "Reliance on outdated and unverifiable information",
                "appeal_claim": "The victim's children from his first wife continue to work at state institutions in Baghdad, which shows the applicant is not in danger.",
                "rebuttal": (
                    "The information about children from the first wife working at state institutions dates back to "
                    "before 2005 and has not been updated or verified for over twenty years. All communication between "
                    "the applicants and the first wife's family has been completely severed since 2005 due to domestic "
                    "hostility. The applicants do not even know whether those individuals are still alive. Basing a "
                    "current security assessment on 20-year-old, unverified information constitutes a factual error "
                    "and inadequate examination in itself."
                )
            },
            {
                "error_number": "5",
                "summary": "Mischaracterization of state protection attempts",
                "appeal_claim": "The applicant did not seek effective protection from official authorities.",
                "rebuttal": (
                    "This assessment contradicts the facts on file. The applicant filed two separate complaints at "
                    "police stations following three home intrusion attempts in 2011, and also applied to the Baghdad "
                    "Court. After the direct death threat of June 1, 2016, she again approached the security checkpoint, "
                    "but officers told her to 'go home and not cause trouble.' Furthermore, EUAA reports confirm that "
                    "Iraqi security institutions are factually unable to provide protection against paramilitary groups "
                    "like AAH that have infiltrated the state."
                )
            },
            {
                "error_number": "6",
                "summary": "Misapplication of international case law – J.K. v. Sweden (2016)",
                "appeal_claim": "Reports from 2018–2023 indicate Iraq is safe; ECtHR decisions (J.K. v. Sweden 2016; J.A. and A.A. v. Turkey 2024) do not prevent return to Iraq.",
                "rebuttal": (
                    "The ECtHR Grand Chamber ruling in J.K. v. Sweden (Application No. 59166/12, 23.08.2016) is "
                    "actually a decision in favor of the applicant. The Court held that where an applicant has been "
                    "previously persecuted or directly threatened, a strong presumption arises that the risk continues, "
                    "and the burden shifts to the State to prove otherwise. General security improvements cannot rebut "
                    "this presumption. The J.A. and A.A. v. Turkey (06.02.2024) ruling concerns applicants with no "
                    "specific political profile, and is therefore not applicable to this case."
                )
            }
        ]

        # === RISK VARIABLES ===
        self.risk_factors: Dict[str, Any] = {
            "past_persecution": True,
            "serious_harm_risk": True,
            "targeted_family": True,
            "state_protection_unavailable": True,
            "non_refoulement_applicable": True,
            "overall_risk_level": "Very High",
            "daughter_specific_risks": [
                "Age 23, unmarried, no male protective relative",
                "Orphan daughter of a publicly executed politician",
                "Bears the 'Al-Kinani' surname known in militant circles",
                "At risk of gender-based violence upon return",
                "No internal flight alternative available due to AAH's nationwide reach"
            ]
        }

        # === CHRONOLOGY OF KEY EVENTS ===
        self.timeline: List[Dict[str, str]] = [
            {"year": "1991–2001", "event": "Salim Jaafar Al-Kinani serves as UN interpreter for approx. 10 years."},
            {"year": "2001–2004", "event": "Al-Kinani becomes Senior Political Advisor to PM Iyad Allawi; nominated as parliamentary candidate for Iraqi National Accord Party."},
            {"year": "2005-01-27", "event": "Al-Kinani kidnapped, filmed, and publicly executed by Al-Qaeda in Iraq (Zarqawi group), three days before the January 30, 2005 elections."},
            {"year": "2006", "event": "Asa'ib Ahl al-Haq (AAH) founded under Qais al-Khazali, declaring armed struggle against US and government collaborators."},
            {"year": "2011", "event": "Three home intrusion attempts against the applicant; two police complaints filed; Baghdad Court application made."},
            {"year": "2014", "event": "AAH formally integrated into Hashd al-Shaabi (Popular Mobilization Forces), gaining state-level status."},
            {"year": "2016-06-01", "event": "Direct death threat issued against applicant; security officer tells her to 'go home'; applicant flees Iraq to Turkey."},
            {"year": "2018", "event": "AAH enters Iraqi Parliament with 15 seats under the Fatah Alliance."},
            {"year": "2020-01", "event": "AAH designated as a terrorist organization by the US State Department."},
            {"year": "2021–2026", "event": "AAH holds 27 parliamentary seats and is a key partner in the Iraqi government within the Coordination Framework."},
            {"year": "2024-10-09", "event": "Afyonkarahisar Governorate rejects the international protection application (Act No. 49024)."},
            {"year": "2025-02-20", "event": "Afyonkarahisar Administrative Court rules in favor of applicants – annulment of the rejection (E: 2024/1174, K: 2025/165)."},
            {"year": "2026-04-24", "event": "Konya Regional Administrative Court (2nd Chamber) overturns the first instance decision and dismisses the case (E: 2025/2104, K: 2026/1777)."},
            {"year": "2026-05-20", "event": "Cassation petition filed before the Council of State (Danıştay)."}
        ]

        # === REQUESTED PROTECTION STATUSES ===
        self.protection_requests: List[Dict[str, str]] = [
            {
                "status": "Conditional Refugee",
                "legal_basis": "Law No. 6458, Article 62",
                "justification": (
                    "Applicants originate from Iraq (a non-European country), face well-founded fear of persecution "
                    "due to political opinion (husband/father's political position) and membership in a particular "
                    "social group (widow and orphan daughter of a martyred government official), and cannot benefit "
                    "from state protection."
                )
            },
            {
                "status": "Subsidiary Protection",
                "legal_basis": "Law No. 6458, Article 63",
                "justification": (
                    "In the event conditional refugee status is not granted: upon return to Iraq, the applicants – "
                    "especially the daughter applicant – face a real risk of torture, inhuman or degrading treatment, "
                    "or death. This risk is concrete and supported by international reports."
                )
            }
        ]

        # === OUTPUT SETTINGS ===
        self.output_settings: Dict[str, Any] = {
            "generate_legal_memo": True,
            "generate_risk_report": True,
            "generate_key_points": True,
            "language": "en",
            "format": ["pdf", "docx", "json"]
        }

        # === TIMESTAMP ===
        self.generated_at: str = datetime.now().isoformat()

    # ------------------------------------------------------------------ #
    #  METHODS                                                             #
    # ------------------------------------------------------------------ #

    def get_case_summary(self) -> str:
        """Returns a concise English summary of the case."""
        return (
            f"Case: {self.case_info['case_name']}\n"
            f"Applicants: {', '.join(a['name'] for a in self.case_info['applicants'])}\n"
            f"Respondent: {self.case_info['respondent_institution']}\n"
            f"First Instance Decision: {self.case_info['first_instance_decision']}\n"
            f"Appeal Decision: {self.case_info['appeal_decision']}\n"
            f"Overall Risk Level: {self.risk_factors['overall_risk_level']}\n"
            f"Generated at: {self.generated_at}"
        )

    def get_appeal_errors_summary(self) -> str:
        """Returns a formatted summary of all identified appeal court errors."""
        lines = ["APPEAL COURT ERRORS & REBUTTALS", "=" * 60]
        for err in self.appeal_court_errors:
            lines.append(f"\nError #{err['error_number']}: {err['summary']}")
            lines.append(f"  Court Claim : {err['appeal_claim']}")
            lines.append(f"  Rebuttal    : {err['rebuttal']}")
        return "\n".join(lines)

    def get_timeline(self) -> str:
        """Returns the chronology of key events."""
        lines = ["CHRONOLOGY OF KEY EVENTS", "=" * 60]
        for entry in self.timeline:
            lines.append(f"  {entry['year']:<12} – {entry['event']}")
        return "\n".join(lines)

    def export_to_json(self, filepath: str = "kinani_case_data.json") -> None:
        """Exports all case data to a JSON file."""
        data = {
            "case_info": self.case_info,
            "victim_info": self.victim_info,
            "evidence_sources": self.evidence_sources,
            "legal_bases": self.legal_bases,
            "appeal_court_errors": self.appeal_court_errors,
            "risk_factors": self.risk_factors,
            "timeline": self.timeline,
            "protection_requests": self.protection_requests,
            "generated_at": self.generated_at
        }
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"[✓] Case data exported to: {filepath}")

    def run_risk_assessment(self) -> Dict[str, Any]:
        """Performs a structured risk assessment and returns a report dict."""
        risk_score = sum([
            10 if self.risk_factors["past_persecution"] else 0,
            10 if self.risk_factors["serious_harm_risk"] else 0,
            10 if self.risk_factors["targeted_family"] else 0,
            10 if self.risk_factors["state_protection_unavailable"] else 0,
            10 if self.risk_factors["non_refoulement_applicable"] else 0,
        ])
        return {
            "risk_score": f"{risk_score}/50",
            "risk_level": self.risk_factors["overall_risk_level"],
            "non_refoulement_triggered": self.risk_factors["non_refoulement_applicable"],
            "daughter_specific_risks": self.risk_factors["daughter_specific_risks"],
            "recommended_status": self.protection_requests[0]["status"],
            "fallback_status": self.protection_requests[1]["status"]
        }


# ------------------------------------------------------------------ #
#  ENTRY POINT                                                        #
# ------------------------------------------------------------------ #

if __name__ == "__main__":
    skill = KinaniCaseSkill()

    print(skill.get_case_summary())
    print()
    print(skill.get_timeline())
    print()
    print(skill.get_appeal_errors_summary())
    print()

    assessment = skill.run_risk_assessment()
    print("RISK ASSESSMENT RESULT")
    print("=" * 60)
    for key, value in assessment.items():
        print(f"  {key:<35} : {value}")

    skill.export_to_json("kinani_case_data.json")
