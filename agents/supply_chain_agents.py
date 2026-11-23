"""
SupplyChain Sentinel
Six specialized CrewAI agents for supply chain
crisis investigation and recovery.
"""

import logging

from crewai import Agent

from services.crewai_llm import get_crewai_llm


# ==========================================
# LOGGING
# ==========================================

logger = logging.getLogger("SupplyChainSentinel.Agents")


# ==========================================
# AGENT FACTORY
# ==========================================

def create_supply_chain_agents():

    """
    Creates and returns all six supply chain agents.

    All agents share the same configured Gemini LLM.
    Each agent has a specialized responsibility.
    """

    logger.info("Initializing SupplyChain Sentinel agents...")

    # Shared Gemini LLM
    llm = get_crewai_llm()

    # ======================================
    # 1. DISRUPTION ANALYST
    # ======================================

    disruption_analyst = Agent(

        role="Supply Chain Disruption Analyst",

        goal=(
            "Investigate supply chain disruptions, "
            "identify their root causes, classify crisis "
            "severity, and determine their immediate "
            "and downstream consequences."
        ),

        backstory=(
            "You are an experienced supply chain risk "
            "investigator specializing in global logistics, "
            "supplier failures, geopolitical disruptions, "
            "natural disasters, port congestion, and "
            "transportation interruptions. "
            "You distinguish confirmed information from "
            "assumptions and identify missing information."
        ),

        llm=llm,

        verbose=False,

        allow_delegation=False,

        max_iter=3,

        max_rpm=10
    )

    # ======================================
    # 2. INVENTORY ANALYST
    # ======================================

    inventory_analyst = Agent(

        role="Inventory Intelligence Analyst",

        goal=(
            "Analyze inventory availability, demand patterns, "
            "stock shortages, reorder requirements, and "
            "potential stockout risks."
        ),

        backstory=(
            "You are an inventory planning specialist "
            "experienced in demand forecasting, warehouse "
            "management, safety stock calculations, and "
            "inventory optimization. "
            "You evaluate available stock against demand "
            "and identify which products require immediate "
            "attention."
        ),

        llm=llm,

        verbose=False,

        allow_delegation=False,

        max_iter=3,

        max_rpm=10
    )

    # ======================================
    # 3. SUPPLIER INTELLIGENCE
    # ======================================

    supplier_intelligence = Agent(

        role="Supplier Intelligence Specialist",

        goal=(
            "Evaluate supplier reliability, identify "
            "supplier-related risks, and recommend "
            "suitable alternative sourcing options."
        ),

        backstory=(
            "You are an expert in supplier relationship "
            "management and procurement intelligence. "
            "You assess supplier performance, reliability, "
            "geographical exposure, production capacity, "
            "lead times, and sourcing alternatives. "
            "You never invent supplier information or "
            "claim an alternative supplier is verified "
            "without supporting data."
        ),

        llm=llm,

        verbose=False,

        allow_delegation=False,

        max_iter=3,

        max_rpm=10
    )

    # ======================================
    # 4. LOGISTICS OPTIMIZER
    # ======================================

    logistics_optimizer = Agent(

        role="Logistics and Transportation Optimizer",

        goal=(
            "Investigate shipment delays, evaluate "
            "transportation bottlenecks, and recommend "
            "alternative delivery and routing strategies."
        ),

        backstory=(
            "You are a transportation optimization "
            "specialist with expertise in freight management, "
            "shipping operations, delivery scheduling, "
            "route alternatives, and transportation costs. "
            "You compare available logistics options and "
            "prioritize delivery reliability and recovery time."
        ),

        llm=llm,

        verbose=False,

        allow_delegation=False,

        max_iter=3,

        max_rpm=10
    )

    # ======================================
    # 5. RISK ANALYST
    # ======================================

    risk_analyst = Agent(

        role="Supply Chain Operational Risk Analyst",

        goal=(
            "Evaluate the financial, operational, "
            "inventory, supplier, and customer impact "
            "of the identified supply chain crisis."
        ),

        backstory=(
            "You are an enterprise risk management "
            "specialist experienced in business continuity, "
            "financial exposure, operational resilience, "
            "and crisis impact assessment. "
            "You prioritize risks based on likelihood, "
            "severity, and business consequences. "
            "You clearly distinguish calculated values "
            "from estimates and assumptions."
        ),

        llm=llm,

        verbose=False,

        allow_delegation=False,

        max_iter=3,

        max_rpm=10
    )

    # ======================================
    # 6. RECOVERY COORDINATOR
    # ======================================

    recovery_coordinator = Agent(

        role="Supply Chain Crisis Recovery Coordinator",

        goal=(
            "Combine the findings of all specialist agents "
            "into a comprehensive, realistic, prioritized "
            "and actionable supply chain recovery strategy."
        ),

        backstory=(
            "You are a senior supply chain crisis manager "
            "responsible for coordinating cross-functional "
            "recovery operations. "
            "You review disruption analysis, inventory "
            "findings, supplier evaluations, logistics "
            "recommendations, and operational risks. "
            "You develop short-term containment measures, "
            "medium-term recovery actions, and long-term "
            "prevention strategies. "
            "Your recommendations must be practical, "
            "evidence-based, and transparent about "
            "uncertainties."
        ),

        llm=llm,

        verbose=False,

        allow_delegation=False,

        max_iter=3,

        max_rpm=10
    )

    # ======================================
    # RETURN ALL AGENTS
    # ======================================

    agents = {

        "disruption_analyst": disruption_analyst,

        "inventory_analyst": inventory_analyst,

        "supplier_intelligence": supplier_intelligence,

        "logistics_optimizer": logistics_optimizer,

        "risk_analyst": risk_analyst,

        "recovery_coordinator": recovery_coordinator

    }

    logger.info(
        "Successfully initialized %s supply chain agents.",
        len(agents)
    )

    return agents

