
import json
import logging

from crewai import Task

logger = logging.getLogger("SupplyChainSentinel.Tasks")


def format_context(data, max_chars=12000):
    """
    Convert crisis details and supply-chain records into readable text
    that can be included in agent tasks.
    """
    if data is None:
        return "No additional data was provided."

    if hasattr(data, "to_dict"):
        try:
            data = data.to_dict(orient="records")
        except TypeError:
            data = data.to_dict()

    if isinstance(data, (dict, list, tuple)):
        formatted = json.dumps(data, indent=2, default=str)
    else:
        formatted = str(data)

    if len(formatted) > max_chars:
        formatted = formatted[:max_chars] + "\n[Additional data truncated to fit the analysis context.]"

    return formatted


def create_supply_chain_tasks(agents, crisis_data, supply_chain_data=None):
    """
    Create the six tasks assigned to the SupplyChain Sentinel agents.

    Args:
        agents: Dictionary returned by create_supply_chain_agents().
        crisis_data: Details entered by the user in the crisis form.
        supply_chain_data: Available supplier, shipment and inventory records.

    Returns:
        A dictionary containing all six CrewAI Task objects.
    """

    required_agents = [
        "disruption_analyst",
        "inventory_analyst",
        "supplier_intelligence",
        "logistics_optimizer",
        "risk_analyst",
        "recovery_coordinator",
    ]

    missing_agents = [name for name in required_agents if name not in agents]
    if missing_agents:
        raise ValueError(
            f"Missing agents required for task creation: {missing_agents}"
        )

    crisis_context = format_context(crisis_data)
    operational_context = format_context(supply_chain_data)

    # --------------------------------------------------
    # TASK 1: DISRUPTION INVESTIGATION
    # --------------------------------------------------

    disruption_task = Task(
        description=f"""
        Investigate the supply-chain crisis described below.

        CRISIS INFORMATION:
        {crisis_context}

        AVAILABLE SUPPLY-CHAIN DATA:
        {operational_context}

        Your responsibilities:
        1. Identify the main disruption and its likely root cause.
        2. Classify the crisis as low, medium, high or critical.
        3. Identify affected suppliers, shipments, products and operations
           using the information provided.
        4. Explain immediate consequences and possible downstream effects.
        5. Identify missing information that would be useful for a more
           accurate investigation.

        Important:
        - Use the supplied records as your evidence.
        - Do not invent shipment statuses, supplier events or facts.
        - Clearly label assumptions and uncertain conclusions.
        - Keep the investigation focused and practical.
        """,
        expected_output="""
        A structured disruption investigation containing:
        - Crisis summary
        - Likely root cause
        - Severity classification and reasoning
        - Affected operations
        - Immediate and downstream consequences
        - Missing information and assumptions
        """,
        agent=agents["disruption_analyst"],
    )

    # --------------------------------------------------
    # TASK 2: INVENTORY ANALYSIS
    # --------------------------------------------------

    inventory_task = Task(
        description=f"""
        Analyze inventory exposure caused by the reported crisis.

        CRISIS INFORMATION:
        {crisis_context}

        AVAILABLE SUPPLY-CHAIN DATA:
        {operational_context}

        DISRUPTION INVESTIGATION:
        Use the preceding Disruption Analyst task as context.

        Your responsibilities:
        1. Identify affected products and available stock where records exist.
        2. Identify possible shortages and stockout risks.
        3. Examine daily demand, reorder levels and safety stock if supplied.
        4. Prioritize inventory that supports critical operations.
        5. Recommend stock redistribution, allocation or replenishment actions.
        6. State which calculations are based on actual data and which are
           estimates.

        Do not invent stock quantities, demand figures or replenishment dates.
        If required information is unavailable, explain what is missing.
        """,
        expected_output="""
        An inventory impact report containing:
        - Available inventory evidence
        - Products at risk
        - Stockout concerns
        - Critical inventory priorities
        - Recommended inventory actions
        - Data gaps and assumptions
        """,
        agent=agents["inventory_analyst"],
        context=[disruption_task],
    )

    # --------------------------------------------------
    # TASK 3: SUPPLIER INTELLIGENCE
    # --------------------------------------------------

    supplier_task = Task(
        description=f"""
        Evaluate supplier exposure and sourcing options for this crisis.

        CRISIS INFORMATION:
        {crisis_context}

        AVAILABLE SUPPLY-CHAIN DATA:
        {operational_context}

        PREVIOUS INVESTIGATION:
        Consider the Disruption Analyst findings.

        Your responsibilities:
        1. Identify suppliers directly or indirectly affected.
        2. Evaluate reliability, lead times, location and capacity only when
           those details are available in the records.
        3. Identify existing alternative suppliers in the supplied dataset.
        4. Compare alternatives using available evidence.
        5. Recommend supplier diversification or temporary sourcing actions.
        6. Identify supplier information that must be verified before action.

        Do not create fictional suppliers or claim that an alternative has
        confirmed capacity unless the records explicitly establish it.
        """,
        expected_output="""
        A supplier intelligence report containing:
        - Affected suppliers
        - Supplier performance observations
        - Existing alternative suppliers
        - Evidence-based supplier comparison
        - Recommended sourcing actions
        - Information requiring verification
        """,
        agent=agents["supplier_intelligence"],
        context=[disruption_task],
    )

    # --------------------------------------------------
    # TASK 4: LOGISTICS OPTIMIZATION
    # --------------------------------------------------

    logistics_task = Task(
        description=f"""
        Investigate the logistics and shipment impact of the crisis.

        CRISIS INFORMATION:
        {crisis_context}

        AVAILABLE SUPPLY-CHAIN DATA:
        {operational_context}

        PREVIOUS INVESTIGATION:
        Consider the Disruption Analyst findings.

        Your responsibilities:
        1. Identify affected shipments and their recorded statuses.
        2. Analyze estimated delays and delivery risks using available data.
        3. Identify operational bottlenecks.
        4. Recommend practical logistics responses, such as prioritization,
           alternative transport modes or rerouting for investigation.
        5. Explain possible trade-offs between speed, cost and reliability.
        6. Identify information needed before a route or delivery change
           can be confirmed.

        Do not invent routes, carrier availability, transit times or costs.
        Recommendations must be clearly distinguished from confirmed facts.
        """,
        expected_output="""
        A logistics impact report containing:
        - Affected shipments
        - Recorded delivery risks
        - Potential bottlenecks
        - Proposed logistics responses
        - Operational trade-offs
        - Data gaps and required confirmations
        """,
        agent=agents["logistics_optimizer"],
        context=[disruption_task],
    )

    # --------------------------------------------------
    # TASK 5: OPERATIONAL RISK ANALYSIS
    # --------------------------------------------------

    risk_task = Task(
        description=f"""
        Assess the overall operational and business risks created by the crisis.

        CRISIS INFORMATION:
        {crisis_context}

        AVAILABLE SUPPLY-CHAIN DATA:
        {operational_context}

        Review the findings from:
        - Disruption Analyst
        - Inventory Analyst
        - Supplier Intelligence
        - Logistics Optimizer

        Your responsibilities:
        1. Assess operational continuity risks.
        2. Assess inventory, supplier, logistics and customer impact.
        3. Identify financial exposure only when sufficient figures are supplied.
        4. Prioritize risks by likelihood and impact.
        5. Recommend mitigation measures.
        6. Identify risks that need immediate management attention.

        Do not invent financial losses or probabilities. If exact calculations
        are not possible, provide qualitative assessments and explain why.
        """,
        expected_output="""
        An operational risk assessment containing:
        - Major identified risks
        - Likelihood and impact assessment
        - Business and customer implications
        - Financial exposure where calculable
        - Risk mitigation recommendations
        - Critical uncertainties
        """,
        agent=agents["risk_analyst"],
        context=[
            disruption_task,
            inventory_task,
            supplier_task,
            logistics_task,
        ],
    )

    # --------------------------------------------------
    # TASK 6: COORDINATED RECOVERY STRATEGY
    # --------------------------------------------------

    recovery_task = Task(
        description=f"""
        You are responsible for coordinating the final response to this
        supply-chain crisis.

        CRISIS INFORMATION:
        {crisis_context}

        AVAILABLE SUPPLY-CHAIN DATA:
        {operational_context}

        You must review and combine the findings from all five preceding tasks:
        1. Disruption Analyst
        2. Inventory Analyst
        3. Supplier Intelligence
        4. Logistics Optimizer
        5. Risk Analyst

        Create one practical, prioritized recovery strategy.

        Organize the strategy into:

        A. EXECUTIVE SUMMARY
        Explain what happened, what is affected and the overall response.

        B. IMMEDIATE CONTAINMENT
        List actions that should be considered within the next 0-24 hours.

        C. SHORT-TERM RECOVERY
        List actions for the next 1-7 days.

        D. MEDIUM-TERM RECOVERY
        List actions for the next 1-4 weeks.

        E. LONG-TERM PREVENTION
        Recommend measures to reduce the chance or impact of similar crises.

        F. PRIORITIZED ACTION PLAN
        For each action, include:
        - Priority: Critical, High, Medium or Low
        - Recommended action
        - Responsible department or role
        - Suggested timeframe
        - Expected operational benefit
        - Any dependency or confirmation required

        G. MANAGEMENT DECISIONS
        Identify decisions that require approval from management.

        H. DATA LIMITATIONS
        State important missing information and assumptions.

        IMPORTANT:
        - Resolve conflicting recommendations where possible.
        - Do not repeat all specialist reports without synthesizing them.
        - Do not present estimates as verified facts.
        - Do not claim that an action has already been executed.
        - Make recommendations realistic and actionable.
        """,
        expected_output="""
        A complete coordinated supply-chain recovery report with:
        - Executive summary
        - Immediate containment plan
        - Short-term and medium-term recovery
        - Long-term prevention measures
        - Prioritized action table
        - Management decisions
        - Data limitations and assumptions
        """,
        agent=agents["recovery_coordinator"],
        context=[
            disruption_task,
            inventory_task,
            supplier_task,
            logistics_task,
            risk_task,
        ],
    )

    logger.info("Created all six supply-chain investigation tasks.")

    return {
        "disruption_task": disruption_task,
        "inventory_task": inventory_task,
        "supplier_task": supplier_task,
        "logistics_task": logistics_task,
        "risk_task": risk_task,
        "recovery_task": recovery_task,
    }
