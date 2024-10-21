from config_SimPy import *
from log_SimPy import *
import environment as env
import pandas as pd
import Visualization

scenario = {"DEMAND": DEMAND_SCENARIO, "LEADTIME": LEADTIME_SCENARIO}
sq_pair = [[1, 1], [1, 2], [1, 3], [1, 4],
           [2, 1], [2, 2], [2, 3], [3, 1], [3, 2]]
# sq_pair = [[2, 3]]
# Create environment
simpy_env, inventoryList, procurementList, productionList, sales, customer, supplierList, daily_events = env.create_env(
    I, P, LOG_DAILY_EVENTS)
env.simpy_event_processes(simpy_env, inventoryList, procurementList,
                          productionList, sales, customer, supplierList, daily_events, I, scenario)
# total_reward = 0
outter_state = {
    'Total': [],
    'Holding': [],
    'Process': [],
    'Delivery': [],
    'Order': [],
    'Shortage': []
}
if PRINT_SIM_EVENTS:
    print(f"============= Initial Inventory Status =============")
    for inventory in inventoryList:
        print(
            f"Day 1 - {I[inventory.item_id]['NAME']} Inventory: {inventory.on_hand_inventory} units")
    print(f"============= SimPy Simulation Begins =============")
columns = []
for pair in sq_pair:
    SQPAIR['Reorder'] = pair[0]
    SQPAIR['Order'] = pair[1]
    state = [0, 0, 0, 0, 0, 0]
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
        # if PRINT_SIM_REPORT:
        #    for id in range(len(inventoryList)):
        #        print(DAILY_REPORTS[x][id])
        env.Cost.update_cost_log(inventoryList)
        for index in range(len(DAILY_COST.keys())):
            state[index +
                  1] += DAILY_COST[list(DAILY_COST.keys())[index]]
        print(state)
        print(DAILY_COST)
        env.Cost.clear_cost()
        print(f"Total Cost: {sum(LOG_COST)}")
        # reward = -daily_total_cost
        # total_reward += reward

    state[0] = sum(LOG_COST)
    outter_state['Total'].append(state[0])
    outter_state['Holding'].append(state[1])
    outter_state['Process'].append(state[2])
    outter_state['Delivery'].append(state[3])
    outter_state['Order'].append(state[4])
    outter_state['Shortage'].append(state[5])
export_Daily_Report = LOG_DAILY_REPORTS
daily_reports = pd.DataFrame(outter_state)
daily_reports.to_csv("./experiment_ss_inven.csv")
# print(total_reward)
