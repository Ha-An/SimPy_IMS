from config import *
import environment as env
import pandas as pd
import Visualization
# Create environment
simpy_env, inventoryList, procurementList, productionList, sales, customer, supplierList, daily_events,daily_reports = env.create_env(
    I, P, DAILY_EVENTS,DAILY_REPORTS)
env.simpy_event_processes(simpy_env, inventoryList, procurementList,
                          productionList, sales, customer, supplierList, daily_events,daily_reports, I)
# total_reward = 0

if PRINT_SIM_EVENTS:
    print(f"============= Initial Inventory Status =============")
    ############## PLEASE CODE HERE ##########

    print(f"============= SimPy Simulation Begins =============")

for x in range(SIM_TIME):
    daily_events.append(f"\nDay {(simpy_env.now) // 24} Report:")
    simpy_env.run(until=simpy_env.now+24)
    # daily_total_cost = env.cal_daily_cost(inventoryList, procurementList, productionList, sales)
    if PRINT_SIM_EVENTS:
        # Print the simulation log every 24 hours (1 day)
        for log in daily_events:
            print(log)
        # print("[Daily Total Cost] ", daily_total_cost)
    daily_events.clear()
    env.record_report(inventoryList)
    if PRINT_SIM_REPORT:
        for id in range(len(inventoryList)):
            print(DAILY_REPORTS[x][id])
    # reward = -daily_total_cost
    # total_reward += reward

export_Daily_Report=[]
for x in range(len(inventoryList)):
    for report in DAILY_REPORTS:
        export_Daily_Report.append(report[x])

Visualization.visualization(export_Daily_Report)
daily_reports=pd.DataFrame(export_Daily_Report)
daily_reports.columns=["Day","Name","Type","Start","Income","Outcome","End"]
daily_reports.to_csv("./Daily_Report.csv")

# print(total_reward)
