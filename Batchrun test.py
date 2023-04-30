# from mesa.batchrunner import BatchRunner
# from SarModel import SearchAndRescue
#
# fixed_parameters = {"width":, "height":,}
# parameters_list = [{“homophily”: 3, “density”: 0.8, “minority_pc”: 0.2},
#                     {“homophily”: 2, “density”: 0.9, “minority_pc”: 0.1},
#                     {“homophily”: 4, “density”: 0.6, “minority_pc”: 0.5}]
#
# num_iterations=100
# num_steps = 500
#
# batch_run = BatchRunner(SearchAndRescue,
#                          fixed_parameters=fixed_parameters,
#                          variable_parameters=parameters_list,
#                          iterations=num_iterations,
#                          max_steps=num_steps,
#                          model_reporters={"Total_infected":calculate_inf,
#                                           "Total_Imm":calculate_imm}
#                         )
