# Given loss data
loss_data = [
    (1, 34.8795), (2, 26.9273), (3, 23.9175), (4, 22.4508), (5, 22.0275),
    (6, 23.3022), (7, 22.6471), (8, 22.2269), (9, 21.1064), (10, 20.8091),
    (11, 21.6410), (12, 21.8925), (13, 20.6888), (14, 20.6657), (15, 21.7803),
    (16, 21.0166), (17, 20.5337), (18, 19.8767), (19, 19.7465), (20, 20.6998),
    (21, 20.2770), (22, 20.0248), (23, 20.5253), (24, 20.4358), (25, 19.9818),
    (26, 19.8725), (27, 19.8338), (28, 19.8738), (29, 19.5667), (30, 19.8371),
    (31, 19.4354), (32, 20.0951), (33, 19.7295), (34, 19.1670), (35, 19.8447),
    (36, 18.6824), (37, 18.9576), (38, 18.5114), (39, 18.1657), (40, 18.4460),
    (41, 19.2566), (42, 18.8092), (43, 18.4683), (44, 18.5863), (45, 18.1664),
    (46, 18.3893), (47, 18.5779), (48, 18.4458), (49, 18.2474), (50, 18.4468)
]

# Calculate average loss decrease per epoch
total_loss_decrease = loss_data[0][1] - loss_data[-1][1]
average_loss_decrease_per_epoch = total_loss_decrease / len(loss_data)

# Initial loss (last loss from the provided data)
initial_loss = loss_data[-1][1]

# Projected losses for the next 50 epochs
projected_losses = []
current_loss = initial_loss
for _ in range(50):
    current_loss -= average_loss_decrease_per_epoch
    projected_losses.append(current_loss)

print(projected_losses)
