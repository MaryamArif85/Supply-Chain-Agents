import logging

from crewai import Crew, Process

from agents.supply_chain_agents import create_supply_chain_agents
from tasks.supply_chain_tasks import create_supply_chain_tasks

logger = logging.getLogger("SupplyChainSentinel.Crew")


def create_supply_chain_crew(crisis_data, supply_chain_data=None):

    agents = create_supply_chain_agents()

    tasks = create_supply_chain_tasks(
        agents=agents,
        crisis_data=crisis_data,
        supply_chain_data=supply_chain_data,
    )

    crew = Crew(
        agents=[
            agents["disruption_analyst"],
            agents["inventory_analyst"],
            agents["supplier_intelligence"],
            agents["logistics_optimizer"],
            agents["risk_analyst"],
            agents["recovery_coordinator"],
        ],
        tasks=[
            tasks["disruption_task"],
            tasks["inventory_task"],
            tasks["supplier_task"],
            tasks["logistics_task"],
            tasks["risk_task"],
            tasks["recovery_task"],
        ],
        process=Process.sequential,
        verbose=False,
        memory=False,
    )

    return crew


def run_crisis_investigation(crisis_data, supply_chain_data=None):

    logger.info("Starting crisis investigation.")

    crew = create_supply_chain_crew(
        crisis_data=crisis_data,
        supply_chain_data=supply_chain_data,
    )

    # kickoff() returns a CrewOutput object.
    # Streamlit will use this returned object to display the report.
    result = crew.kickoff()

    logger.info("Crisis investigation completed.")

    return result

