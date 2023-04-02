def project_estimation(scope, requirements, timeline, resources, risks):
    # Calculate the total number of hours based on scope, requirements, and timeline
    total_hours = scope * requirements * timeline
    
    # Calculate the total cost based on the hourly rate and the number of hours
    hourly_rate = resources * 50  # assuming $50 per hour for each resource
    total_cost = total_hours * hourly_rate
    
    # Adjust the cost based on the risk factor (0 to 1)
    adjusted_cost = total_cost * (1 + risks)
    
    return {"hours": total_hours, "cost": adjusted_cost}

# Example usage:
estimation = project_estimation(scope=10, requirements=5, timeline=8, resources=3, risks=0.2)
print(estimation)  # output: {'hours': 400, 'cost': 78000.0}
