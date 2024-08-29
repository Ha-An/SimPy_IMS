from config_SimPy import *
from log_SimPy import *
import environment as env
import pandas as pd
import Visualization


scenario = {"DEMAND": DEMAND_SCENARIO, "LEADTIME": LEADTIME_SCENARIO}
# Create environment
simpy_env, inventoryList, procurementList, productionList, sales, customer, supplierList, daily_events = env.create_env(
    I, P, DAILY_EVENTS)
env.simpy_event_processes(simpy_env, inventoryList, procurementList,
                          productionList, sales, customer, supplierList, daily_events, I, scenario)
# total_reward = 0

state ={}
for id in I.keys():
    if I[id]["TYPE"] == 'Material':
        state[f"On_Hand_{I[id]['NAME']}"] = []
        if DAILY_CHANGE:
            state[f"Daily_Change_{I[id]['NAME']}"] = []
        if INTRANSIT:
            state[f"In_Transit_{I[id]['NAME']}"] = []
    else:
        state[f"On_Hand_{I[id]['NAME']}"] = []
        if DAILY_CHANGE:
            state[f"Daily_Change_{I[id]['NAME']}"] = []
state["Remain Demand"] = []

print(state)
if PRINT_SIM:
    print(f"============= Initial Inventory Status =============")
    for inventory in inventoryList:
        print(
            f"Day 1 - {I[inventory.item_id]['NAME']} Inventory: {inventory.on_hand_inventory} units")

    print(f"============= SimPy Simulation Begins =============")

for x in range(SIM_TIME):
    daily_events.append(f"\nDay {(simpy_env.now) // 24+1} Report:")
    simpy_env.run(until = simpy_env.now+24)
    # daily_total_cost = env.cal_daily_cost(inventoryList, procurementList, productionList, sales)
    if PRINT_SIM:
        # Print the simulation log every 24 hours (1 day)
        for log in daily_events:
            print(log)
        # print("[Daily Total Cost] ", daily_total_cost)
    daily_events.clear()

    env.update_daily_report(inventoryList)
    #if PRINT_SIM_REPORT:
    #    for id in range(len(inventoryList)):
    #        print(DAILY_REPORTS[x][id])

    env.Cost.update_cost_log(inventoryList)
    
    for key in DAILY_COST_REPORT.keys():
        print(f"{key}: {DAILY_COST_REPORT[key]}")
    print(f"Total cost: {sum(COST_LOG)}")
    env.Cost.clear_cost()
    # reward = -daily_total_cost
    # total_reward += reward

    for id in range(len(I)):
        state[f"On_Hand_{I[id]['NAME']}"].append(STATE_DICT[-1][f"On_Hand_{I[id]['NAME']}"])
        if DAILY_CHANGE == 1:
            state[f"Daily_Change_{I[id]['NAME']}"].append(STATE_DICT[-1][f"Daily_Change_{I[id]['NAME']}"])
        if INTRANSIT == 1:
            if I[id]["TYPE"] == "Material":
                state[f"In_Transit_{I[id]['NAME']}"].append(STATE_DICT[-1][f"In_Transit_{I[id]['NAME']}"])

    state['Remain Demand'].append(I[0]["DEMAND_QUANTITY"] -
                     inventoryList[0].on_hand_inventory)

export_Daily_Report = DAILY_REPORTS
if VISUALIAZTION != False:
    Visualization.visualization(export_Daily_Report)

daily_reports = pd.DataFrame(state) 
daily_reports.to_csv("./Daily_Report.csv")

# print(total_reward)
