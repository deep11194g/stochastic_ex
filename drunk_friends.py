import numpy as np
from matplotlib import pyplot as plt

DIR_DIFF_STEP = {
    'N': [0, 1],
    'S': [0, -1],
    'E': [-1, 0],
    'W': [1, 0],
}


def trajectory_single(max_time):
    x0 = y0 = 0
    trajectory = [[x0], [y0]]
    prev_step = [x0, y0]
    for _ in range(max_time):
        random_dir = np.random.choice(['N', 'S', 'E', 'W'], size=1)[0]
        trajectory[0].append(prev_step[0] + (DIR_DIFF_STEP[random_dir])[0])
        trajectory[1].append(prev_step[1] + (DIR_DIFF_STEP[random_dir])[1])
    return trajectory


def trajectory_couple(max_time):
    trajectory = np.array([[0, 0]])
    time = np.linspace(0, max_time, max_time + 1)
    prev_step = trajectory[0]
    for _ in range(max_time):
        random_dir1 = np.random.choice(['N', 'S', 'E', 'W'], size=1)[0]
        random_dir2 = np.random.choice(['N', 'S', 'E', 'W'], size=1)[0]
        if random_dir1 is not random_dir2:
            curr_step = prev_step
        else:
            curr_step = prev_step + np.array(DIR_DIFF_STEP[random_dir1])
        np.append(trajectory, curr_step)
        prev_step = curr_step
    return trajectory


if __name__ == '__main__':
    traj_single = trajectory_single(6)
    # traj_couple = trajectory_single(6)
    print(traj_single)
    plt.plot(traj_single[0], traj_single[1], 'r.')
    plt.show()
    # plt.plot(traj_couple[0], traj_couple[1], 'b.')
