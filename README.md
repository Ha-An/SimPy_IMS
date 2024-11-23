# SimPy_IMS
SimPy-based Inventory Management Simulation

# About Simulator
* A simulator that implements a company that receives orders from customers, processes and assembles raw materials for one week, and creates products.
* There are four departments within the company: Sales, Production, Inventory, and Procurement.
  * The Sales department is responsible for receiving orders from customers and sending completed products to customers.
  * The Inventory department is a department that manages inventory. It supplies materials to the Production department, stores products, and delivers current raw material inventory information to the Procurement department.
  * The Procurement department is responsible for looking at the inventory information provided by the Inventory department and placing orders when the inventory falls below the set level.
  * The Production department takes materials from the Inventory department and produces WIP and products.
<!-- 
# How to run Simulator
* Python 3.11
* Needed Package
  * Numpy
  * Simpy
  * matplotlib -->

#  How to set parameters
Every parmeters in config_SimPy.py
* SIM_TIME: Set the period to simulate (days per episode)
* DEMAND_SCENARIO: Set distribution for customers to order
* LEADTIME_SCENARIO: Set the leadtime distribution
* USE_SQPOLICY: Must be set to True when running the simulator. When using SQpolicy (DRL is NOT used)
* SQPAIR: Set when and how many raw materials to order. (Ordering rules : Reorder point (S) and Order quantity (Q))

# Version
* Version 1.0

# Contact
* Yosep Oh (yosepoh@hanyang.ac.kr)

