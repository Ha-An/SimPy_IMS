from config_SimPy import *
from log_SimPy import *
import environment as env
import pandas as pd
import Visualization

# Define the scenario
scenario = {"DEMAND": DEMAND_SCENARIO, "LEADTIME": LEADTIME_SCENARIO}

# Create environment
simpy_env, inventoryList, procurementList, productionList, sales, customer, supplierList, daily_events = env.create_env(
    I, P, LOG_DAILY_EVENTS)
env.simpy_event_processes(simpy_env, inventoryList, procurementList,
                          productionList, sales, customer, supplierList, daily_events, I, scenario)


if PRINT_SIM_EVENTS:
    print(f"============= Initial Inventory Status =============")
    for inventory in inventoryList:
        print(
            f"Day 1 - {I[inventory.item_id]['NAME']} Inventory: {inventory.on_hand_inventory} units")

    print(f"============= SimPy Simulation Begins =============")

for x in range(SIM_TIME):
    daily_events.append(f"\nDay {(simpy_env.now) // 24+1} Report:")
    simpy_env.run(until=simpy_env.now+24)
    # daily_total_cost = env.cal_daily_cost(inventoryList, procurementList, productionList, sales)
    if PRINT_SIM_EVENTS:
        # Print the simulation log every 24 hours (1 day)
        for log in daily_events:
            print(log)
        # print("[Daily Total Cost] ", daily_total_cost)
    daily_events.clear()

    env.update_daily_report(inventoryList)
    if PRINT_SIM_REPORT:
        for id in range(len(inventoryList)):
            print(LOG_DAILY_REPORTS[x][id])

    env.Cost.update_cost_log(inventoryList)
    if PRINT_DAILY_COST:
        for key in DAILY_COST.keys():
            print(f"{key}: {DAILY_COST[key]}")
        print(f"Daily Total Cost: {LOG_COST[-1]}")
    print(f"Cumulative Total Cost: {sum(LOG_COST)}")
    env.Cost.clear_cost()
    # reward = -daily_total_cost
    # total_reward += reward
